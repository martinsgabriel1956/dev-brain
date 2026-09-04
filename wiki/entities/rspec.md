---
type: entity
title: "RSpec"
aliases: ["rspec"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 2
tags: [testes, rspec, bdd, ruby, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# RSpec

Framework de testes para Ruby, descrito pelo xUnitPatterns.com como um dos primeiros de uma nova geração de membros da família [[wiki/concepts/tdd|xUnit]] projetados para tornar os testes escritos em [[wiki/concepts/tdd|TDD]] mais úteis como especificação executável (Tests as Specification). Sua diferença central em relação aos membros mais tradicionais da família xUnit é terminológica: abandona o vocabulário de "teste" e adota vocabulário de especificação — "fixture" vira "context" ([[wiki/sources/test-context-xunitpatterns]]), Test Method vira "specify", "assert" vira "should". Disponível originalmente em `rspec.rubyforge.org`. [[wiki/entities/jbehave|JBehave]] é citado pela mesma fonte como o equivalente em Java.

## "Context" em vez de "fixture"

[[wiki/sources/test-context-xunitpatterns]] já havia citado o RSpec de passagem, sem página própria, ao registrar que ele chama o [[wiki/concepts/indirect-input-output|test fixture]] (nomenclatura xUnit) de "context". Este verbete de glossário — dedicado ao próprio framework — fecha essa lacuna com fonte primária direta e amplia a lista de renomeações: não é só "fixture" → "context", mas todo o vocabulário de teste é substituído por vocabulário de especificação.

## Ver também

- [[wiki/concepts/tdd]]
- [[wiki/concepts/bdd]] — RSpec antecede e influencia o vocabulário de "specification" que o BDD formaliza depois com Gherkin; a fonte não faz essa ligação explicitamente
- [[wiki/entities/jbehave]]

## Key Sources

- [[wiki/sources/rspec-xunitpatterns]] — verbete de glossário dedicado ao framework
- [[wiki/sources/test-context-xunitpatterns]] — primeira menção (de passagem), sem página própria na época
