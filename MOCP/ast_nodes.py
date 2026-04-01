class ASTNode:
    def children(self):
        return []

    def label(self):
        return type(self).__name__

    def __str__(self):
        return self.label()


class Programa(ASTNode):
    def __init__(self, elementos):
        self.elementos = elementos

    def label(self):
        return "Programa"

    def children(self):
        return self.elementos


class Prototipo(ASTNode):
    def __init__(self, tipo, nome, parametros):
        self.tipo = tipo
        self.nome = nome
        self.parametros = parametros

    def label(self):
        return f"Prototipo: {self.nome}"

    def children(self):
        return [self.tipo] + self.parametros


class Funcao(ASTNode):
    def __init__(self, tipo, nome, parametros, bloco):
        self.tipo = tipo
        self.nome = nome
        self.parametros = parametros
        self.bloco = bloco

    def label(self):
        return f"Funcao: {self.nome}"

    def children(self):
        return [self.tipo] + self.parametros + [self.bloco]


class Parametro(ASTNode):
    def __init__(self, tipo, nome=None, vetor=False):
        self.tipo = tipo
        self.nome = nome
        self.vetor = vetor

    def label(self):
        sufixo = "[]" if self.vetor else ""
        nome = self.nome if self.nome is not None else "(sem nome)"
        return f"Parametro: {nome}{sufixo}"

    def children(self):
        return [self.tipo]


class Tipo(ASTNode):
    def __init__(self, nome):
        self.nome = nome

    def label(self):
        return f"Tipo: {self.nome}"


class Bloco(ASTNode):
    def __init__(self, instrucoes):
        self.instrucoes = instrucoes

    def label(self):
        return "Bloco"

    def children(self):
        return self.instrucoes


class Declaracao(ASTNode):
    def __init__(self, tipo, variaveis):
        self.tipo = tipo
        self.variaveis = variaveis

    def label(self):
        return "Declaracao"

    def children(self):
        return [self.tipo] + self.variaveis


class Variavel(ASTNode):
    def __init__(self, nome, tamanho=None, inicializacao=None):
        self.nome = nome
        self.tamanho = tamanho
        self.inicializacao = inicializacao

    def label(self):
        if self.tamanho is not None:
            return f"Variavel: {self.nome}[{self.tamanho}]"
        return f"Variavel: {self.nome}"

    def children(self):
        return [self.inicializacao] if self.inicializacao is not None else []


class Atribuicao(ASTNode):
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor

    def label(self):
        return "Atribuicao"

    def children(self):
        return [self.destino, self.valor]


class AcessoVetor(ASTNode):
    def __init__(self, nome, indice):
        self.nome = nome
        self.indice = indice

    def label(self):
        return f"AcessoVetor: {self.nome}"

    def children(self):
        return [self.indice]


class InstrucaoSe(ASTNode):
    def __init__(self, condicao, bloco_then, bloco_else=None):
        self.condicao = condicao
        self.bloco_then = bloco_then
        self.bloco_else = bloco_else

    def label(self):
        return "Se"

    def children(self):
        filhos = [self.condicao, self.bloco_then]
        if self.bloco_else is not None:
            filhos.append(self.bloco_else)
        return filhos


class InstrucaoEnquanto(ASTNode):
    def __init__(self, condicao, bloco):
        self.condicao = condicao
        self.bloco = bloco

    def label(self):
        return "Enquanto"

    def children(self):
        return [self.condicao, self.bloco]


class InstrucaoPara(ASTNode):
    def __init__(self, init, condicao, passo, bloco):
        self.init = init
        self.condicao = condicao
        self.passo = passo
        self.bloco = bloco

    def label(self):
        return "Para"

    def children(self):
        filhos = []
        if self.init is not None:
            filhos.append(self.init)
        if self.condicao is not None:
            filhos.append(self.condicao)
        if self.passo is not None:
            filhos.append(self.passo)
        filhos.append(self.bloco)
        return filhos


class Retorno(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def label(self):
        return "Retorno"

    def children(self):
        return [self.valor]


class ChamadaFuncao(ASTNode):
    def __init__(self, nome, argumentos):
        self.nome = nome
        self.argumentos = argumentos

    def label(self):
        return f"ChamadaFuncao: {self.nome}"

    def children(self):
        return self.argumentos


class Leitura(ASTNode):
    def __init__(self, tipo):
        self.tipo = tipo

    def label(self):
        return f"Leitura: {self.tipo}"


class Escrita(ASTNode):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def label(self):
        return f"Escrita: {self.tipo}"

    def children(self):
        return [self.valor]


class OperacaoBinaria(ASTNode):
    def __init__(self, operador, esquerda, direita):
        self.operador = operador
        self.esquerda = esquerda
        self.direita = direita

    def label(self):
        return f"Operacao: {self.operador}"

    def children(self):
        return [self.esquerda, self.direita]


class Negacao(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def label(self):
        return "Negacao"

    def children(self):
        return [self.valor]


class Cast(ASTNode):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def label(self):
        return f"Cast: {self.tipo}"

    def children(self):
        return [self.valor]


class Identificador(ASTNode):
    def __init__(self, nome):
        self.nome = nome

    def label(self):
        return f"Identificador: {self.nome}"


class Numero(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def label(self):
        return f"Numero: {self.valor}"


class NumeroReal(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def label(self):
        return f"NumeroReal: {self.valor}"


class Texto(ASTNode):
    def __init__(self, valor):
        self.valor = valor

    def label(self):
        return f'Texto: "{self.valor}"'