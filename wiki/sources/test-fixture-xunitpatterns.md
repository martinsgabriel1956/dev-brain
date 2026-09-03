---
type: source
title: "Test Fixture (in xUnit) (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test fixture", "test context", "fixture de teste", "xunit patterns glossary test fixture"]
date_created: 2026-08-31
date_updated: 2026-08-31
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-fixture-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20fixture%20-%20xUnit.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 0
tags: [testes, test-fixture, test-context, testcase-class, junit, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Fixture (in xUnit) (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário curto do catálogo xUnitPatterns.com dedicado ao próprio termo **test fixture** (no contexto do [[wiki/sources/xunit-xunitpatterns|xUnit]], não a acepção mais ampla de "fixture" usada por outras ferramentas de teste, como o FIT). Define **test fixture** como "tudo que precisamos ter em vigor para rodar um teste e esperar um resultado específico" — sinônimo de **test context**, já registrado em [[wiki/sources/fixture-setup-xunitpatterns]] como o produto da fase de fixture setup. O valor novo desta fonte não está em repetir essa definição, mas em uma nuance estrutural que nenhuma fonte anterior da wiki havia registrado: em algumas variantes de xUnit — **JUnit e seus ports diretos entre elas** — o **test context** é mantido conceitualmente separado da **Testcase Class** que o cria. Isso conecta diretamente com o achado de [[wiki/sources/test-case-xunitpatterns]] de que a Testcase Class "é na verdade" uma **Test Suite Factory**: o test fixture é o produto que essa fábrica produz, não um atributo fixo da própria classe.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test fixture é tudo que precisa estar em vigor para rodar um teste e esperar um resultado específico | "all the things we need to have in place in order to run a test and expect a particular outcome" | fonte primária (Meszaros) | alta |
| Test fixture é sinônimo de test context | "Some people call this the test context" | fonte primária | alta |
| Algumas variantes de xUnit mantêm test context separado da Testcase Class que o cria; JUnit e seus ports diretos se enquadram nesse grupo | "Some variants of xUnit keep the concept of the test context separate from the Testcase Class that creates it; JUnit and its direct ports fall into this camp" | fonte primária | alta |
| Configurar o test fixture é a primeira fase do Four-Phase Test | "Setting up the test fixture is the first phase of the Four-Phase Test" | fonte primária | alta |

---

## Key Claims

### 1. Test fixture (test context) é definido aqui pela sua função, não pela sua forma — mesma definição já vista em fixture-setup, agora com citação própria para o substantivo
[[wiki/sources/fixture-setup-xunitpatterns]] já registrava essa mesma equivalência ("test fixture (or test context)"), mas como efeito colateral da definição de **fixture setup** (a fase/verbo). Esta fonte é o verbete dedicado ao substantivo em si — a citação correta para "test fixture"/"test context" como conceito autônomo, independente da fase que o produz.

### 2. JUnit trata o test context como produto de uma fábrica, não como estado embutido na própria Testcase Class
Esta é a contribuição genuinamente nova: nem toda variante de xUnit modela o test fixture do mesmo jeito. Em JUnit e seus ports diretos, o **test context** é conceitualmente separado da [[wiki/sources/test-case-xunitpatterns|Testcase Class]] que o cria — reforçando a reclassificação já registrada em [[wiki/sources/test-case-xunitpatterns]]: a Testcase Class "é na verdade" uma **Test Suite Factory**, e o test fixture é o que essa fábrica produz a cada execução, não um atributo permanente da classe. A fonte não detalha quais variantes de xUnit ficam *fora* desse grupo (ou seja, que fundem test context e Testcase Class num único objeto persistente) — apenas afirma que existem, sem nomeá-las.

### 3. Fixture setup como primeira fase do Four-Phase Test
Reforça, de fonte primária dedicada ao termo "test fixture" (não só à fase "fixture setup"), a mesma cadeia já registrada em [[wiki/concepts/tdd]] e [[wiki/sources/fixture-setup-xunitpatterns]]: configurar o fixture é a primeira das quatro fases do teste (**Four-Phase Test**), precondição para o [[wiki/concepts/test-doubles|SUT]] poder ser exercitado. Nenhuma fonte da wiki ainda isola o próprio **Four-Phase Test** como verbete primário — permanece uma lacuna.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/fixture-setup-xunitpatterns]], [[wiki/sources/test-case-xunitpatterns]] e demais verbetes do glossário
- [[wiki/entities/junit]] — citado nominalmente como exemplo de variante de xUnit que mantém test context separado da Testcase Class, junto de "seus ports diretos" (não nomeados individualmente)

## Conceitos Tocados

- [[wiki/concepts/indirect-input-output]] — test fixture é o produto coletivo da fase de fixture setup, onde control points/Test Doubles entram em cena (já registrado via [[wiki/sources/fixture-setup-xunitpatterns]]); esta fonte acrescenta a nuance de que, em JUnit, esse produto é estruturalmente separado da classe que o gera
- [[wiki/concepts/test-doubles]] — o test fixture é o "palco" onde Test Doubles são instalados durante a fixture setup
- [[wiki/concepts/tdd]] — Four-Phase Test como estrutura formal por trás do ciclo RED-GREEN-REFACTOR

## Questões Abertas

- A fonte não nomeia quais variantes de xUnit **não** se enquadram no grupo "JUnit e ports diretos" — ou seja, quais frameworks fundem test context e Testcase Class num único objeto persistente. Sem essa lista, não é possível confirmar empiricamente o contraste (apenas que ele existe, segundo Meszaros).
- **Four-Phase Test** segue sem fonte primária isolada na wiki — citado de passagem aqui e em [[wiki/sources/fixture-setup-xunitpatterns]], mas nunca como verbete próprio. Candidato natural para a próxima ingestão do mesmo cluster xUnitPatterns.com (a página `Four Phase Test.html` já é referenciada indiretamente por ambas as fontes).
- A página remete a um verbete de desambiguação ("test fixture (disambiguation)") para outros sentidos do termo em ferramentas fora do xUnit (ex.: FIT) — não ingerido; fora do escopo desta sessão.

---

## Citações Relevantes

> "In xUnit, a test fixture is all the things we need to have in place in order to run a test and expect a particular outcome. Some people call this the test context."

> "Some variants of xUnit keep the concept of the test context separate from the Testcase Class that creates it; JUnit and its direct ports fall into this camp."

> "Setting up the test fixture is the first phase of the Four-Phase Test."

*(Tradução completa em `raw/test-fixture-xunitpatterns.md`.)*
