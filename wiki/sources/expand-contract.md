---
type: source
title: "Expand-Contract"
aliases: ["expand contract", "parallel change", "versioned contract migration", "schema migration zero downtime"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/expand-contract.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [expand-contract, parallel-change, zero-downtime, schema-migration, api-versioning, backward-compatibility]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Expand-Contract (também: Parallel Change) é o padrão para mudar contratos — banco, API, eventos — sem downtime e sem coordenação simultânea. 3 fases: Expand (adicionar novo), Migrate (mover clientes), Contract (remover antigo). Aplicável a: renomear coluna, mover campo de API, evoluir schema de evento Kafka. O princípio: nunca remover antes de todos os consumidores migrarem.

## Key Claims

**Claim:** Renomear coluna de banco sem Expand-Contract causa downtime — rolling deploy exige compatibilidade temporária.
**Evidence:** Deploy rolling: app v1 e v2 rodam simultaneamente por N minutos. Se v2 renomeia `first_name` para `full_name` e dropa `first_name` no mesmo migration: v1 ainda em execução falha com "column not found". Solução: Migration 1 ADD COLUMN, Deploy v2 (escreve nos dois), backfill, Migration 2 DROP COLUMN após 100% v2.
**Confidence:** alta

**Claim:** A fase Contract (remoção) só pode acontecer após 100% dos consumidores terem migrado — em microserviços, isso significa verificar todos os clientes.
**Evidence:** API: remover campo da resposta sem verificar todos os clientes = breaking change silencioso. Consumer que depende do campo antigo falha sem mensagem clara. Processo: deprecation notice (`Sunset: date` no header), monitorar logs de acesso ao campo, remover apenas após zero uso confirmado.
**Confidence:** alta

**Claim:** Expand-Contract em eventos Kafka aplica o mesmo princípio — Schema Registry com BACKWARD compatibility faz cumprir.
**Evidence:** Evento v1: `{ orderId, total }`. Novo campo: `currency`. Fase Expand: adicionar `currency` com default como campo opcional (Schema Registry verifica BACKWARD). Fase Migrate: atualizar consumers para ler o campo. Fase Contract: tornar `currency` obrigatório apenas após todos os consumers atualizarem.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/expand-contract]]
- [[concepts/parallel-change]]
- [[concepts/zero-downtime]]
- [[concepts/schema-migration]]
- [[concepts/backward-compatibility]]
- [[concepts/schema-registry]]

## Open Questions

- Expand-Contract em banco com bilhões de rows — como fazer backfill sem locks e sem afetar performance?
- Quando Expand-Contract é over-engineering e uma janela de manutenção é mais simples?
