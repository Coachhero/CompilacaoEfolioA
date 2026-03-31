import sys
from antlr4 import *
from MOCP.MOCPLexer import MOCPLexer
from MOCP.MOCPParser import MOCPParser
from MOCP.MOCErrorListener import MOCErrorListener


def mostrar_tokens(caminho):
    input_stream = FileStream(caminho, encoding="utf-8")

    error_listener = MOCErrorListener()
    lexer = MOCPLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token = lexer.nextToken()

    print("Árvore léxica:")
    print("programa")
    print("└── tokens")

    while token.type != Token.EOF:
        nome_token = lexer.symbolicNames[token.type]
        print(f"    ├── {nome_token}: '{token.text}'")
        token = lexer.nextToken()

    if error_listener.erros:
        print("\nErros léxicos:")
        for erro in error_listener.erros:
            print(erro)


def mostrar_arvore_sintatica(caminho):
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

    if not error_listener.erros:
        print("Árvore sintática:")
        print(tree.toStringTree(recog=parser))
    else:
        for erro in error_listener.erros:
            print(erro)


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python3 main.py -lex <ficheiro.mocp>")
        print("  python3 main.py -syn <ficheiro.mocp>")
        return

    modo = sys.argv[1]
    ficheiro = sys.argv[2]

    if modo == "-lex":
        mostrar_tokens(ficheiro)
    elif modo == "-syn":
        mostrar_arvore_sintatica(ficheiro)
    else:
        print("Modo inválido. Use -lex ou -syn.")


if __name__ == "__main__":
    main()