---
type: source
title: "3 Projetos Que Realmente Ensinam a Programar: Snake, Simulador de Supermercado e Pathfinding"
aliases: ["três projetos para aprender a programar", "snake supermercado pathfinding"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [projetos, aprendizado, iniciantes, algoritmos, modelagem, gerenciamento-de-estado]
skill: tech-mentor-leadership
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tres-projetos-para-aprender-programar.md
source_url: ""
author: "desconhecido (transcrição vídeo PT-BR)"
date_published: 2026-07-31
date_ingested: 2026-07-31
status: stable
---

# 3 Projetos Que Realmente Ensinam a Programar

## TL;DR

Em vez de recomendar projetos pelo critério "fica bonito no portfólio", a fonte propõe três projetos escolhidos pela habilidade fundamental que cada um força a desenvolver: Snake ensina **gerenciamento de estado** (controlar um sistema onde múltiplas coisas mudam ao mesmo tempo e precisam permanecer coerentes), um simulador de supermercado ensina **modelagem de domínio** (transformar regras do mundo real — estoque, preço, concorrência no caixa — em estrutura de dados), e um Pathfinding (labirinto + busca de caminho) ensina **algoritmos** (deixar de pensar em linhas de código e passar a pensar em estratégia de resolução de problema).

## Key Claims

- **Software é argila, não Lego**: a crença de iniciante de que programar é encaixar peças prontas uma a uma, sem retrabalho, é descrita como o modelo mental errado — construir software se parece mais com modelar argila, onde mexer em uma parte frequentemente exige ajustar outra já feita. → [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]]
- **Snake ensina gerenciamento de estado**: a dificuldade do Snake não é a lógica isolada de mover a cobra — é manter posição da cobra, posição da comida e pontuação coerentes entre si a cada frame, sem que uma mudança quebre as outras. → [[wiki/concepts/estado]]
- **Simulador de supermercado ensina modelagem**: ações triviais para um humano (pegar produto, passar no caixa) escondem perguntas não óbvias para o computador — controle de estoque, concorrência (dois clientes comprando o último item), cálculo de total, validação de preço. Modelar é "ensinar o computador como o supermercado funciona", não construir o supermercado. → [[wiki/concepts/modelagem-de-dados]]
- **Pathfinding ensina algoritmos como estratégia, não sintaxe**: resolver um labirinto programaticamente desloca o foco de "como escrever a linha" para "como evitar visitar o mesmo lugar duas vezes" e "o que fazer se o caminho estiver bloqueado" — a entrada para o estudo formal de algoritmos de busca/grafo. → [[wiki/concepts/algoritmos-de-grafo]]
- **Progressão pedagógica dos três projetos**: controlar um sistema (Snake) → modelar um sistema (supermercado) → resolver um problema (Pathfinding). Nenhum foi escolhido por estética de portfólio — a escolha é pela mudança de raciocínio que cada um força. → [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]]

## Entities

*(nenhuma entidade nomeada nesta fonte — autor do vídeo não identificado na transcrição)*

## Concepts

[[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]] · [[wiki/concepts/estado]] · [[wiki/concepts/modelagem-de-dados]] · [[wiki/concepts/algoritmos-de-grafo]] · [[wiki/concepts/algoritmos-e-estruturas-de-dados]] · [[wiki/concepts/projeto-com-adrenalina]]

## Open Questions

- A fonte não especifica se o Pathfinding deve ser resolvido com BFS, DFS, Dijkstra ou A* — trata "algoritmo de busca de caminho" genericamente. Ver [[wiki/concepts/algoritmos-de-grafo]] para a progressão de eficiência entre essas opções.
- Tensão não resolvida com [[wiki/concepts/projeto-com-adrenalina]]: aquela fonte recomenda escolher o projeto pelo critério de interesse genuíno ("adrenalina") do aprendiz; esta fonte recomenda três projetos específicos e prescritos independentemente do interesse pessoal. Não há contradição factual, mas são conselhos de fases diferentes: um é sobre *qual* projeto motiva a pessoa a continuar, o outro é sobre *quais habilidades* um currículo mínimo de projetos deveria cobrir.

## Raw Quotes

> "Construir um programa não funciona assim... software é mais parecido com modelagem com argila. Eu pego um monte de argila, taco na mesa, e vou modelando ao redor — um pedaço de cada vez. Para cada pedaço que eu mexo aqui, tenho que mexer no de baixo."

> "Você não está fazendo um supermercado — você está ensinando um computador como um supermercado funciona."

> "Até agora você estava ensinando o computador como as coisas funcionam. Agora você está ensinando ele como resolver um problema — parece a mesma coisa, mas não é."

> "Nenhum deles foi escolhido porque fica bonito no GitHub. Eles foram escolhidos porque mudam a forma como você pensa sobre programação."
