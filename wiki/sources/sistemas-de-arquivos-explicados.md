---
type: source
title: "Sistemas de Arquivos Explicados"
aliases: ["file systems explained", "FAT vs NTFS vs ext4 vs ZFS"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sistemas-de-arquivos-explicados.md
source_url: ""
author: desconhecido
date_published: desconhecida
date_ingested: 2026-07-09
---

# Sistemas de Arquivos Explicados

## TL;DR

Panorama cronológico dos sistemas de arquivos, do FAT12 (1980) ao ZFS (2006): cada geração resolve o limite de tamanho de arquivo/volume ou a falta de confiabilidade (journaling, checksums) da geração anterior, trocando isso por compatibilidade mais estreita.

## Key Claims

**1. A família FAT evoluiu puramente para destravar limites de tamanho**
- [[concepts/fat32|FAT12]] (1980): arquivos até 32 MB
- FAT16: volumes em GB, arquivos até 2 GB
- [[concepts/fat32|FAT32]]: volumes até 2 TB, mas arquivo individual travado em 4 GB — um vídeo grande não cabe nem sobrando espaço no disco
- FAT32 sobrevive hoje só por compatibilidade universal (pendrives, cartões de memória)
- Fonte: transcrição do vídeo

**2. NTFS resolveu o limite de tamanho e adicionou confiabilidade e controle de acesso**
- [[concepts/ntfs|NTFS]]: arquivo/volume até 16 exabytes (praticamente ilimitado)
- Introduz [[concepts/journaling]]: registra mudanças antes de aplicá-las, permite recuperação após queda de energia
- Adiciona permissões por usuário, criptografia, compressão, cotas de disco
- Trade-off: compatibilidade limitada fora do Windows
- Fonte: transcrição do vídeo

**3. exFAT é o meio-termo deliberado entre FAT32 e NTFS**
- [[concepts/exfat|exFAT]] (Microsoft, 2006): herda o limite quase ilimitado de arquivo do NTFS, mas abre mão de journaling, permissões, criptografia e cotas
- Resultado: mais rápido e mais simples que NTFS, com leitura/escrita nativa em Windows e macOS
- Nicho: pendrives grandes, HDs externos, cartões SDXC de câmeras — onde portabilidade entre SOs importa mais que confiabilidade transacional
- Fonte: transcrição do vídeo

**4. A linhagem Apple (HFS → HFS+ → APFS) trocou o alvo de HD para SSD**
- HFS (1985): arquivos até 2 GB, volumes até 2 TB
- HFS+ (Mac OS Estendido): aumenta limites, adiciona journaling
- [[concepts/apfs|APFS]] (2017): projetado para SSD/flash — criptografia forte, snapshots, gerenciamento de espaço otimizado para storage não-mecânico
- Fonte: transcrição do vídeo

**5. ext2 → ext3 → ext4 seguem o mesmo padrão do NTFS: journaling primeiro, escala depois**
- ext2: eficiente, mas sem journaling — travamento = risco real de corrupção
- ext3: mesma base, adiciona journaling
- [[concepts/ext4|ext4]] (2008): arquivos até ~16 TB, volumes até 1 exabyte; hoje é o padrão do Linux
- Fonte: transcrição do vídeo

**6. ZFS prioriza integridade de dados verificável sobre simplicidade**
- [[concepts/zfs|ZFS]] (Sun Microsystems, 2006): checksums constantes nos dados armazenados, detecta corrupção e repara automaticamente se houver cópia redundante
- Suporta volumes na escala de zettabytes
- Usado em servidores/data centers, não em storage pessoal — mantido hoje pelo projeto OpenZFS (Linux, FreeBSD, Unix)
- Fonte: transcrição do vídeo

**7. Nenhum sistema de arquivos de um SO é lido nativamente por outro SO fora da sua família**
- Windows não lê APFS/HFS+ (Apple) nem ext4 (Linux) sem software adicional
- exFAT é a exceção deliberada — construído para ser lido nativamente por Windows e macOS
- Fonte: transcrição do vídeo

## Entidades

- **FAT12 / FAT16 / FAT32**: família original da Microsoft, ver [[concepts/fat32]]
- **NTFS**: ver [[concepts/ntfs]]
- **exFAT**: ver [[concepts/exfat]]
- **HFS / HFS+ / APFS**: linhagem Apple, ver [[concepts/apfs]]
- **ext2 / ext3 / ext4**: linhagem Linux, ver [[concepts/ext4]]
- **ZFS / OpenZFS**: ver [[concepts/zfs]]
- **Sun Microsystems**: criadora original do ZFS (2006), hoje mantido pelo projeto OpenZFS

## Conceitos Tocados

- [[concepts/sistema-de-arquivos]]
- [[concepts/fat32]]
- [[concepts/exfat]]
- [[concepts/ntfs]]
- [[concepts/apfs]]
- [[concepts/ext4]]
- [[concepts/zfs]]
- [[concepts/journaling]]

## Questões Abertas

- O vídeo não cobre Btrfs (já citado na tabela comparativa de [[concepts/sistema-de-arquivos]]) nem F2FS (otimizado para flash em mobile) — lacuna na cobertura de sistemas de arquivos modernos para flash/SSD além de APFS
- Não há menção a ReFS (Resilient File System), sucessor do NTFS da Microsoft para Windows Server
- O vídeo trata "checksum" do ZFS como recurso único, mas não explica se outros sistemas (ex.: Btrfs, também copy-on-write) oferecem proteção equivalente

## Raw Quotes

> "Quando um sistema é bem feito, tudo funciona muito rápido, organizado e sem desperdício. Já quando não é, você perde tempo, perde dados e perde eficiência."

> "O ZFS verifica constantemente os dados armazenados usando checksums para detectar corrupção. Se dados danificados forem encontrados e existir uma cópia de backup, o ZFS pode repará-los automaticamente."
