---
type: concept
title: "Deep Learning"
aliases: ["aprendizado profundo", "redes profundas"]
date_created: 2026-10-14
date_updated: 2026-11-24
source_count: 3
tags: [ia, deep-learning, redes-neurais, fundamentos]
skill: tech-mentor-ai
status: draft
---

## Definição

[[wiki/concepts/rede-neural-artificial|Redes neurais]] com **muitas camadas ocultas** ("deep" = profundidade). Cada camada aprende um nível de abstração: em rostos, bordas e contrastes → olhos, nariz, boca → rosto completo. Ninguém programa isso; emerge do treino, e cada camada é uma "caixa-preta". [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Habilitadores

[[wiki/concepts/backpropagation]] + camadas ocultas + **grandes bases de dados + GPUs + novas técnicas de treino**. Escala: de centenas de pesos para milhões ou bilhões de parâmetros. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Marco

**2012**: a AlexNet venceu a ImageNet por ampla margem ([[wiki/entities/alexnet]]); dali em diante o deep learning domina aplicações comerciais e pesquisa (visão, voz, tradução, fraude, diagnóstico, carros autônomos, recomendação). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Limite que levou ao próximo passo

Ainda havia dificuldade com **linguagem natural** (contexto longo), resolvida pelo [[wiki/concepts/transformer-architecture]]. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## FrontPUSH: recurso como barreira

[[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]] define "'Deep' = múltiplas camadas neurais" e põe a barreira em "recurso": Big Data, arquiteturas e modelos, e [[wiki/concepts/gpu|GPUs]]. Slide: "Deep Learning consome recurso, agora o hardware consegue fornecer esse recurso". Coincide com os habilitadores acima. Ele não cita backpropagation nem AlexNet.

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: camadas e a tríade GPUs, Big Data, arquiteturas
- [[wiki/sources/frontpush-ia-o-que-sao-as-llms]]: FrontPUSH, módulo de IA, parte 2: recap da barreira de recurso; LLM como "modelos gigantescos de Deep Learning"
