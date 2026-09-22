---
type: source
title: "Test Result (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test result", "resultado de teste", "xunit patterns glossary test result"]
date_created: 2026-09-21
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-result-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20result.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, test-result, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Result (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com que isola, com fonte primária dedicada, a definição do próprio termo **test result**. A definição é minimalista mas carrega uma implicação estrutural relevante: um [[wiki/sources/test-xunitpatterns|test]] ou uma [[wiki/sources/test-suite-xunitpatterns|test suite]] "pode ser executado muitas vezes, cada uma com um test result diferente" — ou seja, o resultado não é uma propriedade fixa do teste, mas um artefato efêmero de cada **[[wiki/concepts/test-suite-object|execução]]** individual. É a primeira fonte primária isolada da wiki para o vocabulário de resultado/execução, área até agora só tocada indiretamente pela prática do "red bar/green bar" documentada em [[wiki/entities/c3-project]] e [[wiki/entities/junit]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Um test ou test suite pode ser executado muitas vezes | "A test or test suite can be run many times" | fonte primária (Meszaros) | alta |
| Cada execução produz um test result próprio, distinto das demais | "each with a different test result" | fonte primária | alta |

---

## Key Claims

### 1. Test result não é atributo do teste, é atributo da execução
A frase "each with a different test result" implica que o mesmo test ou test suite, sem alteração de código, pode produzir test results diferentes em execuções diferentes (ex.: passou hoje, falhou amanhã). Isso é consistente com o vocabulário de [[wiki/concepts/test-suite-object|Test Suite Object]] já ingerido: o teste (código) é uma coisa fixa; o resultado é um produto transitório de cada rodada do [[wiki/concepts/test-runner|Test Runner]] sobre esse código.

### 2. O verbete generaliza test e test suite sob o mesmo conceito de resultado
A definição trata "test" e "test suite" como igualmente sujeitos a ter um "test result" — não introduz um termo separado para "resultado agregado de uma suíte" vs. "resultado de um teste individual". Isso sugere que o catálogo usa "test result" como termo guarda-chuva, deixando a granularidade (indivídual vs. agregada) implícita pelo contexto, sem uma taxonomia formal própria no Glossário.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para os demais verbetes de Glossário ingeridos
- [[wiki/entities/junit]] — prática histórica do "red bar/green bar" (ver [[wiki/entities/c3-project]]) é a manifestação visual mais conhecida, na wiki, do conceito formalizado aqui: cada execução produz um resultado (verde/vermelho) que pode variar de rodada para rodada

## Conceitos Tocados

- [[wiki/concepts/test-suite-object]] — o test result é o produto de cada execução do Test Suite Object pelo Test Runner, não uma propriedade fixa do objeto em si

## Questões Abertas

- ~~O Glossário do site lista termos irmãos ainda não ingeridos que provavelmente refinam este conceito — **test success**, **test failure**, **test error** e **test run** aparecem no índice de Glossário do site, mas nenhum tem verbete isolado na wiki ainda~~ — **resolvido (2026-09-22)**: [[wiki/sources/test-run-xunitpatterns]] fechou "test run" (texto idêntico, palavra por palavra, a este verbete — o catálogo trata "test run" e "test result" como duas faces do mesmo fenômeno). [[wiki/sources/test-failure-xunitpatterns]] fechou "test failure" e [[wiki/sources/test-success-xunitpatterns]] fechou "test success" (par simétrico de definições). [[wiki/sources/test-error-xunitpatterns]] fechou o último termo, "test error" — falha do mecanismo de execução, não do resultado. Os quatro termos irmãos do quarteto original estão agora todos com fonte primária isolada na wiki.
- A fonte não formaliza se "test result" agregado de uma suíte é uma simples lista de resultados individuais ou um objeto com semântica própria (ex.: "N passaram, M falharam") — deixado implícito.

---

## Citações Relevantes

> "A test or test suite can be run many times, each with a different test result."

*(Tradução completa em `raw/test-result-xunitpatterns.md`.)*
