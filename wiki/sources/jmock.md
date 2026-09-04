---
type: source
title: "JMock (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["jmock", "JMock framework", "xunit patterns tools JMock"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/jmock.md
source_url: "http://xunitpatterns.com/JMock.html"
author: "Gerard Meszaros"
date_published: 2011-02-09
date_ingested: 2026-09-04
source_count: 0
tags: [testes, test-doubles, mock, jmock, java, xunit, ferramentas, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# JMock (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto da categoria **Tools** do catálogo xUnitPatterns.com (Gerard Meszaros) descrevendo o **[[wiki/entities/jmock|JMock]]**: um framework dinâmico de **[[wiki/concepts/test-doubles|Mock Object]]** amplamente usado em testes Java, cuja **Configuration Interface** fluente (API de especificação de expectativas via method chaining) é destacada como o diferencial que torna os testes altamente legíveis. É a primeira entrada da categoria "Tools" do site ingerida na wiki — até agora só verbetes de "Glossary" e "Test Refactorings" haviam sido cobertos — e dá um exemplo concreto para o "Configurable Test Double gerado por reflexão/proxy dinâmico" já mencionado sem fonte primária em [[wiki/sources/test-stub-xunitpatterns-meszaros]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| JMock é um framework de Mock Object dinâmico amplamente usado para testes Java | "A widely-used dynamic Mock Object framework for Java tests" | fonte primária (Meszaros) | alta |
| A Configuration Interface fluente para especificar expectativas torna os testes altamente legíveis | "The fluent Configuration Interface used for specifying the expectations makes the tests highly readable" | fonte primária | alta |

---

## Key Claims

### 1. JMock é catalogado como implementação concreta do padrão Mock Object
O verbete não define o padrão Mock Object em si (isso já está em [[wiki/sources/test-double-xunitpatterns-meszaros]]) — apenas nomeia o JMock como ferramenta que o implementa. Confirma o padrão editorial do site: a categoria "Tools" existe para ancorar os padrões abstratos do catálogo (Glossary, Test Refactorings) em software real que os desenvolvedores usam no dia a dia.

### 2. "Fluent Configuration Interface" é o diferencial citado, não a técnica de mock em si
Meszaros não elogia o JMock por "ser um framework de mock" (isso é genérico) — elogia especificamente a **API fluente** usada para configurar expectativas (method chaining que lê como prosa: `mock.expects(once()).method("charge").with(eq(250))`). Isso conecta ao termo **[[wiki/concepts/test-doubles|Configuration Interface]]** já citado de passagem em [[wiki/concepts/test-doubles]] como parte da dualidade Hard-Coded vs. Configurable Test Double — o JMock é o exemplo canônico do lado "Configurable" construído via reflexão/proxy dinâmico, não hard-coded no teste.

### 3. Verbete mínimo — remete à fonte externa para detalhes
Assim como os verbetes de glossário já ingeridos (DOC, SUT, control point), este é deliberadamente curto e remete ao site oficial (jmock.org) para aprofundamento — o xUnitPatterns.com funciona como índice/taxonomia, não como documentação de uso de cada ferramenta.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete, mesma fonte primária já usada para toda a série de glossário/refatorações do xUnitPatterns.com
- [[wiki/entities/jmock]] — a própria ferramenta descrita (nova entidade criada nesta ingestão)

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — JMock é a implementação concreta citada como exemplo do padrão Mock Object e do Configurable Test Double via Configuration Interface
- [[wiki/concepts/tdd]] — JMock é historicamente associado à escola **London/Mockist** de TDD [external]

## Questões Abertas

- O verbete não menciona os autores do JMock (Steve Freeman, Nat Pryce, Joe Walnes) nem sua ligação histórica com o livro *Growing Object-Oriented Software, Guided by Tests* e a escola London/Mockist de TDD — informação relevante mas **[external]**, não presente na fonte primária. Candidato a uma entidade dedicada a Freeman/Pryce se uma fonte primária sobre eles for ingerida no futuro.
- Outras entradas da categoria "Tools" do mesmo site (EasyMock, NMock) ainda não foram ingeridas — candidatas naturais para completar o panorama de frameworks de mock por linguagem.

---

## Citações Relevantes

> "A widely-used dynamic Mock Object framework for Java tests. The fluent Configuration Interface used for specifying the expectations makes the tests highly readable. More information can be found at the JMock website http://www.jmock.org."

*(Tradução completa em `raw/jmock.md`.)*
