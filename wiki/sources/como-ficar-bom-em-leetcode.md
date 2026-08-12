---
type: source
title: "Como ficar bom em LeetCode"
aliases: ["ficar bom em leetcode", "como estudar leetcode", "metodo leetcode"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-ficar-bom-em-leetcode.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-12
source_count: 0
tags: [cs-fundamentals, leetcode, algoritmos, estruturas-de-dados, entrevistas, pratica-deliberada, python]
skill: cs-fundamentals
status: stable
---

# Como ficar bom em LeetCode

## TL;DR

Transcrição de vídeo (pt-BR, canal com foco em Python) com um **método iterativo** para ficar bom em [[wiki/entities/leetcode|LeetCode]]. A tese central é a de [[wiki/concepts/reconhecimento-de-padroes|reconhecimento de padrões]]: você não decora problemas, você constrói um repertório de **padrões de solução** por repetição. O loop é: escolher uma linguagem de baixo boilerplate (Python de preferência) → estudar e **implementar** uma estrutura de dados → aprender os algoritmos/padrões dela → resolver vários problemas do mesmo padrão até reconhecê-lo no enunciado → passar para a próxima estrutura. Corolário anti-frustração: se em ~5-10 min você não enxerga o início de uma solução, **não fique quebrando a cabeça** — leia a solução, reescreva-a linha a linha (sem copiar/colar) e siga para o próximo.

## Key Claims

- **Antes do "como", o "porquê".** Três motivos legítimos para estudar LeetCode: (1) passar em entrevistas — o principal; (2) a ideia de "lógica de programação" — vaga, mas os problemas estilo LeetCode estão entre a classe mais difícil de resolver em computação; (3) interesse genuíno em [[wiki/concepts/algoritmos-e-estruturas-de-dados|algoritmos e estruturas de dados]]. Ressalva honesta: **LeetCode não te faz bom em programação do dia a dia** (erro de CORS, browser incompatível etc. não têm nada a ver) — ajuda tangencialmente e dá fluência na linguagem.
- **Escolha uma linguagem de baixo boilerplate e use só ela.** Recomendação: **Python** (tipagem fraca, poucos imports, rápido de prototipar — e LeetCode é essencialmente prototipar um algoritmo e testar várias vezes). Alternativas boas: **Go** e **JavaScript**. Evite **Rust/Haskell** a menos que já seja muito bom nelas — senão você briga com a linguagem em vez do problema, e mistura dois *skill sets* distintos (aprender a linguagem vs. aprender os algoritmos). → [[wiki/concepts/escolha-de-linguagem-para-leetcode]]
- **Estruturas de dados que cobrem quase tudo:** [[wiki/concepts/array|array]], linked list, queue, stack, [[wiki/concepts/binary-search-tree|binary tree]], [[wiki/concepts/hashmap|hash map]] e graph. B-tree e heap são raras — não priorize no começo.
- **Big O é obrigatório.** "Tem que saber Big O para ficar bom em LeetCode. Ponto." → [[wiki/concepts/big-o]]
- **Implemente cada estrutura por conta própria** (uma árvore binária, uma linked list). É a diferença entre ler sobre e entender. Recursos citados: GeeksforGeeks, curso gratuito do [[wiki/entities/the-primeagen|ThePrimeagen]] no Frontend Masters, e o livro *Entendendo Algoritmos* (*Grokking Algorithms*).
- **Depois da estrutura, aprenda os padrões dela.** Ex.: em binary tree, quase tudo cai em [[wiki/concepts/busca-em-profundidade|DFS]] ou [[wiki/concepts/busca-em-largura|BFS]]. Filtre problemas por tema no LeetCode, ordene por *acceptance rate* (alta ≈ intuitivo) ou Easy→Hard, e resolva em série.
- **Não fique quebrando a cabeça.** Se não sabe resolver, talvez nunca tenha visto o algoritmo — não há nada a ganhar em 3 horas de bloqueio. Timebox de ~5-10 min; se não vier o início de uma solução, abra as *submissions*, entenda o código e **reescreva** (reescrever força atenção que copiar/colar não força). → [[wiki/concepts/pratica-deliberada]]
- **Reconheça o padrão por repetição.** Depois de 2-4 problemas do mesmo tipo (ex.: DFS), você passa a **identificar quando o enunciado pede aquele padrão** — esse é o objetivo real, não a solução de um problema específico. → [[wiki/concepts/reconhecimento-de-padroes]]
- **Padrões prioritários:** [[wiki/concepts/two-pointer|Two Pointer]] (cai muito — "provavelmente o primeiro em que focar"), [[wiki/concepts/hashmap|hash map]] ("resolve quase tudo"), [[wiki/concepts/busca-em-profundidade|DFS]]/[[wiki/concepts/busca-em-largura|BFS]], [[wiki/concepts/sliding-window|sliding window]], [[wiki/concepts/backtracking|backtracking]] e [[wiki/concepts/programacao-dinamica|dynamic programming]] (comece pelo Fibonacci).

## Exemplo trabalhado no vídeo

Problema de [[wiki/concepts/binary-search-tree|BST]]: dados `low` e `high`, somar todos os nós cujo valor está no intervalo `[low, high]`. Se você não conhece "binary search tree", **pesquisa e volta** — uma BST é uma árvore ordenada para busca (à direita, maiores; à esquerda, menores, recursivamente). Timebox de ~10 min; sem solução clara, vai em *Solutions* → filtra por Python → pega a mais votada → é uma **DFS** (como esperado para binary tree). Depois, volta à lista e resolve outro problema de DFS (ex.: *Sum Root to Leaf Numbers*) para fixar o padrão.

## Entities

[[wiki/entities/leetcode]] · [[wiki/entities/the-primeagen]]

## Concepts

[[wiki/concepts/reconhecimento-de-padroes]] · [[wiki/concepts/pratica-deliberada]] · [[wiki/concepts/algoritmos-e-estruturas-de-dados]] · [[wiki/concepts/big-o]] · [[wiki/concepts/two-pointer]] · [[wiki/concepts/hashmap]] · [[wiki/concepts/array]] · [[wiki/concepts/binary-search-tree]] · [[wiki/concepts/busca-em-profundidade]] · [[wiki/concepts/busca-em-largura]] · [[wiki/concepts/sliding-window]] · [[wiki/concepts/backtracking]] · [[wiki/concepts/programacao-dinamica]] · [[wiki/concepts/escolha-de-linguagem-para-leetcode]]

## Conexão com o resto da wiki

Esta fonte é o **lado prático/mecânico** (o "como treinar") da mesma tese que [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] e [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] (Anthony Mays) defendem pelo lado da entrevista: **memorize o padrão, não o problema**. Mays enquadra pela perspectiva do entrevistador (o que gera sinal); esta fonte enquadra pela rotina de estudo (o loop estrutura → padrão → repetição). Ambas convergem em [[wiki/concepts/reconhecimento-de-padroes]] e no valor de não travar. Também dialoga com [[wiki/sources/binary-search-em-5-minutos]] e [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]], que exemplificam padrões concretos (two pointer, hash set, bucket sort) na mesma plataforma.

## Open Questions

- A afirmação "não adianta ficar quebrando a cabeça" tem um limite não explicitado: alguma luta produtiva (*productive struggle*) antes de olhar a solução é o que consolida o padrão — ver [[wiki/concepts/pratica-deliberada]]. O timebox de 5-10 min é uma heurística do autor, não um número validado.
- O conselho de evitar Rust/Haskell é sobre *velocidade de aprendizado de LeetCode*, não sobre a qualidade dessas linguagens — para quem já é fluente nelas, a recomendação se inverte.

## Raw Quotes

> "Não memorize o problema, memorize o padrão."

> "Se você não sabe resolver um problema, você não sabe resolver esse problema. Não tem nada que você vai aprender ficando 3 horas batendo a cabeça no problema."

> "Two pointer sempre cai. Eu acho que esse é o primeiro que você devia focar."

> "Tem que saber Big O para ficar bom em LeetCode. Ponto."
