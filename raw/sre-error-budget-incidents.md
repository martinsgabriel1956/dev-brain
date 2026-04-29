---
date: 2026-04-17
tags: [tech-mentor, sre, error-budget, incident, post-mortem, confiabilidade]
skill: tech-mentor-infra/references/sre
level: arquiteto
---

# SRE — Error Budget, Incident Lifecycle, Post-mortem e Runbook

## Error Budget

### Conceito
Se o SLO é 99.9% de disponibilidade/mês, o **error budget** é os 0.1% restantes — equivalente a ~43 minutos de downtime por mês. É uma ferramenta de alinhamento: o produto decide como "gastar" esse budget entre features arriscadas e confiabilidade.

```
SLO: 99.9% → Error Budget: 43 min/mês

Semana 1: deploy com bug → 15 min de degradação → 28 min restantes
Semana 2: migração de banco → 20 min de degradação → 8 min restantes
Semana 3: se erro → freeze de deploys até virar o mês
```

### Burn Rate Alerting

Em vez de alertar quando o SLO é violado (tarde demais), alerte quando o budget está sendo **consumido em ritmo acelerado**.

```
Burn rate = taxa de consumo atual / taxa sustentável

Se SLO = 99.9% e burn rate = 14.4x:
→ o mês inteiro de budget será consumido em 2 horas
→ alerte agora, não quando o budget acabar
```

```yaml
# Prometheus — alerta de burn rate (Google SRE Workbook approach)
groups:
  - name: error-budget
    rules:
      # Burn rate alto: 14.4x por 5 min → consome budget em 1h
      - alert: ErrorBudgetFastBurn
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[5m])) /
            sum(rate(http_requests_total[5m]))
          ) > 0.144  # 14.4× × (1 - 0.999) = 0.144
        for: 5m
        labels: { severity: critical, page: "true" }
        annotations:
          summary: "Error budget burning at 14.4x rate — exhausted in 1h"

      # Burn rate médio: 6x por 30min → consome em 6h
      - alert: ErrorBudgetSlowBurn
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[30m])) /
            sum(rate(http_requests_total[30m]))
          ) > 0.06
        for: 30m
        labels: { severity: warning }
```

### Política de Error Budget

```
Budget > 50% restante → times podem fazer deploys livremente
Budget entre 10-50%   → deploys requerem aprovação
Budget < 10%          → freeze de deploys não-críticos
Budget esgotado       → apenas hotfixes de segurança/confiabilidade
```

---

## SRE Incident Lifecycle

### Severidades

| Nível | Critério | Resposta |
|---|---|---|
| **SEV-1** | Sistema completamente indisponível, perda financeira ativa | Resposta imediata, war room, C-level notificado |
| **SEV-2** | Feature crítica degradada, impacto a % significativa de usuários | Resposta em < 15min, on-call escalado |
| **SEV-3** | Bug com workaround, impacto limitado | Resposta em < 2h, tratado durante horário comercial |
| **SEV-4** | Inconveniência, sem impacto a usuário | Agendado no próximo sprint |

### Roles no Incidente

**IC (Incident Commander):** coordena a resposta, delega investigação, mantém comunicação.
**TL (Technical Lead):** lidera a investigação técnica, não coordena.
**Comunicador:** atualiza stakeholders e status page.
**Escriba:** documenta timeline em tempo real.

### Fluxo

```
1. Alerta → on-call recebe page
2. Acknowledges em < 5min
3. Avalia severidade → declara incidente se SEV-2+
4. Abre canal de incidente (#incident-YYYY-MM-DD-HH)
5. Assume papel de IC (ou escalona)
6. Investigação → mitigação (não precisa ser a causa raiz)
7. Resolve → comunica resolução
8. Abre post-mortem em 24-48h
```

---

## Post-mortem Blameless

**Princípio:** o sistema falhou, não as pessoas. O objetivo é aprender, não punir.

```markdown
# Post-mortem: [Título descritivo do incidente]

**Data:** 2026-04-15
**Duração:** 47 minutos (14:23 - 15:10 UTC)
**Severidade:** SEV-2
**Impacto:** 23% dos usuários não conseguiram completar checkout

## Resumo Executivo
[2-3 linhas do que aconteceu e como foi resolvido]

## Timeline
- 14:23 — Alerta: taxa de erros 5xx > 5% em order-api
- 14:28 — On-call acknowledges, inicia investigação
- 14:35 — Identifica deploy das 14:15 como causa provável
- 14:40 — Rollback iniciado
- 14:52 — Métricas normalizando
- 15:10 — Incidente encerrado, métricas estáveis

## Causa Raiz
Migration de banco V42 adicionou coluna NOT NULL sem default.
Pods em rolling update tentaram escrever com schema antigo → constraint violation.

## Fatores Contribuintes
- Sem validação de schema compatibility no pipeline de CI
- Expand-Contract não foi seguido (adicionou NOT NULL diretamente)
- Testcontainers não cobria esse caso em testes de integração

## O que Funcionou Bem
- Alerta disparou em 3 minutos após o deploy
- Rollback foi executado rapidamente graças ao runbook atualizado

## Ações Corretivas

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Adicionar validação de migration no CI | @eng-plat | 2026-04-22 |
| Criar guideline de Expand-Contract no wiki | @tech-lead | 2026-04-19 |
| Adicionar teste de migration no Testcontainers | @backend-team | 2026-04-25 |
```

---

## Runbook Efetivo

Um runbook ruim é uma lista de passos que ninguém segue em produção. Um runbook efetivo é **executável sob stress**.

```markdown
# Runbook: Alta Taxa de Erros em order-api

## Quando usar este runbook
Taxa de erros HTTP 5xx > 1% por mais de 3 minutos.

## 1. Diagnóstico Rápido (< 5 min)
```bash
# Ver últimos logs de erro
kubectl logs -n production deploy/order-api --since=5m | grep '"level":"error"' | tail -20

# Verificar se é apenas uma instância (pod específico)
kubectl top pods -n production -l app=order-api
```

## 2. Identificar a causa

**Se os erros começaram após um deploy recente:**
→ Vá para [Rollback](#rollback)

**Se é erro de banco de dados:**
→ Verifique `pg_stat_activity` — possível lock ou connection pool esgotado
→ Vá para [Mitigação de DB](#db)

## 3. Rollback {#rollback}
```bash
# Encontrar revisão anterior
kubectl rollout history deploy/order-api -n production

# Rollback para revisão anterior
kubectl rollout undo deploy/order-api -n production

# Verificar estabilização
kubectl rollout status deploy/order-api -n production
```

## 4. Escalonar para SEV-1
Se não resolver em 15 minutos → pager para tech lead e CTO.
```

---

## Game Day

Exercício planejado onde a equipe simula falhas em produção ou staging para validar runbooks, SLOs e capacidade de resposta.

**Estrutura:**
1. **Objetivo:** "validar que rollback funciona em < 5 minutos"
2. **Escopo:** staging com tráfego sintético
3. **Experimento:** kill de 50% dos pods de order-api
4. **Observação:** latência, taxa de erro, tempo de recuperação
5. **Retrospectiva:** o que funcionou, o que falhou, o que atualizar

## Conceitos Relacionados
[[sre-sli-slo-sla]] · [[observabilidade]] · [[architecture-fitness-functions]] · [[chaos-engineering]] · [[distributed-tracing]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
