---
type: concept
title: "SRE — Site Reliability Engineering"
aliases: ["site reliability engineering", "sre"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 3
tags: [sre, confiabilidade, operações, devops]
skill: tech-mentor-infra
status: stable
---

# SRE — Site Reliability Engineering

Disciplina que trata confiabilidade de sistemas como problema de engenharia. Framework central: definir o que significa "suficientemente confiável" ([[concepts/slo]]), medir se você está lá ([[concepts/sli]]), e usar a folga disponível ([[concepts/error-budget]]) para tomar decisões de velocidade vs. estabilidade.

## Cinco Pilares do "Sucesso" na Visão de um SRE

Framing didático alternativo (não conflitante) ao framework SLI/SLO/Error Budget acima: sucesso na visão de um SRE cobre cinco frentes interligadas — [[wiki/concepts/planejamento-de-capacidade]] (alimentado pelos dados da observabilidade), [[wiki/concepts/observabilidade]] (visão fim-a-fim do fluxo, não só métricas isoladas), [[wiki/concepts/finops|otimização de custo]], Release Engineering ([[wiki/concepts/deploy-strategies]] — a disciplina de entrega de novas versões minimizando impacto) e segurança. Confiabilidade aparece como o guarda-chuva que amarra tudo isso: consistência, durabilidade, [[wiki/concepts/tolerancia-a-falha|tolerância a falhas]], previsibilidade e disponibilidade de recursos (não só uptime).

## Por que importa

Sem esse framework, a discussão de confiabilidade fica na base de "o sistema tá caindo?" — reativa, sem critério de decisão, com tensão crônica entre Dev e Ops.

## Componentes

- [[concepts/sli]] — métrica concreta (o que medir)
- [[concepts/slo]] — meta interna (qual o target)
- [[concepts/sla]] — contrato externo (com penalidade)
- [[concepts/error-budget]] — folga operacional (governa velocidade vs. estabilidade)
- [[concepts/error-budget-policy]] — regras de decisão por nível de budget
- [[concepts/blameless-post-mortem]] — cultura de aprendizado sem blame

## RTO/RPO Como Indicadores do Pior Caso de Confiabilidade

O guarda-chuva de confiabilidade (consistência, durabilidade, tolerância a falhas, previsibilidade, disponibilidade de recursos) cobre operação contínua via SLI/SLO/SLA. Para o cenário de desastre — sistema inteiro caiu, dado precisa ser restaurado de backup —, os indicadores formais são [[wiki/concepts/rto]] (tempo até restaurar) e [[wiki/concepts/rpo]] (dado tolerável de perda), e ambos devem ser definidos a partir da tolerância real do negócio antes da arquitetura, não depois. Ver [[wiki/sources/rto-rpo-recovery-time-point-objective]].

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] — os cinco pilares de sucesso (capacidade, observabilidade, custo, release engineering, segurança) e confiabilidade como guarda-chuva
- [[wiki/sources/rto-rpo-recovery-time-point-objective]] — RTO/RPO como indicadores de confiabilidade no cenário de desastre, definidos a partir da tolerância do negócio
