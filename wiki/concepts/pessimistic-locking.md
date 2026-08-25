---
type: concept
title: "Pessimistic Locking"
aliases: ["locking pessimista", "lock pessimista", "SELECT FOR UPDATE", "for update"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 1
tags: [concorrencia, race-condition, locking, sql, transactions, system-design]
skill: tech-mentor-system-design
status: draft
---

# Pessimistic Locking

Estratégia de controle de concorrência que assume que conflitos **vão** acontecer, e por isso trava o recurso antes de qualquer leitura/escrita crítica — ninguém mais pode tocar naquela linha até quem travou liberar.

## Como funciona (`SELECT ... FOR UPDATE`)

```sql
BEGIN;

SELECT ingressos_disponiveis
FROM shows
WHERE show = 'Linkin Park'
FOR UPDATE; -- trava a linha até COMMIT/ROLLBACK

UPDATE shows
SET ingressos_disponiveis = ingressos_disponiveis - 1
WHERE show = 'Linkin Park'
  AND ingressos_disponiveis > 0;

COMMIT;
```

`FOR UPDATE` diz ao banco: nenhuma outra transação pode modificar essa linha enquanto esta transação não terminar (`COMMIT` ou `ROLLBACK`). Quem chegar depois fica esperando em fila até a linha ser liberada — não recebe um erro, apenas aguarda a vez.

Se a linha travada acabar em um estado que impede a operação do próximo da fila (ex.: ingressos zerados), o `UPDATE` dele simplesmente afeta zero linhas quando é a vez dele rodar — falha de forma limpa, sem cobrar ou processar nada indevido.

## Quando usar

- **Alta contenção**: muitos processos/usuários disputando o mesmo recurso ao mesmo tempo.
- **Custo de conflito alto**: quando um race condition não tratado geraria dano financeiro ou operacional caro o suficiente para justificar aceitar o gargalo de fila.
- Operação protegida é **rápida** — a transação não deve ficar aberta por muito tempo, ou a fila cresce.

## Tradeoff

Trava a linha = potencial gargalo. Sob alta concorrência, todos os processos que disputam o mesmo recurso ficam serializados numa fila — se a operação demora ou a contenção é extrema, a latência percebida cresce. Comparar sempre com [[wiki/concepts/optimistic-concurrency-control]] antes de escolher.

## Erro fatal: transação + chamada externa no meio

Nunca abrir uma transação, travar uma linha com `FOR UPDATE`, e dentro dela fazer uma chamada de rede (API de pagamento, API externa qualquer). Isso mantém a linha travada pelo tempo da chamada de rede (podem ser segundos), formando uma fila enorme para quem só quer ler/escrever aquela linha. A ordem correta: fechar a transação com o banco primeiro (com tudo que precisa ser atômico ali dentro), e só depois — fora da transação — conversar com sistemas externos. Isso é citado explicitamente como motivo de eliminação imediata em [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]].

## Key Sources

- [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] — introdução da técnica com exemplo de venda de ingresso concorrente; demonstração empírica com 5 conexões simultâneas no PostgreSQL confirmando que só a primeira consegue reservar
