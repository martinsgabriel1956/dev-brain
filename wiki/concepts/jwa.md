---
type: concept
title: "JWA — JSON Web Algorithms"
aliases: ["JWA", "JSON Web Algorithms", "RFC 7518"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [jwa, jose, jwt, cipher-agility, algorithm-confusion, seguranca]
skill: tech-mentor-security
status: draft
---

# JWA — JSON Web Algorithms

Especificação do ecossistema [[wiki/concepts/jose]] (RFC 7518) que define o **catálogo de algoritmos criptográficos** válidos para assinar ([[wiki/concepts/jws]]), criptografar ([[wiki/concepts/jwe]]) ou proteger tokens [[wiki/concepts/jwt|JWT]] — em outras palavras, a lista de algoritmos que um token JOSE pode declarar sem fugir da especificação (ex.: `HS256`, `RS256`, `ES256`, `none`).

## O ponto crítico: fonte da cipher agility

O JWA é, na prática, a **origem técnica da [[wiki/concepts/cipher-agility|cipher agility]]** do ecossistema JOSE: ao oferecer uma lista extensa de algoritmos — alguns hoje considerados fracos ou obsoletos, e incluindo o valor `none` — ele delega ao **desenvolvedor** a responsabilidade de escolher (e restringir) o que é seguro. Quando essa escolha não é feita explicitamente — biblioteca configurada no default, sem whitelist — a superfície fica aberta ao ataque de **[[wiki/concepts/algorithm-confusion]]**.

Esse é o trade-off central discutido em [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]: o mesmo mecanismo que permite migrar de um algoritmo obsoleto para um moderno sem quebrar compatibilidade é o que permite a um atacante forçar o verificador a aceitar um algoritmo mais fraco (ou nenhum).

## Relação com outros conceitos

- [[wiki/concepts/jose]] — conceito pai
- [[wiki/concepts/cipher-agility]] — a filosofia de design que o JWA viabiliza
- [[wiki/concepts/algorithm-confusion]] — o ataque que explora a falta de whitelist sobre os algoritmos do JWA
- [[wiki/concepts/paseto]] — resposta de design oposta: cipher rigidity, sem catálogo de algoritmos negociável

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
