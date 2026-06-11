---
type: source
title: "Segurança e Armazenamento de Senhas no Banco de Dados"
aliases: ["password storage security", "armazenamento seguro de senhas"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 0
tags: [segurança, criptografia, password-hashing, bcrypt, argon2, salt, pepper, rainbow-table]
skill: tech-mentor-security
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/seguranca-armazenamento-senhas-banco-de-dados.md
source_url: ""
author: "Renato Augusto"
date_published: 2026-06-11
date_ingested: 2026-06-11
---

# Segurança e Armazenamento de Senhas no Banco de Dados

## TL;DR

Armazenar senhas corretamente exige entender a evolução histórica dos ataques. O caminho vai de plaintext (inseguro) → MD5/SHA (vulnerável a rainbow tables e velocidade) → bcrypt com salt (insuficiente contra rigs de GPU) → **Argon2id + pepper** (estado da arte). A chave é entender que velocidade é um problema, paralelismo é uma ameaça e memória RAM é o gargalo que derrota GPUs.

---

## Linha do Tempo dos Ataques e Defesas

### Era 1: Plaintext (Anos 90)

Senhas armazenadas exatamente como o usuário digitou. Qualquer vazamento de banco expunha tudo imediatamente. O SQL Injection popularizado nos anos 90 tornou esse padrão catastrófico: um atacante com acesso ao banco ganhava também acesso a qualquer outro serviço onde o usuário reutilizasse a senha.

**Caso real:** [[entities/rockyou]] — 2009, 32 milhões de senhas vazadas em plaintext. Originou a wordlist RockYou, hoje com bilhões de senhas reais, usada como base para todos os ataques subsequentes.

### Era 2: MD5 e SHA-1 (Anos 2000)

Funções de hash [[concepts/hashing]] foram adotadas como solução: determinísticas, com efeito avalanche, unidirecionais. O banco armazenava o hash, não a senha.

**Problema 1 — Velocidade:** MD5/SHA geram bilhões de hashes/segundo. Um atacante consegue testar bilhões de candidatas em segundos.

**Problema 2 — Senhas iguais = hashes iguais:** Sem unicidade por usuário, quebrar uma senha quebra todas que usam o mesmo valor.

**Problema 3 — [[concepts/ataque-pre-computacao]]:** Com listas como RockYou, o atacante pré-computa todos os hashes uma vez e reutiliza contra qualquer banco vazado.

### Era 2.5: MD5/SHA + Salt

[[concepts/salt]] resolve o ataque de pré-computação ao forçar recálculo por usuário. Mas não resolve a velocidade — com bilhões de hashes/segundo, fazer um loop em 29 bilhões de candidatas por linha do banco ainda é viável.

### Era 3: BCrypt / PBKDF2 (Anos 2010)

[[concepts/bcrypt]] introduz o conceito de [[concepts/cpu-hard]]: o algoritmo é **intencionalmente lento**. Com fator de trabalho 12, gera ~3 hashes/segundo. O salt já é gerado automaticamente.

**Problema:** GPUs modernas têm dezenas de milhares de núcleos e bcrypt ocupa apenas 4 KB de RAM por instância. Uma RTX 5090 (21.760 núcleos CUDA) consegue testar ~5 bilhões de candidatas/dia. Uma rig com múltiplas GPUs varre um banco em dias.

### Era 4: Argon2id (Estado da Arte)

[[concepts/argon2]] introduz [[concepts/memory-hard]]: além de CPU-hard, ocupa quantidade configurável de RAM por instância (ex: 64 MB). Isso limita o paralelismo de GPUs pelo gargalo de VRAM (32 GB numa RTX 5090 = máximo ~500 instâncias paralelas de 64 MB).

Configuração recomendada: `m=65536` (64 MB), `t=3` iterações, `p=4` threads, variante `argon2id`.

### Técnica Adicional: Pepper

[[concepts/pepper]] é um valor secreto armazenado no ENV do servidor (não no banco). Concatenado à senha antes do hash, inutiliza qualquer tentativa de brute-force mesmo que o banco vaze, porque o atacante não sabe que o pepper existe.

---

## Conceitos Centrais

- [[concepts/password-hashing]] — visão geral do problema
- [[concepts/salt]] — unicidade por usuário, invalida rainbow tables
- [[concepts/rainbow-table]] — ataque de pré-computação que salt resolve
- [[concepts/cpu-hard]] — algoritmos lentos por design
- [[concepts/memory-hard]] — o que derrota GPUs
- [[concepts/bcrypt]] — CPU-hard, obsoleto contra rigs de GPU
- [[concepts/argon2]] — estado da arte, memory-hard
- [[concepts/pepper]] — segredo do servidor, defesa em profundidade
- [[concepts/ataque-pre-computacao]] — como funcionam os ataques históricos

---

## Entidades

- [[entities/rockyou]] — empresa e wordlist originada no vazamento de 2009

---

## Relação com Outros Conceitos do Wiki

- [[concepts/hashing]] — propriedades das funções de hash (determinístico, efeito avalanche, unidirecional)
- [[concepts/sql-injection]] — vetor original que tornou o plaintext perigoso nos anos 90
- [[concepts/timing-attack]] — comparação segura de hashes exige tempo constante

---

## Questões Abertas

1. Qual o `memory_cost` mínimo recomendado para 2026 dado o avanço das GPUs?
2. Como gerenciar rotação do pepper sem invalidar todas as senhas existentes?
3. PBKDF2 ainda é aceitável em sistemas legados ou deve-se migrar para Argon2id?
