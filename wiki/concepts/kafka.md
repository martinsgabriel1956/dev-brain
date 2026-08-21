---
type: concept
title: "Apache Kafka"
aliases: ["kafka", "topics e partitions", "consumer groups", "kafka producer", "kafka consumer"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 3
tags: [kafka, topics, partitions, consumer-groups, mensageria, event-sourcing, murmur-hash, offset-commit, rebalance]
skill: tech-mentor-backend
status: draft
---

# Apache Kafka

Log distribuído de eventos — diferente de uma fila tradicional (RabbitMQ, SQS), o Kafka **retém** eventos depois de entregues, em vez de removê-los ao serem consumidos. É essa retenção que viabiliza [[wiki/concepts/event-sourcing|event sourcing]] e event replay sobre um tópico Kafka.

## Tópico não é fila: offsets

Cada evento publicado num tópico é armazenado numa posição sequencial chamada **offset** (0, 1, 2...). O evento permanece lá pelo tempo configurado, mesmo depois de consumido — ao contrário de uma fila convencional, onde o elemento sai assim que é atendido.

## Partições: a unidade real de paralelismo

Um tópico é subdividido em **partições**. Paralelismo máximo = número de partições — não adianta ter mais consumers do que partições; o consumer excedente fica ocioso. Para trabalhar com N consumers em paralelo, o tópico precisa ter N partições.

```bash
kafka-topics.sh --create --topic match-events --partitions 2 --bootstrap-server localhost:9092
```

### Chave de partição e hash Murmur

Cada mensagem publicada carrega uma **partition key**. O Kafka aplica o algoritmo **Murmur hash** sobre a chave, produzindo um número, e calcula o módulo pelo número de partições (`hash(key) % num_partitions`) para decidir a partição de destino. A mesma chave sempre produz o mesmo número — e portanto sempre cai na mesma partição.

```js
await producer.send({
  topic: 'match-events',
  messages: [{ key: matchId, value: JSON.stringify(event) }],
});
```

Isso garante ordenação por entidade: todos os eventos com a mesma chave (ex.: o mesmo `match_id`, ou o mesmo `order_id`) chegam sempre à mesma partição, processados em ordem por um único consumer. Sem partition key, a distribuição é round-robin e eventos da mesma entidade podem cair em partições diferentes — sem garantia de ordem entre eles.

**Isso é hash-based sharding simples**, com a mesma limitação estrutural que [[wiki/concepts/consistent-hashing]] documenta: mudar o número de partições muda o resultado do módulo para praticamente todas as chaves já existentes, exigindo reprocessamento completo do roteamento — não há "anel" absorvendo a mudança de forma incremental como em consistent hashing.

## Consumer Groups

Consumers se organizam em **consumer groups**, identificados por um `group_id`:

```js
const consumer = kafka.consumer({ groupId: 'event-service' });
```

Dentro de um mesmo consumer group, cada partição é entregue a **um único consumer** — nunca dois consumers do mesmo grupo processam a mesma partição ao mesmo tempo. Isso evita duplicação de processamento (ex.: dois consumers gravando o mesmo gol duas vezes no banco). Consumers de **grupos diferentes**, por outro lado, recebem cópias independentes do mesmo tópico — é assim que dois pipelines distintos (ex.: um gravando a timeline completa no Postgres, outro atualizando um cache de placar no Redis) podem consumir o mesmo tópico sem interferir um no outro.

## Offset Commit: por que mais consumers não paralelizam sozinhos

O Kafka só entrega a próxima mensagem de uma partição para um consumer depois que esse consumer **comita o offset** da mensagem anterior — avisando "já processei, pode me entregar o próximo". Enquanto isso não acontece, nenhum outro consumer do mesmo grupo recebe trabalho daquela partição, mesmo estando ocioso.

Essa é a razão pela qual **subir mais consumers sem criar mais partições não paraleliza nada** — diferente do RabbitMQ/SQS, onde consumers adicionais competem livremente por mensagens da mesma fila. É também o mecanismo que impede perda de eventos: se o Kafka entregasse a próxima mensagem antes do commit e o consumer morresse no meio do processamento, aquele evento seria perdido — o offset commit garante que só se avança quando há confirmação de processamento.

## Rebalance

Se um consumer de um grupo cai, o Kafka reatribui as partições órfãs aos consumers restantes (**rebalance**). Um único consumer pode processar várias partições sem problema — o que nunca pode acontecer é a mesma partição sendo processada por dois consumers do mesmo grupo simultaneamente.

## Event Replay

Como o Kafka retém eventos além do momento em que foram consumidos, é possível criar um consumer novo, com regra de negócio corrigida, e processá-lo desde o primeiro offset do tópico — reconstruindo o estado do zero. Útil para corrigir bugs de processamento retroativamente (ex.: bug de cálculo financeiro) sem perder o histórico original de eventos.

## Configuração de Produtor Segura

`acks=all` (aguarda confirmação de todas as réplicas in-sync, não só do líder) + `enable.idempotence=true` (previne duplicatas em retry via sequência numérica) é a combinação recomendada para dados críticos, onde perda ou duplicação não são aceitáveis.

## Exemplo: Schema de Evento Normalizado (Placar de Futebol)

[[wiki/sources/world-cup-system-design]] mostra o par de schemas que uma Ingestion API tipicamente aplica antes de publicar num tópico: o evento **bruto** recebido do provedor externo é enxuto (`id`, `match`, `team_A`, `team_B`, `competition.title/stage`, `event`, `minute`, `sequence`, `payload`); a Ingestion API o **normaliza** para um formato mais rico antes de publicar no Kafka, adicionando proveniência e um ID próprio:

```json
{
  "event_id": "01XV0NDGSPN02Y6TMR9Y4TCY",
  "external_event_id": "9988123",
  "match": {
    "id": "01XV0NLJMT97YBER4JZYDPVX89",
    "title": "Brazil vs Marrocos",
    "competition": { "title": "world-cup-2026", "stage": "group_stage" },
    "participants": [{ "id": "BRA", "name": "Brazil" }, { "id": "MAR", "name": "Marrocos" }]
  },
  "minute": 21,
  "type": "GOAL",
  "sequence": 2,
  "payload": { "team_id": "MAR", "player_id": "player_10", "player_name": "Ismael Saibari" },
  "received_at": "2026-13-10T19:21:14Z",
  "source": "sports-data-provider-x"
}
```

A taxonomia de eventos de partida é fechada: `MATCH_STARTED`, `GOAL`, `YELLOW_CARD`, `RED_CARD`, `VAR_REVIEW_STARTED`, `VAR_DECISION`, `CORNER_KICK`, `PENALTY`, `FOUL`, `SUBSTITUTION`, `MATCH_ENDED`. O consumer que persiste a timeline completa grava esse evento em duas tabelas relacionais — `matches` (dados da partida) e `match_events` (`event_id`, `external_event_id`, `match_id`, `minute`, `type`, `payload` como JSONB, `received_at`, `source`) — o event log de [[wiki/concepts/event-sourcing]] materializado como schema SQL concreto.

## Key Sources

- [[wiki/sources/kafka]] — partition key e ordenação por entidade, paralelismo limitado ao número de partições, Kafka vs. RabbitMQ, configuração segura de producer (`acks=all`, `enable.idempotence=true`)
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — mecanismo do hash Murmur + módulo para roteamento de partição explicado passo a passo, offset commit como razão de consumers ociosos, dois consumer groups independentes consumindo o mesmo tópico para propósitos diferentes (persistência completa vs. cache de estado), event replay motivado por bug de cálculo financeiro
- [[wiki/sources/world-cup-system-design]] — slide deck da mesma aula: schema JSON completo do evento bruto vs. normalizado, taxonomia fechada de 11 tipos de evento, SQL de persistência em `matches`/`match_events`
