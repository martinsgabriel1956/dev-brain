---
type: concept
title: "Teste de Regressão de Prompt"
aliases: ["prompt regression testing", "regressão de prompt"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [evals, testes, prompt-versioning, regressao, ci-cd]
skill: tech-mentor-ai
status: stub
---

# Teste de Regressão de Prompt

Comparar duas versões do mesmo prompt (ex.: 1 vs. 1.2) contra as **mesmas respostas esperadas** de um [[wiki/concepts/golden-dataset]] para saber se a mudança melhorou ou piorou o resultado. Segundo [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] é o que responde à pergunta que o versionamento sozinho não responde ("essa versão é melhor?"); o autor lista ainda testes unitários e de integração e promete um vídeo dedicado.

## Papel no ciclo

Versionar ([[wiki/concepts/versionamento-de-prompt]]) → testar regressão → promover versão ativa → se falhar em produção, [[wiki/concepts/rollback-de-prompt]]. O gate automático em CI/CD está descrito em [[wiki/concepts/prompt-engineering]] e [[wiki/concepts/llm-evals-testing]]; cadência em [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]].

## Pendências

A fonte só descreve; não mostra ferramenta, métrica nem limiar de aprovação. Aguardar fonte dedicada.

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
