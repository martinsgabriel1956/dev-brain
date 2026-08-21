---
type: concept
title: "Redis"
aliases: ["redis cache", "redis db"]
date_created: 2026-06-26
date_updated: 2026-08-19
source_count: 11
tags: [redis, cache, nosql, banco-in-memory, chave-valor, backend, grande-rollback]
skill: tech-mentor-backend
status: stable
---

# Redis

## TL;DR

Banco [[nosql]] [[banco-in-memory]] do tipo chave-valor. Projetado para latência mínima — armazena tudo na RAM e acessa por chave, sem esquema, sem SQL. Caso de uso principal: [[cache]].

## Modelo de Dados

```
chave                  →  valor
"saldo-cliente-123"    →  "1500.00"
"sessao-abc"           →  { userId: 42, role: "admin" }  (hash)
"fila-emails"          →  ["msg1", "msg2"]               (list)
```

**Tipos de valor suportados:** `string`, `hash`, `list`, `set`, `sorted set`, `stream`, `HyperLogLog`, `bitmap`

A chave pode ser longa e semântica. Busca por prefixo (`GET cod_cliente:*`) permite recuperar ou limpar grupos de registros.

## Pontos Fortes

| Aspecto | Detalhe |
|---|---|
| Performance | Latência sub-milissegundo; o mais rápido para leitura/escrita |
| Difusão | Amplamente conhecido; suporte em todas as linguagens |
| Cloud | Serviço gerenciado nativo em AWS (ElastiCache), GCP, Azure |
| Deploy | Container, local, cloud managed, servidor físico |
| Cluster | [[escalabilidade-horizontal]] simples — bem documentada |

## Pontos Fracos

| Aspecto | Detalhe |
|---|---|
| Memória limitada | Limitado pela RAM disponível na máquina/cluster |
| Single CPU | Uma instância usa apenas 1 núcleo — clusterize para escalar CPU |
| Sem SQL | Sem suporte a queries relacionais |
| Segurança | Permissões estáticas por DB (Redis < 6); Redis 6+ introduziu ACLs granulares |
| Persistência | In-memory por padrão; RDB/AOF são opcionais e adicionam overhead |

## Padrões de Uso

- **[[cache-aside]]** — busca no Redis; em miss vai ao banco e popula com TTL
- **[[cqrs]] read layer** — Redis como projeção otimizada de leitura; SQL como fonte de verdade
- **[[feature-flag]]** — interruptores de código com latência mínima
- **Session store** — tokens de sessão, permissões de menu, extrato do cliente
- **Reserva temporizada (TTL como regra de negócio)** — guardar uma chave com expiração automática para implementar diretamente uma regra do tipo "reserva por N minutos", sem job/cron externo para liberar o recurso. Ver [[wiki/sources/system-design-entrevista-cinema-draw-io]] abaixo — mas note a ressalva de consistência descrita ali.
- **Pub/Sub** — broadcast efêmero em tempo real (sem persistência); `PUBLISH`/`SUBSCRIBE` num canal não exige criação prévia — publicar cria o canal implicitamente. Usado como notificador entre microsserviços em [[wiki/concepts/server-sent-events]]
- **Cache de estado pré-computado alimentado por consumer de fila** — um consumer [[wiki/concepts/kafka|Kafka]] dedicado pode filtrar só os eventos relevantes de um stream (ex.: gol, cartão, substituição, ignorando o resto) e manter um payload já montado no Redis (placar, minuto, últimos eventos), evitando que o caminho de leitura precise recalcular uma projeção inteira a partir do banco relacional a cada requisição. Ver [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]]
- **Streams** — fila robusta com consumer groups e ACK

## Conexão como Singleton

Abrir uma nova conexão Redis por requisição HTTP não escala — 100 usuários simultâneos numa arquitetura SSE/Pub/Sub geram 100 conexões abertas, o que pode derrubar a instância. O Redis é projetado para multiplexar uma única conexão entre muitos assinantes; a prática correta é usar [[wiki/concepts/singleton-pattern]] para reutilizar uma conexão compartilhada. Ver [[wiki/concepts/connection-pooling]] para o mesmo princípio aplicado a bancos relacionais.

## Quando NÃO Usar Redis

