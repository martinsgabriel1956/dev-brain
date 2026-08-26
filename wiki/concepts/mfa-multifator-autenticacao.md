---
type: concept
title: "MFA — Autenticação Multifator"
aliases: ["MFA", "2FA", "multi-factor authentication", "two-factor authentication", "fatores de autenticação"]
date_created: 2026-07-27
date_updated: 2026-08-26
source_count: 3
tags: [mfa, 2fa, autenticacao, seguranca, fatores-de-autenticacao]
skill: tech-mentor-security
status: draft
---

# MFA — Autenticação Multifator

Consenso de segurança de que autenticação robusta exige múltiplas provas de identidade, e que essas provas precisam vir de **categorias diferentes** — não adianta pedir duas senhas.

## As três categorias de fator

1. **Algo que você sabe** — senha, PIN, resposta de pergunta de segurança.
2. **Algo que você tem** — cartão físico, celular, token de hardware ([[wiki/entities/rsa-security|SecurID]], [[wiki/concepts/webauthn-fido2-u2f|U2F/YubiKey]]).
3. **Algo que você é** — impressão digital, reconhecimento facial (ver [[wiki/concepts/mobile-biometria]]).

## Por que categorias diferentes importam

Para comprometer dois fatores da mesma categoria, um atacante muitas vezes usa o mesmo vetor de ataque (ex.: duas senhas vazam juntas no mesmo phishing). Exigir categorias diferentes força dois vetores de ataque simultâneos e independentes — por exemplo, roubar uma senha (phishing) **e** roubar fisicamente um celular, o que é muito mais difícil de fazer ao mesmo tempo.

## Origem histórica: perguntas de segurança

As perguntas de segurança ("nome do seu primeiro animal de estimação", "cidade onde nasceu") foram a primeira tentativa comercial em massa de ir além da senha simples. Na prática eram apenas uma segunda senha mais fraca (mesma categoria: "algo que você sabe"), e hoje são consideradas obsoletas — respostas frequentemente descobríveis via engenharia social ou redes sociais. O valor histórico delas foi conceitual: abriram a ideia de que autenticação não precisa se limitar a um único segredo.

## Evolução do segundo fator

```
anos 90  → RSA SecurID (token de hardware, seed + relógio proprietário)
2005     → HOTP (IETF, RFC 4226) — contador em vez de relógio
depois   → TOTP (IETF, RFC 6238) — relógio, mas padronizado e público
2014     → U2F (criptografia assimétrica, challenge-response)
```

Ver [[wiki/concepts/otp-hotp-totp]] para os detalhes de HOTP/TOTP e [[wiki/concepts/webauthn-fido2-u2f]] para U2F/FIDO2/WebAuthn.

## Resistência a Phishing por Método

| Método | Vulnerabilidade principal |
|---|---|
| SMS | Clonagem de número via SIM swap |
| TOTP | Código pode ser digitado num site de phishing e repassado em tempo real |
| Chave física (ex.: YubiKey) / WebAuthn | Não vulnerável a phishing — prova vinculada ao domínio, ver [[wiki/concepts/webauthn-fido2-u2f]] |

## MFA Só no Login Não Basta: Step-Up Authentication

Aplicar MFA apenas no momento do login protege a entrada, mas não as ações depois dela. Se um atacante já tem uma sessão ativa (ex.: sessão sequestrada), pode trocar e-mail, resetar senha ou desativar o próprio MFA sem nunca precisar do segundo fator de novo. Operações sensíveis exigem reautenticação do segundo fator no momento da ação — ver [[wiki/concepts/step-up-authentication]].

## MFA como Defesa do Ataque Online (e Rede de Segurança no Offline)

[[wiki/concepts/ataque-online-vs-offline-senha]] enquadra MFA — junto com rate limiting/bloqueio de conta — como a defesa específica do ataque online (tentativa repetida de login), distinto de hash/salt/pepper, que defendem o ataque offline (vazamento de banco). MFA também funciona como rede de segurança adicional no cenário offline: mesmo que o atacante quebre o hash da senha, ainda falta o segundo fator para logar de fato.

## Relação com outros conceitos

- [[wiki/concepts/password-hashing]] — o fator "algo que você sabe" continua vulnerável a vazamento mesmo com hash+salt
- [[wiki/concepts/ataque-online-vs-offline-senha]] — MFA como defesa primária do ataque online
- [[wiki/concepts/otp-hotp-totp]] — implementação do fator "algo que você tem" via código temporário
- [[wiki/concepts/webauthn-fido2-u2f]] — implementação do fator "algo que você tem" via criptografia assimétrica
- [[wiki/concepts/mobile-biometria]] — implementação do fator "algo que você é"
- [[wiki/concepts/sso-single-sign-on]] — MFA costuma ser aplicado uma vez no IdP central, não em cada serviço
- [[wiki/concepts/step-up-authentication]] — MFA reaplicado fora do login, em ações sensíveis

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — comparação de resistência a phishing por método; step-up authentication
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] — MFA (autenticador, código via WhatsApp/e-mail) como defesa do ataque online, distinto de hash/salt/pepper
