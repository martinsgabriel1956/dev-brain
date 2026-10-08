---
type: concept
title: "Session Management"
aliases: []
date_created: 2026-09-22
date_updated: 2026-10-08
source_count: 5
tags: [session-management]
skill: tech-mentor-security
status: stub
---

# Session Management

Stub criado durante sweep de lint (links quebrados) a partir de referências em 3 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/autenticacao-segura]]: [[wiki/concepts/session-management]]
- Em [[wiki/sources/oauth2-oidc-jwt]]: [[wiki/concepts/session-management]]
- Em [[wiki/sources/sessions]]: [[wiki/concepts/session-management]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Código Fonte TV — cinco tipos de armazenamento

Sessão como dado key-value com TTL: consultada a cada clique, sem relações, pode expirar ([[wiki/concepts/chave-valor]]).

## Key sources


- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]] — sessão como caso canônico de chave-valor com expiração
- [[wiki/sources/autenticacao-segura]]
- [[wiki/sources/oauth2-oidc-jwt]]
- [[wiki/sources/sessions]]
- [[wiki/sources/load-balancer-como-funciona-algoritmos-health-check-nginx-haproxy]] — sessão local em memória + escala horizontal = perda de estado; IP hash como paliativo
