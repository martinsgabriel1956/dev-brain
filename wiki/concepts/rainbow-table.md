---
type: concept
title: "Rainbow Table"
aliases: ["tabela arco-íris", "lookup table de hashes"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, ataque, rainbow-table, password-hashing]
skill: tech-mentor-security
status: stable
---

# Rainbow Table

Tabela pré-computada que mapeia hashes de volta às senhas originais. É uma forma de [[concepts/ataque-pre-computacao]]: o trabalho computacional é feito **uma vez** e reutilizado contra qualquer banco que use o mesmo algoritmo de hash sem [[concepts/salt]].

Não é "descriptografia" — a função de hash continua unidirecional. A rainbow table simplesmente encontra uma entrada que produza aquele hash por busca em tabela.

---

## Como Funciona

1. Atacante pega uma wordlist (ex: [[entities/rockyou]] — 29 bilhões de senhas reais)
2. Gera o hash de cada senha: `hash("123456") → e10adc...`
3. Armazena a tabela `hash → senha`
4. Quando um banco vaza, busca cada hash do banco na tabela → senha encontrada em milissegundos

O trabalho de computar os hashes foi feito uma vez; o reaproveitamento é ilimitado.

---

## Por Que Salt Derrota Rainbow Tables

Com [[concepts/salt]] único por usuário:
```
hash("123456" + salt_maria) → resultado único para Maria
hash("123456" + salt_julia) → resultado diferente para Julia
```

Para atacar, o adversário teria que recomputar toda a tabela para cada salt diferente — inviabilizando o reaproveitamento.

---

## Sites de "Decrypt"

Sites como "MD5 Decrypt" não revertem hashes criptograficamente. Eles consultam rainbow tables enormes. Se a senha não está na tabela, o site não retorna nada.

---

## Relação com Outros Conceitos

- [[concepts/ataque-pre-computacao]] — categoria de ataque à qual pertence
- [[concepts/salt]] — técnica que invalida rainbow tables
- [[concepts/hashing]] — propriedades das funções de hash
- [[concepts/password-hashing]] — contexto de defesa
- [[entities/rockyou]] — wordlist base para rainbow tables modernas

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
