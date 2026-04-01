from MOCP.MOCPVisitor import MOCPVisitor
from MOCP.ast_nodes import *


class ASTBuilder(MOCPVisitor):
    def _tirar_aspas(self, texto):
        if texto is None:
            return ""
        if len(texto) >= 2 and texto[0] == '"' and texto[-1] == '"':
            return texto[1:-1]
        return texto

    # =========================
    # Estrutura geral
    # =========================

    def visitPrograma(self, ctx):
        elementos = []

        for child in ctx.getChildren():
            nome = type(child).__name__
            if nome.endswith("Context"):
                resultado = self.visit(child)
                if resultado is not None:
                    elementos.append(resultado)

        return Programa(elementos)

    def visitPrototipo(self, ctx):
        tipo = self.visit(ctx.tipo())
        nome = ctx.nomeFuncao().getText()

        parametros = []
        if ctx.listaParametros():
            parametros = self.visit(ctx.listaParametros())

        return Prototipo(tipo, nome, parametros)

    def visitFuncao(self, ctx):
        tipo = self.visit(ctx.tipo())
        nome = ctx.nomeFuncao().getText()

        parametros = []
        if ctx.listaParametros():
            parametros = self.visit(ctx.listaParametros())

        bloco = self.visit(ctx.bloco())

        return Funcao(tipo, nome, parametros, bloco)

    def visitListaParametros(self, ctx):
        if ctx.getText() == "vazio":
            return []

        return [self.visit(param) for param in ctx.parametro()]

    def visitParametro(self, ctx):
        tipo = self.visit(ctx.tipo())
        nome = ctx.IDENTIFICADOR().getText() if ctx.IDENTIFICADOR() else None
        vetor = ctx.LBRACK() is not None

        return Parametro(tipo, nome, vetor)

    def visitTipo(self, ctx):
        return Tipo(ctx.getText())

    # =========================
    # Blocos e instruções
    # =========================

    def visitBloco(self, ctx):
        instrucoes = [self.visit(instr) for instr in ctx.instrucoes()]
        return Bloco(instrucoes)

    def visitInstrucoes(self, ctx):
        for child in ctx.getChildren():
            nome = type(child).__name__
            if nome.endswith("Context"):
                return self.visit(child)
        return None

    def visitDeclaracao(self, ctx):
        tipo = self.visit(ctx.tipo())
        variaveis = [self.visit(v) for v in ctx.listaVariaveis().variavel()]
        return Declaracao(tipo, variaveis)

    def visitVariavel(self, ctx):
        nome = ctx.IDENTIFICADOR().getText()

        # variavel simples
        if ctx.getChildCount() == 1:
            return Variavel(nome)

        # vetor com tamanho fixo: x[10]
        if ctx.INT_LITERAL():
            return Variavel(nome, tamanho=ctx.INT_LITERAL().getText())

        # inicialização com expressão: x = 10
        if ctx.expressao():
            return Variavel(nome, inicializacao=self.visit(ctx.expressao()))

        # inicialização com leitura: x[] = lers()
        if ctx.chamadaLeitura():
            return Variavel(nome, inicializacao=self.visit(ctx.chamadaLeitura()))

        # inicialização com bloco array: x[] = {1,2,3}
        if ctx.blocoArray():
            return Variavel(nome, inicializacao=self.visit(ctx.blocoArray()))

        return Variavel(nome)

    def visitBlocoArray(self, ctx):
        # versão simples para já
        return Texto(ctx.getText())

    def visitListaValores(self, ctx):
        return [self.visit(expr) for expr in ctx.expressao()]

    def visitAtribuicao(self, ctx):
        if len(ctx.expressao()) == 2:
            destino = AcessoVetor(
                ctx.IDENTIFICADOR().getText(),
                self.visit(ctx.expressao(0))
            )
            valor = self.visit(ctx.expressao(1))
        else:
            destino = Identificador(ctx.IDENTIFICADOR().getText())
            valor = self.visit(ctx.expressao(0))

        return Atribuicao(destino, valor)

    def visitInstrucaoSe(self, ctx):
        condicao = self.visit(ctx.expressao())
        bloco_then = self.visit(ctx.bloco(0))
        bloco_else = self.visit(ctx.bloco(1)) if len(ctx.bloco()) > 1 else None

        return InstrucaoSe(condicao, bloco_then, bloco_else)

    def visitInstrucaoEnquanto(self, ctx):
        condicao = self.visit(ctx.expressao())
        bloco = self.visit(ctx.bloco())
        return InstrucaoEnquanto(condicao, bloco)

    def visitInstrucaoPara(self, ctx):
        init = self.visit(ctx.expressaoOuAtribuicao(0)) if len(ctx.expressaoOuAtribuicao()) > 0 else None
        condicao = self.visit(ctx.expressao()) if ctx.expressao() else None
        passo = self.visit(ctx.expressaoOuAtribuicao(1)) if len(ctx.expressaoOuAtribuicao()) > 1 else None
        bloco = self.visit(ctx.bloco())

        return InstrucaoPara(init, condicao, passo, bloco)

    def visitExpressaoOuAtribuicao(self, ctx):
        for child in ctx.getChildren():
            nome = type(child).__name__
            if nome.endswith("Context"):
                return self.visit(child)
        return None

    def visitInstrucaoRetorno(self, ctx):
        return Retorno(self.visit(ctx.expressao()))

    def visitInstrucaoEscrita(self, ctx):
        tipo_escrita = ctx.getChild(0).getText()

        if tipo_escrita == "escreverv":
            valor = Identificador(ctx.IDENTIFICADOR().getText())
        else:
            valor = self.visit(ctx.getChild(2))

        return Escrita(tipo_escrita, valor)

    def visitArgumento_texto(self, ctx):
        if ctx.IDENTIFICADOR():
            return Identificador(ctx.IDENTIFICADOR().getText())
        return Texto(self._tirar_aspas(ctx.getText()))

    def visitChamadaFuncao(self, ctx):
        if ctx.chamadaLeitura():
            return self.visit(ctx.chamadaLeitura())

        nome = ctx.IDENTIFICADOR().getText()
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []

        return ChamadaFuncao(nome, argumentos)

    def visitChamadaLeitura(self, ctx):
        return Leitura(ctx.getChild(0).getText())

    def visitArgumentos(self, ctx):
        return [self.visit(expr) for expr in ctx.expressao()]

    # =========================
    # Expressões
    # =========================

    def visitExpressaoBase(self, ctx):
        return self.visit(ctx.expressao_logica_e())

    def visitOuLogico(self, ctx):
        return OperacaoBinaria(
            "||",
            self.visit(ctx.expressao()),
            self.visit(ctx.expressao_logica_e())
        )

    def visitComparacaoBase(self, ctx):
        return self.visit(ctx.expressao_comparacao())

    def visitELogico(self, ctx):
        return OperacaoBinaria(
            "&&",
            self.visit(ctx.expressao_logica_e()),
            self.visit(ctx.expressao_comparacao())
        )

    def visitAditivaBase(self, ctx):
        return self.visit(ctx.expressao_aditiva())

    def visitComparacao(self, ctx):
        return OperacaoBinaria(
            ctx.opRel().getText(),
            self.visit(ctx.expressao_comparacao()),
            self.visit(ctx.expressao_aditiva())
        )

    def visitMultiplicativaBase(self, ctx):
        return self.visit(ctx.expressao_multiplicativa())

    def visitAdicao(self, ctx):
        return OperacaoBinaria(
            "+",
            self.visit(ctx.expressao_aditiva()),
            self.visit(ctx.expressao_multiplicativa())
        )

    def visitSubtracao(self, ctx):
        return OperacaoBinaria(
            "-",
            self.visit(ctx.expressao_aditiva()),
            self.visit(ctx.expressao_multiplicativa())
        )

    def visitUnariaBase(self, ctx):
        return self.visit(ctx.expressao_unaria())

    def visitMultiplicacao(self, ctx):
        return OperacaoBinaria(
            "*",
            self.visit(ctx.expressao_multiplicativa()),
            self.visit(ctx.expressao_unaria())
        )

    def visitDivisao(self, ctx):
        return OperacaoBinaria(
            "/",
            self.visit(ctx.expressao_multiplicativa()),
            self.visit(ctx.expressao_unaria())
        )

    def visitModulo(self, ctx):
        return OperacaoBinaria(
            "%",
            self.visit(ctx.expressao_multiplicativa()),
            self.visit(ctx.expressao_unaria())
        )

    def visitNegacao(self, ctx):
        return Negacao(self.visit(ctx.expressao_unaria()))

    def visitCastReal(self, ctx):
        return Cast("real", self.visit(ctx.expressao_unaria()))

    def visitCastInteiro(self, ctx):
        return Cast("inteiro", self.visit(ctx.expressao_unaria()))

    def visitPrimariaBase(self, ctx):
        return self.visit(ctx.expressao_primaria())

    def visitAcessoVetor(self, ctx):
        return AcessoVetor(
            ctx.IDENTIFICADOR().getText(),
            self.visit(ctx.expressao())
        )

    def visitChamadaGenerica(self, ctx):
        return self.visit(ctx.chamadaFuncao())

    def visitVariavelID(self, ctx):
        return Identificador(ctx.getText())

    def visitNumero(self, ctx):
        return Numero(ctx.getText())

    def visitNumeroReal(self, ctx):
        return NumeroReal(ctx.getText())

    def visitParenteses(self, ctx):
        return self.visit(ctx.expressao())