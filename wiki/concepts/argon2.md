---
type: concept
title: "Argon2"
aliases: ["argon2id", "argon2i", "argon2d"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, password-hashing, argon2, memory-hard]
skill: tech-mentor-security
status: stable
---

# Argon2

Algoritmo de [[concepts/password-hashing]] vencedor do **Password Hashing Competition (2015)**. Considerado o estado da arte para armazenamento de senhas por combinar [[concepts/cpu-hard]] com [[concepts/memory-hard]], tornando ataques por GPU economicamente inviáveis.

---

## Variantes

| Variante | Uso |
|---|---|
| Argon2i | Resistente a side-channel attacks |
| Argon2d | Máxima resistência a GPU/ASIC |
| **Argon2id** | **Híbrido — recomendado para senhas** |

---

## Estrutura do Hash

```
$argon2id$v=19$m=65536,t=3,p=4$<salt>$<hash>
```

| Campo | Descrição |
|---|---|
| `argon2id` | Variante |
| `v=19` | Versão do algoritmo |
| `m=65536` | Custo de memória em KB (= 64 MB) |
| `t=3` | Número de iterações (time cost) |
| `p=4` | Paralelismo (threads) |

---

## Por Que Memory-Hard Derrota GPUs

[[concepts/bcrypt]] ocupa apenas 4 KB de RAM → uma RTX 5090 (21.760 núcleos, 32 GB VRAM) paralela facilmente.

Argon2 com `m=65536` (64 MB):
- 10 instâncias paralelas → 640 MB de RAM
- 100 instâncias → 6.4 GB
- 500 instâncias → 32 GB (esgota toda a VRAM da RTX 5090)

O atacante pode ter milhões de núcleos CUDA, mas não tem RAM suficiente para aproveitar todos.

---

## Configuração Recomendada

```php
// PHP
$options = [
    'memory_cost' => 65536,  // 64 MB — mínimo; 256 MB+ mais seguro
    'time_cost'   => 3,
    'threads'     => 4,
];
$hash = password_hash($password . $pepper, PASSWORD_ARGON2ID, $options);
```

Sempre usar com [[concepts/pepper]] para defesa em profundidade.

---

## Relação com Outros Conceitos

- [[concepts/password-hashing]] — contexto geral
- [[concepts/memory-hard]] — propriedade central do Argon2
- [[concepts/cpu-hard]] — também presente no Argon2
- [[concepts/bcrypt]] — predecessor, superado pelo paralelismo de GPU
- [[concepts/salt]] — Argon2 gera automaticamente
- [[concepts/pepper]] — camada adicional recomendada

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
