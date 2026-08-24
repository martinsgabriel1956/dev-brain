---
type: source
title: "Control Point (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["control point", "ponto de controle", "xunit patterns glossary control point"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/control-point-xunitpatterns.md
source_url: "http://xunitpatterns.com/control%20point.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-23
source_count: 0
tags: [testes, test-doubles, sut, doc, control-point, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Control Point (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **control point** ("ponto de controle"): a forma como o teste pede ao [[wiki/concepts/test-doubles|SUT]] para fazer algo por ele. A definição é mais ampla do que o uso que a wiki já registrava por menção indireta — não é só o "ponto pelo fundo" usado para injetar [[wiki/concepts/indirect-input-output|indirect input]] via Stub; cobre **qualquer** interação de comando com o SUT, incluindo fixture setup/teardown e a própria chamada de **exercise SUT** (o "front door" normal). É um tipo de **interaction point**. A fonte também isola uma regra de design importante, até agora não formalizada na wiki: alguns control points existem estritamente para os testes e **não devem ser usados pelo production code**, porque contornam validação de entrada ou encurtam o ciclo de vida normal do SUT/DOC.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Control point é como o teste pede ao SUT para fazer algo — em fixture setup/teardown ou na fase de exercise SUT | "how the test asks the system under test (SUT) to do something for it" | fonte primária (Meszaros) | alta |
| Control point é um tipo de interaction point (categoria mais ampla) | "It is a kind of interaction point" | fonte primária | alta |
| Alguns control points existem só para os testes e não devem ser usados por production code, pois bypassam validação de entrada ou o ciclo de vida normal do SUT/DOC | "they should not be used by the production code because they bypass input validation or short-circuit the normal life-cycle of the SUT or some object on which it depends" | fonte primária | alta |

---

## Key Claims

### 1. Control point é mais amplo do que "injeção de indirect input" — inclui o front door
A wiki já conhecia "control point" por menção em [[wiki/sources/indirect-input-xunitpatterns]] ("control point on the back side of the SUT"), o que sugeria um conceito restrito à injeção de valores vindos de um DOC. Este verbete corrige essa impressão: a definição formal cobre **qualquer** ponto de comando — incluindo o próprio ato de chamar o método público do SUT na fase de **exercise SUT** (o "front door" normal do teste). O "back side" citado em indirect input é um **caso específico** de control point (o usado para configurar o DOC antes do teste), não a definição inteira.

### 2. Fixture setup/teardown e exercise SUT compartilham o mesmo mecanismo formal
A fonte agrupa explicitamente dois momentos do ciclo de vida do teste — configurar/desmontar a fixture e exercitar o SUT — sob o mesmo termo. Isso formaliza algo que a wiki já tratava separadamente ([[wiki/concepts/tdd]] e as fases de um teste xUnit): tanto "preparar o cenário" quanto "rodar a ação sob teste" são, tecnicamente, o teste usando um control point para comandar o SUT.

### 3. Regra de design nova: control points exclusivos de teste não devem entrar no production code
Esta é a afirmação de maior valor prático da fonte, sem equivalente explícito ainda na wiki: existem control points criados **só para viabilizar teste** (ex.: um setter de estado interno, um hook de reset) que **bypassam validação de entrada** ou **encurtam o ciclo de vida normal** do SUT/DOC. Usá-los fora do teste é um risco de design — a fonte trata isso como incorreção categórica, não como preferência de estilo.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/indirect-input-xunitpatterns]] e [[wiki/sources/depended-on-component-doc-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/indirect-input-output]] — control point definido com precisão e generalidade maior do que a menção indireta já registrada; a injeção de indirect input é um caso específico, não a definição completa
- [[wiki/concepts/test-doubles]] — control points exclusivos de teste conectam-se à mesma motivação "examinar e controlar" que justifica o Test Double
- [[wiki/concepts/tdd]] — fixture setup/teardown e exercise SUT como usos concretos de control point no ciclo de um teste

## Questões Abertas

- Restam do mesmo glossário: **"observation point"** (contraparte simétrica de control point, para saída indireta/verificação), **"direct input"** e **"fixture teardown"** — ainda conhecidos só por menção nas fontes já ingeridas. "fixture setup" já foi ingerido isoladamente em [[wiki/sources/fixture-setup-xunitpatterns]]. São os últimos candidatos para fechar o vocabulário completo do glossário xUnitPatterns.com usado nesta wiki.
- A fonte não dá exemplo concreto de um "control point exclusivo de teste que bypassa validação" (ex.: um método `_setInternalStateForTest()`) — a regra fica registrada em abstrato; um exemplo de código real seria um enriquecimento útil se aparecer em fonte futura.

---

## Citações Relevantes

> "A control point is how the test asks the system under test (SUT) to do something for it. This could be for the purpose of setting up or tearing down the fixture or it could be used during the exercise SUT phase of the test. It is a kind of interaction point."

> "Some control points are provided strictly for the tests; they should not be used by the production code because they bypass input validation or short-circuit the normal life-cycle of the SUT or some object on which it depends."

*(Tradução completa em `raw/control-point-xunitpatterns.md`.)*
