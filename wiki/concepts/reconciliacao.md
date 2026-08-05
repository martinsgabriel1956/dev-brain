---
type: concept
title: "Reconciliação (Reconciliation)"
aliases: ["reconciliation", "algoritmo de diffing", "keys em listas"]
date_created: 2026-08-03
date_updated: 2026-08-04
source_count: 2
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

## "Entrar no fluxo de renderização" ≠ Tocar o DOM Real

Quando qualquer estado/prop de um componente muda — inclusive quando o componente **pai** re-renderiza por qualquer motivo — o componente sempre gera uma nova versão de si mesmo na [[wiki/concepts/virtual-dom]]. Isso é inevitável e acontece com **todo** componente afetado, independente de qual informação específica mudou.

Só que gerar essa nova versão não significa que o DOM real vai ser tocado. No React DevTools Profiler, um componente que "renderizou" (gerou nova Virtual DOM) mas cuja comparação de reconciliação não encontrou diferença nenhuma aparece colorido no flamegraph — dando a impressão de que algo aconteceu — mas nenhuma mutação de DOM real ocorre. As etapas 2 (diff) e 3 (aplicar mudanças) só têm efeito quando há diferença real; para um componente sem mudança de conteúdo, apenas a etapa 1 (gerar Virtual DOM) roda, e ela sozinha já é a etapa 1 de um processo de 3, então listas grandes ainda pagam esse custo de "gerar de novo" em todo item, mesmo que nenhum deles seja realmente reescrito em tela. [[wiki/concepts/react-memo]] existe justamente para interceptar *antes* dessa etapa 1 e evitar até a geração da nova Virtual DOM quando props/estado não mudaram (resultado visível no Profiler como `did not render`, distinto de "renderizou mas sem mudança de DOM").

## Ver também

- [[wiki/concepts/virtual-dom]] — a estrutura de dados que a reconciliação compara
- [[wiki/concepts/derived-state]] — outro efeito de estado dessincronizado, causa diferente
- [[wiki/concepts/react-memo]] — bloqueia a entrada no fluxo de renderização antes mesmo da etapa 1

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]]
