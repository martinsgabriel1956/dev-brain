---
type: concept
title: "Criptografia"
aliases: ["cryptography", "encryption", "hashing", "criptografia assimétrica", "criptografia simétrica"]
date_created: 2026-06-26
date_updated: 2026-07-28
source_count: 4
tags: [cs-fundamentals, criptografia, seguranca, hashing, tls, https, hmac]
skill: cs-fundamentals
status: draft
---

# Criptografia

**Conjunto de técnicas para proteger dados** — garantindo confidencialidade, integridade e autenticidade. Toda vez que você faz login, manda uma mensagem ou paga um boleto online, a criptografia está operando.

## Três formas fundamentais

### 1. Hashing (impressão digital)

Transforma dados em uma **string de tamanho fixo**. É **irreversível** — não dá para recuperar o original a partir do hash.

```
"senha123" → SHA-256 → "ef92b778bafe771207..."  (sempre o mesmo output)
"senha124" → SHA-256 → "9a4bfca5e31c61e..."     (completamente diferente)
```

**Por que irreversível importa:** sites nunca devem armazenar sua senha — só o hash. Se o banco vazar, o atacante tem hashes, não senhas.

Ver [[password-hashing]] para detalhes sobre bcrypt/Argon2.

### 2. Criptografia Simétrica

**Mesma chave** para encriptar e decriptar. Rápida, eficiente para grandes volumes de dados.

```
AES-256: dado + chave_secreta → cifrado
cifrado + chave_secreta → dado original
```

**Problema:** como compartilhar a chave de forma segura? Se alguém intercepta a chave, quebra tudo. Ver [[wiki/concepts/key-distribution-problem]] — foi exatamente esse problema que motivou a criação da criptografia assimétrica. O exemplo canônico de simétrica em produção é o [[wiki/concepts/aes]].

### 3. Criptografia Assimétrica

Resolve o problema de distribuição de chave com **um par de chaves**:

- **Chave pública** → encripta → qualquer um pode ter
- **Chave privada** → decripta → só o dono tem

```
Remetente: dado + chave_pública_do_destinatário → cifrado
Destinatário: cifrado + chave_privada → dado original
```

A chave pública pode ser distribuída livremente — só a privada precisa ser protegida. O [[wiki/concepts/rsa]] é o exemplo mais citado: baseado na dificuldade de fatorar números primos grandes.

## Como o HTTPS funciona

HTTPS usa as duas formas em conjunto:

1. **Handshake assimétrico** (TLS): browser usa a chave pública do servidor para estabelecer um canal seguro e negociar uma chave de sessão.
2. **Transferência simétrica**: dados da sessão trafegam com AES (mais rápido para volumes grandes).

```
Browser → [chave pública servidor] → negocia chave de sessão AES → dados trafegam cifrados com AES
```

## Assinatura digital

Inversão da assimétrica para **autenticidade**:

- Assina com **chave privada** (só o dono pode assinar)
- Verifica com **chave pública** (qualquer um pode verificar)

Garante que a mensagem veio de quem diz ser.

[[wiki/concepts/ssh]] usa esse mesmo princípio de prova-de-posse: o cliente demonstra ter a chave privada correspondente à chave pública registrada no `authorized_keys` do servidor, sem transmitir a chave privada — mais próximo de assinatura digital do que de "encriptar/decriptar dados".

## HMAC: um meio-termo entre hash e assinatura assimétrica

Nem toda garantia de integridade exige criptografar o dado (perde-se a legibilidade) nem exige chave assimétrica (cara computacionalmente em alto volume). [[wiki/concepts/hmac]] resolve isso derivando duas chaves (interna e externa) a partir do mesmo segredo via padding — em vez de simplesmente concatenar `secret + mensagem` antes de fazer hash, o que é vulnerável a ataque de extensão de mensagem. HMAC garante integridade e autenticidade com o custo baixo de uma função de hash, ao preço de não ter não-repúdio (qualquer lado com o segredo pode gerar ou verificar).

## Medindo Segurança Formalmente: IND-CPA

Não basta um esquema "parecer" embaralhado — [[wiki/concepts/ind-cpa-security]] é um modelo formal onde um atacante escolhe mensagens para cifrar e tenta distinguir qual de duas cifras corresponde a qual mensagem original. Um esquema que preserva padrões (como a [[wiki/concepts/caesar-cipher]], que sempre mapeia a mesma letra para a mesma letra) falha nesse teste — a existência de qualquer vazamento de informação, mesmo sutil, já desqualifica o esquema como seguro.

## Contexto Histórico: de César a Vigenère e Enigma

Antes da criptografia matemática moderna, a criptografia era pura criatividade: a [[wiki/concepts/scytale]] espartana (transposição via bastão), a [[wiki/concepts/caesar-cipher]] (substituição fixa, quebrável por análise de frequência), a [[wiki/concepts/vigenere-cipher]] (substituição polialfabética, "indecifrável" por 300 anos), e a [[wiki/concepts/enigma-machine]] (mecanizada, quebrada por erro operacional de reuso de chave). O objetivo sempre foi o mesmo: um canal seguro dentro de um canal inerentemente inseguro — confidencialidade, integridade e autenticidade.

## Ameaça Quântica: Shor, Grover e Criptografia Pós-Quântica

Computadores quânticos ameaçam parte da criptografia atual de formas distintas: o [[wiki/concepts/shor-algorithm]] resolve fatoração de inteiros em tempo polinomial, quebrando diretamente o [[wiki/concepts/rsa]]; o [[wiki/concepts/grover-algorithm]] apenas acelera busca por força bruta quadraticamente, o que o [[wiki/concepts/aes]] absorve aumentando o tamanho de chave. O risco já é presente hoje via ataque "colha agora, decifre depois" (harvest-now-decrypt-later) — ver [[wiki/concepts/post-quantum-cryptography]].

## Relação com outros conceitos

- [[protocolo-de-rede]] — TLS é a camada que o HTTPS adiciona sobre HTTP/TCP
- [[abstracao]] — HTTPS abstrai toda essa complexidade; o browser exibe um cadeado
- [[password-hashing]] — aplicação específica de hashing para senhas com salt e custo computacional
- [[acid]] — bancos de dados financeiros dependem de canais seguros para operações de transferência
- [[wiki/concepts/ssh]] — autenticação por par de chaves (Ed25519) como aplicação prática de criptografia assimétrica
- [[wiki/concepts/hmac]] — integridade/autenticidade via chave simétrica derivada, sem o custo de assinatura assimétrica
- [[wiki/concepts/local-first]] — caso de uso que motiva HMAC: validar dado do cliente sem persistir no servidor

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/ssh-chaves-como-funcionam]]
- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]
- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
