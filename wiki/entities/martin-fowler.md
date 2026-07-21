---
type: entity
title: "Martin Fowler"
aliases: ["Fowler", "martinfowler.com"]
date_created: 2026-07-07
date_updated: 2026-07-20
source_count: 7
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
- [[contract-testing]] — terminologia (`ContractTest`) usada de forma consistente entre suas fontes
- [[test-doubles]] — divulgou o termo guarda-chuva "TestDouble" no bliki em 2006, mas a taxonomia dos cinco tipos (Dummy/Fake/Stub/Spy/Mock) é de autoria de [[wiki/entities/gerard-meszaros]], não dele — ver [[wiki/sources/test-double-martin-fowler]]
- [[wiki/concepts/seedwork]] — termo cunhado por ele para descrever frameworks mínimos reconstruídos por cada time, a partir de discussão originada num post de Michael Feathers
- [[wiki/concepts/application-boundary]] — tese de 2003 de que "aplicações são construções sociais", argumentando contra a previsão da época de que SOA tornaria aplicações obsoletas — ver [[wiki/sources/application-boundary-martin-fowler]]

## Testemunha e participante da origem do JUnit

Em [[wiki/sources/xunit-martin-fowler]], Fowler relata em primeira pessoa ter usado o framework de testes caseiro de [[wiki/entities/kent-beck]] no projeto [[wiki/entities/c3-project|C3]] (origem da Extreme Programming), e ter sido um dos primeiros usuários alfa do [[wiki/entities/junit]] — chegando a enviar contribuições de volta para Beck e Erich Gamma logo após sua criação em 1997.

## Future of Software Engineering Retreat

[[wiki/sources/cognitive-debt-margaret-storey]] cita uma sessão (breakout session) do "Future of Software Engineering Retreat", organizado por Fowler e a Thoughtworks, onde se discutiu que desenvolvedores precisam desacelerar e usar pair programming, refatoração e TDD para endereçar tanto dívida técnica quanto [[wiki/concepts/divida-cognitiva|dívida cognitiva]]. Citação de segunda mão — a fonte primária (o fragment de Fowler) não foi lida nesta ingestão.

## Anedota (não verificada): origem do ágil e projeto atrasado na Thoughtworks

[[wiki/sources/como-evitar-over-engineering-david-farley]] relata, de segunda mão e sem fonte primária citada, um projeto da Thoughtworks atrasado um ano no qual Fowler teria sido chamado para ajudar — situado como parte da origem do movimento ágil/Extreme Programming (entregar pequenos incrementos com testes automatizados, antes do termo "ágil" ser associado a processos como Scrum). Não verificado nesta wiki; ver "Open Questions" na fonte.

## Ver também

- [[piramide-de-testes]]
- [[ci-cd]] — termo "DeploymentPipeline" é dele
- [[walking-skeleton]] — padrão da mesma tradição de entrega incremental (Extreme Programming/continuous delivery)

## Key Sources

- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/test-double-martin-fowler]]
- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — Future of Software Engineering Retreat
- [[wiki/sources/application-boundary-martin-fowler]] — aplicações como construções sociais
