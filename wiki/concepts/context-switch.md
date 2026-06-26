---
type: concept
title: "Context Switch"
aliases: ["context switch", "troca de contexto", "context switching"]
date_created: 2026-04-22
date_updated: 2026-06-26
source_count: 2
tags: [sistema-operacional, scheduling, performance, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Context Switch (Troca de Contexto)

Operação onde o processador para de executar um processo e começa a executar outro. Acontece milhares de vezes por segundo de forma invisível para o usuário.

## O que acontece

```
1. Timer interrupt dispara → controle vai ao escalonador
2. SO salva estado completo do processo atual:
   → registradores da CPU
   → program counter (onde estava executando)
   → stack pointer
   → estado de memória virtual (TLB)
3. SO carrega estado salvo do próximo processo
4. CPU retoma execução do novo processo de onde parou
```

## Custo

Context switch tem custo real:
- Salvar/restaurar registradores: dezenas de nanosegundos
- **TLB flush** (troca entre processos diferentes): memória virtual precisa ser remapeada — microssegundos
- Cache miss: novo processo provavelmente não tem dados no cache L1/L2

Troca entre **threads do mesmo processo** é mais barata — mesma memória virtual, sem TLB flush.

## Por que é inevitável

Sem context switch, um processo poderia rodar para sempre, monopolizando a CPU. O [[concepts/escalonador]] usa [[concepts/interrupcao-de-hardware]] para forçar a troca periódica.

## Coroutines como alternativa

Coroutines (async/await, goroutines) fazem troca cooperativa **no espaço do usuário** — sem entrar no kernel. Custo próximo de zero comparado ao context switch do kernel. Ideal para I/O-bound com milhares de tarefas concorrentes.

## Ver também

- [[concepts/escalonador]] — decide quando o context switch acontece
- [[concepts/interrupcao-de-hardware]] — trigger que inicia a troca
- [[concepts/processo]] — entidade cujo estado é salvo/restaurado
- [[concepts/memoria-virtual]] — TLB flush é o custo extra na troca entre processos

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
