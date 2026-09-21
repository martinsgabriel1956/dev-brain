---
type: concept
title: "Test Suite Object"
aliases: ["objeto de suíte de teste"]
date_created: 2026-09-11
date_updated: 2026-09-21
source_count: 7
tags: [testes, testcase-class, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Test Suite Object

Coleção que agrupa todos os [[wiki/concepts/testcase-object|Testcase Objects]] produzidos por uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] atuando como Test Suite Factory — um Testcase Object por [[wiki/concepts/test-method|Test Method]]. É o objeto que o [[wiki/concepts/test-runner|Test Runner]] efetivamente consome e executa; nem a Testcase Class nem os Test Methods individuais são executados diretamente pelo runner.

[[wiki/sources/test-suite-xunitpatterns]] acrescenta a origem terminológica: o verbete de Glossário do site define "test suite", em termos deliberadamente informais, como "uma forma de nomear uma coleção de tests que se quer executar juntos" — sem comprometer-se com a representação técnica concreta (o próprio Test Suite Object) detalhada nas fontes de "XUnit Basics" abaixo.

[[wiki/sources/testcase-object-xunitpatterns]] confirma essa mecânica a partir da perspectiva do próprio Testcase Object e acrescenta que o Test Suite Object pode ser montado via **Test Discovery** ou **Test Enumeration**.

[[wiki/sources/test-result-xunitpatterns]] fecha o outro lado do ciclo de vida: o mesmo Test Suite Object "pode ser executado muitas vezes, cada uma com um **test result** diferente" — o resultado não é uma propriedade fixa da suíte montada, mas um artefato transitório de cada execução pelo Test Runner. [[wiki/sources/test-run-xunitpatterns]] nomeia formalmente esse evento de execução — texto idêntico ao de test result, tratando "rodar" (test run) e "o que se obtém ao rodar" (test result) como duas faces do mesmo fenômeno.

## Como o Test Suite Object é montado: Discovery vs. Enumeration

[[wiki/sources/test-discovery-xunitpatterns]] fecha a lacuna sinalizada abaixo: **[[wiki/concepts/test-discovery|Test Discovery]]** monta a Suite of Suites automaticamente via reflection (ou compile-time knowledge), resolvendo em cascata **Testcase Class Discovery** (achar as classes) e **Test Method Discovery** (achar os métodos dentro delas); **[[wiki/concepts/test-enumeration|Test Enumeration]]** é o registro manual equivalente, usado só quando o framework não suporta Discovery ou para montar uma Named Test Suite com subconjunto de testes escolhido a dedo.

## Quando a montagem falha: AllTests Suite e Suite of Suites como pontos de falha

[[wiki/sources/production-bugs-xunitpatterns]] cita explicitamente a **AllTests Suite** e a **Suite of Suites** como os dois lugares onde um Test Method ou uma Testcase Class podem deixar de ser registrados — produzindo um [[wiki/concepts/production-bugs|Lost Test]]. A solução mais simples apontada pela fonte não depende de Discovery: comparar a contagem de testes antes/depois do check-in e falhar o build se ela não cresceu como esperado.

## Status: stub

Conhecido pela descrição de alto nível em [[wiki/sources/testcase-class-xunitpatterns]] e [[wiki/sources/testcase-object-xunitpatterns]], e agora com a mecânica de montagem detalhada em [[wiki/sources/test-discovery-xunitpatterns]]. Ainda sem página própria dedicada a **Test Selection**, citada de passagem como filtro que pode ser aplicado depois da montagem.

## Key Sources

- [[wiki/sources/testcase-class-xunitpatterns]] — situa o Test Suite Object como o produto intermediário entre a Testcase Class (fábrica) e o Test Runner (executor)
- [[wiki/sources/testcase-object-xunitpatterns]] — confirma a mecânica pela perspectiva do Testcase Object; nomeia Test Discovery e Test Enumeration como mecanismos de criação
- [[wiki/sources/test-discovery-xunitpatterns]] — **fonte primária dedicada**: detalha os dois mecanismos de montagem (Discovery automático vs. Enumeration manual) e as duas sub-etapas de Discovery (Testcase Class Discovery, Test Method Discovery)
- [[wiki/sources/test-suite-xunitpatterns]] — verbete de Glossário do mesmo site, isolando a definição informal do próprio termo "test suite": nome dado a uma coleção de tests executados em conjunto, sem comprometer-se com a representação técnica (o Test Suite Object em si)
- [[wiki/sources/test-result-xunitpatterns]] — verbete de Glossário do mesmo site, isolando a definição do próprio termo "test result": o resultado é produto de cada execução, não propriedade fixa do Test Suite Object
- [[wiki/sources/test-run-xunitpatterns]] — verbete de Glossário do mesmo site, isolando a definição do próprio termo "test run": texto idêntico ao de test result, nomeando o evento de execução do qual o test result é o produto
- [[wiki/sources/production-bugs-xunitpatterns]] — nomeia AllTests Suite e Suite of Suites como pontos de falha de registro que produzem um Lost Test
