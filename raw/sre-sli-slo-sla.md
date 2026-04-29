---
date: 2026-04-14
tags: [tech-mentor, sre, observabilidade, confiabilidade, operações]
skill: tech-mentor-infra/references/sre
level: avançado
---

# SRE — SLI, SLO, SLA e Error Budget

## Contexto

Site Reliability Engineering (SRE) é a disciplina que trata confiabilidade de sistemas como um problema de engenharia. O framework central é: definir o que significa "suficientemente confiável" (SLO), medir se você está lá (SLI) e usar a "folga" disponível (Error Budget) para tomar decisões de velocidade vs. estabilidade.

Sem esse framework, a discussão de confiabilidade fica na base de "o sistema tá caindo?" — reativa e sem critério de decisão.

## Como Funciona

### SLI — Service Level Indicator

Métrica concreta que mede um aspecto da qualidade do serviço. Deve ser um número entre 0 e 1 (ou porcentagem).

```
Tipos comuns de SLI:

Disponibilidade:
  SLI = requests_success / requests_total

Latência:
  SLI = requests_under_300ms / requests_total

Freshness (dados):
  SLI = records_updated_in_last_hour / total_records

Durabilidade (storage):
  SLI = bytes_successfully_retrieved / bytes_written
```

```yaml
# Prometheus — SLI de disponibilidade
# Proporção de requests 2xx sobre o total (excluindo 4xx que são erro do cliente)

- record: sli:availability:rate5m
  expr: |
    sum(rate(http_requests_total{status=~"2.."}[5m]))
    /
    sum(rate(http_requests_total{status!~"4.."}[5m]))
```

### SLO — Service Level Objective

Meta interna de confiabilidade. Define o threshold do SLI que você se compromete a manter. É a fonte da verdade para decisões operacionais.

```
Exemplos de SLO:

Disponibilidade:
  "99.9% dos requests bem-sucedidos em uma janela de 30 dias"

Latência:
  "99% dos requests atendidos em < 300ms, medido em janela de 30 dias"

Freshness:
  "95% dos dados da dashboard atualizados em < 5 minutos"
```

**Escolhendo o SLO correto:**
- Muito alto (99.99%) → pressão constante no time, zero margem para manutenção
- Muito baixo (95%) → usuários insatisfeitos, sinal que você não se importa com qualidade
- Regra: comece com o que você *já entrega* hoje, meça por 30 dias, depois decida o target

### SLA — Service Level Agreement

Contrato externo com penalidades. É derivado do SLO com margem de segurança — geralmente SLO interno é mais rigoroso que o SLA externo.

```
SLO interno:  99.9% disponibilidade  ← operacional, critério para Error Budget
SLA externo:  99.5% disponibilidade  ← contratual, com créditos se violado

Margem de segurança: 0.4%
→ Se o SLO for violado, você ainda tem folga antes de violar o SLA e gerar multa
```

### Error Budget

O Error Budget é o "quanto você pode falhar" antes de violar o SLO. É a ferramenta central de decisão: se o budget está alto, você pode ser mais agressivo em deploys; se está zerado, você para de fazer mudanças arriscadas.

```
SLO: 99.9% de disponibilidade em 30 dias

30 dias = 43.200 minutos
Error Budget = 0.1% de 43.200 = 43.2 minutos de indisponibilidade permitida

Incidente: 15 minutos de downtime
→ Error Budget restante: 28.2 minutos (34.7% consumido)
```

```yaml
# Prometheus — alerting baseado em Error Budget burn rate
# Queima rápida do budget (> 14x a taxa normal em 1h) = alerta crítico

- alert: ErrorBudgetFastBurn
  expr: |
    (
      1 - sum(rate(http_requests_total{status=~"2.."}[1h]))
          / sum(rate(http_requests_total{status!~"4.."}[1h]))
    ) > (14 * 0.001)  # 14x a taxa normal de erros para SLO de 99.9%
  for: 2m
  labels:
    severity: critical
  annotations:
    summary: "Error budget burning fast — SLO em risco"

- alert: ErrorBudgetSlowBurn
  expr: |
    (
      1 - sum(rate(http_requests_total{status=~"2.."}[6h]))
          / sum(rate(http_requests_total{status!~"4.."}[6h]))
    ) > (6 * 0.001)   # queima moderada — investigar
  for: 15m
  labels:
    severity: warning
```

### Política de Error Budget

```
Error Budget > 50%:
  → Releases normais permitidas
  → Pode fazer experimentos e mudanças de risco moderado

Error Budget 10% - 50%:
  → Apenas features críticas
  → Foco em reliability work
  → Alertas automáticos para o time

Error Budget < 10%:
  → Freeze de features novas
  → Apenas hotfixes e reliability fixes
  → Reunião obrigatória de post-mortem de todos os incidentes recentes

Error Budget esgotado:
  → Stop shipping
  → Time foca 100% em estabilidade até budget se recuperar no próximo período
```

### Blameless Post-mortem

A cultura de SRE coloca "o que falhou no sistema" acima de "quem falhou". Sistemas com blame culture têm escalonamento tardio e aprendizado superficial.

```markdown
## Post-mortem Template

**Impacto:** 15 minutos de indisponibilidade parcial, ~3.000 usuários afetados, 12% do Error Budget consumido.

**Linha do Tempo:**
  14:32 — Deploy da v2.3.1 iniciado
  14:45 — Primeiros alertas de latência elevada
  14:50 — IC (Incident Commander) designado
  14:55 — Rollback iniciado
  14:58 — Sistema estabilizado

**Root Cause:** migration de índice em tabela com 50M rows causou lock table. Query de leitura escalou para timeout.

**Fatores Contribuintes:**
  - Migration não testada com volume de dados de produção
  - Sem alerting de lock wait no PostgreSQL
  - Rollout não verificou latência de banco antes de prosseguir

**Ações Corretivas:**
  [ ] Adicionar alerta de pg_locks no Grafana (responsável: @eng1, prazo: 2026-04-20)
  [ ] Incluir teste de migration com dataset de produção no CI (responsável: @eng2)
  [ ] Atualizar runbook de deploy para verificar métricas de banco pós-deploy
```

## Trade-offs

| Aspecto | Com SLO/Error Budget | Sem SLO/Error Budget |
|---|---|---|
| **Decisões** | Baseadas em dados objetivos | Baseadas em feeling e pressão |
| **Velocidade vs. estabilidade** | Trade-off explícito e negociado | Tensão crônica entre Dev e Ops |
| **Incidentes** | Aprendizado estruturado com post-mortem | Blame, solução ad-hoc, sem melhoria |
| **Produto** | Produto entende impacto de dívida técnica | Produto ignora confiabilidade |

## Quando Usar / Quando Evitar

**Implementar SLO/Error Budget quando:**
- Sistema tem usuários reais com expectativas de disponibilidade
- Time tem capacidade de medir (Prometheus, logs estruturados)
- Existe tensão frequente entre entregas e estabilidade
- Planejando escalar o time — SLOs criam autonomia sem precisar aprovar cada deploy

**Começar simples:**
- 1 SLI de disponibilidade e 1 de latência são suficientes para começar
- Não espere ter a infra perfeita — meça o que você tem agora
- Refine os SLOs após 2-3 ciclos de 30 dias com dados reais

## Conceitos Relacionados

[[observabilidade]] · [[distributed-tracing]] · [[cicd-pipeline]] · [[graceful-degradation]] · [[circuit-breaker]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-14*
