---
type: concept
title: "Complexidade Computacional"
aliases: ["computational complexity", "complexidade de tempo", "complexidade de espaço", "teoria da complexidade"]
date_created: 2026-08-07
date_updated: 2026-08-07
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, complexidade-computacional, big-o, tempo, espaco]
skill: cs-fundamentals
status: stub
---

# Complexidade Computacional

Área da teoria da computação que estuda a **eficiência dos algoritmos** em termos de duas medidas finitas: **tempo** (quanto o algoritmo leva para terminar) e **espaço** (quanta memória usa durante a execução). São finitas porque não temos tempo infinito nem memória infinita — daí a necessidade de medi-las.

## Por que o programador se importa

A complexidade computacional é inerente à profissão, ainda que invisível: acompanha todo algoritmo escrito ao longo da carreira. Há uma classe de problemas que **não** se resolve em tempo/recursos viáveis — quer porque o tempo explode, quer porque a memória necessária é impraticável. Reconhecer que se está diante de um problema desses e adotar uma **solução razoável** (não perfeita, mas suficiente para entregar o produto) é uma habilidade central de quem resolve problemas.

## Medindo com Big O

A ferramenta canônica é a [[wiki/concepts/big-o|notação Big O]], que descreve o **comportamento assintótico** — como o custo cresce quando o tamanho da entrada tende ao infinito. Ela substitui a medida em segundos (instável: varia com máquina, processos concorrentes e ambiente) por uma classe de crescimento independente dessas variáveis. Exemplos contrastados pela fonte:

| Notação | Entrada 1 | Entrada 100 | Entrada 1.000 |
|---|---|---|---|
| O(n) linear | 1 | 100 | 1.000 |
| O(n²) quadrática | 1 | 10.000 | 1.000.000 |
| O(2ⁿ) exponencial | 2 | 2¹⁰⁰ (para n=100) | — |

A exponencial dobra o custo a cada `+1` na entrada — para n=100 já é `2¹⁰⁰`, um número inviável de aguardar.

## Ligação com determinismo

As classes formais de complexidade nascem da distinção [[wiki/concepts/determinismo-vs-nao-determinismo|determinismo vs. não-determinismo]]: há problemas que só seriam resolvidos em tempo razoável por uma máquina de Turing **não-determinística**. Essa é a intuição por trás de P vs NP (a fonte não nomeia as classes formalmente). `[skill: cs-fundamentals — references/computation-theory.md]`

## Aplicação: por que a criptografia é segura

A segurança da criptografia moderna se apoia justamente na inviabilidade da complexidade exponencial. Quebrar um hash por força bruta exige percorrer o espaço de chaves; conforme a chave cresce (mais caracteres, incluindo letras, números, especiais, maiúsculas e minúsculas), esse espaço — o tamanho da entrada do algoritmo de quebra — cresce, e o tempo dispara exponencialmente. Por isso é praticamente impossível descriptografar sem a chave, mesmo com hardware avançado. Ver [[wiki/concepts/criptografia]].

> Nota de precisão: "quebrar criptografia é O(2ⁿ)" é uma generalização didática. A dureza real depende do algoritmo (fatoração/logaritmo discreto na assimétrica, busca de chave na simétrica) e não é *provada* exponencial em todos os casos. `[skill: cs-fundamentals]`

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação usada para expressar complexidade de tempo e espaço
- [[wiki/concepts/determinismo-vs-nao-determinismo]] — a origem das classes P e NP
- [[wiki/concepts/maquina-de-turing]] — o modelo em que tempo e espaço são formalmente definidos
- [[wiki/concepts/time-space-tradeoff]] — trocar mais espaço por menos tempo (e vice-versa) é decisão recorrente
- [[wiki/concepts/criptografia]] — aplicação prática: dificuldade computacional como garantia de segurança

## Key sources

- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — complexidade como estudo de tempo e espaço; Big O como comportamento assintótico; conexão exponencial ↔ criptografia
