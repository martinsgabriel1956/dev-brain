---
type: source
title: "Fixture Setup (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["fixture setup", "test fixture", "test context", "configuração de fixture"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/fixture-setup-xunitpatterns.md
source_url: "http://xunitpatterns.com/fixture%20setup.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-23
source_count: 0
tags: [testes, test-doubles, sut, fixture, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Fixture Setup (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **fixture setup**: a fase do teste em que as precondições necessárias para o [[wiki/concepts/test-doubles|SUT]] ser exercitado são configuradas. A fonte também fixa dois termos irmãos usados em toda a wiki sem definição própria até agora — **test fixture** e seu sinônimo **test context** —, definidos como o conjunto coletivo de todos os objetos (e seu estado) que essa fase estabelece.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Fixture setup é a fase que configura as precondições do teste, necessária antes do SUT poder ser exercitado | "Before the desired logic of the system under test (SUT) can be exercised, the preconditions of the test need to be setup" | fonte primária (Meszaros) | alta |
| Test fixture (ou test context) é o conjunto coletivo de todos os objetos e seu estado configurados nessa fase | "Collectively, all the objects (and their state) is called the test fixture (or test context)" | fonte primária | alta |
| "Fixture setup" nomeia a fase; "test fixture"/"test context" nomeia o resultado dela | "the phase of the test that sets it up is called fixture setup" | fonte primária | alta |

---

## Key Claims

### 1. Fixture setup é uma fase, test fixture é o seu produto
A fonte separa com precisão dois termos que a wiki já usava de forma intercambiável por inferência: **fixture setup** é o verbo — a fase executada em sequência antes de exercitar o SUT; **test fixture** (ou **test context**) é o substantivo — o conjunto de objetos e estado que essa fase deixa pronto. Sem essa fonte, a wiki conhecia "test fixture" apenas por menção lateral em outras páginas do mesmo glossário (ex.: [[wiki/sources/control-point-xunitpatterns]] cita "setting up or tearing down the fixture"), sem uma definição própria e citável.

### 2. Fixture setup é o palco onde control points e Test Doubles entram em cena
A fonte primária isolada de "control point" ([[wiki/sources/control-point-xunitpatterns]]) já registrava que control points são usados "for the purpose of setting up or tearing down the fixture" — este verbete formaliza o outro lado dessa relação: é durante a fixture setup que o teste usa esses pontos de controle, tipicamente via [[wiki/concepts/test-doubles|Test Double]], para colocar o SUT e seus DOCs no estado ("the 'before' picture") necessário para o comportamento esperado ser observável.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/control-point-xunitpatterns]], [[wiki/sources/depended-on-component-doc-xunitpatterns]] e [[wiki/sources/indirect-input-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/tdd]] — fixture setup como a primeira fase do Four-Phase Test, precondição para o ciclo RED-GREEN-REFACTOR poder exercitar o SUT
- [[wiki/concepts/test-doubles]] — Test Double como o mecanismo típico usado durante a fixture setup para colocar DOCs no estado necessário
- [[wiki/concepts/indirect-input-output]] — fixture setup como o momento em que control points (já definidos nesse conceito) são efetivamente usados

## Questões Abertas

- Restam do mesmo glossário: **"fixture teardown"** (contraparte simétrica, ainda conhecida só por menção em [[wiki/sources/control-point-xunitpatterns]]), **"observation point"** e **"direct input"** — últimos candidatos para fechar o vocabulário completo do glossário xUnitPatterns.com usado nesta wiki.
- A fonte não detalha as "Fixture Setup Patterns" (categoria própria listada no menu do site, ex.: Inline Setup, Implicit Setup, Delegated Setup) — apenas o verbete de glossário do termo em si. Candidato a ingestão futura se o objetivo for cobrir as técnicas concretas de implementação, não só a terminologia.

---

## Citações Relevantes

> "Before the desired logic of the system under test (SUT) can be exercised, the preconditions of the test need to be setup. Collectively, all the objects (and their state) is called the test fixture (or test context) and the phase of the test that sets it up is called fixture setup."

*(Tradução completa em `raw/fixture-setup-xunitpatterns.md`.)*
