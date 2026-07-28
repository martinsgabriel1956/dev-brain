---
type: concept
title: "Key Distribution Problem"
aliases: ["problema de distribuicao de chaves", "troca de chaves segura"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, criptografia-simetrica, criptografia-assimetrica]
skill: tech-mentor-security
status: stub
---

## Definição

Problema central da criptografia simétrica ([[wiki/concepts/aes]]): como transmitir a chave secreta compartilhada entre duas partes de forma segura, se o próprio canal de comunicação é inseguro? Enviar por e-mail expõe a um invasor; enviar por mensagem pode vazar; combinar pessoalmente não escala para várias pessoas.

## Solução: Criptografia Assimétrica

A resposta histórica foi inverter o modelo: em vez de uma única chave secreta, um **par de chaves** — pública (distribuível livremente) e privada (nunca sai do dono). O [[wiki/concepts/rsa]] foi a implementação citada como exemplo. Na prática moderna (TLS/HTTPS), o padrão é híbrido: usa-se a troca assimétrica só para negociar uma chave de sessão simétrica, que então cifra o volume real de dados.

## Relação com outros conceitos

- [[wiki/concepts/aes]] — criptografia simétrica, onde o problema se manifesta
- [[wiki/concepts/rsa]] — solução assimétrica ao problema
- [[wiki/concepts/criptografia]] — contexto geral (seção HTTPS já documenta o modelo híbrido)

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
