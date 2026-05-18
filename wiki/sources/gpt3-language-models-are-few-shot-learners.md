---
type: source
title: "Language Models are Few-Shot Learners (GPT-3)"
aliases: ["GPT-3 paper", "Brown et al. 2020"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/gpt3-language-models-are-few-shot-learners.md"
source_url: "https://arxiv.org/abs/2005.14165"
author: "Tom B. Brown et al. (OpenAI)"
date_published: 2020-05-28
date_ingested: 2026-05-17
source_count: 0
tags: [llm, gpt-3, few-shot-learning, in-context-learning, scaling-laws, openai, transformer]
skill: tech-mentor-ai
status: stable
---

# Language Models are Few-Shot Learners (GPT-3)

## TL;DR

GPT-3 (175B parâmetros) demonstra que escalar modelos de linguagem melhora drasticamente a capacidade de aprender tarefas a partir de poucos exemplos no contexto — sem atualização de pesos. O paper cunha e formaliza o conceito de [[in-context-learning]] e estabelece a distinção zero-shot / one-shot / few-shot como protocolo de avaliação padrão para LLMs.

## Argumento Central

Fine-tuning exige datasets rotulados por tarefa e cria risco de overfitting a artefatos de distribuição. Humanos aprendem de poucos exemplos. Modelos maiores são meta-aprendizes melhores: eles absorvem o padrão da tarefa a partir de exemplos no prompt (contexto), sem gradient descent — isso é [[in-context-learning]].

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Escalar parâmetros melhora few-shot mais do que zero-shot | Performance few-shot cresce mais steeply que zero-shot em todos os 42 benchmarks | Alta |
| GPT-3 few-shot rivaliza com fine-tuned SOTA em várias tarefas | TriviaQA: 71.2 vs RAG 68.0; PIQA: 82.8 vs SOTA 79.4 | Alta |
| Modelos treinados na internet herdam vieses na escala da internet | Análise de viés de gênero, raça e religião conduzida pelos autores | Alta |
| Data contamination tem efeito mínimo na maioria dos benchmarks | Ferramentas de deduplicação e análise de overlap construídas no paper | Média |

## Conceitos Introduzidos / Formalizados

- [[in-context-learning]] — aprender tarefa via exemplos no prompt, sem atualizar pesos
- [[few-shot-learning]] — variante de ICL com 10–100 exemplos demonstrativos
- [[scaling-laws]] — performance segue power law em função de parâmetros, dados e compute
- [[data-contamination]] — sobreposição entre dados de treino e benchmarks de teste

## Entidades

- [[wiki/entities/openai]] — organização responsável pelo GPT-3

## Conceitos Relacionados

- [[foundation-model]] — GPT-3 é um dos primeiros exemplos do termo
- [[autoregressive-language-model]] — arquitetura base do GPT-3
- [[fine-tuning]] — abordagem que GPT-3 busca substituir / reduzir dependência

## Questões em Aberto

1. In-context learning é aprendizado real ou recuperação sofisticada de padrões do pré-treino?
2. Até onde as scaling laws se sustentam? (GPT-4, Claude 3, Gemini sugerem que sim, mas com diminishing returns)
3. Como medir data contamination de forma robusta em modelos que não publicam seus dados de treino?

## Citações Relevantes

> "Humans can generally perform a new language task from only a few examples or from simple instructions – something which current NLP systems still largely struggle to do."

> "Internet-trained models have internet-scale biases."

## Referências Citadas no Paper

- GPT-2 (Radford et al., 2019) — arquitetura base
- Scaling Laws for Neural Language Models (Kaplan et al., 2020) — fundamento teórico
- Sparse Transformer (Child et al., 2019) — padrões de atenção esparsa
- RAG (Lewis et al., 2020) — baseline de QA open-domain
- T5 (Raffel et al., 2019) — baseline de fine-tuning
