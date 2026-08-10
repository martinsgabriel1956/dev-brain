---
type: concept
title: "Paradoxo da Aceleração"
aliases: ["acceleration paradox", "paradoxo da aceleracao", "velocidade individual atrito sistemico"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [ia-produtividade, engineering-metrics, code-review, faros-ai, gargalo]
skill: tech-mentor-leadership
status: draft
---

# Paradoxo da Aceleração

**TL;DR:** Termo da [[wiki/entities/faros-ai]] para o descompasso entre **velocidade individual** (que sobe muito com IA) e **throughput do sistema** (que quase não sobe, ou piora). A IA acelera a etapa errada — a escrita — enquanto o gargalo real migra para a revisão, que não escala junto.

## O mecanismo

```
IA acelera a escrita de código
    ↓
Devs fazem 21% mais tarefas, ~2x mais PRs (individualmente)
    ↓
Mas a revisão exige julgamento humano e não escala igual
    ↓
Tempo de code review sobe 91% → fila de PRs
    ↓
Ganho individual não vira ganho de time (empresa: só +10%)
```

Antes da IA havia equilíbrio: um dev escrevia, outro revisava, mergeava — ritmos compatíveis. A IA rompe esse equilíbrio acelerando só a produção. O gargalo deixa de ser a escrita e passa a ser a **revisão** — uma tarefa que exige atenção, contexto do sistema e julgamento, que a IA não resolve e ainda **alimenta com mais código para revisar**.

## Por que a revisão não escala

Código gerado por IA **não é mais simples de revisar** — às vezes é mais difícil: é tecnicamente válido (segue padrões) mas pode ser arquiteturalmente errado, passar nos testes e quebrar a lógica de negócio. Ver [[wiki/concepts/gaming-de-testes-por-ia]] e [[wiki/concepts/ia-como-amplificador]].

## Os números (Faros AI)

| Métrica | Valor |
|---|---|
| Adoção de IA entre devs | 93% |
| Ganho de produtividade da empresa | 10% |
| Tarefas por dev | +21% |
| PRs mergeados por dev | ~2x |
| Tempo de code review | +91% |
| Devs que já bateram limites de uso | 30% |

> Números da fonte primária Faros AI reportados via transcrição — ver ressalva em [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]].

## Relação com outros paradoxos

Estrutura análoga ao [[wiki/concepts/roi-de-ia]] (ganho individual que não sobe para a empresa) e ao [[wiki/concepts/paradoxo-de-jevons]] (mais eficiência → mais consumo). A raiz comum é medir a etapa errada — ver [[wiki/concepts/output-vs-outcome]] e [[wiki/concepts/goodharts-law]].

## Conceitos Relacionados

[[wiki/concepts/ia-como-amplificador]] · [[wiki/concepts/output-vs-outcome]] · [[wiki/concepts/code-review]] · [[wiki/concepts/roi-de-ia]] · [[wiki/concepts/dora-metrics]]

## Key Sources

- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]]
