# Generated from MOCP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MOCPParser import MOCPParser
else:
    from MOCPParser import MOCPParser

# This class defines a complete listener for a parse tree produced by MOCPParser.
class MOCPListener(ParseTreeListener):

    # Enter a parse tree produced by MOCPParser#programa.
    def enterPrograma(self, ctx:MOCPParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MOCPParser#programa.
    def exitPrograma(self, ctx:MOCPParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MOCPParser#prototipo.
    def enterPrototipo(self, ctx:MOCPParser.PrototipoContext):
        pass

    # Exit a parse tree produced by MOCPParser#prototipo.
    def exitPrototipo(self, ctx:MOCPParser.PrototipoContext):
        pass


    # Enter a parse tree produced by MOCPParser#funcao.
    def enterFuncao(self, ctx:MOCPParser.FuncaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#funcao.
    def exitFuncao(self, ctx:MOCPParser.FuncaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#nomeFuncao.
    def enterNomeFuncao(self, ctx:MOCPParser.NomeFuncaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#nomeFuncao.
    def exitNomeFuncao(self, ctx:MOCPParser.NomeFuncaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#listaParametros.
    def enterListaParametros(self, ctx:MOCPParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by MOCPParser#listaParametros.
    def exitListaParametros(self, ctx:MOCPParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by MOCPParser#parametro.
    def enterParametro(self, ctx:MOCPParser.ParametroContext):
        pass

    # Exit a parse tree produced by MOCPParser#parametro.
    def exitParametro(self, ctx:MOCPParser.ParametroContext):
        pass


    # Enter a parse tree produced by MOCPParser#tipo.
    def enterTipo(self, ctx:MOCPParser.TipoContext):
        pass

    # Exit a parse tree produced by MOCPParser#tipo.
    def exitTipo(self, ctx:MOCPParser.TipoContext):
        pass


    # Enter a parse tree produced by MOCPParser#declaracao.
    def enterDeclaracao(self, ctx:MOCPParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#declaracao.
    def exitDeclaracao(self, ctx:MOCPParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#listaVariaveis.
    def enterListaVariaveis(self, ctx:MOCPParser.ListaVariaveisContext):
        pass

    # Exit a parse tree produced by MOCPParser#listaVariaveis.
    def exitListaVariaveis(self, ctx:MOCPParser.ListaVariaveisContext):
        pass


    # Enter a parse tree produced by MOCPParser#variavel.
    def enterVariavel(self, ctx:MOCPParser.VariavelContext):
        pass

    # Exit a parse tree produced by MOCPParser#variavel.
    def exitVariavel(self, ctx:MOCPParser.VariavelContext):
        pass


    # Enter a parse tree produced by MOCPParser#blocoArray.
    def enterBlocoArray(self, ctx:MOCPParser.BlocoArrayContext):
        pass

    # Exit a parse tree produced by MOCPParser#blocoArray.
    def exitBlocoArray(self, ctx:MOCPParser.BlocoArrayContext):
        pass


    # Enter a parse tree produced by MOCPParser#listaValores.
    def enterListaValores(self, ctx:MOCPParser.ListaValoresContext):
        pass

    # Exit a parse tree produced by MOCPParser#listaValores.
    def exitListaValores(self, ctx:MOCPParser.ListaValoresContext):
        pass


    # Enter a parse tree produced by MOCPParser#bloco.
    def enterBloco(self, ctx:MOCPParser.BlocoContext):
        pass

    # Exit a parse tree produced by MOCPParser#bloco.
    def exitBloco(self, ctx:MOCPParser.BlocoContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucoes.
    def enterInstrucoes(self, ctx:MOCPParser.InstrucoesContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucoes.
    def exitInstrucoes(self, ctx:MOCPParser.InstrucoesContext):
        pass


    # Enter a parse tree produced by MOCPParser#atribuicao.
    def enterAtribuicao(self, ctx:MOCPParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#atribuicao.
    def exitAtribuicao(self, ctx:MOCPParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucaoSe.
    def enterInstrucaoSe(self, ctx:MOCPParser.InstrucaoSeContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucaoSe.
    def exitInstrucaoSe(self, ctx:MOCPParser.InstrucaoSeContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucaoEnquanto.
    def enterInstrucaoEnquanto(self, ctx:MOCPParser.InstrucaoEnquantoContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucaoEnquanto.
    def exitInstrucaoEnquanto(self, ctx:MOCPParser.InstrucaoEnquantoContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucaoPara.
    def enterInstrucaoPara(self, ctx:MOCPParser.InstrucaoParaContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucaoPara.
    def exitInstrucaoPara(self, ctx:MOCPParser.InstrucaoParaContext):
        pass


    # Enter a parse tree produced by MOCPParser#expressaoOuAtribuicao.
    def enterExpressaoOuAtribuicao(self, ctx:MOCPParser.ExpressaoOuAtribuicaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#expressaoOuAtribuicao.
    def exitExpressaoOuAtribuicao(self, ctx:MOCPParser.ExpressaoOuAtribuicaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucaoRetorno.
    def enterInstrucaoRetorno(self, ctx:MOCPParser.InstrucaoRetornoContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucaoRetorno.
    def exitInstrucaoRetorno(self, ctx:MOCPParser.InstrucaoRetornoContext):
        pass


    # Enter a parse tree produced by MOCPParser#instrucaoEscrita.
    def enterInstrucaoEscrita(self, ctx:MOCPParser.InstrucaoEscritaContext):
        pass

    # Exit a parse tree produced by MOCPParser#instrucaoEscrita.
    def exitInstrucaoEscrita(self, ctx:MOCPParser.InstrucaoEscritaContext):
        pass


    # Enter a parse tree produced by MOCPParser#argumento_texto.
    def enterArgumento_texto(self, ctx:MOCPParser.Argumento_textoContext):
        pass

    # Exit a parse tree produced by MOCPParser#argumento_texto.
    def exitArgumento_texto(self, ctx:MOCPParser.Argumento_textoContext):
        pass


    # Enter a parse tree produced by MOCPParser#chamadaFuncao.
    def enterChamadaFuncao(self, ctx:MOCPParser.ChamadaFuncaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#chamadaFuncao.
    def exitChamadaFuncao(self, ctx:MOCPParser.ChamadaFuncaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#chamadaLeitura.
    def enterChamadaLeitura(self, ctx:MOCPParser.ChamadaLeituraContext):
        pass

    # Exit a parse tree produced by MOCPParser#chamadaLeitura.
    def exitChamadaLeitura(self, ctx:MOCPParser.ChamadaLeituraContext):
        pass


    # Enter a parse tree produced by MOCPParser#argumentos.
    def enterArgumentos(self, ctx:MOCPParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by MOCPParser#argumentos.
    def exitArgumentos(self, ctx:MOCPParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by MOCPParser#ExpressaoBase.
    def enterExpressaoBase(self, ctx:MOCPParser.ExpressaoBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#ExpressaoBase.
    def exitExpressaoBase(self, ctx:MOCPParser.ExpressaoBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#OuLogico.
    def enterOuLogico(self, ctx:MOCPParser.OuLogicoContext):
        pass

    # Exit a parse tree produced by MOCPParser#OuLogico.
    def exitOuLogico(self, ctx:MOCPParser.OuLogicoContext):
        pass


    # Enter a parse tree produced by MOCPParser#ComparacaoBase.
    def enterComparacaoBase(self, ctx:MOCPParser.ComparacaoBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#ComparacaoBase.
    def exitComparacaoBase(self, ctx:MOCPParser.ComparacaoBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#ELogico.
    def enterELogico(self, ctx:MOCPParser.ELogicoContext):
        pass

    # Exit a parse tree produced by MOCPParser#ELogico.
    def exitELogico(self, ctx:MOCPParser.ELogicoContext):
        pass


    # Enter a parse tree produced by MOCPParser#Comparacao.
    def enterComparacao(self, ctx:MOCPParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Comparacao.
    def exitComparacao(self, ctx:MOCPParser.ComparacaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#AditivaBase.
    def enterAditivaBase(self, ctx:MOCPParser.AditivaBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#AditivaBase.
    def exitAditivaBase(self, ctx:MOCPParser.AditivaBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#MultiplicativaBase.
    def enterMultiplicativaBase(self, ctx:MOCPParser.MultiplicativaBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#MultiplicativaBase.
    def exitMultiplicativaBase(self, ctx:MOCPParser.MultiplicativaBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#Adicao.
    def enterAdicao(self, ctx:MOCPParser.AdicaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Adicao.
    def exitAdicao(self, ctx:MOCPParser.AdicaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#Subtracao.
    def enterSubtracao(self, ctx:MOCPParser.SubtracaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Subtracao.
    def exitSubtracao(self, ctx:MOCPParser.SubtracaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#Multiplicacao.
    def enterMultiplicacao(self, ctx:MOCPParser.MultiplicacaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Multiplicacao.
    def exitMultiplicacao(self, ctx:MOCPParser.MultiplicacaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#UnariaBase.
    def enterUnariaBase(self, ctx:MOCPParser.UnariaBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#UnariaBase.
    def exitUnariaBase(self, ctx:MOCPParser.UnariaBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#Modulo.
    def enterModulo(self, ctx:MOCPParser.ModuloContext):
        pass

    # Exit a parse tree produced by MOCPParser#Modulo.
    def exitModulo(self, ctx:MOCPParser.ModuloContext):
        pass


    # Enter a parse tree produced by MOCPParser#Divisao.
    def enterDivisao(self, ctx:MOCPParser.DivisaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Divisao.
    def exitDivisao(self, ctx:MOCPParser.DivisaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#Negacao.
    def enterNegacao(self, ctx:MOCPParser.NegacaoContext):
        pass

    # Exit a parse tree produced by MOCPParser#Negacao.
    def exitNegacao(self, ctx:MOCPParser.NegacaoContext):
        pass


    # Enter a parse tree produced by MOCPParser#CastReal.
    def enterCastReal(self, ctx:MOCPParser.CastRealContext):
        pass

    # Exit a parse tree produced by MOCPParser#CastReal.
    def exitCastReal(self, ctx:MOCPParser.CastRealContext):
        pass


    # Enter a parse tree produced by MOCPParser#CastInteiro.
    def enterCastInteiro(self, ctx:MOCPParser.CastInteiroContext):
        pass

    # Exit a parse tree produced by MOCPParser#CastInteiro.
    def exitCastInteiro(self, ctx:MOCPParser.CastInteiroContext):
        pass


    # Enter a parse tree produced by MOCPParser#PrimariaBase.
    def enterPrimariaBase(self, ctx:MOCPParser.PrimariaBaseContext):
        pass

    # Exit a parse tree produced by MOCPParser#PrimariaBase.
    def exitPrimariaBase(self, ctx:MOCPParser.PrimariaBaseContext):
        pass


    # Enter a parse tree produced by MOCPParser#AcessoVetor.
    def enterAcessoVetor(self, ctx:MOCPParser.AcessoVetorContext):
        pass

    # Exit a parse tree produced by MOCPParser#AcessoVetor.
    def exitAcessoVetor(self, ctx:MOCPParser.AcessoVetorContext):
        pass


    # Enter a parse tree produced by MOCPParser#ChamadaGenerica.
    def enterChamadaGenerica(self, ctx:MOCPParser.ChamadaGenericaContext):
        pass

    # Exit a parse tree produced by MOCPParser#ChamadaGenerica.
    def exitChamadaGenerica(self, ctx:MOCPParser.ChamadaGenericaContext):
        pass


    # Enter a parse tree produced by MOCPParser#VariavelID.
    def enterVariavelID(self, ctx:MOCPParser.VariavelIDContext):
        pass

    # Exit a parse tree produced by MOCPParser#VariavelID.
    def exitVariavelID(self, ctx:MOCPParser.VariavelIDContext):
        pass


    # Enter a parse tree produced by MOCPParser#Numero.
    def enterNumero(self, ctx:MOCPParser.NumeroContext):
        pass

    # Exit a parse tree produced by MOCPParser#Numero.
    def exitNumero(self, ctx:MOCPParser.NumeroContext):
        pass


    # Enter a parse tree produced by MOCPParser#NumeroReal.
    def enterNumeroReal(self, ctx:MOCPParser.NumeroRealContext):
        pass

    # Exit a parse tree produced by MOCPParser#NumeroReal.
    def exitNumeroReal(self, ctx:MOCPParser.NumeroRealContext):
        pass


    # Enter a parse tree produced by MOCPParser#Parenteses.
    def enterParenteses(self, ctx:MOCPParser.ParentesesContext):
        pass

    # Exit a parse tree produced by MOCPParser#Parenteses.
    def exitParenteses(self, ctx:MOCPParser.ParentesesContext):
        pass


    # Enter a parse tree produced by MOCPParser#opRel.
    def enterOpRel(self, ctx:MOCPParser.OpRelContext):
        pass

    # Exit a parse tree produced by MOCPParser#opRel.
    def exitOpRel(self, ctx:MOCPParser.OpRelContext):
        pass



del MOCPParser