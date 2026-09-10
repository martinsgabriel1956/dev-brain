---
type: concept
title: "Ataque Online vs. Offline a Senha"
aliases: ["online attack", "offline attack", "modelo de ameaça de senha"]
date_created: 2026-08-26
date_updated: 2026-09-08
source_count: 2
tags: [segurança, autenticação, password-hashing, rate-limiting, mfa, modelo-de-ameaca, user-enumeration, brute-force]
skill: tech-mentor-security
status: draft
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

## Demonstração Prática do Ataque Online: Três Ferramentas, Mesma Falha

[[wiki/sources/brute-force-painel-admin-vibe-coding-pizzaria-burp-ffuf-hydra]] fornece a demonstração ferramental que faltava a esta página: um painel admin (encontrado por fuzzing de diretórios com dirsearch, ver [[wiki/concepts/attack-surface]]) sem rate limit, sem account lockout, sem CAPTCHA e sem MFA tem a senha do usuário `admin` quebrada por brute force com **Burp Intruder**, **ffuf** e **Hydra** — as três convergindo na mesma senha, usando o mesmo sinal de sucesso (ausência da frase de erro "senha incorreta" na resposta, ou um status code 302 em vez de 200 no caso do Burp).

**Pré-condição habilitadora: user enumeration.** Antes do brute force de senha, a fonte identifica que a aplicação responde com mensagens diferentes para "usuário não encontrado" (`teste` + qualquer senha) e "senha incorreta" (`admin` + qualquer senha) — confirmando `admin` como conta válida sem precisar adivinhar. Isso reduz o ataque de "descobrir usuário E senha" para "descobrir só a senha de um usuário já confirmado", tornando o brute force objetivamente mais rápido.

## Por Que a Distinção Importa

Um erro comum é achar que implementar Argon2 + salt + pepper "resolve segurança de senha" — na prática isso só cobre o cenário de vazamento de banco. Sem rate limit e MFA, o sistema continua vulnerável a alguém simplesmente testando senhas comuns pelo formulário de login público. As duas famílias de defesa são complementares, não substitutas.

## Relação com Outros Conceitos

- [[wiki/concepts/password-hashing]] — defesa do lado offline
- [[wiki/concepts/rate-limiting]] — defesa do lado online
- [[wiki/concepts/mfa-multifator-autenticacao]] — defesa do lado online, também mitiga parte do offline (senha vazada sozinha não basta)

## Key Sources

- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]]
- [[wiki/sources/brute-force-painel-admin-vibe-coding-pizzaria-burp-ffuf-hydra]] — demonstração prática do ataque online com três ferramentas (Burp Intruder, ffuf, Hydra) e user enumeration como pré-condição habilitadora
