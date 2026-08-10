---
type: concept
title: "Open Redirect (em Fluxos OAuth)"
aliases: ["open redirect", "redirect_uri malicioso", "validação de redirect URI"]
date_created: 2026-08-03
date_updated: 2026-08-06
source_count: 2
tags: [open-redirect, oauth2, seguranca, autorizacao]
skill: tech-mentor-security
status: stub
---

# Open Redirect (em Fluxos OAuth)

Falha em que o Authorization Server de um fluxo [[wiki/concepts/oauth2|OAuth]] aceita uma `redirect_uri` que não corresponde exatamente à URL registrada pelo client, permitindo que o atacante redirecione o **código de autorização** para um domínio próprio.

## Como funciona

```
1. Client registra redirect_uri = https://app.com/callback
2. Se o Authorization Server valida por prefixo/wildcard (ex.: aceita
   qualquer coisa começando com "https://app.com"), o atacante monta:
   https://app.com.attacker.com/callback ou https://app.com@attacker.com/callback
3. Vítima completa o login legítimo, mas o browser é redirecionado
   para o domínio do atacante — levando o authorization_code junto
4. Atacante troca o código pelo access_token (se não houver PKCE),
   ou pelo menos captura informações sensíveis da URL
```

## Mitigação

A validação da `redirect_uri` deve ser uma **comparação exata, caractere por caractere**, contra uma lista de URIs pré-registradas — nunca por prefixo, substring ou wildcard. É a mesma classe de erro de outras validações de URL mal feitas (ex.: checar `.includes("app.com")` em vez de igualdade estrita).

## Variante: escopo/permissão aceito via URL sem validação

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], um pentest encontrou uma variante desse tipo de falha no SaaS "Find My SaaS": não era estritamente a `redirect_uri` que faltava validação, e sim parâmetros de escopo/permissão do Authorization Request aceitos pela URL sem checagem — permitindo um link malicioso que solicitava permissões além do padrão do app. O relato original não detalha se `redirect_uri` também estava envolvido; tratado como caso adjacente à mesma família de erro (confiar em parâmetros de URL de um fluxo OAuth sem validação server-side estrita). Ver [[wiki/concepts/oauth2]] para o caso completo.

## Relação com outros conceitos

- [[wiki/concepts/oauth2]] — o `redirect_uri` é parâmetro central do Authorization Code Flow; open redirect explora sua validação frouxa
- [[wiki/concepts/pkce]] — mitiga parcialmente o impacto (o atacante ainda precisaria do `code_verifier` para trocar o código por token), mas não substitui a validação exata da URI

## Key Sources

- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — variante com parâmetros de escopo/permissão aceitos sem validação
