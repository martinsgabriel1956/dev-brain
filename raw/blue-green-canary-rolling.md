---
date: 2026-04-14
tags: [tech-mentor, devops, deploy, resiliência, cicd]
skill: tech-mentor-platform/references/cicd
level: intermediário
---

# Blue/Green, Canary e Rolling Deploy

## Contexto

Estratégias de deploy determinam como uma nova versão de software é liberada para produção. O objetivo em todos os casos é o mesmo: reduzir o risco de uma versão defeituosa impactar usuários, mantendo a capacidade de rollback rápido.

Cada estratégia tem um perfil diferente de trade-off entre velocidade, risco e complexidade de infraestrutura.

## Como Funciona

### Blue/Green Deploy

Dois ambientes idênticos: Blue (versão atual) e Green (nova versão). A troca é atômica no load balancer — sem downtime e com rollback instantâneo.

```
           Load Balancer
                │
          ┌─────┴─────┐
          │           │
       Blue (v1)   Green (v2)
       [100%]       [0%]    ← antes do deploy

                │ swap
                ▼

       Blue (v1)   Green (v2)
         [0%]      [100%]   ← após deploy
         ↑
         (fica ligado para rollback imediato)
```

```yaml
# Kubernetes com dois Deployments
# Troca feita via Service selector

apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
    version: green  # ← muda de "blue" para "green" para fazer o swap
  ports:
    - port: 80
      targetPort: 3000
```

**Vantagens:** rollback instantâneo, sem tráfego misto, testável em produção antes da troca.

**Desvantagens:** dobra o custo de infraestrutura durante o deploy, migrations de DB precisam ser compatíveis com ambas as versões simultaneamente.

### Canary Release

Uma porcentagem pequena do tráfego vai para a nova versão. O percentual aumenta gradualmente conforme métricas são validadas. Rollback automático se métricas degradam.

```
v1: ████████████████████ 95%
v2: █                    5%   ← Canary inicial

→ sem alertas após 30min

v1: ████████████████     80%
v2: ████                 20%  → sem alertas

→ sem alertas após 1h

v1:                       0%
v2: ████████████████████ 100% → deploy completo
```

```yaml
# Argo Rollouts — canary automatizado com análise
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: app-rollout
spec:
  strategy:
    canary:
      steps:
        - setWeight: 5     # 5% do tráfego para nova versão
        - pause: { duration: 30m }
        - setWeight: 20
        - pause: { duration: 1h }
        - analysis:
            templates:
              - templateName: error-rate-check
        - setWeight: 100
      analysis:
        templates:
          - templateName: error-rate-check
        startingStep: 2

---
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: error-rate-check
spec:
  metrics:
    - name: error-rate
      successCondition: result[0] < 0.01  # < 1% de erros
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{status=~"5.."}[5m])) /
            sum(rate(http_requests_total[5m]))
```

**Vantagens:** exposição gradual ao risco, feedback real de produção com impacto limitado, rollback automático baseado em métricas.

**Desvantagens:** duas versões simultâneas requerem backward compatibility (API, DB schema), requer observabilidade madura para análise automática.

### Rolling Update

Pods/instâncias são substituídas gradualmente, um lote por vez. Sempre há uma mistura de versões durante o deploy.

```
Deployment com 4 réplicas, maxUnavailable=1, maxSurge=1:

Passo 1: [v1, v1, v1, v1]
Passo 2: [v2, v1, v1, v1]  ← 1 pod atualizado
Passo 3: [v2, v2, v1, v1]  ← 2 pods atualizados
Passo 4: [v2, v2, v2, v1]
Passo 5: [v2, v2, v2, v2]  ← deploy completo
```

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1   # máximo de pods indisponíveis durante update
      maxSurge: 1         # máximo de pods extras durante update
```

**Vantagens:** sem custo extra de infraestrutura, nativo no Kubernetes, simples de configurar.

**Desvantagens:** tráfego misto inevitável (v1 e v2 servindo requests ao mesmo tempo), rollback mais lento (precisa fazer o processo inverso), sem análise automática de métricas.

### Comparação

| Estratégia | Rollback | Custo | Tráfego misto | Quando usar |
|---|---|---|---|---|
| **Blue/Green** | Instantâneo (segundos) | 2x infraestrutura | Não | Deploy de alto risco, precisa de rollback imediato |
| **Canary** | Automático + rápido | +5-20% extra temporário | Sim | Mudanças que afetam UX ou comportamento, com observabilidade madura |
| **Rolling** | Lento (réplica por réplica) | Sem custo extra | Sim | Deploy rotineiro de baixo risco |

### Database Migrations Durante Deploy

O ponto crítico: a migration de banco deve ser compatível com **ambas** as versões do código durante a janela de deploy.

```
Cenário: renomear coluna user_email → email

❌ Errado — migration e deploy simultâneos
  1. Deploy v2 com campo "email"
  2. Migration renomeia "user_email" → "email"
  (durante a transição, v1 ainda usa "user_email" → quebra)

✅ Correto — Expand-Contract em 3 fases
  Fase 1: migration adiciona coluna "email" (nullable), mantém "user_email"
           v1 usa "user_email", v2 escreve em ambas e lê de "email"
  Fase 2: backfill de "user_email" para "email" em todos os rows
  Fase 3: migration remove "user_email" quando v1 não existe mais
```

## Quando Usar / Quando Evitar

**Blue/Green:** releases críticos (checkout, pagamentos), quando rollback em segundos é mandatório.

**Canary:** features novas que podem ter impacto imprevisto no comportamento do usuário, quando você tem Prometheus + análise automática configurados.

**Rolling:** deploys rotineiros de microsserviços, quando a mudança é backwards compatible e você aceita um rollback mais lento.

## Conceitos Relacionados

[[feature-flags]] · [[zero-downtime-deploy]] · [[strangler-fig]] · [[observabilidade]] · [[cicd-pipeline]]

---
*Fonte: tech-mentor skill · tech-mentor-platform · 2026-04-14*
