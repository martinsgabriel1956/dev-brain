---
type: concept
title: "Compilador"
aliases: ["compiler", "compilação", "interpretador", "AST", "análise léxica"]
date_created: 2026-06-26
date_updated: 2026-07-09
source_count: 3
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

### 3. Análise Semântica

Entre a AST e a otimização existe um estágio que verifica se o programa *faz sentido*, não só se está bem formado: tipos compatíveis, variáveis declaradas antes do uso, funções existentes com aridade correta. A ferramenta central é a **tabela de símbolos** — mapeia cada nome (variável, função) ao seu tipo, escopo e posição de armazenamento (registrador ou stack). Ela é construída conforme o compilador percorre a AST: cada declaração adiciona uma entrada, cada uso consulta a tabela para resolver a que declaração aquele nome se refere. `int x = "hello";` tem sintaxe perfeita mas falha aqui — string atribuída a inteiro.

### 4. Representação Intermediária (IR)

Antes de otimizar e gerar código, a AST validada é convertida numa forma mais simples e independente de arquitetura: cada instrução IR faz uma única operação (`a + b * 2` vira "multiplica b por 2, guarda em t1; soma a com t1, guarda em result"). É essa forma atômica que torna a otimização tratável, e é o que evita a explosão combinatória de N linguagens × M arquiteturas — cada linguagem só precisa traduzir para IR, e cada arquitetura só precisa traduzir do IR.

### 5. Otimização + Geração de Código

Analisa a IR, aplica otimizações (dead code elimination, inlining, constant folding, loop unrolling) e gera código de máquina — frequentemente **mais eficiente** do que o que o humano escreveu. Na geração de código, um dos problemas mais difíceis é a **alocação de registradores**: a CPU tem poucos registradores, então o compilador decide quais variáveis ficam neles (tipicamente as usadas em loop) e quais vão para a stack (uso único). O assembler traduz para bytes (object file); o linker resolve referências externas e produz o executável — ver [[wiki/concepts/pipeline-de-compilacao]] para o detalhamento dessa fase final.

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

Bytecode é sequencial e compacto, o que o torna mais rápido de executar do que percorrer uma AST nó por nó — e mais simples de implementar do que um compilador nativo completo (que exige lidar com registradores e alocação de memória por arquitetura de CPU). Python (CPython) e Lua (Lua VM) seguem o mesmo modelo. Um JIT identifica em runtime as partes do código mais executadas ("hot paths") e as compila para código nativo enquanto o programa roda, combinando a portabilidade do bytecode com performance próxima da nativa nos trechos que importam.

## Decisões de design que antecedem o pipeline

O pipeline lexer → parser → AST → codegen é o *mecanismo*. Antes dele, quem projeta uma linguagem decide: qual [[wiki/concepts/sistema-de-tipos|sistema de tipos]] usar (estática/dinâmica/inferência), qual [[wiki/concepts/gerenciamento-de-memoria|modelo de gerenciamento de memória]] (manual/GC/ownership) e como a [[wiki/concepts/gramatica-formal-ebnf|gramática formal]] resolve ambiguidade via precedência e associatividade. Essas escolhas não são independentes — o propósito da linguagem (controle de hardware vs. produtividade vs. segurança de memória) determina em cascata as demais.

## Relação com abstração

O compilador é a [[abstracao]] que permite escrever `let x = 10` e não se preocupar com registradores, pilha de execução ou endereços de memória. É uma das camadas mais importantes da hierarquia de abstrações.

## Relação com outros conceitos

- [[abstracao]] — compilador é a abstração que separa linguagem humana de linguagem de máquina
- [[logica-booleana]] — o output final são instruções que operam em bits via portas lógicas
- [[recursao]] — parsers recursivos descendentes são implementações clássicas de analisadores sintáticos

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/como-criar-uma-linguagem-de-programacao]] — decisões de design (propósito, gramática, tipos, memória, ecossistema) que antecedem e envolvem o pipeline de compilação
- [[wiki/sources/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina]] — detalhamento da análise semântica (tabela de símbolos), da IR como forma atômica que evita explosão N×M, e da alocação de registradores na geração de código
