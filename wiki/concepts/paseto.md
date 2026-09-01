---
type: concept
title: "PASETO — Platform Agnostic Security Token"
aliases: ["PASETO", "Platform Agnostic Security Token", "cipher rigidity token"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [paseto, jwt, jose, cipher-rigidity, algorithm-confusion, seguranca, criptografia]
skill: tech-mentor-security
status: draft
---

# PASETO — Platform Agnostic Security Token

Especificação de token de segurança desenhada como alternativa inerentemente segura ao [[wiki/concepts/jwt|JWT]]/ecossistema [[wiki/concepts/jose|JOSE]], adotando **cipher rigidity** (rigidez de cifra) — o oposto filosófico da [[wiki/concepts/cipher-agility|cipher agility]] que caracteriza o JOSE.

## Diferença central: sem negociação de algoritmo

Enquanto o JWT permite que o cliente declare o algoritmo no header (a raiz do ataque de [[wiki/concepts/algorithm-confusion]]), o PASETO usa **versões fixas e imutáveis** — V1, V2, V3, V4 — cada uma implementando um único conjunto de algoritmos criptográficos modernos e de alta performance (ex.: **Ed25519** para assinatura, **AES-256-GCM** para criptografia autenticada). Não há campo de algoritmo negociável no token: a versão *é* o algoritmo. Isso impede completamente ataques de algorithm confusion e a variante `alg: none`, por eliminar a superfície de decisão que os causa.

## Purpose: local vs. public

No PASETO, escolhe-se entre dois propósitos:

- **`local`** — token **criptografado**, análogo ao [[wiki/concepts/jwe|JWE]]: payload cifrado, ilegível sem a chave.
- **`public`** — token **assinado**, análogo ao [[wiki/concepts/jws|JWS]]: payload legível (mesmas ressalvas de não colocar dado sensível em claro), porém imutável e verificável.

## Estrutura

Três partes, mas diferentes das do JWT: **versão** (`v1`–`v4`), **purpose** (`local` ou `public`) e **payload** — sem o header completo do JWT, já que a versão substitui a necessidade de declarar o algoritmo.

## Trade-off

PASETO troca a flexibilidade do JOSE (poder trocar algoritmo sem reescrever código) pela eliminação de uma classe inteira de vulnerabilidade de implementação. Recomendado especialmente para projetos novos que não têm compromisso de compatibilidade retroativa com JWT — não é um substituto drop-in, é uma escolha de design desde o início.

## Relação com outros conceitos

- [[wiki/concepts/cipher-agility]] — princípio de design que o PASETO rejeita deliberadamente
- [[wiki/concepts/algorithm-confusion]] — classe de ataque que o PASETO elimina por design
- [[wiki/concepts/jwt]] — alternativa direta, mesmo caso de uso (token autocontido de autenticação/autorização)
- [[wiki/concepts/jws]] / [[wiki/concepts/jwe]] — análogos conceituais dos purposes `public`/`local` do PASETO

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
