---
type: concept
title: "Password Hashing"
aliases: ["hashing de senhas", "armazenamento seguro de senhas", "password storage"]
date_created: 2026-06-11
date_updated: 2026-08-26
source_count: 6
tags: [segurança, criptografia, password-hashing, autenticação]
skill: tech-mentor-security
status: stable
---

# Password Hashing

Técnica de transformar uma senha em um valor irreversível antes de armazenar no banco de dados, de forma que mesmo com acesso ao banco o atacante não possa recuperar a senha original diretamente.

Não confundir com [[concepts/hashing]] genérico: funções de hash de propósito geral (MD5, SHA-256) são **rápidas demais** para senhas. Password hashing usa algoritmos especializados e intencionalmente lentos.

---

## O Problema Central

Senhas precisam ser verificadas (login), mas nunca lidas. A solução é armazenar uma transformação irreversível e, no login, aplicar a mesma transformação à senha digitada e comparar os resultados.

**O risco:** se o banco vaza, o atacante tenta reverter os hashes por força bruta — testando candidatas até achar um match. A velocidade com que ele consegue testar candidatas determina o quanto tempo ele tem antes de quebrar as senhas.

---

## Origem Histórica: Unix (1976)

O Unix foi um dos primeiros sistemas a abandonar o armazenamento de senha em texto puro, adotando hash + salt no arquivo de senhas. O salt resolveu o problema de a função de hash ser determinística (mesma senha → mesmo hash sempre): ele não precisa ser secreto, só único por usuário, o que já inviabiliza ataques de [[concepts/rainbow-table]] pré-computados para múltiplos usuários de uma vez.

## Evolução das Técnicas

| Técnica | Problema |
|---|---|
| Plaintext | Qualquer vazamento expõe tudo |
| MD5/SHA sem salt | [[concepts/rainbow-table]] invalida tudo |
| MD5/SHA + [[concepts/salt]] | Velocidade ainda permite força bruta |
| [[concepts/bcrypt]] | [[concepts/cpu-hard]], mas GPU paralela ainda viável |
| [[concepts/argon2]] | [[concepts/cpu-hard]] + [[concepts/memory-hard]] — derrota GPU |
| Argon2 + [[concepts/pepper]] | Defesa em profundidade — ~99.9% seguro |

---

## Por Que Hash Genérico (SHA-256) Não Serve

Uma GPU moderna calcula cerca de **1 bilhão de hashes SHA-256 por segundo** — rápido o suficiente para um atacante testar bilhões de senhas candidatas em segundos após um vazamento. O *work factor* de bcrypt/Argon2 (número de rodadas de processamento configurável) força cada hash a levar centenas de milissegundos, o que transforma um ataque de força bruta de segundos em anos, mesmo com hardware dedicado.

---

## Propriedades que um Algoritmo de Password Hashing Deve Ter

1. **Determinístico** — mesma entrada + mesmo salt → mesmo hash (para verificação funcionar)
2. **Unidirecional** — não reversível
3. **Lento** (CPU-hard) — dificulta força bruta
4. **Memory-hard** (ideal) — derrota paralelismo de GPU
5. **Salt automático** — unicidade por usuário, sem depender do programador

---

## Configuração Recomendada (2026)

```php
// PHP
$hash = password_hash($password . $pepper, PASSWORD_ARGON2ID, [
    'memory_cost' => 65536,  // 64 MB
    'time_cost'   => 3,
    'threads'     => 4,
]);
```

---

## Relação com Outros Conceitos

- [[concepts/hashing]] — propriedades gerais de funções de hash
- [[concepts/salt]] — unicidade por usuário
- [[concepts/pepper]] — segredo do servidor
- [[concepts/bcrypt]] — algoritmo CPU-hard (legado)
- [[concepts/argon2]] — estado da arte
- [[concepts/rainbow-table]] — ataque que motivou o salt
- [[concepts/ataque-pre-computacao]] — classe de ataques que password hashing mitiga
- [[concepts/timing-attack]] — comparação de hashes deve usar tempo constante

## Caso Real Citado: Vazamento no Ministério da Saúde

[[wiki/entities/fabio-akita]] cita o vazamento de dados do Ministério da Saúde (Brasil) como exemplo de amadorismo: senhas de usuário gravadas como *plaintext* no banco. Heurística prática para identificar esse tipo de falha de fora: se um site oferece "receber sua senha esquecida por e-mail" (em vez de um link de reset), ele necessariamente armazena a senha em texto plano ou reversível — sinal de que a aplicação está insegura.

## Ver também

- [[wiki/concepts/mfa-multifator-autenticacao]] — password hashing protege o fator "algo que você sabe", mas não substitui a necessidade de fatores adicionais
- [[wiki/concepts/ataque-online-vs-offline-senha]] — password hashing é a defesa do ataque offline; rate limit/MFA cobrem o ataque online, que hash sozinho não previne
- [[wiki/concepts/identity-provider-terceirizacao-autenticacao]] — escada de terceirização (lib → framework → identity provider → passwordless) para quem não quer implementar isso do zero

## Key Sources

- [[sources/seguranca-armazenamento-senhas-banco-de-dados]]
- [[wiki/sources/akita-oferta-procura-matematica-carreira]]
- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — comparação numérica SHA-256 (1 bilhão hashes/s em GPU) vs. work factor de bcrypt/Argon2
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] — enquadra hash/salt/pepper como defesa do ataque offline especificamente, distinto de rate limit/MFA para o ataque online
