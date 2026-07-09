---
type: concept
title: "ext4 (e a linhagem ext2/ext3)"
aliases: ["ext4", "ext3", "ext2", "Extended File System", "sistema de arquivos estendido"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# ext4 (e a linhagem ext2/ext3)

Sistema de arquivos padrão do Linux, terceira geração da família ext ("extended", estendido).

## Linhagem

| Sistema | Journaling | Notas |
|---|---|---|
| ext2 | Não | Eficiente, mas travamento/queda de energia arrisca corrupção de arquivos |
| ext3 | Sim | Mesma base do ext2, adiciona [[concepts/journaling]] — mesmo salto que o NTFS deu sobre o FAT |
| ext4 | Sim | Lançado em 2008. Arquivos até ~16 TB, volumes até 1 exabyte |

O padrão se repete: cada geração resolve um limite (confiabilidade no ext2→ext3, escala no ext3→ext4) sem trocar a filosofia geral do sistema.

## Por que é o padrão do Linux

ext4 é o sistema de arquivos default da maioria das distribuições Linux para disco de sistema e servidores. Combina journaling, limites de tamanho generosos (16 TB por arquivo, 1 exabyte por volume) e décadas de maturidade/estabilidade no kernel.

## Compatibilidade

Windows e macOS não leem ext4 nativamente — conectar um disco ext4 num PC Windows normalmente falha sem software adicional (ex.: drivers de terceiros). Por isso ext4 aparece em discos de sistema Linux e servidores, não em mídia portátil compartilhada entre SOs (esse papel é do [[concepts/exfat]]).

## Papel equivalente em outros SOs

ext4 ocupa, no Linux, o papel que [[concepts/ntfs]] ocupa no Windows e [[concepts/apfs]] ocupa no macOS.

## Alternativa mais recente no ecossistema Linux

[[concepts/zfs]] cobre um nicho diferente do ext4 — não é o sistema de arquivos default de distribuições Linux, mas é a escolha em servidores/data centers onde integridade de dados verificada por checksum importa mais que ser o padrão "de fábrica".

## Ver também

- [[concepts/sistema-de-arquivos]]
- [[concepts/journaling]]

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
