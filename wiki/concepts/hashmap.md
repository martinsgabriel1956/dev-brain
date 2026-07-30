---
type: concept
title: "Hashmap"
aliases: ["hash map", "hash table", "dicionário", "mapa", "dictionary"]
date_created: 2026-06-01
date_updated: 2026-07-29
source_count: 4
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

## Relação com Sistemas Reais

- **Caches** (Redis): chave → valor, O(1)
- **Índices de banco de dados**: hash index para equality lookups
- **DNS**: hostname → IP address
- **Variáveis de ambiente**: nome → valor

## Relação com outros conceitos

- [[array]] — alternativa quando acesso por posição é suficiente
- [[arvore]] — alternativa para buscas ordenadas e por intervalo
- [[wiki/concepts/time-space-tradeoff]] — hashmap é o exemplo canônico de trocar memória por velocidade de busca

## Key sources

- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — exemplo do trade-off tempo/memória: índice por e-mail (hashmap) troca espaço extra por busca O(1) em vez de O(n) numa lista
- [[wiki/sources/indice-de-banco-de-dados]] — índice hash de banco de dados como aplicação direta de hashmap: match exato O(1), sem suporte a range/ordenação/prefixo
