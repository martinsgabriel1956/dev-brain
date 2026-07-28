---
type: concept
title: "Expand-Contract"
aliases: ["expand contract pattern", "parallel change", "migration em 3 fases"]
date_created: 2026-04-22
date_updated: 2026-07-28
source_count: 2
tags: [devops, deploy, database, migration, backward-compatibility, infra]
skill: tech-mentor-infra
status: stable
---

# Expand-Contract

Padrão para DB migrations compatíveis com duas versões do código simultaneamente — obrigatório em [[concepts/blue-green-deploy]], [[concepts/canary-release]] e [[concepts/rolling-update]].

## O Problema

```
❌ Errado — migration e deploy simultâneos
  1. Deploy v2 com campo "email"
  2. Migration renomeia "user_email" → "email"
  Durante a transição: v1 ainda usa "user_email" → quebra
```

## Solução: 3 Fases

```
Fase 1 — EXPAND
  Migration: adiciona coluna "email" (nullable), mantém "user_email"
  v1: lê/escreve em "user_email"
  v2: escreve em ambas, lê de "email"

Fase 2 — BACKFILL
  Script migra dados de "user_email" → "email" em todos os rows
  Ambas as versões funcionam

Fase 3 — CONTRACT
  v1 removida do tráfego
  Migration: remove coluna "user_email"
```

## Regra

Qualquer migration que renomeia, remove ou muda tipo de coluna **deve** usar Expand-Contract quando há deploy sem downtime. Nunca faça rename atômico em produção com tráfego ativo.

## Relacionado

[[concepts/database-transactions]] — cada fase é uma transação atômica separada.

[[wiki/concepts/database-migration]] — Expand-Contract é o padrão a aplicar quando a operação de migration não é trivial (rename, drop, mudança de tipo). Relato de incidente real: adicionar campo derivado em tabela com ~100k linhas travou a tabela por ~5 minutos em produção — exemplo do custo de pular direto para a operação final em vez de expandir/preencher/contrair.

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — incidente de lock em produção ao alterar tabela grande
