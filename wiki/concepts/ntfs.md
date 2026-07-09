---
type: concept
title: "NTFS"
aliases: ["NTFS", "New Technology File System", "sistema de arquivos de nova tecnologia"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# NTFS

Sistema de arquivos padrão do Windows moderno, sucessor da família [[concepts/fat32|FAT]]. Resolve tanto o problema de tamanho quanto o de confiabilidade que o FAT nunca resolveu.

## O que resolve em relação ao FAT

- **Tamanho:** arquivo e volume até 16 exabytes (1 exabyte = 1 milhão de TB) — na prática ilimitado, contra os 4 GB por arquivo do [[concepts/fat32|FAT32]]
- **Confiabilidade:** é um sistema de arquivos com [[concepts/journaling]] — registra mudanças antes de aplicá-las, reduzindo o risco de corrupção após queda de energia ou travamento
- **Controle de acesso:** permissões por usuário/grupo (somente leitura, acesso restrito), diferente do FAT que não distingue usuários
- **Recursos extras:** criptografia de arquivos (EFS), compressão nativa, cotas de disco por usuário

## Por que o Windows exige NTFS

Recursos modernos do SO (permissões de segurança, restauração de sistema, deduplicação, cotas) dependem de metadados que só o NTFS suporta. É por isso que a instalação do Windows exige o disco de sistema formatado em NTFS — FAT32 e exFAT não sustentam essas garantias.

## A limitação real

Compatibilidade fora do ecossistema Windows é limitada. Linux consegue ler/escrever NTFS via driver (ntfs-3g ou o suporte nativo mais recente do kernel), mas macOS só lê NTFS nativamente — escrita exige software de terceiros. Isso torna o NTFS uma escolha ruim para mídia removível compartilhada entre SOs, papel que fica com [[concepts/exfat]].

## Comparáveis em outros SOs

O papel que o NTFS ocupa no Windows (sistema de arquivos principal, com journaling e recursos avançados) é ocupado por [[concepts/apfs]] no macOS e por [[concepts/ext4]] no Linux.

## Ver também

- [[concepts/sistema-de-arquivos]]
- [[concepts/journaling]]
- [[concepts/exfat]] — a alternativa quando compatibilidade cruzada importa mais que os recursos do NTFS

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
