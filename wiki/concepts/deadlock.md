---
type: concept
title: "Deadlock"
aliases: ["deadlock", "impasse", "bloqueio mútuo", "abraço mortal"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistema-operacional, concorrência, sincronização, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Deadlock

Situação onde duas ou mais threads ficam bloqueadas para sempre, cada uma esperando um recurso que a outra segura.

## Como acontece

```
Thread A: segura recurso 1, espera recurso 2
Thread B: segura recurso 2, espera recurso 1

→ Nenhuma das duas avança. Para sempre.
```

Analogia: cruzamento onde 4 carros chegam ao mesmo tempo e nenhum dá passagem — todo mundo fica parado.

## As 4 Condições de Coffman

Para um deadlock ocorrer, as 4 condições devem ser verdadeiras simultaneamente:

1. **Mutual exclusion**: recurso pode ser usado por apenas uma thread por vez
2. **Hold and wait**: thread segura recurso enquanto espera outro
3. **No preemption**: recurso só é liberado voluntariamente
4. **Circular wait**: cadeia circular de espera (A→B→C→A)

Quebrar qualquer uma das 4 previne deadlock.

## Estratégias de prevenção

- **Ordenação de locks**: sempre adquirir locks na mesma ordem global (quebra circular wait)
- **Lock timeout**: tentar adquirir com timeout — se não conseguir, libera o que tem e tenta de novo
- **Lock hierarchy**: numerar recursos, sempre pegar em ordem crescente
- **Detecção + recovery**: sistema detecta ciclo no grafo de espera e mata um dos processos

## Deadlock vs Starvation

- **Deadlock**: threads bloqueadas para sempre (nenhuma avança)
- **Starvation**: thread nunca é agendada, mas o sistema avança. Solução: aging de prioridade no [[concepts/escalonador]]

## Ver também

- [[concepts/mutex]] — mecanismo que, se mal usado, causa deadlock
- [[concepts/thread]] — unidade de execução que pode entrar em deadlock
- [[concepts/escalonador]] — aging evita starvation mas não resolve deadlock

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
