---
type: concept
title: "Hotspot Analysis (Dívida Técnica)"
aliases: ["análise de hotspots", "code churn", "complexidade ciclomática", "code hotspot"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [tech-debt, metricas, complexidade-ciclomatica, code-churn, sonarqube, codescene]
skill: tech-mentor-leadership
status: stub
---

# Hotspot Analysis

## TL;DR

Técnica de priorização de dívida técnica que cruza duas dimensões: **complexidade** do código e **frequência de mudança** (code churn). Código complexo que quase nunca muda não é prioridade; código simples que muda toda semana também não é o problema — o hotspot real é a interseção das duas coisas.

```
Débito mais urgente = código mais complexo E que muda com mais frequência
```

## As Duas Métricas

- **Complexidade ciclomática** — quantidade de branches de decisão (`if`/`else`, loops, `switch`) num trecho de código. Mais branches = mais caminhos de execução possíveis = mais difícil de entender, testar e manter com segurança.
- **Code churn** — com que frequência um arquivo é modificado. Pode ser medido diretamente no histórico do git: `git log --since="90 days ago" --format="" --name-only | sort | uniq -c | sort -rn`.

## Por Que a Interseção Importa

Um arquivo complexo que ninguém toca há um ano não está causando dor no dia a dia — baixo risco prático, mesmo com métrica de qualidade ruim. Um arquivo simples que muda toda semana também não é hotspot, porque mudar nele é barato. O hotspot é o arquivo complexo **e** que muda com frequência: cada mudança nele custa caro (difícil entender o impacto) e é frequente (o custo se repete). Essa é a mesma lógica por trás da regra de Pareto aplicada a dívida técnica: **80% da dor geralmente vem de 20% dos arquivos** — os hotspots.

## Sinais Complementares

- **Lead time crescente** — se o tempo entre commit e produção cresce ao longo do tempo para o mesmo tipo de feature, é sinal indireto de dívida técnica entupindo o pipeline (ver [[wiki/concepts/dora-metrics]]).
- **DORA como proxy de débito** — deployment frequency baixa, change failure rate alto ou MTTR alto também apontam para dívida técnica não medida diretamente por complexidade/churn.

## Ferramentas

CodeScene (hotspots + comportamento de time), SonarQube (métricas de qualidade, dívida em dias/horas), `lizard` (CLI de complexidade ciclomática).

## Relacionado

[[wiki/concepts/debt-ratio-sqale]] — dá o número agregado; hotspot analysis diz *onde* dentro desse número atacar primeiro. [[wiki/concepts/paid-framework]] — heurística alternativa mais qualitativa para o mesmo objetivo de priorização.

## Key Sources

- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]]
