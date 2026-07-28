---
type: source
title: "Ponteiros em C++, Go e C# — Stack, Heap e Smart Pointers"
aliases: ["ponteiros cpp go csharp", "ponteiros de verdade", "stack heap raii video"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ponteiros-cpp-go-csharp.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [cpp, go, csharp, ponteiros, stack, heap, raii, smart-pointers, gerenciamento-de-memoria, undefined-behavior]
skill: lang-systems
status: stable
---

## TL;DR

Vídeo didático comparando ponteiros em três linguagens para descer "o nível" até a memória de verdade: C++ dá endereço cru e deixa o programador quebrar o programa; Go usa a mesma sintaxe de ponteiro (`&`, `*`) mas protege com escape analysis + garbage collector; C# esconde tudo atrás de referências gerenciadas (reference types). O núcleo técnico é o bug clássico de retornar endereço de variável local — undefined behavior em C++, mas resolvido automaticamente em Go (a variável escapa para a heap) e inexistente em C# (reference types já vivem na heap). Termina em C++ moderno: RAII e `unique_ptr`/`std::move` eliminam a maior parte do `new`/`delete` manual e dos memory leaks por caminho de saída não previsto.

## Key Claims

**Claim:** Um ponteiro é uma variável cujo dado armazenado é o endereço de outra variável — mesmo conceito em C++ e Go, com sintaxe idêntica (`&var` pega endereço, `*ptr` dereferencia).
**Evidence:** Exemplo do vídeo em ambas as linguagens: `idade := 25; ptr := &idade` — imprimir `idade` dá 25, imprimir `ptr` dá o endereço, imprimir `*ptr` dá 25 de novo; escrever em `*ptr = 30` muda `idade` para 30 nas duas linguagens, porque é o mesmo endereço de memória.
**Confidence:** alta

**Claim:** Retornar o endereço de uma variável local (que vive na stack) causa *undefined behavior* em C++, mas o mesmo padrão de código funciona corretamente em Go graças a **escape analysis**.
**Evidence:** Função `criarValor()` que cria `int valor = 42` na stack e retorna `&valor`: em C++ a stack daquele frame já foi liberada quando a função retorna, e o ponteiro aponta para memória inválida (resultado imprevisível — pode ler 42, lixo, ou dar segfault; o compilador emite warning mas compila e roda mesmo assim). O compilador de Go detecta que a variável "escapa" da função e a aloca na heap em vez da stack automaticamente, então o endereço continua válido depois que a função termina.
**Confidence:** alta — comportamento de escape analysis em Go e undefined behavior em C++ são fatos bem estabelecidos da linguagem, consistentes com [skill: lang-systems / references/c-cpp.md e go-production-patterns.md]

**Claim:** Em C#, esse mesmo bug de ponteiro "não existe no uso normal" porque *reference types* (classes, arrays) já vivem na heap por padrão, e o garbage collector só libera quando não há mais referência apontando para o objeto.
**Evidence:** Exemplo: classe `Pessoa` com propriedade `Idade`, passada por referência para um método `Modificar` que muda `Idade` para 30 — a mudança é visível de volta no chamador porque não houve cópia, foi passada a referência ao mesmo objeto. C# permite ponteiros reais via `unsafe`, mas isso é descrito como raramente usado no dia a dia.
**Confidence:** alta

**Claim:** C++ moderno resolve a maior parte do gerenciamento manual de memória (`new`/`delete`) com o padrão RAII, principalmente via `std::unique_ptr` — sem precisar de `delete` explícito, mesmo em código com múltiplos caminhos de saída (early return, exceção).
**Evidence:** Exemplo com `std::make_unique<int>(42)` — destruído automaticamente ao sair de escopo, sem `delete` em lugar nenhum. Contraste explícito com o caso de `new int[1000]` sem RAII: se uma exceção ou `return` antecipado ocorre antes do `delete[]`, aquele bloco de heap nunca é liberado (*memory leak*). `std::move` transfere a *ownership* de um `unique_ptr` para outro, deixando o ponteiro original `nullptr`.
**Confidence:** alta — padrão RAII e API de `unique_ptr`/`make_unique`/`std::move` batem com [skill: lang-systems / references/c-cpp.md]

**Claim:** Stack e heap não são exclusivos de C++ — Go e C# também separam memória entre os dois; a diferença entre linguagens está em quem decide onde alocar e quem libera a heap depois.
**Evidence:** Tabela do vídeo: em C++ o programador decide e libera manualmente (ou via smart pointer); em Go o compilador decide via escape analysis e o GC libera; em C# a regra é fixa (value types → stack, reference types → heap) e o GC libera.
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/ponteiros-cpp-stack-heap-raii]]
- [[wiki/concepts/gerenciamento-de-memoria]]
- [[wiki/concepts/rust-ownership-borrowing-lifetimes]]
- [[wiki/concepts/go-fundamentos]]
- [[wiki/concepts/lista-encadeada]]
- [[wiki/concepts/sistema-de-tipos]]
- [[wiki/concepts/compilador]]

## Open Questions

- O vídeo não cobre `shared_ptr`/`weak_ptr` em profundidade (menciona só de passagem em outras fontes da skill) — reference counting e ciclos de referência ficam para uma fonte futura sobre C++ avançado.
- Não é discutido como `unsafe` em C# de fato expõe ponteiros brutos (sintaxe, `fixed`, `stackalloc`) — fonte futura se o tema aparecer com mais profundidade.
- O vídeo não aprofunda o algoritmo de escape analysis do compilador Go (quais heurísticas decidem stack vs. heap) — tratado aqui só no nível de comportamento observável.
