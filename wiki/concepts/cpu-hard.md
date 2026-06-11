---
type: concept
title: "CPU-Hard"
aliases: ["computacionalmente custoso", "work factor", "fator de trabalho"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, password-hashing, cpu-hard]
skill: tech-mentor-security
status: stable
---

# CPU-Hard

Propriedade de algoritmos de [[concepts/password-hashing]] que os torna **intencionalmente lentos**, consumindo ciclos de CPU de forma proporcional a um fator configurável. O objetivo é que cada tentativa de brute-force seja cara o suficiente para tornar ataques inviáveis.

Contraposição direta a algoritmos de hash genéricos (MD5, SHA-256) que são otimizados para **velocidade máxima** — exatamente o oposto do que se quer em password hashing.

---

## Por Que Velocidade é um Problema

MD5/SHA geram **bilhões de hashes/segundo**. Um atacante com uma wordlist de 29 bilhões de senhas consegue testar tudo em segundos.

[[concepts/bcrypt]] com fator 12: ~3 hashes/segundo → mesma wordlist levaria **centenas de anos** num único núcleo de CPU.

---

## Fator de Trabalho

O custo é configurável e cresce em escala logarítmica no BCrypt (`2^N` iterações) ou linearmente no [[concepts/argon2]] (`time_cost`).

**Regra:** ajustar periodicamente conforme o hardware avança, para manter o tempo de geração entre 100-500ms por hash em produção.

---

## Limitação: Paralelismo de GPU

CPU-hard protege contra CPU, mas GPUs têm dezenas de milhares de núcleos e podem paralelizar instâncias do algoritmo. [[concepts/bcrypt]] (apenas CPU-hard) pode ser atacado por rigs de GPU.

A solução é [[concepts/memory-hard]] — ver [[concepts/argon2]].

---

## Relação com Outros Conceitos

- [[concepts/password-hashing]] — contexto de uso
- [[concepts/bcrypt]] — implementação clássica de CPU-hard
- [[concepts/argon2]] — combina CPU-hard com memory-hard
- [[concepts/memory-hard]] — extensão que derrota GPU

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
