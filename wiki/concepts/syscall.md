---
type: concept
title: "Syscall"
aliases: ["syscall", "system call", "chamada de sistema", "chamada ao kernel"]
date_created: 2026-04-22
date_updated: 2026-06-26
source_count: 2
tags: [sistema-operacional, kernel, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Syscall (Chamada de Sistema)

Interface pela qual programas em user mode pedem serviços ao [[concepts/kernel]]. Nenhum programa acessa hardware diretamente — tudo passa pelo kernel via syscall.

## Por que existe

Sem syscalls, qualquer programa poderia acessar qualquer parte do disco, memória de outros processos ou hardware — seria um caos de segurança.

A separação user mode / kernel mode garante que programas só façam o que o SO permite.

## Como funciona

```
Programa (user mode):
  fd = open("arquivo.txt", O_RDONLY)  ← syscall

  1. CPU salva estado do programa
  2. CPU troca de user mode para kernel mode (software interrupt / trap)
  3. Kernel executa a operação (abre o arquivo, verifica permissões)
  4. Kernel retorna resultado para o programa
  5. CPU volta para user mode
  6. Programa recebe o file descriptor
```

## Exemplos comuns

| Syscall | O que faz |
|---|---|
| `open()` | Abre um arquivo |
| `read()` | Lê dados de um file descriptor |
| `write()` | Escreve dados |
| `fork()` | Cria um novo processo (clone do atual) |
| `exec()` | Substitui processo atual por novo programa |
| `mmap()` | Mapeia arquivo ou memória |
| `socket()` | Cria socket de rede |
| `exit()` | Termina processo |

## Custo

Syscall tem overhead — troca de modo (user → kernel → user) custa dezenas a centenas de nanosegundos. Por isso bibliotecas de alto nível fazem **buffering**: acumulam várias escritas pequenas e fazem uma syscall grande ao invés de uma syscall por byte.

## Ver também

- [[concepts/kernel]] — recebe e executa as syscalls
- [[concepts/interrupcao-de-hardware]] — syscall usa mecanismo similar (software interrupt/trap)
- [[concepts/processo]] — contexto em que a syscall é feita

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
