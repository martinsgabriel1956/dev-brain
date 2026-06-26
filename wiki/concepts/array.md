---
type: concept
title: "Array"
aliases: ["vetor", "lista indexada", "indexed array"]
date_created: 2026-06-01
date_updated: 2026-06-26
source_count: 2
tags: [cs-fundamentals, estruturas-de-dados, array, performance, big-o]
skill: cs-fundamentals
status: draft
---

# Array

Coleção **ordenada** de elementos onde cada item ocupa uma posição numérica chamada **índice**. A contagem começa em zero — o primeiro elemento está na posição 0, o segundo na posição 1, e assim por diante.

## Operações e Complexidade

| Operação | Complexidade | Por quê |
|---|---|---|
| Acesso por índice | **O(1)** | Posição conhecida — vai diretamente |
| Busca por valor | O(n) | Percorre um por um até encontrar |
| Inserção no final | O(1) amortizado | Sem deslocamento |
| Inserção no meio | **O(n)** | Todos os elementos seguintes se deslocam |
| Remoção no meio | **O(n)** | Idem — deslocamento obrigatório |

## Ponto Forte

Acesso por índice em tempo constante. Você sabe exatamente onde o elemento está — sem busca.

```python
usuarios[9]  # acessa o 10º usuário diretamente — O(1)
```

## Ponto Fraco

Inserir ou remover no meio é caro. Remover o elemento da posição 3 de um array com 1 milhão de elementos exige deslocar todos os ~999.997 elementos seguintes.

## Quando Usar

- A ordem importa e você acessa por posição
- Você vai iterar por todos os elementos em sequência
- O tamanho é previsível e relativamente fixo
- Leituras são muito mais frequentes que inserções no meio

## Quando Não Usar

- Você busca elementos por atributo (use [[hashmap]])
- Você insere ou remove no meio com frequência (considere linked list)
- Você precisa de estrutura FIFO/LIFO (use [[fila]] ou [[pilha]])

## Analogia

Uma fila de pessoas num show. Você sabe que a 10ª pessoa está na posição 9. Para acessar, vai direto — sem percorrer.

## Relação com outros conceitos

- [[hashmap]] — alternativa quando a busca é por atributo, não por posição
- [[algoritmos-e-estruturas-de-dados]] — array é a estrutura mais básica da sequência de aprendizado

## Key sources

- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
