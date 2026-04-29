---
type: source
title: "DynamoDB — Single-Table Design, GSI/LSI, Streams e DAX"
aliases: ["dynamodb", "single table design", "gsi dynamodb", "dynamodb streams", "dax", "partition key dynamodb"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/dynamodb.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [dynamodb, single-table-design, gsi, lsi, dynamodb-streams, dax, partition-key, access-pattern, nosql, aws]
skill: tech-mentor-data
status: stable
---

## TL;DR

DynamoDB: NoSQL serverless AWS com escala ilimitada. Single-Table Design: todos os tipos de entidade em uma tabela, acesso por PK+SK patterns. GSI (Global Secondary Index) permite queries por outras dimensões. DAX: cache in-memory para reads com latência de microssegundos. DynamoDB Streams para CDC e triggers Lambda. Modelagem orientada a access patterns — definir queries antes de definir schema.

## Key Claims

**Claim:** Single-Table Design é obrigatório no DynamoDB — uma tabela por entidade é anti-pattern.
**Evidence:** DynamoDB cobra por RCU/WCU por tabela. JOIN não existe — para buscar Order + OrderItems em uma query, ambos devem estar na mesma tabela. PK: `USER#123`, SK: `ORDER#456` para order; `ORDER#456#ITEM#1` para item. Query: `PK = USER#123 AND SK begins_with ORDER#` retorna tudo de uma vez. Uma tabela, múltiplos tipos de entidade.
**Confidence:** alta

**Claim:** Access patterns devem ser definidos antes da modelagem — DynamoDB não permite queries ad-hoc como SQL.
**Evidence:** PostgreSQL: qualquer coluna pode ser filtrada ad-hoc (full scan se não tiver índice). DynamoDB: apenas PK e SK (ou GSI/LSI) são eficientes. Query não planejado sem índice = Scan completo (caro e lento). Processo: listar todas as queries que a aplicação precisa → derivar PK/SK/GSI que as suportam.
**Confidence:** alta

**Claim:** GSI é a forma de suportar múltiplos access patterns — cada GSI é uma cópia parcial da tabela.
**Evidence:** Tabela principal: PK=userId, SK=orderId. GSI "by-status": PK=status, SK=createdAt → query "todos os pedidos pending ordenados por data". GSI cobra storage adicional (cópia dos dados) e RCU/WCU independentes. Até 20 GSIs por tabela.
**Confidence:** alta

**Claim:** DynamoDB Streams + Lambda é o CDC nativo AWS — reage a INSERT/UPDATE/DELETE sem polling.
**Evidence:** Stream entrega cada modificação com before/after state para a função Lambda. Casos: invalidar cache no DAX, sincronizar com Elasticsearch, audit log imutável, replicação cross-region. Garantia: at-least-once, ordenado por partition key. Lambda processa em batch configurável.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/dynamodb]]
- [[concepts/single-table-design]]
- [[concepts/gsi]]
- [[concepts/dynamodb-streams]]
- [[entities/dax]]
- [[concepts/access-pattern-design]]
- [[entities/aws]]

## Open Questions

- Single-Table Design com muitos access patterns (20+) — quando é hora de separar em múltiplas tabelas?
- DynamoDB vs MongoDB para casos de uso de documento com queries flexíveis — quando cada um vence?
