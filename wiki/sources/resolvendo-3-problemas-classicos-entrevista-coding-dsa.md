---
type: source
title: "Resolvendo 3 dos problemas mais populares de entrevista de coding (Estruturas de Dados e Algoritmos)"
aliases: ["longest consecutive sequence", "top k frequent elements", "reverse only letters", "3 problemas de entrevista de coding"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 0
tags: [entrevista-tecnica, coding-interview, algoritmos, hashmap, array, big-o, two-pointer, leetcode]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/resolvendo-3-problemas-classicos-entrevista-coding-dsa.md
source_url: ""
author: "não identificado no vídeo (indício de autoria: cupom de patrocínio \"Augusto 20\")"
date_published: ""
date_ingested: 2026-08-04
---

# Resolvendo 3 dos problemas mais populares de entrevista de coding (Estruturas de Dados e Algoritmos)

## TL;DR

Vídeo em português resolvendo três problemas clássicos de [[wiki/concepts/entrevista-tecnica-coding|entrevista técnica de coding]] estilo LeetCode: **Longest Consecutive Sequence** (array + hash set, O(n) contra O(n log n) de uma solução por ordenação), **Top K Frequent Elements** (hash map + bucket sort por frequência, O(n) contra O(n log n) de ordenar o mapa) e **Reverse Only Letters** (two pointers, O(n)). A tese central do vídeo não é a resposta certa em si, mas o raciocínio: cada problema é resolvido em pelo menos duas versões (uma boa, uma ótima), com justificativa explícita de por que a solução ótima vence — o valor de entrevista está em demonstrar domínio de array, hash map/set, algoritmos de ordenação e [[wiki/concepts/big-o|Big O]] notation, não em decorar a resposta.

## Key Claims

- **Ordenar um array nunca é "de graça" computacionalmente**: uma solução que parece O(n) porque só percorre o array ordenado uma vez, na verdade é O(n log n) no total, porque a transformação prévia (`sort()`) já custa O(n log n) — o algoritmo de ordenação interno (quicksort, mergesort, timsort) domina a complexidade total, mesmo que a pessoa candidata não lembre o nome exato do algoritmo usado internamente pela linguagem. → [[wiki/concepts/algoritmos-de-ordenacao]], [[wiki/concepts/big-o]]
- **Busca em [[wiki/concepts/hashmap|hash set]] é O(1) independente do tamanho do set** — 1 elemento ou 1 milhão de elementos custam o mesmo para checar membership — e transformar um array num set custa O(n), mais barato que ordenar (O(n log n)) para arrays de tamanho relevante.
- **A sacada central de Longest Consecutive Sequence**: só vale a pena expandir uma sequência a partir do elemento que é seu **início** (`x` é início se `x - 1` não está no set) — checar a partir de elementos no meio da sequência é trabalho redundante. Isso transforma o algoritmo em O(n) total mesmo repetindo buscas no set durante a expansão, porque cada elemento só é "gasto" computando a sequência que o contém uma única vez ao longo de toda a execução. → [[wiki/concepts/time-space-tradeoff]]
- **Bucket sort por frequência evita ordenar o mapa de frequências em Top K Frequent Elements**: como o tamanho do array (`n`) é o teto absoluto de quantas vezes qualquer elemento pode se repetir, um array de `n + 1` "baldes" indexados pela frequência permite posicionar cada elemento em O(1) (a posição já é conhecida: a própria frequência) — efetivamente uma ordenação sem custo de comparação, resultando em O(n) total em vez de O(n log n) via `sort()`. → [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- **Constantes são descartadas em Big O**: uma solução que percorre o array três vezes (popular o mapa de frequências, inicializar buckets, popular buckets) é tecnicamente O(3n), mas em notação Big O isso se simplifica para O(n) — 1n, 2n, 20n ou 2 milhões de n, todos permanecem O(n). → [[wiki/concepts/big-o]]
- **Two pointers resolve Reverse Only Letters em O(n)**: dois ponteiros (início e fim da string) avançam/recuam de forma independente conforme o caractere na posição correspondente é ou não uma letra, trocando de posição apenas quando os dois apontam para letras, até se encontrarem. → [[wiki/concepts/two-pointer]]
- **O valor de entrevista de cada um dos três problemas está na demonstração de conhecimento, não na resposta**: Longest Consecutive Sequence exige array + hash set + sort + Big O; Top K Frequent Elements exige hash map/dictionary com "maestria" (a estrutura mais usada no dia a dia de programação, segundo o autor, mais do que árvore binária); Reverse Only Letters exige a técnica de two pointers. → [[wiki/concepts/entrevista-tecnica-coding]], [[wiki/concepts/reconhecimento-de-padroes]]

## Entities

[[wiki/entities/leetcode]] (plataforma referenciada e usada para validar as três soluções) · [[wiki/entities/augusto-galego]] (autoria não confirmada no vídeo — ver Open Questions)

## Concepts

[[wiki/concepts/algoritmos-e-estruturas-de-dados]] · [[wiki/concepts/array]] · [[wiki/concepts/hashmap]] · [[wiki/concepts/big-o]] · [[wiki/concepts/algoritmos-de-ordenacao]] · [[wiki/concepts/two-pointer]] · [[wiki/concepts/time-space-tradeoff]] · [[wiki/concepts/entrevista-tecnica-coding]] · [[wiki/concepts/reconhecimento-de-padroes]] · [[wiki/concepts/bucket-sort]]

## Implementações de Referência

**Longest Consecutive Sequence — O(n):**
```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in nums:
        if num - 1 not in num_set:
            current_num, current_streak = num, 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
```

**Top K Frequent Elements — O(n), bucket sort por frequência:**
```python
def top_k_frequent(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, freq in frequency_map.items():
        buckets[freq].append(num)

    result = []
    for frequency in range(n, 0, -1):
        for num in buckets[frequency]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

**Reverse Only Letters — O(n), two pointers:**
```python
def reverse_only_letters(s):
    s_list = list(s)
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
    return ''.join(s_list)
```

## Open Questions

- **Autoria não identificada no vídeo.** O único indício é o cupom de patrocínio repetido "Augusto 20" (serviço de câmbio/remessas internacionais), que sugere o nome do apresentador ser Augusto — coincidindo com [[wiki/entities/augusto-galego]], já documentado na wiki com conteúdo de carreira, system design e infraestrutura. Diferente de casos anteriores de autoria inferida desse mesmo autor (mesmo padrão de patrocínio HostGator, mesma política de reembolso do curso pago), aqui a única evidência é o nome no cupom de um patrocinador *diferente* (câmbio, não hosting) — sinal mais fraco que os usados nas inferências anteriores. Tratado como hipótese não confirmada, registrada em ambos os lados do link.
- **Se `n` (tamanho do array) fosse muito grande e a distribuição de frequências muito desigual**, o array de buckets de tamanho `n + 1` do Top K Frequent Elements aloca espaço O(n) mesmo que a maioria dos buckets fique vazia (ex.: um elemento que aparece `n` vezes e todos os outros aparecem 1 vez) — o vídeo não discute esse custo de espaço nem compara com a alternativa de heap de tamanho `k` (O(n log k)), citada como abordagem padrão em `references/data-structures.md` da skill `cs-fundamentals` para "top-k eficiente".
- **A afirmação "ordenar um array pequeno pode ser mais rápido que transformá-lo em set"** é mencionada de passagem, sem quantificação (não fica claro o limiar de tamanho onde a troca compensa) — tratada como intuição de constantes, não como claim verificável.

## Raw Quotes

> "Vamos primeiro ver como que a gente soluciona esse problema de qualquer jeito, do da primeira maneira que surgir na cabeça... essa solução é péssima, é porque a gente não sabe onde que os elementos estão."

> "A gente ordenar um array não é de graça — mas você precisa saber que essa transformação não é gratuita em termos computacionais."

> "Não faz sentido procurar o quatro se a gente já olhou a sequência 1, 2, 3, 4 — é uma computação desnecessária."

> "Ser um programador, a estrutura de dados dictionary/hashmap é uma das mais úteis no seu trabalho — eu acho que no meu emprego eu nunca usei uma árvore binária, mas dictionary eu uso provavelmente toda semana."

> "Não é odn, é n log n — porque sim, para ordenar um array... embora essa solução seja muito boa, tem uma melhor."

## Nota sobre skill carregada

Skill `cs-fundamentals` carregada de `/home/gabriel-martins/Documentos/skills/cs-fundamentals/SKILL.md` (o caminho apontado pelo `CLAUDE.md` do repositório, `/home/nemomartins/Documentos/new/skills/`, não existe neste ambiente — mesma situação já registrada em ingestões anteriores). Referências consultadas: `references/algorithms-complexity.md` (seção "Algoritmos de Ordenação" para confirmar as complexidades de quicksort/mergesort/timsort citadas no vídeo, e seção "Big-O" para a regra de descarte de constantes) e `references/data-structures.md` (seção "Hash Map / Hash Table" para o funcionamento de O(1) amortizado, e a tabela de decisão "Top-k / menor/maior eficiente → Heap", usada para registrar a comparação com a alternativa de heap não discutida na fonte).
