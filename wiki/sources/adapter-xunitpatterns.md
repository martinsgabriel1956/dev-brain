---
type: source
title: "Adapter (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["adapter xunitpatterns", "external patterns adapter", "GOF adapter citation xunitpatterns"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/adapter-xunitpatterns.md
source_url: "http://xunitpatterns.com/Adapter.html"
author: "Gerard Meszaros (verbete de citação); Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides — GOF (definição original citada)"
date_published: 2011-02-09
date_ingested: 2026-09-21
source_count: 0
tags: [design-patterns, adapter, structural, gof, xunit, external-patterns, fonte-primaria]
skill: tech-mentor-backend
status: stable
---

# Adapter (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo da categoria **External Patterns** do catálogo xUnitPatterns.com — mesmo formato mínimo já visto em [[wiki/sources/decorator-xunitpatterns|Decorator]], [[wiki/sources/command-xunitpatterns|Command]] e [[wiki/sources/pluggable-behavior-xunitpatterns|Pluggable Behavior]]: citação direta da definição canônica do **[[wiki/concepts/adapter-pattern|Adapter]]** do **[[wiki/entities/gang-of-four|GOF]]** (*Design Patterns*, 1994), sem elaboração própria de Meszaros. Fecha, com fonte primária isolada em inglês, a lacuna que [[wiki/sources/test-fixture-fit-xunitpatterns|Test Fixture (Fit)]] já havia deixado em aberto: aquela fonte *aplicava* o Adapter Pattern ao conceito de "fixture" no framework Fit (o Adapter que interpreta uma tabela de dados e invoca o SUT) sem citar a definição formal do padrão em si — esta fonte fornece exatamente essa definição, no texto original do GOF.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Adapter converte a interface fornecida por um objeto para outra, esperada por um cliente | "Convert the interface provided by an object to one needed by a client." | fonte primária (Meszaros) | alta |
| Converte a interface de uma classe em outra interface que os clientes esperam, permitindo que classes com interfaces incompatíveis trabalhem juntas | "Convert the interface of a class into another interface clents [sic] expect. Adapters lets classes work together that couldn't otherwise because of incompatible interfaces." | fonte primária | alta |
| A definição citada não é formulação original de Meszaros — é atribuída diretamente ao GOF | "From [GOF]." | fonte primária (citação) | alta |

---

## Key Claims

### 1. Confirma, com fonte primária dedicada, a definição de Adapter já usada na wiki para explicar o caso do Fit
[[wiki/concepts/adapter-pattern]] já registrava, via [[wiki/sources/test-fixture-fit-xunitpatterns]], que no framework Fit "fixture" é o nome dado ao Adapter que interpreta uma tabela de dados e invoca o SUT — mas sem citar a definição formal do próprio padrão Adapter, apenas sua aplicação nomeada nesse contexto específico. Esta fonte fecha essa lacuna: fornece o texto canônico do GOF ("convert the interface of a class into another interface clients expect"), permitindo comparar a definição geral do padrão com essa aplicação específica (interpretar uma representação tabular de dados e invocá-la contra uma interface de SUT ↔ converter qualquer interface incompatível para a esperada pelo cliente).

### 2. Erro de digitação do próprio site ("clents") preservado na citação
A definição citada no site tem um erro de digitação ("clents" em vez de "clients") — mantido na citação literal desta fonte por fidelidade ao texto original, mas não propagado para a tradução em `raw/adapter-xunitpatterns.md` nem para o restante da wiki. Sinal adicional (junto com a nota de obsolescência do site) de que a página é um rascunho não revisado, não o texto final publicado no livro.

### 3. Quinta entrada da categoria External Patterns ingerida, mesmo formato mínimo e mesma nota de obsolescência
Como em [[wiki/sources/decorator-xunitpatterns]], [[wiki/sources/command-xunitpatterns]] e [[wiki/sources/pluggable-behavior-xunitpatterns]], a página é um rascunho mínimo (resumo de uma frase + definição formal + "From [GOF]") com a mesma nota do site alertando que o conteúdo "provavelmente mudou substancialmente" desde a publicação do livro em 2007. Reforça o padrão já observado: as entradas de External Patterns são citações de vocabulário emprestado, não elaborações próprias de Meszaros como as entradas de Glossary ou XUnit Basics.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete de citação, mesma fonte primária usada para toda a série de glossário/ferramentas/referências/external patterns do xUnitPatterns.com
- [[wiki/entities/gang-of-four]] — autoria original da definição citada (*Design Patterns: Elements of Reusable Object-Oriented Software*, 1994)

## Conceitos Tocados

- [[wiki/concepts/adapter-pattern]] — recebe a definição formal do GOF como fonte primária adicional, em inglês, citada diretamente; fecha a lacuna deixada pela aplicação ao Fit em [[wiki/sources/test-fixture-fit-xunitpatterns]]

## Questões Abertas

- As demais entradas da categoria "External Patterns" (Composite, Facade, Observer, Singleton, Strategy, Template Method, entre outras listadas na barra lateral) seguem majoritariamente não ingeridas — candidatas naturais para completar o panorama da categoria.
- A nota do site sobre o conteúdo ter "mudado substancialmente" não é datada nem detalhada — não há como confirmar se a definição final publicada no livro (2007) diverge da citação nesta página web (gerada em 2011).

---

## Citações Relevantes

> "Convert the interface provided by an object to one needed by a client."

> "Convert the interface of a class into another interface clents expect. Adapters lets classes work together that couldn't otherwise because of incompatible interfaces."

> "From [GOF]."

*(Tradução completa em `raw/adapter-xunitpatterns.md`.)*
