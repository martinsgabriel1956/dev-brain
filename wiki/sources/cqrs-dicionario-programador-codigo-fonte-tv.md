---
type: source
title: "CQRS — Dicionário do Programador (Código Fonte TV)"
aliases: ["CQRS Dicionário do Programador"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-dicionario-programador-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: 2026-08-17
source_count: 0
tags: [cqrs, arquitetura, ddd, event-sourcing, bounded-context, task-based-ui, command-bus, dicionario-do-programador]
skill: tech-mentor-system-design
status: stable
---

# CQRS — Dicionário do Programador (Código Fonte TV)

## TL;DR

Episódio da série "Dicionário do Programador" do [[wiki/entities/codigo-fonte-tv]] explicando CQRS (Command Query Responsibility Segregation) do zero: por que separar leitura e escrita, o vocabulário de Command/Query, um diagrama de fluxo write→sync→read, as estratégias de sincronização, e os quatro aspectos de implementação segundo Greg Young/Martin Fowler (UI baseada em tarefas, Command sem retorno de valor, consistência de sincronização, domain events). Fecha com uma menção a Event Sourcing citando José Carlos Macoratti.

## Claims Principais

| Claim | Confiança |
|---|---|
| CQRS é um padrão (pattern), não uma arquitetura — não deve ser aplicado ao sistema inteiro, só a bounded contexts específicos onde leitura e escrita têm cargas/requisitos genuinamente diferentes | Alta |
| A necessidade de CQRS cresce com a concorrência: single-user (sem necessidade) → LAN multi-atendente (concorrência moderada) → SaaS multi-tenant com 100k+ usuários (CQRS passa a fazer sentido) | Alta |
| Query nunca altera dados; Command nunca deveria retornar dados (nem um ID) — retornar dados de um Command quebra a separação entre os modelos | Média — o vídeo relativiza: "se você precisa disso, talvez não devesse usar CQRS para essa parte" |
| CQRS deve ser orientado a uma UI baseada em tarefas (task-based UI), não a uma UI que é só uma camada fina de CRUD sobre o banco | Alta |
| Consistência eventual (ex.: contador de views do YouTube, atualizado em lote e não em tempo real) evita dores de cabeça quando a aplicação não exige resposta imediata | Alta |
| Mensageria não é obrigatória para sincronizar write model e read model, mas ajuda | Média |
| Event Sourcing é comumente usado junto de CQRS, mas é um padrão distinto: captura toda alteração de estado como um evento imutável, armazenado em sequência | Alta |

## Entidades

- [[wiki/entities/codigo-fonte-tv]] — canal, segmento "Dicionário do Programador"

## Conceitos

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/ddd]] (bounded context)
- [[wiki/concepts/task-based-ui]] (novo)
- [[wiki/concepts/command-bus]] (novo)

## Open Questions

- O vídeo cita "macoratti" (José Carlos Macoratti, autor/blogueiro brasileiro de referência técnica) para a definição de Event Sourcing, mas sem URL ou publicação específica — não foi criada entidade dedicada por ser citação pontual, não foco do episódio.
- Não menciona explicitamente as quatro categorias formais de Greg Young (task-based UI, command validation, benefits of a task-based UI, eventual consistency) por nome — a estrutura de "quatro aspectos" do vídeo mapeia de perto para esse framework difundido por Martin Fowler/Greg Young, mas a fonte não cita essa origem diretamente. Registrado aqui como inferência do ingest, não como claim do vídeo.

## Contradições com a Wiki Existente

Nenhuma. Esta fonte é consistente com [[wiki/concepts/cqrs]] (já cobre a separação command/query, event sourcing, e a versão "duplicar o banco em write/read" de [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]]) e com [[wiki/sources/cqrs]] (fonte técnica mais densa, já cobre bounded context e a regra "Commands retornam void ou ID"). Esta fonte contribui principalmente com: (1) a progressão de cenários de motivação (single-user → LAN → SaaS multi-tenant) como narrativa didática de "quando CQRS passa a fazer sentido"; (2) o conceito de **task-based UI**, ausente nas outras fontes de CQRS já ingeridas; (3) o termo **command bus**, também ausente.

## Citações Brutas Preservadas

> "CQRS não está focado em ser um CRUD: ele permite escrever uma UI baseada em tarefas que atravessa a aplicação para oferecer uma interface rica e baseada em intenção."

> "Um Command nunca deve retornar dados, porque isso quebraria a separação entre os modelos de leitura e gravação."

> "CQRS não é uma arquitetura para o sistema todo — é um padrão para bounded contexts específicos onde leitura e escrita têm requisitos genuinamente diferentes." (paráfrase do encerramento do vídeo)

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/task-based-ui]]
- [[wiki/concepts/command-bus]]
- [[wiki/entities/codigo-fonte-tv]]
