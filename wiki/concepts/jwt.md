---
type: concept
title: "JWT — JSON Web Token"
aliases: ["JWT", "JSON Web Token", "access token", "refresh token"]
date_created: 2026-07-27
date_updated: 2026-09-01
source_count: 5
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

## HMAC vs. RSA/ECDSA: Qual Algoritmo de Assinatura Usar

- **HMAC** (`HS256`): chave **simétrica** — a mesma chave assina e verifica. Adequado quando um único servidor faz tudo, já que qualquer parte que verifica precisa ter acesso à mesma chave que assina (o que a torna sensível: quem consegue verificar também consegue forjar).
- **RSA/ECDSA** (`RS256`/`ES256`): par **assimétrico** — a chave privada assina, a chave pública verifica. Essencial em microsserviços: cada serviço só precisa da chave pública para validar tokens, e a chave privada nunca sai do servidor de autenticação, eliminando o risco de qualquer serviço consumidor conseguir forjar tokens.

## Chave Fraca e Falta de Validação de Issuer/Audience

Duas falhas comuns de implementação:

- **Chave secreta HMAC fraca** (`secret`, `password123`): um atacante testa um dicionário de chaves comuns e, se acertar, forja qualquer token. A chave precisa ter pelo menos 256 bits de entropia, gerada aleatoriamente, nunca hardcoded — sempre em variável de ambiente.
- **Verificar só a assinatura, ignorando `issuer`/`audience`**: sem checar essas claims, um token emitido para o serviço A pode ser reutilizado no serviço B. Cada API deve validar que o token veio da fonte esperada (`issuer`) e foi emitido para ela especificamente (`audience`) — não basta a assinatura bater.

## Onde Armazenar o Token no Cliente

- **`localStorage`**: simples de acessar via JavaScript, mas por isso mesmo qualquer script malicioso injetado via [[wiki/concepts/xss|XSS]] também consegue ler e exfiltrar o token.
- **Cookie `HttpOnly`**: JavaScript não consegue acessar, e o browser envia automaticamente em toda requisição — a opção recomendada para aplicações web.

Regra prática: em aplicação web, prefira cookie `HttpOnly` sobre `localStorage` para guardar o token.

## Rotação do Refresh Token

Boa prática de revogação: a cada uso do refresh token, o servidor invalida aquele token e emite um novo no lugar (rotação). Se um atacante roubou um refresh token antigo mas o dono legítimo já o usou (disparando a rotação), o token roubado deixa de funcionar — reduz a janela de exploração de um refresh token vazado sem exigir denylist ativa. Detalhamento completo (reuse detection, fingerprinting de dispositivo) em [[wiki/concepts/refresh-token-rotation]].

## Janela de Exposição

Mesmo com refresh token revogável, o Access Token já emitido continua válido até expirar — nada verifica revogação a cada requisição enquanto ele não expira. Se um usuário é banido, o pior caso é ele continuar acessando o sistema pelo tempo de vida restante do Access Token (tipicamente 5-15min). Só a *renovação* via refresh token é bloqueada a partir daí. Esse risco residual costuma ser aceitável (redes sociais, e-commerce, backoffice), mas sistemas de alta criticidade — pagamentos instantâneos, operações financeiras de alto valor, tempo real — podem não tolerar nem essa janela curta, exigindo repensar o modelo de autenticação.

## Access Token de Longa Duração é uma Falha de Segurança

Um JWT com validade de meses ou anos parece resolver a fricção de relogin, mas amplia o risco: por ser auto-contido e stateless, o token trafega por logs de servidor, VPNs, load balancers e serviços de nuvem intermediários — qualquer vazamento nesses pontos dá ao atacante acesso pelo prazo de validade inteiro, já que não há como revogá-lo antes de expirar. Analogia útil: o Access Token deveria funcionar como um crachá de visitante que expira no fim do dia, não como uma chave real de fechadura.

## O problema da revogação

Como o JWT é stateless, não dá para invalidar um token antes de expirar sem reintroduzir estado (ex.: uma denylist), o que anula parte do ganho. A solução prática é combinar dois tokens de durações diferentes:

