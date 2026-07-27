---
type: entity
title: "Edgar F. Codd"
aliases: ["Codd", "E.F. Codd"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [banco-de-dados, historia-da-computacao, modelo-relacional, ibm]
skill: tech-mentor-backend
status: stub
---

# Edgar F. Codd

Pesquisador da IBM que, em 1970, publicou o paper "A Relational Model of Data for Large Shared Data Banks", propondo o **modelo relacional**: o programa declara o que quer e o sistema decide como buscar os dados fisicamente — conceito batizado de **independência de dados**.

## Contexto

Antes do paper, sistemas dos anos 70/80 (COBOL, Clipper, Assembly) manipulavam arquivos ISAM/CSV diretamente, com o programa acoplado à estrutura física do arquivo — qualquer novo campo quebrava todos os módulos que liam aquele arquivo, e buscas sem índice varriam o arquivo inteiro sequencialmente.

## Impacto

A ideia de Codd fundamentou os primeiros bancos relacionais comerciais: Oracle V2 (1979) e IBM DB2 (1983). Meio século depois, o modelo relacional ainda domina — não por falta de inovação, mas porque o problema que ele resolve (consistência, integridade referencial, independência de dados) nunca mudou. Ver [[wiki/concepts/acid]].

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
