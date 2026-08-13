---
type: concept
title: "APFS (e a linhagem HFS/HFS+)"
aliases: ["APFS", "Apple File System", "HFS", "HFS+", "Mac OS Estendido", "Hierarchical File System"]
date_created: 2026-07-09
date_updated: 2026-08-13
source_count: 2
tags: [sistema-operacional, storage, hardware, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# APFS (e a linhagem HFS/HFS+)

Sistema de arquivos padrão do macOS moderno (desde 2017), terceira geração de uma linhagem que começou com o HFS em 1985.

## Linhagem

| Sistema | Ano | Notas |
|---|---|---|
| HFS | 1985 | Arquivos até 2 GB, volumes até 2 TB. Sem journaling |
| HFS+ (Mac OS Estendido) | — | Aumenta limites de armazenamento, adiciona [[concepts/journaling]] |
| APFS | 2017 | Redesenho completo, alvo é SSD/flash em vez de HD mecânico |

## O salto do HFS+ para o APFS

APFS não é uma evolução incremental do HFS+ — foi projetado do zero para storage flash moderno (SSD), enquanto HFS+ carregava premissas de disco mecânico (HD). Recursos que o APFS traz:

- **Criptografia forte nativa** por arquivo/volume
- **Snapshots** — capturas do estado do sistema de arquivos num instante, usadas para backup e rollback
- **Gerenciamento de espaço otimizado** para as características de leitura/escrita do flash (sem as penalidades de fragmentação que HDs mecânicos sofrem)

## Compatibilidade

Assim como o [[concepts/ext4|ext4]] do Linux, APFS e HFS+ não são suportados nativamente pelo Windows — ler um disco APFS num PC Windows exige software adicional. Essa falta de compatibilidade cruzada é o motivo pelo qual dispositivos portáteis compartilhados entre Mac e Windows usam [[concepts/exfat]] em vez de APFS.

## Papel equivalente em outros SOs

APFS ocupa, no macOS, o mesmo papel que [[concepts/ntfs]] ocupa no Windows e [[concepts/ext4]] ocupa no Linux: sistema de arquivos principal do disco de sistema, com journaling/proteção de dados e recursos avançados.

## Ver também

- [[concepts/sistema-de-arquivos]]
- [[concepts/journaling]]
- [[concepts/ssd]] — a mídia flash que o APFS foi desenhado para explorar; a transição HD→SSD (2017) motivou o novo formato

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
- [[wiki/sources/tipos-de-armazenamento-de-dados]] — a passagem de disco magnético (HD) para flash (SSD) que o APFS acompanha
