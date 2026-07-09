---
type: concept
title: "exFAT"
aliases: ["exFAT", "Extended File Allocation Table"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# exFAT

Sistema de arquivos lançado pela Microsoft em 2006, pensado como um meio-termo deliberado entre [[concepts/fat32]] e [[concepts/ntfs]].

## O que herda de cada lado

- **Do NTFS:** limite de tamanho de arquivo praticamente ilimitado (até 16 exabytes) — resolve a limitação de 4 GB por arquivo do FAT32
- **Do FAT32:** simplicidade e velocidade — sem [[concepts/journaling]], sem permissões por usuário, sem criptografia, sem cotas de disco

Essa simplicidade não é uma limitação acidental, é a escolha de design: exFAT é otimizado para leitura/escrita rápida em mídia removível, não para ser um sistema de arquivos "de trabalho" de um SO inteiro.

## Por que existe

Compatibilidade cruzada nativa entre Windows e macOS, com leitura/escrita completas em ambos — algo que [[concepts/ntfs]] e a linhagem [[concepts/apfs|Apple]] não oferecem uma para a outra sem software adicional. Por isso exFAT é o formato de fato para:

- Pendrives grandes (> 32 GB, onde FAT32 já não serve)
- HDs/SSDs externos usados entre Mac e Windows
- Cartões SDXC de câmeras e gravadores

## Trade-off central

exFAT troca confiabilidade transacional (journaling, recuperação após queda de energia) por portabilidade entre sistemas operacionais. Para um disco de sistema, essa troca seria inaceitável — por isso nenhum SO usa exFAT como sistema de arquivos principal.

## Ver também

- [[concepts/fat32]] — a base da qual o exFAT herda a simplicidade
- [[concepts/ntfs]] — de onde vem o limite de tamanho quase ilimitado
- [[concepts/journaling]] — o recurso que o exFAT deliberadamente não tem

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
