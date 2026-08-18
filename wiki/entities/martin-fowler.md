---
type: entity
title: "Martin Fowler"
aliases: ["Fowler", "martinfowler.com"]
date_created: 2026-07-07
date_updated: 2026-08-18
source_count: 17
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

## A 2ª edição de Refactoring (20 anos depois)

Segundo [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]], Fowler explicou numa entrevista com uma funcionária brasileira da [[wiki/entities/thoughtworks]] os motivos da 2ª edição de *Refactoring*, lançada 20 anos após a primeira: o código de exemplo tinha ficado datado (Java antigo, com uso de classes como `Vector`, hoje em desuso), e várias refatorações do livro original estavam demais atreladas ao paradigma orientado a objetos, apesar de refatoração valer para qualquer paradigma. A nova edição passou a usar JavaScript e trocou o exemplo didático central — de uma locadora de fitas de vídeo para um sistema de gestão de peças de teatro — escolhido por ser um domínio mais permanente da atividade humana (peças de teatro existem desde a Grécia Antiga), o que aumenta a durabilidade didática do livro. Ver [[wiki/concepts/essential-complexity]] e [[wiki/concepts/accidental-complexity]] — a fonte usa esse caso como prova de que tecnologia é acidental e princípios de design são essenciais.

**Nota de contradição:** essa mesma fonte afirma que a Thoughtworks "foi fundada também pelo Martin Fowler". Isso contradiz o que já está registrado nesta entity (Fowler é Chief Scientist, não fundador da empresa) — tratado como possível imprecisão do autor do vídeo, não como fato verificado. Ver open questions em [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]].

## Termos e frameworks cunhados/popularizados, presentes nesta wiki

- [[teste-de-integracao-estreito-vs-amplo]] — narrow vs. broad integration test, system test
- [[unit-test-solitario-vs-sociavel]] — solitary vs. sociable unit test
- [[quadrante-de-fowler]] — categorização de tech debt (deliberado/inadvertido × prudente/imprudente)
- [[tolerant-reader]] / [[wiki/sources/tolerant-reader]] — robustez de consumers em schema evolution
- Repository e Active Record (via *PoEAA*) — ver [[design-patterns]]
- Feature Toggles — ver [[wiki/sources/feature-flags]]
- [[contract-testing]] — terminologia (`ContractTest`) usada de forma consistente entre suas fontes; artigo próprio original chamava-se "Integration Contract Test", renomeado depois para "Contract Test" quando o termo mais curto ganhou adoção na indústria — ver [[wiki/sources/contract-test-martin-fowler]]
- [[wiki/concepts/self-initializing-fake]] — recomenda esse padrão de Fake auto-validável como técnica para construir doubles usados em contract tests
- [[wiki/concepts/monolith-first]] — princípio (bliki, martinfowler.com/bliki/MonolithFirst.html) de que projetos novos não devem começar com microsserviços; formulado a partir da observação de que quase toda história de microsserviços bem-sucedida começou como monolito, e quase todo sistema que nasceu já distribuído teve sérios problemas — ver [[wiki/sources/microsservicos-monolito-first-renato-augusto]]
- [[test-doubles]] — divulgou o termo guarda-chuva "TestDouble" no bliki em 2006, mas a taxonomia dos cinco tipos (Dummy/Fake/Stub/Spy/Mock) é de autoria de [[wiki/entities/gerard-meszaros]], não dele — ver [[wiki/sources/test-double-martin-fowler]] (relato de Fowler) e agora também a **fonte primária** de Meszaros em [[wiki/sources/test-double-xunitpatterns-meszaros]]
- [[wiki/concepts/seedwork]] — termo cunhado por ele para descrever frameworks mínimos reconstruídos por cada time, a partir de discussão originada num post de Michael Feathers
- [[wiki/concepts/application-boundary]] — tese de 2003 de que "aplicações são construções sociais", argumentando contra a previsão da época de que SOA tornaria aplicações obsoletas — ver [[wiki/sources/application-boundary-martin-fowler]]
- [[wiki/concepts/microsservicos]] — coautor (com [[wiki/entities/james-lewis]]) do artigo de 2014 que cunhou a definição do termo hoje citada universalmente na indústria; mesma característica de precisão terminológica descrita acima aparece aqui como recusa a declarar microsserviços "o futuro" sem ressalvas — ver [[wiki/sources/microsservicos-martin-fowler-james-lewis]]
- [[wiki/concepts/cqrs]] — post do bliki (2011) que popularizou a definição mais citada do termo; mesmo traço de cautela terminológica aparece aqui como reserva explícita ("a maioria das implementações que vi foi problemática") e como restrição de escopo a [[wiki/concepts/bounded-context]] — ver [[wiki/sources/cqrs-martin-fowler]]

