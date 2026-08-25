---
type: source
title: "Busca Binária: Encontrando a Posição de um Protocolo numa Fila Ordenada (Live Coding)"
aliases: ["busca binária protocolos de atendimento", "busca binária entendendo algoritmos", "binary search fila ordenada"]
date_created: 2026-08-25
date_updated: 2026-08-25
source_count: 0
tags: [cs-fundamentals, algoritmos, busca, binary-search, big-o, logaritmo]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/busca-binaria-fila-protocolos-atendimento-live-coding.md
source_url:
author: canal de cortes de "Fernanda Kiperdev" (live coding, com leitura do livro Entendendo Algoritmos)
date_published:
date_ingested: 2026-08-25
---

# Busca Binária: Encontrando a Posição de um Protocolo numa Fila Ordenada (Live Coding)

## TL;DR

Corte de live coding que introduz [[wiki/concepts/algoritmos-de-busca|busca binária]] por dois caminhos combinados: (1) um exercício ao vivo com o chat — encontrar a posição de um protocolo de atendimento numa fila ordenada de até 1 milhão de itens, resolvido manualmente passo a passo descartando metade da lista a cada comparação — e (2) a leitura direta de trechos do livro *Entendendo Algoritmos*, incluindo a analogia de "adivinhar um número de 1 a 100 com o menor número de tentativas" e o exemplo do dicionário de 240.000 palavras (18 etapas via busca binária vs. até 239.999 via força bruta). Fecha com a fórmula geral log₂(n) e uma pergunta do chat sobre por que a metade descartada nunca pode conter a resposta — respondida pela pré-condição de lista ordenada.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Busca binária só é válida em lista ordenada; sem essa pré-condição, "toda a lógica cairia por terra" | "porque a lista está ordenada... se ela não tivesse ordenada, toda essa lógica cairia por terra" | Alta |
| A posição do elemento é sempre contada a partir do índice zero da lista | "uma lista sempre começa no índice zero... se uma lista tem 100 números, os índices vão de zero a 99" | Alta |
| A eficiência do algoritmo só importa na prática com listas grandes (milhares a milhões de itens) | "com cinco elementos, dez elementos, isso aí é irrisório... o problema mesmo vai ser quando eu tiver lidando com milhares, centenas ou milhões de dados" | Alta |
| Busca linear/brute force (`pesquisa simples` / `pesquisa estúpida`) elimina apenas um elemento por tentativa | "a cada tentativa você está eliminando apenas um número. Se o meu número fosse o 99, você precisaria de 99 chances para acertar" | Alta |
| Busca binária elimina metade dos elementos restantes a cada tentativa, sempre testando o elemento do meio | "a cada próximo chute eu vou eliminando metade dos elementos restantes, porque eu sempre vou chutando o número do meio" | Alta |
| Com 100 itens, o pior caso da busca binária é resolvido em 7 etapas | "com 100 itens... seja qual for o número que eu estiver pensando, você pode adivinhá-lo em um máximo de sete tentativas" | Alta |
| Num dicionário de 240.000 palavras, busca binária resolve em no máximo 18 etapas vs. até 239.999 no brute force | "usando o algoritmo de pesquisa binária é levar a 18 etapas" | Alta |
| A complexidade da busca binária é log₂(n); a busca simples é O(n) | "para uma lista de n números, a pesquisa binária precisa de log de 2 na n... enquanto a pesquisa simples precisaria de n etapas" | Alta |
| Se a lista não estiver ordenada, é preciso ordená-la primeiro (ou usar outro algoritmo) antes de aplicar busca binária | "eu posso primeiro ordenar essa lista, colocá-la em ordem, e depois usar a busca binária, ou eu posso usar outros algoritmos de busca" | Alta |
| Retorno "não encontrado" (nil) ocorre quando a lista restante fica com zero elementos | "eu fico com uma lista com zero elementos... e aí eu sei que o 1013 não tá nessa lista, e retorno nil" | Alta |

## Trace passo a passo (fila de protocolos 1001–1038, busca por 1024)

1. Meio = 1019. `1019 < 1024` → descarta metade inferior (tudo ≤ 1019).
2. Resta {1024, 1030, 1038}. Meio = 1030. `1030 > 1024` → descarta metade superior.
3. Resta {1024}. Meio = 1024. `1024 == 1024` → encontrado.

O mesmo trace é repetido na fonte para 1008 (2 etapas), 1012 (3 etapas) e para o caso de ausência, 1013 (3 etapas até a lista restante ficar vazia e retornar "não encontrado").

## Entidades Mencionadas

- [[wiki/entities/fernanda-kipper]] — canal principal de onde o corte foi extraído ("Fernanda Kiperdev"), com live coding quinzenal (2º e 4º domingo do mês)
- *Entendendo Algoritmos* (livro, tradução PT-BR de *Grokking Algorithms*, Aditya Bhargava) — citado extensamente com leitura direta de trechos; ver [[wiki/concepts/livros-recomendados-programador]]
- Facebook — citado no livro como exemplo real de busca binária em nome de usuário num banco de dados

## Conceitos Tocados

- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/logaritmo]]
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]]
- [[wiki/concepts/algoritmos-de-ordenacao]]
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- [[wiki/concepts/array]]
- [[wiki/concepts/livros-recomendados-programador]]

## Open Questions

- A fonte não formaliza o pseudocódigo/implementação (nenhum código é escrito na tela neste corte) — é um exercício conceitual de mesa, complementado pela implementação real já coberta em [[wiki/sources/busca-linear-e-binaria-giovana]] e [[wiki/sources/binary-search-em-5-minutos]].
- Não menciona overflow de índice (`(first + last) / 2`) nem a técnica [[wiki/concepts/two-pointer]] pelo nome — só descreve "guardar a cabeça da lista" para saber o índice, informalmente equivalente ao ponteiro `first`/`left`.
- O exemplo do Facebook citado no livro (buscar `kalmcdaggon` pelos "Ms") pressupõe uma lista ordenada alfabeticamente de usernames — simplificação didática, já que sistemas reais usam índice de banco de dados (hash/B-tree), não busca binária em array plano.

## Raw Quotes

> "Se ela não tivesse ordenada, toda essa lógica cairia por terra. Se a lista tá desordenada, daí eu tenho outro problema — daí eu poderia primeiro ordenar a lista, por exemplo, e depois encontrar."

> "O problema de eu ficar tentando um por um, que é o brute force... é que eu vou testar várias vezes, isso vai levar tempo. Quando eu uso um algoritmo como a busca binária, eu consigo ir reduzindo significativamente esse tempo."

> "Para uma lista de n números... a pesquisa binária precisa de log de 2 na n para retornar o valor correto... enquanto a pesquisa simples precisaria de n etapas."

> "Não tem como o número estar na metade retirada. Esse algoritmo só se aplica para quando a lista tiver ordenada."
