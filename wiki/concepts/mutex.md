---
type: concept
title: "Mutex"
aliases: ["mutex", "mutual exclusion", "lock", "semáforo binário"]
date_created: 2026-04-22
date_updated: 2026-06-26
source_count: 3
tags: [sistema-operacional, concorrência, sincronização, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Mutex

**Mutual Exclusion** — mecanismo de sincronização que garante que apenas uma thread acesse um recurso compartilhado por vez.

## Como funciona

Funciona como uma chave de porta:

```
Thread A: acquire(mutex) → entra na seção crítica
Thread B: tenta acquire(mutex) → bloqueada até A liberar
Thread A: release(mutex) → B é desbloqueada, adquire o mutex
```

## Por que é necessário

Sem sincronização, duas threads modificando o mesmo estado simultaneamente produzem resultados imprevisíveis (race condition):

```
// Saldo inicial: 100
// Thread A lê saldo: 100
// Thread B lê saldo: 100
// Thread A: 100 - 50 = 50, salva
// Thread B: 100 - 30 = 70, salva  ← sobrescreve thread A!
// Resultado: 70 (deveria ser 20)
```

## Mutex vs Semáforo

- **Mutex**: binário (travado/livre), pertence a uma thread específica — só quem travou pode liberar
- **Semáforo**: contador — permite N threads simultâneas, qualquer thread pode liberar

## Custo e cuidados

- Mutex bem usado: overhead baixo
- Mutex mal usado: [[concepts/deadlock]] quando duas threads esperam uma pela outra
- **Granularidade**: mutex muito amplo = serialização desnecessária; muito fino = overhead de múltiplos locks

## Alternativas para casos específicos

- **Read-Write Lock**: múltiplos leitores simultâneos, escritor exclusivo
- **Atomic operations**: para operações simples (incremento, CAS) sem lock
- **Imutabilidade**: dados que nunca mudam não precisam de sincronização

## Ver também

- [[concepts/deadlock]] — consequência de mutex mal usado
- [[concepts/thread]] — entidade que adquire e libera mutex

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
