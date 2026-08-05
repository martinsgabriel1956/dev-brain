---
type: source
title: "Binary Search em 5 Minutos"
aliases: ["binary search", "busca binária leetcode", "two pointer binary search"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 0
tags: [cs-fundamentals, algoritmos, busca, binary-search, two-pointer, big-o, leetcode]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/binary-search-em-5-minutos.md
source_url:
author: desconhecido (canal com curso próprio de estruturas de dados e algoritmos)
date_published:
date_ingested: 2026-08-04
---

# Binary Search em 5 Minutos

## TL;DR

Vídeo curto explicando [[wiki/concepts/algoritmos-de-busca|binary search]] do zero até resolver o problema no LeetCode em menos de cinco minutos. Percurso didático: por que busca linear é O(n), por que binary search exige array ordenado e chega em O(log n), e por que a implementação real usa **two pointers** (`left`/`right`) em vez de recriar sub-arrays recursivamente a cada chamada — evitando o custo computacional de alocar um novo array a cada nível de recursão. Fecha com a implementação completa em Python e a regra de convenção do LeetCode de retornar `-1` quando o elemento não é encontrado.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Binary search só funciona em array ordenado | "a gente só consegue isso porque esse array sempre está ordenado. Se ele não estiver ordenado, o binary search não funciona" | Alta |
| Binary search é O(log n) contra O(n) da busca linear | Exemplo comparativo no mesmo array: busca linear pelo item 9 percorre 5 posições (-1, 0, 3, 5, 9); binary search encontra o mesmo item em 2 passos (olha o meio, corta a metade, olha o novo meio) | Alta |
| Recriar arrays recursivamente a cada chamada é computacionalmente caro — daí a implementação com two pointers | "como criar e recriar array recursivamente ia ser muito computacionalmente caro, existe uma implementação com basicamente two pointer para fazer binary search" | Alta — é a motivação explícita dada para a escolha de implementação, embora sem quantificar o custo (implicitamente: espaço extra O(n) por chamada recursiva com slicing, contra O(1) de espaço extra da versão iterativa com ponteiros) |
| O ponto médio é sempre `(left + right) // 2`, com cuidado de overflow em linguagens que não são Python | "se não for Python você tem que tomar cuidado com o overflow" — mesmo cuidado documentado na forma `lo + Math.floor((hi - lo) / 2)` no material de referência da skill | Alta |
| Convenção do LeetCode é retornar -1 quando o elemento não está no array | "por default o LeetCode quer que a gente retorne o -1" | Alta |

## Pseudocódigo central (two pointers)

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

## Entidades Mencionadas

- [[wiki/entities/leetcode]] — plataforma onde a solução foi validada ao vivo

## Conceitos Tocados

- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/two-pointer]]
- [[wiki/concepts/recursao]]
- [[wiki/concepts/array]]
- [[wiki/concepts/entrevista-tecnica-coding]]

## Open Questions

- A fonte não discute variantes (`lower_bound`/`upper_bound`) nem aplicação de binary search fora de arrays (ex: busca em espaço de decisão monotônico) — ver `references/algorithms-complexity.md` da skill `cs-fundamentals`, que cobre essas variantes e a aplicação arquitetural (ex: encontrar o menor rate limit que não degrada SLA via binary search no espaço de valores).
- Não há discussão de por que `(left + right) // 2` pode estourar em linguagens com inteiro de tamanho fixo (a fonte só alerta "tome cuidado"), nem a forma alternativa mais segura `left + (right - left) // 2` — lacuna coberta por `references/algorithms-complexity.md`, marcada aqui como `[skill: cs-fundamentals]`.

## Raw Quotes

> "A gente só consegue isso porque esse array sempre está ordenado. Se ele não estiver ordenado, o binary search não funciona."

> "Como criar e recriar array recursivamente ia ser muito computacionalmente caro, existe uma implementação com basicamente two pointer para fazer binary search."

> "A gente efetivamente encontrou ele em dois passos só, em log de n, ao invés de n — não precisou percorrer tudo."