## Hospeda, mas não escreve: Consumer-Driven Contracts

[[wiki/sources/consumer-driven-contracts-martin-fowler]] (2006) é um artigo publicado no site de Fowler mas escrito por [[wiki/entities/ian-robinson]], da Thoughtworks — cunha o padrão Consumer-Driven Contracts, hoje frequentemente associado ao nome de Fowler por estar no seu domínio. A distinção autor vs. host é registrada explicitamente na fonte, na mesma linha da precisão terminológica que caracteriza este entity (ver seção acima).

## Testemunha e participante da origem do JUnit

Em [[wiki/sources/xunit-martin-fowler]], Fowler relata em primeira pessoa ter usado o framework de testes caseiro de [[wiki/entities/kent-beck]] no projeto [[wiki/entities/c3-project|C3]] (origem da Extreme Programming), e ter sido um dos primeiros usuários alfa do [[wiki/entities/junit]] — chegando a enviar contribuições de volta para Beck e Erich Gamma logo após sua criação em 1997.

## Future of Software Engineering Retreat

[[wiki/sources/cognitive-debt-margaret-storey]] cita uma sessão (breakout session) do "Future of Software Engineering Retreat", organizado por Fowler e a Thoughtworks, onde se discutiu que desenvolvedores precisam desacelerar e usar pair programming, refatoração e TDD para endereçar tanto dívida técnica quanto [[wiki/concepts/divida-cognitiva|dívida cognitiva]]. Citação de segunda mão — a fonte primária (o fragment de Fowler) não foi lida nesta ingestão.

## Anedota (não verificada): origem do ágil e projeto atrasado na Thoughtworks

[[wiki/sources/como-evitar-over-engineering-david-farley]] relata, de segunda mão e sem fonte primária citada, um projeto da Thoughtworks atrasado um ano no qual Fowler teria sido chamado para ajudar — situado como parte da origem do movimento ágil/Extreme Programming (entregar pequenos incrementos com testes automatizados, antes do termo "ágil" ser associado a processos como Scrum). Não verificado nesta wiki; ver "Open Questions" na fonte.

## "Quem precisa de um arquiteto?" e a definição de arquitetura de Ralph Johnson

[[wiki/sources/arquitetura-limpa-na-pratica]] abre discutindo definições de arquitetura de software e cita o artigo de Fowler para a IEEE Software (2003), *Who Needs an Architect?*, no qual ele recolhe a definição de Ralph Johnson: arquitetura é o "entendimento compartilhado" que os desenvolvedores mais experientes de um projeto têm sobre a divisão do sistema em componentes e como esses componentes interagem via interfaces. O mesmo livro também usa o padrão **Unit of Work** de Fowler (*PoEAA*) como alternativa ao Repository simples para lidar com concorrência — ver [[wiki/concepts/repository-pattern]].

## Ver também

- [[piramide-de-testes]]
- [[ci-cd]] — termo "DeploymentPipeline" é dele
- [[walking-skeleton]] — padrão da mesma tradição de entrega incremental (Extreme Programming/continuous delivery)

## Key Sources

- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/contract-test-martin-fowler]]
- [[wiki/sources/test-double-martin-fowler]]
- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — Future of Software Engineering Retreat
- [[wiki/sources/application-boundary-martin-fowler]] — aplicações como construções sociais
- [[wiki/sources/talk-about-platforms-evan-bottcher]] — artigo de [[wiki/entities/evan-bottcher]] (2018) **hospedado** no site de Fowler; define [[wiki/concepts/plataforma-digital|plataforma digital]] (mesmo padrão host≠autor de Consumer-Driven Contracts / Ian Robinson)
- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] — motivos da 2ª edição de Refactoring, 20 anos depois
- [[wiki/sources/consumer-driven-contracts-martin-fowler]] — artigo de Ian Robinson hospedado no site de Fowler, não escrito por ele
- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] — revisita o Quadrante de Fowler e acrescenta camada de mensuração formal (debt ratio/SQALE) e alocação de tempo (regra dos 20%/25%)
- [[wiki/sources/microsservicos-martin-fowler-james-lewis]] — artigo de 2014 que cunhou a definição de microsserviços, coautoria com [[wiki/entities/james-lewis]]
- [[wiki/sources/arquitetura-limpa-na-pratica]] — definição de arquitetura de Ralph Johnson (via artigo de Fowler "Who Needs an Architect?"); Unit of Work como alternativa ao Repository simples
- [[wiki/sources/cqrs-martin-fowler]] — post original do bliki (2011) que popularizou a definição de CQRS; tom de cautela contra aplicar o padrão ao sistema inteiro
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — princípio Monolith First (bliki), atribuído via fonte secundária (transcrição de Renato Augusto, sem link direto ao artigo original)
