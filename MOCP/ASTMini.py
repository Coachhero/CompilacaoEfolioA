from MOCP.ast_nodes import *


class MiniNode:
    def __init__(self, label, children=None):
        self.label = str(label)
        self.children = children if children else []

    def print_tree(self, prefix="", is_last=True):
        connector = "└── " if is_last else "├── "
        print(prefix + connector + self.label)

        new_prefix = prefix + ("    " if is_last else "│   ")

        filhos_validos = [c for c in self.children if c is not None]
        for i, child in enumerate(filhos_validos):
            child.print_tree(new_prefix, i == len(filhos_validos) - 1)

    def to_string(self, indent=0):
        prefix = "    " * indent
        s = prefix + self.label + "\n"
        for c in self.children:
            if c is not None:
                s += c.to_string(indent + 1)
        return s

    def __str__(self):
        return self.to_string()


class ASTMiniBuilder:
    def build(self, node):
        if node is None:
            return None

        # =========================
        # RAIZ / NÓS ESTRUTURAIS
        # =========================
        if isinstance(node, Programa):
            filhos = []
            for elem in node.elementos:
                r = self.build(elem)
                if r is not None:
                    if isinstance(r, list):
                        filhos.extend(r)
                    else:
                        filhos.append(r)
            return filhos

        if isinstance(node, Funcao):
            return self.build(node.bloco)

        if isinstance(node, Prototipo):
            return None

        if isinstance(node, Parametro):
            return None

        if isinstance(node, Tipo):
            return None

        if isinstance(node, Declaracao):
            return None

        if isinstance(node, Variavel):
            return None

        # =========================
        # BLOCO
        # =========================
        if isinstance(node, Bloco):
            filhos = []
            for instr in node.instrucoes:
                r = self.build(instr)
                if r is not None:
                    if isinstance(r, list):
                        filhos.extend(r)
                    else:
                        filhos.append(r)
            return filhos

        # =========================
        # ATRIBUIÇÃO
        # =========================
        if isinstance(node, Atribuicao):
            return MiniNode("=", [
                self.build(node.destino),
                self.build(node.valor)
            ])

        if isinstance(node, AcessoVetor):
            return MiniNode(f"{node.nome}[]", [
                self.build(node.indice)
            ])

        # =========================
        # CONTROLO
        # =========================
        if isinstance(node, InstrucaoSe):
            filhos = [self.build(node.condicao)]

            then_part = self.build(node.bloco_then)
            if then_part is not None:
                if isinstance(then_part, list):
                    filhos.extend(then_part)
                else:
                    filhos.append(then_part)

            if node.bloco_else is not None:
                else_part = self.build(node.bloco_else)
                if else_part is not None:
                    if isinstance(else_part, list):
                        filhos.extend(else_part)
                    else:
                        filhos.append(else_part)

            return MiniNode("se", filhos)

        if isinstance(node, InstrucaoEnquanto):
            corpo = self.build(node.bloco)

            filhos = [self.build(node.condicao)]
            if corpo is not None:
                if isinstance(corpo, list):
                    filhos.extend(corpo)
                else:
                    filhos.append(corpo)

            return MiniNode("enquanto", filhos)

        if isinstance(node, InstrucaoPara):
            filhos = []

            if node.init is not None:
                filhos.append(self.build(node.init))
            if node.condicao is not None:
                filhos.append(self.build(node.condicao))
            if node.passo is not None:
                filhos.append(self.build(node.passo))

            corpo = self.build(node.bloco)
            if corpo is not None:
                if isinstance(corpo, list):
                    filhos.extend(corpo)
                else:
                    filhos.append(corpo)

            return MiniNode("para", filhos)

        if isinstance(node, Retorno):
            return MiniNode("retorna", [
                self.build(node.valor)
            ])

        # =========================
        # CHAMADAS / I-O
        # =========================
        if isinstance(node, ChamadaFuncao):
            filhos = []
            for arg in node.argumentos:
                r = self.build(arg)
                if r is not None:
                    filhos.append(r)
            return MiniNode(node.nome, filhos)

        if isinstance(node, Leitura):
            return MiniNode(node.tipo)

        if isinstance(node, Escrita):
            return MiniNode(node.tipo, [
                self.build(node.valor)
            ])

        # =========================
        # EXPRESSÕES
        # =========================
        if isinstance(node, OperacaoBinaria):
            return MiniNode(node.operador, [
                self.build(node.esquerda),
                self.build(node.direita)
            ])

        if isinstance(node, Negacao):
            return MiniNode("!", [
                self.build(node.valor)
            ])

        if isinstance(node, Cast):
            return MiniNode(f"cast_{node.tipo}", [
                self.build(node.valor)
            ])

        # =========================
        # VALORES
        # =========================
        if isinstance(node, Identificador):
            return MiniNode(node.nome)

        if isinstance(node, Numero):
            return MiniNode(node.valor)

        if isinstance(node, NumeroReal):
            return MiniNode(node.valor)

        if isinstance(node, Texto):
            return MiniNode(f'"{node.valor}"')

        # =========================
        # FALLBACK FINAL
        # =========================
        return None