---
type: source
title: "Replace Dependency with Test Double (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["replace dependency with test double", "test refactoring test double", "xunit test patterns replace dependency"]
date_created: 2026-08-31
date_updated: 2026-09-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/replace-dependency-with-test-double-xunitpatterns.md
source_url: "http://xunitpatterns.com/Replace%20Dependency%20with%20Test%20Double.html"
author: "Gerard Meszaros"
date_published: 2007-01-01
date_ingested: 2026-08-31
source_count: 0
tags: [testes, test-doubles, refactoring, dependency-injection, dependency-lookup, xunit, sut, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Replace Dependency with Test Double (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Página canônica da **Test Refactoring** "Replace Dependency with Test Double" no catálogo xUnitPatterns.com — o procedimento mecânico que conecta a taxonomia de [[wiki/concepts/test-doubles|Test Double]] (já ingerida via [[wiki/sources/test-double-xunitpatterns-meszaros]] e [[wiki/sources/test-stub-xunitpatterns-meszaros]]) ao **como fazer** na prática. Resolve o problema "as dependências do objeto sob teste atrapalham a execução do teste" quebrando a dependência com um Test Double. Define uma sequência de decisões ortogonais entre si: (1) mecanismo de substituição — [[wiki/concepts/dependency-injection|Dependency Injection]] (melhor para unit tests) vs. **Dependency Lookup** (melhor para customer tests); (2) papel do double — Fake Object, Test Stub ou Mock Object, conforme o uso no teste; (3) técnica de construção — Hard-Coded vs. Configurable Test Double. Fecha com o passo final do teste (construir, configurar, instalar o double, e opcionalmente chamar `verification`) e observa que, em linguagens estaticamente tipadas, normalmente é preciso aplicar antes a refatoração **Extract Interface** [Fowler].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Dependency Injection é a melhor opção para unit tests; Dependency Lookup costuma funcionar melhor para customer tests | Primeiro parágrafo de "Implementation Notes" | fonte primária (Meszaros) | alta |
| A escolha entre Fake Object, Test Stub e Mock Object depende de como o double será **usado** pelo teste — não é uma decisão de construção | Segundo parágrafo; remete à narrativa "Using Test Doubles" | fonte primária (definição de autor) | alta |
| A escolha Hard-Coded vs. Configurable Test Double é ortogonal à escolha do papel (Stub/Mock/Fake) e determina o "formato" do teste | Terceiro parágrafo — testes com Mock Object são descritos como mais "front loaded" | fonte primária | alta |
| Em linguagens estaticamente tipadas, pode ser necessário aplicar **Extract Interface** [Fowler] antes de introduzir a implementação falsa | Último parágrafo | fonte primária (referência cruzada a Fowler) | alta |
| Alguns tipos de Mock Object exigem uma chamada explícita a um método de `verification` ao final do teste | Último parágrafo | fonte primária | média-alta (não detalha quais tipos exigem, remete a outro capítulo) |

---

## Key Claims

### 1. A decisão de *mecanismo* (DI vs. Lookup) precede a decisão de *papel* (Stub/Mock/Fake)
Antes de escolher qual variação de Test Double usar, é preciso decidir **como** ela chega ao SUT. [[wiki/concepts/dependency-injection|Dependency Injection]] — receber a dependência de fora, via construtor/setter/parâmetro — é apontada como a opção preferida para unit tests; **Dependency Lookup** (buscar a dependência via um registro/service locator) é apontada como mais adequada para customer tests. A fonte não detalha por que a preferência se inverte entre os dois níveis de teste, mas a distinção reforça que a taxonomia de Test Double (Dummy/Stub/Fake/Spy/Mock) e o mecanismo de instalação são perguntas **independentes** — a mesma separação "por que vs. como" já registrada em [[wiki/sources/test-double-xunitpatterns-meszaros]] para a construção (Hard-Coded vs. Configurable) se repete aqui, um nível acima, para a instalação.

### 2. Três decisões ortogonais, não uma escolha única
A refatoração encadeia três eixos independentes: **mecanismo de substituição** (DI vs. Dependency Lookup) → **papel do double** (Fake/Stub/Mock, decidido por como o teste usa o double) → **técnica de construção** (Hard-Coded vs. Configurable). Cada eixo tem seu próprio critério de decisão e nenhum determina os outros — um Mock Object, por exemplo, pode ser instalado por DI ou por Lookup, e pode ser Hard-Coded ou Configurable, sem que isso mude sua classificação como Mock.

### 3. Mock Object "front-loads" o teste
Diferente de Stub/Fake, testes com Mock Object concentram trabalho na fase de **construção** do double (montar expectativas antes de exercitar o SUT), e normalmente fecham com uma chamada a `verification` — um passo que Stub e Fake não têm, porque não verificam saídas indiretas. Isso é consistente com a definição de Mock em [[wiki/sources/test-double-xunitpatterns-meszaros]]: "ênfase na verificação", não apenas fornecer um valor de retorno.

### 4. Extract Interface como pré-requisito em linguagens estaticamente tipadas
Para introduzir um Test Double sem alterar o tipo declarado da dependência, muitas vezes é preciso primeiro extrair uma interface da implementação real (refatoração **Extract Interface**, atribuída a [Fowler], não a Meszaros). O double então implementa essa interface, e a variável que guarda a **substitutable dependency** é tipada pela interface, não pela classe concreta — mecanismo que viabiliza a própria ideia de "dependência substituível" central a [[wiki/concepts/test-doubles]].

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor da fonte; mesma autoria do restante do cluster xUnitPatterns já ingerido
- [[wiki/entities/martin-fowler|Fowler]] — citado como autor da refatoração **Extract Interface**, referenciada como pré-requisito em linguagens estaticamente tipadas
- [[wiki/entities/jmock]] — exemplo concreto de framework que constrói o Configurable Test Double via toolkit (Configuration Interface), em vez de Hard-Coded manual; ver [[wiki/sources/jmock]]

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — conceito central; esta fonte é o "como fazer" mecânico que conecta a taxonomia já documentada ao processo de refatoração do teste
- [[wiki/concepts/dependency-injection]] — mecanismo apontado como preferido para unit tests nesta refatoração
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — DI/Lookup são os mecanismos que tornam um teste solitário possível, ao substituir o DOC

## Questões Abertas

- **Dependency Lookup não tem página própria na wiki.** A fonte o cita como alternativa à DI para customer tests, mas o mecanismo (service locator/registro) não está documentado em nenhum concept page existente — candidato a stub numa futura ingestão, caso surja fonte dedicada.
- **Extract Interface [Fowler] também não tem página própria.** Citada apenas de passagem como pré-requisito técnico; não há fonte primária de Fowler sobre essa refatoração específica ainda ingerida na wiki.
- **Por que DI é melhor para unit tests e Lookup para customer tests não é explicado** — a fonte afirma a preferência sem justificar a causa raiz (possivelmente relacionado a granularidade: customer tests operam num nível onde um registro global de dependências é mais prático que injeção explícita ponto a ponto, mas isso é inferência, não afirmação da fonte).
- Nenhuma contradição encontrada com o que já estava na wiki sobre Test Doubles — esta fonte é estritamente elaborativa, preenchendo a lacuna "mecânica de refatoração" que faltava entre a taxonomia (Test Double, Test Stub) e a prática de escrever o teste.

---

## Citações Relevantes

> "The dependencies of an object being tested are getting in the way of running tests."

> "Dependency Injection (page X) is best for unit tests while Dependency Lookup (page X) often works better for customer tests."

> "Mock Object tests are more 'front loaded' by the construction of the Mock Object."

> "In statically typed languages, we may have to do an Extract Interface [Fowler] refactoring before we can introduce the fake implementation."
