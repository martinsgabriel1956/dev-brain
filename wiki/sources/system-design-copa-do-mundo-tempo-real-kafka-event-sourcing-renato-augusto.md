---
type: source
title: "System Design: Resultados de Jogos da Copa do Mundo em Tempo Real (Event Sourcing + Kafka)"
aliases: ["copa do mundo tempo real", "sistema de placar ao vivo estilo Google", "match events kafka partitions"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 0
tags: [system-design, event-sourcing, kafka, partitions, consumer-groups, mensageria, redis, redis-pub-sub, server-sent-events, escalabilidade-horizontal, murmur-hash, event-replay]
skill: tech-mentor-system-design
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto.md
source_url:
author: Renato Augusto (inferido — ver Open Questions)
date_published:
date_ingested: 2026-08-19
---

# System Design: Resultados de Jogos da Copa do Mundo em Tempo Real (Event Sourcing + Kafka)

## TL;DR

Aula de system design que arquiteta, do zero, um sistema de placar de futebol em tempo real estilo Google (10M usuários simultâneos, 24x7, consistência forte, sem perda de dados). A arquitetura evolui em camadas: (1) data provider → API de ingestão → tópico Kafka único → um consumer → Postgres → servidor web consultando o banco a cada requisição — versão que **não funciona** em escala, usada apenas para introduzir o conceito filosófico de event sourcing (placar não é armazenado, é *derivado* de uma timeline de eventos ordenados); (2) escalabilidade horizontal da API de ingestão e dos consumers via load balancer e consumer groups; (3) mergulho nos fundamentos do Kafka — por que um tópico não é uma fila convencional, offset commit como mecanismo que impede paralelismo dentro de uma única partição, partições como unidade real de paralelismo, e a chave de partição (`match_id`) roteada por hash murmur + módulo garantindo que todos os eventos da mesma partida caiam sempre na mesma partição/consumer; (4) um segundo consumer group (`score-service`) que filtra só eventos relevantes (gol, cartão, substituição) e mantém um placar pré-calculado no Redis, evitando recalcular a timeline inteira a cada leitura; (5) tempo real via SSE (conexão HTTP que nunca fecha) alimentado por Redis Pub/Sub, com o servidor mantendo um mapa em memória de `match_id → conexões SSE interessadas` para saber a quem repassar cada atualização.

## Key Claims

| Claim | Evidência |
|---|---|
| O placar de uma partida não deve ser armazenado como estado mutável — deve ser *derivado* (projetado) de uma sequência ordenada de eventos imutáveis (event sourcing) | Explicação central do vídeo: "2 a 1" não existe como linha numa tabela; é o resultado de processar `match_started`, `goal`, `goal`, `match_ended` em ordem, usando o campo `sequence` para desempatar eventos no mesmo minuto |
| Recalcular a timeline completa do banco a cada requisição de leitura não escala para 10M de usuários simultâneos — é necessário pré-computar e cachear o estado derivado | Problema nº 1 explicitamente levantado pelo autor: buscar todos os gols, ordenar, interpretar payload, somar por time, considerar VAR, a cada requisição, com 10M de requisições batendo no Postgres |
| Dentro de um Kafka consumer group, uma mensagem só é entregue a um único consumer por vez — o Kafka não paraleliza automaticamente subindo mais consumers | Demonstração passo a passo: dois consumers no mesmo `group_id`, o segundo evento (dentro da mesma partição) só é entregue ao consumer 1 após ele comitar o offset do evento anterior; o consumer 2 fica ocioso mesmo com trabalho disponível |
| O paralelismo real no Kafka vem do número de partições, não do número de consumers — paralelismo máximo = número de partições | Regra explícita: "para eu trabalhar com dois consumidores eu preciso ter duas partições"; consumer extra sem partição correspondente fica ocioso, mesma regra já documentada em [[wiki/sources/kafka]] |
| A chave de partição (`match_id`) passa por hash (algoritmo Murmur) e depois módulo pelo número de partições — a mesma chave sempre cai na mesma partição, garantindo que todos os eventos de uma partida sejam processados em ordem por um único consumer | Explicação do mecanismo interno (`hash(match_id) % num_partitions`) com exemplo de duas partidas simultâneas (Brasil x Marrocos, Alemanha x Curaçao) roteadas para partições diferentes |
| Escalar horizontalmente nem sempre é sobre volumetria — pode ser puramente sobre redundância/alta disponibilidade, mesmo quando um único servidor já suportaria a carga | Afirmação explícita: os data providers produzem "centenas ou milhares" de eventos por segundo, não milhões; um servidor só bastaria, mas a exigência de alta disponibilidade (requisito não-funcional) força a escalabilidade horizontal de qualquer forma |
| Um segundo consumer group dedicado, filtrando só um subconjunto de tipos de evento (gol, cartão, substituição) e escrevendo um payload pré-calculado no Redis, evita que o caminho de leitura em tempo real precise tocar o banco relacional ou recalcular a timeline | Desenho do `score-service`: consumer separado do que grava a timeline completa no Postgres, publicando apenas o "estado atual" (placar, minuto, gols, cartões) já montado no Redis |
| SSE (`text/event-stream` + conexão HTTP nunca finalizada) resolve a atualização em tempo real sem polling, e Redis Pub/Sub é o mecanismo que propaga a atualização do consumer para os servidores web que mantêm as conexões SSE abertas | Fluxo completo: primeira requisição normal busca o cache no Redis; em seguida o front end abre EventSource; o servidor se inscreve (`SUBSCRIBE`) no canal Redis Pub/Sub daquele `match_id`; o `score-service` publica (`PUBLISH`) a cada novo evento relevante |
| Um servidor com múltiplas conexões SSE abertas precisa de um mapa em memória (`match_id → lista de conexões`) para saber para quais clientes repassar cada atualização recebida do Redis Pub/Sub | Explicação direta do autor sobre "como o servidor sabe para quem entregar cada mensagem", com exemplo de mapa `{ matchId: [conexaoA, conexaoB, conexaoC] }" |
| Se qualquer elemento da arquitetura cair (API de ingestão, Kafka, consumer, banco), toda a cadeia de atualização para — não há degradação graciosa nessa primeira versão sem redundância | Requisito não-funcional de alta disponibilidade 24x7 citado como motivador direto de escalar horizontalmente cada componente (API de ingestão, consumers/partições, Redis em cluster, réplicas de banco) |
| Event replay — reprocessar a timeline completa do zero com uma nova regra de negócio — é viável precisamente porque o Kafka retém eventos além do momento em que foram consumidos (diferente de uma fila tradicional que remove a mensagem ao entregá-la) | Exemplo hipotético dado pelo autor: bug de cálculo usando `float` para dinheiro num sistema financeiro, corrigido criando um consumer novo que reprocessa desde o primeiro evento do tópico |

## Entidades

- [[wiki/entities/renato-augusto]] — autoria inferida com confiança alta, não confirmada explicitamente na transcrição (ver Open Questions). O estilo, o vocabulário ("bora lá", "botar a mão na massa") e a menção ao "Mapa do Arquiteto" como produto de mentoria de carreira em arquitetura de software batem exatamente com o padrão já registrado em outras fontes deste autor na wiki (ex.: [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]], [[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]]).

## Conceitos

- [[wiki/concepts/event-sourcing]] — nova contribuição concreta: exemplo de domínio (placar de futebol) explicando o conceito filosófico de estado derivado vs. estado persistido, complementando o exemplo bancário já documentado
- [[wiki/concepts/kafka]] — página nova criada nesta ingestão, consolidando partições, chave de partição via hash murmur + módulo, consumer groups, offset commit e rebalance, que antes só existiam dispersos em [[wiki/sources/kafka]] sem uma página de conceito dedicada
- [[wiki/concepts/mensageria]] — reforça a distinção Kafka (stream, retém eventos) vs. fila tradicional (remove ao entregar), com o exemplo didático de "por que o segundo consumer fica parado"
- [[wiki/concepts/redis]] — novo caso de uso: cache de estado pré-computado (placar já montado) alimentado por um consumer dedicado, evitando recomputação da timeline a cada leitura
- [[wiki/concepts/pub-sub]] — novo exemplo ponta a ponta de Redis Pub/Sub como ponte entre um consumer Kafka e conexões SSE distribuídas entre múltiplas instâncias de servidor web
- [[wiki/concepts/server-sent-events]] — nova contribuição: exemplo completo de mapa em memória `match_id → conexões` para rotear atualizações de Pub/Sub às conexões SSE corretas, complementando o mecanismo de escalonamento via Redis Pub/Sub já documentado
- [[wiki/concepts/escalabilidade-horizontal]] — nova contribuição: exemplo explícito de escalar horizontalmente por redundância/alta disponibilidade, não por volumetria
- [[wiki/concepts/consistent-hashing]] — conexão nova: a chave de partição do Kafka (`hash(match_id) % num_partitions`) é uma instância do mesmo hash-based sharding simples que essa página já descreve como tendo o problema de resharding total ao mudar N

## Open Questions

- **Autoria não confirmada explicitamente.** A transcrição não cita nome, canal ou identidade do apresentador. A atribuição a [[wiki/entities/renato-augusto]] é inferência por similaridade de estilo e pela menção ao "Mapa do Arquiteto" — mesmo produto já citado em fontes anteriores confirmadas desse autor. Se uma fonte futura confirmar ou contradizer essa atribuição, revisar.
- **Rebalanceamento de partições não é aprofundado tecnicamente.** O vídeo afirma que o Kafka "rebalanceia" quando um consumer cai, sem detalhar os protocolos reais (eager vs. cooperative sticky assignor) — a mesma lacuna já registrada como open question em [[wiki/sources/kafka]].
- **Nenhuma menção a schema registry, DLQ ou garantias de entrega (`acks`, idempotência de producer)** apesar do requisito não-funcional explícito de "consistência forte e nenhuma perda de dados" — [[wiki/sources/kafka]] cobre `acks=all` e `enable.idempotence=true` como a configuração mais segura para esse cenário, mas esta fonte não entra nesse nível de detalhe operacional; lacuna a preencher se aparecer uma fonte mais operacional sobre Kafka em produção.
- **Redis Pub/Sub não tem garantia de entrega** (mensagem se perde se o assinante não estiver conectado no momento do `PUBLISH`) — o vídeo não menciona esse risco, apesar de ser exatamente o mecanismo escolhido para propagar atualizações de um sistema com requisito de consistência forte. Já documentado como armadilha em [[wiki/concepts/mensageria]] e [[wiki/concepts/server-sent-events]]; não é uma contradição, é uma lacuna da fonte.

## Key Sources

_Este é o documento primário._
