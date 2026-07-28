---
type: concept
title: "Debt Ratio / SQALE"
aliases: ["technical debt ratio", "SQALE method", "razão de dívida técnica"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [tech-debt, sqale, metricas, sonarqube, medicao]
skill: tech-mentor-leadership
status: stub
---

# Debt Ratio / SQALE

## TL;DR

Fórmula para quantificar dívida técnica como percentual: `Technical Debt Ratio = Remediation Cost / Development Cost`. Base do método **SQALE** (Software Quality Assessment based on Lifecycle Expectations), usado por ferramentas como SonarQube para reportar dívida em tempo (dias/horas) e como percentual do custo total de desenvolvimento.

## A Fórmula

```
Debt Ratio = Custo de Remediação / Custo de Desenvolvimento
```

Exemplo: se corrigir a dívida custaria $100.000 num sistema que custou $500.000 para construir, o debt ratio é 20%.

## Faixas de Risco

| Debt Ratio | Interpretação |
|---|---|
| < 5% | Saudável — manter |
| 5–10% | Ainda ok, mas monitorar |
| 10–20% | Risco moderado — começa a prejudicar velocidade de entrega |
| > 20% | Crítico — dificuldade de entregar qualquer coisa sem atrito constante |

## Relação com Outros Frameworks

O debt ratio dá um número agregado (útil para reporting a stakeholders — ver [[wiki/concepts/tech-debt-como-ferramenta]]), mas não diz **onde** atacar primeiro. Para priorização dentro desse percentual, usar [[wiki/concepts/hotspot-analysis]] (complexidade ciclomática × frequência de mudança) ou o [[wiki/concepts/paid-framework]].

## Key Sources

- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]]
