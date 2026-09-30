---
type: concept
title: "Ttl"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-30
source_count: 4
tags: [ttl]
skill: tech-mentor-backend
status: stub
---

# Ttl

Stub criado durante sweep de lint (links quebrados) a partir de referências em 3 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/cache-stampede-invalidation]]: [[ttl]]
- Em [[wiki/sources/cache-strategies]]: [[ttl]]
- Em [[wiki/sources/cache]]: [[ttl]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Caso: TTL de 5 Minutos em Cache de Perfil

TTL de 5 min na chave `user_id` → `photo_url`, combinado com atualização no upload; define a janela máxima de desatualização caso a atualização falhe (inferência).

## Key sources

- [[wiki/sources/cache-stampede-invalidation]]
- [[wiki/sources/cache-strategies]]
- [[wiki/sources/cache]]
- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — Instagram simplificado: TTL de 5 min no cache da URL da foto de perfil
