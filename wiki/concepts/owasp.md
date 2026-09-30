---
type: concept
title: "Owasp"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-30
source_count: 4
tags: [owasp]
skill: tech-mentor-security
status: stub
---

# Owasp

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/api-security]]: [[concepts/owasp]]
- Em [[wiki/sources/owasp-top10]]: [[concepts/owasp]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## OWASP Cheat Sheet Series como origem de decisões de projeto

[[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: o autor recomenda ler todo o Cheat Sheet Series ("se você publica qualquer coisa") e diz que conheceu ali o [[wiki/concepts/cross-site-websocket-hijacking]], que moldou o desenho do [[wiki/entities/omxterm]].

## SQL Injection como Item Histórico do Top 10

[[wiki/sources/sql-injection-sqlmap-luiz-viana]] trata [[wiki/concepts/sql-injection]] como uma das categorias mais conhecidas do OWASP (Injection), demonstrando a exploração ponta a ponta com [[wiki/concepts/sqlmap]] — da quebra manual de query com aspa simples até extração automatizada de dados, leitura de arquivo no servidor e bypass de WAF.

## Key sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — Cheat Sheet Series levou ao desenho anti-CSWSH
- [[wiki/sources/api-security]]
- [[wiki/sources/owasp-top10]]
- [[wiki/sources/sql-injection-sqlmap-luiz-viana]] — SQL Injection explorada ponta a ponta com SQLMap
