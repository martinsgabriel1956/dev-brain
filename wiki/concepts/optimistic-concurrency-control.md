---
type: concept
title: "Optimistic Concurrency Control (OCC)"
aliases: ["controle de concorrência otimista", "optimistic locking", "OCC", "version column"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 1
tags: [concorrencia, race-condition, locking, sql, version, system-design]
skill: tech-mentor-system-design
status: draft
---

# Optimistic Concurrency Control (OCC)

Estratégia de controle de concorrência que assume que conflitos são **raros** — não trava nada antecipadamente; em vez disso, detecta o conflito no momento da escrita, comparando o estado atual com o estado que foi lido antes.

## Como funciona

```sql
-- SELECT anterior leu ingressos_disponiveis = 1
UPDATE shows
SET ingressos_disponiveis = ingressos_disponiveis - 1
WHERE show_id = 'linkin-park'
  AND ingressos_disponiveis = 1; -- condição = valor lido antes
```

Se, entre o `SELECT` e o `UPDATE`, outro processo já tiver alterado a linha, a condição do `WHERE` deixa de bater e o `UPDATE` afeta **zero linhas** (`rowCount = 0`). A aplicação trata isso como conflito e decide: retry, ou informar o usuário que alguém chegou primeiro.

## A coluna `version`

Para tabelas com múltiplas colunas onde qualquer mudança pode gerar conflito (não só um contador simples), o padrão de mercado é uma coluna `version`, incrementada a cada escrita bem-sucedida:

```sql
ALTER TABLE accounts ADD COLUMN version INTEGER DEFAULT 0;

UPDATE accounts
SET balance = 70, version = version + 1
WHERE id = 1 AND version = 5; -- falha (0 rows) se version já mudou
```

Quem lê `version = 5` e tenta escrever só consegue se ninguém mais tiver escrito (e incrementado a version) nesse meio tempo. `rowCount = 0` → conflito → retry.

### Variação: condição de faixa em vez de igualdade exata

Em vez de `version = valor_lido` (igualdade exata, falha para todo mundo menos o primeiro), pode-se usar uma condição de faixa como `estoque > 0` — múltiplos compradores concorrentes conseguem escrever com sucesso enquanto o recurso não se esgotar de fato, em vez de o segundo já falhar mesmo havendo saldo suficiente. É uma decisão de regra de negócio, não uma regra fixa do padrão.

## Quando usar

- Conflitos são **raros** na prática — a maioria das tentativas de escrita não vai colidir.
- Menor latência que [[wiki/concepts/pessimistic-locking]]: não há fila/espera, porque nada é travado.
- Operações **longas** entre leitura e escrita (lock pessimista manteria o recurso travado por mais tempo).

## Tradeoff — degrada sob alta contenção

Sob alta contenção (muita gente disputando o mesmo recurso), a maioria das tentativas falha e precisa de retry — com 100 processos disputando, a cada rodada só um consegue e os outros ~99 tentam de novo, o que pode ser menos eficiente que simplesmente serializar tudo com [[wiki/concepts/pessimistic-locking]]. A escolha entre as duas estratégias depende diretamente da frequência esperada de conflito, não é uma preferência estilística.

## Prova empírica

[[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] demonstra a técnica com 5 conexões simultâneas contra PostgreSQL: o banco sempre serializa escritas concorrentes na mesma linha (nunca duas ao mesmo tempo), então só a primeira a rodar o `UPDATE` bate a condição de `version`; as demais descobrem, no `rowCount = 0`, que perderam a corrida.

## Relacionado

[[wiki/concepts/event-sourcing]] usa o mesmo mecanismo sob o nome `expectedRevision` para detectar conflito de escrita concorrente num stream de eventos.

## Key Sources

- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — introdução com exemplo de contador simples e coluna `version`; variação `estoque > 0`; demonstração empírica confirmando o mecanismo
