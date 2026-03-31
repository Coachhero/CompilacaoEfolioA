grammar MOCP;

programa
    : (prototipo | declaracao | funcao)* EOF
    ;

prototipo
    : tipo nomeFuncao LPAREN listaParametros? RPAREN PONTOVIRG
    ;

funcao
    : tipo nomeFuncao LPAREN listaParametros? RPAREN bloco
    ;

nomeFuncao
    : IDENTIFICADOR
    | PRINCIPAL
    ;

listaParametros
    : VAZIO
    | parametro (VIRG parametro)*
    ;

parametro
    : tipo IDENTIFICADOR? (LBRACK RBRACK)?
    ;

tipo
    : INTEIRO
    | REAL
    | VAZIO
    ;

declaracao
    : tipo listaVariaveis PONTOVIRG
    ;

listaVariaveis
    : variavel (VIRG variavel)*
    ;

variavel
    : IDENTIFICADOR
    | IDENTIFICADOR ASSIGN expressao
    | IDENTIFICADOR LBRACK INT_LITERAL RBRACK
    | IDENTIFICADOR LBRACK RBRACK ASSIGN blocoArray
    | IDENTIFICADOR LBRACK RBRACK ASSIGN chamadaLeitura
    ;

blocoArray
    : LCHAVE listaValores? RCHAVE
    ;

listaValores
    : expressao (VIRG expressao)*
    ;

bloco
    : LCHAVE instrucoes* RCHAVE
    ;

instrucoes
    : declaracao
    | atribuicao PONTOVIRG
    | instrucaoEscrita PONTOVIRG
    | instrucaoRetorno PONTOVIRG
    | instrucaoSe
    | instrucaoEnquanto
    | instrucaoPara
    | chamadaFuncao PONTOVIRG
    | bloco
    ;

atribuicao
    : IDENTIFICADOR ASSIGN expressao
    | IDENTIFICADOR LBRACK expressao RBRACK ASSIGN expressao
    ;

instrucaoSe
    : SE LPAREN expressao RPAREN bloco (SENAO bloco)?
    ;

instrucaoEnquanto
    : ENQUANTO LPAREN expressao RPAREN bloco
    ;

instrucaoPara
    : PARA LPAREN expressaoOuAtribuicao? PONTOVIRG expressao? PONTOVIRG expressaoOuAtribuicao? RPAREN bloco
    ;

expressaoOuAtribuicao
    : atribuicao
    | expressao
    ;

instrucaoRetorno
    : RETORNAR expressao
    ;

instrucaoEscrita
    : ESCREVER LPAREN expressao RPAREN
    | ESCREVERC LPAREN expressao RPAREN
    | ESCREVERV LPAREN IDENTIFICADOR RPAREN
    | ESCREVERS LPAREN argumento_texto RPAREN
    ;

argumento_texto
    : IDENTIFICADOR
    | TEXTO_LITERAL
    ;

chamadaFuncao
    : chamadaLeitura
    | IDENTIFICADOR LPAREN argumentos? RPAREN
    ;

chamadaLeitura
    : LER LPAREN RPAREN
    | LERC LPAREN RPAREN
    | LERS LPAREN RPAREN
    ;

argumentos
    : expressao (VIRG expressao)*
    ;

expressao
    : expressao OR expressao_logica_e                  # OuLogico
    | expressao_logica_e                               # ExpressaoBase
    ;

expressao_logica_e
    : expressao_logica_e AND expressao_comparacao      # ELogico
    | expressao_comparacao                             # ComparacaoBase
    ;

expressao_comparacao
    : expressao_comparacao opRel expressao_aditiva     # Comparacao
    | expressao_aditiva                                # AditivaBase
    ;

expressao_aditiva
    : expressao_aditiva PLUS expressao_multiplicativa  # Adicao
    | expressao_aditiva MINUS expressao_multiplicativa # Subtracao
    | expressao_multiplicativa                         # MultiplicativaBase
    ;

expressao_multiplicativa
    : expressao_multiplicativa STAR expressao_unaria   # Multiplicacao
    | expressao_multiplicativa DIV expressao_unaria    # Divisao
    | expressao_multiplicativa MOD expressao_unaria    # Modulo
    | expressao_unaria                                 # UnariaBase
    ;

expressao_unaria
    : NOT expressao_unaria                             # Negacao
    | LPAREN REAL RPAREN expressao_unaria              # CastReal
    | LPAREN INTEIRO RPAREN expressao_unaria           # CastInteiro
    | expressao_primaria                               # PrimariaBase
    ;

expressao_primaria
    : IDENTIFICADOR LBRACK expressao RBRACK            # AcessoVetor
    | chamadaFuncao                                    # ChamadaGenerica
    | IDENTIFICADOR                                    # VariavelID
    | INT_LITERAL                                      # Numero
    | REAL_LITERAL                                     # NumeroReal
    | LPAREN expressao RPAREN                          # Parenteses
    ;

opRel
    : EQUAL
    | NOTEQUAL
    | LESS
    | GREATER
    | LESSEQ
    | GREATEREQ
    ;

INTEIRO        : 'inteiro';
REAL           : 'real';
VAZIO          : 'vazio';
PRINCIPAL      : 'principal';
SE             : 'se';
SENAO          : 'senao';
ENQUANTO       : 'enquanto';
PARA           : 'para';
RETORNAR       : 'retornar';
LER            : 'ler';
LERC           : 'lerc';
LERS           : 'lers';
ESCREVER       : 'escrever';
ESCREVERC      : 'escreverc';
ESCREVERV      : 'escreverv';
ESCREVERS      : 'escrevers';

PLUS           : '+';
MINUS          : '-';
STAR           : '*';
DIV            : '/';
MOD            : '%';
ASSIGN         : '=';
EQUAL          : '==';
NOTEQUAL       : '!=';
LESS           : '<';
GREATER        : '>';
LESSEQ         : '<=';
GREATEREQ      : '>=';
AND            : '&&';
OR             : '||';
NOT            : '!';
PONTOVIRG      : ';';
VIRG           : ',';
LPAREN         : '(';
RPAREN         : ')';
LCHAVE         : '{';
RCHAVE         : '}';
LBRACK         : '[';
RBRACK         : ']';

REAL_LITERAL   : [0-9]+ '.' [0-9]+;
INT_LITERAL    : [0-9]+;
TEXTO_LITERAL  : '"' (ESC_SEQ | ~["\\])* '"';
IDENTIFICADOR  : [a-zA-Z_áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ] [a-zA-Z_0-9áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]*;

fragment ESC_SEQ : '\\' [btnr"\\];

LINE_COMMENT   : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT  : '/*' .*? '*/' -> skip;
WS             : [ \t\r\n]+ -> skip;