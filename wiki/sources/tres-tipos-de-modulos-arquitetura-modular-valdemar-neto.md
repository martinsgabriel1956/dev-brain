---
type: source
title: "Três Tipos de Módulos numa Arquitetura de Monolito Modular"
aliases: ["três tipos de módulos", "módulos de domínio vs infraestrutura vs feature", "core supporting infrastructure pure infrastructure"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-09-01
source_count: 0
tags: [monolito-modular, arquitetura-modular, clean-architecture, hexagonal-architecture, ddd, tipos-de-modulos, nestjs, backend]
skill: tech-mentor-backend
status: stable
---

# Três Tipos de Módulos numa Arquitetura de Monolito Modular

## TL;DR

Segundo vídeo de [[wiki/entities/valdemar-neto|Valdemar Neto]] na wiki (após [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]]), usando o mesmo exemplo de código (sistema de streaming "Fake Flix" em NestJS, curso "Aplicações Enterprise" da [[wiki/entities/tech-leads-club|Tech Leads Club]]). A fonte faz duas contribuições novas: (1) posiciona a arquitetura modular como **um nível acima** de [[wiki/concepts/clean-architecture|Clean Architecture]] e [[wiki/concepts/hexagonal-architecture|Hexagonal Architecture]] — ambas já separam domínio do mundo externo, mas nenhuma trata explicitamente de *reuso de infraestrutura entre contextos* nem de *rodar partes do código em processos diferentes* (nem mesmo o Shared Kernel do [[wiki/concepts/ddd|DDD]] cobre isso); microsserviços não resolveram essa lacuna, porque cada serviço continua sendo um codebase singular internamente — só a arquitetura modular parte o mesmo codebase em módulos. (2) Define uma camada intermediária de três: **Core** (lógica de negócio — services, entidades, use cases), **Supporting Infrastructure** (controllers, resolvers GraphQL, API clients, repositórios — tem conhecimento específico do contexto de domínio, por isso não é totalmente reusável) e **Infraestrutura Pura** (lib de banco, logger, monitoring, config — genérica, movível entre módulos sem alteração). A partir dessa base, nomeia e avalia **três tipos de módulos**: módulos de domínio (mais importantes — Billing, Content, Identity), módulos de infraestrutura pura (compartilháveis entre módulos de domínio — HTTP, logger, persistence), e módulos de feature (o autor evita — granularidade sem bounded context claro, exemplificado com o repositório de terceiros "Ultimate NestJS").

## Claims Principais

| Claim | Confiança |
|---|---|
| Clean Architecture e Hexagonal Architecture compartilham o mesmo princípio central — domínio/lógica de negócio isolado no meio, recebendo entrada de controllers/repositórios de fora — mas nenhuma das duas trata explicitamente de reuso de infraestrutura entre contextos, nem de separar partes do sistema para rodar em processos diferentes | Alta — consistente com o que já está documentado em [[wiki/concepts/clean-architecture]] e [[wiki/concepts/hexagonal-architecture]] (ambas focadas em isolamento de domínio via inversão de dependência, não em topologia de deploy); é a primeira fonte na wiki a nomear essa lacuna explicitamente |
| Nem o Shared Kernel do DDD cobre essa lacuna — DDD não fala muito sobre reuso de infraestrutura nem sobre rodar módulos em processos separados | Média-Alta — claim específico do autor, não verificado contra [[wiki/concepts/ddd]] em detalhe nesta ingestão (página de DDD não documenta Shared Kernel com profundidade suficiente para confirmar ou refutar) |
| A transição de monolitos tradicionais para microsserviços não mudou a forma como Clean/Hexagonal são aplicadas internamente — ambos continuam sendo "codebase singular": o monolito é um codebase singular grande, o microsserviço é um codebase singular menor. A arquitetura modular é o próximo nível: o mesmo codebase passa a ser dividido por módulos | Alta — reforça e generaliza a tese central de [[wiki/concepts/arquitetura-modular]] (microsserviços não compõem porque vivem em codebases diferentes) com um ângulo novo: a distinção monolito/microsserviço nunca foi sobre *como o código é organizado internamente*, e sim sobre *quantos processos/deploys* existem |
| Estrutura de três camadas do autor: **Core** (services, entidades, use cases — lógica de negócio) → **Supporting Infrastructure**/Adapters/Gateways (controllers, GraphQL resolvers, clients de API externa, repositórios — tem conhecimento específico do contexto de domínio, por isso não é totalmente compartilhável) → **Infraestrutura Pura** (lib de banco, logger, monitoring, config — genérica, movível entre módulos sem alteração) | Alta — mapeamento direto e explícito do autor sobre onde cada peça do vocabulário Clean/Hexagonal ([[wiki/concepts/clean-architecture]] Use Cases/Entities, [[wiki/concepts/hexagonal-architecture]] Ports/Adapters) se encaixa dentro de um módulo de domínio; distinção nova entre dois níveis de "infraestrutura" (contextual vs. pura) não nomeada antes na wiki |
| **Módulos de domínio** são o tipo mais importante e comum: abrangentes como um microsserviço ou maiores (Billing, Content, Identity no exemplo). Podem rodar juntos (monolito) ou separados (processos/contêineres distintos), sem mudar o código do módulo | Alta — mesmo exemplo (Billing/Content/Identity) já documentado em [[wiki/concepts/arquitetura-modular]] via a fonte anterior; reforça sem contradizer |
| **Módulos de infraestrutura pura** (HTTP, logger, persistence) são o segundo tipo mais importante: totalmente genéricos, plugáveis em qualquer módulo de domínio sem modificação (ex.: o mesmo `TypeORM persistence module` ou `DynamoDB persistence module` usado dentro de `content` e de outros módulos de domínio). São o que viabiliza reuso e escala sem forçar os módulos de domínio a reimplementar infraestrutura | Alta — mecanismo concreto de código (NestJS), consistente com a "infraestrutura pura" definida na estrutura de três camadas acima; primeira vez que a wiki nomeia esse tipo de módulo especificamente (distinto do módulo de domínio) |
| **Módulos de feature** (granularidade abaixo de módulo de domínio — quebrar um domínio em funcionalidades, ex.: `category`, `auth`, `chat`, `health` no repositório de terceiros "Ultimate NestJS") são desaconselhados pelo autor: (1) perdem o bounded context — não fica claro de que domínio uma feature isolada faz parte; (2) compartilhar entidades entre módulos de feature tende a gerar acoplamento e abstração desnecessária | Alta — opinião explícita e justificada do autor, primeira vez que a wiki documenta uma crítica direta a esse padrão de granularidade; ressalva do próprio autor: quebrar um módulo de domínio muito grande em 2-3 submódulos é um caso legítimo, diferente de modularizar por feature desde o início |
| Exemplo de módulo de infraestrutura pura sendo consumido por um módulo de domínio: dentro de `content`, a camada de `persistence` importa o módulo `TypeORM persistence` (ou `DynamoDB persistence`) — o módulo de infraestrutura pura não sabe nada sobre `content`, só expõe uma API genérica de persistência | Alta — exemplo concreto de código citado no vídeo, consistente com a definição de infraestrutura pura acima |

