---
type: concept
title: "Incident Severity (SEV)"
aliases: ["severidade de incidente", "sev1", "sev2", "sev3", "sev4", "incident severity levels"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sre, incidentes, operações, on-call]
skill: tech-mentor-infra
status: stable
---

# Incident Severity (SEV)

Classificação de incidentes por impacto — determina velocidade de resposta e escalonamento. Definir severidade imediatamente após o acknowledge evita both sub-reação (SEV-1 tratado como SEV-3) e over-reação (SEV-4 gerando war room).

## Níveis

| Nível | Critério | Tempo de Resposta | Escalonamento |
|---|---|---|---|
| **SEV-1** | Sistema completamente indisponível ou perda financeira ativa | Imediato | War room, C-level notificado |
| **SEV-2** | Feature crítica degradada, impacto a % significativa de usuários | < 15min | On-call escalado |
| **SEV-3** | Bug com workaround disponível, impacto limitado | < 2h | Horário comercial |
| **SEV-4** | Inconveniência, sem impacto a usuário | Próximo sprint | Nenhum |

## Critério de Upgrade

Incidente pode ser promovido de severidade durante a resposta. Se SEV-3 não resolve em 2h ou impacto se expande → promove para SEV-2 e escala.

## Relação com Error Budget

Cada incidente consome [[concepts/error-budget]] proporcional à duração × impacto. SEV-1 de 1h pode esgotar o budget mensal inteiro.

## Key Sources

- [[sources/sre-error-budget-incidents]]
