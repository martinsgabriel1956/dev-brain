---
type: concept
title: "Hashing"
aliases: ["hashing", "hash", "função hash", "hash criptográfico"]
date_created: 2026-04-29
date_updated: 2026-07-28
source_count: 3
tags: [hashing, segurança, senhas, integridade, criptografia, sha256, bcrypt, argon2]
skill: tech-mentor-security
status: stable
---

## Definição

Hashing é o processo de converter dados em uma representação de comprimento fixo (o hash) por meio de um algoritmo matemático. A transformação é **irreversível** — dado o hash, não é possível reconstruir o dado original.

## Três propriedades obrigatórias

1. **Unidirecional:** Não é possível reverter um hash para obter a entrada original.
2. **Determinístico:** A mesma entrada sempre produz o mesmo hash.
3. **Comprimento fixo:** Independente do tamanho do input, o hash tem sempre o mesmo tamanho de output.

## Como funciona no armazenamento de senhas

1. Usuário cria conta → senha é hasheada → **apenas o hash é armazenado**.
2. Usuário faz login → senha digitada é hasheada → hash comparado com o hash armazenado.
3. Se iguais → login bem-sucedido. O sistema **nunca conhece a senha original**.

## Usos principais

| Uso | Como funciona |
|---|---|
| **Senhas** | Hash armazenado; login compara hashes |
| **Integridade de arquivos** | Hash do arquivo original publicado; hash do download comparado |
| **Estruturas de dados** | Hash tables, consistent hashing em sistemas distribuídos |
| **Blockchain** | Cada bloco contém hash do bloco anterior |

## Algoritmos

| Algoritmo | Uso | Observação |
|---|---|---|
| MD5 | Legado | **Não usar para segurança** — colisões conhecidas |
| SHA-256 | Integridade de arquivos, certificados | Seguro para integridade, não para senhas |
| bcrypt | Senhas | Inclui salt + custo computacional intencional |
| Argon2 | Senhas | Vencedor do Password Hashing Competition — preferido |

**Importante:** SHA-256 e bcrypt não são intercambiáveis. Para senhas, use bcrypt ou argon2 — eles incluem salt (proteção contra rainbow tables) e custo computacional ajustável (proteção contra força bruta).

## Por Que Velocidade é um Problema em Password Hashing

MD5 e SHA geram **bilhões de hashes/segundo** — ótimo para integridade de arquivos, catastrófico para senhas. Um atacante com a wordlist [[entities/rockyou]] (29 bilhões de senhas reais) testa tudo em segundos.

Algoritmos especializados ([[concepts/bcrypt]], [[concepts/argon2]]) são **intencionalmente lentos** ([[concepts/cpu-hard]]). O [[concepts/argon2]] adiciona [[concepts/memory-hard]]: ocupa RAM configurável por instância, limitando o paralelismo de GPUs. Com [[concepts/salt]] por usuário, [[concepts/rainbow-table]]s pré-computadas se tornam inviáveis.

Ver [[concepts/password-hashing]] para a visão completa do problema.

## Relação com outros conceitos

- [[concepts/encoding]] — reversível, sem chave. Hashing é irreversível.
- [[concepts/encryption]] — reversível com chave. Hashing é irreversível.
- [[concepts/password-hashing]] — aplicação especializada de hashing para senhas
- [[concepts/salt]] — unicidade por usuário em password hashing
- [[concepts/rainbow-table]] — ataque baseado em hashes pré-computados

## Key Sources

- [[sources/encoding-hashing-encryption]]
- [[sources/autenticacao-segura]]
- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
