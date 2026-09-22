---
type: concept
title: "Schema Evolution"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 2
tags: [schema-evolution]
skill: tech-mentor-ai
status: stub
---

# Schema Evolution

Stub criado durante sweep de lint (links quebrados) a partir de referências em 3 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/entities/microsoft]]: [[wiki/sources/seedwork-martin-fowler]] (2003) cita o "DLL-hell" da Microsoft — bibliotecas compartilhadas do Windows que quebravam quando versões diferentes, atualizadas em cronogramas distintos, entravam em conflito — como prova de que mesmo reuso de código maduro (não só o [[wiki/concepts/seedwork|seedwork]] improvisado) é difícil de acertar na prática. Décadas antes da economia de IA descrita 
- Em [[wiki/sources/seedwork-martin-fowler]]: **Mesmo o reuso maduro é difícil**: bibliotecas compartilhadas que evoluem em cronogramas diferentes geram problemas de versionamento — cita explicitamente o "DLL-hell" da Microsoft e um incidente pessoal de dependências quebradas no RedHat. Antecipa, em 2003, a mesma dor que hoje justifica práticas como [[wiki/concepts/schema-evolution|schema evolution]] e versionamento semântico de contratos.
- Em [[wiki/sources/serialization-protocols]]: [[concepts/schema-evolution]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Key sources

- [[wiki/entities/microsoft]]
- [[wiki/sources/seedwork-martin-fowler]]
- [[wiki/sources/serialization-protocols]]
