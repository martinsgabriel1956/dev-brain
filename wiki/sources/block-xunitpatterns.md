---
type: source
title: "Block (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["block", "block closure", "bloco de código xunitpatterns"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/block-xunitpatterns.md
source_url: "http://xunitpatterns.com/block.html"
author: "Gerard Meszaros"
date_published: 2011-02-09
date_ingested: 2026-09-21
source_count: 0
tags: [testes, xunit, fonte-primaria, terminologia, oop, closures, smalltalk, ruby, glossary]
skill: tech-mentor-testing
status: stable
---

# Block (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que define **block** (também conhecido como *block closure*): um bloco de código executável passado como argumento para um método, que pode então rodá-lo em seu próprio contexto — mecanismo nativo de Smalltalk e Ruby. Meszaros situa três alternativas equivalentes em linguagens sem suporte direto a blocks: "anonymous inner classes" em Java e "delegates" em C#. Fecha, do lado da *closure*, o par de mecanismos de "comportamento como valor" já iniciado pelo lado do *function pointer* em [[wiki/sources/procedure-variable-xunitpatterns]] — e dá, pela primeira vez com fonte primária isolada, o vocabulário formal por trás da variação **Pluggable Block** já registrada em [[wiki/concepts/pluggable-behavior]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Block é um bloco de código que pode ser executado | "A block of code that can be run." | fonte primária (Meszaros) | alta |
| Smalltalk e Ruby usam blocks ("block closures") para passar um trecho de código a um método, que o executa em seu próprio contexto | "Many programming languages (most notably Smalltalk and Ruby) use blocks (also known as 'block closures') as a way of passing a chunk of code to a method which can then run it in its own context." | fonte primária | alta |
| Java usa "anonymous inner classes" para o mesmo efeito, sem suporte direto a blocks; C# usa "delegates" | "Java's 'anonymous inner classes' are a way to achieve the same thing without direct support for blocks. C# uses 'delegates' to achieve a similar purpose." | fonte primária | alta |

---

## Key Claims

### 1. "Block" é o termo que faltava para nomear formalmente a variação Pluggable Block
[[wiki/concepts/pluggable-behavior]] já distinguia **Pluggable (Method) Selector** de **Pluggable Block** citando [[wiki/sources/pluggable-behavior-xunitpatterns]], mas sem fonte primária isolada para o próprio termo "block" — apenas o usava de passagem ("quem cria o objeto injeta um bloco de código arbitrário"). Esta fonte fecha essa lacuna: define formalmente o que é um block (código executável passado a um método) e nomeia sua origem em Smalltalk, a mesma linguagem de onde vem *Smalltalk Best Practice Patterns* [SBPP], livro de Kent Beck que cunhou o Pluggable Behavior.

### 2. Completa o par "comportamento como valor": closure (block) vs. function pointer (procedure variable)
[[wiki/sources/procedure-variable-xunitpatterns]] já registrava o mecanismo de **function pointer/delegate** (variável que referencia código, permitindo dynamic binding) como precursor histórico do polimorfismo. Este verbete descreve o mecanismo irmão do lado das linguagens dinâmicas/funcionais: em vez de uma variável que aponta para um procedimento *nomeado* já existente, o block é um trecho de código *anônimo*, definido inline, criado no ponto de chamada — mesma motivação (passar comportamento como valor), implementação distinta (closure capturando contexto léxico vs. ponteiro para código compilado). Nota: interessantemente, a própria definição de block cita "delegates" (C#) como equivalente ao que a fonte de procedure variable já chamava assim — o vocabulário do glossário não distingue os dois verbetes por esse termo, mas por *mecanismo de linguagem* (closure vs. ponteiro).

### 3. Verbete mínimo, sem elaboração própria de Meszaros além do mapeamento entre linguagens
Como em outros verbetes curtos do Glossário (ex.: [[wiki/sources/attribute-xunitpatterns]]), o conteúdo é essencialmente um mapeamento terminológico entre linguagens (Smalltalk/Ruby → block; Java → anonymous inner class; C# → delegate), sem discussão de uso em testes especificamente. A relevância para a wiki vem inteiramente do link indireto com Pluggable Block, não de conteúdo explícito sobre xUnit neste verbete.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete, mesma fonte primária usada para toda a série de glossário do xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/pluggable-behavior]] — fonte primária isolada para o termo "block", usado na variação Pluggable Block já registrada
- [[wiki/sources/procedure-variable-xunitpatterns]] — par de mecanismos de "comportamento como valor": closure (block) vs. function pointer (procedure variable)

## Questões Abertas

- A fonte não dá exemplo de código (nem Smalltalk, nem Ruby) mostrando um block sendo passado como Pluggable Block num Testcase Object — a conexão com Pluggable Behavior é inferência da wiki a partir de [[wiki/sources/pluggable-behavior-xunitpatterns]], não afirmação explícita deste verbete.
- O termo irmão "block closure" tem verbete próprio no Glossário (visto na barra lateral desta página, `block closure.html`) e ainda não foi ingerido isoladamente — candidato natural para aprofundar a distinção entre "block" (o bloco de código) e "block closure" (o bloco capturando o contexto léxico).

---

## Citações Relevantes

> "A block of code that can be run."

> "Many programming languages (most notably Smalltalk and Ruby) use blocks (also known as 'block closures') as a way of passing a chunk of code to a method which can then run it in its own context."

> "Java's 'anonymous inner classes' are a way to achieve the same thing without direct support for blocks. C# uses 'delegates' to achieve a similar purpose."

*(Tradução completa em `raw/block-xunitpatterns.md`.)*
