---
type: concept
title: "Eixo Visual"
aliases: ["eixo", "eixo de alinhamento", "eixo de reforço", "eixo de movimento", "eixo de continuidade", "visual axis"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 1
tags: [ui, ui-design, layout, alinhamento, grid, hierarquia-visual]
skill: ux-ui-mentor
status: stub
---

# Eixo Visual

Linha imaginária usada para organizar um grupo de elementos na interface. É a base dos grids: um grid é um conjunto de eixos ("literalmente colunas"). Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], o eixo tem quatro usos.

| Uso | O que comunica | Exemplo da aula |
|---|---|---|
| **Alinhamento** | Ordem; itens no mesmo eixo e do mesmo tamanho são da mesma categoria | Faixas de um álbum num app de música |
| **Reforço** | Quebrar o eixo marca subordinação: o item deslocado pertence ao de cima | Retweet e resposta no feed do [[wiki/entities/twitter]] |
| **Movimento** | Num eixo horizontal, card cortado na borda indica que há mais | Fileiras de filmes da [[wiki/entities/netflix]] |
| **Continuidade** | Sem ponto final definido, o olho segue o eixo; base do feed infinito | Explorar do Instagram ([[wiki/entities/meta]]) |

Alinhamento e reforço também criam [[wiki/concepts/hierarquia-visual]]: a posição em relação ao eixo diz o que é igual e o que é filho. O reforço é a [[wiki/concepts/lei-da-proximidade-gestalt]] aplicada a uma linha: o deslocamento agrupa o item com o de cima.

A relação entre os eixos (iguais ou não) é o que [[wiki/concepts/simetria-visual]] trata.

`[skill: ux-ui-mentor]` Na implementação, os eixos viram as colunas e gutters do grid (12 colunas no desktop, 4 no mobile) e o espaçamento num sistema de 8pt. Na implementação, o card cortado da Netflix sai de um container com `overflow-x: auto` cujo último card visível não cabe inteiro (nota do agente).

`[skill: ux-ui-mentor]` Infinite scroll, consequência do eixo de continuidade, serve a feeds exploratórios mas impede bookmarking e esconde o rodapé.

## Key Sources

- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]
