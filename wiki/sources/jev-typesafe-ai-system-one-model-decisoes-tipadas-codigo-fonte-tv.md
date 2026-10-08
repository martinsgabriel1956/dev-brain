---
type: source
title: "Jev (TypeSafe AI): o modelo System One que decide em vez de escrever texto (Código Fonte TV)"
aliases: ["jev typesafe", "system one model"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV (inferido)"
date_published: ""
date_ingested: 2026-10-08
source_count: 0
tags: [ia, system-one-model, decisoes-tipadas, classificacao, confianca, rlcd]
skill: tech-mentor-ai
status: draft
---

# Jev (TypeSafe AI): System One model

## TL;DR

A [[wiki/entities/typesafe-ai]] lançou o [[wiki/entities/jev]], o primeiro [[wiki/concepts/system-one-model]]: em vez de gerar texto token a token e depois fazer parse, recebe um estado + [[wiki/concepts/perguntas-tipadas-choice-score-noul]] e devolve decisões já tipadas, com probabilidade e confiança, treinado via [[wiki/concepts/rlcd]]. Regra prática: [[wiki/concepts/jev-para-ramificar-llm-para-ler]]. Ressalva-chave: [[wiki/concepts/zero-erro-de-schema-nao-e-correcao-semantica]].

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Decisões simples não precisam de LLM gerativo + parse + validação | Argumento da TypeSafe AI | Média |
| RLCD treina decisão + confiança calibrada (vs. RLHF, que otimiza respostas "boas" para humanos) | Descrição da empresa | Média (vendor); `[external]` corrobora o desenho |
| Vercel: até 18x mais rápido e mais preciso em comandos de segurança | Reportagem citada, não identificada | Baixa-média |
| MotherDuck: classificação 50x mais rápida a ~1% do custo (100 mil linhas em 40 s) | Citado em vídeo; unidades de custo ambíguas | Baixa-média |
| Jev é foundation model, não wrapper | Afirmação do apresentador | Média |
| "Não alucina" porque expõe confiança | Interpretação popular; o vídeo a qualifica | Baixa: ver [[wiki/concepts/zero-erro-de-schema-nao-e-correcao-semantica]] |

## Entidades

[[wiki/entities/typesafe-ai]], [[wiki/entities/jev]], [[wiki/entities/diogo-almeida]], [[wiki/entities/motherduck]], [[wiki/entities/vercel]], [[wiki/entities/openai]], [[wiki/entities/hostinger]] (patrocínio, Dokploy), [[wiki/entities/codigo-fonte-tv]].

## Conceitos

[[wiki/concepts/system-one-model]], [[wiki/concepts/rlcd]], [[wiki/concepts/perguntas-tipadas-choice-score-noul]], [[wiki/concepts/jev-para-ramificar-llm-para-ler]], [[wiki/concepts/zero-erro-de-schema-nao-e-correcao-semantica]], [[wiki/concepts/saida-estruturada-llm]], [[wiki/concepts/alucinacao-llm]], [[wiki/concepts/cascade-pattern-llm]], [[wiki/concepts/tool-call]], [[wiki/concepts/agente-ia]].

## Perguntas em aberto

- A primitiva "no" é grafada "noul" em fonte externa ([external] https://nexos.ai/blog/what-is-jev/); no vídeo, ASR ambíguo.
- Números de Vercel/MotherDuck não verificados contra fonte primária; "Luna 5.6" é ASR ambíguo.
- Calibração (confiança alta = acurácia alta) é alegação do fornecedor; sem benchmark independente.
- Disponibilidade: inscrições fechadas no momento do vídeo; fontes externas divergem (early access vs. coming soon).
- O vídeo patrocinado ([[wiki/entities/hostinger]]) pode ter viés de entusiasmo.

## Citações

> "Se a saída da etapa for um valor que o seu código vai usar para ramificar, considere o Jev. Se for um texto que uma pessoa vai ler, use um LLM."
> "State entra e decisões tipadas saem."
