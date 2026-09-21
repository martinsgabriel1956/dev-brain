---
type: entity
title: "JUnit"
aliases: ["junit"]
date_created: 2026-07-19
date_updated: 2026-09-21
source_count: 11
tags: [testes, tdd, junit, xunit, kent-beck, erich-gamma, test-fixture]
skill: tech-mentor-testing
status: stub
---

# JUnit

Framework de testes unitários para Java, criado por [[wiki/entities/kent-beck]] e [[wiki/entities/gang-of-four|Erich Gamma]] num voo de Zurique para a OOPSLA 1997, programado em par e feito test-first. É o membro fundador da família de frameworks conhecida como "[[wiki/concepts/tdd|Xunit]]" — nome que deriva diretamente dele. O verbete de glossário [[wiki/sources/xunit-xunitpatterns]] define formalmente "xUnit" como qualquer framework baseado no padrão do **JUnit ou SUnit** — cita [[wiki/entities/sunit|SUnit]], o framework caseiro de Beck em Smalltalk, como o segundo ancestral de referência, ao lado do próprio JUnit.

## Origem e impacto

Antes do JUnit, Kent Beck já mantinha frameworks de teste caseiros em Smalltalk (ver [[wiki/entities/c3-project]]), mas eram [[wiki/concepts/seedwork|Seedwork]] — cada time reconstruía o próprio. JUnit foi o primeiro a ganhar tração ampla fora do Smalltalk, e Fowler credita sua simplicidade e adoção pela indústria como fator essencial no crescimento de Extreme Programming e Test-Driven Development. Introduziu o indicador de progresso vermelho/verde ("red bar/green bar"), que se tornou vocabulário padrão em ferramentas de teste — manifestação visual do conceito formalizado em [[wiki/sources/test-result-xunitpatterns|test result]]: cada execução do mesmo teste pode produzir um resultado diferente da anterior.

## Test context separado da Testcase Class

O verbete de glossário dedicado ao termo [[wiki/sources/test-fixture-xunitpatterns|test fixture]] cita JUnit nominalmente como exemplo de variante de xUnit que mantém o **test context** (o [[wiki/concepts/indirect-input-output|test fixture]]) conceitualmente separado da **Testcase Class** que o cria — "JUnit and its direct ports fall into this camp". Isso reforça a reclassificação já registrada em [[wiki/sources/test-case-xunitpatterns]]: a Testcase Class "é na verdade" uma **Test Suite Factory**, e o test fixture é o produto dessa fábrica a cada execução de teste, não um atributo fixo embutido na própria classe. A fonte não nomeia quais variantes de xUnit ficam fora desse grupo (fundindo os dois conceitos num único objeto persistente).

## Primeiro exemplo de código de uma Testcase Class

[[wiki/sources/testcase-class-xunitpatterns]] traz o primeiro exemplo de código de uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] já ingerido na wiki: `TestScheduleFlight extends TestCase`, estilo JUnit 3, com três [[wiki/concepts/test-method|Test Methods]] testando transições de estado de um objeto `Flight`. Cada método monta seu próprio fixture localmente via um helper (`FlightTestHelper`), sem depender de estado de instância compartilhado da classe — consistente, na prática, com a observação já registrada acima de que JUnit mantém o test context separado da Testcase Class que o cria.

## "JUnit New Instance Behavior" — a exceção do NUnit e do TestNG

[[wiki/sources/there-is-always-an-exception-xunitpatterns]] nomeia explicitamente o comportamento de instanciação do JUnit — criar um [[wiki/concepts/testcase-object|Testcase Object]] separado a cada [[wiki/concepts/test-method|Test Method]] — como "JUnit New Instance Behavior", tratando-o como a regra fundamental que a família xUnit segue para garantir Independent Test. Segundo a fonte, [[wiki/entities/nunit|NUnit]] (2.x) e [[wiki/entities/testng|TestNG]] são as únicas exceções conhecidas: ambos reutilizam uma única instância da Testcase Class entre todos os Test Methods, o que [[wiki/entities/james-newkirk]] (coautor do NUnit 2.0) admite publicamente ter sido um erro de design — a reutilização cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito, fonte de [[wiki/concepts/erratic-test|Erratic Test]] por dependência de ordem de execução. [[wiki/entities/martin-fowler]] considerou o caso relevante o bastante para escrever um artigo dedicado ("JunitNewInstance") defendendo a abordagem do JUnit.

