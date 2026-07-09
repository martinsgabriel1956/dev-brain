---
type: concept
title: "Gerenciamento de Memória (Linguagens de Programação)"
aliases: ["memory management", "garbage collector", "GC", "ownership", "manual memory management"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, linguagens-de-programacao, memoria, garbage-collector, rust, runtime]
skill: cs-fundamentals
status: draft
---

# Gerenciamento de Memória (Linguagens de Programação)

Toda variável criada num programa ocupa memória, que precisa ser liberada quando deixa de ser necessária. Como uma linguagem decide *quem* faz isso é uma das decisões de design mais difíceis de reverter depois de a linguagem ganhar usuários.

## Três abordagens

### Manual

O programador aloca e libera memória explicitamente (`malloc`/`free` em C). Dá controle total, mas um erro humano causa vazamento de memória (esqueceu de liberar) ou *use-after-free* (acessou memória já liberada).

### Garbage Collector (GC)

O runtime monitora quais objetos ainda estão referenciados/em uso e libera automaticamente os que não estão. Usado por Java, Go, Python, JavaScript. Mais seguro para a maioria dos programas — mas tem custo: dependendo do algoritmo do coletor, o GC pode pausar o programa inteiro por um tempo para limpar a memória ("stop-the-world").

### Ownership (Rust)

Cada valor tem exatamente um dono. Quando o dono sai do escopo, a memória é liberada automaticamente. Não existe GC nem `free` manual espalhado pelo código — o compilador (*borrow checker*) verifica essas regras em tempo de compilação, eliminando a classe inteira de bugs de manual (use-after-free, double-free) sem o custo de runtime de um GC.

## Por que a decisão é difícil de reverter

O modelo de memória escolhido molda como todo o resto da linguagem — e do código escrito nela — se comporta. O mesmo vale para o modelo de concorrência associado ao runtime (threads, event loop, goroutines): o código de usuário se apoia nessas garantias desde o primeiro programa escrito, tornando mudanças posteriores extremamente custosas.

## Relação com outros conceitos

- [[wiki/concepts/sistema-de-tipos]] — em Rust, ownership é parcialmente implementado como parte do sistema de tipos, verificado em compile-time
- [[wiki/concepts/compilador]] — a estratégia de execução (interpretador, compilação nativa, bytecode+VM) interage com o modelo de memória: um GC, por exemplo, precisa rodar dentro do runtime, não apenas no código gerado
- [[wiki/concepts/concorrencia]] — modelo de memória e modelo de concorrência do runtime são decisões acopladas (memória compartilhada entre threads exige sincronização; ownership em Rust é o que torna "fearless concurrency" possível sem data races)

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
