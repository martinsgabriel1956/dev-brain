---
type: source
title: "Test-First Development (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test first development xunitpatterns", "test-first glossary xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-first-development-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20first%20development.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, emergent-design]
skill: tech-mentor-testing
status: stable
---

# Test-First Development (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do xUnitPatterns.com que define formalmente **test-first development**: um processo de desenvolvimento que exige escrever e automatizar os [[wiki/concepts/tdd|unit tests]] antes que o desenvolvimento das unidades correspondentes seja iniciado, garantindo que as responsabilidades de cada unidade fiquem claras antes de serem codificadas. Fecha a lacuna deixada pela ingestão anterior de [[wiki/sources/test-driven-development-xunitpatterns]] (que só citava este termo por contraste, sem defini-lo): confirma que **test-first é o guarda-chuva genérico** — apenas exige que o teste seja escrito antes do código de produção —, enquanto [[wiki/concepts/tdd|test-driven development]] é o caso específico que também exige fazer o código funcionar **um teste de cada vez** ([[wiki/concepts/emergent-design|emergent design]]). Acrescenta um dado novo: test-first development pode ser aplicado tanto no nível de **unit test** quanto de **customer test**, dependendo de quais testes o time escolhe automatizar.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test-first é escrever/automatizar os testes antes de desenvolver a unidade correspondente | "A development process that entails writing and automating unit tests before the development of the corresponding units is started" | fonte primária (Meszaros) | alta |
| O objetivo é garantir que as responsabilidades da unidade sejam entendidas antes da codificação | "This ensures that the responsibilities of each software unit are well understood before they are coded" | fonte primária | alta |
| Test-first ≠ TDD: test-first só exige escrever o teste antes; não implica trabalhar um teste de cada vez | "Unlike test-driven development, test-first development merely says the tests are written before the production code; it does not imply that the production code is made to work one test at a time (emergent design)" | fonte primária | alta |
| Test-first pode ser aplicado no nível de unit test e/ou customer test | "Test-first development may be applied at either the unit test and/or customer test level depending on which tests we have chosen to automate" | fonte primária | alta |

---

## Key Claims

### 1. Confirma e fecha a distinção test-first vs. TDD com fonte primária direta
A ingestão anterior ([[wiki/sources/test-driven-development-xunitpatterns]]) já havia estabelecido essa distinção, mas a partir do verbete de TDD, que cita test-first apenas por contraste. Este verbete é a fonte primária direta e simétrica: confirma exatamente a mesma relação (test-first é o guarda-chuva; TDD acrescenta a exigência de [[wiki/concepts/emergent-design|emergent design]]), sem introduzir nenhuma nuance nova sobre esse ponto. Fecha, com fonte própria, a lacuna registrada como open question em [[wiki/concepts/test-first-development]] e no log da ingestão de TDD.

### 2. Dado novo: nível de aplicação — unit test vs. customer test
Esta é a única informação genuinamente nova frente ao que já estava inferido: test-first development não é exclusivo de testes de unidade — pode ser praticado também no nível de customer test (teste de aceitação/funcionalidade visível ao cliente, ver [[wiki/concepts/piramide-de-testes]] e [[wiki/sources/customer-test-xunitpatterns]]), dependendo de qual conjunto de testes o time decide automatizar antes de implementar. Isso aproxima test-first, no nível de customer test, do que a wiki já suspeitava sobre [[wiki/concepts/storytest-driven-development|storytest-driven development]] (STDD) — praticar test-first no nível de story/customer test é essencialmente a definição operacional de STDD, embora esta fonte não faça essa ligação explicitamente.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-driven-development-xunitpatterns]] e outras entradas do glossário xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/test-first-development]] — promovido de stub inferido por contraste para definição com fonte primária própria; `source_count` 1 → 2
- [[wiki/concepts/tdd]] — reforça (sem alterar) a distinção já registrada na ingestão anterior
- [[wiki/concepts/emergent-design]] — reforça a definição já existente (característica que test-first *não* exige, mas TDD sim)
- [[wiki/concepts/piramide-de-testes]] — nova conexão: test-first development pode operar no nível de customer test, não só no de unit test

## Questões Abertas

- **Conexão com storytest-driven development não confirmada por esta fonte**: test-first no nível de customer test é operacionalmente parecido com a definição suspeita de STDD em [[wiki/concepts/storytest-driven-development]], mas o verbete não faz essa ligação explícita — permanece inferência, não fonte primária confirmada.
- Sem contradição com o resto da wiki — a fonte apenas confirma e formaliza, com citação direta, o que já havia sido inferido por contraste na ingestão anterior.

---

## Citações Relevantes

> "A development process that entails writing and automating unit tests before the development of the corresponding units is started. This ensures that the responsibilities of each software unit are well understood before they are coded."

> "Unlike test-driven development, test-first development merely says the tests are written before the production code; it does not imply that the production code is made to work one test at a time (emergent design.) Test-first development may be applied at either the unit test and/or customer test level depending on which tests we have chosen to automate."

*(Tradução completa em `raw/test-first-development-xunitpatterns.md`.)*
