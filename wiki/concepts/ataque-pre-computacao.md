---
type: concept
title: "Ataque de Pré-computação"
aliases: ["precomputation attack", "ataque de tabela pré-computada"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, ataque, password-hashing, rainbow-table]
skill: tech-mentor-security
status: stable
---

# Ataque de Pré-computação

Classe de ataque onde o trabalho computacional é realizado **antes** do ataque em si, gerando uma tabela que pode ser reutilizada contra múltiplos alvos. No contexto de senhas, consiste em pré-computar hashes de senhas candidatas e armazená-los para comparação imediata quando um banco de dados vaza.

O exemplo mais comum é a [[concepts/rainbow-table]].

---

## Funcionamento

1. Coleta uma wordlist (ex: [[entities/rockyou]] — 29 bilhões de senhas reais vazadas)
2. Gera `hash(senha)` para cada entrada
3. Armazena a tabela `{hash: senha}`
4. Quando um banco vaza, compara os hashes do banco com a tabela → senha encontrada instantaneamente

O custo computacional é pago **uma vez** e o benefício é reutilizado contra qualquer banco que use o mesmo algoritmo sem [[concepts/salt]].

---

## Por Que Salt Invalida o Ataque

Com salt único por usuário, o atacante teria que recomputar a tabela inteira para cada salt diferente. Se há 1 milhão de usuários com salts distintos, o reaproveitamento desaparece — cada usuário exige sua própria pré-computação.

---

## Contramedidas

| Técnica | Efeito |
|---|---|
| [[concepts/salt]] | Invalida reutilização de tabelas pré-computadas |
| [[concepts/cpu-hard]] | Torna a pré-computação lenta demais |
| [[concepts/memory-hard]] | Limita o paralelismo mesmo com hardware potente |

---

## Relação com Outros Conceitos

- [[concepts/rainbow-table]] — implementação mais comum
- [[concepts/salt]] — principal defesa
- [[concepts/hashing]] — o que é hashado
- [[concepts/password-hashing]] — contexto de aplicação
- [[entities/rockyou]] — a wordlist que potencializou esses ataques

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
