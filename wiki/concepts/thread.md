---
type: concept
title: "Thread"
aliases: ["thread", "linha de execução", "worker thread", "multithreading"]
date_created: 2026-04-22
date_updated: 2026-09-14
source_count: 4
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

## Worker Threads em Node.js: escape para trabalho CPU-bound

Node.js roda sua [[wiki/concepts/event-loop-performance-js|main thread]] como single thread: um processador de JavaScript por processo, executando uma operação por vez. Isso funciona bem porque a maior parte do trabalho de servidor é I/O-bound (delegável ao sistema operacional sem ocupar a thread). Mas trabalho **CPU-bound** de verdade — parse de payload grande, criptografia, e notavelmente renderização SSR complexa (ver [[wiki/concepts/renderizacao-ssr-vs-csr]]) — segura a main thread inteira e bloqueia toda requisição nova até terminar.

A saída é mover esse trabalho para uma **worker thread**: uma thread separada dentro do mesmo processo, com memória compartilhada eficiente via `SharedArrayBuffer`, que processa o trabalho pesado e devolve o resultado — deixando a thread principal livre para continuar atendendo. Isso é distinto de **Cluster** (múltiplos processos, cada um com seu próprio event loop, usado para escalar entre CPUs) e de **Child Process** (processo isolado via IPC, para isolamento total ou scripts externos que podem falhar sem derrubar o processo principal).

## Ver também

- [[concepts/processo]] — container que abriga as threads
- [[concepts/deadlock]] — bloqueio mútuo entre threads
- [[concepts/mutex]] — mecanismo de sincronização
- [[concepts/escalonador]] — como o kernel agenda threads e processos
- [[wiki/concepts/event-loop-performance-js]] — por que Node.js precisa de worker threads para trabalho CPU-bound
- [[wiki/concepts/renderizacao-ssr-vs-csr]] — SSR pesado como caso concreto de trabalho CPU-bound que se beneficia de worker threads

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]] — worker threads como uma das três soluções (junto de chunking e filas) para SSR CPU-bound travando o event loop; distinção worker threads vs. cluster vs. child process calibrada com `references/nodejs-core.md` da skill `lang-dynamic`
