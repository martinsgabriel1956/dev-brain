---
type: concept
title: "Backpropagation"
aliases: ["retropropagação do erro", "back propagation"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [ia, redes-neurais, treinamento, otimizacao]
skill: tech-mentor-ai
status: stub
---

## Definição

Algoritmo que calcula **quanto cada neurônio de cada camada contribuiu para o erro final** e ajusta todos os pesos de forma coordenada para reduzi-lo. Popularizado em **1986** e peça-chave para treinar redes com camadas ocultas ([[wiki/concepts/deep-learning]]). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Ciclo descrito no vídeo

palpite → erro contra o gabarito ([[wiki/concepts/aprendizado-supervisionado]]) → ajuste dos pesos (não mais aleatório) → novo palpite; repetir até o erro cair ao nível desejado. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

[external] Rumelhart, Hinton & Williams (1986), https://www.nature.com/articles/323533a0. O ajuste em si é feito por descida de gradiente (não detalhada na fonte).

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
