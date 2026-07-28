---
type: concept
title: "Algoritmo de Shor"
aliases: ["shor algorithm", "algoritmo de shor", "fatoracao quantica"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, computacao-quantica, shor, rsa, criptografia-pos-quantica]
skill: tech-mentor-security
status: stable
---

## Definição

Algoritmo quântico capaz de resolver o problema da **fatoração de inteiros em tempo polinomial** — ou seja, de forma eficiente, o que é computacionalmente inviável em computadores clássicos para números grandes. É essa dificuldade de fatoração que garante a segurança do [[wiki/concepts/rsa]]; um computador quântico suficientemente grande, rodando Shor, quebra RSA em minutos, independentemente do tamanho da chave.

## Impacto Prático

Referência da skill `tech-mentor-security` (`references/post-quantum-crypto.md`) estima 10-15 anos para um computador quântico "criptograficamente relevante" — mas o risco já existe hoje via **harvest-now-decrypt-later**: um atacante coleta e armazena tráfego cifrado agora, para decifrá-lo retroativamente quando tiver acesso a poder quântico suficiente. Isso afeta especialmente dados com prazo de sigilo longo (governo, saúde, segredos industriais).

## Algoritmos Vulneráveis vs. Seguros

| Vulnerável a Shor | Seguro pós-Shor |
|---|---|
| RSA (qualquer tamanho de chave) | [[wiki/concepts/aes]] (256 bits, resistente ao Grover) |
| ECDSA / EdDSA / ECDH | SHA-256/SHA-3 |
| Diffie-Hellman clássico | Algoritmos NIST PQC (ML-KEM/Kyber, ML-DSA/Dilithium) |

## Relação com outros conceitos

- [[wiki/concepts/rsa]] — algoritmo diretamente quebrado por Shor
- [[wiki/concepts/grover-algorithm]] — outra ameaça quântica, mas de natureza diferente (busca, não fatoração)
- [[wiki/concepts/post-quantum-cryptography]] — resposta da indústria à ameaça de Shor
- [[wiki/concepts/aes]] — permanece seguro (Grover reduz, Shor não se aplica a cifra simétrica de bloco)

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
