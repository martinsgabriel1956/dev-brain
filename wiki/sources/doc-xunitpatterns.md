---
type: source
title: "DOC — Depended-On Component (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["DOC", "depended-on component", "componente do qual se depende", "xunit patterns glossary DOC"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/doc-xunitpatterns.md
source_url: "http://xunitpatterns.com/DOC.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-21
source_count: 0
tags: [testes, test-doubles, sut, doc, control-point, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# DOC — Depended-On Component (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **DOC (depended-on component)**: uma classe individual ou componente de granularidade grossa do qual o [[wiki/concepts/test-doubles|SUT]] depende, tipicamente por delegação via chamadas de método. É a metade do par SUT/DOC já usado em toda a wiki para explicar [[wiki/concepts/test-doubles|Test Doubles]] — o DOC é precisamente **o que um double substitui**. Esta fonte isola a definição formal, complementando [[wiki/sources/test-double-xunitpatterns-meszaros]] e [[wiki/sources/indirect-input-xunitpatterns]], que já usavam o termo sem uma citação primária dedicada a ele.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| DOC é uma classe ou componente de granularidade grossa do qual o SUT depende | "An individual class or a large-grained component on which the system under test (SUT) depends" | fonte primária (Meszaros) | alta |
| A dependência é tipicamente delegação via chamadas de método | "The dependency is usually one of delegation via method calls" | fonte primária | alta |
| Em automação de testes, o interesse no DOC está em examinar e controlar suas interações com o SUT para cobertura completa | "we need to be able to examine and control its interactions with the SUT to get complete test coverage" | fonte primária | alta |

---

## Key Claims

### 1. DOC é definido pela relação de dependência, não pela granularidade
Meszaros deixa explícito que o DOC pode ser "uma classe individual" ou "um componente de granularidade grossa" — ou seja, o conceito é agnóstico de escala. O que importa é a relação: o SUT depende dele. Isso reforça que a dupla SUT/DOC se aplica igualmente a um teste unitário (DOC = uma classe colaboradora) e a um teste de componente/integração (DOC = um serviço externo inteiro), consistente com o uso já feito em [[wiki/concepts/test-doubles]].

### 2. Examinar e controlar são as duas operações que motivam os Test Doubles
A frase final do verbete — "precisamos examinar e controlar suas interações com o SUT" — é, em outras palavras, o par **ponto de observação / ponto de controle** já formalizado em [[wiki/concepts/indirect-input-output]]. "Controlar" motiva o Stub (via [[wiki/sources/indirect-input-xunitpatterns]]); "examinar" motiva Spy/Mock. Este verbete curto de DOC funciona como a peça que amarra a definição do "quem" (DOC) à motivação do "por quê" (indirect input/output) já documentada.

### 3. Verbete mínimo, sem exemplo — vocabulário puro
Diferente de [[wiki/sources/test-double-xunitpatterns-meszaros]] (que traz a taxonomia completa com exemplos), este verbete de glossário é deliberadamente enxuto — duas frases, sem exemplo de código. Serve como referência rápida de definição, não como material de aprendizado por si só.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]] e [[wiki/sources/indirect-input-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — DOC é o que um Test Double substitui
- [[wiki/concepts/indirect-input-output]] — "examinar e controlar" é o mesmo eixo observação/controle já documentado ali

## Questões Abertas

- Os verbetes irmãos "control point", "observation point" e "direct input" do mesmo glossário ainda não foram ingeridos individualmente — candidatos naturais para fechar o vocabulário completo junto com [[wiki/sources/indirect-input-xunitpatterns]].

---

## Citações Relevantes

> "An individual class or a large-grained component on which the system under test (SUT) depends."

> "The dependency is usually one of delegation via method calls. In test automation, it is primarily of interest in that we need to be able to examine and control its interactions with the SUT to get complete test coverage."

*(Tradução completa em `raw/doc-xunitpatterns.md`.)*
