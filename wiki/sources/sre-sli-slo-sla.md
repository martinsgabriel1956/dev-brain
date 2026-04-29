---
type: source
title: "SRE — SLI, SLO, SLA e Error Budget"
aliases: ["sre", "sli", "slo", "sla", "error budget"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sre, observabilidade, confiabilidade, sli, slo, sla, error-budget, post-mortem, prometheus]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/sre-sli-slo-sla.md
source_url: ""
author: ""
date_published: 2026-04-14
date_ingested: 2026-04-22
---

# SRE — SLI, SLO, SLA e Error Budget

## TL;DR

SRE trata confiabilidade como problema de engenharia. O framework: SLI mede, SLO define a meta interna, SLA é o contrato externo com margem de segurança, Error Budget é a "folga" que governa velocidade vs. estabilidade.

## Key Claims

**Claim:** SLI é a métrica concreta que mede qualidade do serviço — sempre um número entre 0 e 1.
**Evidence:** Disponibilidade = `requests_success / requests_total`. Latência = `requests_under_300ms / requests_total`. Freshness = `records_updated_in_last_hour / total_records`. Prometheus: `sum(rate(http_requests_total{status=~"2.."}[5m])) / sum(rate(http_requests_total{status!~"4.."}[5m]))`.
**Confidence:** alta

**Claim:** SLO é a meta interna derivada do SLI — fonte da verdade para decisões operacionais, não o SLA.
**Evidence:** Ex: "99.9% dos requests bem-sucedidos em janela de 30 dias". Regra de escolha: comece com o que você já entrega hoje, meça 30 dias, depois decida o target. Muito alto → pressão constante; muito baixo → usuários insatisfeitos.
**Confidence:** alta

**Claim:** SLA é derivado do SLO com margem de segurança — SLO interno mais rigoroso que SLA externo.
**Evidence:** SLO interno 99.9% + SLA externo 99.5% = margem de 0.4%. Se SLO for violado, ainda há folga antes de gerar penalidade contratual.
**Confidence:** alta

**Claim:** Error Budget governa velocidade vs. estabilidade de forma objetiva.
**Evidence:** SLO 99.9% em 30 dias = 43.2 minutos de downtime permitido. Budget > 50% → releases normais. Budget 10–50% → apenas features críticas. Budget < 10% → freeze. Budget zerado → stop shipping.
**Confidence:** alta

**Claim:** Alerting por burn rate é mais eficaz que alerting por threshold absoluto.
**Evidence:** `FastBurn`: taxa de erro > 14× a normal em 1h → critical. `SlowBurn`: > 6× em 6h → warning. Detecta esgotamento antecipado do budget sem esperar violação do SLO.
**Confidence:** alta

**Claim:** Blameless post-mortem é fundação cultural do SRE — blame culture causa escalonamento tardio e aprendizado superficial.
**Evidence:** Template obrigatório: impacto quantificado (% do Error Budget), linha do tempo, root cause, fatores contribuintes, ações corretivas com responsável e prazo.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/sre]] · [[concepts/sli]] · [[concepts/slo]] · [[concepts/sla]] · [[concepts/error-budget]] · [[concepts/error-budget-policy]] · [[concepts/blameless-post-mortem]] · [[concepts/graceful-degradation]] · [[concepts/circuit-breaker]]

## Open Questions

- SLO para sistemas batch/async — como medir freshness de forma equivalente a disponibilidade?
- Error Budget compartilhado entre múltiplos serviços de um domínio — quem "paga" o incidente?
- Quando introduzir SLOs em sistemas internos (sem SLA contratual) vale o overhead?
