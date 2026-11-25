---
type: concept
title: "Engenharia de Features"
aliases: ["feature engineering", "features", "características do modelo", "extração de features"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [ia, machine-learning, features, representation-learning, fundamentos]
skill: tech-mentor-ai
status: stub
---

## Definição

Etapa em que um humano decide **quais características (features)** dos dados brutos o modelo vai receber. No reconhecimento de rosto, por exemplo: distância entre os olhos, formato do nariz, contorno facial. Os **pesos** de cada feature, por outro lado, o próprio treino aprende ([[wiki/concepts/modelo-de-machine-learning]]). [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]

## Por que importa na evolução da IA

É a limitação do [[wiki/concepts/machine-learning]] clássico apontada em [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: "Humanos precisavam dizer quais características importar [...] o humano escolhia as features". O [[wiki/concepts/deep-learning]] contorna isso com *representation learning*: as camadas de uma [[wiki/concepts/rede-neural-artificial]] aprendem as próprias features (bordas → partes → rosto). [external] Bengio, Courville e Vincent (2013), https://arxiv.org/abs/1206.5538

## Ressalva

Na fala da aula, o humano também "coloca qual parâmetro pesa mais". Isso confunde features com pesos: escolher features é trabalho humano, mas ajustar pesos é o que o treino faz desde a regressão linear. [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]

## Key Sources

- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: o limite do ML é o humano escolher as features
