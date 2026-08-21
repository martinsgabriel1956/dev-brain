---
type: source
title: "Recursão em JavaScript: Fatorial e Fibonacci"
aliases: ["recursão vs iteração", "função recursiva javascript", "fatorial recursivo", "fibonacci recursivo", "caso base e chamada recursiva"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 0
tags: [cs-fundamentals, javascript, recursao, algoritmos, call-stack, fibonacci, fatorial]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/recursao-fatorial-fibonacci-javascript.md
source_url:
author: desconhecido (canal de vídeo)
date_published:
date_ingested: 2026-08-18
---

# Recursão em JavaScript: Fatorial e Fibonacci

## TL;DR

Introdução didática a recursão em JavaScript: contrasta função iterativa (`for`) com recursiva (chamada a si mesma) usando dois exemplos clássicos — fatorial e Fibonacci — implementados nas duas formas. Explica caso base e chamada recursiva como as duas partes obrigatórias de toda recursão, traça o desenrolar da call stack passo a passo para ambos os exemplos, e fecha com o trade-off: recursão é geralmente mais lenta e consome mais memória, mas pode ser mais simples de escrever/ler.

## Key Claims

**Claim:** Função iterativa usa loop (`for`/`while`) para repetir instruções até uma condição de parada; função recursiva chama a si mesma até uma condição ser atendida, dividindo o problema em subproblemas menores e depois combinando os resultados.
**Evidence:** Comparação direta entre as duas implementações de fatorial — a iterativa acumula em `resultado` dentro de um `for`; a recursiva retorna `n * fatorial(n - 1)` até o caso base.
**Confidence:** alta

**Claim:** Toda função recursiva precisa obrigatoriamente de duas partes: caso base (condição de parada) e chamada recursiva (onde a função invoca a si mesma reduzindo o problema).
**Evidence:** Sem caso base, a recursão entraria em loop infinito. No fatorial recursivo, `n === 0 || n === 1` é o caso base; `n * fatorial(n - 1)` é a chamada recursiva. Na Fibonacci recursiva, `p === 1` e `p === 2` são os dois casos base (retornam 0 e 1, os dois primeiros termos da sequência); `fibonacci(p - 1) + fibonacci(p - 2)` é a chamada recursiva.
**Confidence:** alta

**Claim:** O desenrolar de uma recursão acontece "de trás para frente" — as chamadas ficam pendentes na memória até a chamada mais profunda (caso base) retornar, e então cada nível pendente se resolve na ordem inversa em que foi empilhado.
**Evidence:** Trace completo de `fatorial(5)`: a cadeia de chamadas desce até `fatorial(1) → 1`, e então cada nível pendente resolve na volta — `2×1=2 → 3×2=6 → 4×6=24 → 5×24=120`. Mesmo padrão traçado para `fibonacci(3)` e generalizado para `fibonacci(5) → 3`.
**Confidence:** alta

**Claim:** Recursão em geral é mais lenta e consome mais memória que iteração (porque cria múltiplas cópias/frames da função), mas pode simplificar a legibilidade do problema em troca dessa performance.
**Evidence:** Conclusão explícita da fonte: "as funções iterativas são mais eficientes, porém mais complexas, e as funções recursivas em geral são mais lentas, porém mais simples de escrever." Não quantifica (sem Big-O explícito) — afirmação qualitativa.
**Confidence:** média — a fonte não distingue recursão ingênua exponencial (Fibonacci sem memoização, O(2ⁿ)) de recursão linear (fatorial, O(n)); trata "recursão" como uma categoria única mais lenta, o que é impreciso — ver [[wiki/concepts/recursao]] e [[wiki/concepts/programacao-dinamica]] para a distinção real de complexidade.

## Entities & Concepts Touched

- [[wiki/concepts/recursao]]
- [[wiki/concepts/programacao-dinamica]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/pilha]]

## Open Questions

- A fonte não menciona que a Fibonacci recursiva ingênua é O(2ⁿ) (recomputação de subárvores repetidas) nem apresenta memoização como solução — fica implícito que "recursão = mais lenta" sem diferenciar recursão linear (fatorial) de recursão em árvore exponencial (Fibonacci). Ver [[wiki/concepts/programacao-dinamica]] para o tratamento correto dessa distinção.
- Não aborda tail call optimization nem o fato de o JavaScript não garantir TCO (V8 nunca implementou apesar de estar na spec ES2015) — ponto já registrado em [[wiki/concepts/recursao]].

## Raw Quotes

> "É como se você tivesse um sonho dentro de um sonho, ou como uma boneca russa, onde você precisa abrir todas as bonecas uma dentro da outra até chegar na menor de todas — e depois faz a mesma coisa de trás para frente para voltar elas ao formato original."

> "É como se você quisesse pegar água de um poço. Você começa com um balde na superfície e tem que baixar ele até o fundo do poço [...]. Lá no fundo você pega a água — que nesse caso seria o caso base da função recursiva — e então você traz o balde para cima de novo [...] até que o balde retorna cheio de água, ou seja, com o resultado esperado."
