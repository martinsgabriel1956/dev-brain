---
type: concept
title: "Step-Up Authentication"
aliases: ["step-up authentication", "reautenticação para ação sensível", "MFA em ações sensíveis"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [step-up-authentication, mfa, autenticacao, seguranca, autorizacao]
skill: tech-mentor-security
status: stub
---

# Step-Up Authentication

Prática de exigir uma nova verificação do segundo fator ([[wiki/concepts/mfa-multifator-autenticacao|MFA]]) antes de liberar uma ação sensível, mesmo que o usuário já tenha uma sessão autenticada válida.

## O problema que resolve

Aplicar MFA **só no momento do login** protege a entrada, mas não protege o que acontece depois. Se um atacante já conseguiu uma sessão ativa (sessão sequestrada, token roubado, dispositivo destravado), ele pode executar ações críticas sem nunca precisar do segundo fator de novo — trocar o e-mail cadastrado, resetar a senha, desativar o próprio MFA, ou transferir dinheiro.

## Onde aplicar

Operações de alto impacto e baixa frequência são as candidatas naturais:

- Trocar e-mail ou telefone de recuperação
- Mudar ou resetar a senha
- Desativar MFA
- Adicionar um novo método de pagamento ou transferir valores
- Revogar/criar chaves de API com privilégios elevados

## Relação com outros conceitos

- [[wiki/concepts/mfa-multifator-autenticacao]] — step-up authentication é MFA aplicado fora do fluxo de login, em pontos específicos de risco elevado
- [[wiki/concepts/autenticacao-e-autorizacao]] — trata sessão autenticada e permissão para uma ação específica como coisas distintas, mesmo dentro da mesma sessão
- [[wiki/concepts/sessoes-http-cookies]] — pressupõe que uma sessão válida não é, por si só, prova suficiente de intenção para toda e qualquer ação

## Key Sources

- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]]
