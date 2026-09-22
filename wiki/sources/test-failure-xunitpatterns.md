---
type: source
title: "Test Failure (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test failure", "falha de teste", "xunit patterns glossary test failure"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-failure-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20failure.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, test-failure, tdd, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Failure (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com que isola, com fonte primária dedicada, a definição do próprio termo **test failure**: ocorre quando um [[wiki/sources/test-xunitpatterns|test]] é executado e o resultado real (*actual outcome*) não corresponde ao resultado esperado (*expected outcome*). O verbete contrasta explicitamente **test failure** com **test error** e **test success** — os dois termos irmãos que [[wiki/sources/test-result-xunitpatterns]] já tinha sinalizado como lacuna, e que ainda seguem sem fonte isolada própria. Fecha metade dessa lacuna de três termos (junto com [[wiki/sources/test-run-xunitpatterns]], que já tinha fechado "test run").

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test failure ocorre quando o resultado real de um teste não bate com o esperado | "When a test is run and the actual outcome does not match the expected outcome" | fonte primária (Meszaros) | alta |
| Test failure é distinto de test error e de test success | "Contrast this with test error and test success" | fonte primária | alta |

---

## Key Claims

### 1. Test failure é definido por comparação, não por exceção
A definição não menciona exceção, crash ou erro de execução — é puramente sobre **discrepância entre resultado observado e resultado esperado**. Isso implica uma distinção formal (ainda não definida em fonte primária própria na wiki) entre **test failure** (a asserção rodou e discordou do esperado) e **test error** (algo impediu a asserção de sequer rodar, tipicamente uma exceção não tratada) — a mesma distinção que ferramentas de teste modernas (JUnit, pytest, Vitest) reportam separadamente como "failures" vs. "errors".

### 2. Test failure é o motor do ciclo RED do TDD
A definição formaliza, com fonte primária, o que [[wiki/concepts/tdd]] já descreve operacionalmente na fase **RED** do ciclo: "escreva um teste que falha — o comportamento ainda não existe". Um test failure não é um evento indesejado no TDD — é o estado inicial esperado e necessário de cada ciclo, a prova de que o teste de fato exercita um comportamento que ainda não existe (evitando o falso positivo de um teste que "passa" mesmo sem testar nada).

### 3. Fecha lacuna parcial dos termos irmãos de test result
[[wiki/sources/test-result-xunitpatterns]] listava **test success**, **test failure**, **test error** e **test run** como termos do Glossário sem verbete isolado. [[wiki/sources/test-run-xunitpatterns]] já tinha coberto "test run" (com texto idêntico ao de "test result", tratando execução e resultado como duas faces do mesmo fenômeno). Este verbete cobre "test failure" isoladamente. **test success** e **test error** seguem sem fonte isolada própria na wiki.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para os demais verbetes de Glossário ingeridos

## Conceitos Tocados

- [[wiki/concepts/tdd]] — test failure é o mecanismo formal por trás da fase RED do ciclo TDD: o teste deve falhar antes de passar, como prova de que exercita um comportamento real
- [[wiki/concepts/test-runner]] — test failure é um dos possíveis resultados que o Test Runner reporta ao final de uma execução

## Questões Abertas

- ~~**test success** e **test error** seguem sem verbete de glossário isolado na wiki~~ — **atualização 2026-09-22**: [[wiki/sources/test-success-xunitpatterns]] fechou "test success" e [[wiki/sources/test-error-xunitpatterns]] fechou "test error" (mesma série de ingests).
- ~~A fonte não formaliza a distinção entre "test failure" (asserção discordou) e "test error" (exceção impediu a asserção de rodar) — fica implícita pelo contraste mencionado, sem definição própria de "test error" ainda disponível na wiki para confirmar.~~ — **confirmado (2026-09-22)**: [[wiki/sources/test-error-xunitpatterns]] formaliza textualmente essa distinção — test error é "um erro que impede o teste de rodar até a conclusão", categoricamente diferente de test failure (asserção rodou, resultado divergiu).

---

## Citações Relevantes

> "When a test is run and the actual outcome does not match the expected outcome. Contrast this with test error and test success."

*(Tradução completa em `raw/test-failure-xunitpatterns.md`.)*
