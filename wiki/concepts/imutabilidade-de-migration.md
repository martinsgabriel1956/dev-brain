---
type: concept
title: "Imutabilidade de Migration"
aliases: ["erro de checksum", "não editar migration aplicada", "flyway checksum"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [flyway, migrations, checksum, imutabilidade]
skill: tech-mentor-backend
status: draft
---

# Imutabilidade de Migration

Regra: **uma migration já aplicada não se edita**. Ela virou parte do histórico do banco. Se algo precisa mudar, cria-se um **script novo** (V3, V4...).

## Mecanismo

O [[wiki/entities/flyway]] guarda o checksum de cada script em [[wiki/concepts/flyway-schema-history]]. Se o arquivo mudar depois de aplicado, o checksum não bate e a aplicação não sobe (erro de checksum). Pela skill `[skill: tech-mentor-backend]`, é a opção `validate-on-migrate` que faz a subida falhar. O mesmo checksum evita reexecutar um script já aplicado.

## Por que faz sentido

- Os bancos de outras pessoas e ambientes já rodaram a versão antiga; editar o arquivo faria cada banco divergir silenciosamente ([[wiki/concepts/drift-de-schema-entre-ambientes]]).
- O histórico vira trilha de auditoria confiável.
- Relação de ideia (**inferência minha**) com [[wiki/concepts/imutabilidade]] em programação funcional: em vez de mutar o artefato, acrescenta-se um novo.

## Consequência para correções

Errou na V2? A correção é a V3 (ex.: `ALTER`/`DROP COLUMN`), mesmo que "feio". Para mudanças destrutivas em produção, o padrão sequencial é [[wiki/concepts/expand-contract]]. Ver também [[wiki/concepts/database-migration]].

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]] (o erro é descrito, não demonstrado)
