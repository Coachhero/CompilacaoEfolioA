# Generated from MOCP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MOCPParser import MOCPParser
else:
    from MOCPParser import MOCPParser

# This class defines a complete generic visitor for a parse tree produced by MOCPParser.

class MOCPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MOCPParser#programa.
    def visitPrograma(self, ctx:MOCPParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#prototipo.
    def visitPrototipo(self, ctx:MOCPParser.PrototipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#funcao.
    def visitFuncao(self, ctx:MOCPParser.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#nomeFuncao.
    def visitNomeFuncao(self, ctx:MOCPParser.NomeFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#listaParametros.
    def visitListaParametros(self, ctx:MOCPParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#parametro.
    def visitParametro(self, ctx:MOCPParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#tipo.
    def visitTipo(self, ctx:MOCPParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#declaracao.
    def visitDeclaracao(self, ctx:MOCPParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#listaVariaveis.
    def visitListaVariaveis(self, ctx:MOCPParser.ListaVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#variavel.
    def visitVariavel(self, ctx:MOCPParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#blocoArray.
    def visitBlocoArray(self, ctx:MOCPParser.BlocoArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#listaValores.
    def visitListaValores(self, ctx:MOCPParser.ListaValoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#bloco.
    def visitBloco(self, ctx:MOCPParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucoes.
    def visitInstrucoes(self, ctx:MOCPParser.InstrucoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#atribuicao.
    def visitAtribuicao(self, ctx:MOCPParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucaoSe.
    def visitInstrucaoSe(self, ctx:MOCPParser.InstrucaoSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucaoEnquanto.
    def visitInstrucaoEnquanto(self, ctx:MOCPParser.InstrucaoEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucaoPara.
    def visitInstrucaoPara(self, ctx:MOCPParser.InstrucaoParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#expressaoOuAtribuicao.
    def visitExpressaoOuAtribuicao(self, ctx:MOCPParser.ExpressaoOuAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucaoRetorno.
    def visitInstrucaoRetorno(self, ctx:MOCPParser.InstrucaoRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#instrucaoEscrita.
    def visitInstrucaoEscrita(self, ctx:MOCPParser.InstrucaoEscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#argumento_texto.
    def visitArgumento_texto(self, ctx:MOCPParser.Argumento_textoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:MOCPParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#chamadaLeitura.
    def visitChamadaLeitura(self, ctx:MOCPParser.ChamadaLeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#argumentos.
    def visitArgumentos(self, ctx:MOCPParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#ExpressaoBase.
    def visitExpressaoBase(self, ctx:MOCPParser.ExpressaoBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#OuLogico.
    def visitOuLogico(self, ctx:MOCPParser.OuLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#ComparacaoBase.
    def visitComparacaoBase(self, ctx:MOCPParser.ComparacaoBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#ELogico.
    def visitELogico(self, ctx:MOCPParser.ELogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Comparacao.
    def visitComparacao(self, ctx:MOCPParser.ComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#AditivaBase.
    def visitAditivaBase(self, ctx:MOCPParser.AditivaBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#MultiplicativaBase.
    def visitMultiplicativaBase(self, ctx:MOCPParser.MultiplicativaBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Adicao.
    def visitAdicao(self, ctx:MOCPParser.AdicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Subtracao.
    def visitSubtracao(self, ctx:MOCPParser.SubtracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Multiplicacao.
    def visitMultiplicacao(self, ctx:MOCPParser.MultiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#UnariaBase.
    def visitUnariaBase(self, ctx:MOCPParser.UnariaBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Modulo.
    def visitModulo(self, ctx:MOCPParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Divisao.
    def visitDivisao(self, ctx:MOCPParser.DivisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Negacao.
    def visitNegacao(self, ctx:MOCPParser.NegacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#CastReal.
    def visitCastReal(self, ctx:MOCPParser.CastRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#CastInteiro.
    def visitCastInteiro(self, ctx:MOCPParser.CastInteiroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#PrimariaBase.
    def visitPrimariaBase(self, ctx:MOCPParser.PrimariaBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#AcessoVetor.
    def visitAcessoVetor(self, ctx:MOCPParser.AcessoVetorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#ChamadaGenerica.
    def visitChamadaGenerica(self, ctx:MOCPParser.ChamadaGenericaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#VariavelID.
    def visitVariavelID(self, ctx:MOCPParser.VariavelIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Numero.
    def visitNumero(self, ctx:MOCPParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#NumeroReal.
    def visitNumeroReal(self, ctx:MOCPParser.NumeroRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#Parenteses.
    def visitParenteses(self, ctx:MOCPParser.ParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MOCPParser#opRel.
    def visitOpRel(self, ctx:MOCPParser.OpRelContext):
        return self.visitChildren(ctx)



del MOCPParser