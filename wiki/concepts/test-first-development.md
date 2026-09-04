---
type: concept
title: "Test-First Development"
aliases: ["test first development", "desenvolvimento orientado a testes primeiro"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 3
tags: [testes, tdd, xunit]
skill: tech-mentor-testing
status: stable
---

# Test-First Development

Termo do glossário do xUnitPatterns.com ([[wiki/entities/gerard-meszaros]]) para a prática genérica de **escrever e automatizar os testes antes do código de produção**, garantindo que as responsabilidades de cada unidade fiquem claras antes de serem codificadas. É o guarda-chuva mais amplo do qual [[wiki/concepts/tdd|test-driven development]] é um caso específico: TDD acrescenta a exigência de que o código evolua **um teste de cada vez** (ver [[wiki/concepts/emergent-design]]), enquanto test-first development, por si só, não exige essa incrementalidade — é possível escrever todos os testes antes e só depois implementar o código de uma vez, e ainda assim ser "test-first".

Pode ser aplicado em dois níveis, dependendo de quais testes o time escolhe automatizar: **unit test** ou **customer test** (funcionalidade visível ao cliente — ver [[wiki/concepts/piramide-de-testes]]). Praticar test-first no nível de customer test é exatamente a definição de [[wiki/concepts/storytest-driven-development|storytest-driven development (STDD)]] — confirmado por [[wiki/sources/storytest-driven-development-xunitpatterns]], que fecha essa ligação antes só inferida por contraste.

## Key Sources

- [[wiki/sources/test-first-development-xunitpatterns]] — **fonte primária dedicada**: define o termo diretamente e acrescenta o dado dos dois níveis de aplicação (unit test / customer test)
- [[wiki/sources/test-driven-development-xunitpatterns]] — citado por contraste no verbete de TDD, sem definição própria
- [[wiki/sources/storytest-driven-development-xunitpatterns]] — confirma que test-first no nível de customer test é operacionalmente a mesma prática nomeada STDD
