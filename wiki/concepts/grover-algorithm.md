---
type: concept
title: "Algoritmo de Grover"
aliases: ["grover algorithm", "algoritmo de grover", "busca quadratica quantica"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, computacao-quantica, grover, criptografia-pos-quantica]
skill: tech-mentor-security
status: stable
---

## Definição

Algoritmo quântico que oferece uma **aceleração quadrática** para busca em dados não ordenados. Diferente do [[wiki/concepts/shor-algorithm]], Grover não quebra diretamente um esquema de criptografia — mas acelera consideravelmente ataques de força bruta contra qualquer espaço de busca, incluindo chaves simétricas.

## Impacto no AES

Para o [[wiki/concepts/aes]], Grover reduz a segurança efetiva pela metade em termos de bits — AES-256 se torna equivalente a uma busca de força bruta de ~128 bits, o que ainda é considerado seguro na prática (referência da skill `tech-mentor-security`, `references/post-quantum-crypto.md`). Por isso a resposta da indústria a Grover, ao contrário da resposta a Shor, é simplesmente usar chaves simétricas maiores (256 bits), não trocar de algoritmo.

## Relação com outros conceitos

- [[wiki/concepts/shor-algorithm]] — outra ameaça quântica; Shor quebra fatoração (RSA), Grover acelera busca (força bruta)
- [[wiki/concepts/aes]] — impacto mitigável apenas aumentando o tamanho de chave
- [[wiki/concepts/post-quantum-cryptography]] — contexto mais amplo da resposta da indústria

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
