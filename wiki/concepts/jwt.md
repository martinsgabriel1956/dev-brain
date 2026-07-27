---
type: concept
title: "JWT — JSON Web Token"
aliases: ["JWT", "JSON Web Token", "access token", "refresh token"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [jwt, autenticacao, stateless, token, seguranca]
skill: tech-mentor-security
status: draft
---

# JWT — JSON Web Token

Token de autenticação **stateless**: toda a informação necessária para validar a identidade do usuário fica dentro do próprio token, não em uma entrada de banco de dados no servidor. Resolve o problema de escala das [[wiki/concepts/sessoes-http-cookies|sessões tradicionais]], que exigem um armazenamento central (ex.: Redis) consultado a cada requisição.

## Estrutura

Três partes separadas por ponto: `header.payload.signature`.

- **Header**: tipo de token e algoritmo de assinatura (ex.: `HS256`).
- **Payload**: dados (claims) — user ID, permissões, tempo de expiração.
- **Signature**: garante integridade.

Header e payload são codificados em **Base64, não criptografados** — qualquer um pode ler o conteúdo. O que impede alteração é a signature: mudar o payload invalida a assinatura, e o servidor rejeita o token.

```typescript
// Verificação correta — especifique algoritmos permitidos explicitamente
import { verify } from 'jsonwebtoken'

const payload = verify(token, process.env.JWT_SECRET, {
  algorithms: ['HS256'], // nunca deixe vazio ou aceite 'none'
  issuer: 'sua-api',
  audience: 'seu-cliente',
})
```

## Fluxo

1. No login, o servidor gera e assina o JWT, envia para o cliente.
2. Nas próximas requisições, o cliente envia o token no header.
3. O servidor só verifica a assinatura — sem consultar banco de dados. Qualquer servidor com a chave de verificação valida o token, o que escala melhor que sessão centralizada.

## O problema da revogação

Como o JWT é stateless, não dá para invalidar um token antes de expirar sem reintroduzir estado (ex.: uma denylist), o que anula parte do ganho. A solução prática é combinar dois tokens de durações diferentes:

- **Access Token**: curta duração (15min-1h), usado em toda requisição, stateless.
- **Refresh Token**: longa duração (dias/semanas), armazenado no servidor (por isso revogável), usado só para obter um novo Access Token quando o antigo expira.

Se o usuário faz logout ou a conta é comprometida, o servidor marca o Refresh Token como revogado; na próxima tentativa de renovação, o servidor recusa e o usuário precisa autenticar de novo. É o equilíbrio entre requisições rápidas/stateless e controle de revogação centralizado.

## ID Token vs Access Token

No contexto de [[wiki/concepts/openid-connect]], o ID Token é especificamente um JWT com claims padronizadas (`issuer`, `subject`, `audience`) que prova **quem é o usuário**, diferente do Access Token do [[wiki/concepts/oauth2]], que prova **o que o app pode fazer**.

## Relação com outros conceitos

- [[wiki/concepts/sessoes-http-cookies]] — alternativa stateful que o JWT substitui em arquiteturas distribuídas
- [[wiki/concepts/oauth2]] — emite Access Token, frequentemente em formato JWT
- [[wiki/concepts/openid-connect]] — emite o ID Token, sempre em formato JWT
- [[wiki/concepts/token-relay-pattern]] — propagação do token (incluindo JWT) por múltiplos serviços internos
- [[wiki/concepts/criptografia]] — assinatura do JWT usa HMAC (chave simétrica) ou par de chaves assimétrico, dependendo do algoritmo

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
