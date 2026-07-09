---
type: concept
title: "Modelagem de Dados"
aliases: ["data modeling", "modelagem relacional", "normalização"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [banco-de-dados, modelagem, normalizacao, indice, backend]
skill: tech-mentor-backend
status: stub
---

# Modelagem de Dados

Decidir como o mundo real vira estrutura no banco. Um pedido tem usuário, itens, pagamento, endereço, status — e a forma como essas entidades se relacionam determina o quanto o resto do sistema sofre depois.

## O tradeoff central

| Erro | Consequência |
|---|---|
| Modelar mal / pouco | Regra de negócio fica confusa, dados inconsistentes |
| Normalizar demais | Toda consulta envolve vários joins, complexidade cresce |

## Performance é parte da modelagem

Uma query mal servida por índice pode virar um full scan gigante; a mesma query com índice adequado encontra o dado em poucos passos. Quando um sistema fica lento, o primeiro lugar a olhar costuma ser: falta algum índice? As tabelas foram organizadas de um jeito que obriga o banco a ler dado de vários lugares?

## Relação com outros conceitos

- [[wiki/concepts/database-transactions]] — depois de modelado, o dado precisa se manter correto sob concorrência
- [[wiki/concepts/cache]] — cache é a camada que se apoia em cima de uma modelagem já feita
- Ver aprofundamento de índices, EXPLAIN ANALYZE e query optimization em `references/database-query-optimization.md` (tech-mentor-backend)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
