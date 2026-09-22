---
type: concept
title: "Test Method"
aliases: ["método de teste"]
date_created: 2026-09-11
date_updated: 2026-09-21
source_count: 9
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Method

Unidade elementar de lógica de teste em [[wiki/concepts/tdd|xUnit]]: um método que implementa um único [[wiki/sources/test-case-xunitpatterns|test case]]. Precisa estar associado a uma classe em linguagens orientadas a objetos — é exatamente esse o papel da [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]], que agrupa um conjunto de Test Methods relacionados. Em tempo de execução, cada Test Method vira um [[wiki/concepts/testcase-object|Testcase Object]] separado, instanciando a Testcase Class uma vez por método — o que permite manipular Test Methods individualmente (selecioná-los, pular, reordenar) em vez de tratá-los como um bloco monolítico.

## Nem todo membro da família instancia um Testcase Object por Test Method

[[wiki/sources/there-is-always-an-exception-xunitpatterns]] documenta a exceção a essa regra: [[wiki/entities/nunit|NUnit]] (2.x) e [[wiki/entities/testng|TestNG]] reutilizam uma única instância da Testcase Class para todos os Test Methods, em vez de instanciar uma nova a cada método (o "JUnit New Instance Behavior"). Isso cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito entre Test Methods — qualquer variável de instância referenciada por um método fica visível para os demais, habilitando dependência de ordem de execução ([[wiki/concepts/erratic-test|Erratic Test]]).

## Como o nome do Test Method chega ao Testcase Object

[[wiki/sources/testcase-object-xunitpatterns]] detalha, pela primeira vez na wiki, o mecanismo pelo qual um [[wiki/concepts/testcase-object|Testcase Object]] sabe qual Test Method invocar: o construtor da Testcase Class recebe o nome do método como parâmetro (um caso de **[[wiki/concepts/pluggable-behavior|Pluggable Behavior]]** [SBPP] — especificamente a variação **Pluggable (Method) Selector**, definida com fonte primária dedicada em [[wiki/sources/pluggable-behavior-xunitpatterns]]) e o armazena numa variável de instância; o método `run` usa **[[wiki/concepts/reflection|reflection]]** para encontrar e invocar o Test Method correspondente — mecanismo hoje com fonte primária isolada em [[wiki/sources/reflection-xunitpatterns]]. É também essa fonte que nomeia a convenção pela qual o nome do Test Method vira, por padrão, o nome do próprio Testcase Object exibido num **Test Tree Explorer**.

## Como o framework reconhece que um método É um Test Method

[[wiki/sources/test-discovery-xunitpatterns]], fonte primária dedicada a **[[wiki/concepts/test-discovery|Test Method Discovery]]**, fecha uma lacuna distinta da seção acima: não como o Testcase Object invoca o Test Method certo (já coberto acima via Pluggable Behavior + reflection), mas como o framework primeiro **identifica** quais métodos da classe são Test Methods. Duas formas: **convenção de nomenclatura** (prefixo `"test"`, ex.: `testCounters` — a forma tradicional, JUnit 3/xUnit legado) ou **[[wiki/sources/method-attribute-xunitpatterns|method attribute]]**/**[[wiki/sources/annotation-xunitpatterns|annotation]]** (`[Test]`/`@Test`) — o termo genérico "method attribute" ganhou fonte primária isolada em [[wiki/sources/method-attribute-xunitpatterns]], espelhando o já fechado para **[[wiki/sources/class-attribute-xunitpatterns|class attribute]]** no nível de classe. Ao migrar para um framework que descobre por nome, pode ser necessário um **[[wiki/concepts/rename-method|Rename Method]]** [Fowler] nos Test Methods existentes.

## Como um Test Method se perde

[[wiki/sources/production-bugs-xunitpatterns]] lista as formas concretas pelas quais um Test Method deixa de rodar: esquecer o atributo `[test]` ou usar um nome que não bate com a convenção de [[wiki/concepts/test-discovery|Test Discovery]], esquecer a chamada `suite.addTest` (Test Enumeration manual), renomear o método de forma que quebre a convenção de nomenclatura, ou adicionar um atributo `[Ignore]` (ex.: [[wiki/entities/nunit|NUnit]]) — este último tipicamente para "destravar" um build com teste falhando, e depois esquecido. Ver [[wiki/concepts/production-bugs|Production Bugs]] / Lost Test.

## Status: stub

Citado por nome em quase todas as fontes já ingeridas do cluster xUnitPatterns.com ([[wiki/sources/test-case-xunitpatterns]], [[wiki/sources/test-fixture-xunitpatterns]], [[wiki/sources/annotation-xunitpatterns]]), mas até [[wiki/sources/testcase-class-xunitpatterns]] nenhuma fonte tratava o termo como assunto central — apenas de passagem. Sem página primária dedicada ("Test Method.html" no site), a mecânica de como um Test Method vira Testcase Object fica limitada ao que [[wiki/sources/testcase-class-xunitpatterns]] descreve a partir da perspectiva da Testcase Class, complementada pela exceção documentada acima e pelo mecanismo de reconhecimento (Test Method Discovery) documentado nesta seção.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — descreve, pela primeira vez de forma central, como Test Methods são agrupados numa Testcase Class e transformados em Testcase Objects em tempo de execução
- [[wiki/sources/test-case-xunitpatterns]] — cita Test Method como o que a Testcase Class agrupa
- [[wiki/sources/annotation-xunitpatterns]] — cita Test Method como uma das duas coisas que JUnit 4.0 marca via annotation (a outra é a própria Testcase Class)
- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — documenta a exceção à regra de um Testcase Object por Test Method (NUnit 2.x, TestNG)
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — fonte primária dedicada ao padrão que nomeia o mecanismo de despacho do Test Method certo (Pluggable Method Selector)
- [[wiki/sources/reflection-xunitpatterns]] — fonte primária isolada do mecanismo que `run` usa para invocar o Test Method pelo nome
- [[wiki/sources/test-discovery-xunitpatterns]] — fonte primária dedicada ao mecanismo pelo qual o framework identifica quais métodos são Test Methods (convenção de nomenclatura vs. method attribute/annotation)
- [[wiki/sources/production-bugs-xunitpatterns]] — cataloga as formas concretas pelas quais um Test Method deixa de rodar (esquecimento de registro ou desabilitação via `[Ignore]`)
- [[wiki/sources/method-attribute-xunitpatterns]] — fonte primária dedicada ao termo genérico "method attribute", nomeando formalmente o mecanismo por trás do exemplo `[Test]` já citado acima
