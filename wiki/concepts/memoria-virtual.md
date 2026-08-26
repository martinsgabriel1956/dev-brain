---
type: concept
title: "Memória Virtual"
aliases: ["virtual memory", "espaço de endereçamento virtual", "page table", "paging"]
date_created: 2026-04-22
date_updated: 2026-08-26
source_count: 3
tags: [sistema-operacional, memória, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Memória Virtual

Abstração que faz cada processo acreditar que tem toda a memória disponível para si — mesmo que a RAM física seja compartilhada entre dezenas de processos.

## Como funciona

```
Processo A usa endereço virtual 100
    ↓ (SO consulta page table do processo A)
Endereço físico real: 4096

Processo B usa endereço virtual 100
    ↓ (SO consulta page table do processo B)
Endereço físico real: 8192
```

O SO mantém uma **page table** por processo que traduz endereços virtuais para físicos. O hardware (MMU — Memory Management Unit) faz essa tradução a cada acesso à memória.

## Benefícios

- **Isolamento**: processo A não pode ler/escrever na memória do processo B (violação gera segfault)
- **Ilusão de RAM abundante**: processo pode endereçar mais memória do que existe fisicamente (via [[concepts/swap]])
- **Simplificação**: programas não precisam saber onde na RAM física estão alocados

## Page Fault

Quando o processo acessa endereço virtual que não está mapeado para RAM física:

```
Minor fault: página existe mas não estava mapeada → rápido (microsegundos)
Major fault: página estava em swap (disco) → lento (milissegundos, I/O de disco)
```

Muitos major faults = sistema usando swap excessivamente = degradação severa.

## TLB (Translation Lookaside Buffer)

Cache de traduções recentes (virtual → físico). Quando o [[concepts/context-switch]] troca entre processos diferentes, o TLB precisa ser limpo (**TLB flush**) — é um dos principais custos do context switch.

## Ver também

- [[concepts/swap]] — extensão da RAM no disco quando a memória física esgota
- [[concepts/processo]] — cada processo tem sua própria page table
- [[concepts/context-switch]] — TLB flush é parte do custo da troca entre processos
- [[concepts/kernel]] — mantém e gerencia as page tables
- [[wiki/concepts/memoria-ram]] — o recurso físico (RAM DDR) que a memória virtual abstrai e compartilha entre processos

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/evolucao-memorias-ram-ddr1-a-ddr5]] — lado físico (voltagem, pinagem, frequência, gerações DDR1–DDR5) da RAM que esta página abstrai via page table/TLB
