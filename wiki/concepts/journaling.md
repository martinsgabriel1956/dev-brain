---
type: concept
title: "Journaling (Sistemas de Arquivos)"
aliases: ["journaling", "write-ahead log de disco", "log de transações de disco"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [sistema-operacional, storage, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Journaling (Sistemas de Arquivos)

Mecanismo que registra as mudanças pendentes num log (o "journal") antes de aplicá-las de fato aos blocos do disco.

## O problema que resolve

Uma escrita em disco não é atômica — envolve múltiplos passos (atualizar dados, atualizar metadados, atualizar a tabela de alocação). Se o sistema travar ou perder energia no meio desse processo, o [[concepts/sistema-de-arquivos]] pode ficar num estado inconsistente: metadado aponta para blocos que não foram escritos, ou vice-versa. Isso é corrupção de dados.

## Como funciona

1. Antes de alterar os blocos reais, o sistema escreve a intenção da mudança no journal (uma área reservada do disco)
2. Só depois aplica a mudança nos blocos de dados/metadados
3. Se o sistema cair no meio do processo, na próxima inicialização ele lê o journal e:
   - Refaz (`replay`) mudanças que estavam completas no journal mas não foram aplicadas
   - Descarta mudanças incompletas

Isso reduz drasticamente as chances de corrupção — não elimina, mas transforma um scan completo do disco (como o `chkdsk`/`fsck` de sistemas sem journaling) em uma recuperação rápida baseada no log.

## Quem tem, quem não tem

| Com journaling | Sem journaling |
|---|---|
| [[concepts/ntfs]], HFS+, [[concepts/ext4]] (e ext3), [[concepts/zfs]] (via ZIL) | FAT12/16/[[concepts/fat32\|32]], [[concepts/exfat]], ext2, HFS (original) |

exFAT é o caso notável de trade-off deliberado: mantém a simplicidade do FAT em troca de não ter journaling, mesmo suportando arquivos gigantes como o NTFS.

## Custo

Journaling não é grátis — cada escrita lógica vira (pelo menos) duas escritas físicas (journal + dado real), o que reduz throughput. É por isso que dispositivos portáteis simples (pendrives, cartões SD) frequentemente usam sistemas de arquivos sem journaling: prioriza-se velocidade e simplicidade sobre resiliência a queda de energia.

## Ver também

- [[concepts/sistema-de-arquivos]] — onde o journaling se encaixa na pilha do SO
- [[concepts/database-transactions]] — o mesmo princípio de write-ahead log aparece em bancos de dados (WAL)

## Key Sources

- [[wiki/sources/sistemas-de-arquivos-explicados]]
