---
type: entity
title: "CppUnit"
aliases: ["cppunit"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [testes, xunit, cpp]
skill: tech-mentor-testing
status: stub
---

# CppUnit

Porta da família [[wiki/concepts/tdd|xUnit]] para C++, criada por Michael Feathers — segundo [[wiki/entities/junit]], provavelmente o primeiro port de JUnit para outra linguagem, ponto de partida da proliferação que deu origem ao termo "xUnit" como família. Ganha aqui sua primeira página dedicada, a partir de [[wiki/sources/test-discovery-xunitpatterns]].

## Os dois lados de Test Discovery, no mesmo framework

[[wiki/sources/test-discovery-xunitpatterns]] usa o CppUnit para ilustrar tanto o estado "antes" quanto uma forma alternativa de **[[wiki/concepts/test-discovery|Test Discovery]]**:

- **Sem Test Discovery** (versão mais antiga do tutorial): uma função `suite()` que constrói manualmente um `CppUnit::TestSuite`, registrando cada [[wiki/concepts/test-method|Test Method]] explicitamente via `addTest(new CppUnit::TestCaller<...>(...))` — o exemplo motivador que mostra o código que Test Discovery elimina.
- **Test Method Discovery via macro de compilação** (versões mais recentes): a macro `CPPUNIT_TEST_SUITE_REGISTRATION(NomeDaClasse)` gera, em **tempo de compilação**, o mesmo código de registro a partir de convenção de nomenclatura de método — uma forma de Discovery que não usa reflection em runtime, ao contrário do mecanismo genérico descrito no "How It Works" da mesma fonte.

## Status: stub

Conhecido até esta ingestão apenas por uma menção de passagem em [[wiki/entities/junit]] (autoria por Michael Feathers, papel de primeiro port). Sem página dedicada anterior cobrindo histórico completo, versões ou ecossistema do framework em si além do mecanismo de Test Discovery detalhado acima.

## Key Sources

- [[wiki/sources/test-discovery-xunitpatterns]] — **fonte primária dedicada** a este ingest: exemplo pré-Discovery e exemplo de Discovery via macro de compilação
- [[wiki/entities/junit]] — menção de passagem: CppUnit como provável primeiro port de JUnit, criado por Michael Feathers
