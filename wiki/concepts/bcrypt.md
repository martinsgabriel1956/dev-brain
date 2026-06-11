---
type: concept
title: "BCrypt"
aliases: ["bcrypt", "blowfish crypt"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, password-hashing, bcrypt, cpu-hard]
skill: tech-mentor-security
status: stable
---

# BCrypt

Algoritmo de [[concepts/password-hashing]] baseado no cifrador Blowfish, introduzido em 1999. Foi o padrão da indústria por mais de uma década por ser [[concepts/cpu-hard]] — intencionalmente lento. Ainda aceitável em sistemas legados com fator de trabalho alto, mas **superado pelo [[concepts/argon2]]** para novos projetos.

---

## Estrutura do Hash

```
$2a$12$<22 chars salt><31 chars hash>
```

| Campo | Descrição |
|---|---|
| `2a` | Versão do algoritmo |
| `12` | Fator de trabalho (work factor) |
| Próximos 22 chars | [[concepts/salt]] gerado automaticamente |
| Últimos 31 chars | Hash resultante |

---

## Fator de Trabalho (Work Factor)

Escala logarítmica: `2^N` iterações internas.

| Fator | Iterações | Tempo aproximado (CPU moderna) |
|---|---|---|
| 10 | 1.024 | ~80 ms |
| 12 | 4.096 | ~320 ms (~3 hashes/s) |
| 14 | 16.384 | ~1.3 s |

Cada incremento de 1 **dobra o tempo**. Recomendação mínima atual: fator 12.

---

## O Limite do BCrypt: Paralelismo de GPU

BCrypt ocupa apenas **4 KB de RAM** por instância, portanto cabe em qualquer GPU com paralelismo massivo.

**RTX 5090 (21.760 núcleos CUDA):**
```
3 hashes/s × 21.760 = 65.280 hashes/s
= ~5 bilhões de tentativas/dia
= ~2 trilhões/ano
```

Uma rig com múltiplas GPUs varre um banco de tamanho médio em dias. Por isso o BCrypt não é mais considerado suficiente — [[concepts/argon2]] resolve via [[concepts/memory-hard]].

---

## Ainda Usando BCrypt?

Se o sistema é legado e não suporta Argon2:
- Use fator de trabalho ≥ 12 (idealmente 13-14)
- Adicione [[concepts/pepper]] no ENV
- Considere migração progressiva: re-hash no próximo login do usuário

---

## Relação com Outros Conceitos

- [[concepts/password-hashing]] — contexto geral
- [[concepts/cpu-hard]] — conceito central do BCrypt
- [[concepts/salt]] — gerado automaticamente pelo BCrypt
- [[concepts/argon2]] — sucessor, adiciona memory-hard
- [[concepts/memory-hard]] — propriedade que BCrypt não tem

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
