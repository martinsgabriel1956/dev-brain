---
type: concept
title: "LLM (Large Language Model)"
aliases: ["LLM", "large language model", "modelo de linguagem grande"]
date_created: 2026-10-14
date_updated: 2026-11-24
source_count: 3
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

## FrontPUSH: "IA é probabilidade"

Em [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]], [[wiki/entities/nasser|Násser]] resume o LLM como "calculando a probabilidade da próxima palavra" a cada iteração, com muito poder computacional e dados da internet, e conclui que ele "não pensa, nem sente" e "não entende como um ser humano". O laço de geração está certo; sobre "não entende", ver a ressalva de interpretabilidade em "Como gera". A aula coloca o LLM como "um tipo de Deep Learning" e deixa o detalhe para a parte 2.

## FrontPUSH: "cuspir texto", o tradutor e os quatro pilares

[[wiki/sources/frontpush-ia-o-que-sao-as-llms]] usa a mesma definição ("modelos gigantescos de Deep Learning baseados em Transformers treinados em enormes volumes de texto") e resume: "ela prevê o próximo token. Só isso. Mas em escala gigantesca. Feito pra 'cuspir' texto". Os quatro pilares do slide são tokens, contexto, attention e parâmetros. A metáfora do "tradutor" entre o deep learning ("o árabe") e as pessoas vale para a interface, não para a arquitetura: o LLM *é* o deep learning, e não uma camada sobre outro modelo. A aula também afirma que o modelo ajusta pesos quando o usuário aponta um erro, o que está errado ([[wiki/concepts/bajulacao-llm]]).

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: próxima palavra e "não pensa, nem sente"
- [[wiki/sources/frontpush-ia-o-que-sao-as-llms]]: FrontPUSH, módulo de IA, parte 2: definição, fluxo do prompt à resposta e quatro pilares
