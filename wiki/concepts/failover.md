---
type: concept
title: "Failover"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-19
source_count: 5
tags: [failover]
skill: tech-mentor-system-design
status: stub
---

# Failover

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/dns]]: [[failover]]
- Em [[wiki/sources/multi-region-global-lb]]: [[failover]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## "Se cair um servidor tem outro" (FrontPUSH)

Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], a vantagem da CDN de bibliotecas é ter "espelhamento" e "recorrência" (redundância): "se cair um servidor tem outro". É failover entre pontos de presença; não envolve banco de dados, como a fala sugere.

## Key sources

- [[wiki/sources/dns]]
- [[wiki/sources/multi-region-global-lb]]
- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]] — fallback entre provedores de LLM na OpenRouter; pool de ≥3
- [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]: FrontPUSH, React aula 04: "servidor espelhado para quando um cair o outro subir", citado como solução de carga
- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: redundância da CDN