- Dados financeiros críticos onde consistência > performance
- Dados com alta volatilidade (mudam a cada request)
- Datasets que cabem em memória de processo (L1 cache resolve sem Redis)

## Caso Real: Substituindo Redis por SQL Puro (Grande Rollback)

A [[wiki/entities/shopify]] tinha reserva de estoque em Redis com fonte de verdade em [[wiki/concepts/mysql]] — duas escritas não-atômicas sincronizadas (reservar no Redis, depois confirmar/limpar no MySQL). Esse desenho gerava um problema clássico: dependendo da ordem das duas operações, o item vendia sem dar baixa no estoque real, ou ficava bloqueado como "fantasma" no banco. A solução não foi otimizar a sincronização — foi eliminar a necessidade dela, movendo a reserva inteira para dentro do MySQL com [[wiki/concepts/skip-locked]], numa única transação atômica. Ver [[wiki/concepts/grande-rollback]] e [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]].

## Escalabilidade

- **Sentinel** — HA sem sharding; failover automático; dataset cabe em um nó
- **Cluster** — sharding horizontal com 16.384 hash slots; dataset maior que memória de um nó

## Redis Quase Nunca é o Banco Principal

Reforço direto do caso Shopify acima: em quase 100% dos casos reais, Redis não é a fonte de verdade — ele vive como camada de velocidade em cima de um banco relacional (MySQL, PostgreSQL, Oracle), que continua sendo quem detém o dado real. Quando o cache expira, a aplicação busca no banco relacional e recarrega no Redis — uma arquitetura de duas camadas de leitura. Performance de referência: >100 mil operações/segundo em hardware comum, até ~1 milhão OPS/s com pipeline e batching, latência sub-milissegundo por tudo estar em RAM. Persistência (RDB/AOF) é opcional por design — se o servidor cair sem AOF configurado, os dados são perdidos desde o último snapshot.

## Cache de Estado vs. Barramento Pub/Sub: Instâncias Separadas

[[wiki/sources/world-cup-system-design]] desenha o Redis usado como cache de placar pré-computado (alimentado pelo Score Service) e o Redis usado como barramento [[wiki/concepts/pub-sub|Pub/Sub]] (que notifica o Web Server para repassar via SSE) como **dois blocos separados no diagrama de arquitetura**, não uma única instância acumulando as duas funções — e só o Redis de cache evolui para cluster multi-nó na versão final da arquitetura; o Redis Pub/Sub permanece single-node. O board não justifica essa separação explicitamente (ver open question na fonte), mas é consistente com o princípio de que cache (dado que precisa sobreviver e ser consultável) e pub/sub (broadcast efêmero, sem persistência) têm perfis de uso e de disponibilidade diferentes.

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — Redis Pub/Sub como notificador entre microsserviços, armadilha da conexão sem Singleton
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — Redis Pub/Sub como broker entre servidores WebSocket replicados, tópico por usuário/grupo
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — caso onde Redis + MySQL sincronizados foi substituído por MySQL puro com SKIP LOCKED
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — Redis como camada de velocidade sobre banco relacional, nunca fonte de verdade; números de OPS/s e riscos de persistência
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — Redis como cache para hotspots num encurtador de URL (URLs virais), tirando a carga dessas queries do banco principal
- [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]] — citado como exemplo de SGBD NoSQL chave-valor e classificado didaticamente como CP no Teorema CAP em material de concurso
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — reserva de assento de cinema por 15 minutos guardando `seatmapId`+`seatId` com TTL; a chave expira sozinha e libera o assento, mas o desenho não consulta o Redis antes de responder disponibilidade a partir da API externa de seatmap, gerando um bug de consistência assumido pelo próprio autor (ver [[wiki/concepts/distributed-lock]])
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — Redis via Docker como broker de uma fila BullMQ na demo de admission control com low/high watermark
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — cache de placar pré-computado alimentado por um consumer group Kafka dedicado, evitando recalcular a timeline completa a cada leitura; Redis Pub/Sub propagando atualizações para conexões SSE distribuídas entre instâncias
- [[wiki/sources/world-cup-system-design]] — slide deck da mesma aula: Redis de cache e Redis Pub/Sub desenhados como duas instâncias separadas, só a de cache clusterizada na arquitetura final
