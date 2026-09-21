---
type: concept
title: "Test Discovery"
aliases: ["descoberta de testes", "testcase class discovery", "test method discovery"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 5
tags: [testes, testcase-class, test-runner, xunit, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Discovery

Mecanismo pelo qual o **Test Automation Framework** encontra automaticamente, em tempo de execução (via [[wiki/concepts/reflection|reflection]]) ou em tempo de compilação, todos os [[wiki/concepts/test-method|Test Methods]] e/ou [[wiki/concepts/test-suite-object|Test Suite Objects]] que compõem a suíte, sem que o desenvolvedor precise registrar cada teste manualmente. Fecha a lacuna, já sinalizada em [[wiki/concepts/test-suite-object]] e [[wiki/concepts/testcase-object]], sobre como o [[wiki/concepts/test-runner|Test Runner]] efetivamente sabe quais testes rodar — segundo [[wiki/sources/test-discovery-xunitpatterns]], fonte primária dedicada ao termo.

## Hierarquia de preferência: Discovery primeiro, Enumeration como fallback

A fonte estabelece uma ordem de preferência explícita, não duas técnicas equivalentes: usar *Test Discovery* sempre que o framework suportar. A alternativa manual, **[[wiki/concepts/test-enumeration|Test Enumeration]]**, só se justifica em dois cenários específicos: (a) o framework não suporta Discovery, ou (b) o time quer montar uma **Named Test Suite** — um subconjunto de testes escolhidos a dedo de várias suítes, como uma suíte de *Smoke Test* — e o framework também não suporta **Test Selection**. É comum combinar Test *Suite* Enumeration manual com Test *Method* Discovery automático; o inverso é raro.

## Duas descobertas em cascata: classe primeiro, método depois

Montar a **Suite of Suites** que o Test Runner executa exige resolver dois problemas (não necessariamente nessa ordem):

### Testcase Class Discovery

Como o framework encontra as [[wiki/sources/testcase-class-xunitpatterns|Testcase Classes]] sobre as quais fazer Test Method Discovery. Quatro mecanismos, cada um com um trade-off de acoplamento diferente:

1. Subclassificar uma **Testcase Superclass**, ou implementar uma **[[wiki/concepts/marker-interface|Marker Interface]]** [PJV1] — acopla via herança/tipo.
2. **Class attribute** (ex.: `[TestFixture]`, NUnit) ou **annotation** (ex.: `@Testcase`) — acopla via metadado declarativo, sem herança forçada. Mecanismo já detalhado em [[wiki/sources/annotation-xunitpatterns]] e [[wiki/sources/attribute-xunitpatterns]]; [[wiki/sources/class-attribute-xunitpatterns]] nomeia e define formalmente o termo genérico ("um attribute colocado numa classe para dizer ao compilador/runtime que ela é 'especial'"), do qual `[TestFixture]` é uma instância concreta.
3. Diretório comum apontado ao Test Runner — acoplamento zero ao código-fonte, total à convenção de organização de arquivos.
4. Convenção de nomenclatura de arquivo, resolvida por um programa externo. O exemplo em Ruby desta fonte (`Dir['tests/*.rb'].each { |f| require f }`) implementa exatamente essa variante: o `Dir['tests/*.rb']` faz a Testcase Class Discovery, e o `require` delega a Test Method Discovery ao interpretador Ruby e ao `Test::Unit`.

### Test Method Discovery

Como o framework encontra os [[wiki/concepts/test-method|Test Methods]] dentro de uma Testcase Class já descoberta. Duas formas básicas, na mesma dualidade nomenclatura vs. metadado vista acima:

- **Convenção de nomenclatura** — prefixo `"test"` (ex.: `testCounters`), a forma mais tradicional (JUnit 3 e xUnit legado em geral). O framework itera sobre todos os métodos da classe, filtra os que começam com `"test"`, e chama o construtor de um argumento para criar o [[wiki/concepts/testcase-object|Testcase Object]] correspondente.
- **Method attribute** (`[Test]`, NUnit/.NET) ou **annotation** (`@Test`, JUnit 4+) — o exemplo em C# desta fonte mostra dois method attributes compostos no mesmo método (`[Test]` + `[ExpectedException(...)]`), primeiro exemplo multi-atributo concreto na wiki. [[wiki/sources/method-attribute-xunitpatterns]] nomeia e define formalmente o termo genérico ("um attribute colocado num método para dizer ao compilador/runtime que ele é 'especial'"), do qual `[Test]` é uma instância concreta — espelhando o já fechado para class attribute/`[TestFixture]` acima.

## CppUnit: os dois lados da mesma moeda

A fonte usa o [[wiki/entities/cppunit|CppUnit]] para ilustrar tanto o estado "pré-Discovery" quanto uma forma alternativa de Discovery:

- **Sem Test Discovery**: um exemplo de código legado do CppUnit mostra o trabalho manual que Test Discovery elimina — uma função `suite()` que registra explicitamente cada `Test Method`, via `addTest`/`TestCaller`, um por um. É o motivador ("Motivating Example") de todo o verbete: mostrar o código que desaparece quando o framework passa a suportar Discovery.
- **Discovery via macro de compilação**: uma versão mais recente do CppUnit usa a macro `CPPUNIT_TEST_SUITE_REGISTRATION`, que gera esse mesmo código de registro em **tempo de compilação**, a partir de convenção de nomenclatura de método — uma forma de Test Method Discovery resolvida estaticamente, sem reflection em runtime. Isso contraria, na prática, a formulação inicial de "How It Works", que cita apenas reflection como mecanismo — a fonte não nomeia a via de compile time com o mesmo detalhe, tratando-a como nota lateral.

## Refatoração de migração: Rename Method

Ao adotar um framework existente, a recomendação é seguir a convenção de descoberta que ele já implementa: se for por nome, pode ser necessário um **[[wiki/concepts/rename-method|Rename Method]]** [Fowler] para que os Test Methods existentes passem a ser descobertos; se for por atributo, basta adicionar o atributo correspondente. [[wiki/sources/rename-method-xunitpatterns]] agora dá fonte primária isolada à refatoração em si: "o nome de um método não revela seu propósito" → "mude o nome do método" — verbete genérico, sem menção a teste; a aplicação a Test Method Discovery é feita inteiramente por esta fonte.

## Consequência quando falha: Lost Test

[[wiki/sources/production-bugs-xunitpatterns]] nomeia o sintoma que ocorre quando a Test Discovery falha silenciosamente ou é contornada: um [[wiki/concepts/production-bugs|Lost Test]] — um Test Method que deixa de corresponder à convenção de nomenclatura (renomeação acidental) ou uma Testcase Class que nunca foi registrada na `AllTests Suite`. A fonte lista isso como uma causa raiz irmã de **Test Enumeration** malfeita (esquecer `suite.addTest`), reforçando por que a preferência por Discovery automático reduz esse risco.

## Status: stable

Primeira fonte primária dedicada ao termo na wiki — fecha a lacuna estrutural que três páginas diferentes ([[wiki/concepts/test-suite-object]], [[wiki/concepts/testcase-object]], [[wiki/sources/testcase-class-xunitpatterns]]) já sinalizavam como pendente. A técnica-irmã, **[[wiki/concepts/test-enumeration|Test Enumeration]]**, segue como stub — citada extensivamente aqui por contraste, mas ainda sem verbete de glossário dedicado ingerido.

## Key Sources

- [[wiki/sources/test-discovery-xunitpatterns]] — **fonte primária dedicada**: mecânica completa (Testcase Class Discovery + Test Method Discovery), hierarquia Discovery vs. Enumeration, seis exemplos de código (C++/CppUnit, Java/JUnit, C#/NUnit, Ruby)
- [[wiki/concepts/test-suite-object]] — consumidor da montagem via Test Discovery; sinalizava a lacuna antes desta ingestão
- [[wiki/concepts/testcase-object]] — Test Discovery era um dos dois mecanismos de criação apenas nomeados antes desta ingestão
- [[wiki/sources/testcase-class-xunitpatterns]] — descreve a mecânica de alto nível (Testcase Class como Test Suite Factory) que esta fonte detalha do lado da descoberta
- [[wiki/sources/production-bugs-xunitpatterns]] — nomeia Lost Test como o sintoma resultante de falhas nesse mecanismo
- [[wiki/sources/class-attribute-xunitpatterns]] — fonte primária dedicada ao termo genérico "class attribute", do qual `[TestFixture]` (NUnit) é a instância concreta já documentada
- [[wiki/sources/method-attribute-xunitpatterns]] — fonte primária dedicada ao termo genérico "method attribute", do qual `[Test]` (NUnit) é a instância concreta já documentada
- [[wiki/sources/rename-method-xunitpatterns]] — fonte primária dedicada à refatoração Rename Method, citada aqui como técnica de migração quando Test Method Discovery é feita por convenção de nomenclatura
