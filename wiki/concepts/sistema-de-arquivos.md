---
type: concept
title: "Sistema de Arquivos"
aliases: ["file system", "filesystem", "ext4", "NTFS", "APFS", "sistema de arquivo"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 3
tags: [sistema-operacional, storage, cs-fundamentals]
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
| FAT12/16/[[concepts/fat32\|32]] | Windows / universal | Sem journaling, arquivo até 4 GB (FAT32) — sobrevive por compatibilidade |
| [[concepts/exfat]] | Windows + macOS | Sucessor do FAT32 sem o limite de 4 GB, ainda sem journaling — mídia portátil |
| [[concepts/ntfs]] | Windows | Permissões granulares, journaling, compressão |
| [[concepts/apfs]] (e HFS+) | macOS | Snapshots, criptografia nativa, copy-on-write |
| [[concepts/ext4]] (e ext2/3) | Linux | Journaling, performance geral, padrão |
| [[concepts/zfs]] | Linux/BSD | Integridade (checksums), snapshots, RAID integrado |
| **Btrfs** | Linux | Copy-on-write, snapshots, subvolumes |

Linhagem histórica completa (evolução dentro de cada família) em [[wiki/sources/sistemas-de-arquivos-explicados]].

## Journaling

Mecanismo que registra operações pendentes em um log antes de executá-las. Se o sistema travar no meio de uma escrita, o journal permite recuperação consistente. Detalhado em [[concepts/journaling]].

## Ver também

- [[concepts/kernel]] — o kernel implementa as operações do sistema de arquivos via VFS
- [[concepts/syscall]] — `open()`, `read()`, `write()` são syscalls que acessam o sistema de arquivos
- [[concepts/swap]] — também usa o disco, mas gerenciado separadamente

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/sistemas-de-arquivos-explicados]]
