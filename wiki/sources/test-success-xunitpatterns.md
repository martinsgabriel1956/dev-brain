---
type: source
title: "Test Success (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test success", "sucesso de teste", "xunit patterns glossary test success"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-success-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20success.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, test-success, tdd, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Success (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com que isola, com fonte primária dedicada, a definição do próprio termo **test success**: ocorre quando um [[wiki/sources/test-xunitpatterns|test]] é executado e **todos** os resultados reais (*actual outcomes*) correspondem aos resultados esperados (*expected outcomes*). É o par simétrico exato de [[wiki/sources/test-failure-xunitpatterns]] — mesma estrutura de definição, mesmo contraste cruzado (cada verbete cita os outros dois). Com este verbete, fecham-se **dois dos três** termos irmãos que [[wiki/sources/test-result-xunitpatterns]] tinha sinalizado como lacuna; resta apenas **test error** sem fonte isolada.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test success ocorre quando **todos** os resultados reais de um teste batem com os esperados | "A test is run and all actual outcomes match the expected outcomes" | fonte primária (Meszaros) | alta |
| Test success é distinto de test failure e de test error | "Contrast this with test failure and test error" | fonte primária | alta |

---

## Key Claims

### 1. "Todos" é a palavra que diferencia test success de "não-failure"
A definição de [[wiki/sources/test-failure-xunitpatterns]] fala de discrepância em geral; esta define sucesso como correspondência **total** — "**all** actual outcomes match". Isso implica que um teste com múltiplas asserções só é test success se **cada uma** delas passar; uma única asserção discordante já basta para deixar de ser test success (torna-se test failure, por definição de contraste). A fonte não formaliza o caso de execução parcial (algumas asserções nunca chegam a rodar por causa de um erro anterior) — esse caso cai melhor sob **test error**, ainda sem fonte isolada.

### 2. Test success é o motor do ciclo GREEN do TDD
Assim como [[wiki/sources/test-failure-xunitpatterns]] formaliza a fase RED, este verbete formaliza a fase **GREEN** de [[wiki/concepts/tdd]]: "escreva o mínimo de código para o teste passar". Test success não é apenas "ausência de falha" — é a condição positiva de parada de cada iteração do ciclo, o sinal para avançar para REFACTOR.

### 3. Fecha a segunda de três lacunas de termos irmãos
[[wiki/sources/test-result-xunitpatterns]] listava **test success**, **test failure**, **test error** e **test run** como termos do Glossário sem verbete isolado. [[wiki/sources/test-run-xunitpatterns]] fechou "test run"; [[wiki/sources/test-failure-xunitpatterns]] fechou "test failure"; este verbete fecha **test success**. Resta apenas **test error** — o único que não define diretamente um resultado (sucesso/falha), mas uma falha do próprio mecanismo de verificação (ex.: exceção não tratada) antes mesmo de a asserção rodar.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para os demais verbetes de Glossário ingeridos

## Conceitos Tocados

- [[wiki/concepts/tdd]] — test success é o mecanismo formal por trás da fase GREEN do ciclo TDD: condição de parada de cada iteração antes do refactor
- [[wiki/concepts/test-runner]] — test success é o outro dos possíveis resultados (par de test failure) que o Test Runner reporta ao final de uma execução

## Questões Abertas

- ~~**test error** segue sem verbete de glossário isolado na wiki — é o único termo restante do quarteto original (test success, test failure, test error, test run) sinalizado em [[wiki/sources/test-result-xunitpatterns]].~~ — **resolvido (2026-09-22)**: [[wiki/sources/test-error-xunitpatterns]] fecha o quarteto completo.
- ~~A fonte não trata o caso de execução parcial (asserções que nunca rodam por erro anterior) — provavelmente cai sob "test error", mas isso permanece inferência da wiki, não afirmação da fonte primária.~~ — **confirmado (2026-09-22)**: [[wiki/sources/test-error-xunitpatterns]] confirma textualmente que um erro "impede o teste de rodar até a conclusão" — a categoria correta para execução interrompida antes da asserção completar.

---

## Citações Relevantes

> "A test is run and all actual outcomes match the expected outcomes. Contrast this with test failure and test error."

*(Tradução completa em `raw/test-success-xunitpatterns.md`.)*
