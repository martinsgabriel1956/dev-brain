---
type: concept
title: "RSA"
aliases: ["rsa", "rivest shamir adleman", "criptografia assimetrica rsa"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, rsa, criptografia-assimetrica, numeros-primos]
skill: tech-mentor-security
status: stable
---

## Definição

Algoritmo de **criptografia assimétrica** (chave pública) baseado na dificuldade computacional de fatorar números grandes em seus fatores primos. É essa dificuldade — não um segredo compartilhado — que garante a segurança do RSA.

## Como funciona

1. Escolhem-se dois números primos grandes, **P** e **Q**.
2. Calcula-se **N = P × Q**.
3. Calcula-se o **totiente de Euler** de N — quantos números menores que N são coprimos com N.
4. Escolhe-se um expoente público **e**, coprimo com o totiente.
5. Calcula-se o expoente privado **d**, a partir de e e do totiente.

A **chave pública** é o par (e, N) — pode ser distribuída livremente. A **chave privada** é (d, N) — só o dono deve ter. Para criptografar, a mensagem (convertida para forma numérica) é elevada a e mod N; para descriptografar, o ciphertext é elevado a d mod N.

## Resolve o Key Distribution Problem

RSA nasceu para resolver o [[wiki/concepts/key-distribution-problem]] da criptografia simétrica ([[wiki/concepts/aes]]): em vez de uma única chave secreta compartilhada, há um par — pública (todo mundo tem) e privada (só o dono tem). Na prática (TLS, HTTPS), RSA/assimétrica é usado para negociar uma chave de sessão simétrica, não para cifrar o volume de dados em si (lento demais).

## Ameaça Quântica: Algoritmo de Shor

O [[wiki/concepts/shor-algorithm]] resolve o problema da fatoração de inteiros em tempo polinomial — uma ameaça direta e completa ao RSA. Um computador quântico suficientemente grande pode quebrar RSA em minutos, independentemente do tamanho da chave. Essa é a motivação central da [[wiki/concepts/post-quantum-cryptography]] e do risco de "colha agora, decifre depois".

## Relação com outros conceitos

- [[wiki/concepts/aes]] — par simétrico cujo problema de distribuição de chave o RSA resolve
- [[wiki/concepts/key-distribution-problem]] — problema que motivou a criação da criptografia assimétrica
- [[wiki/concepts/shor-algorithm]] — algoritmo quântico que quebra a segurança do RSA
- [[wiki/concepts/post-quantum-cryptography]] — sucessores planejados para substituir RSA
- [[wiki/entities/rsa-security]] — empresa homônima (SecurID), não confundir: entidade comercial vs. este algoritmo

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
