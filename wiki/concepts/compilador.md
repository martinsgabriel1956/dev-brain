---
type: concept
title: "Compilador"
aliases: ["compiler", "compilação", "interpretador", "AST", "análise léxica"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [cs-fundamentals, compiladores, interpretadores, ast, linguagens-de-programacao]
skill: cs-fundamentals
status: draft
---

# Compilador

Programa que **traduz código-fonte** em linguagem de alto nível para código que o computador pode executar (código de máquina ou bytecode). A ponte entre o que o humano escreve e o que o processador entende.

## Pipeline de compilação

```
Código-fonte → [Lexer] → Tokens → [Parser] → AST → [Otimizador] → Código de máquina
```

### 1. Análise Léxica (Lexer / Tokenizer)

Quebra o texto em unidades atômicas chamadas **tokens**:

```
let x = 10 + 5;
→ [KEYWORD:let] [IDENT:x] [OP:=] [NUM:10] [OP:+] [NUM:5] [SEMI:;]
```

### 2. Análise Sintática (Parser)

Organiza os tokens numa **AST** (Abstract Syntax Tree) que representa a estrutura lógica do programa:

```
Assignment
├── Identifier: x
└── BinaryOp: +
    ├── Literal: 10
    └── Literal: 5
```

### 3. Otimização + Geração de Código

Analisa a AST, aplica otimizações (dead code elimination, inlining, constant folding) e gera código de máquina — frequentemente **mais eficiente** do que o que o humano escreveu.

## Compilador vs Interpretador

| | Compilador | Interpretador |
|---|---|---|
| **Quando traduz** | Antes da execução (offline) | Durante a execução (online) |
| **Output** | Executável ou bytecode | Executa diretamente |
| **Velocidade** | Mais rápido em runtime | Mais lento — traduz linha por linha |
| **Flexibilidade** | Menor (precisa recompilar) | Maior (executa código dinâmico) |
| **Exemplos** | C, C++, Rust, Go | Python, Ruby, JavaScript (Node) |

## O meio-termo: Bytecode + VM

Java e C# compilam para um **código intermediário** (bytecode) que roda numa **máquina virtual** (JVM, .NET CLR). Portabilidade sem abrir mão de otimização JIT (Just-In-Time compilation).

```
Java source → javac → .class (bytecode) → JVM → código de máquina nativo (JIT)
```

## Relação com abstração

O compilador é a [[abstracao]] que permite escrever `let x = 10` e não se preocupar com registradores, pilha de execução ou endereços de memória. É uma das camadas mais importantes da hierarquia de abstrações.

## Relação com outros conceitos

- [[abstracao]] — compilador é a abstração que separa linguagem humana de linguagem de máquina
- [[logica-booleana]] — o output final são instruções que operam em bits via portas lógicas
- [[recursao]] — parsers recursivos descendentes são implementações clássicas de analisadores sintáticos

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
