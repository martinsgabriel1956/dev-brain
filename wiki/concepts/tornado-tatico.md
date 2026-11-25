---
type: concept
title: "Tornado Tático"
aliases: ["tactical tornado", "tornado tatico"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 2
tags: [design, ousterhout, programacao-tatica, cultura-de-engenharia, tech-debt]
skill: tech-mentor-backend
status: stub
---

# Tornado Tático

## TL;DR

É o nome que [[wiki/entities/john-ousterhout]] dá ao desenvolvedor que leva a [[wiki/concepts/programacao-tatica-vs-estrategica|programação tática]] ao extremo ([[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]], seção 3.1). É prolífico e entrega muito mais rápido que os outros, mas de forma totalmente tática, deixando "um rastro de destruição por onde passa".

## O problema de incentivo

- A gerência às vezes o trata como herói, porque só vê a velocidade de entrega.
- Os engenheiros que herdam o código raramente pensam assim.
- Quem limpa a bagunça são "os verdadeiros heróis", e justamente por isso parecem mais lentos que o tornado.

O custo do tornado não aparece na métrica de quem o avalia, e aparece na de quem trabalha depois dele. É um caso de métrica que premia o comportamento errado; ver [[wiki/concepts/goodharts-law]] (ligação da wiki, não do livro).

## O que o separa de uma entrega tática disciplinada

[[wiki/concepts/tech-debt-como-ferramenta]] registra, pelo podcast sobre o livro, o hábito de abrir um ticket e deixar um link no código quando se aceita uma solução tática sob pressão. É o oposto do tornado: entrega rápido, mas deixa a dívida visível e com dono.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]: seção 3.1
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: menção no resumo do cap. 3
