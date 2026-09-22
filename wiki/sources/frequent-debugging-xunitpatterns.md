---
type: source
title: "Frequent Debugging (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["frequent debugging", "manual debugging", "depuração manual", "depuração frequente"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: "raw/frequent-debugging-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Frequent%20Debugging.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, test-smell, behavior-smell, xunit, fonte-primaria, terminologia, tdd, defect-localization]
skill: tech-mentor-testing
status: stable
---

# Frequent Debugging (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Test smell de categoria "Behavior Smells" do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]] — primeira fonte da wiki dessa terceira subcategoria de Test Smells (as outras duas já documentadas são Code Smells, com [[wiki/sources/hard-to-test-code-xunitpatterns]], e Project Smells, com [[wiki/sources/production-bugs-xunitpatterns]] e [[wiki/sources/developers-not-writing-tests-xunitpatterns]]). *Frequent Debugging* (a.k.a. Manual Debugging) descreve o sintoma de precisar de um debugger interativo ou prints para entender a maioria das falhas de teste — sinal de que a suíte carece de **Defect Localization**: os testes que falham não dizem, por si só, o que quebrou. Duas causas raiz nomeadas: (1) faltam unit tests ou component tests granulares o bastante para isolar o erro (agravado quando Mock Objects substituem depended-on objects mas seus unit tests não batem com o comportamento programado nos mocks), e (2) **Infrequently Run Tests** — já documentado como sub-causa de [[wiki/concepts/production-bugs|Production Bugs]] — porque rodar os testes a cada pequena mudança preserva a memória de "o que mudei desde a última execução". A solução central, citada explicitamente, é **test-driven development** verdadeiro (não apenas test-first) combinado com **storytest-driven development** para também cobrir a camada de component tests.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Frequent Debugging é causado pela falta de Defect Localization: os testes que falham deveriam indicar o problema por si (mensagem de falha ou padrão de falhas), e quando não indicam, exige-se depuração manual | "*Frequent Debugging* is caused by a lack of Defect Localization [...] The failed tests should tell us what went wrong either through their individual failure messages [...] or through the pattern of test failures" | fonte primária (Meszaros) | alta |
| Falta de component tests para um cluster de classes, especialmente quando Mock Objects substituem depended-on objects mas os unit tests desses objetos não correspondem ao comportamento programado nos mocks, é uma causa direta | "We may be missing the component tests for a cluster of classes [...] This can happen when we use Mock Objects extensively to replace depended-on objects but the unit tests of the depended-on objects don't match the way the Mock Objects are being programmed to behave" | fonte primária | alta |
| O padrão mais comum observado pelo autor é ter testes funcionais/de componente de nível alto sem os unit tests correspondentes por método — o que ele distingue de test-first development vs. test-driven development | "I've encountered this problem most frequently when I had written the higher level (functional or component) tests but had failed to write all the unit tests for the individual methods" | fonte primária | alta |
| Infrequently Run Tests é uma segunda causa raiz: rodar os testes a cada pequena mudança preserva a memória de onde um bug foi introduzido, eliminando a necessidade de troubleshooting | "If we run our tests after every little change we make to the software we can remember what we changed since the last time we ran the tests [...] we know where it is because we remember putting it there!" | fonte primária | alta |
| A depuração manual tem custo de produtividade concreto — uma única sessão pode estender o prazo de desenvolvimento em meio dia ou mais | "a single manual debugging session could extend the time required to develop the software by half a day or more" | fonte primária | alta |
| A solução recomendada é test-driven development verdadeiro combinado com storytest-driven development, cobrindo unit tests de classes individuais e component tests de clusters relacionados | "Doing true test-driven development is the best way to avoid the circumstances that lead to Frequent Debugging [...] do storytest-driven development writing unit tests for individual classes as well as component tests" | fonte primária | alta |

---

## Key Claims

### 1. Primeira fonte da wiki para a subcategoria "Behavior Smells" — fecha a taxonomia de três ramos de Test Smells
A wiki já tinha Code Smells ([[wiki/sources/hard-to-test-code-xunitpatterns]]) e Project Smells ([[wiki/sources/production-bugs-xunitpatterns]], [[wiki/sources/developers-not-writing-tests-xunitpatterns]]) documentados, mas nenhuma fonte da terceira subcategoria irmã do catálogo (sidebar do site lista Assertion Roulette, Erratic Test, Fragile Test, Frequent Debugging, Manual Intervention, Slow Tests). Esta fonte fecha essa lacuna estrutural, permitindo à wiki nomear explicitamente as três subcategorias de Test Smells pela primeira vez.

