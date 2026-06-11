---
type: entity
title: "RockYou"
aliases: ["rockyou", "rockyou.txt", "RockYou wordlist"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, vazamento, wordlist, história]
skill: tech-mentor-security
status: stable
---

# RockYou

Empresa de desenvolvimento de widgets para MySpace, ligada ao Facebook, que em **2009** sofreu um dos primeiros grandes vazamentos de banco de dados da história: **32 milhões de senhas de usuários expostas em plaintext**.

O incidente tornou-se um marco histórico na segurança de senhas e gerou um dos artefatos mais usados em segurança ofensiva: a wordlist `rockyou.txt`.

---

## O Vazamento (2009)

- **Causa:** ataque hacker (SQL Injection)
- **Exposição:** 32 milhões de senhas em plaintext — sem nenhum hashing
- **Impacto:** evidenciou que empresas ainda armazenavam senhas sem proteção décadas após as primeiras recomendações de segurança

---

## A Wordlist RockYou

O arquivo `rockyou.txt` tornou-se a base das wordlists usadas em ataques de senha. A comunidade de hackers foi atualizando com novos vazamentos ao longo dos anos:

| Versão | Ano | Tamanho aprox. |
|---|---|---|
| Original | 2009 | 32 milhões de senhas |
| All-In-One (2026) | 2026 | ~29,6 bilhões de senhas, 317 GB |

Disponível em [SecLists](https://github.com/danielmiessler/SecLists) e similares. Usada como base para [[concepts/rainbow-table]]s e ataques de [[concepts/ataque-pre-computacao]].

---

## Legado

O vazamento do RockYou demonstrou empiricamente que:
1. Armazenar senhas em plaintext ainda era comum em 2009
2. Usuários reutilizam senhas em múltiplos serviços — um vazamento compromete outros
3. Wordlists com senhas reais são muito mais eficazes que listas geradas artificialmente

---

## Relação com Outros Conceitos

- [[concepts/ataque-pre-computacao]] — o vazamento alimentou as tabelas pré-computadas
- [[concepts/rainbow-table]] — rockyou.txt é a base mais comum
- [[concepts/salt]] — técnica que invalida o reaproveitamento dessas listas
- [[concepts/password-hashing]] — o problema que o RockYou evidenciou em escala

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
