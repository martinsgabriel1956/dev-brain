---
type: source
title: "Test Error (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test error", "erro de teste", "xunit patterns glossary test error"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-error-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20error.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, test-error, xunit, fonte-primaria, terminologia, defect-localization]
skill: tech-mentor-testing
status: stable
---

# Test Error (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com que isola, com fonte primária dedicada, a definição do próprio termo **test error**: ocorre quando um [[wiki/sources/test-xunitpatterns|test]] é executado e um erro acontece que o impede de rodar até a conclusão — levantado explicitamente pelo [[wiki/sources/sut-xunitpatterns|SUT]] ou pelo próprio teste, ou lançado pelo runtime (SO, VM, etc.). Diferente de [[wiki/sources/test-failure-xunitpatterns]] e [[wiki/sources/test-success-xunitpatterns]], que definem *resultados* de uma asserção que rodou até o fim, **test error** define a falha do próprio mecanismo de execução — a asserção nunca chega a ser avaliada. Com este verbete, **fecham-se os quatro termos irmãos** sinalizados desde [[wiki/sources/test-result-xunitpatterns]]: test run, test result, test failure, test success e test error.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test error ocorre quando um erro impede o teste de rodar até a conclusão | "an error occurs that keeps it from running to completion" | fonte primária (Meszaros) | alta |
| O erro pode vir do SUT, do próprio teste, ou do runtime (SO, VM) | "may be explicitly raised or thrown by the SUT or by the test itself, or it may be thrown by the runtime system" | fonte primária | alta |
| Test error é mais fácil de depurar que test failure, porque a causa tende a ser mais local ao ponto onde ocorre | "it is much easier to debug a test error than a test failure because the cause of the problem tends to be much more local" | fonte primária | alta |
| Test error é distinto de test failure e de test success | "Contrast this with test failure and test success" | fonte primária | alta |

---

## Key Claims

### 1. Test error é falha do mecanismo, não do resultado
[[wiki/sources/test-failure-xunitpatterns]] e [[wiki/sources/test-success-xunitpatterns]] pressupõem que a asserção rodou até o fim — a diferença entre elas é se o resultado real bateu com o esperado. **Test error** é categoricamente diferente: algo (uma exceção não tratada, um erro de runtime) interrompe a execução *antes* de a asserção sequer poder ser avaliada. É exatamente a distinção que [[wiki/sources/test-failure-xunitpatterns]] já tinha inferido sem fonte própria — agora confirmada textualmente pela fonte primária: "an error occurs that keeps it from running to completion" versus "the actual outcome does not match the expected outcome".

### 2. Localidade da causa é o critério que a fonte usa para comparar as duas categorias
A fonte não apenas define test error — afirma algo operacional sobre ele: é **mais fácil depurar** que test failure, porque a causa "tende a ser muito mais local ao ponto onde o test error ocorre" (ex.: stack trace aponta a linha exata da exceção). Uma test failure, por contraste, exige raciocinar sobre *por que* o valor observado diverge do esperado — a causa pode estar várias camadas de código antes do ponto onde a asserção falhou. Essa é a primeira vez, na wiki, que a fonte primária do Glossário faz uma afirmação comparativa sobre dificuldade de depuração entre dois termos, e conecta diretamente ao conceito de **Defect Localization** já nomeado em [[wiki/concepts/frequent-debugging]].

### 3. Fecha a última lacuna do quarteto de termos irmãos
[[wiki/sources/test-result-xunitpatterns]] listava **test success**, **test failure**, **test error** e **test run** como termos do Glossário sem verbete isolado. [[wiki/sources/test-run-xunitpatterns]] fechou "test run"; [[wiki/sources/test-failure-xunitpatterns]] fechou "test failure"; [[wiki/sources/test-success-xunitpatterns]] fechou "test success"; este verbete fecha **test error** — o último e único que não define um resultado de asserção (sucesso/falha), mas uma falha do próprio mecanismo de verificação antes mesmo de a asserção rodar.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para os demais verbetes de Glossário ingeridos

## Conceitos Tocados

- [[wiki/concepts/frequent-debugging]] — a afirmação central da fonte (test error é mais fácil de depurar por ter causa mais local) é uma instância direta do conceito de **Defect Localization** já nomeado nesta página: quanto mais local a causa, menor o Defect Localization necessário para achá-la
- [[wiki/concepts/tdd]] — test error não mapeia limpo para nenhuma das fases RED/GREEN (que pressupõem asserção avaliada); é a interrupção que impede o ciclo de sequer chegar a um veredito RED ou GREEN
- [[wiki/concepts/test-runner]] — test error é o terceiro dos três resultados possíveis (junto com test failure e test success) que o Test Runner reporta ao final de uma execução

## Questões Abertas

- ~~**test error** segue sem verbete de glossário isolado na wiki~~ — **resolvido nesta ingestão**: fecha a última lacuna do quarteto sinalizado desde [[wiki/sources/test-result-xunitpatterns]] (test run, test result, test failure, test success, test error — todos com fonte primária isolada agora).
- A fonte não formaliza se um test error interrompe apenas o teste individual ou também os testes subsequentes da mesma test suite (ex.: erro de fixture setup compartilhado) — fica implícito que o escopo é por teste, sem confirmação textual.

---

## Citações Relevantes

> "When a test is run and an error occurs that keeps it from running to completion. The error may be explicitly raised or thrown by the SUT or by the test itself, or it may be thrown by the runtime system (operating system, virtual machine, etc..) In general, it is much easier to debug a test error than a test failure because the cause of the problem tends to be much more local to where the test error occurs. Contrast this with test failure and test success."

*(Tradução completa em `raw/test-error-xunitpatterns.md`.)*
