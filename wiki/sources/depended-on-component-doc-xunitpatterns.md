---
type: source
title: "Depended-On Component / DOC (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["DOC", "depended-on component", "componente do qual se depende", "xunit patterns glossary DOC"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/depended-on-component-doc-xunitpatterns.md
source_url: "http://xunitpatterns.com/DOC.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-23
source_count: 0
tags: [testes, test-doubles, sut, doc, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Depended-On Component / DOC (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **depended-on component (DOC)**: uma classe individual ou componente de granularidade grossa do qual o [[wiki/concepts/test-doubles|SUT]] depende, tipicamente por delegação via chamadas de método. A fonte isola o motivo pelo qual o DOC importa para automação de testes: precisamos **examinar e controlar** suas interações com o SUT para obter cobertura completa — é exatamente essa necessidade de examinar/controlar que motiva o padrão [[wiki/concepts/test-doubles|Test Double]]. Este termo já era usado extensivamente na wiki via [[wiki/sources/test-double-xunitpatterns-meszaros]] e [[wiki/sources/indirect-input-xunitpatterns]], mas agora ganha sua própria citação primária isolada, fechando o trio DOC/indirect-input junto com o vocabulário de Test Double.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| DOC é uma classe individual ou componente de granularidade grossa do qual o SUT depende | "An individual class or a large-grained component on which the system under test (SUT) depends" | fonte primária (Meszaros) | alta |
| A dependência do SUT sobre o DOC é tipicamente de delegação via chamadas de método | "The dependency is usually one of delegation via method calls" | fonte primária | alta |
| O interesse em automação de testes é poder examinar e controlar as interações do DOC com o SUT para cobertura completa | "we need to be able to examine and control its interactions with the SUT to get complete test coverage" | fonte primária | alta |

---

## Key Claims

### 1. DOC é definido pela relação de dependência, não pelo tamanho
A definição não distingue DOC por ser "pequeno" (uma classe) ou "grande" (um componente) — ambos contam, desde que o SUT dependa deles por delegação. Isso confirma que o vocabulário SUT/DOC já usado em [[wiki/concepts/test-doubles]] se aplica tanto a substituir uma única classe colaboradora quanto um subsistema inteiro (ex.: um gateway de pagamento).

### 2. "Examinar e controlar" é a motivação formal para o Test Double
A fonte conecta diretamente o DOC ao motivo de existir um double: sem a capacidade de examinar (observar) e controlar as interações do SUT com o DOC real, não há cobertura de teste completa. Esse é o mesmo par observação/controle já formalizado em [[wiki/concepts/indirect-input-output]] (ponto de controle para entrada indireta, ponto de observação para saída indireta) — aqui a fonte primária do próprio termo DOC confirma que essa é a razão de ser do conceito, não um detalhe incidental do Test Double.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]] e [[wiki/sources/indirect-input-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — DOC é o que o Test Double substitui; a definição formal do termo mais citado (e menos formalmente definido até agora) do vocabulário
- [[wiki/concepts/indirect-input-output]] — "examinar e controlar" mapeia diretamente para ponto de observação/ponto de controle
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — narrow integration test substitui justamente o DOC por um double fiel
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — "todo DOC substituído" é a definição de unit test solitário

## Questões Abertas

- Com DOC, indirect input, control point e fixture setup isolados como fontes primárias próprias (ver [[wiki/sources/control-point-xunitpatterns]] e [[wiki/sources/fixture-setup-xunitpatterns]]), restam do mesmo glossário: "indirect output", "observation point", "direct input" e "fixture teardown" — ainda conhecidos só por menção nas fontes já ingeridas ([[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/indirect-input-xunitpatterns]]). Candidatos naturais para fechar o vocabulário completo do glossário xUnitPatterns.com.

---

## Citações Relevantes

> "An individual class or a large-grained component on which the system under test (SUT) depends. The dependency is usually one of delegation via method calls."

> "In test automation, it is primarily of interest in that we need to be able to examine and control its interactions with the SUT to get complete test coverage."

*(Tradução completa em `raw/depended-on-component-doc-xunitpatterns.md`.)*
