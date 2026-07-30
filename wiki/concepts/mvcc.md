---
type: concept
title: "MVCC (Multi-Version Concurrency Control)"
aliases: ["mvcc", "controle de concorrência por múltiplas versões", "multi-version concurrency control"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [banco-de-dados, mvcc, concorrencia, postgresql, database-internals]
skill: tech-mentor-data
status: stub
---

# MVCC (Multi-Version Concurrency Control)

Mecanismo que permite leituras e escritas concorrentes sem que uma bloqueie a outra. Quando uma transação altera uma linha, o banco não sobrescreve o dado no lugar — ele mantém a versão antiga por um tempo e cria uma versão nova. Leituras que já haviam começado continuam enxergando a versão antiga; a escrita segue criando a versão nova.

## Por que existe

Sem MVCC, o banco precisaria escolher entre travar leituras enquanto há escrita pendente (lento) ou arriscar inconsistência. Com MVCC, uma consulta de extrato não precisa esperar só porque outra transação (ex.: outro Pix) acabou de mudar o saldo — cada uma enxerga a versão coerente com o momento em que começou.

## Relação com locks

MVCC não elimina [[wiki/concepts/concorrencia|locks]] — eles continuam necessários quando duas escritas competem pelo mesmo dado ao mesmo tempo (ex.: dois débitos na mesma conta). MVCC resolve especificamente o atrito entre leitura e escrita; locks continuam resolvendo o atrito entre escrita e escrita.

## Relação com isolamento

O que cada transação enxerga sob MVCC — a versão antiga ou a mais recente — é exatamente a pergunta que o nível de [[wiki/concepts/isolation-levels]] responde. Em Read Committed, cada comando pode ver uma versão mais nova a cada execução; em Repeatable Read, a transação mantém a mesma versão (snapshot) do início ao fim.

## Efeito colateral: table bloat

Versões antigas de uma linha (dead tuples) não desaparecem sozinhas — precisam ser limpas depois que nenhuma transação ativa mais as referencia. É esse o trabalho do `VACUUM`/autovacuum no PostgreSQL, sem o qual a tabela "incha" com lixo. Ver `references/databases/postgresql-internals.md` da skill `tech-mentor-data`.

## Relação com outros conceitos

- [[wiki/concepts/isolation-levels]] — define qual versão cada transação pode enxergar
- [[wiki/concepts/concorrencia]] — MVCC é uma estratégia específica de controle de concorrência, alternativa a lock puro
- [[wiki/concepts/database-transactions]] — MVCC opera no nível da transação, criando/consumindo versões
- [[wiki/concepts/acid]] — parte de como o banco entrega Isolation sem sacrificar performance

## Key Sources

- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — MVCC explicado via exemplo de Pix concorrente e extrato não bloqueante
