# Compilador MOCP com ANTLR (Python)

## Descrição geral
Este projeto implementa um compilador para a linguagem MOCP utilizando ANTLR4 com geração de código em Python. O programa realiza análise léxica e análise sintática de ficheiros .mocp, apresentando os resultados e os erros no terminal.

---

## Objetivo do programa
O objetivo do programa é:

- realizar análise léxica de programas escritos em MOCP;
- realizar análise sintática de programas escritos em MOCP;
- apresentar erros léxicos e sintáticos no ecrã;
- permitir testar programas válidos e inválidos;
- construir uma AST (Árvore Sintática Abstrata);
- gerar uma versão simplificada da AST (ASTMini).

---

## Requisitos necessários
Antes de executar o projeto, é necessário ter instalado:

- Python 3
- pip
- Java
- ANTLR4

---

## 1. Verificar se o Python está instalado

```bash
python3 --version
```

---

## 2. Criar ambiente virtual

```bash
python3 -m venv antlr
```

---

## 3. Ativar ambiente virtual

### Linux / macOS
```bash
source antlr/bin/activate
```

### Windows
```bash
antlr\Scripts\activate
```

---

## 4. Instalar dependências Python

```bash
pip install antlr4-python3-runtime
pip install antlr4-tools
```

---

## 5. Gerar o lexer e o parser a partir da gramática

```bash
antlr4 -Dlanguage=Python3 -listener -visitor -o MOCP MOCP/MOCP.g4
```

Este comando gera automaticamente os ficheiros principais do ANTLR em Python, nomeadamente:

- MOCPLexer.py
- MOCPParser.py
- MOCPListener.py
- MOCPVisitor.py

---

## Estrutura do projeto

```
.
├── main.py
├── MOCP/
│   ├── MOCP.g4
│   ├── MOCErrorListener.py
│   ├── MOCPLexer.py
│   ├── MOCPParser.py
│   ├── MOCPListener.py
│   ├── MOCPVisitor.py
│   ├── MOCP.interp
│   ├── MOCP.tokens
│   ├── MOCPLexer.interp
│   └── MOCPLexer.tokens
├── exemplos/
│   ├── exemplo1_se.mocp
│   ├── exemplo2_enquanto.mocp
│   ├── exemplo3_para.mocp
│   ├── exemplo4_recursivo.mocp
│   └── exemplo5_media_vetor.mocp
├── testes/
│   ├── teste1_valido_se.mocp
│   ├── teste2_valido_enquanto.mocp
│   ├── teste3_valido_para.mocp
│   ├── teste4_erro_lexico_simbolo.mocp
│   ├── teste5_erro_lexico_texto.mocp
│   ├── teste6_erro_sintatico_pontovirgula.mocp
│   ├── teste7_erro_sintatico_parenteses.mocp
│   └── teste8_erro_sintatico_c.mocp
└── README.md
```

---

## Como executar o programa

```bash
python3 main.py <modo> <ficheiro.mocp>
```

---

## Modos disponíveis

- -lex → análise léxica  
- -syn → análise sintática  
- -synraw → árvore completa do ANTLR  
- -ast → AST construída com Visitor  
- -astmini → AST simplificada  

---

# Análise léxica

## Exemplos
```bash
python3 main.py -lex exemplos/exemplo1_se.mocp
python3 main.py -lex exemplos/exemplo2_enquanto.mocp
python3 main.py -lex exemplos/exemplo3_para.mocp
python3 main.py -lex exemplos/exemplo4_recursivo.mocp
python3 main.py -lex exemplos/exemplo5_media_vetor.mocp
```

## Testes
```bash
python3 main.py -lex testes/teste1_valido_se.mocp
python3 main.py -lex testes/teste2_valido_enquanto.mocp
python3 main.py -lex testes/teste3_valido_para.mocp
python3 main.py -lex testes/teste4_erro_lexico_simbolo.mocp
python3 main.py -lex testes/teste5_erro_lexico_texto.mocp
python3 main.py -lex testes/teste6_erro_sintatico_pontovirgula.mocp
python3 main.py -lex testes/teste7_erro_sintatico_parenteses.mocp
python3 main.py -lex testes/teste8_erro_sintatico_c.mocp
```

---

# Análise sintática

## Exemplos
```bash
python3 main.py -syn exemplos/exemplo1_se.mocp
python3 main.py -syn exemplos/exemplo2_enquanto.mocp
python3 main.py -syn exemplos/exemplo3_para.mocp
python3 main.py -syn exemplos/exemplo4_recursivo.mocp
python3 main.py -syn exemplos/exemplo5_media_vetor.mocp
```

## Testes
```bash
python3 main.py -syn testes/teste1_valido_se.mocp
python3 main.py -syn testes/teste2_valido_enquanto.mocp
python3 main.py -syn testes/teste3_valido_para.mocp
python3 main.py -syn testes/teste4_erro_lexico_simbolo.mocp
python3 main.py -syn testes/teste5_erro_lexico_texto.mocp
python3 main.py -syn testes/teste6_erro_sintatico_pontovirgula.mocp
python3 main.py -syn testes/teste7_erro_sintatico_parenteses.mocp
python3 main.py -syn testes/teste8_erro_sintatico_c.mocp
```

---

# Árvore sintática completa

```bash
python3 main.py -synraw exemplos/exemplo1_se.mocp
```

---

# AST

## Exemplos
```bash
python3 main.py -ast exemplos/exemplo1_se.mocp
python3 main.py -ast exemplos/exemplo2_enquanto.mocp
python3 main.py -ast exemplos/exemplo3_para.mocp
python3 main.py -ast exemplos/exemplo4_recursivo.mocp
python3 main.py -ast exemplos/exemplo5_media_vetor.mocp
```

---

# AST Simplificada

## Exemplos
```bash
python3 main.py -astmini exemplos/exemplo1_se.mocp
python3 main.py -astmini exemplos/exemplo2_enquanto.mocp
python3 main.py -astmini exemplos/exemplo3_para.mocp
python3 main.py -astmini exemplos/exemplo4_recursivo.mocp
python3 main.py -astmini exemplos/exemplo5_media_vetor.mocp
```

---

# Árvore gráfica (ANTLR)

```bash
antlr4-parse MOCP/MOCP.g4 programa -gui exemplos/exemplo1_se.mocp
antlr4-parse MOCP/MOCP.g4 programa -gui exemplos/exemplo2_enquanto.mocp
antlr4-parse MOCP/MOCP.g4 programa -gui exemplos/exemplo3_para.mocp
antlr4-parse MOCP/MOCP.g4 programa -gui exemplos/exemplo4_recursivo.mocp
antlr4-parse MOCP/MOCP.g4 programa -gui exemplos/exemplo5_media_vetor.mocp
```

---

## Notas importantes

- AST e ASTMini utilizam o padrão Visitor
- -synraw mostra a árvore completa
- -astmini é a versão mais simples

---

## Autores

- Joao Lima  
- Miguel Couceiro
