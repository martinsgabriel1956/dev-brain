---
type: concept
title: "Criptografia Pós-Quântica"
aliases: ["post-quantum cryptography", "pqc", "criptografia pos-quantica", "harvest now decrypt later", "colha agora decifre depois"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, computacao-quantica, criptografia-pos-quantica, nist-pqc]
skill: tech-mentor-security
status: stub
---

## Definição

Conjunto de algoritmos criptográficos projetados para resistir a ataques de computadores quânticos, especificamente ao [[wiki/concepts/shor-algorithm]] (quebra RSA/ECDSA por fatoração/logaritmo discreto) e, em menor grau, ao [[wiki/concepts/grover-algorithm]] (acelera busca por força bruta).

## Harvest-Now-Decrypt-Later

A ameaça não é hipotética-futura, é presente: um atacante pode coletar e armazenar hoje tráfego cifrado com RSA/ECDSA (TLS, VPN, e-mail), e decifrá-lo retroativamente assim que um computador quântico suficientemente potente existir. Dados com prazo de sigilo longo (décadas — saúde, governo, defesa, propriedade intelectual) precisam de proteção pós-quântica *já*, mesmo que o computador quântico "relevante" esteja estimado em 10-15 anos de distância.

## Padrões NIST (2024)

| Algoritmo | Substitui | Uso |
|---|---|---|
| ML-KEM (CRYSTALS-Kyber) | ECDH | Encapsulamento/troca de chave |
| ML-DSA (CRYSTALS-Dilithium) | ECDSA | Assinatura digital |
| SLH-DSA (SPHINCS+) | — | Assinatura baseada em hash, mais conservadora |

Estratégia recomendada de transição: **TLS híbrido** (ex.: X25519 + ML-KEM-768) — combina algoritmo clássico com pós-quântico, protegendo a sessão mesmo que só um dos dois seja quebrado.

## Relação com outros conceitos

- [[wiki/concepts/shor-algorithm]] — ameaça que motiva a migração
- [[wiki/concepts/grover-algorithm]] — ameaça secundária, mitigada por chaves simétricas maiores
- [[wiki/concepts/rsa]] — algoritmo que a criptografia pós-quântica busca substituir
- [[wiki/concepts/aes]] — permanece seguro, não precisa de substituição pós-quântica

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
