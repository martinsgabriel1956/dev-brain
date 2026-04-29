---
type: source
title: "Encoding vs Hashing vs Encryption — Qual a Diferença?"
aliases: ["encoding hashing encryption", "encoding vs hashing", "criptografia fundamentos basicos"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 0
tags: [encoding, hashing, encryption, criptografia, segurança, base64, caesar-cipher, fundamentos]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/encoding-hashing-encryption.md
source_url: ""
author: "ByteByteGo"
date_published: ""
date_ingested: 2026-04-29
---

## TL;DR

Três conceitos frequentemente confundidos com propósitos radicalmente diferentes. Encoding é reversível por qualquer um e serve para representação de dados. Hashing é irreversível e serve para verificação de integridade e senhas. Encryption é reversível apenas com a chave correta e serve para confidencialidade.

---

## Key Claims

**Claim:** Encoding não é segurança — é representação.
**Evidence:** `%20` em URLs pode ser decodificado de volta para espaço por qualquer pessoa. UTF-8, base64, hex são todos reversíveis sem nenhum segredo.
**Source:** ByteByteGo.
**Confidence:** Alta — definição padrão da indústria.

**Claim:** Hashing é irreversível por design.
**Evidence:** Senhas são armazenadas como hash. No login, a senha digitada é hasheada e comparada — nunca revertida. Mesmo o sistema não sabe a senha original.
**Source:** ByteByteGo.
**Confidence:** Alta.

**Claim:** Hashing tem três propriedades obrigatórias: unidirecional, determinístico, comprimento fixo.
**Evidence:** Mesma entrada sempre produz mesmo hash. Hash de qualquer tamanho de input tem o mesmo comprimento de output.
**Source:** ByteByteGo.
**Confidence:** Alta — propriedades formais de funções hash criptográficas.

**Claim:** Encryption é reversível — mas só com a chave correta.
**Evidence:** WhatsApp criptografa no dispositivo antes de enviar. Sem a chave de decriptação, mesmo os servidores do WhatsApp veem apenas ruído.
**Source:** ByteByteGo, exemplo WhatsApp E2E.
**Confidence:** Alta.

---

## Resumo comparativo

| | Encoding | Hashing | Encryption |
|---|---|---|---|
| **Propósito** | Representação / transmissão | Verificação de integridade | Confidencialidade |
| **Reversível?** | Sim, por qualquer um | Não | Sim, só com a chave |
| **Exemplos** | UTF-8, binário, hex, base64 | MD5, SHA-256, bcrypt | AES, RSA, E2E (WhatsApp) |
| **Uso típico** | URLs, imagens inline, CSS | Senhas, integridade de arquivos | Mensagens, documentos sensíveis |

---

## Conceitos

- [[concepts/encoding]]
- [[concepts/hashing]]
- [[concepts/encryption]]
- [[concepts/caesar-cipher]]

---

## Open Questions

- Qual a diferença entre hashing de senha (bcrypt/argon2) e hashing de integridade (SHA-256)? O source trata como o mesmo conceito — mas têm propriedades diferentes (salt, custo computacional intencional).
- O source não menciona encoding vs encryption como erro comum (ex: base64 não é criptografia). Vale um concept separado sobre esse antipadrão?

---

## Contradições / Tensões com o Wiki

- [[sources/criptografia-fundamentos]] provavelmente cobre o mesmo terreno com mais profundidade — verificar sobreposição.
- [[sources/autenticacao-segura]] cobre bcrypt/argon2 para senhas — complementa a seção de hashing deste source.
