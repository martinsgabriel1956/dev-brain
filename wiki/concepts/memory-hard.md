---
type: concept
title: "Memory-Hard"
aliases: ["memory hardness", "custo de memória"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, password-hashing, memory-hard, gpu]
skill: tech-mentor-security
status: stable
---

# Memory-Hard

Propriedade de algoritmos que exigem uma quantidade significativa de **memória RAM** para executar, proporcional a um parâmetro configurável. O objetivo é limitar o paralelismo de GPUs e ASICs, cujo gargalo é a VRAM — não a capacidade de processamento.

É a propriedade que diferencia [[concepts/argon2]] de [[concepts/bcrypt]] e o que torna o Argon2 resistente a ataques por rigs de GPU.

---

## O Gargalo das GPUs

GPUs têm poder de processamento massivo (ex: RTX 5090 → 21.760 núcleos CUDA), mas memória limitada (32 GB de VRAM no topo de linha).

[[concepts/bcrypt]] ocupa 4 KB de RAM por instância → cabe ~8 milhões de instâncias em 32 GB.
[[concepts/argon2]] com `m=65536` (64 MB) → cabe ~500 instâncias em 32 GB.

O atacante pode ter 21.760 núcleos, mas só consegue usar ~500 deles em paralelo. Aumentar `memory_cost` para 256 MB reduz para ~125 instâncias paralelas.

---

## Configuração

No Argon2, o parâmetro `memory_cost` define o consumo em KB:

| `memory_cost` | RAM por instância | Instâncias em 32 GB VRAM |
|---|---|---|
| 65536 | 64 MB | ~500 |
| 262144 | 256 MB | ~125 |
| 1048576 | 1 GB | ~32 |

Aumentar `memory_cost` é a alavanca mais poderosa para tornar ataques por GPU inviáveis.

---

## Relação com Outros Conceitos

- [[concepts/argon2]] — o algoritmo que implementa memory-hard para senhas
- [[concepts/cpu-hard]] — propriedade complementar (BCrypt tem só CPU-hard)
- [[concepts/password-hashing]] — contexto de uso
- [[concepts/bcrypt]] — não é memory-hard, daí sua vulnerabilidade a GPU

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
