---
type: concept
title: "Session Fixation"
aliases: ["session fixation", "fixação de sessão", "sessão fixada"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [session-fixation, sessao, autenticacao, seguranca, cookie]
skill: tech-mentor-security
status: stub
---

# Session Fixation

Ataque em que o atacante **planta** um session ID conhecido no browser da vítima antes dela se autenticar, e depois usa esse mesmo ID para herdar a sessão já autenticada.

## Como funciona

```
1. Atacante obtém/gera um session ID válido (ex.: visitando o site)
2. Atacante induz a vítima a usar esse mesmo session ID
   (ex.: link com session ID na URL, ou cookie plantado via subdomínio)
3. Vítima faz login normalmente — mas o servidor reaproveita o session ID
   já conhecido pelo atacante, em vez de gerar um novo
4. Atacante usa o mesmo session ID e herda a sessão autenticada da vítima
```

A falha central não é o roubo de um identificador — é o servidor **não trocar** o session ID no momento em que o nível de privilégio muda (anônimo → autenticado).

## Mitigação

**Regenerar o session ID sempre após o login** (e idealmente em qualquer mudança de privilégio, como elevação a admin), invalidando explicitamente o ID anterior. A maioria dos frameworks web faz isso automaticamente ao chamar o equivalente de "regenerate session" no login — mas vale confirmar em vez de assumir.

## Relação com outros conceitos

- [[wiki/concepts/sessoes-http-cookies]] — session fixation é um ataque específico contra o modelo de sessão stateful baseado em cookie
- [[wiki/concepts/autenticacao-e-autorizacao]] — explora a transição do momento "não autenticado" para "autenticado"

## Key Sources

- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]]
