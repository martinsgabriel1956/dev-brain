---
type: concept
title: "Thread"
aliases: ["thread", "linha de execução", "worker thread", "multithreading"]
date_created: 2026-04-22
date_updated: 2026-06-26
source_count: 3
tags: [sistema-operacional, concorrência, thread, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Thread

Unidade de execução dentro de um processo. Permite que um único processo faça várias coisas ao mesmo tempo (ex: navegador renderizando página, tocando vídeo e respondendo ao teclado simultaneamente).

## Características

- Tem sua própria **pilha de execução** (stack)
- Compartilha **memória** com todas as outras threads do mesmo processo
- Agendada pelo kernel (diferente de coroutines, que são agendadas no espaço do usuário)

## Processo vs Thread

```
Processo: empresa nova no prédio
  → sala própria, contrato próprio, tudo separado

Thread: funcionário novo na mesma empresa
  → usa os mesmos recursos (sala, impressora, memória)
```

| | Processo | Thread |
|---|---|---|
| Memória | Espaço separado | Compartilhada |
| Isolamento | Alto — crash não afeta outros | Baixo — crash derruba processo |
| Custo de criação | Alto (~1MB stack, syscall) | Médio (~8KB–1MB stack) |
| Comunicação | IPC (pipes, sockets) | Direto via memória compartilhada |
| Context switch | Mais caro (TLB flush) | Menos caro |

## O Preço da Memória Compartilhada

Se duas threads modificam o mesmo estado ao mesmo tempo, o resultado é imprevisível — **race condition**. A solução é sincronização via [[concepts/mutex]] ou outros mecanismos.

## Deadlock

Quando thread A espera thread B que espera thread A → ambas bloqueadas para sempre. Ver [[concepts/deadlock]].

## Alternativas

- **Coroutines / async-await**: concorrência cooperativa no espaço do usuário, custo mínimo (~2-8KB), ideal para I/O-bound
- **Processos**: isolamento máximo, custo alto, para workloads não-confiáveis

## Ver também

- [[concepts/processo]] — container que abriga as threads
- [[concepts/deadlock]] — bloqueio mútuo entre threads
- [[concepts/mutex]] — mecanismo de sincronização
- [[concepts/escalonador]] — como o kernel agenda threads e processos

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
