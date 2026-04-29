---
type: concept
title: "Runbook"
aliases: ["runbook", "playbook", "operational runbook"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, operações, incidentes, documentação, kubernetes]
skill: tech-mentor-infra
status: stable
---

# Runbook

Documento operacional executável sob stress. Runbook ruim = lista de passos genéricos que ninguém segue em produção. Runbook efetivo = diagnóstico rápido + árvore de decisão + comandos copiáveis.

## Estrutura Efetiva

```markdown
# Runbook: [Sintoma específico, não nome do sistema]

## Quando usar
[Condição objetiva — ex: "taxa de erros 5xx > 1% por > 3 minutos"]

## 1. Diagnóstico Rápido (< 5 min)
[Comandos prontos para copiar]

## 2. Árvore de Causa
Se [sintoma A] → [ação A]
Se [sintoma B] → [ação B]

## 3. Ações por Causa
[Comandos específicos por causa]

## 4. Critério de Escalona
Se não resolver em X minutos → SEV-1, page [quem]
```

## Exemplo — Alta Taxa de Erros em order-api

```bash
# Diagnóstico: últimos logs de erro
kubectl logs -n production deploy/order-api --since=5m | grep '"level":"error"' | tail -20

# Verificar se é pod específico
kubectl top pods -n production -l app=order-api

# Rollback se causa for deploy recente
kubectl rollout history deploy/order-api -n production
kubectl rollout undo deploy/order-api -n production
kubectl rollout status deploy/order-api -n production
```

## Critérios de Qualidade

- Alguém que nunca viu o sistema consegue executar?
- Tem comando para cada ação descrita?
- Tem critério explícito de quando escalonar?
- Foi testado em [[concepts/game-day]]?

## Onde Manter

Versionado junto ao código (mesmo repo) garante atualização junto com mudanças de infraestrutura. Wiki pode ficar desatualizado.

## Key Sources

- [[sources/sre-error-budget-incidents]]
