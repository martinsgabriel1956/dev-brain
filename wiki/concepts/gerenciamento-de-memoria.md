---
type: concept
title: "Gerenciamento de Memória (Linguagens de Programação)"
aliases: ["memory management", "garbage collector", "GC", "ownership", "manual memory management"]
date_created: 2026-07-09
date_updated: 2026-08-27
source_count: 4
tags: [cs-fundamentals, lang-systems, linguagens-de-programacao, memoria, garbage-collector, rust, runtime, raii, cpp, baixo-nivel]
skill: cs-fundamentals
status: draft
---

# Gerenciamento de Memória (Linguagens de Programação)

Toda variável criada num programa ocupa memória, que precisa ser liberada quando deixa de ser necessária. Como uma linguagem decide *quem* faz isso é uma das decisões de design mais difíceis de reverter depois de a linguagem ganhar usuários.

## Três abordagens

### Manual

O programador aloca e libera memória explicitamente (`malloc`/`free` em C). Dá controle total, mas um erro humano causa vazamento de memória (esqueceu de liberar) ou *use-after-free* (acessou memória já liberada).

Em C++ moderno, o padrão **RAII** (Resource Acquisition Is Initialization) mitiga boa parte do risco humano do modelo manual sem introduzir GC: um smart pointer como `std::unique_ptr` libera o recurso automaticamente no destrutor, quando o objeto sai de escopo — sem precisar de `delete` explícito, mesmo em caminhos de saída não previstos (early return, exceção). Detalhamento completo (stack vs. heap, o bug clássico de retornar endereço de variável local, `unique_ptr`/`std::move`) em [[wiki/concepts/ponteiros-cpp-stack-heap-raii]].

### Garbage Collector (GC)

O runtime monitora quais objetos ainda estão referenciados/em uso e libera automaticamente os que não estão. Usado por Java, Go, Python, JavaScript. Mais seguro para a maioria dos programas — mas tem custo: dependendo do algoritmo do coletor, o GC pode pausar o programa inteiro por um tempo para limpar a memória ("stop-the-world").

### Ownership (Rust)

Cada valor tem exatamente um dono. Quando o dono sai do escopo, a memória é liberada automaticamente. Não existe GC nem `free` manual espalhado pelo código — o compilador (*borrow checker*) verifica essas regras em tempo de compilação, eliminando a classe inteira de bugs de manual (use-after-free, double-free) sem o custo de runtime de um GC. Detalhamento completo (borrowing, `&`/`&mut`, lifetimes, e por que isso também elimina data races) em [[wiki/concepts/rust-ownership-borrowing-lifetimes]].

## Por que a decisão é difícil de reverter

O modelo de memória escolhido molda como todo o resto da linguagem — e do código escrito nela — se comporta. O mesmo vale para o modelo de concorrência associado ao runtime (threads, event loop, goroutines): o código de usuário se apoia nessas garantias desde o primeiro programa escrito, tornando mudanças posteriores extremamente custosas.

## Gerenciamento manual como motivação e como filtro de entrada em baixo nível

Em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]], o gerenciamento manual de memória em [[wiki/concepts/linguagem-c|C]] — e os bugs clássicos que ele produz (memory leak, double free) — é citado logo na abertura como o tipo de dor de cabeça que atrai (ou afasta) quem migra de linguagens de alto nível para baixo nível. Também aparece como parte central do que um [[wiki/concepts/sistemas-operacionais|sistema operacional]] precisa oferecer às aplicações: a fonte cita `malloc` e proteção de memória entre processos como responsabilidades centrais do SO, ao lado de escalonamento e sistema de arquivos.

## Relação com outros conceitos

- [[wiki/concepts/sistema-de-tipos]] — em Rust, ownership é parcialmente implementado como parte do sistema de tipos, verificado em compile-time
- [[wiki/concepts/compilador]] — a estratégia de execução (interpretador, compilação nativa, bytecode+VM) interage com o modelo de memória: um GC, por exemplo, precisa rodar dentro do runtime, não apenas no código gerado
- [[wiki/concepts/concorrencia]] — modelo de memória e modelo de concorrência do runtime são decisões acopladas (memória compartilhada entre threads exige sincronização; ownership em Rust é o que torna "fearless concurrency" possível sem data races)
- [[wiki/concepts/ponteiros-cpp-stack-heap-raii]] — o mesmo bug (retornar endereço de variável local) é undefined behavior em C++ manual, mas não existe em Go (escape analysis realoca a variável para a heap) nem em C# (reference types já vivem na heap sob GC)

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] — aprofundamento de ownership em Rust: move semantics, regra de exclusividade do borrowing (N leitores OU 1 escritor) e lifetimes como garantia de que referência não outlive o valor
- [[wiki/sources/ponteiros-cpp-go-csharp]] — comparação prática C++/Go/C#: stack vs. heap, escape analysis em Go, RAII e `unique_ptr` em C++ moderno
- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] — gerenciamento manual (malloc, memory leak, double free) como motivação de estudo e como responsabilidade central de um sistema operacional
