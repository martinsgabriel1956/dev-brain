---
type: entity
title: "Gerard Meszaros"
aliases: ["Meszaros", "xUnit Test Patterns author"]
date_created: 2026-07-19
date_updated: 2026-09-04
source_count: 24
tags: [testes, autor, test-doubles, xunit, taxonomia]
skill: tech-mentor-testing
status: draft
---

# Gerard Meszaros

Autor de *xUnit Test Patterns: Refactoring Test Code* (2007), livro de padrões para os frameworks da família [[wiki/concepts/tdd|Xunit]]. Criou a taxonomia dos cinco tipos de [[wiki/concepts/test-doubles|Test Double]] — Dummy, Fake, Stub, Spy, Mock — relatada e divulgada por [[wiki/entities/martin-fowler]] em seu bliki em 2006, antes mesmo do livro ser publicado.

## Autoria da taxonomia de Test Doubles

A distinção entre os cinco tipos de dublê de teste é frequentemente associada a Fowler por ser a fonte mais citada, mas o próprio Fowler credita a autoria a Meszaros explicitamente: ele estava "escrevendo um livro para capturar padrões de uso dos vários frameworks Xunit" e criou o vocabulário para resolver a inconsistência de nomes (stub, mock, fake, dummy) que já existia informalmente na comunidade. Ver [[wiki/sources/test-double-martin-fowler]].

A **fonte primária** dessa taxonomia — a própria página `Test Double` do catálogo xUnitPatterns.com, escrita por Meszaros como versão preliminar do capítulo do livro (p. 522) — está ingerida em [[wiki/sources/test-double-xunitpatterns-meszaros]]. Além dos cinco tipos, ela fixa o vocabulário que os sustenta: **SUT** (sistema sob teste, nunca substituído), **DOC** (componente-dependência, o que se substitui), **entrada/saída indireta** e **pontos de controle/observação**. Duas definições normativas dele que valem citar: um **Mock não é "Stub + asserção"** (a ênfase na *verificação* das saídas indiretas o torna um uso fundamentalmente diferente), e um **Test Spy é "apenas um" Stub com gravação**.

## Contribuidor recorrente do bliki de Fowler sobre test doubles

Além de ser a fonte da taxonomia relatada por Fowler, Meszaros é creditado como um dos contribuidores de ideias no bliki [[wiki/sources/self-initializing-fake-martin-fowler]] (2009), ao lado de Josh Price e Darren Cotterill — indício de que a relação entre os dois não se limitou à divulgação da taxonomia em 2006, mas incluiu troca continuada sobre padrões de teste.

## Ver também

- [[wiki/concepts/test-doubles]]
- [[wiki/entities/martin-fowler]] — divulgou a taxonomia de Meszaros no bliki antes do livro sair

## Key Sources

- [[wiki/sources/test-double-xunitpatterns-meszaros]] — **fonte primária**: a página canônica `Test Double` do próprio Meszaros (xUnitPatterns.com), com o vocabulário completo e as cinco variações
- [[wiki/sources/test-stub-xunitpatterns-meszaros]] — fonte primária dedicada à variação Test Stub: Responder vs. Saboteur, Entity Chain Snipping
- [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — fonte primária da refatoração "Replace Dependency with Test Double": mecânica de decisão entre DI/Dependency Lookup, papel do double e técnica de construção
- [[wiki/sources/control-point-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do termo control point
- [[wiki/sources/depended-on-component-doc-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do termo DOC
- [[wiki/sources/indirect-input-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "indirect input"
- [[wiki/sources/doc-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição formal de DOC (depended-on component)
- [[wiki/sources/sut-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição formal de SUT (system under test) e as siglas irmãs CUT/OUT/MUT/AUT
- [[wiki/sources/unit-test-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição formal de unit test (critério: tamanho do SUT) e os sinônimos de XP (developer test, programmer test)
- [[wiki/sources/test-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição mais básica de todas: o próprio termo "test" (procedimento que verifica o SUT), sinônimo de test case
- [[wiki/sources/test-automater-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "test automater": a pessoa/papel do projeto que constrói os testes, distinta do "subject matter expert" que define quais testes devem existir
- [[wiki/sources/test-case-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "test case": sinônimo de test, mas também nomeia a Testcase Class (Test Suite Factory que agrupa Test Methods)
- [[wiki/sources/fixture-setup-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "fixture setup" e "test fixture"/"test context"
- [[wiki/sources/test-fixture-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "test fixture"/"test context" e a nuance de que JUnit o mantém separado da Testcase Class que o cria
- [[wiki/sources/xunit-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição formal do próprio termo "xUnit" (padrão baseado em JUnit ou SUnit)
- [[wiki/sources/test-double-martin-fowler]] — fonte secundária que popularizou e atribuiu a taxonomia a ele
- [[wiki/sources/self-initializing-fake-martin-fowler]] — creditado como contribuidor de ideias, junto com Josh Price e Darren Cotterill
- [[wiki/sources/procedure-variable-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "procedure variable" (function pointer/delegate): mecanismo de dynamic binding por trás do Configurable Test Double, e precursor histórico do despacho polimórfico
- [[wiki/sources/observation-point-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "observation point": contraparte simétrica de control point, fecha a hierarquia interaction point → control point | observation point
- [[wiki/sources/interaction-point-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "interaction point": a categoria mãe da qual control point e observation point são os dois subtipos exaustivos
- [[wiki/sources/extreme-programming-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição mais genérica do próprio termo "eXtreme Programming": metodologia ágil que destaca pair programming, testes unitários automatizados e iterações curtas
- [[wiki/sources/customer-test-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "customer test": teste da funcionalidade visível do sistema, independente das decisões de design internas ao SUT — fecha, de fonte primária isolada, o par de contraste com "unit test"
- [[wiki/sources/jmock]] — primeira entrada da categoria "Tools" do site ingerida na wiki: descreve o [[wiki/entities/jmock]] como framework de Mock Object para Java, com destaque para a Configuration Interface fluente
- [[wiki/sources/utwhcm-xunitpatterns]] — primeira entrada da categoria "References" (bibliografia) do site ingerida na wiki: verbete de citação ao artigo externo de Sven Gorts sobre mocks construídos à mão
- [[wiki/sources/decorator-xunitpatterns]] — primeira entrada da categoria "External Patterns" do site ingerida na wiki: verbete curto que cita a definição original do GOF para o Decorator, sem elaboração própria de Meszaros
