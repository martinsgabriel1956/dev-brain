---
type: concept
title: "Inbox Pattern"
aliases: ["inbox", "transactional inbox", "webhook deduplication", "consumer idempotency"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 2
tags: [sistemas-distribuidos, mensageria, idempotencia, webhook, at-least-once]
skill: tech-mentor-backend
status: stub
---

# Inbox Pattern

Complementar ao [[wiki/concepts/outbox-pattern]], mas do lado de quem **consome** um evento ou webhook em vez de publicá-lo. Garante que uma entrega repetida — inevitável sob **at-least-once delivery** — não aplique o mesmo efeito duas vezes.

## Mecanismo

Uma tabela `inbox_events` guarda a combinação `provedor + event_id` (ou `topic + partition + offset` em mensageria):

```sql
INSERT INTO inbox_events (provider, event_id, processed_at)
VALUES ($1, $2, NOW())
ON CONFLICT (provider, event_id) DO NOTHING
RETURNING event_id;
-- linha retornada → primeira entrega, aplicar o efeito
-- nenhuma linha retornada → entrega duplicada, responder sucesso sem reaplicar
```

O primeiro evento cria o registro e aplica a mudança de negócio (ex.: crédito numa fatura). As entregas seguintes encontram o registro já existente, não aplicam o efeito de novo, e ainda respondem sucesso ao provedor — o que encerra o retry do lado dele.

## Por Que É Necessário Mesmo Quando a API Funciona

Mesmo que a chamada original tenha sido bem-sucedida, o provedor pode reentregar o mesmo evento depois — não porque o evento falhou, mas porque a *confirmação* de recebimento se perdeu no caminho. O provedor vê a chamada como pendente e reentrega achando que nada foi processado. Sem inbox, essa reentrega duplicaria o efeito (crédito, baixa de boleto, liquidação de cartão).

## Onde Aparece

Webhooks (ver [[wiki/concepts/webhook-signature-validation]]), consumidores Kafka/SQS com at-least-once delivery, e qualquer fronteira de serviço onde uma [[wiki/concepts/idempotencia|chave idempotente]] precisa atravessar de um sistema para outro.

## Key Sources

- [[wiki/sources/outbox-pattern]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — inbox persistente por `provedor + event ID`, e por que a confirmação de recebimento perdida (não a entrega em si) motiva a reentrega
