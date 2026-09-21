---
type: source
title: "Testcase Object (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["testcase object", "objeto de caso de teste", "test as command"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/testcase-object-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Testcase%20Object.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
tags: [testes, xunit, testcase-object, command-pattern, gof, junit, terminologia, fonte-primaria, tech-mentor-testing]
skill: tech-mentor-testing
status: stable
---

# Testcase Object (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete da categoria **XUnit Basics** do catálogo xUnitPatterns.com dedicado ao próprio termo **Testcase Object** — fecha a lacuna sinalizada como stub em [[wiki/concepts/testcase-object]] desde a ingestão de [[wiki/sources/testcase-class-xunitpatterns]]. Problema que o padrão resolve: "como executamos os testes?". Resposta central: cada teste vira um objeto **Command** [GOF] — instanciado a partir da [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] — e o [[wiki/concepts/test-runner|Test Runner]] o executa chamando um método `run` padrão, sem precisar conhecer a interface específica de cada teste. A fonte detalha pela primeira vez na wiki o mecanismo interno de despacho: o construtor da Testcase Class recebe o nome do [[wiki/concepts/test-method|Test Method]] a invocar como parâmetro (um caso de **Pluggable Behavior** [SBPP]), armazena-o numa variável de instância, e o método `run` usa **reflection** para localizar e invocar esse método pelo nome. Também traz o primeiro exemplo visual de **Test Tree Explorer** da wiki (árvore de testes do [[wiki/entities/junit]] no Eclipse), mostrando a convenção de nomenclatura: nome da classe fora dos parênteses, nome do Testcase Object (= nome do Test Method) dentro.

---

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Cada teste é representado por um objeto **Command** [GOF], instanciado a partir da Testcase Class | "We instantiate a Command[GOF] object to represent each Test Method to execute" | Alta — fonte primária |
| A Testcase Class atua como **Test Suite Factory** para criar um **Test Suite Object** contendo todos os Testcase Objects | "We use the Testcase Class as a Test Suite Factory [...] to create a Test Suite Object to hold all the Testcase Objects" | Alta — confirma e não contradiz o já registrado em [[wiki/sources/testcase-class-xunitpatterns]] |
| Testcase Objects podem ser criados via **Test Discovery** ou **Test Enumeration** | "We can use either Test Discovery or Test Enumeration to create the Testcase Objects" | Alta — apenas nomeados, sem detalhamento nesta fonte |
| Tratar testes como objetos de primeira classe permite mantê-los em coleções, iterar, invocar — mais fácil que tratá-los como procedimentos simples | Afirmação central da seção "Why We Do This" | Alta |
| A maioria dos membros do xUnit cria um Testcase Object separado por teste para isolar testes (Independent Test); há sempre uma exceção | Remete diretamente a [[wiki/sources/there-is-always-an-exception-xunitpatterns]], já ingerida | Alta — consistente com fonte já ingerida |
| Cada Testcase Object implementa uma interface de teste padrão, permitindo ao Test Runner tratá-lo como Command sem conhecer a especificidade de cada teste | "Each Testcase Object implements a standard test interface [...] This allows each Testcase Object to act as a Command object" | Alta |
| O despacho do Test Method correto usa **Pluggable Behavior** [SBPP]: o construtor recebe o nome do método como parâmetro, armazenado numa instance variable; `run` usa reflection para achar e invocar | Parágrafo central de "Implementation Notes" | Alta |
| Por convenção, o nome do Testcase Object é o nome do Test Method executado; o nome do Test Suite Object é a string passada ao construtor | Explicado a partir do exemplo do Test Tree Explorer do JUnit/Eclipse | Alta |

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesmo cluster de fontes primárias do catálogo já ingerido
- [[wiki/entities/junit]] — exemplo do Graphical Test Runner embutido no Eclipse, mostrando a árvore `TestSuite` → `TestApproveFlight`/`TestDescheduleFlight`/etc.
- [[wiki/entities/gang-of-four]] — origem do padrão **Command**, citado explicitamente como `[GOF]`

## Conceitos Tocados

- [[wiki/concepts/testcase-object]] — fonte primária dedicada que esta ingestão finalmente traz, fechando o stub existente
- [[wiki/concepts/test-method]] — cada Testcase Object corresponde a exatamente um Test Method
- [[wiki/concepts/test-runner]] — consumidor final; ganha aqui o primeiro exemplo concreto (Eclipse) de **Test Tree Explorer**
- [[wiki/concepts/test-suite-object]] — reafirmado como o agrupador de Testcase Objects produzido pela Testcase Class
- [[wiki/concepts/command-pattern]] — aplicação concreta do padrão GOF: cada teste é um Command, com `run` como método de execução padrão
- [[wiki/concepts/pluggable-behavior]] — mecanismo de despacho do Test Method certo, agora com fonte primária dedicada em [[wiki/sources/pluggable-behavior-xunitpatterns]]
- [[wiki/entities/nunit]] / [[wiki/entities/testng]] — citados indiretamente via referência a "There's Always an Exception", já coberta em fonte anterior

## Open Questions

1. **Test Discovery, Test Enumeration e Test Selection** são citados como os mecanismos de criação dos Testcase Objects, mas nenhum tem página/fonte primária dedicada ainda (mesma lacuna já sinalizada em [[wiki/sources/testcase-class-xunitpatterns]] e em [[wiki/concepts/test-suite-object]]) — candidatos naturais para a próxima ingestão do cluster "XUnit Basics".
2. ~~**Pluggable Behavior [SBPP]** (Smalltalk Best Practice Patterns, Kent Beck) é citado como o padrão que nomeia a técnica de passar o nome do método a invocar via construtor — não tem página própria na wiki; candidato a stub numa ingestão futura.~~ **Resolvida em 2026-09-21:** [[wiki/sources/pluggable-behavior-xunitpatterns]] fecha essa lacuna com fonte primária dedicada — define as duas variações do padrão (Pluggable Method Selector, Pluggable Block) e classifica este uso como Pluggable Method Selector. Ver [[wiki/concepts/pluggable-behavior]].
3. ~~**Reflection** (glossário do site, `reflection.html`) é citado como o mecanismo que o método `run` usa para localizar/invocar o Test Method pelo nome — página de glossário dedicada ainda não ingerida.~~ **Resolvida em 2026-09-21:** [[wiki/sources/reflection-xunitpatterns]] fecha essa lacuna com fonte primária dedicada. Ver [[wiki/concepts/reflection]].
4. **Test Tree Explorer** ganha aqui sua primeira menção com imagem/exemplo concreto na wiki, mas segue sem fonte primária própria — é tratado como subseção de [[wiki/concepts/test-runner]], não como conceito próprio, por enquanto.

## Raw Quotes

> "We create a Command object for each test and call the run method when we wish to execute it."

> "Treating tests as first-class objects opens up a lot of possibilities that are not available to us if we treat them as simple procedures."

> "The constructor of the Testcase Class takes the name of the method to be invoked as a parameter and stores this name in an instance variable. When the run method is invoked by the Test Runner on the Testcase Object, it uses reflection to find and invoke the method whose name is in the variable."

*(Tradução completa em `raw/testcase-object-xunitpatterns.md`.)*

## Key Sources (fontes citadas nesta ingestão)

- [[wiki/sources/testcase-class-xunitpatterns]] — já descrevia a mecânica em alto nível a partir da perspectiva da Testcase Class; esta fonte a detalha a partir da perspectiva do próprio Testcase Object
- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — a exceção à regra "um Testcase Object por Test Method" (NUnit 2.x, TestNG), referenciada diretamente por esta fonte
