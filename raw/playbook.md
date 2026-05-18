---
date: 2026-05-17
tags: [tech-mentor, infra, ops, playbook, incident-response]
skill: tech-mentor-infra/references/ops-docs
level: intermediário
---

# Playbook

## Contexto
Playbook é um documento **estratégico e situacional** que define como responder a uma classe de problema ou incidente. Diferente do runbook, ele não pressupõe que você sabe o que fazer — ele te guia pela **tomada de decisão sob pressão**.

Vive no ciclo **durante o incidente**: é consultado quando um alerta dispara e a causa ainda é desconhecida.

## Como Funciona

Um playbook tem **árvores de decisão**, não passos lineares. A premissa é: algo deu errado, agora preciso descobrir o quê e agir.

Estrutura típica:

- **Sintoma / Trigger** — qual alerta ou comportamento levou aqui
- **Hipóteses ordenadas por probabilidade** — do mais comum ao mais raro
- **Verificações por hipótese** — como confirmar ou descartar cada causa
- **Ações por hipótese** — o que fazer se a hipótese for verdadeira
- **Escalada** — quando e para quem escalar

## Código de Referência

```markdown
## Playbook: Alta latência na API (p99 > 2s)

**Trigger:** alerta `api_latency_p99 > 2000ms` por mais de 5 minutos

---

### 1. Checar saúde dos pods
```bash
kubectl get pods -n production
kubectl top pods -n production
```
- CPU > 80% → escalar horizontalmente: `kubectl scale deployment/api --replicas=+2`
- Pods em `CrashLoopBackOff` → checar logs: `kubectl logs <pod> --previous`

---

### 2. Checar slow queries no banco
```bash
# No RDS Performance Insights ou via psql:
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```
- Query > 500ms sem index → adicionar index em hotfix branch, abrir ticket
- Lock ativo → identificar PID e avaliar kill: `SELECT pg_terminate_backend(pid)`

---

### 3. Checar dependências externas
- Stripe: https://status.stripe.com
- SendGrid: https://status.sendgrid.com
- Se down → ativar feature flag `USE_CIRCUIT_BREAKER=true` e notificar stakeholders

---

### 4. Checar cache hit rate Redis
```bash
redis-cli INFO stats | grep keyspace_hits
redis-cli INFO stats | grep keyspace_misses
```
- Hit rate < 80% → investigar TTL e padrões de invalidação

---

### 5. Nenhuma hipótese confirmada → Escalar
- Abrir incidente P1 no PagerDuty
- Notificar canal #incidents no Slack
- Considerar rollback do último deploy: `kubectl rollout undo deployment/api`
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Decisão estruturada | Reduz cognitive load em momentos de stress | Pode dar falsa sensação de cobertura total |
| Onboarding | Novos engenheiros respondem incidentes mais rápido | Requer manutenção ativa para não ficar defasado |
| Cobertura | Cobre classes de problemas, não casos únicos | Situações novas exigem improviso mesmo com playbook |

## Quando Usar / Quando Evitar

**Usar quando:**
- Um alerta disparou e a causa é desconhecida
- O problema tem múltiplas causas possíveis com passos diferentes para cada uma
- Quero onboarding rápido de novos engenheiros em resposta a incidentes

**Evitar quando:**
- A operação é bem definida e sem decisões → use [[runbook]]
- O problema nunca aconteceu antes (não há padrão para playbook ainda)

## Conceitos Relacionados
[[runbook]] · [[post-mortem]] · [[sre]] · [[oncall]] · [[circuit-breaker]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-05-17*
