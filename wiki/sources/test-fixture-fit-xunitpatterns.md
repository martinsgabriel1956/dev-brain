---
type: source
title: "Test Fixture (Fit) (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["fixture (Fit)", "Fit fixture", "test fixture (disambiguation)", "xunit patterns glossary test fixture Fit"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-fixture-fit-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20fixture%20-%20FIT.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, fit, adapter, data-driven-test, sut, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Fixture (Fit) (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário curtíssimo do catálogo xUnitPatterns.com que isola o **terceiro sentido** distinto da palavra "fixture" no vocabulário de testes — depois de (1) [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] (o nome que VbUnit/NUnit dão à classe) e (2) [[wiki/sources/test-fixture-xunitpatterns|test fixture/test context]] (as precondições do teste em xUnit). No framework **[[wiki/entities/fit|Fit]]**, "fixture" é o **[[wiki/concepts/adapter-pattern|Adapter]]** [GOF] que interpreta a tabela do Fit e invoca métodos no **[[wiki/sources/sut-xunitpatterns|SUT]]**, implementando assim um **[[wiki/concepts/data-driven-test|Data-Driven Test]]**. Esta fonte fecha a lacuna citada de passagem tanto em [[wiki/sources/testcase-class-xunitpatterns]] ("Neither should it be confused with the fixture term as used by the Fit framework...") quanto em [[wiki/sources/test-fixture-xunitpatterns]] (que remetia a este mesmo verbete de desambiguação sem o ingerir).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| No Fit, "fixture" é o Adapter [GOF] que interpreta a tabela do Fit | "In Fit, 'fixture' is what we call the Adapter[GOF] that interprets the Fit table" | fonte primária (Meszaros) | alta |
| Esse Adapter invoca métodos no SUT | "...and invokes methods on the system under test (SUT)" | fonte primária | alta |
| Isso implementa um Data-Driven Test | "...thereby implementing a Data-Driven Test" | fonte primária | alta |
| A palavra "fixture" tem outros sentidos em outros contextos, remetidos por links de desambiguação | "For meanings in other contexts, please see test fixture (disambiguation), test fixture (in xUnit) and test fixture (in NUnit)" | fonte primária | alta |

---

## Key Claims

### 1. Terceiro sentido formal de "fixture" na taxonomia da wiki: nem Testcase Class, nem test context — um Adapter concreto
Com esta fonte, a wiki agora tem os três sentidos de "fixture" citados por Meszaros com fonte primária isolada cada um: **Testcase Class** ([[wiki/sources/testcase-class-xunitpatterns]], nome usado por VbUnit/NUnit), **test context** ([[wiki/sources/test-fixture-xunitpatterns]], as precondições do Four-Phase Test) e agora **o Adapter do Fit** (este verbete). Os três são coisas estruturalmente diferentes — uma classe, um conjunto de precondições, e um objeto Adapter — que só compartilham o nome.

### 2. O fixture do Fit é definido por sua função dupla: interpretar dados + invocar o SUT
A definição amarra dois padrões GOF num só papel: o fixture é um **Adapter** (traduz a representação tabular do Fit para chamadas de método reais) cujo efeito colateral é produzir um **Data-Driven Test** — um teste cujo comportamento é guiado por dados externos (a tabela), não por código escrito à mão para cada caso. Isso é uma aplicação concreta e nomeada do [[wiki/concepts/adapter-pattern]] já documentado na wiki, mas com um propósito específico (dirigir testes por dados) que os exemplos anteriores do Adapter na wiki não cobriam.

### 3. Fecha uma lacuna dupla, citada em duas fontes anteriores da mesma série
[[wiki/sources/testcase-class-xunitpatterns]] já citava esta definição quase palavra por palavra ao explicar por que "fixture" não deve ser confundido com Testcase Class; [[wiki/sources/test-fixture-xunitpatterns]] remetia a este mesmo verbete como "não ingerido; fora do escopo desta sessão". Esta fonte formaliza, com citação primária dedicada, o que antes só existia por citação indireta em outras duas páginas.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para toda a série xUnitPatterns.com
- [[wiki/entities/fit]] — primeira fonte primária isolada dedicada, ainda que indiretamente (o verbete é sobre "fixture", não sobre o Fit em si), ao framework Fit

## Conceitos Tocados

- [[wiki/concepts/adapter-pattern]] — o fixture do Fit é citado como aplicação nomeada e concreta do Adapter [GOF], com propósito específico (interpretar tabela de dados e invocar o SUT)
- [[wiki/concepts/data-driven-test]] — novo conceito: teste cujo comportamento é guiado por uma fonte externa de dados (a tabela do Fit), e não por asserções escritas à mão caso a caso

## Questões Abertas

- **Fit em si (o framework)** não tem verbete de glossário próprio no catálogo xUnitPatterns.com — apenas citado de passagem em verbetes sobre outros termos ("Testcase Class", este). A página `FIT.html` linkada aqui (`<a href='FIT.html' class='GlossaryRef'>Fit</a>`) não foi ingerida nesta sessão; candidata natural para a próxima ingestão, e resolveria a lacuna de fonte primária dedicada ao próprio Fit, hoje registrada apenas como stub em [[wiki/entities/fit]].
- **Data-Driven Test** e **Interpreter [GOF]** (citado por Meszaros como o padrão que o Data-Driven Test implementa) seguem sem página/fonte primária dedicada própria — esta fonte cria o stub de conceito para Data-Driven Test, mas sem uma fonte primária isolada que o defina (a definição vem por composição: Adapter + tabela = Data-Driven Test).
- As páginas "test fixture (in xUnit)" e "test fixture (in NUnit)", citadas nos links de desambiguação deste verbete, já foram ingeridas ([[wiki/sources/test-fixture-xunitpatterns]] cobre o sentido xUnit; o sentido NUnit está coberto por [[wiki/sources/testcase-class-xunitpatterns]], que registra que NUnit chama a própria Testcase Class de "test fixture") — nenhuma lacuna nova aberta por esses dois links.

---

## Citações Relevantes

> "In Fit, 'fixture' is what we call the Adapter[GOF] that interprets the Fit table and invokes methods on the system under test (SUT) thereby implementing a Data-Driven Test."

> "For meanings in other contexts, please see test fixture (disambiguation), test fixture (in xUnit) and test fixture (in NUnit)."

*(Tradução completa em `raw/test-fixture-fit-xunitpatterns.md`.)*
