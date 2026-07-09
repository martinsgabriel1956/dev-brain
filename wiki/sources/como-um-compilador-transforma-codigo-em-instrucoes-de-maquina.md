---
type: source
title: "Como um Compilador Transforma Código em Instruções de Máquina"
aliases: ["seis etapas de um compilador", "compiler pipeline six stages", "lexing parsing semantic IR optimization codegen"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [cs-fundamentals, compiladores, lexing, parsing, ast, analise-semantica, ir, otimizacao, geracao-de-codigo, jit, tabela-de-simbolos]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina.md
source_url:
author: desconhecido (canal YouTube)
date_published:
date_ingested: 2026-07-09
---

# Como um Compilador Transforma Código em Instruções de Máquina

## TL;DR

Transcrição que percorre o pipeline de um compilador em seis estágios explícitos — análise léxica, análise sintática, análise semântica, representação intermediária (IR), otimização e geração de código — usando o exemplo `a + b * 2` para mostrar como texto vira tokens, tokens viram AST, a AST é validada via tabela de símbolos, simplificada em IR, otimizada (constant folding, dead code elimination, loop unrolling, inlining) e finalmente traduzida em instruções de máquina com alocação de registradores. Fecha com compilador vs. interpretador vs. JIT (Java/JVM, V8) e o argumento de que TypeScript, Babel e Webpack são compiladores no mesmo sentido técnico.

## Key Claims

1. **O compilador é um pipeline de seis estágios**, cada um resolvendo um problema bem definido e passando sua saída para o próximo: lexing → parsing → análise semântica → IR → otimização → geração de código. Cross-checado contra `cs-fundamentals/compiler-fundamentals.md` — mesma sequência, mesma ordem, nomenclatura equivalente (a referência chama de "Semantic Analysis" e "IR Generation" separadamente, igual à fonte).
2. **Análise léxica (lexing) agrupa caracteres em tokens** — keywords, identificadores, operadores, literais — descartando espaços e comentários; não resolve estrutura, só reconhece pedaços.
3. **Análise sintática (parsing) monta a AST** respeitando precedência de operadores (`a + b * 2` agrupa `b * 2` primeiro porque multiplicação tem precedência sobre soma); erro de sintaxe ocorre quando o parser não consegue montar a árvore.
4. **Análise semântica verifica significado, não apenas estrutura** — tipos compatíveis, variáveis declaradas antes do uso, funções existentes, aridade correta — via uma **tabela de símbolos** construída durante o percurso da AST (nome → tipo, escopo, posição na stack).
5. **IR existe para evitar a explosão combinatória N×M** entre linguagens e arquiteturas — cada linguagem traduz para IR, cada arquitetura traduz do IR; a IR quebra expressões compostas em instruções atômicas de uma operação cada.
6. **Otimizações citadas**: constant folding (`2+3` → `5` em compile time), dead code elimination (remove blocos inalcançáveis como `if false`), loop unrolling (desenrola iterações fixas para eliminar overhead de branch/contador) e function inlining (copia corpo de função pequena no call site, eliminando custo de stack frame). Todas batem com as descrições e exemplos de código em `cs-fundamentals/compiler-fundamentals.md`.
7. **Geração de código traduz IR em instruções da arquitetura alvo**, com **alocação de registradores** como um dos problemas mais difíceis: variáveis usadas em loop preferencialmente em registrador, variáveis de uso único podem ir para a stack. Assembler traduz para bytes (object file); linker resolve referências externas e gera o executável.
8. **Compilador vs. interpretador**: compilador traduz o programa inteiro antes de rodar (compila uma vez, roda várias vezes, execução rápida); interpretador traduz e executa linha por linha (início instantâneo, execução mais lenta por chamada).
9. **JIT como meio-termo**: JVM interpreta bytecode e compila para nativo os trechos "quentes" (hot paths); V8 (JavaScript) faz o mesmo, começando por interpretação e promovendo hot paths para código nativo em runtime.
10. **TypeScript, Babel e Webpack são compiladores** no sentido técnico pleno — fazem análise léxica, sintática, semântica, transformação e geram output, seguindo o mesmo pipeline descrito.
11. **Ler mensagens de erro à luz do pipeline**: erro de sintaxe = parser não montou a árvore; erro de tipo = análise semântica encontrou incompatibilidade; "variável undefined" = tabela de símbolos não encontrou o nome.

## Entidades Mencionadas

- JVM / Java (bytecode + JIT)
- V8 / JavaScript (interpretação inicial + TurboFan-style hot path compilation, não citado por nome mas descrito)
- TypeScript, Babel, Webpack (compiladores do ecossistema JS)
- x86 (arquitetura usada nos exemplos de assembly: `imul`, `add`, `move`)

## Conceitos Tocados

- [[wiki/concepts/compilador]]
- [[wiki/concepts/pipeline-de-compilacao]]

## Open Questions

- A fonte não detalha as técnicas de parsing (recursive descent, LR(k), Pratt parser) nem cita ferramentas reais (YACC, ANTLR) — ver `cs-fundamentals/compiler-fundamentals.md` para a tabela de técnicas.
- Não menciona LLVM, GraalVM nem WebAssembly como targets de geração de código — fonte fica no nível conceitual do pipeline genérico, sem entrar em backends reais.
- Não explica algoritmos de alocação de registradores (graph coloring, linear scan) — apenas cita a heurística informal "usado em loop vai pro registrador".
- Não aprofunda por que exatamente N linguagens × M arquiteturas seria custoso sem IR — afirma o princípio mas não quantifica.

## Raw Quotes

> "Seis tokens de código, duas instruções de máquina: algo transformou um no outro, e não foi uma tradução simples. Foram seis etapas."

> "Pensa no lexer como alguém lendo uma frase e separando cada palavra e pontuação: não precisa entender o significado, só precisa saber onde começa e termina cada pedaço e de que tipo é."

> "Por que não ir direto para código de máquina? Porque existem muitas linguagens e muitas arquiteturas de processador. Com IR, cada linguagem traduz para IR e cada arquitetura traduz do IR — evitando combinações N×M."

> "O código legível que você escreveu roda tão rápido quanto código otimizado à mão, às vezes até mais rápido, porque o compilador enxerga otimizações que humanos não enxergam."

> "A diferença entre compilador e interpretador é cada vez mais difícil de traçar — a maioria das linguagens modernas usa os dois."
