---
type: source
title: "Production Bugs (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["production bugs", "bugs em produção", "lost test", "teste perdido", "missing unit test", "untested code", "untested requirement", "neverfail test"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/production-bugs-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Production%20Bugs.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, test-smell, project-smell, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Production Bugs (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Test smell de categoria "Project Smell" do catálogo xUnitPatterns.com: bugs demais aparecem em teste formal ou em **produção**, apesar do esforço investido em testes automatizados. A fonte é uma árvore de causas, não uma causa única — **Infrequently Run Tests** (testes rodados com pouca frequência) e **Untested Code** (código não testado) são as duas raízes; a segunda se ramifica em **Missing Unit Test** e **Lost Test**. A partir daí a página detalha, com sintomas/causa raiz/solução para cada uma, cinco sub-causas irmãs: **Lost Test**, **Missing Unit Test**, **Untested Code**, **Untested Requirement** e **Neverfail Test**. É a primeira fonte da wiki que nomeia formalmente por que testes que existem param de rodar (Lost Test) e por que testes que rodam não capturam bugs mesmo passando (Untested Requirement, Neverfail Test) — três modos de falha distintos que costumavam ficar implícitos em [[wiki/concepts/test-discovery]] e [[wiki/concepts/erratic-test]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Bugs em produção têm duas causas-raiz: Infrequently Run Tests ou Untested Code; a segunda se divide em Missing Unit Test e Lost Test | "They can be caused Infrequently Run Tests or by Untested Code. The latter can be cause by Missing Unit Tests or Lost Tests" | fonte primária (Meszaros) | alta |
| Lost Test ocorre quando um Test Method ou Testcase Class foi desabilitado ou nunca foi adicionado à AllTests Suite | "Lost Tests can be caused by either a Test Method or a Testcase Class that has been disabled or has never been added to the AllTests Suite" | fonte primária | alta |
| Untested Requirement ocorre quando o SUT tem indirect outputs (efeitos colaterais) que não são observados diretamente pelo teste | "It may have expected 'side effects' that cannot be directly observed directly by the test [...] We call these side effects indirect outputs" | fonte primária | alta |
| Neverfail Test é frequentemente causado por asserções mal codificadas ou por falhas em thread assíncrona que o Test Runner não enxerga | "This can be caused by improperly coded assertions [...] When we have asynchronous tests, failures thrown in the other thread or process may not be seen or reported by the Test Runner" | fonte primária | alta |
| A solução recomendada contra Lost Test é comparar a contagem de testes antes/depois do check-in, além de configurar o CI para falhar acima de um limiar de testes ignorados | "We can compare the number of tests we have after check-in with the number that existed in the code branch immediately before [...] configure our continuous integration tool to fail the build if the number of tests 'ignored' is above a certain threshold" | fonte primária | alta |

---

## Key Claims

### 1. "Lost Test" formaliza um modo de falha que a wiki só tinha implícito
[[wiki/concepts/test-discovery]] já registrava, por fonte primária dedicada, os dois mecanismos de montagem de suíte (Discovery automático vs. Enumeration manual) e listava várias formas de esquecer de registrar um teste. Esta fonte nomeia formalmente o *sintoma* resultante — **Lost Test**: a contagem de testes cai ou não cresce como esperado, e só se descobre ao investigar um bug que "deveria" ter sido pego. A causa raiz aqui é dupla: testes nunca chegam a rodar (esquecimento na fase de escrita/registro) **ou** testes que rodavam foram desabilitados (renomeação que quebra a convenção de Test Discovery, atributo `[Ignore]`, código de registro comentado/apagado) — tipicamente quando alguém desabilita um teste falhando para "destravar" o build e esquece de reabilitá-lo depois.

