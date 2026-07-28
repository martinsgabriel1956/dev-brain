---
type: concept
title: "Lista Encadeada"
aliases: ["linked list", "lista ligada", "linked-list"]
date_created: 2026-06-26
date_updated: 2026-07-28
source_count: 2
tags: [cs-fundamentals, estruturas-de-dados, lista-encadeada, ponteiros]
skill: cs-fundamentals
status: draft
---

# Lista Encadeada

Coleção de **nós** onde cada nó armazena um valor e um ponteiro para o próximo nó. Não há índices — para chegar ao nó 10 você precisa percorrer todos os anteriores.

```
[A | →] → [B | →] → [C | →] → [D | null]
```

## Operações e Complexidade

| Operação | Complexidade | Por quê |
|---|---|---|
| Acesso por posição | **O(n)** | Percorre do início até a posição |
| Busca por valor | O(n) | Percorre até encontrar |
| Inserção no início | **O(1)** | Cria nó, aponta para o antigo head |
| Inserção no meio (com ponteiro) | **O(1)** | Redireciona ponteiros — sem deslocamento |
| Remoção no meio (com ponteiro) | **O(1)** | Idem |

## Vantagem sobre [[array]]

Inserir ou remover no meio sem deslocar elementos. Enquanto o array move ~n elementos, a lista só redireciona ponteiros.

```
Inserir C entre B e D:
Antes: [A]→[B]→[D]
Depois: [A]→[B]→[C]→[D]
Custo: 2 operações de ponteiro — O(1)
```

## Desvantagem em relação a [[array]]

Acesso aleatório é O(n). Não há atalho para "me dá o 500º elemento" — você percorre do início.

Além disso, usa mais memória por elemento (valor + ponteiro).

## Variações

- **Duplamente encadeada**: cada nó tem ponteiro para anterior e próximo — remoção mais fácil
- **Circular**: último nó aponta para o primeiro — útil para buffers circulares e implementação de [[fila]]

## Quando usar

- Implementar [[fila]] ou [[pilha]] onde inserções/remoções ocorrem nas pontas
- Histórico de ações (desfazer) onde elementos são adicionados/removidos do topo
- Quando o tamanho é desconhecido e cresce/shrink frequentemente

## Relação com outros conceitos

- [[array]] — os dois são sequências; lista ganha em inserção, array ganha em acesso
- [[big-o]] — entender a diferença O(1) vs O(n) em cada estrutura é o ponto central
- [[arvore]] — árvores são extensões de listas onde cada nó tem múltiplos "próximos"
- [[wiki/concepts/ponteiros-cpp-stack-heap-raii]] — o custo O(1) de inserção/remoção com ponteiro depende do modelo de memória: em C/C++ o nó é alocado manualmente na heap (`new`/`malloc`), em Go e C# o GC decide e libera

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/ponteiros-cpp-go-csharp]] — ponteiro de nó como o mecanismo concreto por trás do O(1) de redirecionamento
