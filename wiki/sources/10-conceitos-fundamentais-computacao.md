---
type: source
title: "10 Conceitos Fundamentais da Computação"
aliases: ["10 fundamentos da computação", "10 ideias fundamentais CS"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 0
tags: [cs-fundamentals, algoritmos, estruturas-de-dados, big-o, recursao, concorrencia, compiladores, redes, banco-de-dados, criptografia, abstracao]
skill: cs-fundamentals
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/10-conceitos-fundamentais-computacao.md
source_url:
author: desconhecido (canal de vídeo)
date_published:
date_ingested: 2026-06-26
---

# 10 Conceitos Fundamentais da Computação

## TL;DR

Transcrição de vídeo que apresenta os 10 conceitos base de toda a computação — do binário à abstração — em ordem crescente de importância. O argumento central: linguagens e frameworks mudam, mas esses 10 conceitos não. Quem os entende reconhece padrões em qualquer tecnologia nova.

## Key Claims

1. **Tudo é binário** — texto, imagem, som são sequências de 0s e 1s manipulados por AND, OR, NOT. As três operações combinadas constroem qualquer circuito.
2. **A escolha da estrutura de dados muda tudo** — o mesmo conjunto de 1000 nomes requer 1000 comparações em lista, 10 numa BST, 1 numa hash table.
3. **Big O é a linguagem do desempenho** — O(n!) com 20 elementos supera qualquer computador; O(log n) com 1 bilhão de elementos precisa de apenas 30 passos.
4. **Recursão divide problemas sem solução direta** — toda função recursiva precisa de caso base (parar) e caso recursivo (dividir).
5. **Concorrência ≠ Paralelismo** — um cozinheiro pode ser concorrente mas nunca paralelo sozinho; race conditions aparecem quando threads compartilham estado.
6. **Compiladores abstraem a tradução** — lexer → parser → AST → otimizador → código de máquina. Compilado é mais rápido, interpretado é mais flexível.
7. **Redes são camadas de abstração** — HTTP diz o que, TCP garante entrega, IP define rota, física transmite bits.
8. **Bancos de dados garantem ACID** — atomicidade é o que evita que o dinheiro suma; índices fazem a diferença entre 1s e 1ms.
9. **Criptografia protege dados em três formas** — hashing irreversível, simétrica (mesma chave), assimétrica (chave pública + privada). HTTPS usa assimétrica no handshake.
10. **Abstração é o meta-conceito** — cada um dos nove anteriores é uma camada que esconde a complexidade da camada abaixo.

## Entidades Mencionadas

- Problema do Caixeiro Viajante (NP-hard, O(n!))
- HTTPS / TLS (criptografia assimétrica na web)

## Conceitos Tocados

- [[logica-booleana]]
- [[lista-encadeada]]
- [[arvore]]
- [[array]]
- [[hashmap]]
- [[big-o]]
- [[recursao]]
- [[concorrencia]]
- [[paralelismo]]
- [[race-condition]]
- [[compilador]]
- [[protocolo-de-rede]]
- [[acid]]
- [[criptografia]]
- [[abstracao]]
- [[deadlock]]
- [[mutex]]
- [[thread]]

## Open Questions

- A fonte não cita autores ou referências — os conceitos são apresentados de forma didática mas sem rigor acadêmico formal.
- "Busca binária requer apenas 30 comparações para 1 bilhão de elementos" — correto: log₂(10⁹) ≈ 30. Confirmado.

## Raw Quotes

> "Cada camada esconde a complexidade da anterior. As estruturas de dados abstraem como a memória organiza bits. Compiladores abstraem a tradução para código de máquina. Banco de dados abstraem a persistência em disco."

> "Com apenas 20 elementos o número de operações passa de dois quintilhões — mais do que qualquer computador do mundo consegue processar."

> "Sem abstração, cada programa precisaria lidar com tudo do transistor até o pixel."
