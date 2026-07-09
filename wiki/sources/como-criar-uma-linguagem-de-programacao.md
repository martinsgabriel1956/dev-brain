---
type: source
title: "Como Criar uma Linguagem de Programação"
aliases: ["criar linguagem de programação do zero", "anatomia de um compilador/interpretador", "como funciona uma linguagem de programação"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [cs-fundamentals, compiladores, interpretadores, parsers, sistema-de-tipos, runtime, garbage-collector, bytecode, llvm, linguagens-de-programacao]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-criar-uma-linguagem-de-programacao.md
source_url: ""
author: "desconhecido (canal YouTube)"
date_published: "desconhecido"
date_ingested: 2026-07-09
---

# Como Criar uma Linguagem de Programação

## TL;DR

Percurso completo de como uma linguagem de programação nasce e roda, em sete decisões encadeadas: (1) definir o **propósito** — que problema a linguagem resolve melhor que as alternativas, o que determina tipagem, modelo de execução e gerenciamento de memória; (2) formalizar a **gramática** com EBNF, resolvendo ambiguidade via precedência e associatividade; (3) construir o **front end** — [[wiki/concepts/compilador|lexer e parser]], gerando uma AST, escrito à mão (descida recursiva) ou via gerador PEG; (4) escolher o **[[wiki/concepts/sistema-de-tipos|sistema de tipos]]** — estática vs. dinâmica, com inferência como meio-termo; (5) escolher o **modelo de execução** — interpretador direto (lento, simples), compilação nativa via IR (rápido, difícil) ou bytecode + VM (meio-termo, com JIT); (6) escolher o **[[wiki/concepts/gerenciamento-de-memoria|gerenciamento de memória]]** — manual, garbage collector ou ownership (Rust); (7) construir **standard library, package manager e tooling** (formatter, linter, [[wiki/concepts/language-server-protocol|LSP]]) — sem isso, nenhuma linguagem tecnicamente boa sobrevive sem comunidade. Aponta *Crafting Interpreters* (Robert Nystrom), o *Dragon Book* e LLVM como recursos para quem quer implementar isso na prática.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Toda linguagem nasce resolvendo um problema específico, não tentando ser boa em tudo (C = controle de hardware, Python = produtividade, SQL = consulta de dados, Rust = segurança de memória sem GC, Go = concorrência simples, Elixir = tolerância a falhas herdada do Erlang) | Exemplos comparativos diretos na fonte | Alta |
| A escolha de propósito determina em cascata as decisões de tipagem, compilação/interpretação e gerenciamento de memória — não são escolhas independentes | Argumento estrutural central da fonte | Alta |
| Regras de precedência e associatividade existem para eliminar ambiguidade sintática (`1 + 2 * 3` só tem uma leitura válida se a gramática for bem definida) | Exemplo direto da fonte | Alta |
| Muitos compiladores importantes (Go, Rust, TypeScript) usam parsers escritos à mão por descida recursiva em vez de geradores de parser (PEG), por controle sobre erros e casos especiais de sintaxe | Exemplos citados nominalmente na fonte | Média (fonte não cita contra-exemplos de linguagens que usam geradores com sucesso) |
| Tipagem estática pega erros em tempo de compilação e melhora autocomplete, ao custo de mais verbosidade; tipagem dinâmica é mais rápida de escrever, mas erros só aparecem em tempo de execução (às vezes em produção) | Comparação direta na fonte | Alta |
| Inferência de tipos (TypeScript, Rust) é um meio-termo real — mantém segurança estática com sintaxe mais enxuta | Exemplo `let x = 42` | Alta |
| Interpretador direto (tree-walking) é a forma mais simples de implementar uma linguagem, mas é lenta porque percorrer uma árvore prejudica a localidade de cache do processador | Explicação técnica da fonte | Alta |
| Compilação nativa via IR (C, C++, Rust) é o caminho mais rápido em runtime, mas o mais difícil de implementar (registradores, alocação, geração de instruções por arquitetura) | Comparação direta na fonte | Alta |
| Bytecode + VM é o meio-termo dominante em linguagens modernas (JVM para Java, CPython para Python, Lua VM para Lua) — mais rápido que tree-walking, mais simples que compilação nativa completa | Exemplos nominais na fonte | Alta |
| JIT identifica em runtime as partes do código mais executadas e as compila para código nativo enquanto o programa roda | Explicação da fonte | Média (não detalha threshold/heurística de "hot path") |
| Três modelos de gerenciamento de memória cobrem o espaço de design: manual (C, `malloc`/`free`), garbage collector (Java, Go, Python, JavaScript) e ownership (Rust — dono sai do escopo, memória libera, verificado em compile-time, sem GC nem `free` manual) | Comparação de três vias feita explicitamente na fonte | Alta |
| Garbage collectors têm custo de pausas de runtime ("stop-the-world") dependendo do coletor | Afirmação da fonte, sem citar algoritmos específicos (mark-and-sweep, geracional, etc.) | Média |
| O modelo de concorrência do runtime (threads em Java, event loop em JavaScript, goroutines em Go) é uma decisão difícil de reverter depois, porque o código de usuário se apoia nela | Argumento da fonte | Alta |
| Uma linguagem tecnicamente boa não sobrevive sem standard library robusta, package manager, ferramentas (formatter/linter/debugger) e LSP — a comunidade é o fator decisivo de longevidade | Exemplos: Python "batteries included", Go com tooling embutido (`gofmt`, `go test`, `go build`), LSP criado pela Microsoft habilitando múltiplos editores | Alta |
| *Crafting Interpreters* (Robert Nystrom) é apontado como o melhor recurso introdutório gratuito — guia a construção de duas implementações completas da linguagem Lox (interpretador em Java, VM em bytecode em C) | Recomendação direta e nominal da fonte | Alta |
| LLVM como backend permite gerar IR e delegar otimização + geração de código multi-arquitetura — usado por Rust e Swift | Afirmação da fonte | Média (não detalha a API do LLVM nem o formato do IR) |

## Concepts & Entities Touched

[[wiki/concepts/compilador]] · [[wiki/concepts/pipeline-de-compilacao]] · [[wiki/concepts/sistema-de-tipos]] · [[wiki/concepts/gerenciamento-de-memoria]] · [[wiki/concepts/gramatica-formal-ebnf]] · [[wiki/concepts/language-server-protocol]] · [[wiki/concepts/standard-library-e-ecossistema]] · [[wiki/concepts/concorrencia]] · [[wiki/entities/robert-nystrom]] · [[wiki/entities/llvm]]

## Open Questions

- Nome do canal/autor não identificado na transcrição — sem URL de origem fornecida (mesma limitação já registrada em outras fontes de transcrição bruta desta wiki, ex. [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]).
- A fonte não aprofunda algoritmos concretos de garbage collection (mark-and-sweep, geracional, incremental) nem o mecanismo interno de borrow checking do Rust — candidato a fonte futura dedicada a `gerenciamento-de-memoria`.
- Não detalha a heurística de "hot path" usada por JITs reais (V8, JVM HotSpot) para decidir o que compilar nativamente.
- Complementa diretamente [[wiki/concepts/compilador]] e [[wiki/concepts/pipeline-de-compilacao]] (que cobrem o *mecanismo* lexer→parser→AST→codegen) adicionando a camada de *decisão de design* que antecede e envolve esse mecanismo — nenhuma contradição encontrada, é uma ampliação do mesmo território conceitual com foco em "por que escolher X" em vez de apenas "como X funciona".
