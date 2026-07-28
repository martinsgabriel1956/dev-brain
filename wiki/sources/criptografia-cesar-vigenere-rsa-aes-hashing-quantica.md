---
type: source
title: "Criptografia — de César aos Computadores Quânticos"
aliases: ["cifra de cesar historia", "vigenere", "scytale", "ind-cpa", "shor grover", "colha agora decifre depois"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/criptografia-cesar-vigenere-rsa-aes-hashing-quantica.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [criptografia, historia, caesar-cipher, scytale, vigenere, enigma, aes, rsa, ind-cpa, shor, grover, criptografia-pos-quantica, hashing, password-hashing, bcrypt, argon2, salt, pepper, rainbow-table]
skill: tech-mentor-security
status: stable
---

## TL;DR

Percurso histórico da criptografia, da cifra de César e da cítala espartana (criatividade, não matemática) até a cifra de Vigenère (primeira substituição polialfabética, "indecifrável" por 300 anos) e a máquina Enigma (quebrada por reuso de chave). Chega à criptografia moderna: simétrica (AES, rápida, mas com o key distribution problem) vs. assimétrica (RSA, baseado na dificuldade de fatoração de primos grandes, resolve a distribuição via par público/privado). Introduz IND-CPA como modelo formal de segurança — demonstra que a cifra de César falha nele por preservar padrão de repetição de caracteres. Cobre a ameaça quântica (Shor quebra fatoração em tempo polinomial, Grover acelera busca quadraticamente) e o ataque "colha agora, decifre depois". Fecha com hashing determinístico como falha de segurança em senhas (rainbow tables) e a defesa via salt + pepper + BCrypt (EKS-Blowfish, lento de propósito, limite de 72 caracteres) + Argon2id (memory-hard, três fases).

## Key Claims

**Claim:** A cifra de César não é IND-CPA segura porque preserva o padrão de repetição de caracteres da mensagem original no ciphertext.
**Evidence:** Ao criptografar duas mensagens candidatas do mesmo tamanho, a mensagem cujas posições de repetição de uma letra (ex.: "E") coincidem com as posições de repetição de uma letra na cifra (ex.: "H") é identificável — porque a substituição César é sempre a mesma letra → mesma letra, exposição direta de frequência/padrão.
**Confidence:** alta — consistente com a fraqueza clássica de cifras monoalfabéticas por análise de frequência, já documentada em [[wiki/concepts/caesar-cipher]].

**Claim:** A cifra de Vigenère era considerada "indecifrável" por mais de 300 anos.
**Evidence:** É a primeira cifra polialfabética popularizada (c. 1500) — a mesma letra da mensagem pode virar letras diferentes da cifra dependendo da posição da chave repetida, quebrando a análise de frequência simples que derruba o César. Só foi quebrada com o método de Kasiski/Friedman (não detalhado na fonte).
**Confidence:** média — afirmação histórica repetida na fonte sem citar o método de quebra; consistente com o que é conhecido publicamente sobre a cifra.

**Claim:** A máquina Enigma foi quebrada porque operadores repetiam a chave.
**Evidence:** Fonte afirma isso como causa direta, sem detalhar a criptoanálise de Turing/Bletchley Park (explicitamente fora de escopo — "tem um filme só para isso").
**Confidence:** média — simplificação; a quebra histórica envolveu múltiplas fraquezas operacionais e criptoanálise formal, não só repetição de chave.

**Claim:** BCrypt faz hash apenas dos 72 primeiros caracteres da senha; qualquer excesso é ignorado.
**Evidence:** Limitação do algoritmo EKS-Blowfish subjacente ao BCrypt.
**Confidence:** alta — limitação conhecida e documentada de implementações de BCrypt.

**Claim:** O algoritmo de Shor ameaça RSA porque resolve fatoração de inteiros em tempo polinomial; o algoritmo de Grover acelera busca não ordenada quadraticamente, mas não quebra criptografia simétrica diretamente.
**Evidence:** Consistente com `references/post-quantum-crypto.md` da skill: AES-256 permanece seguro pós-Grover (equivalente a ~128 bits), enquanto RSA/ECDSA são quebrados por Shor.
**Confidence:** alta.

**Claim:** "Colha agora, decifre depois" (harvest-now-decrypt-later) é uma ameaça presente mesmo sem computador quântico disponível hoje.
**Evidence:** Atacante coleta e armazena ciphertext hoje para decifrar quando tiver poder computacional quântico suficiente.
**Confidence:** alta — mesmo conceito documentado em `references/post-quantum-crypto.md` (HNDL).

## Entities & Concepts Touched

- [[wiki/concepts/caesar-cipher]]
- [[wiki/concepts/scytale]]
- [[wiki/concepts/vigenere-cipher]]
- [[wiki/concepts/enigma-machine]]
- [[wiki/concepts/aes]]
- [[wiki/concepts/rsa]]
- [[wiki/concepts/key-distribution-problem]]
- [[wiki/concepts/ind-cpa-security]]
- [[wiki/concepts/shor-algorithm]]
- [[wiki/concepts/grover-algorithm]]
- [[wiki/concepts/post-quantum-cryptography]]
- [[wiki/concepts/criptografia]]
- [[wiki/concepts/hashing]]
- [[wiki/concepts/password-hashing]]
- [[wiki/concepts/bcrypt]]
- [[wiki/concepts/argon2]]
- [[wiki/concepts/salt]]
- [[wiki/concepts/pepper]]
- [[wiki/concepts/rainbow-table]]

## Open Questions

- A fonte não detalha o método de Kasiski/Friedman que efetivamente quebrou a cifra de Vigenère — vale um concept separado se alguma fonte futura cobrir isso.
- A fonte simplifica a quebra da Enigma como "reuso de chave", sem mencionar a criptoanálise de Turing/Bletchley Park (bombe, cribs) — se uma fonte futura tratar disso em profundidade, revisar [[wiki/concepts/enigma-machine]].
- Nenhuma menção a algoritmos NIST PQC específicos (ML-KEM/Kyber, ML-DSA/Dilithium) — a fonte evita entrar em pós-quântica "porque não ia conseguir entender"; `references/post-quantum-crypto.md` da skill cobre isso em detalhe.

## Contradições / Tensões com o Wiki

Nenhuma contradição encontrada. Esta fonte é complementar a [[wiki/sources/criptografia-fundamentos]] e [[wiki/sources/encoding-hashing-encryption]] (mesmo terreno de hash vs. encryption, simétrica vs. assimétrica) e a [[wiki/sources/seguranca-armazenamento-senhas-banco-de-dados]] (BCrypt/Argon2/salt/pepper), mas contribui genuinamente conteúdo novo: a linha do tempo histórica completa (César → Cítala → Vigenère → Enigma), o mecanismo RSA passo a passo (P, Q, N, totiente de Euler, e, d), o modelo formal IND-CPA com demonstração de por que César falha nele, e a distinção Shor (quebra fatoração) vs. Grover (acelera busca) que não estava presente na wiki antes desta ingestão.
