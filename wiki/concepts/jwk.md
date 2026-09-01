---
type: concept
title: "JWK — JSON Web Key"
aliases: ["JWK", "JSON Web Key", "JWKS", "jwks.json", "RFC 7517"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [jwk, jose, jwt, rotacao-de-chave, seguranca]
skill: tech-mentor-security
status: draft
---

# JWK — JSON Web Key

Especificação do ecossistema [[wiki/concepts/jose]] (RFC 7517) que padroniza como **chaves criptográficas** devem ser representadas e transportadas em formato JSON — eliminando a necessidade de lidar com formatos binários/complexos como arquivos `.pem`.

## Como funciona na prática

Um servidor de autorização publica suas chaves **públicas** em um endpoint, tipicamente `/.well-known/jwks.json` (o conjunto de chaves é chamado de JWKS — JSON Web Key Set). APIs consumidoras baixam esse JSON dinamicamente e usam o campo **`kid`** (Key ID) presente no header do [[wiki/concepts/jwt|token]] para localizar a chave pública correta e validar a assinatura ([[wiki/concepts/jws]]) — sem precisar de chave hardcoded em código ou variável de ambiente.

## Por que isso importa

- **Rotação de chave sem downtime**: o authorization server pode publicar uma chave nova no JWKS, assinar novos tokens com ela, e o `kid` no header direciona os verificadores para a chave certa automaticamente — os dois conjuntos de chave (antiga e nova) convivem até os tokens antigos expirarem.
- **Múltiplos algoritmos simultâneos**: cada entrada do JWKS pode declarar seu próprio algoritmo, permitindo migração gradual de um algoritmo para outro.

## Relação com outros conceitos

- [[wiki/concepts/jose]] — conceito pai
- [[wiki/concepts/jws]] — a chave publicada via JWK é usada para validar a assinatura JWS
- [[wiki/concepts/jwt]] — o `kid` no header do JWT referencia uma entrada do JWKS

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
