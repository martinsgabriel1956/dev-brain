---
type: concept
title: "FAT (FAT12/FAT16/FAT32)"
aliases: ["FAT32", "FAT16", "FAT12", "File Allocation Table", "tabela de alocação de arquivos"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# FAT (FAT12/FAT16/FAT32)

Família de [[concepts/sistema-de-arquivos|sistemas de arquivos]] mais antiga em uso, criada pela Microsoft. O nome vem da estrutura central: uma tabela que mapeia quais blocos do disco pertencem a cada arquivo.

## Linhagem

| Versão | Ano | Limite de arquivo | Limite de volume |
|---|---|---|---|
| FAT12 | 1980 | 32 MB | — |
| FAT16 | — | 2 GB | GBs (HDs) |
| FAT32 | — | 4 GB | 32 GB (Windows) / 2 TB (outros SOs) |

Cada versão existiu para destravar o limite de tamanho que a anterior batia — não para adicionar recursos novos.

## A pegadinha do FAT32 hoje

O limite de 4 GB por arquivo ainda é real em 2026: copiar um vídeo de 5 GB para um pendrive formatado em FAT32 falha mesmo com espaço livre sobrando, porque o limite é por arquivo, não por volume. Um HD de 4 TB formatado em FAT32 pode ser dividido em duas partições de 2 TB em vez de uma única, porque FAT32 também trava em 2 TB por partição.

## Por que ainda existe

FAT32 não tem [[concepts/journaling]], permissões, criptografia ou compressão — é o sistema de arquivos mais "burro" ainda em uso comum. Sobrevive por um único motivo: **compatibilidade universal**. Praticamente qualquer sistema operacional, câmera, console ou dispositivo embarcado consegue ler/escrever FAT32 sem driver adicional. Por isso ainda é o padrão de fábrica de pendrives e cartões de memória pequenos.

## Sucessores diretos

- [[concepts/exfat]] — mesma simplicidade, sem o limite de 4 GB
- [[concepts/ntfs]] — adiciona journaling, permissões e limites praticamente ilimitados, ao custo de compatibilidade fora do Windows

## Ver também

- [[concepts/sistema-de-arquivos]]
- [[concepts/journaling]]

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
