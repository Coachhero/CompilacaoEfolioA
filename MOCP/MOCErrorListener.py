from antlr4.error.ErrorListener import ErrorListener

class MOCErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = getattr(offendingSymbol, "text", "(simbolo invalido)")

        if "token recognition error" in msg:
            char_errado = msg.split("at:")[-1].strip()
            mensagem = f"[Erro Lexico] Token invalido {char_errado} na linha {line}, coluna {column}."

        elif "extraneous input" in msg:
            mensagem = f"[Erro Sintatico] O simbolo '{simbolo}' e inesperado nesta posicao (linha {line}, coluna {column})."

        elif "no viable alternative" in msg:
            expressao = msg.split("input")[-1].strip().strip("'")
            mensagem = f"[Erro Sintatico] Expressao mal formada: {expressao} (linha {line}, coluna {column})."

        elif "missing" in msg:
            esperado = msg.split("missing")[-1].split("at")[0].strip().strip("'")
            mensagem = f"[Erro Sintatico] Falta o elemento '{esperado}' perto de '{simbolo}' (linha {line}, coluna {column})."

        elif "mismatched input" in msg and "expecting" in msg:
            mensagem = f"[Erro Sintatico] O simbolo '{simbolo}' nao era esperado (linha {line}, coluna {column})."

        else:
            mensagem = f"[Erro Sintatico] Erro de sintaxe perto de '{simbolo}' (linha {line}, coluna {column}): {msg}"

        self.erros.append(mensagem)
