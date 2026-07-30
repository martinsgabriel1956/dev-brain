---
type: source
title: "RFC 7636 — Proof Key for Code Exchange by OAuth Public Clients"
aliases: ["rfc 7636", "pkce rfc", "proof key for code exchange"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rfc-7636-pkce-oauth-public-clients.md
source_url: "https://datatracker.ietf.org/doc/html/rfc7636"
author: "N. Sakimura (Ed.), J. Bradley, N. Agarwal — IETF OAuth Working Group"
date_published: "2015-09"
date_ingested: 2026-07-30
source_count: 0
tags: [pkce, oauth2, rfc-7636, ietf, standards-track, code-verifier, code-challenge, authorization-code, seguranca, primary-source]
skill: tech-mentor-security
status: stable
---

## TL;DR

Texto normativo completo do RFC 7636 (IETF, setembro de 2015), traduzido para PT-BR. É a fonte primária que define formalmente o PKCE já documentado em [[wiki/concepts/pkce]] e [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]]: especifica a sintaxe exata do `code_verifier` (43–128 caracteres, ABNF), os dois métodos de `code_challenge` (`plain` e `S256`), os novos parâmetros de protocolo, as regras `MUST`/`SHOULD` de compatibilidade e IANA, e — principal valor agregado desta fonte sobre as anteriores — a seção 7 de Security Considerations, com o raciocínio explícito sobre entropia mínima, por que `S256` é obrigatório e `plain` desaconselhado, e por que não se usa salting no `code_challenge`.

## Key Claims

**Claim:** Clientes públicos OAuth 2.0 usando Authorization Code Grant são vulneráveis a interceptação do código de autorização via apps maliciosos registrados no mesmo custom URI scheme do app legítimo.
**Evidence:** Seção 1 detalha 4 pré-condições do ataque (app malicioso registrável no SO com o mesmo scheme; uso do authorization code grant; atacante com acesso ao `client_id`/`client_secret` compartilhado entre instâncias do app nativo; e capacidade de observar respostas — ou requisições — do authorization endpoint) e ilustra com diagrama de sequência (Figura 1) mostrando o app malicioso interceptando o Authorization Code no passo (4) e trocando-o por access token nos passos (5)-(6).
**Confidence:** alta — fonte primária normativa, é a origem do próprio ataque que motivou o PKCE, já referenciado de forma resumida em [[wiki/concepts/pkce]].

**Claim:** O `code_verifier` deve ser uma string aleatória de alta entropia, entre 43 e 128 caracteres, usando o alfabeto unreserved da RFC 3986 (`[A-Z][a-z][0-9]-._~`).
**Evidence:** ABNF formal na Seção 4.1 (`code-verifier = 43*128unreserved`); nota recomenda gerar 32 octetos aleatórios e codificar em base64url, produzindo exatamente 43 caracteres. Seção 7.1 reforça: mínimo de 256 bits de entropia.
**Confidence:** alta — especificação normativa exata; [[wiki/concepts/pkce]] já cita "32 bytes, base64url" mas sem o limite superior de 128 caracteres nem o ABNF formal, que esta fonte adiciona.

**Claim:** O cliente DEVE usar o método `S256` sempre que tecnicamente capaz; `plain` só é permitido por limitação técnica e mediante conhecimento prévio (fora de banda) de que o servidor o suporta.
**Evidence:** Seção 4.2 define `S256` como Mandatory To Implement (MTI) no servidor. Seção 7.2 explica o porquê: com `plain`, `code_challenge == code_verifier`, então um atacante que observa a *requisição* de autorização (não só a resposta) já obtém o verifier — o método `S256` é o único que protege contra esse cenário mais sofisticado (pré-condição 4b da Seção 1). Reforça: clientes NÃO DEVEM fazer downgrade de `S256` para `plain`.
**Confidence:** alta — detalhe de threat model ausente nas fontes anteriores da wiki, que mencionavam `S256` como exemplo mas não como MTI normativo nem explicavam a diferença de superfície de ataque entre os dois métodos.

**Claim:** O `code_challenge` não usa salting porque o `code_verifier` já contém entropia suficiente (256 bits) para tornar um ataque de força bruta impraticável, diferente de senhas de baixa entropia.
**Evidence:** Seção 7.3 argumenta que concatenar um valor público antes do SHA-256 não aumentaria o número de tentativas necessárias para quebrar um `code_verifier` de 256 bits por força bruta — ao contrário de senhas, onde salting expande o espaço de busca de um dicionário. Nota que GPUs modernas já tornam o salting pouco eficaz mesmo para senhas de baixa entropia.
**Confidence:** alta — raciocínio criptográfico explícito, não presente em nenhuma fonte anterior da wiki sobre PKCE.

**Claim:** Servidores devem aceitar clientes que não implementam PKCE (retrocompatibilidade), mas clientes devem enviar os parâmetros PKCE para todos os servidores independente de saberem se há suporte.
**Evidence:** Seção 5 (Compatibility): se o servidor não recebe `code_verifier`, reverte ao fluxo OAuth 2.0 padrão sem a extensão; como as respostas do servidor OAuth 2.0 não mudam com PKCE, o cliente não precisa negociar suporte — deve simplesmente sempre enviar os parâmetros.
**Confidence:** alta — detalhe operacional ausente em [[wiki/concepts/pkce]], relevante para quem implementa clients que precisam funcionar contra múltiplos Authorization Servers.

## Entities & Concepts Touched

- [[wiki/concepts/pkce]]
- [[wiki/concepts/oauth2]]

## Open Questions

- O RFC define apenas `plain` e `S256` no registro inicial (Seção 6.2.2), mas estabelece um registro IANA extensível para novos `code_challenge_method`s — não há, nesta wiki, nenhuma fonte cobrindo se algum método adicional foi de fato registrado desde 2015.
- Seção 7.5 (TLS Security Considerations) aponta para a BCP 195/RFC 7525 como referência viva de recomendações de TLS — essa RFC não está ingerida na wiki; qualquer claim sobre versão mínima de TLS para PKCE hoje deveria checar a BCP 195 diretamente, não este RFC (que apenas a referencia).
