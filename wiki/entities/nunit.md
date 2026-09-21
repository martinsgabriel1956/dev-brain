---
type: entity
title: "NUnit"
aliases: ["nunit"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 6
tags: [testes, xunit, dotnet, csharp, test-fixture]
skill: tech-mentor-testing
status: stub
---

# NUnit

Porta da família [[wiki/concepts/tdd|xUnit]] para .NET. Já mencionado de passagem em [[wiki/sources/annotation-xunitpatterns]] (attributes do NUnit como equivalente às annotations do JUnit 4.0) e em [[wiki/entities/junit]] (NUnit 2.0 influenciando de volta o próprio Java, com o uso de atributos elogiado por Anders Hejlsberg), mas ganha aqui sua primeira página dedicada.

## A exceção da versão 2.x

Segundo [[wiki/sources/there-is-always-an-exception-xunitpatterns]], o NUnit (versão 2.x) é um dos dois únicos membros conhecidos da família xUnit (o outro é o [[wiki/entities/testng]]) que **não** cria um [[wiki/concepts/testcase-object|Testcase Object]] separado por [[wiki/concepts/test-method|Test Method]]. Em vez disso, instancia a Testcase Class (que o NUnit chama de "test fixture") uma única vez e a reutiliza para todos os métodos de teste. [[wiki/entities/james-newkirk]], coautor do NUnit 2.0, admite publicamente que essa foi uma decisão de design equivocada: a reutilização cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito via variáveis de instância, habilitando dependência de ordem de execução entre testes. A correção paliativa adotada — tornar as variáveis de fixture `static` — não resolve o problema de raiz, apenas o torna explícito.

## Discovery via method e class attributes: `[Test]` e `[TestFixture]`

[[wiki/sources/test-discovery-xunitpatterns]] traz o primeiro exemplo de código concreto de **[[wiki/concepts/test-discovery|Test Discovery]]** via NUnit na wiki: o **method attribute** `[Test]` (composto com `[ExpectedException(...)]` no mesmo método, primeiro exemplo multi-atributo já ingerido) para **Test Method Discovery**, e o **class attribute** `[TestFixture]` para **Testcase Class Discovery** — confirmando, de fonte primária dedicada ao tema, o mesmo mecanismo já citado de passagem em [[wiki/sources/annotation-xunitpatterns]] e [[wiki/sources/attribute-xunitpatterns]]. [[wiki/sources/class-attribute-xunitpatterns]] nomeia formalmente o termo genérico "class attribute" do qual `[TestFixture]` é instância: "um attribute colocado numa classe para dizer ao compilador/runtime que ela é 'especial'". [[wiki/sources/method-attribute-xunitpatterns]] faz o mesmo para `[Test]` no nível de método, fechando o par simétrico.

## `[Ignore]` como causa de Lost Test

[[wiki/sources/production-bugs-xunitpatterns]] cita o atributo `[Ignore]` do NUnit como o exemplo concreto do mecanismo "fornecido pelo próprio xUnit" para desabilitar um Test Method — normalmente usado para destravar um build com teste falhando, e risco de virar um [[wiki/concepts/production-bugs|Lost Test]] se ninguém lembrar de reabilitá-lo depois.

## Status: stub

Conhecido até esta ingestão apenas por menções de passagem e pela exceção de instanciação documentada acima. Sem página dedicada anterior cobrindo sintaxe, atributos (`[Test]`, `[SetUp]`) ou histórico do framework em si.

## Key Sources

- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — fonte primária da exceção de instanciação do NUnit 2.x
- [[wiki/sources/annotation-xunitpatterns]] — cita NUnit como equivalente ao JUnit 4.0 via "attributes"
- [[wiki/sources/attribute-xunitpatterns]] — confirma, do verbete "attribute" em si, o mesmo mecanismo já citado em annotation-xunitpatterns
- [[wiki/sources/test-discovery-xunitpatterns]] — exemplos de código concretos de `[Test]` (Test Method Discovery) e `[TestFixture]` (Testcase Class Discovery)
- [[wiki/sources/production-bugs-xunitpatterns]] — cita `[Ignore]` como exemplo concreto do mecanismo de desabilitação de teste do NUnit
- [[wiki/sources/class-attribute-xunitpatterns]] — define formalmente o termo genérico "class attribute" do qual `[TestFixture]` é instância concreta
- [[wiki/sources/method-attribute-xunitpatterns]] — define formalmente o termo genérico "method attribute" do qual `[Test]` é instância concreta
