---
type: source
title: "Mappers — Conversão de Entidades Entre Camadas"
aliases: ["mapper pattern", "PrismaNotificationMapper", "toPrisma", "data mapper por camada"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/mappers-conversao-entre-camadas.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-10
source_count: 0
tags: [mapper, clean-architecture, hexagonal, prisma, ddd, value-object, repository, camadas]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Em arquiteturas por camadas (Clean Architecture, Ports & Adapters), a mesma entidade de domínio (ex: `Notification`) precisa ser representada em formatos diferentes em cada camada: classe de domínio na camada de aplicação, formato de tabela na camada de persistência (Prisma), formato de resposta na camada HTTP. Um **mapper** é uma classe dedicada, atrelada a uma camada/tecnologia específica, com método estático (ex: `PrismaNotificationMapper.toPrisma()`) que converte a entidade de domínio para o formato daquela camada — evitando repetir a lógica de conversão em cada método do repositório e isolando o acoplamento à tecnologia (ex: Prisma) em um único lugar.

## Key Claims

**Claim:** a mesma entidade de domínio é representada de formas distintas em cada camada de uma arquitetura em camadas, e essas representações divergentes exigem conversão explícita entre si.
**Evidence:** exemplo da entidade `Notification` — classe de domínio nas `entities`; formato de tabela na camada de persistência via Prisma; e um formato de resposta HTTP que idealmente expõe só os campos relevantes (`id`, `content.value` do Value Object, `category`, `recipientId`), moldado deliberadamente diferente do objeto de domínio original. O retorno formatado deixa de ser instância da classe `Notification` original — é conceitualmente uma nova representação, ainda que a mesma entidade de negócio.
**Confidence:** alta

**Claim:** o mapper deve ser implementado como método estático porque não há necessidade de estado ou de instanciar a classe para converter dados.
**Evidence:** `PrismaNotificationMapper.toPrisma(notification)` é chamado diretamente na classe, sem `new PrismaNotificationMapper()`. O método recebe a entidade de domínio e retorna um objeto plano no formato exigido pelo Prisma.
**Confidence:** alta

**Claim:** o mapper fica acoplado à tecnologia/camada que representa — trocar de ORM (ou de camada de saída) provavelmente exige reescrever o mapper, não o resto do domínio.
**Evidence:** o autor nomeia explicitamente a classe como `PrismaNotificationMapper` (não `NotificationMapper` genérico), justificando que se o Prisma for trocado por outro ORM, o formato de dados esperado muda e o mapper precisa mudar junto — mas o domínio (a entidade `Notification`) permanece intocado.
**Confidence:** alta

**Claim:** o objeto convertido no repositório costuma ser nomeado `raw` (não pode reusar o nome `notification`, já ocupado pelo parâmetro de entrada) por ser um nome curto que não prejudica a leitura, mesmo sem descrever tecnicamente o formato de destino.
**Evidence:** alternativa citada e descartada por brevidade: `persistenceNotification`. Convenção de nomenclatura pessoal do autor, não uma regra universal do padrão.
**Confidence:** média (escolha estilística do autor, não consenso da indústria)

## Entities & Concepts Touched

- [[wiki/concepts/hexagonal-architecture]]
- [[wiki/concepts/repository-pattern]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/adapter-pattern]]
- [[wiki/sources/presenters]]

## Open Questions

- O vídeo não cobre o caminho inverso (`toDomain`/`fromPrisma`) — como o repositório reconstrói a entidade de domínio (com Value Objects) a partir da linha crua vinda do Prisma. Provável tópico de um mapper simétrico (`toDomain`) não mostrado nesta transcrição.
- Não fica claro se o autor recomenda um mapper por camada de saída (HTTP, persistência) sempre, ou só quando a divergência de formato justifica — a fonte trata do caso de persistência em detalhe e menciona o caso HTTP apenas como motivação, sem mostrar a implementação de um `HttpNotificationMapper` equivalente.
