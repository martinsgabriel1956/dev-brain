---
type: concept
title: "Hashmap"
aliases: ["hash map", "hash table", "dicionário", "mapa", "dictionary"]
date_created: 2026-06-01
date_updated: 2026-08-27
source_count: 7
tags: [cs-fundamentals, estruturas-de-dados, hashmap, performance, big-o]
skill: cs-fundamentals
status: draft
---

# Hashmap

Estrutura de dados que armazena pares **chave → valor**. O acesso é feito pela chave — que pode ser qualquer coisa: um e-mail, um ID, um nome, uma string arbitrária.

## Operações e Complexidade

| Operação | Complexidade média | Caso pior |
|---|---|---|
| Acesso por chave | **O(1)** | O(n) com muitas colisões |
| Inserção | O(1) | O(n) |
| Remoção | O(1) | O(n) |
| Verificar existência | **O(1)** | O(n) |

O caso pior ocorre em cenários de muitas colisões de hash — raro em implementações modernas com boas funções de hash.

## Por que é Mais Rápido que Array para Busca

No [[array]], buscar um usuário pelo e-mail exige percorrer todos os elementos até encontrar:

```python
# Array — O(n): percorre todos
usuario = next(u for u in usuarios if u.email == "x@y.com")

# Hashmap — O(1): vai direto
usuario = usuarios_por_email["x@y.com"]
```

Com 10 registros, a diferença é imperceptível. Com 1 milhão, é brutal.

## Analogia

Um dicionário físico. Você não lê página por página — vai direto à letra e busca a palavra.

## Quando Usar

- Busca por identificador (ID, e-mail, nome, código)
- Verificar se algo existe rapidamente
- Associar uma chave a um valor (cache, lookup tables)
- Contagem de frequência (chave → contador)

## Quando Não Usar

- A ordem dos elementos importa (hashmap não garante ordem)
- Você precisa de intervalos de valores (ex.: todos os IDs entre 100 e 200) — use [[arvore]] ou array ordenado
- Você precisa iterar em ordem de inserção (use linked hashmap ou array)

## Hash Set: membership check sem valor associado

Um **set** é a mesma estrutura por baixo (hash table), mas guarda só a chave, sem valor associado — usado para checar rapidamente "esse elemento já existe?" (`x in set`) em O(1), em vez de armazenar dados por chave. Documentado em [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]]: transformar um array num set custa O(n) (percorrer uma vez, inserir cada elemento em O(1)) e permite checar existência de qualquer elemento em O(1) — mais barato que ordenar (O(n log n)) quando o objetivo é só saber "esse valor está presente?", sem precisar de ordem.

## Relação com Sistemas Reais

- **Caches** (Redis): chave → valor, O(1)
- **Índices de banco de dados**: hash index para equality lookups
- **DNS**: hostname → IP address
- **Variáveis de ambiente**: nome → valor

## Relação com outros conceitos

- [[array]] — alternativa quando acesso por posição é suficiente
- [[arvore]] — alternativa para buscas ordenadas e por intervalo
- [[wiki/concepts/time-space-tradeoff]] — hashmap é o exemplo canônico de trocar memória por velocidade de busca

## Heurística dos "Três Níveis de Profundidade"

[[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] usa `Map` como exemplo canônico de uma heurística de estudo: saber usar uma estrutura abstrata (nível 1 — "usei Map") não é o mesmo que saber qual implementação concreta a linguagem usa por baixo (nível 2 — "é uma hash table"), nem entender como essa implementação resolve seus próprios problemas internos (nível 3 — "como ela resolve colisão de hash", ver [[wiki/concepts/hashing]]). A fonte argumenta que esse aprofundamento continua justificando prática de LeetCode/estruturas de dados mesmo numa era em que a IA gera a implementação — o conhecimento de nível 2-3 é o que permite avaliar/depurar o código gerado, não só usá-lo.

## Key sources

- [[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] — heurística dos três níveis de profundidade (Map → hash table → resolução de colisão de hash)
- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — exemplo do trade-off tempo/memória: índice por e-mail (hashmap) troca espaço extra por busca O(1) em vez de O(n) numa lista
- [[wiki/sources/indice-de-banco-de-dados]] — índice hash de banco de dados como aplicação direta de hashmap: match exato O(1), sem suporte a range/ordenação/prefixo
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — hash set para membership check O(1) (Longest Consecutive Sequence) e hash map de frequências como pré-passo de [[wiki/concepts/bucket-sort]] (Top K Frequent Elements); citação de dictionary/hashmap como a estrutura mais usada no dia a dia de programação, mais que árvore binária
- [[wiki/sources/como-ficar-bom-em-leetcode]] — hash map como padrão que "resolve quase tudo"; entre os primeiros a treinar depois de two pointer
