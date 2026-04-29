---
type: source
title: "Post-Quantum Cryptography (PQC)"
aliases: ["post quantum cryptography", "pqc", "crystals-kyber", "ml-kem", "crystals-dilithium", "ml-dsa", "harvest now decrypt later"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/post-quantum-crypto.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [post-quantum-cryptography, kyber, dilithium, sphincs, nist-pqc, harvest-now-decrypt-later, hybrid-crypto, migration]
skill: tech-mentor-security
status: stable
---

## TL;DR

Computadores quânticos quebrarão RSA e ECC via algoritmo de Shor (fatoração eficiente). NIST padronizou em 2024: CRYSTALS-Kyber/ML-KEM (troca de chave), CRYSTALS-Dilithium/ML-DSA (assinatura). AES-256 e SHA-256 sobrevivem (resistentes a quântico com dobro do tamanho de chave). Ameaça imediata: Harvest-Now-Decrypt-Later — dados coletados hoje serão decriptados quando computador quântico existir.

## Key Claims

**Claim:** Harvest-Now-Decrypt-Later é a ameaça real hoje — dados sensíveis coletados agora podem ser decriptados no futuro.
**Evidence:** Adversários (estado-nação) já coletam tráfego TLS cifrado hoje. Quando computador quântico criptograficamente relevante existir (estimativa: 2030-2040), esses dados são decriptados. Dados com vida útil longa (segredos médicos, documentos governamentais, propriedade intelectual): migrar para PQC agora reduz a janela de vulnerabilidade.
**Confidence:** alta

**Claim:** Abordagem híbrida (clássico + PQC) é o caminho seguro de migração — mantém proteção mesmo que um dos algoritmos seja quebrado.
**Evidence:** TLS 1.3 com `X25519Kyber768Draft00`: combina ECDH (proteção atual) com ML-KEM (proteção pós-quântica). Se ML-KEM for vulnerável (algoritmo novo, menos analisado), ECDH ainda protege. Se computador quântico quebrar ECDH, ML-KEM ainda protege. Custo: overhead de handshake (~40KB vs ~1KB com ECDH puro).
**Confidence:** alta

**Claim:** AES-256 e SHA-256 sobrevivem ao quântico — apenas algoritmos assimétricos (RSA, ECC) são vulneráveis.
**Evidence:** Algoritmo de Grover reduz eficiência de busca em AES pela metade: AES-256 → equivalência de AES-128 contra quântico. Ainda seguro. SHA-256: mesmo raciocínio. RSA e ECC: algoritmo de Shor resolve fatoração de inteiros e logaritmo discreto em tempo polinomial — quebra completamente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/post-quantum-cryptography]]
- [[concepts/crystals-kyber]]
- [[concepts/crystals-dilithium]]
- [[concepts/harvest-now-decrypt-later]]
- [[concepts/hybrid-cryptography]]
- [[concepts/aes-gcm]]

## Open Questions

- Timeline real para computador quântico criptograficamente relevante (CRQC) — 2030 é pessimista ou otimista?
- Implementação de ML-KEM em bibliotecas Node.js/Go — quais têm suporte estável em produção hoje?
