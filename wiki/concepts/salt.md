---
type: concept
title: "Salt"
aliases: ["salting", "salt criptográfico", "password salt"]
date_created: 2026-06-11
date_updated: 2026-08-26
source_count: 4
tags: [segurança, criptografia, password-hashing, salt]
skill: tech-mentor-security
status: stable
---

# Salt

String aleatória e única gerada para cada usuário, concatenada à senha antes do hash. Garante que senhas iguais gerem hashes diferentes e invalida [[concepts/rainbow-table]]s pré-computadas.

O salt **não precisa ser secreto** — fica armazenado junto ao hash no banco de dados. Sua força vem da unicidade, não do sigilo.

---

## Por Que Resolve as Rainbow Tables

Sem salt:
```
hash("123456") → e10adc... (sempre igual)
```
Uma rainbow table mapeia `e10adc...` → `"123456"` e serve contra qualquer banco.

Com salt único por usuário:
```
hash("123456" + "dHuY7k3m") → a4f91c...
hash("123456" + "xQ2mN5pL") → 7b3e2a...  ← hash diferente, mesma senha
```
O atacante teria que recomputar toda a tabela para cada salt — inviabilizando o reaproveitamento do trabalho.

---

## Salt vs. Pepper

| | Salt | Pepper |
|---|---|---|
| Unicidade | Por usuário | Único global |
| Onde fica | No banco (público) | No ENV do servidor (secreto) |
| Objetivo | Invalidar rainbow tables | Defesa se apenas o banco vazar |

Ver [[concepts/pepper]] para a combinação ideal.

---

## Salt em Algoritmos Modernos

[[concepts/bcrypt]] e [[concepts/argon2]] geram o salt automaticamente e o embutem no hash resultante. Não é necessário gerenciar salt manualmente — o algoritmo cuida disso.

---

## Relação com Outros Conceitos

- [[concepts/password-hashing]] — contexto de uso
- [[concepts/rainbow-table]] — o ataque que salt invalida
- [[concepts/pepper]] — complemento ao salt, armazenado no servidor
- [[concepts/bcrypt]] — gera salt automaticamente
- [[concepts/argon2]] — gera salt automaticamente

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]]
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] — exemplo didático Bob/Alice com mesma senha, salts diferentes
