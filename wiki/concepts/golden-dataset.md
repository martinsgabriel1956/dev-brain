---
type: concept
title: "Golden Dataset"
aliases: ["golden test", "dataset dourado", "golden set"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [evals, testes, llm, golden-dataset]
skill: tech-mentor-ai
status: stub
---

# Golden Dataset

Base curada de entradas com as **respostas esperadas** do LLM, usada como régua fixa para comparar versões de prompt. Na fonte ([[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]) o autor a chama de "golden test"/"golden dataset" quase como sinônimos e adia a demonstração para outro vídeo.

## Uso

Rodar versão 1 e versão 1.2 do mesmo prompt sobre as mesmas respostas esperadas e ver se a mudança foi melhor ou pior "para os nossos dados" ([[wiki/concepts/teste-de-regressao-de-prompt]]).

## Complemento da skill `[skill: tech-mentor-ai]`

Boas práticas de referência: conjunto de pares (input, esperado) versionado junto aos prompts; adicionar um caso sempre que um bug de LLM chegar a produção; avaliar toda mudança de prompt/modelo antes de ir a produção. Ver [[wiki/concepts/llm-evals-testing]] e [[wiki/concepts/evals-llm]].

## Pendências

Fonte não explica como as respostas esperadas são comparadas (igualdade exata, LLM-as-judge, métricas). Precisa de fonte dedicada.

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
