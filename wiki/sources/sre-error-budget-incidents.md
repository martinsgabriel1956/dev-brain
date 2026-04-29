---
type: source
title: "SRE — Error Budget, Incident Lifecycle, Post-mortem e Runbook"
aliases: ["sre incidents", "incident lifecycle", "runbook sre"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sre, error-budget, incidentes, post-mortem, runbook, game-day, prometheus, kubernetes]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/sre-error-budget-incidents.md
source_url: ""
author: ""
date_published: 2026-04-17
date_ingested: 2026-04-22
---

# SRE — Error Budget, Incident Lifecycle, Post-mortem e Runbook

## TL;DR

Error Budget é ferramenta de alinhamento produto/engenharia — não métrica de punição. Incidente tem papéis definidos (IC, TL, Comunicador, Escriba) e fluxo previsível. Post-mortem blameless foca no sistema. Runbook efetivo é executável sob stress. Game Day valida tudo isso antes do incidente real.

## Key Claims

**Claim:** Burn rate alerting é superior a threshold absoluto — alerta quando o budget está sendo consumido em ritmo insustentável, não quando já foi violado.
**Evidence:** `burn rate = taxa atual / taxa sustentável`. SLO 99.9% + burn rate 14.4× → budget inteiro consumido em 1h. FastBurn (14.4× por 5min) = critical page. SlowBurn (6× por 30min) = warning. Prometheus YAML fornecido.
**Confidence:** alta

**Claim:** Incidente tem 4 papéis distintos que não devem se misturar — IC coordena, TL investiga, Comunicador atualiza, Escriba documenta.
**Evidence:** IC não deve investigar tecnicamente (perde visão de coordenação). TL não deve coordenar (perde foco na causa raiz). Separação de papéis reduz tempo de resolução.
**Confidence:** alta

**Claim:** Severidade define tempo de resposta e escalonamento — SEV-1 = war room imediato, SEV-4 = próximo sprint.
**Evidence:** Tabela: SEV-1 (sistema indisponível, perda financeira ativa) → resposta imediata + C-level. SEV-2 (feature crítica degradada) → < 15min. SEV-3 (bug com workaround) → < 2h. SEV-4 (inconveniência) → sprint.
**Confidence:** alta

**Claim:** Post-mortem blameless requer seção "O que Funcionou Bem" — não apenas o que falhou.
**Evidence:** Template completo inclui: resumo executivo, timeline, causa raiz, fatores contribuintes, **o que funcionou bem**, ações corretivas com responsável e prazo. Seção positiva reforça blameless culture e preserva o que não deve ser mudado.
**Confidence:** alta

**Claim:** Runbook efetivo é executável sob stress — diagnóstico rápido (< 5min), árvore de decisão, comandos copiáveis.
**Evidence:** Estrutura: quando usar → diagnóstico rápido com comandos kubectl → árvore de causa → ações específicas por causa → critério de escalona para SEV-1.
**Confidence:** alta

**Claim:** Game Day valida runbooks e SLOs antes do incidente real — experimento planejado de falha em staging.
**Evidence:** Estrutura: objetivo mensurável → escopo (staging + tráfego sintético) → experimento (ex: kill 50% dos pods) → observação de métricas → retrospectiva. Resultado: runbooks atualizados, gaps descobertos sem impacto em produção.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/error-budget]] · [[concepts/error-budget-policy]] · [[concepts/blameless-post-mortem]] · [[concepts/incident-lifecycle]] · [[concepts/incident-severity]] · [[concepts/incident-roles]] · [[concepts/runbook]] · [[concepts/game-day]] · [[concepts/sre]]

## Open Questions

- Como coordenar Game Day em sistemas multi-squad sem criar dependências de agenda?
- Runbook versionado junto com o código (mesmo repo) vs wiki — qual o trade-off de atualização?
- SEV-1 com múltiplos sistemas afetados — quem é o IC quando há dois on-calls simultâneos?
