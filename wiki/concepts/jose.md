---
type: concept
title: "JOSE — JSON Object Signing and Encryption"
aliases: ["JOSE", "JSON Object Signing and Encryption", "ecossistema JOSE"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [jose, jwt, jws, jwe, jwk, jwa, seguranca, criptografia]
skill: tech-mentor-security
status: draft
---

# JOSE — JSON Object Signing and Encryption

Conjunto de especificações do IETF que define **como** um token JSON deve ser assinado e/ou criptografado. O [[wiki/concepts/jwt|JWT]] é o **formato** de token; JOSE é o guarda-chuva de especificações que rege esse formato — a grosso modo, um JWT é uma instância de um token JOSE.

## Os Quatro Pilares

- [[wiki/concepts/jws]] — **JSON Web Signature**: integridade e autenticidade via assinatura digital. O payload permanece legível.
- [[wiki/concepts/jwe]] — **JSON Web Encryption**: confidencialidade via criptografia autenticada. O payload fica cifrado.
- [[wiki/concepts/jwk]] — **JSON Web Key**: representação de chaves criptográficas em formato JSON.
- [[wiki/concepts/jwa]] — **JSON Web Algorithms**: catálogo de algoritmos criptográficos válidos para os outros três pilares.

## O Custo da Flexibilidade

O JOSE foi desenhado com **[[wiki/concepts/cipher-agility|cipher agility]]** — suporte simultâneo a múltiplos algoritmos, escolhidos via metadado no próprio header do token. Essa flexibilidade é exatamente o que abre espaço para o ataque de **[[wiki/concepts/algorithm-confusion]]**: como o header é controlado pelo cliente, um back end que confia nele sem whitelist explícita pode ser enganado a aceitar um algoritmo mais fraco — ou nenhum algoritmo.

A alternativa de design oposta é o **[[wiki/concepts/paseto]]**, que adota "cipher rigidity" (versões fixas, sem escolha de algoritmo pelo cliente) especificamente para eliminar essa classe de vulnerabilidade.

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — formato concreto de token que instancia as especificações JOSE
- [[wiki/concepts/criptografia]] — base teórica (simétrica/assimétrica) usada por JWS e JWE
- [[wiki/concepts/rfc-request-for-comments]] — JWS/JWE/JWK/JWA são RFCs do IETF (7515–7518)

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