- **Access Token**: curta duração (15min-1h), usado em toda requisição, stateless.
- **Refresh Token**: longa duração (dias/semanas), armazenado no servidor (por isso revogável), usado só para obter um novo Access Token quando o antigo expira.

Se o usuário faz logout ou a conta é comprometida, o servidor marca o Refresh Token como revogado; na próxima tentativa de renovação, o servidor recusa e o usuário precisa autenticar de novo. É o equilíbrio entre requisições rápidas/stateless e controle de revogação centralizado.

## O Ecossistema JOSE por Trás do JWT

O JWT é apenas o **formato**; quem define como ele é assinado e/ou criptografado é o ecossistema [[wiki/concepts/jose|JOSE]] (JSON Object Signing and Encryption) — quatro especificações do IETF: [[wiki/concepts/jws]] (assinatura — o que este documento descreve acima), [[wiki/concepts/jwe]] (criptografia do payload, para quando dado sensível não pode ficar nem em base64), [[wiki/concepts/jwk]] (formato JSON para publicar/rotacionar chaves públicas via endpoint `.well-known/jwks.json`) e [[wiki/concepts/jwa]] (catálogo de algoritmos válidos).

O JWA é a origem de um trade-off importante: por listar múltiplos algoritmos válidos e permitir que o header do próprio token declare qual usar ([[wiki/concepts/cipher-agility|cipher agility]]), ele abre a superfície para o ataque de **[[wiki/concepts/algorithm-confusion]]** — um verificador que confia cegamente no `alg` do header pode ser enganado a aceitar `alg: none` (sem assinatura) ou a confundir um algoritmo assimétrico com um simétrico. A defesa é a mesma já recomendada acima: sempre declarar `algorithms: [...]` explicitamente na verificação, nunca deixar o token decidir seu próprio algoritmo.

A alternativa que elimina essa classe de ataque por design é o [[wiki/concepts/paseto]], que troca a flexibilidade de algoritmo por versões fixas e imutáveis.

## ID Token vs Access Token

No contexto de [[wiki/concepts/openid-connect]], o ID Token é especificamente um JWT com claims padronizadas (`issuer`, `subject`, `audience`) que prova **quem é o usuário**, diferente do Access Token do [[wiki/concepts/oauth2]], que prova **o que o app pode fazer**.

## Relação com outros conceitos

- [[wiki/concepts/sessoes-http-cookies]] — alternativa stateful que o JWT substitui em arquiteturas distribuídas
- [[wiki/concepts/oauth2]] — emite Access Token, frequentemente em formato JWT
- [[wiki/concepts/openid-connect]] — emite o ID Token, sempre em formato JWT
- [[wiki/concepts/token-relay-pattern]] — propagação do token (incluindo JWT) por múltiplos serviços internos
- [[wiki/concepts/criptografia]] — assinatura do JWT usa HMAC (chave simétrica) ou par de chaves assimétrico, dependendo do algoritmo
- [[wiki/concepts/refresh-token-rotation]] — aprofundamento da rotação: reuse detection e fingerprinting de dispositivo
- [[wiki/concepts/jose]] — ecossistema de especificações (JWS/JWE/JWK/JWA) que define como o JWT é assinado/criptografado
- [[wiki/concepts/algorithm-confusion]] — ataque que explora a cipher agility do JWA quando o servidor confia no `alg` do header
- [[wiki/concepts/paseto]] — alternativa de cipher rigidity que elimina algorithm confusion por design

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — HMAC vs. RSA/ECDSA, chave fraca, validação de issuer/audience, localStorage vs. cookie httpOnly, rotação de refresh token
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — o ID Token do OIDC é um JWT distinto do access token, destinado à aplicação cliente (não à API)
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — janela de exposição, por que Access Token de longa duração é falha de segurança, e por que armazenar refresh token só no backend quebra o fluxo stateless
- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]] — ecossistema JOSE (JWS/JWE/JWK/JWA) por trás do JWT, ataque de algorithm confusion (`alg: none` e RS256→HS256), e o PASETO como alternativa de cipher rigidity
