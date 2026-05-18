---
type: concept
title: "Data Contamination"
aliases: ["contaminação de dados", "benchmark contamination", "test leakage"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, avaliação, benchmarks, treinamento, data-contamination]
skill: tech-mentor-ai
status: stable
---

# Data Contamination

## Definição

Sobreposição entre os dados de treinamento de um modelo e os conjuntos de teste de benchmarks usados para avaliá-lo. Quando ocorre, a performance reportada pode estar **inflada** — o modelo pode ter memorizado exemplos de teste durante o pré-treinamento.

Problema crescente com modelos treinados em web-scale data (Common Crawl, etc.), pois benchmarks públicos frequentemente aparecem na web.

Formalizado como problema de pesquisa em [[wiki/sources/gpt3-language-models-are-few-shot-learners]].

## Por Que é Difícil Detectar

1. Datasets de treinamento têm trilhões de tokens — inspecionar manualmente é inviável.
2. Contaminação pode ser parcial (alguns exemplos do teste, não todos).
3. Reformulações e paráfrases podem não ser detectadas por matching exato.

## Abordagem do GPT-3

O paper GPT-3 construiu ferramentas sistemáticas para medir contaminação:
- Deduplicação fuzzy em nível de documento durante a construção do dataset.
- Pós-análise de overlap entre dados de treino e benchmarks.
- Resultados marcados com `*` quando contaminação potencial foi detectada.
- Benchmarks removidos do relatório quando contaminação foi severa.

Conclusão: contaminação teve efeito mínimo na maioria dos benchmarks, mas alguns foram comprometidos.

## Implicações para Avaliação de LLMs

- Benchmarks públicos se tornam **obsoletos** mais rapidamente — modelos treinados após a publicação do benchmark podem ter visto os dados.
- Há pressão crescente por benchmarks **dinâmicos** ou mantidos privados.
- Modelos que não publicam dados de treino tornam a detecção de contaminação impossível para externos.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
