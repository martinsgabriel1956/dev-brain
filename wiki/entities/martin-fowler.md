---
type: entity
title: "Martin Fowler"
aliases: ["Fowler", "martinfowler.com"]
date_created: 2026-07-07
date_updated: 2026-08-23
source_count: 26
tags: [thoughtworks, autor, testes, arquitetura, tech-debt, refactoring, agile]
skill: tech-mentor-testing
status: stable
---

# Martin Fowler

Chief Scientist da Thoughtworks, autor de *Refactoring* e *Patterns of Enterprise Application Architecture (PoEAA)*. Mantém o [bliki](https://martinfowler.com/bliki/) — cruzamento de blog e wiki — onde cunha e refina terminologia usada amplamente na indústria.

## Curador de folclore de engenharia, não só de terminologia

Além de cunhar e refinar termos técnicos, Fowler mantém páginas de bliki que curam **folclore** da profissão — em [[wiki/sources/two-hard-things-martin-fowler]] (2009) ele registra a citação clássica de [[wiki/entities/phil-karlton]] sobre naming e cache invalidation como os dois problemas difíceis da Ciência da Computação, junto com variações (*riffs*) coletadas de outras pessoas ao longo de mais de uma década, admitindo abertamente que nunca confirmou a atribuição original a Karlton com uma fonte primária. Ver [[wiki/concepts/two-hard-things]].

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
- [[wiki/concepts/self-initializing-fake]] — bliki próprio de 2009 ([[wiki/sources/self-initializing-fake-martin-fowler]]) detalhando o padrão: um Fake que na primeira chamada encaminha ao serviço real e grava a resposta em cache, servindo daí em diante; recomendado depois, em 2011, como técnica para construir doubles usados em contract tests
- [[wiki/concepts/monolith-first]] — princípio (bliki, 2015, martinfowler.com/bliki/MonolithFirst.html) de que projetos novos não devem começar com microsserviços; formulado a partir da observação de que quase toda história de microsserviços bem-sucedida começou como monolito, e quase todo sistema que nasceu já distribuído teve sérios problemas; sustentado por YAGNI e pela dificuldade de acertar bounded contexts no início — ver a fonte primária [[wiki/sources/monolith-first-martin-fowler]]
- [[test-doubles]] — divulgou o termo guarda-chuva "TestDouble" no bliki em 2006, mas a taxonomia dos cinco tipos (Dummy/Fake/Stub/Spy/Mock) é de autoria de [[wiki/entities/gerard-meszaros]], não dele — ver [[wiki/sources/test-double-martin-fowler]] (relato de Fowler) e agora também a **fonte primária** de Meszaros em [[wiki/sources/test-double-xunitpatterns-meszaros]]
- [[wiki/concepts/seedwork]] — termo cunhado por ele para descrever frameworks mínimos reconstruídos por cada time, a partir de discussão originada num post de Michael Feathers; fonte primária agora ingerida em [[wiki/sources/seedwork-martin-fowler]], publicada no mesmo dia (2003-09-11) que [[wiki/sources/application-boundary-martin-fowler]] e reutilizando a mesma tese central (ApplicationBoundary como construção social) para explicar por que reuso de código entre aplicações é difícil
- [[wiki/concepts/application-boundary]] — tese de 2003 de que "aplicações são construções sociais", argumentando contra a previsão da época de que SOA tornaria aplicações obsoletas — ver [[wiki/sources/application-boundary-martin-fowler]]
- [[wiki/concepts/microsservicos]] — coautor (com [[wiki/entities/james-lewis]]) do artigo de 2014 que cunhou a definição do termo hoje citada universalmente na indústria; mesma característica de precisão terminológica descrita acima aparece aqui como recusa a declarar microsserviços "o futuro" sem ressalvas — ver [[wiki/sources/microsservicos-martin-fowler-james-lewis]]
- [[wiki/concepts/cqrs]] — post do bliki (2011) que popularizou a definição mais citada do termo; mesmo traço de cautela terminológica aparece aqui como reserva explícita ("a maioria das implementações que vi foi problemática") e como restrição de escopo a [[wiki/concepts/bounded-context]] — ver [[wiki/sources/cqrs-martin-fowler]]

## Hospeda, mas não escreve: Consumer-Driven Contracts

[[wiki/sources/consumer-driven-contracts-martin-fowler]] (2006) é um artigo publicado no site de Fowler mas escrito por [[wiki/entities/ian-robinson]], da Thoughtworks — cunha o padrão Consumer-Driven Contracts, hoje frequentemente associado ao nome de Fowler por estar no seu domínio. A distinção autor vs. host é registrada explicitamente na fonte, na mesma linha da precisão terminológica que caracteriza este entity (ver seção acima).

## Testemunha e participante da origem do JUnit

Em [[wiki/sources/xunit-martin-fowler]], Fowler relata em primeira pessoa ter usado o framework de testes caseiro de [[wiki/entities/kent-beck]] no projeto [[wiki/entities/c3-project|C3]] (origem da Extreme Programming), e ter sido um dos primeiros usuários alfa do [[wiki/entities/junit]] — chegando a enviar contribuições de volta para Beck e Erich Gamma logo após sua criação em 1997.

## Consultor no C3 desde 1993

[[wiki/sources/c3-martin-fowler]] é o relato dedicado de Fowler sobre o projeto [[wiki/entities/c3-project|C3]], onde ele próprio atuou como consultor a partir de 1993 — dois anos antes do início do desenvolvimento em Smalltalk e três antes do recomeço de 1996 que consolidou a [[wiki/concepts/extreme-programming|Extreme Programming]]. Ele nota que faltam análises confiáveis sobre o projeto vindas de quem participou em tempo integral, e reafirma (como já fizera em [[wiki/sources/xunit-martin-fowler]]) que a página da Wikipedia sobre o C3 é enganosa.

## Cunhou "Very Low Defect Project" (2004)

[[wiki/sources/very-low-defect-project-martin-fowler]] — bliki de janeiro de 2004, publicado sete meses antes do relato dedicado ao C3 — em que Fowler observa e nomeia a tendência de times de [[wiki/concepts/extreme-programming|Extreme Programming]] com menos de um bug em produção por mês, a partir de quatro casos (incluindo ex-colegas do [[wiki/entities/c3-project|C3]] e projetos-candidato da própria [[wiki/entities/thoughtworks]]). Mesmo traço de cautela terminológica descrito acima: ele evita afirmar que XP garante o resultado ou que outros processos não conseguiriam o mesmo. Ver [[wiki/concepts/very-low-defect-project]].

## Future of Software Engineering Retreat

[[wiki/sources/cognitive-debt-margaret-storey]] cita uma sessão (breakout session) do "Future of Software Engineering Retreat", organizado por Fowler e a Thoughtworks, onde se discutiu que desenvolvedores precisam desacelerar e usar pair programming, refatoração e TDD para endereçar tanto dívida técnica quanto [[wiki/concepts/divida-cognitiva|dívida cognitiva]]. Citação de segunda mão — a fonte primária (o fragment de Fowler) não foi lida nesta ingestão.

## Anedota (não verificada): origem do ágil e projeto atrasado na Thoughtworks

[[wiki/sources/como-evitar-over-engineering-david-farley]] relata, de segunda mão e sem fonte primária citada, um projeto da Thoughtworks atrasado um ano no qual Fowler teria sido chamado para ajudar — situado como parte da origem do movimento ágil/Extreme Programming (entregar pequenos incrementos com testes automatizados, antes do termo "ágil" ser associado a processos como Scrum). Não verificado nesta wiki; ver "Open Questions" na fonte.

## "Quem precisa de um arquiteto?" e a definição de arquitetura de Ralph Johnson

[[wiki/sources/arquitetura-limpa-na-pratica]] abre discutindo definições de arquitetura de software e cita o artigo de Fowler para a IEEE Software (2003), *Who Needs an Architect?*, no qual ele recolhe a definição de Ralph Johnson: arquitetura é o "entendimento compartilhado" que os desenvolvedores mais experientes de um projeto têm sobre a divisão do sistema em componentes e como esses componentes interagem via interfaces. O mesmo livro também usa o padrão **[[wiki/concepts/unit-of-work|Unit of Work]]** de Fowler (*PoEAA*) como alternativa ao Repository simples para lidar com concorrência — ver [[wiki/concepts/repository-pattern]].

## Unit of Work (PoEAA): mecanismo completo demonstrado com SQLAlchemy

[[wiki/sources/unit-of-work-padrao-de-design]] detalha o padrão de Fowler independentemente da menção acima: um ponto de coleta que acumula operações (criar, atualizar, remover) e as aplica todas de uma vez num `commit`, com `rollback` desfazendo o lote inteiro se qualquer operação falhar. Demonstrado com uma implementação artesanal em Python e depois com SQLAlchemy, onde o objeto `Session` é a implementação real do padrão — ver [[wiki/concepts/unit-of-work]].

## Unit of Work: fonte primária (eaaCatalog)

[[wiki/sources/unit-of-work-martin-fowler]] é a própria página do padrão no catálogo online de *PoEAA* (martinfowler.com/eaaCatalog), publicada em 05 de março de 2003 — a definição formal citada acima ("mantém uma lista de objetos afetados por uma transação de negócio e coordena a escrita das alterações e a resolução de problemas de concorrência") vem diretamente dela. É apenas o resumo do catálogo; remete ao Capítulo 11 do ebook para o detalhamento, não lido nesta ingestão.

## Cunhou "Continuous Delivery" formalmente, com ajuda de Jez Humble

[[wiki/sources/continuous-delivery-martin-fowler]] (bliki, mesma data de 2013 que o de Deployment Pipeline) define o termo "Continuous Delivery" propriamente dito: a capacidade — não o ato — de lançar software em produção a qualquer momento, com quatro indicadores concretos desenvolvidos pelo grupo de trabalho de CD da [[wiki/entities/thoughtworks]]. Fowler separa a disciplina com precisão de Continuous Deployment (mesmo traço de precisão terminológica descrito acima), e credita [[wiki/entities/jez-humble]] com "ajuda detalhada" na redação da própria página — Humble e [[wiki/entities/david-farley]] são citados como autores do livro fundacional *Continuous Delivery*. É também aqui que Fowler cunha, via nota de rodapé, a leitura ampla de "[[wiki/concepts/devops-culture|DevOps culture]]" (além de dev+ops) como um dos dois requisitos de CD, ao lado da automação via deployment pipeline.

## Ver também

- [[piramide-de-testes]]
- [[ci-cd]] — termo "DeploymentPipeline" é dele (bliki de 2013, fonte primária agora ingerida em [[wiki/sources/deployment-pipeline-martin-fowler]]): estágios progressivos por confiança, escopo além de testes (performance/segurança/usabilidade), colaboração e trilha de auditoria
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
- [[wiki/sources/unit-of-work-padrao-de-design]] — Unit of Work (PoEAA) detalhado: mecanismo de commit/rollback em lote, implementação artesanal em Python e exemplo real com SQLAlchemy
- [[wiki/sources/unit-of-work-martin-fowler]] — fonte primária: página do padrão no eaaCatalog (05 mar 2003), definição formal do próprio Fowler
- [[wiki/sources/cqrs-martin-fowler]] — post original do bliki (2011) que popularizou a definição de CQRS; tom de cautela contra aplicar o padrão ao sistema inteiro
- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária do bliki Monolith First (2015): MicroservicePremium, YAGNI, dificuldade de bounded contexts, quatro caminhos práticos de execução
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — princípio Monolith First (bliki), atribuído via fonte secundária (transcrição de Renato Augusto, sem link direto ao artigo original)
- [[wiki/sources/seedwork-martin-fowler]] — bliki de 2003 sobre reuso via frameworks mínimos ("seedwork"); reabilita parcialmente reuso por copiar-e-colar como alternativa pragmática quando um bom framework compartilhado não está disponível
- [[wiki/sources/self-initializing-fake-martin-fowler]] — bliki de 2009: mecanismo do Fake que se autoinicializa contra o serviço real na primeira chamada e passa a servir do cache; publicado cerca de um ano e meio antes de recomendar o padrão em [[wiki/sources/contract-test-martin-fowler]] (2011)
- [[wiki/sources/two-hard-things-martin-fowler]] — bliki de 2009, mantido como página viva: citação de Phil Karlton (naming + cache invalidation), atribuição nunca confirmada, quatro riffs coletados entre 2010 e 2021
- [[wiki/sources/c3-martin-fowler]] — relato dedicado ao projeto C3, onde Fowler atuou como consultor desde 1993; linha do tempo completa e a tese de que "XP não é garantia de sucesso"
- [[wiki/sources/very-low-defect-project-martin-fowler]] — bliki de 2004 que cunha o termo VeryLowDefectProject a partir de quatro casos observados, incluindo ex-colegas do C3 e Thoughtworks
- [[wiki/sources/deployment-pipeline-martin-fowler]] — bliki de 2013 que cunha "Deployment Pipeline": estágios progressivos por confiança, escopo além de testes, colaboração e trilha de auditoria
- [[wiki/sources/continuous-delivery-martin-fowler]] — bliki de 2013 que define "Continuous Delivery": quatro indicadores, distinção vs. Continuous Deployment, DevOps culture, crédito a Jez Humble
