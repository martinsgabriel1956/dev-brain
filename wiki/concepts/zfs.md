---
type: concept
title: "ZFS"
aliases: ["ZFS", "Zettabyte File System", "OpenZFS"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# ZFS

Sistema de arquivos desenvolvido originalmente pela Sun Microsystems, lançado em 2006. Prioriza integridade de dados verificável acima de tudo — é o outlier da lista de sistemas de arquivos: não compete em compatibilidade nem em simplicidade, compete em confiabilidade.

## O que o diferencia dos demais

Todo sistema de arquivos com [[concepts/journaling]] (NTFS, ext3/4, HFS+) protege contra inconsistência causada por interrupção no meio de uma escrita. O ZFS vai além:

- **Checksums constantes** em todos os dados armazenados — não só nas transações em andamento, mas nos dados já gravados, detectando corrupção silenciosa (bit rot) que journaling não pega
- **Auto-reparo**: se um checksum não bate e existe uma cópia redundante (RAID-Z, mirror), o ZFS corrige automaticamente o bloco corrompido

## Escala

Suporta volumes na escala de zettabytes (1 zettabyte = 1 bilhão de TB) — muito além de qualquer necessidade de computador pessoal. Esse tipo de escala só faz sentido em storage agregado de data center.

## Onde é usado

Servidores, data centers, sistemas de armazenamento corporativo — qualquer contexto onde a pergunta "esse dado que voltou do disco é realmente o dado que eu escrevi?" precisa de resposta verificável, não apenas assumida. Não é o sistema de arquivos default de nenhuma distribuição Linux mainstream (esse papel é do [[concepts/ext4]]), mas está disponível como opção no Linux, FreeBSD e outros Unix.

## Estado atual

Continua desenvolvido pelo projeto **OpenZFS**, sucessor comunitário/open-source após a aquisição da Sun Microsystems pela Oracle.

## Ver também

- [[concepts/sistema-de-arquivos]]
- [[concepts/journaling]] — proteção que o ZFS tem e vai além dela com checksums
- [[concepts/ext4]] — o sistema de arquivos que o ZFS não substitui como default, mas complementa em cenários de alta confiabilidade

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
