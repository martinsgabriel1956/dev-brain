---
type: concept
title: "Ponteiros, Stack/Heap e RAII (C++ vs. Go vs. C#)"
aliases: ["ponteiros c++", "stack vs heap", "raii", "unique_ptr", "dangling pointer", "escape analysis", "smart pointers"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [cpp, ponteiros, stack, heap, raii, smart-pointers, gerenciamento-de-memoria, go, csharp, undefined-behavior]
skill: lang-systems
status: draft
---

# Ponteiros, Stack/Heap e RAII (C++ vs. Go vs. C#)

Um ponteiro é uma variável cujo dado é o endereço de outra variável — `*ptr` dereferencia (lê/escreve no endereço apontado), `&var` pega o endereço. C++, Go e C# expõem o mesmo conceito de formas radicalmente diferentes: C++ dá acesso cru ao endereço sem rede de segurança; Go mantém a sintaxe de ponteiro (`&`, `*`) mas protege com garbage collector; C# esconde o endereço atrás de referências gerenciadas — só C# usa `unsafe` para chegar a ponteiro real, o que raramente acontece no dia a dia. Ver [[wiki/concepts/gerenciamento-de-memoria]] para as três estratégias de runtime (manual, GC, ownership) por trás dessa diferença.

## Stack vs. Heap

Toda variável mora em um de dois lugares:

- **Stack** — variáveis locais de uma função. Alocação e liberação são automáticas e ligadas ao escopo: a função termina, tudo que estava na stack desaparece. Rápida, espaço limitado.
- **Heap** — memória dinâmica, pedida explicitamente (`new` em C++, `make`/alocação implícita em Go, `new` em C#). Sobrevive ao fim da função que a criou. Mais espaço, mas alguém precisa liberar — e é exatamente esse "alguém" que muda de linguagem para linguagem.

| Linguagem | Quem decide stack vs. heap | Quem libera a heap |
|---|---|---|
| C++ | O programador escolhe (`new` = heap explícito) | O programador (`delete`) ou um smart pointer |
| Go | O compilador, via **escape analysis** | Garbage collector |
| C# | Regra fixa: value types → stack, reference types → heap | Garbage collector |

## O bug clássico: retornar endereço de variável local

Em C, o padrão mais comum de bug de ponteiro é retornar o endereço de uma variável que vive na stack de uma função:

```c
int* criar_valor() {
    int valor = 42; // stack
    return &valor;  // a stack desse frame já foi liberada quando a função retorna
}
```

Isso é **undefined behavior** em C/C++: o compilador não impede, geralmente emite um warning, mas compila e roda — o resultado de acessar aquele ponteiro depois é imprevisível (pode ler 42 por acidente, pode ler lixo, pode dar segfault).

O mesmo padrão de código em **Go não quebra**: o compilador detecta, via escape analysis, que o valor está "escapando" da função (o endereço dele sai do escopo onde foi criado) e realoca essa variável na heap automaticamente, em vez da stack. Em **C#**, como todo *reference type* já vive na heap por padrão, o garbage collector simplesmente não libera enquanto existir uma referência apontando para o objeto — o bug não existe na classe de erro, não porque alguém o preveniu manualmente.

## RAII e smart pointers em C++ moderno

C++ moderno resolve a maior parte do problema de gerenciamento manual (`new`/`delete`) com o padrão **RAII** (Resource Acquisition Is Initialization): um objeto adquire um recurso no construtor e libera no destrutor, e o destrutor é chamado automaticamente quando o objeto sai de escopo — vale para memória, arquivos, mutexes, conexões.

O principal smart pointer é `std::unique_ptr`:

```cpp
auto ptr = std::make_unique<int>(42);
// destruído automaticamente ao sair de escopo — sem delete

auto ptr2 = std::move(ptr); // transfere ownership; ptr vira nullptr
```

`unique_ptr` é o dono exclusivo do dado que aponta. Sem `delete` explícito, sem risco de esquecer, sem *memory leak* por caminho de saída não previsto (early return, exceção no meio da função). A transferência de posse é explícita via `std::move` — só o novo dono é responsável por liberar depois disso.

Esse design tem uma linha direta de influência sobre padrões de outras linguagens: RAII inspirou tanto o `defer` de Go quanto o modelo de *ownership* de Rust (ver [[wiki/concepts/rust-ownership-borrowing-lifetimes]]) — a ideia central de "liberação atrelada ao fim do escopo, não a uma chamada manual em algum lugar do meio do código" é a mesma, só que Rust formaliza como regra de compilador em vez de padrão de biblioteca.

## Relação com outros conceitos

- [[wiki/concepts/gerenciamento-de-memoria]] — as três estratégias de runtime (manual, GC, ownership) que explicam por que esse mesmo código quebra em C++ e funciona em Go/C#
- [[wiki/concepts/rust-ownership-borrowing-lifetimes]] — RAII em C++ como precursor conceitual do ownership em Rust, com a diferença de ser verificado em compile-time em vez de convenção de biblioteca
- [[wiki/concepts/go-fundamentos]] — sintaxe de ponteiro em Go (`&`, `*`) idêntica à de C, protegida por escape analysis + GC
- [[wiki/concepts/lista-encadeada]] — estrutura de dados cujo custo O(1) de inserção/remoção depende diretamente de redirecionar ponteiros

## Key sources

- [[wiki/sources/ponteiros-cpp-go-csharp]]
