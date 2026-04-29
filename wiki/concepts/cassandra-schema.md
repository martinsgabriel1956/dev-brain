---
type: concept
title: "Cassandra Schema Design"
aliases: ["cassandra", "cassandra schema", "wide column", "partition key", "clustering key"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, cassandra, nosql, wide-column, system-design, escrita-intensa]
skill: tech-mentor-system-design
status: stable
---

# Cassandra Schema Design

Banco wide-column projetado para escrita intensa, TTL nativo, e scale linear horizontal. Schema deve ser modelado pelo padrão de acesso — não pelo domínio.

## Por que Cassandra para Chat

```
✅ 1.15M writes/s — quase sempre INSERT, sem update de rows existentes
✅ TTL nativo por célula — apagar mensagens pendentes após 30 dias
✅ Scale linear: adicionar nós aumenta capacidade proporcionalmente
✅ Replicação multi-datacenter nativa
✅ Leitura por conversa: últimas N mensagens — padrão simples de range scan
❌ Sem joins — aceitável para chat (sem necessidade de joins)
❌ Eventual consistency — tolerável (ordenação via Snowflake ID)
```

## Schema WhatsApp

```sql
-- Mensagens de uma conversa
CREATE TABLE messages (
  conversation_id UUID,
  message_id      BIGINT,   -- Snowflake ID: ordena cronologicamente
  sender_id       UUID,
  content         TEXT,
  type            TEXT,     -- text, image, video
  status          TEXT,
  created_at      TIMESTAMP,
  PRIMARY KEY (conversation_id, message_id)
) WITH CLUSTERING ORDER BY (message_id DESC);
-- partition_key = conversation_id → mesma conversa no mesmo nó
-- clustering_key = message_id DESC → mais recentes primeiro

-- Fila de mensagens offline
CREATE TABLE pending_messages (
  recipient_id UUID,
  message_id   BIGINT,
  -- ... demais campos
  PRIMARY KEY (recipient_id, message_id)
) WITH default_time_to_live = 2592000;  -- TTL 30 dias
```

## Regra de Ouro

**Partition key = como você vai buscar**. Mensagens buscadas por conversa → `conversation_id` como partition key. Mensagens pendentes buscadas por destinatário → `recipient_id`.

## Relacionado

[[concepts/nosql]] — comparativo com outros tipos de NoSQL.

## Key Sources

- [[sources/case-whatsapp]]
