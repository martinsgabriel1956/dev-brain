---
type: concept
title: "Pepper"
aliases: ["password pepper", "server-side secret"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [segurança, criptografia, password-hashing, pepper, defesa-em-profundidade]
skill: tech-mentor-security
status: stable
---

# Pepper

Valor secreto único armazenado no **ENV do servidor** (nunca no banco de dados), concatenado à senha antes de gerar o hash. É a última camada de defesa: mesmo que o banco de dados vaze completamente, o atacante não consegue fazer brute-force porque desconhece o pepper.

---

## Como Funciona

```
hash_input = senha_do_usuario + PEPPER_VALUE
hash_final = argon2id(hash_input)
```

Exemplo:
- Senha: `123456`
- Pepper (no ENV): `f3A7cB9xQ2mN5pL8vR1sY4`
- Valor hasheado: `123456f3A7cB9xQ2mN5pL8vR1sY4`

O banco armazena apenas `hash_final`. Mesmo com acesso ao banco + salt + parâmetros do algoritmo, o atacante tentaria reverter `hash("123456f3A7...")` sem saber que existe o sufixo.

---

## Implementação

```bash
# .env
PASSWORD_PEPPER=f3A7cB9xQ2mN5pL8vR1sY4
```

```php
$pepper = $_ENV['PASSWORD_PEPPER'];
$hash = password_hash($password . $pepper, PASSWORD_ARGON2ID, [
    'memory_cost' => 65536,
    'time_cost'   => 3,
    'threads'     => 4,
]);
```

---

## Diferença para Salt

| | [[concepts/salt]] | Pepper |
|---|---|---|
| Unicidade | Por usuário | Global (mesmo valor para todos) |
| Onde fica | No banco (junto ao hash) | No servidor (`.env`) |
| Secreto? | Não | Sim |
| Objetivo | Invalida rainbow tables | Defesa se só o banco vazar |

---

## Quando Pepper NÃO ajuda

Se o atacante comprometeu também o servidor (acesso ao `.env`), o pepper é exposto. Por isso, pepper é defesa em profundidade — assume que servidores e bancos têm vetores de ataque diferentes e complementa [[concepts/argon2]], não o substitui.

---

## Rotação do Pepper

Rotacionar pepper requer re-hash de todas as senhas, o que exige que o usuário faça login (única forma de obter a senha em plaintext novamente). Estratégia: marcar hashes com versão do pepper e re-hashar progressivamente a cada login.

---

## Relação com Outros Conceitos

- [[concepts/password-hashing]] — contexto geral
- [[concepts/salt]] — complemento ao pepper
- [[concepts/argon2]] — algoritmo com o qual pepper combina
- [[concepts/bcrypt]] — também pode ser usado com pepper

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
