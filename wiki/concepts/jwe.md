---
type: concept
title: "JWE — JSON Web Encryption"
aliases: ["JWE", "JSON Web Encryption", "RFC 7516"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [jwe, jose, jwt, confidencialidade, seguranca, criptografia]
skill: tech-mentor-security
status: draft
---

# JWE — JSON Web Encryption

Especificação do ecossistema [[wiki/concepts/jose]] (RFC 7516, 2015) voltada para **confidencialidade**: diferente do [[wiki/concepts/jws]], que apenas assina os dados (payload continua legível em base64), o JWE **criptografa** o payload em texto cifrado. Sem a chave de decriptação, ninguém — nem o cliente que carrega o token — consegue ler o conteúdo.

É o padrão indicado quando o token precisa transportar dado sensível (dado pessoal, segredo de negócio) que não pode ficar exposto, ao contrário do JWT/JWS comum, onde a recomendação padrão é justamente **nunca** colocar dado sensível no payload porque ele é apenas codificado, não cifrado (ver [[wiki/concepts/jwt#Onde Armazenar o Token no Cliente]] e a nota de payload mínimo).

## Estrutura: cinco partes

Diferente das três partes do JWS, o JWE é composto por: **header**, **chave de criptografia cifrada**, **vetor de inicialização (IV)**, **cipher text** e **authentication tag**.

## Fluxo de criação

1. Header com os algoritmos especificados, codificado em base64.
2. Gera-se a **Content Encryption Key (CEK)** — chave simétrica aleatória.
3. Gera-se um **IV** aleatório.
4. Criptografa-se o payload com a CEK + IV usando um algoritmo de criptografia **autenticada** (ex.: AES-GCM) → produz cipher text + tag.
5. Criptografa-se a própria CEK com a chave **pública** do destinatário.
6. Concatenam-se as cinco partes, cada uma em base64.

## Fluxo de decodificação

1. Separa as cinco partes.
2. Decodifica o header.
3. Descriptografa a CEK com a chave **privada** do destinatário (o destinatário — não necessariamente o cliente — precisa ter essa chave).
4. Usa a CEK + IV + tag para descriptografar o cipher text, validando a tag no processo.

Bibliotecas modernas de JWE abstraem esse fluxo — normalmente basta um `encrypt(payload, publicKey)`.

## Relação com outros conceitos

- [[wiki/concepts/jose]] — conceito pai
- [[wiki/concepts/jws]] — contraparte de integridade/autenticidade (assina, não cifra)
- [[wiki/concepts/jwt]] — payload em claro por padrão; JWE é a opção quando isso é inaceitável
- [[wiki/concepts/criptografia]] — base de criptografia autenticada (AES-GCM) e assimétrica reaplicada aqui

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
