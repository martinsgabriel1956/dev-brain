---
type: concept
title: "AES (Advanced Encryption Standard)"
aliases: ["aes", "aes-256", "aes-gcm", "advanced encryption standard"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, aes, criptografia-simetrica, cifra-por-bloco]
skill: tech-mentor-security
status: stable
---

## Definição

Algoritmo de **criptografia simétrica por blocos** — a mesma chave criptografa e descriptografa, e os dados são processados em grupos fixos de bits por vez (diferente de cifras de fluxo, que processam byte a byte). Suporta chaves de 128, 192 ou 256 bits; o tamanho da chave determina o número de rodadas de embaralhamento (substituição de bytes, rotação de linhas da matriz, transformação matemática nas colunas). Até hoje nenhuma vulnerabilidade foi encontrada no AES quando usado corretamente.

Usado em Wi-Fi (WPA2/3), criptografia de disco, VPNs, e é o padrão de referência para dados em repouso — ver `references/crypto.md` da skill `tech-mentor-security` para o modo GCM (autenticado) em detalhe.

## O Problema que a Criptografia Simétrica Não Resolve

AES é rápido e eficiente, mas carrega o [[wiki/concepts/key-distribution-problem]]: como transmitir a chave secreta compartilhada de forma segura entre as partes sem que ela vaze no caminho. É esse problema que motiva a existência do [[wiki/concepts/rsa]] e da criptografia assimétrica.

## Resistência à Computação Quântica

Diferente do [[wiki/concepts/rsa]], o AES-256 permanece considerado seguro mesmo pós [[wiki/concepts/grover-algorithm]] — a aceleração quadrática de Grover reduz a segurança efetiva para o equivalente a ~128 bits, ainda aceitável.

## Relação com outros conceitos

- [[wiki/concepts/vigenere-cipher]] — ancestral histórico do princípio de chave simétrica compartilhada
- [[wiki/concepts/rsa]] — par assimétrico que resolve o problema de distribuição de chave do AES
- [[wiki/concepts/key-distribution-problem]] — limitação central da criptografia simétrica
- [[wiki/concepts/grover-algorithm]] — ameaça quântica mitigada (AES permanece seguro)
- [[wiki/concepts/criptografia]] — contexto geral

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
- [[wiki/sources/criptografia-fundamentos]]
