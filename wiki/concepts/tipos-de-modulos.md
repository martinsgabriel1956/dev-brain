---
type: concept
title: "Tipos de Módulos (Domínio, Infraestrutura Pura, Feature)"
aliases: ["tipos de módulos", "domain modules", "pure infrastructure modules", "feature modules", "módulos de domínio vs feature"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [tipos-de-modulos, arquitetura-modular, monolito-modular, bounded-context, backend]
skill: tech-mentor-backend
status: draft
---

# Tipos de Módulos (Domínio, Infraestrutura Pura, Feature)

Taxonomia de [[wiki/entities/valdemar-neto|Valdemar Neto]] para os três tipos de módulo mais comuns dentro de uma arquitetura de [[wiki/concepts/monolito-modular|monolito modular]]/[[wiki/concepts/arquitetura-modular|arquitetura modular]]. Nasce de uma estrutura de três camadas dentro de cada módulo (ver seção abaixo), e serve como critério prático para decidir *o que* virar um módulo — não só *como* estruturar internamente um módulo já decidido.

## As Três Camadas Dentro de um Módulo

Mapeamento do autor de onde cada peça do vocabulário de [[wiki/concepts/clean-architecture]]/[[wiki/concepts/hexagonal-architecture]] se encaixa, com uma distinção nova de granularidade dentro do que normalmente se chama só de "infraestrutura":

1. **Core** — lógica de negócio: services, entidades, use cases. Equivale ao domínio/Use Cases/Entities de Clean Architecture, ou ao domínio protegido em [[wiki/concepts/hexagonal-architecture]].
2. **Supporting Infrastructure** (Adapters/Gateways) — controllers, resolvers GraphQL, clients de API externa, repositórios de banco. Interage com o Core, mas **tem conhecimento específico do contexto de domínio** (ex.: `IdentityController`, `UserController`) — por isso não é totalmente genérica nem compartilhável entre módulos.
3. **Infraestrutura Pura** — lib de banco (ORM), logger, monitoring, config. Totalmente genérica: pode ser movida entre módulos sem alteração nenhuma.

Essa distinção entre infraestrutura *contextual* (camada 2) e infraestrutura *pura* (camada 3) é o que torna possível compartilhar infraestrutura entre módulos de domínio sem acoplá-los entre si — só a infraestrutura pura é candidata a virar um módulo compartilhado.

## Os Três Tipos de Módulo

### 1. Módulos de Domínio (mais importante)

Módulos abrangentes — do tamanho de um microsserviço ou maiores. Exemplo (sistema de streaming "Fake Flix"): `billing` (cobrança), `content` (indexação, streaming, recomendação, distribuição de conteúdo), `identity` (autenticação/autorização, gestão de usuário). Cada um pertence a um domínio de [[wiki/concepts/ddd|DDD]] estratégico (design estratégico, bounded context), não a uma feature isolada. Podem rodar juntos (monolito) ou separados (processos/contêineres distintos), sem alterar o código do módulo — mesma tese de "monolito é escolha de deploy" já documentada em [[wiki/concepts/monolito-modular]].

### 2. Módulos de Infraestrutura Pura (segundo mais importante)

Módulos totalmente genéricos e reusáveis: HTTP, logger, persistência (ex.: `TypeORM persistence module`, `DynamoDB persistence module`). Um módulo de domínio como `content` simplesmente importa o módulo de persistência pronto — o módulo de infraestrutura pura não sabe nada sobre `content`. É o que viabiliza reuso e escala sem forçar cada módulo de domínio a reimplementar infraestrutura, e o que mantém os módulos de domínio focados só em lógica de domínio (Core + Supporting Infrastructure contextual).

### 3. Módulos de Feature (o autor evita)

Granularidade abaixo de módulo de domínio: quebrar um domínio inteiro em funcionalidades separadas. Exemplo citado como anti-padrão: o repositório público de terceiros "Ultimate NestJS" (não afiliado ao autor, não é código de produção), com módulos como `category`, `auth`, `chat`, `health`.

**Dois problemas apontados:**

- **Perda de bounded context** — não fica claro a que domínio uma feature isolada pertence (`auth` é de quê? `category` é mais específico que quê?).
- **Acoplamento via compartilhamento de entidade** — compartilhar uma entidade entre módulos de feature tende a virar abstração desnecessária, já que os módulos não têm fronteira de domínio clara para justificar a separação.

**Exceção legítima**: quebrar um módulo de domínio muito grande em 2-3 submódulos internos é diferente de modularizar por feature desde o início — nesse caso os submódulos ainda herdam o bounded context do domínio pai.

## Por que essa Taxonomia Existe: a Lacuna que Clean/Hexagonal e DDD Não Cobrem

Segundo o autor, nem [[wiki/concepts/clean-architecture]]/[[wiki/concepts/hexagonal-architecture]] (que isolam domínio do mundo externo, mas não tratam de reuso de infraestrutura entre contextos nem de rodar partes em processos diferentes) nem o Shared Kernel de [[wiki/concepts/ddd]] cobrem essa questão — e a transição para microsserviços também não resolveu, porque cada microsserviço continua sendo um codebase singular internamente (mesma limitação de um monolito, só que menor). A [[wiki/concepts/arquitetura-modular|arquitetura modular]] é apresentada como o próximo nível: o mesmo codebase passa a ser dividido por módulos com tipos e responsabilidades explícitos — daí a necessidade de nomear os três tipos acima.

## Key Sources

- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — origem desta taxonomia; estrutura Core/Supporting Infrastructure/Infraestrutura Pura; exemplo "Fake Flix" (billing/content/identity) e anti-exemplo "Ultimate NestJS" (category/auth/chat/health)
