---
type: concept
title: "Identity Provider e Terceirização de Autenticação"
aliases: ["identity provider", "auth as a service", "Clerk", "Auth0", "Cognito", "Better Auth"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [segurança, autenticação, identity-provider, clerk, auth0, cognito, better-auth, passwordless]
skill: tech-mentor-security
status: stub
---

# Identity Provider e Terceirização de Autenticação

Escada de opções para lidar com armazenamento e verificação de senha, em ordem crescente de terceirização — cada nível delega mais responsabilidade de segurança para fora do código da própria aplicação.

## Os Quatro Níveis

1. **Lib de hashing consagrada** — implementar você mesmo o fluxo de cadastro/login, mas usando [[wiki/concepts/argon2]] (ou equivalente) via biblioteca auditada, nunca hash/salt escritos à mão. Máximo controle, máxima responsabilidade.
2. **Framework de autenticação** — ex.: **Better Auth**. Cuida do armazenamento, hashing e fluxo de sessão por você, mas ainda roda dentro da própria infraestrutura da aplicação. Delega a parte que "desenvolvedores geralmente não são bons em fazer direito" sem sair do próprio banco de dados.
3. **Identity provider completo (terceirização total)** — **Clerk**, **Auth0**, **Cognito** (AWS). Toda a lógica de login, senha, sessão e MFA vive fora da aplicação; o time não lida mais com armazenamento de credencial nenhuma.
4. **Eliminar senha** — **Magic Link** por e-mail, ou login social (Google/GitHub via [[wiki/concepts/oauth2]]/[[wiki/concepts/openid-connect]]). Não há segredo do usuário para armazenar ou vazar no aplicativo.

## Por Que Terceirizar

Argumento central: desenvolvedores em geral não são especialistas em segurança, e a superfície de erro em autenticação é grande (rotação de pepper, geração de salt, work factor de hash, sessão, MFA). Delegar para algo já testado em produção por muitos outros times reduz a chance de erro monumental — especialmente relevante para times pequenos (ex.: solo founder de SaaS) sem capacidade de manter expertise de segurança interna.

## Trade-off

Quanto mais alto na escada, menos controle e maior dependência de um fornecedor externo — decisão de arquitetura, não só de segurança. Nenhum dos quatro níveis é estritamente "certo"; a escolha depende de quanto risco/complexidade o time está disposto a manter internamente.

## Relação com Outros Conceitos

- [[wiki/concepts/password-hashing]] — o que os níveis 1 e 2 ainda exigem entender
- [[wiki/concepts/oauth2]] / [[wiki/concepts/openid-connect]] — mecanismo por trás do login social no nível 4
- [[wiki/concepts/federated-identity]] — mesma lógica de terceirização de confiança, em contexto corporativo/B2B

## Key Sources

- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]]