### 2. Untested Requirement é distinto de Untested Code — a diferença é onde mora a lacuna
*Untested Code* é sobre caminhos de código que o SUT tem mas que nenhum teste exercita (tipicamente porque não se consegue controlar os **indirect inputs** de um depended-on component — ver [[wiki/concepts/indirect-input-output]]). *Untested Requirement* é o espelho do lado da saída: o SUT tem comportamento correto ou incorreto que nenhum teste consegue *observar*, porque esse comportamento se manifesta como **indirect output** (efeito colateral — grava um arquivo, chama outro objeto) e não como valor de retorno. A fonte dá um exemplo concreto e citável: um teste que verifica `removeFlight()` mas nunca verifica se o log foi escrito corretamente — o código tem um bug real (`logMessage("CreateFlight", ...)` em vez de `"RemoveFlight"`) que passa despercebido porque nenhuma asserção olha para o log. A solução apontada é **Behavior Verification** via **Mock Objects** — ligação direta com a taxonomia de [[wiki/entities/gerard-meszaros]] já registrada em [[wiki/concepts/test-doubles]].

### 3. Neverfail Test é o oposto simétrico de Lost Test — e tem uma causa "mais sinistra" que engano de sintaxe
Um teste "never fails" não é apenas um teste mal escrito (`assertTrue` chamado com a assinatura errada em vez de `assertEquals`); a fonte destaca especificamente **asynchronous tests** como causa sistêmica: falhas lançadas em outra thread ou processo podem simplesmente não ser vistas pelo [[wiki/concepts/test-runner|Test Runner]]. A solução apontada — refatorar para **Humble Executable** (variação de **Humble Object**) — é a mesma família de padrão de design-for-testability já mencionada de passagem em fontes anteriores do cluster, agora com um motivo concreto de por que ela importa para confiabilidade de teste, não só para cobertura.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros verbetes
- [[wiki/entities/nunit]] — citado como exemplo concreto do atributo `[Ignore]` usado para desabilitar um Test Method
- [[wiki/entities/junit]] — citado indiretamente via convenção de nomenclatura "test..." para Test Discovery

## Conceitos Tocados

- [[wiki/concepts/test-discovery]] — Lost Test é o sintoma que ocorre quando os mecanismos de Test Discovery/Enumeration falham silenciosamente
- [[wiki/concepts/test-suite-object]] — AllTests Suite / Suite of Suites são os pontos de falha citados nas causas de Lost Test
- [[wiki/concepts/erratic-test]] — Chained Tests (forma deliberada de Interacting Tests) dificulta a solução de isolar e rodar um único teste
- [[wiki/concepts/code-smells]] — Production Bugs é classificado como "Project Smell" na mesma taxonomia de smells do catálogo
- [[wiki/concepts/ci-cd]] — solução recomendada envolve configurar o CI para falhar acima de um limiar de testes ignorados
- [[wiki/concepts/test-doubles]] — Behavior Verification via Mock Objects é a solução apontada para Untested Requirement
- [[wiki/concepts/indirect-input-output]] — Untested Code (indirect input não controlado) e Untested Requirement (indirect output não observado) são as duas faces desse conceito

## Questões Abertas

- **Chained Tests** ainda não tem página própria na wiki, apenas citado de passagem aqui e em fontes anteriores — candidato a stub futuro.
- **Humble Object / Humble Executable** segue sem página dedicada, citado como solução para Neverfail Test — mesma lacuna teria valor para consultas futuras sobre design-for-testability.
- A fonte não detalha **Test Selection** nem **Smoke Test** além de mencioná-los de passagem — potencial ponto de expansão se uma fonte futura os detalhar.

---

## Citações Relevantes

> "Lost Tests can be caused by either a Test Method or a Testcase Class that has been disabled or has never been added to the AllTests Suite."

> "It may have expected 'side effects' that cannot be directly observed directly by the test (such as writing out a file or record or calling a method on another object or component.) We call these side effects indirect outputs."

> "When we have asynchronous tests, failures thrown in the other thread or process may not be seen or reported by the Test Runner."

*(Tradução completa em `raw/production-bugs-xunitpatterns.md`.)*
