---
type: concept
title: "Two Pointer"
aliases: ["two pointers", "dois ponteiros", "técnica de dois ponteiros"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 3
tags: [cs-fundamentals, algoritmos, two-pointer, array, binary-search]
skill: cs-fundamentals
status: draft
---

# Two Pointer

Técnica que percorre uma estrutura linear (tipicamente um [[wiki/concepts/array|array]] ordenado) usando dois índices móveis em vez de recriar sub-estruturas a cada passo. Evita o custo de alocação repetida que uma abordagem recursiva ingênua teria ao fatiar/recriar o array em cada chamada.

## Por que existe

A alternativa recursiva "óbvia" para muitos problemas de array — dividir o problema fatiando um novo sub-array a cada chamada — tem custo de espaço/tempo extra por causa da cópia. Two pointer resolve o mesmo problema navegando pelos mesmos índices do array original, sem nunca recriá-lo: os ponteiros se movem, os dados ficam parados.

## Aplicação em Binary Search

Exemplo canônico documentado em [[wiki/sources/binary-search-em-5-minutos]]: em vez de recriar recursivamente metades do array a cada chamada, dois ponteiros (`left`, `right`) delimitam a região de busca atual. O ponto médio é recalculado a cada iteração (`(left + right) // 2`), e um dos dois ponteiros se move para dentro dessa região a cada passo, conforme o elemento do meio for maior ou menor que o alvo — ver [[wiki/concepts/algoritmos-de-busca]] para o algoritmo completo.

```python
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

## Aplicação em Reverse Only Letters (ponteiros independentes)

[[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] documenta uma variante onde os dois ponteiros **não se movem em sincronia** por uma regra geométrica fixa (como em binary search), mas de forma independente conforme uma condição local: um ponteiro no início e outro no fim de uma string avançam sozinhos enquanto o caractere na própria posição não for uma letra; só trocam de posição (e avançam os dois juntos) quando ambos apontam simultaneamente para letras. Ilustra que "two pointer" não é uma única regra de movimento, mas uma família de técnicas que usa dois índices em vez de recriar a estrutura — O(n), uma única passagem pela string.

```python
left, right = 0, len(s_list) - 1
while left < right:
    if not s_list[left].isalpha():
        left += 1
    elif not s_list[right].isalpha():
        right -= 1
    else:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
```

## Outras aplicações citadas na wiki

[[wiki/sources/two-sum-explicacao]] menciona Two Sum em array ordenado como variante resolvível com two pointers em O(n) sem espaço extra (alternativa ao hash map, que usa O(n) de memória) — pergunta deixada em aberto naquela fonte sobre se compensa a troca.

## Relação com outros conceitos

- [[wiki/concepts/algoritmos-de-busca]] — binary search é o exemplo mais comum de two pointer sobre array ordenado
- [[wiki/concepts/array]] — a técnica só funciona porque array garante acesso O(1) por índice
- [[wiki/concepts/recursao]] — two pointer é frequentemente escolhido como alternativa iterativa a uma versão recursiva mais cara em espaço
- [[wiki/concepts/time-space-tradeoff]] — troca recursão (espaço extra por chamada/cópia) por iteração com dois índices (espaço O(1))

## Key sources

- [[wiki/sources/binary-search-em-5-minutos]] — implementação completa de binary search com two pointers, contrastada explicitamente com a alternativa recursiva de recriar arrays
- [[wiki/sources/two-sum-explicacao]] — menção de two pointers como variante O(n) sem espaço extra para Two Sum em array ordenado
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — Reverse Only Letters: dois ponteiros com movimento independente por condição local, não por regra geométrica fixa
