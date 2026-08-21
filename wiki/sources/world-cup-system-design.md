---
type: source
title: "World Cup System Design (slide deck / Miro board)"
aliases: ["world cup system design pdf", "placar copa do mundo slides", "match-events topic diagram"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 0
tags: [system-design, kafka, event-sourcing, redis, redis-pub-sub, server-sent-events, escalabilidade-horizontal, load-balancer, read-replicas, multi-tenancy, api-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/world-cup-system-design.pdf
source_url:
author: não identificado (mesma aula que [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — ver Open Questions)
date_published:
date_ingested: 2026-08-19
---

# World Cup System Design (slide deck / Miro board)

## TL;DR

PDF exportado de um board Miro (27 páginas/slides) que é o material visual de apoio da **mesma aula** já ingerida como transcrição em [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — mesmo domínio (placar de Copa do Mundo em tempo real), mesmos requisitos (10M usuários simultâneos, alta disponibilidade 24/7, consistência forte, sem perda de dados), mesma evolução arquitetural (Ingestion API → Kafka particionado → Consumer Groups → Redis + Postgres → Redis Pub/Sub → SSE). O valor incremental desta fonte não está na narrativa (já coberta), mas em **artefatos concretos que a transcrição não capturava**: contratos de API explícitos, taxonomia fechada de eventos de partida, schemas JSON completos (payload bruto do provedor vs. evento normalizado pela Ingestion API), SQL de persistência, e um requisito de escala adicional não mencionado na transcrição — a decisão do produto de atender **todos os campeonatos do mundo**, não só a Copa, como o gatilho final que força a arquitetura a suportar múltiplas partidas simultâneas em qualquer lugar do planeta.

## Key Claims

| Claim | Evidência |
|---|---|
| A API expõe contrato REST explícito por partida: `GET /matches/{match_id}` como endpoint principal de consulta de estado de uma partida | Slide "Etapa 2 - Defina os Endpoints da API", isolado como etapa própria do exercício de design, algo que a transcrição não formaliza como contrato |
| A taxonomia de eventos de uma partida é fechada e enumerada: `MATCH_STARTED`, `GOAL`, `YELLOW_CARD`, `RED_CARD`, `VAR_REVIEW_STARTED`, `VAR_DECISION`, `CORNER_KICK`, `PENALTY`, `FOUL`, `SUBSTITUTION`, `MATCH_ENDED` | Lista explícita renderizada num card do diagrama de eventos do Data Provider, ausente da transcrição (que só cita gol/cartão/substituição como exemplos soltos) |
| O evento bruto do provedor de dados (FIFA/Football API) tem um schema mínimo (`id`, `match`, `team_A`, `team_B`, `competition.title`, `competition.stage`, `event`, `minute`, `sequence`, `payload`); a Ingestion API o **normaliza** para um schema próprio mais rico antes de publicar no Kafka (`event_id`, `external_event_id`, `match` completo com `participants`, `minute`, `type`, `sequence`, `payload`, `received_at`, `source`) | Dois JSONs lado a lado no diagrama: o card do Data Provider (schema do provedor) e o card abaixo da Ingestion API (schema já normalizado, com `received_at` e `source: "sports-data-provider-x"` adicionados) |
| A persistência final em Postgres usa duas tabelas: `matches` (id, title, competition_title, competition_stage, participants como JSONB) e `match_events` (event_id, external_event_id, match_id, minute, type, payload como JSONB, received_at, source) | Snippets SQL `INSERT INTO matches (...)` e `INSERT INTO match_events (...)` explícitos no diagrama, gerados pelo Event Service consumer |
| O gatilho final e mais forte de escala nesta fonte não é o volume de eventos por segundo (já coberto na transcrição), mas a decisão de negócio de **atender todos os campeonatos do mundo simultaneamente** — não só a Copa | Slide "Problema 5: A empresa agora decidiu atender todos os campeonatos ao redor do mundo", acompanhado de um mosaico de 14 logos de competições reais (Champions League, Premier League, Bundesliga, Brasileirão, Libertadores, Club World Cup, Liga Portugal, Saudi Pro League, Euro, Copa América, La Liga, Copa do Brasil, Serie A, Ligue 1) — ausente da transcrição, que trata o sistema como escopo fixo de uma única competição |
| O cache de placar pré-computado (Redis, usado pelo Score Service) e o barramento de notificação em tempo real (Redis Pub/Sub, usado pelo Web Server) são desenhados como **duas instâncias/papéis Redis distintos**, não uma única instância acumulando os dois usos | Diagrama final mostra dois blocos separados rotulados "Redis" e "Redis Pub/Sub", cada um com seta própria para o Web Server, e o "Redis" (cache) evolui para cluster de múltiplos nós na última iteração do diagrama, enquanto o "Redis Pub/Sub" permanece single-node |
| O Web Server final expõe 5 endpoints distintos, não só o placar ao vivo: `GET /matches/{match_id}`, `GET /matches/{match_id}/stream` (SSE), `GET /matches/{match_id}/statistic`, `GET /team/{team_id}/history`, `GET /player/{player_id}/history` | Rótulos explícitos nas setas entre Web Server e User Application nos últimos slides do diagrama — a transcrição só menciona o fluxo de placar ao vivo via SSE, sem detalhar o restante da superfície de API |
| A camada de persistência final ganha réplicas de leitura explícitas (`Replica 1`, `Replica 2`) ao lado do banco primário, alimentando o Web Server para as consultas de estatística/histórico (não o placar ao vivo, que vem do Redis) | Diagrama final mostra `Database` com duas réplicas anexadas e uma seta separada do Web Server direto às réplicas, distinta da escrita feita pelo Event Service no primário |
| A evolução do diagrama segue exatamente os "5 problemas" já descritos na transcrição (recalcular a timeline a cada request, cliente precisa dar refresh manual, sem alta disponibilidade, volume de usuários derruba servidor/banco), mas os apresenta como uma lista visual explícita numerada de 1 a 5 antes de cada correção arquitetural subsequente | Slide único listando os 5 problemas lado a lado com o estado então-atual do diagrama, servindo de "checkpoint" antes de cada camada de solução (load balancer, partições Kafka, consumer groups, Score Service, Redis Pub/Sub, réplicas) |

## Entidades

- [[wiki/entities/renato-augusto]] — mesma inferência de autoria da fonte-irmã (não confirmada; ver Open Questions), reforçada agora por um segundo artefato (slides) do mesmo curso/aula

## Conceitos

- [[wiki/concepts/kafka]] — nova contribuição concreta: schema JSON completo do evento normalizado publicado no tópico `match-events`, taxonomia fechada de 11 tipos de evento
- [[wiki/concepts/event-sourcing]] — reforça (sem contradizer) o exemplo já documentado do placar de futebol, agora com o schema de persistência exato (`match_events` como o event log relacional)
- [[wiki/concepts/redis]] — nova distinção: Redis de cache de estado e Redis Pub/Sub desenhados como instâncias separadas, uma delas clusterizada e outra não
- [[wiki/concepts/server-sent-events]] — nova contribuição: superfície completa de endpoints do Web Server além do stream (`/statistic`, `/team/{id}/history`, `/player/{id}/history`)
- [[wiki/concepts/escalabilidade-horizontal]] — novo gatilho de escala: decisão de negócio de atender todos os campeonatos do mundo, não só volumetria de eventos por partida
- [[wiki/concepts/load-balancer]] — reforça (sem novidade) o LB na frente da Ingestion API já documentado na fonte-irmã
- [[wiki/concepts/read-replicas]] — nova contribuição: réplicas de leitura explícitas no diagrama final, servindo consultas de estatística/histórico separadas da escrita do Event Service
- [[wiki/concepts/multi-tenancy]] — conexão fraca/inferida: "atender todos os campeonatos do mundo" é mais um problema de volume e particionamento de dados (mais partidas, mais partições Kafka, mais linhas em `matches`) do que isolamento de tenant no sentido de SaaS B2B que esta página documenta; registrado aqui como observação, não como caso de uso central da página

## Open Questions

- **Mesma lacuna de autoria da fonte-irmã.** O PDF não traz identificação textual do autor/canal nos slides lidos. Atribuição a [[wiki/entities/renato-augusto]] herda a mesma confiança (alta, não confirmada) já registrada em [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]].
- **Redundância declarada.** Grande parte da narrativa e das claims de fundamentos de Kafka (partições, consumer groups, hash de partição) já está integralmente coberta pela fonte-irmã e por [[wiki/concepts/kafka]] — esta fonte foi mantida como página própria por trazer artefatos concretos (schemas, SQL, contrato de API, taxonomia de eventos) que a transcrição não capturava, não por conteúdo narrativo novo.
- **"Atender todos os campeonatos do mundo" não é aprofundado tecnicamente.** O slide levanta o requisito e mostra os logos das competições, mas o board não detalha se isso implica sharding por competição, um tópico Kafka por campeonato, ou apenas mais volume no mesmo tópico particionado por `match_id` — lacuna a preencher se uma fonte futura sobre esse mesmo case aprofundar a resposta dada em aula.
- **Papel exato do "Redis" (cache) vs. "Redis Pub/Sub" como duas instâncias não é justificado explicitamente no board** — é uma inferência visual (dois blocos, duas setas) de que são deployments separados, não uma afirmação textual explícita nos slides lidos. Pode ser simplificação didática do diagrama, não necessariamente a recomendação real de produção.

## Key Sources

_Este é o documento primário. Ver também [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] como fonte-irmã (transcrição em áudio da mesma aula)._
