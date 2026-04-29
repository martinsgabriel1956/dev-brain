---
type: source
title: "Avaliação Sistemática (Evals)"
aliases: ["evals", "avaliacao llm", "llm-as-judge", "ragas", "deepeval", "promptfoo"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/evals-sistematicas.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [evals, llm-as-judge, golden-dataset, ragas, deepeval, g-eval, promptfoo, evalite, ci-evals, prompt-versioning]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Evals são testes para sistemas LLM: offline (golden dataset + métricas automáticas), online (sampling de produção + LLM-as-judge), CI (bloqueantes por PR). LLM-as-judge escala onde humano não consegue — mas precisa calibração. RAGAS para RAG (faithfulness, context_recall). promptfoo para comparar variantes de prompt em CI/CD.

## Key Claims

**Claim:** Pipeline de evals em 3 níveis é o padrão de produção.
**Evidence:** Offline: golden dataset com casos de teste fixos, roda antes de deploy. Online: sampling de 1–5% do tráfego real, LLM-as-judge assíncrono. CI: subset de evals críticos que bloqueia PR se regression detectada.
**Confidence:** alta

**Claim:** LLM-as-Judge tem biases conhecidos que precisam de calibração explícita.
**Evidence:** Preferência por respostas longas (penalize verbosidade no prompt do juiz), posição bias (rodar A/B com ordem invertida e fazer média), auto-preferência (usar provider diferente como juiz). Calibração: 5–10% com humano, Spearman > 0.7 é aceitável.
**Confidence:** alta

**Claim:** RAGAS mede as métricas corretas para RAG: faithfulness e context_recall.
**Evidence:** Faithfulness: resposta está ancorada nos documentos recuperados? Context_recall: documentos relevantes foram recuperados? Essas métricas não fazem sentido fora de RAG — para chat geral, usar relevance + coherence.
**Confidence:** alta

**Claim:** promptfoo é a melhor ferramenta para comparar variantes de prompt em CI.
**Evidence:** YAML-driven, gera matrix de modelos × prompts × test cases, output side-by-side, integra com GitHub Actions. Permite detectar regressão antes de deploy.
**Confidence:** alta

**Claim:** Prompt Versioning como código é obrigatório para rastrear regressões.
**Evidence:** Prompt como arquivo versionado no Git + eval score associado ao commit. Mudança de prompt = novo commit = rodada de evals. Sem versionamento, impossível saber qual prompt causou regressão.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/evals-llm]]
- [[concepts/llm-as-judge]]
- [[concepts/golden-dataset]]
- [[concepts/ragas]]
- [[entities/promptfoo]]
- [[entities/deepeval]]

## Open Questions

- Como construir golden dataset quando não há histórico de uso? (cold start problem)
- Qual o número mínimo de test cases no golden dataset para detectar regressão com 95% de confiança?