## Graphical Test Runner no Eclipse: Command Pattern em ação

[[wiki/sources/testcase-object-xunitpatterns]] usa o Graphical Test Runner do JUnit embutido no Eclipse como o exemplo concreto de **Test Tree Explorer**: uma árvore navegável (`TestSuite("...AllTests")` → `TestSuite("...TestApproveFlight")` → `TestApproveFlight("testScheduledState_...")`) onde cada nó folha é um [[wiki/concepts/testcase-object|Testcase Object]] individual, nomeado por convenção com o nome do [[wiki/concepts/test-method|Test Method]] que executa. É a primeira evidência visual concreta, na wiki, de por que tratar testes como objetos ([[wiki/concepts/command-pattern|Command Pattern]]) importa na prática: só assim um runner gráfico consegue deixar o usuário inspecionar e selecionar testes individualmente na árvore.

## Test Method Discovery: prefixo "test" (JUnit 3) vs. annotation (JUnit 4+)

[[wiki/sources/test-discovery-xunitpatterns]] usa o JUnit para ilustrar os dois lados históricos da dualidade de **[[wiki/concepts/test-discovery|Test Method Discovery]]**: JUnit 3 identificava Test Methods pela convenção de nomenclatura (prefixo `"test"`, ex.: `testDisplayCurrentTime_AtMidnight`), enquanto JUnit 4+ passou a usar a annotation `@Test` — mesma transição já registrada em [[wiki/sources/annotation-xunitpatterns]] do lado da marcação de Testcase Classes, agora confirmada também do lado dos métodos com exemplo de código dedicado.

## Proliferação de ports

Michael Feathers criou o CppUnit (provavelmente o primeiro port para outra linguagem); a partir daí praticamente toda linguagem ganhou um port de JUnit — a família XUnit. NUnit (C#) chegou a influenciar de volta o próprio Java: o uso de atributos no NUnit 2.0 (elogiado por Anders Hejlsberg) antecipou o padrão que o Java adotaria como annotations.

## Ver também

- [[wiki/concepts/tdd]]
- [[wiki/entities/gang-of-four]] — Erich Gamma, coautor do JUnit, também é um dos quatro autores do *Design Patterns*

## Key Sources

- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/xunit-xunitpatterns]] — verbete de glossário que define formalmente "xUnit" e nomeia SUnit como o segundo framework de referência da família
- [[wiki/sources/seedwork-martin-fowler]] — fonte primária do termo Seedwork usado para descrever o antecessor caseiro do JUnit
- [[wiki/sources/c3-martin-fowler]] — linha do tempo do C3 (1993-1999), projeto onde o antecessor do JUnit foi usado
- [[wiki/sources/test-fixture-xunitpatterns]] — verbete de glossário dedicado ao termo test fixture/test context: cita JUnit e seus ports diretos como exemplo de variante de xUnit que mantém o test context separado da Testcase Class que o cria
- [[wiki/sources/annotation-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "annotation": JUnit 4.0 como exemplo canônico (marca Testcase Classes e Test Methods), com NUnit citado como equivalente via "attributes"
- [[wiki/sources/testcase-class-xunitpatterns]] — verbete de glossário do mesmo site, dedicado ao termo Testcase Class: traz o primeiro exemplo de código de uma Testcase Class em Java/JUnit 3 já ingerido na wiki
- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — sidebar do mesmo site nomeando o "JUnit New Instance Behavior" como a regra que NUnit 2.x e TestNG rompem; contraste que reforça, por comparação negativa, por que o comportamento de instanciação do JUnit é considerado o padrão correto da família
- [[wiki/sources/testcase-object-xunitpatterns]] — verbete de glossário do mesmo site, dedicado ao próprio termo Testcase Object: usa o Graphical Test Runner do JUnit no Eclipse como exemplo concreto de Test Tree Explorer
- [[wiki/sources/test-discovery-xunitpatterns]] — usa JUnit para ilustrar as duas gerações de Test Method Discovery: convenção de nomenclatura (JUnit 3) e annotation `@Test` (JUnit 4+)
- [[wiki/sources/test-result-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição do próprio termo "test result": fecha a lacuna de fonte primária isolada para o conceito por trás da prática histórica do red bar/green bar
