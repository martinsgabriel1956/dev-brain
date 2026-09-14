---
type: source
title: "Annotation (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["annotation", "anotação", "xunit patterns glossary annotation"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_file: /home/nemomartins/Documentos/new/dev-study/raw/annotation-xunitpatterns.md
source_url: "http://xunitpatterns.com/annotation.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-11
source_count: 0
tags: [testes, junit, nunit, xunit, fonte-primaria, terminologia, metaprogramacao]
skill: tech-mentor-testing
status: stable
---

# Annotation (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que define **annotation**: uma forma de indicar algo sobre algo. Usa o **JUnit 4.0** como exemplo canônico — annotations marcam quais classes são [[wiki/entities/junit|Testcase Classes]] e quais métodos são Test Methods — e cita o **NUnit** como equivalente que usa **attributes** em vez de annotations. O conteúdo já estava resumido de passagem em [[wiki/entities/junit]] (linha sobre NUnit 2.0 influenciar o Java); esta ingestão dá fonte primária isolada e dedicada ao próprio termo.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Annotation é "uma forma de indicar algo sobre algo" | "A way of indicating something about something." | fonte primária (Meszaros) | alta |
| JUnit 4.0 usa annotations para marcar Testcase Classes e Test Methods | "JUnit version 4.0 uses annotations to indicate which classes are Testcase Classes and which methods are Test Methods" | fonte primária | alta |
| NUnit usa attributes com o mesmo propósito | "NUnit uses attributes" | fonte primária | alta |

---

## Key Claims

### 1. Definição deliberadamente genérica, ancorada em um exemplo concreto
O verbete não define annotation como um mecanismo de linguagem específico (não fala de reflection, metadata em bytecode, ou processamento em compile-time/runtime) — define pela **função**: sinalizar algo sobre um elemento de código. A concretização vem inteiramente do exemplo JUnit 4.0, que já era a versão em que o framework migrou de convenção de nomenclatura (métodos prefixados com `test`, herança de `TestCase`) para annotations (`@Test`, `@Before`, etc.).

### 2. Annotation (JUnit) e attribute (NUnit) são apresentados como sinônimos funcionais entre frameworks irmãos
O verbete não elabora a diferença de implementação entre annotations Java e attributes .NET — apenas registra que cumprem o mesmo papel em frameworks equivalentes da família [[wiki/concepts/tdd|Xunit]]. Isso é consistente com o já registrado em [[wiki/entities/junit]]: o uso de atributos no NUnit 2.0 antecipou, e possivelmente influenciou, a adoção de annotations pelo Java.

### 3. Fonte fecha, de forma isolada, um detalhe até agora só mencionado de passagem
Antes desta ingestão, a relação annotation↔attribute só aparecia em [[wiki/entities/junit]] e em [[wiki/sources/xunit-martin-fowler]], sempre no contexto da história de proliferação de ports do JUnit — nunca como definição própria do termo "annotation". Este verbete, apesar de mínimo, é a primeira fonte primária dedicada ao termo em si.

---

## Entidades Mencionadas

- [[wiki/entities/junit]] — exemplo canônico citado no verbete (annotations desde a versão 4.0)
- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/tdd|Xunit]] — annotation/attribute como mecanismo de marcação usado pelos frameworks da família (JUnit, NUnit)

## Questões Abertas

- O verbete não menciona se o **NUnit** já tinha página própria dedicada na wiki — não tinha, e continua sem: é citado apenas de passagem em [[wiki/entities/junit]] e nas fontes sobre a proliferação de ports do JUnit. Pendente para uma futura ingestão focada no framework.
- Não há detalhe mecânico sobre **como** annotations Java funcionam por baixo dos panos (retenção em runtime via reflection vs. só em compile-time) nem sobre a diferença de implementação entre annotations e attributes .NET — o verbete é deliberadamente genérico.

---

## Citações Relevantes

> "A way of indicating something about something. JUnit version 4.0 uses annotations to indicate which classes are Testcase Classes and which methods are Test Methods; NUnit uses attributes."

*(Tradução completa em `raw/annotation-xunitpatterns.md`.)*
