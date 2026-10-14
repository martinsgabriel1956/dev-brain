---
type: concept
title: "LLM (Large Language Model)"
aliases: ["LLM", "large language model", "modelo de linguagem grande"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [ia, llm, llm-fundamentals, transformers, probabilistico]
skill: tech-mentor-ai
status: draft
---

## Definição

[[wiki/concepts/transformer-architecture|Transformer]] treinado em volume gigantesco de texto (livros, artigos, sites, documentação) com centenas de bilhões de parâmetros. *Language* = linguagem natural; *large* = dados e parâmetros. É um [[wiki/concepts/deep-learning|modelo de deep learning]] — **não substitui** ML, redes neurais ou deep learning; é a combinação deles em escala. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Como gera

Prevê o próximo [[wiki/concepts/tokenizacao|token]] mais provável dado o contexto, anexa à entrada e repete ("autocomplete com lasers"). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]] [external] A fonte diz que a rede "nunca planeja"; pesquisa de interpretabilidade da Anthropic mostra planejamento antecipado interno (https://www.anthropic.com/research/tracing-thoughts-language-model). Descrição correta do laço, simplificação do mecanismo.

## Probabilístico

A mesma pergunta pode gerar respostas diferentes; sem garantia de correção, pois não consulta base de fatos e prevê padrões ([[wiki/concepts/determinismo-vs-probabilismo-em-ia]], [[wiki/concepts/alucinacao-llm]]). [skill: tech-mentor-ai] a aleatoriedade é ajustável por temperatura ([[wiki/concepts/hyperparameters-llm]]). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Medidas práticas

Janela de contexto e custo em tokens ([[wiki/concepts/janela-de-contexto]], [[wiki/concepts/token-tax-multilingual]]). Acima do LLM, [[wiki/concepts/agente-ia|agentes]] adicionam ferramentas e ações.

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
