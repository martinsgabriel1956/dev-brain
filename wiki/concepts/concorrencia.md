---
type: concept
title: "Concorrência"
aliases: ["concurrency", "execução concorrente", "multitarefa"]
date_created: 2026-06-26
date_updated: 2026-07-16
source_count: 3
tags: [cs-fundamentals, concorrencia, paralelismo, race-condition, threads]
skill: cs-fundamentals
status: draft
---

# Concorrência

**Gerenciar várias tarefas ao mesmo tempo** — não necessariamente executando-as simultaneamente. Um único processador pode ser concorrente alternando entre tarefas rapidamente (interleaving), dando a ilusão de simultaneidade.

## Concorrência ≠ Paralelismo

| | Concorrência | [[paralelismo]] |
|---|---|---|
| **Definição** | Lida com múltiplas tarefas | Executa múltiplas tarefas ao mesmo tempo |
| **Processadores** | 1 suficiente | Exige múltiplos cores |
| **Analogia** | Cozinheiro sozinho alternando entre tarefas | Dois cozinheiros cozinhando ao mesmo tempo |
| **Exemplo** | Event loop do Node.js | SIMD, GPU, multicore |

## O problema central: Race Condition

Quando duas [[thread]]s acessam o mesmo dado compartilhado sem coordenação, o resultado depende da **ordem de execução** — que é imprevisível.

### Exemplo clássico — saldo bancário

```
Thread A lê saldo: R$ 100
Thread B lê saldo: R$ 100
Thread A subtrai 50, grava: R$ 50
Thread B subtrai 50, grava: R$ 50  ← sobrescreve Thread A
Resultado: R$ 50 (deveria ser R$ 0)
```

Dinheiro foi criado do nada — a race condition corrompeu o estado.

## Mecanismos de controle

| Mecanismo | O que faz |
|---|---|
| [[mutex]] | Garante acesso exclusivo a uma seção crítica |
| Semáforo | Controla quantas threads acessam simultaneamente |
| Lock | Variante de mutex com escopo mais explícito |
| Operação atômica | Leitura + escrita indivisível no nível de hardware |

## O risco de coordenação: [[deadlock]]

Se Thread A espera Thread B liberar o recurso X, e Thread B espera Thread A liberar o recurso Y — nenhuma avança para sempre.

## Concorrência em diferentes modelos

- **Threads** (C, Java, Python GIL) — memória compartilhada, necessita locks
- **Event Loop** (Node.js, JavaScript) — single-thread concorrente via callbacks/Promises; sem race conditions mas também sem paralelismo real de CPU
- **Actor Model** (Erlang, Akka) — atores comunicam via mensagens, sem memória compartilhada
- **CSP** (Go channels) — goroutines se comunicam por canais tipados

## Fearless concurrency (Rust)

Em vez de detectar data races em runtime (sanitizers) ou evitá-las por convenção, o borrow checker do Rust rejeita em compile-time qualquer código onde uma referência mutável (`&mut`) coexista com qualquer outra referência ao mesmo dado — a regra é N leitores OU 1 escritor, nunca os dois. Como um data race exige que pelo menos um dos acessos concorrentes seja escrita sem coordenação, essa regra torna a classe inteira de data races irrepresentável no código que compila. É esse mecanismo, aplicado por padrão a toda referência da linguagem (não uma ferramenta opcional), que a comunidade chama de *fearless concurrency*. Detalhe completo em [[wiki/concepts/rust-ownership-borrowing-lifetimes]].

## Decisão de design em linguagens novas

Ao projetar uma linguagem do zero, o modelo de concorrência do runtime (threads, event loop, goroutines/CSP) é uma das decisões mais difíceis de reverter depois: todo código escrito pelos usuários passa a se apoiar nela desde o primeiro programa. Está diretamente acoplada à decisão de [[wiki/concepts/gerenciamento-de-memoria]] — memória compartilhada entre threads exige sincronização (mutex, locks), enquanto o modelo de ownership do Rust é o que viabiliza concorrência segura sem data races em tempo de compilação.

## Relação com outros conceitos

- [[paralelismo]] — a distinção é fundamental; confundir os dois leva a soluções erradas
- [[thread]] — a unidade de execução que torna concorrência possível
- [[deadlock]] — o pior caso quando coordenação falha
- [[mutex]] — o mecanismo mais comum de proteção
- [[wiki/concepts/gerenciamento-de-memoria]] — modelo de memória e modelo de concorrência do runtime são decisões de design acopladas
- [[wiki/concepts/rust-ownership-borrowing-lifetimes]] — a regra de exclusividade do borrowing como mecanismo concreto de "fearless concurrency"

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/como-criar-uma-linguagem-de-programacao]] — concorrência como decisão de runtime ao projetar uma linguagem, difícil de reverter depois
- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] — borrow checker eliminando data races em compile-time via regra N leitores OU 1 escritor