## Entidades

- [[wiki/entities/valdemar-neto]] — mesmo autor da fonte anterior sobre arquitetura modular
- [[wiki/entities/tech-leads-club]] — curso "Aplicações Enterprise" citado novamente como origem do exemplo de código; app de exemplo nomeado nesta fonte como "Fake Flix" (não nomeado explicitamente na fonte anterior)

## Conceitos

- [[wiki/concepts/tipos-de-modulos]] (novo) — módulos de domínio, de infraestrutura pura e de feature; camadas Core/Supporting Infrastructure/Infraestrutura Pura
- [[wiki/concepts/arquitetura-modular]]
- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/clean-architecture]]
- [[wiki/concepts/hexagonal-architecture]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/composicao-de-modulos]]
- [[wiki/concepts/monorepo-backend]]
- [[wiki/concepts/microsservicos]]

## Open Questions

- **"Ultimate NestJS"** é citado como repositório público de terceiros, explicitamente não afiliado ao autor e não sendo "código de produção" — usado só como exemplo negativo de módulos de feature; nenhuma página de entidade criada para ele nesta ingestão (não é central o suficiente, e o autor não é o mantenedor).
- **"Fake Flix"** é o nome do app de exemplo do curso "Aplicações Enterprise" — não nomeado na fonte anterior ([[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]]), mas evidentemente o mesmo codebase (mesmos módulos Billing/Content/Identity). Registrado como alias/nota em [[wiki/entities/tech-leads-club]], sem página própria.
- O claim de que "DDD não fala muito sobre Shared Kernel cobrindo reuso de infraestrutura" não foi verificado contra uma fonte primária de DDD (Evans/Vernon) nesta ingestão — [[wiki/concepts/ddd]] na wiki não documenta Shared Kernel com profundidade suficiente para confirmar ou contestar; registrado como afirmação do autor, não como fato triangulado.

## Contradições com a Wiki Existente

Nenhuma contradição — a fonte é altamente complementar às duas fontes já ingeridas sobre o mesmo autor/exemplo de código ([[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] e, por extensão de tema, [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]]). Contribuição nova e não sobreposta: (1) o posicionamento explícito da arquitetura modular como "um nível acima" de Clean/Hexagonal Architecture, nomeando a lacuna específica (reuso de infraestrutura entre contextos, execução em processos separados) que nem DDD nem microsserviços resolveram; (2) a camada intermediária "Supporting Infrastructure" (infraestrutura contextual, não genérica) entre Core e Infraestrutura Pura — distinção de granularidade dentro de "infraestrutura" que não existia antes na wiki; (3) a taxonomia nomeada de três tipos de módulo (domínio, infraestrutura pura, feature), com uma crítica explícita e justificada a módulos de feature que não existia antes.

## Citações Brutas Preservadas

> "Por que que arquiteturas modulares puxam esses limites um pouco mais? Porque, por mais que o Domain-Driven Design fale de Shared Kernel e tal, não se fala muito sobre reuso de infraestrutura, e não se fala muito sobre como separar as coisas para rodar elas separadas."

> "A gente foi de monolitos tradicionais para arquiteturas como microsserviço, onde para esse tipo de arquitetura em si nada mudou: elas ainda ficavam num codebase singular basicamente [...] Com arquiteturas modulares a gente passa um nível adiante: a gente tem o mesmo codebase separado por módulos."

> "Qual o problema de módulos puramente de feature? Tu não sabe o contexto deles [...] Compartilhar coisa entre módulos de feature acaba sendo complexo e acaba acoplando eles demais [...] acaba ficando uma abstração desnecessária na maioria dos casos."

> "Na dúvida... " *(nota: heurística de módulos grandes já citada na fonte anterior; nesta fonte o autor reafirma o caso legítimo de quebrar um módulo de domínio muito grande em dois ou três submódulos, sem repetir a heurística completa.)*

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/tipos-de-modulos]]
- [[wiki/concepts/arquitetura-modular]]
- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/clean-architecture]]
- [[wiki/concepts/hexagonal-architecture]]
- [[wiki/concepts/composicao-de-modulos]]
- [[wiki/concepts/monorepo-backend]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/ddd]]
- [[wiki/entities/valdemar-neto]]
- [[wiki/entities/tech-leads-club]]
