---
type: concept
title: "Rede Neural Artificial"
aliases: ["rede neural", "neural network", "neurônio artificial", "perceptron"]
date_created: 2026-10-14
date_updated: 2026-11-24
source_count: 2
tags: [ia, redes-neurais, deep-learning, fundamentos]
skill: tech-mentor-ai
status: draft
---

## Definição

Estrutura de **neurônios artificiais** — unidades que recebem entradas, ponderam cada uma por um **peso**, combinam e emitem uma saída que alimenta outros neurônios. Um neurônio decide pouco; a inteligência emerge do conjunto. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Histórico

McCulloch e Pitts (1943, primeiro modelo matemático); Rosenblatt e o Perceptron (1958, [[wiki/entities/frank-rosenblatt]]); estagnação após 1969 ([[wiki/concepts/inverno-da-ia]]); uso real nos anos 80–90 (dígitos em cheques, fraude, OCR, defeitos industriais); retomada com [[wiki/concepts/deep-learning]]. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Exemplo: dígitos manuscritos

Imagem 28×28 → 784 entradas; 10 saídas (0–9); cada entrada conectada a cada saída por pesos. Pesos iniciam aleatórios; o erro contra o gabarito ajusta os pesos via [[wiki/concepts/backpropagation]]; repetir por todas as imagens, várias vezes. A rede descobre sozinha os traços relevantes. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Relação com outros itens

É a forma de [[wiki/concepts/modelo-de-machine-learning|modelo]] sobre a qual se constroem o [[wiki/concepts/deep-learning]], [[wiki/concepts/recurrent-neural-network|RNNs]] e o [[wiki/concepts/transformer-architecture|Transformer]].

## FrontPUSH: a rede como resposta à barreira das features

Em [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: "tentam imitar parcialmente o cérebro humano. Não biologicamente... mas matematicamente"; "cada conexão possui um peso matemático" ajustado no treino. Ele apresenta a rede como o passo seguinte ao ML, para "automatizar [...] o peso matemático". A ordem é didática, porque o Perceptron (1958) é anterior a SVM e random forest. O ganho real foi a rede aprender as features sozinha ([[wiki/concepts/engenharia-de-features]]), não o ajuste de pesos, que o ML clássico já fazia. A barreira que ele aponta: "pra ser bom, precisa de muitos parâmetros. Para ter muitos parâmetros precisa de muito recurso".

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: pesos, parâmetros e recurso
