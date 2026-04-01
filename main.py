import sys
from antlr4 import *
from antlr4.tree.Tree import TerminalNode

from MOCP.MOCPLexer import MOCPLexer
from MOCP.MOCPParser import MOCPParser
from MOCP.MOCErrorListener import MOCErrorListener
from MOCP.ASTBuilder import ASTBuilder
from MOCP.ASTMini import ASTMiniBuilder


def mostrar_tokens(caminho):
    input_stream = FileStream(caminho, encoding="utf-8")

    error_listener = MOCErrorListener()
    lexer = MOCPLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token = lexer.nextToken()

    print("Tokens:")

    while token.type != Token.EOF:
        nome_token = lexer.symbolicNames[token.type]
        print(f"{nome_token:15} -> '{token.text}'")
        token = lexer.nextToken()

    if error_listener.erros:
        print("\nErros léxicos:")
        for erro in error_listener.erros:
            print(erro)


def imprimir_arvore(no, parser, prefixo="", ultimo=True):
    conector = "└── " if ultimo else "├── "

    if isinstance(no, TerminalNode):
        texto = no.getText()
        if texto != "<EOF>":
            print(prefixo + conector + texto)
        return

    nome_regra = parser.ruleNames[no.getRuleIndex()]
    print(prefixo + conector + nome_regra)

    novo_prefixo = prefixo + ("    " if ultimo else "│   ")
    filhos = [no.getChild(i) for i in range(no.getChildCount())]

    filhos_validos = []
    for filho in filhos:
        if isinstance(filho, TerminalNode) and filho.getText() == "<EOF>":
            continue
        filhos_validos.append(filho)

    for i, filho in enumerate(filhos_validos):
        imprimir_arvore(filho, parser, novo_prefixo, i == len(filhos_validos) - 1)


def imprimir_ast(no, prefixo="", ultimo=True):
    if no is None:
        return

    conector = "└── " if ultimo else "├── "
    print(prefixo + conector + no.label())

    novo_prefixo = prefixo + ("    " if ultimo else "│   ")
    filhos = [f for f in no.children() if f is not None]

    for i, filho in enumerate(filhos):
        imprimir_ast(filho, novo_prefixo, i == len(filhos) - 1)


def preparar_parser(caminho):
    input_stream = FileStream(caminho, encoding="utf-8")
    error_listener = MOCErrorListener()

    lexer = MOCPLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token_stream = CommonTokenStream(lexer)

    parser = MOCPParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.programa()
    return tree, parser, error_listener


def mostrar_arvore_sintatica(caminho):
    tree, parser, error_listener = preparar_parser(caminho)

    if not error_listener.erros:
        print("Árvore sintática:")
        imprimir_arvore(tree, parser)
    else:
        print("Erros sintáticos:")
        for erro in error_listener.erros:
            print(erro)


def mostrar_arvore_sintatica_bruta(caminho):
    tree, parser, error_listener = preparar_parser(caminho)

    if not error_listener.erros:
        print("Árvore sintática bruta:")
        print(tree.toStringTree(recog=parser))
    else:
        print("Erros sintáticos:")
        for erro in error_listener.erros:
            print(erro)


def mostrar_ast(caminho):
    tree, parser, error_listener = preparar_parser(caminho)

    if not error_listener.erros:
        builder = ASTBuilder()
        ast = builder.visit(tree)

        print("Árvore sintática abstrata:")
        imprimir_ast(ast)
    else:
        print("Erros sintáticos:")
        for erro in error_listener.erros:
            print(erro)


def mostrar_ast_mini(caminho):
    tree, parser, error_listener = preparar_parser(caminho)

    if not error_listener.erros:
        builder = ASTBuilder()
        ast = builder.visit(tree)

        mini_builder = ASTMiniBuilder()
        mini = mini_builder.build(ast)

        print("AST simplificada:")

        if isinstance(mini, list):
            for i, node in enumerate(mini):
                if node is not None:
                    node.print_tree("", i == len(mini) - 1)
        elif mini is not None:
            mini.print_tree()
    else:
        print("Erros sintáticos:")
        for erro in error_listener.erros:
            print(erro)


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python3 main.py -lex <ficheiro.mocp>")
        print("  python3 main.py -syn <ficheiro.mocp>")
        print("  python3 main.py -synraw <ficheiro.mocp>")
        print("  python3 main.py -ast <ficheiro.mocp>")
        print("  python3 main.py -astmini <ficheiro.mocp>")
        return

    modo = sys.argv[1]
    ficheiro = sys.argv[2]

    if modo == "-lex":
        mostrar_tokens(ficheiro)
    elif modo == "-syn":
        mostrar_arvore_sintatica(ficheiro)
    elif modo == "-synraw":
        mostrar_arvore_sintatica_bruta(ficheiro)
    elif modo == "-ast":
        mostrar_ast(ficheiro)
    elif modo == "-astmini":
        mostrar_ast_mini(ficheiro)
    else:
        print("Modo inválido. Use -lex, -syn, -synraw, -ast ou -astmini.")


if __name__ == "__main__":
    main()