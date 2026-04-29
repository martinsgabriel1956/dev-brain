---
type: concept
title: "Game Day"
aliases: ["game day", "chaos day", "simulação de falha", "fire drill"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, resiliencia, chaos-engineering, operações, runbook]
skill: tech-mentor-infra
status: stable
---

# Game Day

Exercício planejado onde a equipe simula falhas em staging para validar runbooks, SLOs e capacidade de resposta — antes do incidente real.

## Estrutura

```
1. Objetivo mensurável: "validar que rollback funciona em < 5 minutos"
2. Escopo: staging com tráfego sintético (nunca produção sem aprovação)
3. Experimento: ação de falha específica (ex: kill 50% dos pods de order-api)
4. Observação: latência, taxa de erro, tempo de recuperação, aderência ao runbook
5. Retrospectiva: o que funcionou, o que falhou, o que atualizar
```

## Resultado Esperado

- [[concepts/runbook]] atualizado com gaps descobertos
- Time treinado para executar o fluxo de [[concepts/incident-lifecycle]] sob pressão simulada
- SLOs validados contra falhas reais (não apenas teóricas)
- Confiança → escalona menos, resolve mais rápido

## Relação com Chaos Engineering

Game Day é chaos engineering com escopo controlado e objetivo definido. Chaos engineering pode ser contínuo e automatizado; Game Day é episódico e humano.

## Key Sources

- [[sources/sre-error-budget-incidents]]
