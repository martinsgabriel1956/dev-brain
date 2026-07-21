---
type: entity
title: "Moonshot AI"
aliases: ["Moonshot", "Kimi"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [moonshot, kimi, china, llm, open-source, organização]
skill: tech-mentor-ai
status: stub
---

# Moonshot AI

Lab de IA chinês, criador da família de modelos **Kimi**. Autor do modelo já citado nesta wiki [[wiki/concepts/modelo-frontier|Kimi K2.6]] (referenciado como open-weight competitivo com frontier fechados por fração do preço) e, mais recentemente, do **Kimi K3**.

## Kimi K3 (lançamento parcial)

Divulgado em [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]: modelo de **2,8 trilhões de parâmetros**, arquitetura [[wiki/concepts/mixture-of-experts|MoE]] com **896 experts, dos quais só 16 ativados por inferência**. Lançamento parcial — API oficial e benchmarks já disponíveis, pesos ainda não públicos no momento da fonte. Divulgou um novo método de inferência com até 75% de economia de [[wiki/concepts/kv-cache|KV Cache]], com perda de precisão considerada irrelevante nos benchmarks.

## Estratégia de abertura como diferencial de mercado

Diferente de labs fechados (OpenAI, Anthropic), a Moonshot publica não só o modelo mas o método de servi-lo em inferência — qualquer provedor com hardware suficiente pode replicar a "receita" e servir o modelo, descentralizando o conhecimento de inferência que hoje é concentrado em poucas big techs (Microsoft, AWS). Isso é discutido como parte do contexto mais amplo de [[wiki/concepts/export-controls-chips-ia|sanções de exportação de chips]] pressionando inovação arquitetural em labs sem acesso irrestrito a hardware de ponta.

## Key Sources

- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
