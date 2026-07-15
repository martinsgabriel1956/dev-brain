---
type: entity
title: "Martin Fowler"
aliases: ["Fowler", "martinfowler.com"]
date_created: 2026-07-07
date_updated: 2026-07-15
source_count: 3
tags: [thoughtworks, autor, testes, arquitetura, tech-debt, refactoring, agile]
skill: tech-mentor-testing
status: stable
---

# Martin Fowler

Chief Scientist da Thoughtworks, autor de *Refactoring* e *Patterns of Enterprise Application Architecture (PoEAA)*. Mantém o [bliki](https://martinfowler.com/bliki/) — cruzamento de blog e wiki — onde cunha e refina terminologia usada amplamente na indústria.

## Traço característico: precisão terminológica

Fowler é conhecido por identificar quando um termo popular carrega significados conflitantes e propor uma separação mais precisa em vez de deixar a ambiguidade se acumular — como fez com "integration test" (ver [[teste-de-integracao-estreito-vs-amplo]] e [[unit-test-solitario-vs-sociavel]]).

## Autor do livro-fonte de Refatoração

*Refactoring: Improving the Design of Existing Code* é citado em [[wiki/sources/o-que-e-refatoracao-quando-usar]] como referência para a política de tratamento de bugs encontrados durante uma refatoração: bug já conhecido e priorizado fica como está (o objetivo é reproduzir exatamente o comportamento externo pré-refatoração); bug novo pode ser corrigido na hora, mas só com certeza absoluta de que é real. O mesmo livro é citado como fonte de gráficos que argumentam que investir continuamente no design interno reduz — não aumenta — o tempo de entrega de features futuras. Ver [[wiki/concepts/refatoracao]].

## Termos e frameworks cunhados/popularizados, presentes nesta wiki

- [[teste-de-integracao-estreito-vs-amplo]] — narrow vs. broad integration test, system test
- [[unit-test-solitario-vs-sociavel]] — solitary vs. sociable unit test
- [[quadrante-de-fowler]] — categorização de tech debt (deliberado/inadvertido × prudente/imprudente)
- [[tolerant-reader]] / [[wiki/sources/tolerant-reader]] — robustez de consumers em schema evolution
- Repository e Active Record (via *PoEAA*) — ver [[design-patterns]]
- Feature Toggles — ver [[wiki/sources/feature-flags]]
- [[contract-testing]] e [[test-doubles]] — terminologia (`TestDouble`, `ContractTest`) usada de forma consistente entre suas fontes

## Anedota (não verificada): origem do ágil e projeto atrasado na Thoughtworks

[[wiki/sources/como-evitar-over-engineering-david-farley]] relata, de segunda mão e sem fonte primária citada, um projeto da Thoughtworks atrasado um ano no qual Fowler teria sido chamado para ajudar — situado como parte da origem do movimento ágil/Extreme Programming (entregar pequenos incrementos com testes automatizados, antes do termo "ágil" ser associado a processos como Scrum). Não verificado nesta wiki; ver "Open Questions" na fonte.

## Ver também

- [[piramide-de-testes]]
- [[ci-cd]] — termo "DeploymentPipeline" é dele
- [[walking-skeleton]] — padrão da mesma tradição de entrega incremental (Extreme Programming/continuous delivery)

## Key Sources

- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]]
