---
type: concept
title: "Ataque Online vs. Offline a Senha"
aliases: ["online attack", "offline attack", "modelo de ameaça de senha"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [segurança, autenticação, password-hashing, rate-limiting, mfa, modelo-de-ameaca]
skill: tech-mentor-security
status: stub
---

# Ataque Online vs. Offline a Senha

Distinção de modelo de ameaça que organiza que defesa resolve qual problema no armazenamento de senhas: **hash/salt/pepper e MFA/rate limit não são intercambiáveis — cada um neutraliza um tipo de ataque diferente.**

## Ataque Online

Atacante tenta autenticar repetidamente contra o sistema em produção, testando senhas candidatas uma a uma via login. [[wiki/concepts/password-hashing]] **não previne** esse ataque — se o atacante puder tentar indefinidamente, eventualmente acerta, independente de como a senha está armazenada no banco.

**Defesas específicas:**
- [[wiki/concepts/rate-limiting]] por IP, dispositivo ou usuário
- Bloqueio de conta após N tentativas malsucedidas
- [[wiki/concepts/mfa-multifator-autenticacao]] — mesmo com a senha certa, falta o segundo fator

## Ataque Offline

Atacante obtém acesso direto ao banco de dados (vazamento, dump) e tenta reverter os hashes de senha localmente, sem precisar interagir com o sistema em produção — sem rate limit possível, porque a tentativa não passa pela aplicação.

**Defesas específicas:**
- [[wiki/concepts/hashing]] (nunca plaintext)
- [[wiki/concepts/salt]] — invalida ataques de senha pré-computada ([[wiki/concepts/ataque-pre-computacao]])
- [[wiki/concepts/pepper]] — segredo que não vaza junto com o banco
- [[wiki/concepts/argon2]] — torna o brute force local computacionalmente inviável

## Por Que a Distinção Importa

Um erro comum é achar que implementar Argon2 + salt + pepper "resolve segurança de senha" — na prática isso só cobre o cenário de vazamento de banco. Sem rate limit e MFA, o sistema continua vulnerável a alguém simplesmente testando senhas comuns pelo formulário de login público. As duas famílias de defesa são complementares, não substitutas.

## Relação com Outros Conceitos

- [[wiki/concepts/password-hashing]] — defesa do lado offline
- [[wiki/concepts/rate-limiting]] — defesa do lado online
- [[wiki/concepts/mfa-multifator-autenticacao]] — defesa do lado online, também mitiga parte do offline (senha vazada sozinha não basta)

## Key Sources

- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]]
