---
type: concept
title: "Sistema de Arquivos"
aliases: ["file system", "filesystem", "ext4", "NTFS", "APFS", "sistema de arquivo"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 4
tags: [sistema-operacional, storage, hardware, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Sistema de Arquivos

Camada de abstração que organiza dados brutos no disco (sequência de zeros e uns) em hierarquia de arquivos e pastas com nomes.

## O problema que resolve

Disco é um bloco gigante de bits sem estrutura. O sistema de arquivos cria:
- **Nomes** para dados
- **Hierarquia** (pastas dentro de pastas)
- **Metadados** (dono, permissões, timestamps)
- **Mapa de onde cada pedaço está**

## Como arquivos são armazenados

Um arquivo de 12MB pode estar fragmentado em blocos espalhados pelo disco:

```
Arquivo: documento.pdf (12MB)
Blocos: [47] [193] [512] [1024] [...]  ← fora de ordem no disco

Sistema de arquivos mantém tabela:
  documento.pdf → blocos 47, 193, 512, 1024...

Ao abrir: SO lê os blocos, monta na ordem correta, entrega o arquivo inteiro
```

## O que acontece ao "deletar"

Na maioria dos sistemas de arquivos, deletar apenas **remove a entrada da tabela**. Os dados permanecem no disco até serem sobrescritos por outro arquivo.

Por isso:
- Programas de recuperação de dados conseguem restaurar arquivos deletados
- Deleção é rápida (só remove metadado)
- Dados sensíveis precisam de **secure delete** (sobrescrever os blocos)

## Comparativo de sistemas de arquivos

| Sistema | SO | Destaques |
|---|---|---|
| FAT12/16/[[wiki/concepts/fat32\|32]] | Windows / universal | Sem journaling, arquivo até 4 GB (FAT32) — sobrevive por compatibilidade |
| [[wiki/concepts/exfat]] | Windows + macOS | Sucessor do FAT32 sem o limite de 4 GB, ainda sem journaling — mídia portátil |
| [[wiki/concepts/ntfs]] | Windows | Permissões granulares, journaling, compressão |
| [[wiki/concepts/apfs]] (e HFS+) | macOS | Snapshots, criptografia nativa, copy-on-write |
| [[wiki/concepts/ext4]] (e ext2/3) | Linux | Journaling, performance geral, padrão |
| [[wiki/concepts/zfs]] | Linux/BSD | Integridade (checksums), snapshots, RAID integrado |
| **Btrfs** | Linux | Copy-on-write, snapshots, subvolumes |

Linhagem histórica completa (evolução dentro de cada família) em [[wiki/sources/sistemas-de-arquivos-explicados]].

## Journaling

Mecanismo que registra operações pendentes em um log antes de executá-las. Se o sistema travar no meio de uma escrita, o journal permite recuperação consistente. Detalhado em [[wiki/concepts/journaling]].

## Ver também

- [[wiki/concepts/kernel]] — o kernel implementa as operações do sistema de arquivos via VFS
- [[wiki/concepts/syscall]] — `open()`, `read()`, `write()` são syscalls que acessam o sistema de arquivos
- [[wiki/concepts/swap]] — também usa o disco, mas gerenciado separadamente

## A camada de baixo: a mídia física

O sistema de arquivos é uma **abstração sobre uma mídia** — os "blocos do disco" moram fisicamente em um [[wiki/concepts/hd-disco-rigido]], um [[wiki/concepts/ssd]] ([[wiki/concepts/memoria-flash]]), um cartão ou um pen drive. A mídia influencia o design: o [[wiki/concepts/apfs]] é otimizado para flash (copy-on-write, sem penalidade de fragmentação), enquanto FAT/exFAT são o padrão de mídia portátil por compatibilidade. Ver o panorama de mídias em [[wiki/sources/tipos-de-armazenamento-de-dados]].

## Key Sources

- [[wiki/sources/sistema-operacional-por-baixo-dos-panos]]
- [[wiki/sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/sistemas-de-arquivos-explicados]]
- [[wiki/sources/tipos-de-armazenamento-de-dados]] — as mídias físicas sob a abstração de arquivos (HD, SSD/flash, óptico, fita)
