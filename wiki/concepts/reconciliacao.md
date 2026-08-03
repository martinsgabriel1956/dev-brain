---
type: concept
title: "Reconciliação (Reconciliation)"
aliases: ["reconciliation", "algoritmo de diffing", "keys em listas"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, react, virtual-dom, reconciliacao, keys, performance]
skill: tech-mentor-frontend
status: stable
---

# Reconciliação

Algoritmo que frameworks baseados em [[wiki/concepts/virtual-dom]] usam para descobrir a diferença entre um render e o anterior, e aplicar só as mudanças necessárias no [[wiki/concepts/dom]] real.

## Regras centrais

- **Tipo de elemento diferente** (ex. `div` → `span`, ou troca de componente): o framework destrói a subárvore antiga e monta uma nova do zero — todo o estado interno daquele nó se perde.
- **Tipo igual**: o framework reaproveita o nó e só atualiza as props/atributos que mudaram.

## Listas e `key`

Ao comparar uma lista de elementos, o framework precisa de uma forma de saber "qual item é qual" entre um render e outro:

- **Sem key** (ou usando o índice do array como key): a comparação é posicional — primeiro item novo com primeiro antigo, segundo com segundo. Deletar um item do meio faz o framework achar que os itens seguintes mudaram de conteúdo, quando na verdade só a posição shiftou. Isso é seguro **apenas** em listas estáticas que nunca reordenam, inserem ou removem itens no meio.
- **Com key estável** (ex. um ID): a comparação é por identidade — o framework sabe que o item "Ana" continua sendo "Ana" independente de posição, e só o item genuinamente removido é tratado como removido.

**Sintomas de key errada** (índice em lista dinâmica): inputs perdem o texto digitado ao reordenar, animações resetam, estado interno de um item "vaza" para outro item na posição errada.

**Técnica deliberada**: para forçar reset completo de um componente (perder todo estado interno e remontar do zero), basta mudar a `key` — o framework trata como um componente totalmente novo.

## Ver também

- [[wiki/concepts/virtual-dom]] — a estrutura de dados que a reconciliação compara
- [[wiki/concepts/derived-state]] — outro efeito de estado dessincronizado, causa diferente

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
