---
type: concept
title: "Machine Learning"
aliases: ["aprendizado de máquina", "ML"]
date_created: 2026-10-14
date_updated: 2026-11-24
source_count: 2
tags: [ia, machine-learning, fundamentos]
skill: tech-mentor-ai
status: draft
---

## Definição

Paradigma em que, em vez de programar as regras, fornecemos **exemplos em forma de dados** e deixamos o algoritmo **encontrar os padrões**, ajustando parâmetros matemáticos para reduzir o erro (é, essencialmente, **otimização**). Termo cunhado por [[wiki/entities/arthur-samuel|Arthur Samuel]] em 1959 (programa de damas na IBM). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Por que surgiu

Escrever regras deixou de ser viável para problemas complexos e instáveis; o exemplo do spam mostra que regras rígidas geram exceções sem fim ([[wiki/concepts/sistema-especialista]]). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Tipos de aprendizado

- [[wiki/concepts/aprendizado-supervisionado]] — dados com gabarito (detalhado no vídeo).
- **Não supervisionado** — agrupa dados sem gabarito (só citado).
- **Por reforço** — tentativa e erro (só citado). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Produto final

O resultado do treino é um [[wiki/concepts/modelo-de-machine-learning|modelo]]. Modelos de ML incluem regressão linear, árvores de decisão, random forest, SVM e [[wiki/concepts/rede-neural-artificial|redes neurais]]. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## FrontPUSH: spam, features e a "curva de Gauss"

[[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]] repete o exemplo do spam: palavras proibidas no if/else × "mostrar milhões de emails" para o modelo perceber palavras, estruturas e comportamentos, aplicado no [[wiki/entities/gmail|Gmail]]. Duas precisões. (1) Ele descreve o mecanismo como "uma curva de Gauss"; o filtro estatístico clássico é o Naive Bayes ([external] http://www.paulgraham.com/spam.html). (2) A limitação que aponta ("humanos precisavam dizer quais características importar") é a [[wiki/concepts/engenharia-de-features]]. Na fala, porém, o humano também "dá os pesos", o que contradiz a definição acima: os pesos são o que o treino aprende.

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: spam, lista de modelos e limitação das features
