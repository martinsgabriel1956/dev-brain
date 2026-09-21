---
type: concept
title: "Testcase Object"
aliases: ["objeto de caso de teste", "test as command"]
date_created: 2026-09-11
date_updated: 2026-09-21
source_count: 8
tags: [testes, testcase-class, xunit, command-pattern, gof, terminologia]
skill: tech-mentor-testing
status: stable
---

# Testcase Object

Instância de uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]], criada em tempo de execução — uma para cada [[wiki/concepts/test-method|Test Method]]. É o mecanismo concreto por trás da reclassificação já registrada em [[wiki/sources/test-case-xunitpatterns]] de que a Testcase Class "é na verdade" uma **Test Suite Factory**: ao instanciar-se uma vez por Test Method, a fábrica produz um Testcase Object por método, e todos eles são agrupados num [[wiki/concepts/test-suite-object|Test Suite Object]] que o [[wiki/concepts/test-runner|Test Runner]] executa.

## Cada teste é um Command [GOF]

[[wiki/sources/testcase-object-xunitpatterns]], fonte primária dedicada ao termo, resolve o problema "como executamos os testes?" respondendo: cada Testcase Object **é** um objeto **[[wiki/concepts/command-pattern|Command]]** [GOF]. Ele implementa uma interface de teste padrão — em particular, um método `run` — de modo que o Test Runner não precisa conhecer a interface específica de cada teste individual; basta invocar `run` uniformemente sobre qualquer Testcase Object da coleção. É esse encapsulamento (tratar um teste como um objeto de primeira classe, e não como um procedimento solto) que permite manter Testcase Objects em coleções (Test Suite Object), iterar sobre eles, contá-los, exibi-los — tudo o que um framework precisa fazer com um conjunto de testes. [[wiki/sources/command-xunitpatterns]] fornece, à parte, a definição formal do GOF para o padrão — confirma que essa aplicação usa apenas a faceta de "objetificar uma chamada", sem queue/log/undo.

## Mecânica de despacho: Pluggable Behavior + reflection

Como a maioria das linguagens exige uma classe para definir o comportamento do Testcase Object, e é mais conveniente hospedar vários Test Methods numa única Testcase Class (menos classes para gerenciar, reuso de [[wiki/sources/testcase-class-xunitpatterns|Test Utility Methods]] mais fácil) do que criar uma classe por teste, surge um problema: como cada Testcase Object sabe qual Test Method específico deve invocar? A resposta, segundo a fonte, é **[[wiki/concepts/pluggable-behavior|Pluggable Behavior]]** [SBPP, Kent Beck]: o construtor da Testcase Class recebe o nome do método a ser executado como parâmetro, e o armazena numa variável de instância. Quando o Test Runner chama `run` sobre o Testcase Object, ele usa **[[wiki/concepts/reflection|reflection]]** para localizar e invocar o método cujo nome está guardado ali — mecanismo hoje com fonte primária isolada em [[wiki/sources/reflection-xunitpatterns]]. [[wiki/sources/pluggable-behavior-xunitpatterns]], fonte primária dedicada ao padrão (que aqui só era citado de passagem), classifica precisamente esse uso: é um **Pluggable (Method) Selector** — o construtor escolhe entre métodos já existentes na classe pelo nome — e não um **Pluggable Block**, a outra variação do padrão, onde seria injetado um bloco de código arbitrário em vez de um nome.

## Convenção de nomenclatura no Test Tree Explorer

No exemplo do [[wiki/entities/junit]] rodando dentro do **Graphical Test Runner** do Eclipse (**Test Tree Explorer**), o nome fora dos parênteses é o nome da classe, e a string dentro dos parênteses é o nome do objeto criado a partir dela. Por convenção, o nome de um Testcase Object é o nome do Test Method que ele executa; o nome de um [[wiki/concepts/test-suite-object|Test Suite Object]] é a string passada ao construtor no momento da criação.

## A regra de "um por Test Method" — e a exceção

[[wiki/sources/there-is-always-an-exception-xunitpatterns]] eleva essa regra ("um Testcase Object por Test Method") a mecanismo de design fundamental do xUnit para alcançar Independent Test, e documenta a única exceção conhecida pelo autor: [[wiki/entities/nunit|NUnit]] (2.x) e [[wiki/entities/testng|TestNG]] instanciam a Testcase Class **uma única vez** e a reutilizam para todos os Test Methods, em vez de criar um Testcase Object separado a cada um. [[wiki/entities/james-newkirk]], coautor do NUnit 2.0, admite que essa foi uma decisão de design equivocada — a reutilização cria um [[wiki/concepts/shared-fixture|Shared Fixture]] implícito, habilitando dependência de ordem de execução entre testes ([[wiki/concepts/erratic-test|Erratic Test]]).

## Como os Testcase Objects são criados

[[wiki/sources/testcase-object-xunitpatterns]] cita **Test Discovery** e **Test Enumeration** como os dois mecanismos possíveis para criar os Testcase Objects de uma Testcase Class, sem detalhar nenhum dos dois — lacuna fechada por [[wiki/sources/test-discovery-xunitpatterns]], fonte primária dedicada ingerida em 2026-09-21: **[[wiki/concepts/test-discovery|Test Discovery]]** é o caminho automático (reflection em runtime ou conhecimento em compile-time), preferido sempre que o framework suportar; **[[wiki/concepts/test-enumeration|Test Enumeration]]** é o registro manual, reservado a frameworks sem suporte a Discovery ou a suítes nomeadas com subconjunto de testes escolhido a dedo.

## Quando o objeto nunca chega a existir: Lost Test

[[wiki/sources/production-bugs-xunitpatterns]] nomeia o caso em que um Testcase Object nunca chega a ser criado: se o Test Method correspondente não é descoberto (falha de nomenclatura/atributo) nem enumerado manualmente (`suite.addTest` esquecido), simplesmente não existe Testcase Object para ele — sintoma catalogado como [[wiki/concepts/production-bugs|Lost Test]].

## Key Sources

- [[wiki/sources/testcase-object-xunitpatterns]] — **fonte primária dedicada**: Command pattern, Pluggable Behavior + reflection, convenção de nomenclatura, Test Discovery/Test Enumeration
- [[wiki/sources/testcase-class-xunitpatterns]] — descreve o Testcase Object como o produto da Testcase Class atuando como Test Suite Factory, um por Test Method
- [[wiki/sources/there-is-always-an-exception-xunitpatterns]] — documenta a regra "um por Test Method" como mecanismo de Independent Test, e a exceção do NUnit 2.x/TestNG
- [[wiki/sources/command-xunitpatterns]] — fonte primária isolada da definição formal do GOF para o Command, o padrão do qual o Testcase Object é uma aplicação parcial
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — fonte primária isolada da definição formal do padrão citado de passagem acima; classifica o despacho como Pluggable (Method) Selector, não Pluggable Block
- [[wiki/sources/reflection-xunitpatterns]] — fonte primária isolada do mecanismo usado por `run` para localizar e invocar o Test Method pelo nome
- [[wiki/sources/test-discovery-xunitpatterns]] — fecha a lacuna de como Testcase Objects são criados: Test Discovery (automático) vs. Test Enumeration (manual), detalhados com fonte primária dedicada
- [[wiki/sources/production-bugs-xunitpatterns]] — nomeia o caso em que o Testcase Object nunca chega a ser criado (Lost Test)
