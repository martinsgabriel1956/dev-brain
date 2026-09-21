---
type: source
title: "Reflection (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["reflection", "reflexão", "xunit patterns glossary reflection"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/reflection-xunitpatterns.md
source_url: "http://xunitpatterns.com/reflection.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, xunit, fonte-primaria, terminologia, glossario, reflection]
skill: tech-mentor-testing
status: stable
---

# Reflection (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que define **reflection**: a capacidade de um programa examinar sua própria estrutura enquanto está em execução, usada com frequência em ferramentas para reduzir o trabalho de adicionar novas funcionalidades. Fecha uma lacuna de fonte primária isolada citada de passagem em três páginas já ingeridas — [[wiki/sources/testcase-object-xunitpatterns]], [[wiki/concepts/pluggable-behavior]] e [[wiki/concepts/test-method]] — todas as quais descrevem o mesmo mecanismo concreto: o método `run` de um [[wiki/concepts/testcase-object|Testcase Object]] usa reflection para localizar e invocar, pelo nome, o [[wiki/concepts/test-method|Test Method]] armazenado numa instance variable pelo construtor (Pluggable Method Selector).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Reflection é a capacidade de um programa examinar sua própria estrutura em tempo de execução | "The ability of a software program to examine it's own structure as it is executing." | fonte primária (Meszaros) | alta |
| É usada com frequência em ferramentas para reduzir o trabalho de adicionar novas funcionalidades | "This is often used in tools to make it less work to add new capabilities." | fonte primária | média — afirmação genérica, sem exemplo concreto no próprio verbete |

---

## Key Claims

### 1. Definição deliberadamente genérica, sem amarração a nenhuma linguagem específica
Diferente de outros verbetes da mesma série (por exemplo [[wiki/sources/block-xunitpatterns]], que lista equivalentes por linguagem), este não cita nenhum mecanismo concreto (`getClass()`, `typeof`, `Method.invoke`, etc.) nem nenhuma linguagem. A definição é puramente conceitual: o programa consegue "olhar para si mesmo" enquanto roda.

### 2. Fecha a lacuna de fonte primária isolada apontada em três páginas já ingeridas
[[wiki/sources/testcase-object-xunitpatterns]] listava explicitamente, em suas Questões Abertas, que "Reflection (glossário do site, `reflection.html`) é citado como o mecanismo que o método `run` usa para localizar/invocar o Test Method pelo nome — página de glossário dedicada ainda não ingerida." Esta ingestão resolve essa lacuna. O mesmo mecanismo era citado, sem fonte própria, em [[wiki/concepts/pluggable-behavior]] e [[wiki/concepts/test-method]].

### 3. Conecta-se ao segundo sentido de "attribute" só de forma indireta
[[wiki/sources/attribute-xunitpatterns]] já registrava reflection en passant como mecanismo por trás de annotations (não no verbete, mas na análise da wiki). O verbete de "reflection" em si não menciona annotation nem attribute — a ligação entre os três termos (annotation/attribute são descobertos via reflection) é inferência da wiki, não afirmação da fonte primária.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/reflection]] — novo stub criado a partir deste verbete
- [[wiki/concepts/testcase-object]] — usuário concreto do mecanismo: `run` usa reflection para invocar o Test Method pelo nome
- [[wiki/concepts/pluggable-behavior]] — a variação Pluggable (Method) Selector depende de reflection para resolver o nome guardado em runtime

## Questões Abertas

- O verbete não detalha nenhum mecanismo concreto de reflection por linguagem (Java `Method.invoke`, Ruby `send`, Smalltalk `perform:`, C# `MethodInfo.Invoke`) — candidato a aprofundamento numa fonte externa, já que o próprio catálogo não vai além da definição genérica.
- Não há menção no verbete a custo de performance ou a alternativas (ex.: geração de código, interfaces marker) — a wiki não tem ainda uma fonte que discuta os trade-offs de usar reflection num Test Runner.

---

## Citações Relevantes

> "The ability of a software program to examine it's own structure as it is executing. This is often used in tools to make it less work to add new capabilities."

*(Tradução completa em `raw/reflection-xunitpatterns.md`.)*
