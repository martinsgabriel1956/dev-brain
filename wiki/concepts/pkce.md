---
type: concept
title: "PKCE — Proof Key for Code Exchange"
aliases: ["pkce", "pixi", "proof key for code exchange", "code_verifier", "code_challenge", "rfc 7636"]
date_created: 2026-07-30
date_updated: 2026-08-03
source_count: 4
tags: [pkce, oauth2, oidc, seguranca, authorization-code, implicit-flow, rfc-7636, oauth2-1]
skill: tech-mentor-security
status: draft
---

# PKCE — Proof Key for Code Exchange

Extensão do [[wiki/concepts/oauth2|Authorization Code Flow]] (RFC 7636, 2015) que resolve um problema específico: clientes públicos — single page applications e apps mobile — não têm onde esconder um client secret. Todo o código roda no dispositivo do usuário, então qualquer segredo estático embutido no bundle JS ou no binário é visível a quem abrir o DevTools ou fizer engenharia reversa do app.

A ideia central: trocar o client secret **estático** por um segredo **dinâmico e descartável**, gerado a cada tentativa de login, em vez de acoplado ao código-fonte.

## Por que existe — o problema do Implicit Flow

Antes do PKCE se popularizar, o OAuth tentava resolver autenticação em SPA via **Implicit Flow**: o Authorization Server devolvia o access token direto no fragmento da URL de redirecionamento. Isso criava três falhas graves:

- **Vazamento no histórico** — o token, indo pela barra de endereço, fica salvo no histórico do navegador.
- **Interceptação fácil** — extensões maliciosas, proxies e apps espiões conseguem capturar o token em texto claro no redirecionamento.
- **Falta de prova de posse** — o Authorization Server não tinha como confirmar que quem estava recebendo o token era a mesma instância que iniciou o login.

Por ser um canal considerado inseguro, refresh tokens eram proibidos nesse fluxo — o que forçava o usuário a reautenticar com muito mais frequência. O Implicit Flow foi removido no OAuth 2.1.

## Como funciona

```
1. Client gera code_verifier — string randômica grande (ex.: 32 bytes, base64url)
2. Client aplica hash SHA-256 no code_verifier → code_challenge
3. Client envia code_challenge (+ code_challenge_method=S256) na etapa
   de autorização, junto das credenciais de login do usuário
4. Authorization Server armazena o code_challenge recebido
5. Usuário autentica e recebe o authorization_code (tradicional do OAuth)
6. Client troca o authorization_code por token — mas agora envia o
   code_verifier original (não o hash) junto do pedido
7. Authorization Server reaplica SHA-256 no code_verifier recebido e
   compara com o code_challenge armazenado:
   bate → libera access_token / refresh_token
   não bate → 401
```

```typescript
const codeVerifier = crypto.randomBytes(32).toString('base64url');
const codeChallenge = crypto.createHash('sha256')
    .update(codeVerifier).digest('base64url');

// Etapa de autorização — só o hash viaja na URL
const authUrl = `${authServer}/authorize?response_type=code&client_id=${clientId}` +
    `&code_challenge=${codeChallenge}&code_challenge_method=S256` +
    `&redirect_uri=${redirectUri}&state=${state}`;

// Troca do código por token — code_verifier original, nunca exposto antes
const tokens = await fetch(`${authServer}/token`, {
    method: 'POST',
    body: new URLSearchParams({
        grant_type: 'authorization_code',
        code: authCode,
        code_verifier: codeVerifier,
        redirect_uri: redirectUri,
    }),
});
```

O ponto-chave: mesmo que um atacante intercepte o `authorization_code` (via redirect URI mal configurado, log, etc.), ele não consegue trocá-lo por um token sem o `code_verifier` original — que nunca trafega antes da etapa final, e é descartado após o uso. O par `code_verifier`/`code_challenge` precisa ser altamente volátil e de vida curta.

## Especificação normativa (RFC 7636)

O `code_verifier` tem tamanho definido por ABNF formal: entre 43 e 128 caracteres do alfabeto *unreserved* da RFC 3986 (`[A-Z][a-z][0-9]-._~`). Gerar 32 octetos aleatórios e codificar em base64url produz exatamente os 43 caracteres mínimos com 256 bits de entropia recomendados.

`S256` é *Mandatory To Implement* (MTI) no servidor — o cliente DEVE usá-lo sempre que tecnicamente capaz, e NÃO DEVE fazer downgrade para `plain` depois de tentar `S256`. A razão é a superfície de ataque: com `plain`, `code_challenge == code_verifier`, então um atacante capaz de observar a *requisição* de autorização (não só a resposta) já obtém o verifier — cenário que só `S256` mitiga, pois o hash não é reversível. `plain` existe apenas para compatibilidade com clientes que não conseguem calcular SHA-256.

O `code_challenge` não usa salting: como o `code_verifier` já carrega 256 bits de entropia, concatenar um valor público antes do hash não aumentaria o número de tentativas necessárias para um ataque de força bruta (diferente de senhas de baixa entropia, onde salting expande o espaço de busca de um dicionário).

Servidores DEVEM aceitar clientes que não implementam PKCE (retrocompatibilidade — revertem ao OAuth 2.0 puro se `code_verifier` não for enviado), mas clientes DEVERIAM enviar os parâmetros PKCE para todos os servidores, independente de saberem se há suporte, já que a resposta do servidor OAuth 2.0 não muda com a extensão.

## PKCE no OAuth 2.1

Batizado originalmente como "Proof Key for Code Exchange **by OAuth Public Clients**" — pensado para clientes públicos (SPA, mobile). No **OAuth 2.1**, a recomendação virou universal: PKCE obrigatório para **todos** os clients, inclusive backends robustos que já teriam onde guardar um secret estático. O OAuth 2.1 também formaliza a remoção do Implicit Flow. Perfeitamente utilizável no OAuth 2.0 como extensão, mesmo sem estar no core da spec.

Grandes provedores de identidade (Keycloak, Auth0) e frameworks (Spring Security, NestJS) já implementam PKCE nativamente — o Authorization Server só precisa de um lugar para armazenar temporariamente o `code_challenge` recebido na etapa de autorização.

## Relação com outros conceitos

- [[wiki/concepts/oauth2]] — PKCE é uma extensão do Authorization Code Flow do OAuth
- [[wiki/concepts/jwt]] — o token trocado ao final do fluxo PKCE é, tipicamente, um JWT
- [[wiki/concepts/bff-pattern]] — arquitetura alternativa para o mesmo problema: mover a posse do token para um servidor intermediário em vez de confiar em prova criptográfica no cliente público

## Key Sources

- [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]]
- [[wiki/sources/oauth2-oidc-jwt]]
- [[wiki/sources/rfc-7636-pkce-oauth-public-clients]] — texto normativo original (IETF, 2015), traduzido; fonte da especificação exata (ABNF, MTI de S256, security considerations)
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — reforço da motivação (apps mobile não guardam client_secret com segurança) no fluxo de ponta a ponta de autenticação
