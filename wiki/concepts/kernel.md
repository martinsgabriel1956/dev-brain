---
type: concept
title: "Kernel"
aliases: ["kernel", "núcleo do SO", "kernel mode", "ring 0"]
date_created: 2026-04-22
date_updated: 2026-06-26
source_count: 2
tags: [sistema-operacional, kernel, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Kernel

Núcleo do sistema operacional — a parte com acesso total ao hardware. É a fundação sobre a qual tudo o mais roda.

## Responsabilidades

- Gerenciar [[concepts/processo|processos]] e [[concepts/thread|threads]]
- Controlar acesso à memória ([[concepts/memoria-virtual]])
- Implementar o [[concepts/sistema-de-arquivos]]
- Receber e tratar [[concepts/interrupcao-de-hardware|interrupções]]
- Expor serviços aos programas via [[concepts/syscall|syscalls]]
- Controlar dispositivos de hardware

## User mode vs Kernel mode

```
User mode (ring 3):
  → Programas normais rodam aqui
  → Acesso limitado: não pode falar diretamente com hardware
  → Crash afeta só o processo

Kernel mode (ring 0):
  → Kernel roda aqui
  → Acesso total: hardware, memória de qualquer processo
  → Crash = sistema inteiro para (BSOD, kernel panic)
```

A separação é implementada pelo hardware (proteção de rings da CPU). Tentar acessar hardware de user mode gera **General Protection Fault**.

## Por que o kernel panic é fatal

O kernel é a fundação. Não há nada "embaixo" que possa salvá-lo. Se o kernel trava:
- Windows: **BSOD** (Blue Screen of Death)
- Linux: **kernel panic**
- macOS: **kernel panic** (tela cinza)

Programas comuns travam sem afetar o sistema porque rodam em user mode, isolados.

## Tipos de kernel

| Tipo | Característica | Exemplos |
|---|---|---|
| **Monolítico** | Tudo no kernel mode — drivers, FS, rede | Linux, Windows NT |
| **Microkernel** | Só o mínimo no kernel mode — rest em user mode | QNX, seL4 |
| **Híbrido** | Monolítico com elementos de microkernel | macOS (XNU), Windows |

Linux é monolítico mas suporta **módulos de kernel** carregados dinamicamente (drivers, por exemplo).

## Ver também

- [[concepts/syscall]] — interface entre user mode e kernel
- [[concepts/interrupcao-de-hardware]] — kernel recebe e processa interrupções
- [[concepts/processo]] — kernel cria e gerencia processos
- [[concepts/memoria-virtual]] — kernel mantém as page tables

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
