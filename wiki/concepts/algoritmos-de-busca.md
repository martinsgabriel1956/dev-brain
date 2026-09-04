---
type: concept
title: "Algoritmos de Busca"
aliases: ["searching algorithms", "search", "busca", "linear search", "binary search"]
date_created: 2026-07-09
date_updated: 2026-09-03
source_count: 8
tags: [cs-fundamentals, algoritmos, searching, big-o, linear-search, binary-search, two-pointer, logaritmo]
skill: cs-fundamentals
status: draft
---

# Algoritmos de Busca

Métodos para encontrar um elemento em uma estrutura de dados ou confirmar sua existência/localização. A escolha certa depende de uma pergunta simples: os dados estão ordenados?

## Linear Search (Busca Linear)

Verifica cada elemento em sequência até encontrar o alvo ou a lista terminar. Não exige nenhuma ordenação prévia.

- **Melhor caso:** O(1) — alvo na primeira posição
- **Pior caso / caso médio:** O(n)
- Bom se o alvo tende a estar perto do início; ruim se está no fim ou ausente. Ver [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] para a distinção formal entre os três cenários.

## Binary Search (Busca Binária)

Divide repetidamente o intervalo de busca ao meio, comparando o elemento do meio com o alvo e descartando a metade que não pode conter o resultado.

- **Tempo médio/pior caso:** O(log n)
- **Pré-requisito obrigatório:** o array precisa estar ordenado.
- Significativamente mais rápida que a busca linear para conjuntos grandes — em 1 bilhão de elementos, ~30 comparações (ver [[wiki/concepts/big-o]]).

### Além de arrays: espaço de decisão monotônico

`[skill: cs-fundamentals]` Binary search não é só para arrays — qualquer **espaço de decisão monotônico** pode ser buscado da mesma forma. Exemplo arquitetural: encontrar o menor rate limit que não degrada o SLA fazendo binary search no espaço de valores possíveis, em vez de testar valor por valor.

### Implementação real: two pointers, não recursão com recriação de array

A alternativa recursiva "óbvia" — fatiar/recriar um novo sub-array a cada chamada — é computacionalmente cara por causa da cópia repetida. A implementação padrão usa a técnica [[wiki/concepts/two-pointer]]: dois índices (`left`, `right`) delimitam a região de busca atual sem nunca recriar o array original.

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
```

Cuidado de implementação: em linguagens com inteiro de tamanho fixo, `(left + right) // 2` pode estourar (overflow) — Python não sofre com isso, mas outras linguagens devem preferir `left + (right - left) // 2`.

## Outras variantes citadas na fonte

Jump search, exponential search, Fibonacci search, e busca em hash table (O(1) esperado, buscando a chave diretamente — mas não garantido em todos os casos, ex: colisões).

## Caso de Borda Obrigatório: "Não Está na Coleção"

[[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] enfatiza, ao construir o pseudocódigo de busca binária num catálogo telefônico passo a passo, que todo algoritmo de busca precisa de um ramo explícito para o caso "o item não está na coleção" — sem esse `senão, desista` final, o algoritmo (e o programa real que o implementa) fica com comportamento indefinido, o que na prática se manifesta como travamentos ou reinícios espontâneos de software. É um lembrete de engenharia defensiva, não um detalhe puramente acadêmico: o caso de borda mais fácil de esquecer é justamente aquele em que a busca falha.

## O trade-off central

Binary Search só é possível porque alguém pagou o custo de ordenar os dados primeiro (ver [[wiki/concepts/algoritmos-de-ordenacao]]). Se os dados mudam com frequência e a ordenação tem que ser refeita a cada busca, Linear Search pode acabar sendo mais barato no total.

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — O(log n) vs O(n): a diferença prática em datasets grandes
- [[wiki/concepts/algoritmos-de-ordenacao]] — pré-requisito de Binary Search
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista busca como terceiro passo da sequência de aprendizado de DSA
- [[wiki/concepts/hashmap]] — busca por chave O(1) amortizado como alternativa a busca em array
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] — busca linear como exemplo didático dos três cenários de complexidade
- [[wiki/concepts/two-pointer]] — técnica usada na implementação real de binary search (evita recriação recursiva de sub-arrays)
- [[wiki/concepts/logaritmo]] — por que binary search é O(log n): cada passo descarta metade do problema (`2^x = n`)

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — busca binária como exemplo canônico de O(log n) (cada passo descarta metade do problema); distinção melhor/pior/caso médio
- [[wiki/sources/binary-search-em-5-minutos]] — implementação two pointers completa, resolvida ao vivo no LeetCode em menos de 5 minutos
- [[wiki/sources/busca-linear-e-binaria-giovana]] — analogia física (achar página 310 num livro de 423 páginas), contador de etapas (7 vs. 3) e derivação da complexidade logarítmica (`2^x = n`, base 2)
- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] — três algoritmos físicos num catálogo telefônico de ~1000 páginas (1 página, 2 páginas, dividir ao meio) buscando "John Harvard"; caso de borda obrigatório "item ausente"; construção do pseudocódigo passo a passo
- [[wiki/sources/busca-binaria-fila-protocolos-atendimento-live-coding]] — trace manual (sem código) buscando um protocolo numa fila ordenada, com leitura direta do livro *Entendendo Algoritmos*: analogia "adivinhar 1-100 com menor número de tentativas" e dicionário de 240.000 palavras (18 etapas vs. até 239.999 no brute force)
- [[wiki/sources/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort]] — ordenação como pré-requisito de Binary Search: seis algoritmos de ordenação (Quicksort incluído) detalhados mecanismo a mecanismo
- [[wiki/sources/como-calcular-complexidade-de-algoritmos-big-o-em-3-passos]] — busca linear em vetor como primeiro exemplo do método de 3 passos (achar o loop → checar `size()` é O(1) → complexidade final O(n)); busca em estrutura ordenada via `count()` como O(log n)