### 2. Conecta explicitamente Mock Objects mal calibrados a um sintoma observável (depuração manual), não apenas a um risco abstrato
[[wiki/concepts/test-doubles]] já documenta a taxonomia completa de Meszaros e o "code smell: mocks excessivos", mas não tinha uma fonte descrevendo o *sintoma prático* de um Mock Object dessincronizado do comportamento real do objeto que substitui: sessões de depuração manual, porque a suíte "passa localmente" mas não reflete o comportamento real do DOC. É o mesmo mecanismo de risco já citado informalmente em [[wiki/concepts/tdd]] sobre a escola London/Mockist ("mocks podem mascarar integração quebrada"), agora com uma consequência concreta e nomeada.

### 3. Cruza com Infrequently Run Tests (Production Bugs) por um ângulo diferente do já documentado
[[wiki/concepts/production-bugs]] já cita Infrequently Run Tests como causa raiz de bugs em produção (testes lentos/instáveis levam devs a pararem de rodá-los). Esta fonte usa a mesma sub-causa para explicar um sintoma distinto: não é que o bug escape para produção, é que ele vira mais caro de *localizar* quando finalmente é achado, porque a "memória" de qual mudança o causou já se perdeu. É a mesma causa raiz alimentando dois smells-irmãos diferentes.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete

## Conceitos Tocados

- [[wiki/concepts/production-bugs]] — segunda citação independente de Infrequently Run Tests, agora como causa de depuração manual cara, não só de bugs escapando para produção; também cita Untested Requirement como cenário relacionado
- [[wiki/concepts/developers-not-writing-tests]] — mesma raiz estrutural: ausência de unit/component tests suficientes
- [[wiki/concepts/test-doubles]] — Mock Objects dessincronizados do comportamento real do DOC como causa concreta e nomeada de depuração manual
- [[wiki/concepts/tdd]] — test-driven development (não apenas test-first) citado como a solução central; storytest-driven development como complemento na camada de component test
- [[wiki/concepts/test-runner]] — ponto de partida do smell: a saída do Test Runner é insuficiente para localizar o problema
- [[wiki/concepts/code-smells]] — nova entrada na taxonomia de Meszaros, primeira da subcategoria Behavior Smells

## Questões Abertas

- **Defect Localization** é citado como o conceito-chave por trás do smell (via "Goals of Test Automation"), mas não tem página própria na wiki — candidato forte a ingestão futura, já que amarra tanto este smell quanto os já documentados (Production Bugs, Hard-to-Test Code).
- **Assertion Message** é citado como um dos dois mecanismos pelos quais um teste comunica a causa da falha (o outro é o padrão de falhas), mas não tem página própria.
- **Untested Requirement** (sub-causa de Production Bugs) é citado aqui num cenário ligeiramente diferente — falta de customer test que exponha um problema achado em teste manual do usuário — reforçando a necessidade de eventualmente desdobrar as sub-causas de Production Bugs em páginas próprias.
- **Component test** como categoria de teste (entre unit test e customer test) é citado repetidamente mas ainda não tem página conceitual própria na wiki, apesar de aparecer em múltiplas fontes já ingeridas.

---

## Citações Relevantes

> "*Frequent Debugging* is caused by a lack of Defect Localization in our suite of automated tests. The failed tests should tell us what went wrong either through their individual failure messages [...] or through the pattern of test failures."

> "This can happen when we use Mock Objects extensively to replace depended-on objects but the unit tests of the depended-on objects don't match the way the Mock Objects are being programmed to behave."

> "If we run our tests after every little change we make to the software we can remember what we changed since the last time we ran the tests [...] we know where it is because we remember putting it there!"

> "Doing true test-driven development is the best way to avoid the circumstances that lead to Frequent Debugging."

*(Tradução completa em `raw/frequent-debugging-xunitpatterns.md`.)*
