---
type: concept
title: "Projetos Fundamentais para Aprender a Programar"
aliases: ["Snake, supermercado e pathfinding", "três projetos de aprendizado", "software é argila não lego"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [projetos, aprendizado, iniciantes, algoritmos, modelagem, gerenciamento-de-estado]
skill: tech-mentor-leadership
status: draft
---

# Projetos Fundamentais para Aprender a Programar

Três projetos de aprendizado escolhidos não pelo critério "fica bonito no portfólio", mas pela habilidade fundamental que cada um força a desenvolver: **Snake** (controlar um sistema), um **simulador de supermercado** (modelar um sistema) e um **Pathfinding** (resolver um problema).

## O Modelo Mental Errado: Software Como Lego

A crença comum de iniciante é que programar é como montar Lego: encaixar uma peça, depois outra, depois outra, e no final tudo funciona magicamente sem retrabalho. Esse modelo quebra na prática — a frustração de "por que isso não funciona" depois de uma hora de trabalho vem justamente dessa expectativa errada.

O modelo mais preciso é **software como argila**: você joga um monte de argila na mesa e vai modelando ao redor, um pedaço de cada vez — e mexer em um pedaço frequentemente obriga a ajustar o pedaço vizinho. Construir software é iterativo e acoplado, não sequencial e independente.

## Os Três Projetos

### 1. Snake → Gerenciamento de Estado

A dificuldade do Snake não está em nenhuma peça isolada de lógica — está em manter posição da cobra, posição da comida e pontuação coerentes entre si a cada frame, sem que a mudança de uma quebre as outras. Isso é [[wiki/concepts/estado]]: impedir que o sistema fique inconsistente enquanto múltiplas partes mudam ao mesmo tempo.

### 2. Simulador de Supermercado → Modelagem de Domínio

Ações triviais para um humano — pegar produto, passar no caixa, ir embora — escondem perguntas nada óbvias para o computador: como saber que o produto ainda tem estoque? Como impedir que dois clientes comprem o último item ao mesmo tempo? Como calcular o total? Como validar que o preço não é um erro? Construir esse projeto não é "fazer um supermercado" — é ensinar o computador como um supermercado funciona. Essa habilidade é [[wiki/concepts/modelagem-de-dados|modelagem]]: pegar algo do mundo real e transformá-lo em sistema.

### 3. Pathfinding → Algoritmos como Estratégia

Criar um labirinto e fazer o computador descobrir sozinho o melhor caminho até a saída desloca o foco de "como escrever a linha de código" para "como resolver o problema": e se esse caminho estiver bloqueado? Como evitar visitar o mesmo lugar duas vezes? Essa mudança de raciocínio — de sintaxe para estratégia — é a porta de entrada para [[wiki/concepts/algoritmos-de-grafo|algoritmos de busca em grafo]] (BFS, DFS, Dijkstra, A*).

## Progressão Pedagógica

```
Snake            → controlar um sistema     (estado)
Supermercado     → modelar um sistema        (modelagem de domínio)
Pathfinding      → resolver um problema      (algoritmos)
```

Cada projeto força um tipo de raciocínio diferente dos outros dois — não são variações de dificuldade do mesmo problema, são três habilidades ortogonais.

## Relação com outros conceitos

- [[wiki/concepts/estado]] — habilidade central exercitada pelo Snake
- [[wiki/concepts/modelagem-de-dados]] — habilidade central exercitada pelo simulador de supermercado; ver também [[wiki/concepts/modelagem-orientada-a-objetos]]
- [[wiki/concepts/algoritmos-de-grafo]] — algoritmos de busca de caminho aplicáveis ao Pathfinding (BFS, DFS, Dijkstra, A*)
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub mais amplo de DSA; este projeto é uma aplicação prática e motivadora de estudar a área
- [[wiki/concepts/projeto-com-adrenalina]] — tensão de fase: aquele conceito recomenda escolher o projeto pelo interesse genuíno do aprendiz; este propõe três projetos prescritos por habilidade, independentemente do interesse pessoal — resolvem perguntas diferentes ("o que me motiva a continuar" vs. "quais habilidades um currículo mínimo de projetos deveria cobrir")

## Key Sources

- [[wiki/sources/tres-projetos-para-aprender-programar]]
