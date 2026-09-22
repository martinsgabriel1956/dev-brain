---
type: source
title: "test debt (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test debt", "dívida de teste"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: "raw/test-debt-xunitpatterns.md"
source_url: "http://xunitpatterns.com/test%20debt.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, terminologia, xunit, fonte-primaria, test-debt, glossario]
skill: tech-mentor-testing
status: stable
---

# test debt (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]], isolando a definição formal do próprio termo **test debt** que já era citado e discutido em profundidade em [[wiki/sources/developers-not-writing-tests-xunitpatterns]] (o Project Smell irmão). Meszaros situa a origem do termo: conheceu o conceito de "dívida" em suas várias formas através da lista de discussão Industrial XP, e generaliza a metáfora — dívida é "não fazer o suficiente de" algo, e sair dela exige esforço extra depois. Aplicado a testes: test debt é o que se acumula quando não escrevemos todos os testes que deveríamos ter escrito, deixando "código desprotegido" (código que pode quebrar sem que nenhum teste falhe). É a mesma definição operacional já registrada na wiki via a fonte-irmã, mas agora com uma fonte primária isolada, no padrão já usado para dezenas de outros termos do glossário deste catálogo (ver [[wiki/entities/gerard-meszaros]] → Key Sources).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| O termo "debt" (dívida), em suas várias formas, tem origem rastreável pelo autor à lista de discussão Industrial XP | "I first became aware of the concept of various kinds of debts via the Industrial XP mailing list on the Internet" | fonte primária (Meszaros) | alta |
| "Dívida" é uma metáfora genérica para "não fazer o suficiente de" algo; sair da dívida exige esforço extra no que estava sendo negligenciado | "The concept of 'debt' is a metaphor for 'not doing enough of' something. To get out of debt we need to put extra effort into the something we were not doing enough of" | fonte primária | alta |
| Test debt, especificamente, é consequência de não escrever todos os testes que deveriam ter sido escritos, resultando em código sem proteção (pode quebrar sem falha de teste) | "Test debt is what happens when we haven't been writing all the tests we should have written. As a result, we have 'unprotected code' in that the code could be broken without causing any tests to fail" | fonte primária | alta |

---

## Key Claims

### 1. Este verbete fecha, com fonte primária isolada, um termo que a wiki já documentava em profundidade via outra fonte
[[wiki/concepts/developers-not-writing-tests]] já registra "test debt" com a mesma definição operacional (consequência de não escrever testes → código desprotegido → velocidade decrescente e refatoração arriscada), citando [[wiki/sources/developers-not-writing-tests-xunitpatterns]] como fonte. Este verbete de glossário não adiciona mecanismo novo — é o padrão recorrente do catálogo de Meszaros de manter uma página de Glossary dedicada e curta para cada termo cunhado em texto corrido nas páginas de Project/Test Smells, análogo ao que já aconteceu com dezenas de outros pares (ex.: [[wiki/sources/sut-xunitpatterns]] isolando SUT, [[wiki/sources/test-xunitpatterns]] isolando "test").

### 2. "Test debt" tem duas definições concorrentes e não-idênticas na wiki: origem de Meszaros vs. uso do tech-mentor-testing
Ao carregar a skill `tech-mentor-testing` para calibrar esta ingestão, a referência `test-strategy.md` usa "Test Debt" para um conceito relacionado mas distinto: testes com ROI negativo (flaky, acoplados à implementação, lentos, redundantes) — ou seja, dívida gerada pelo *código de teste em si* ser ruim, não pela *ausência* de testes. A definição de Meszaros é sobre código de produção desprotegido por falta de cobertura; a definição da skill é sobre testes existentes que custam mais do que valem. São mecanismos de dívida diferentes que compartilham o mesmo nome — colisão terminológica que vale registrar como questão em aberto, não uma contradição a resolver por enquanto.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete

## Conceitos Tocados

- [[wiki/concepts/developers-not-writing-tests]] — já documenta o mesmo termo em profundidade; este verbete fecha a lacuna de fonte primária isolada
- [[wiki/concepts/tech-debt-como-ferramenta]] — mecanismo genérico de dívida técnica do qual test debt é caso nomeado e específico

## Questões Abertas

- **Colisão terminológica**: "test debt" segundo Meszaros (ausência de testes = código desprotegido) não é o mesmo conceito que "Test Debt" descrito em `references/test-strategy.md` da skill `tech-mentor-testing` (testes de ROI negativo — flaky, acoplados, lentos). Nenhuma fonte na wiki ainda reconcilia ou distingue os dois usos explicitamente.

---

## Citações Relevantes

> "I first became aware of the concept of various kinds of debts via the Industrial XP mailing list on the Internet. The concept of 'debt' is a metaphor for 'not doing enough of' something."

> "Test debt is what happens when we haven't been writing all the tests we should have written. As a result, we have 'unprotected code' in that the code could be broken without causing any tests to fail."

*(Tradução completa em `raw/test-debt-xunitpatterns.md`.)*
