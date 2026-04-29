---
type: concept
title: "Blameless Post-mortem"
aliases: ["post-mortem", "blameless postmortem", "post mortem sem blame"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, cultura, incidentes, aprendizado]
skill: tech-mentor-infra
status: stable
---

# Blameless Post-mortem

Análise de incidente focada em "o que falhou no sistema" — não "quem falhou". Blame culture causa escalonamento tardio (pessoas escondem problemas) e aprendizado superficial (solução é punir, não corrigir o sistema).

## Template

```markdown
**Impacto:** [duração], [usuários afetados], [% do Error Budget consumido]

**Linha do Tempo:**
  HH:MM — evento
  HH:MM — IC designado
  HH:MM — mitigação iniciada
  HH:MM — sistema estabilizado

**Root Cause:** [causa raiz — sistema, não pessoa]

**Fatores Contribuintes:**
  - [o que tornou o sistema suscetível]
  - [o que dificultou a detecção]
  - [o que atrasou a mitigação]

**Ações Corretivas:**
  [ ] Ação concreta (responsável: @eng, prazo: YYYY-MM-DD)
```

## Template Completo

```markdown
# Post-mortem: [Título descritivo]

**Data / Duração / Severidade / Impacto**

## Resumo Executivo
[2-3 linhas do que aconteceu e como foi resolvido]

## Timeline
HH:MM — evento
HH:MM — IC designado
HH:MM — mitigação iniciada
HH:MM — sistema estabilizado

## Causa Raiz
[sistema, não pessoa]

## Fatores Contribuintes
- o que tornou o sistema suscetível
- o que dificultou a detecção
- o que atrasou a mitigação

## O que Funcionou Bem
- [preservar o que não deve ser mudado]

## Ações Corretivas
| Ação | Responsável | Prazo |
```

## Critério de Qualidade

Post-mortem ruim: "o dev X fez deploy sem testar."
Post-mortem bom: "o processo de deploy não exige verificação de métricas de banco pós-rollout e não há alerta de lock wait no PostgreSQL."

A seção "O que Funcionou Bem" é obrigatória — reforça blameless culture e preserva o que não deve ser alterado.

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[sources/sre-error-budget-incidents]]
