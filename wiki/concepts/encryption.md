---
type: concept
title: "Encryption (Criptografia)"
aliases: ["encryption", "criptografia", "cifra", "encriptação"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [encryption, criptografia, segurança, chave, aes, rsa, e2e, confidencialidade]
skill: tech-mentor-security
status: stable
---

## Definição

Encryption (criptografia) é a transformação de dados em uma forma ilegível (ciphertext) que só pode ser revertida com a **chave correta**. Diferente do hashing, é reversível — mas apenas por quem possui a chave.

**Propósito:** confidencialidade. Não é sobre representação (encoding) nem sobre integridade (hashing) — é sobre garantir que apenas partes autorizadas acessem os dados.

## Cifra de César — o exemplo histórico

Júlio César deslocava cada letra da mensagem por 3 posições no alfabeto:

```
H E L L O  →  K H O O R
```

A chave era o número do deslocamento (3). Quem soubesse a chave revertia o deslocamento. Hoje é trivialmente quebrável, mas ilustra o princípio: **a mensagem só é legível para quem tem a chave**.

## Tipos de encryption

### Simétrica
Mesma chave para cifrar e decifrar. Rápida.
- **AES-256-GCM** — padrão atual para dados em repouso e em trânsito.
- Problema: como compartilhar a chave com segurança?

### Assimétrica (chave pública/privada)
Chave pública cifra; chave privada decifra. Resolve o problema de distribuição de chaves.
- **RSA, Ed25519, ECDSA** — usados em TLS, SSH, assinaturas digitais.
- Mais lenta que simétrica — geralmente usada para trocar chaves simétricas (ex: TLS handshake).

### End-to-End (E2E)
Os dados são criptografados no dispositivo do remetente e só decriptados no dispositivo do destinatário. Nem o servidor intermediário tem acesso.
- **WhatsApp, Signal** — usam E2E. Os próprios servidores veem apenas ciphertext.

## Propriedades

- **Reversível** — com a chave correta.
- **Confidencialidade** — sem a chave, o conteúdo é ilegível.
- **Não garante integridade sozinha** — para isso, combine com HMAC ou use modos autenticados como AES-GCM.

## Relação com outros conceitos

- [[concepts/encoding]] — reversível sem chave. Encryption requer chave.
- [[concepts/hashing]] — irreversível. Encryption é reversível com chave.
- [[concepts/caesar-cipher]] — exemplo histórico do princípio de encryption.

## Key Sources

- [[sources/encoding-hashing-encryption]]
- [[sources/criptografia-fundamentos]]
