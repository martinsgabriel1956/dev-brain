---
type: concept
title: "XSS (Cross-Site Scripting)"
aliases: ["xss", "cross-site scripting", "injeção javascript", "script injection"]
date_created: 2026-06-10
date_updated: 2026-08-03
source_count: 3
tags: [security, xss, owasp, appsec, input-sanitization, attack-surface]
skill: tech-mentor-security
status: stub
---

# XSS (Cross-Site Scripting)

Vulnerabilidade que permite injetar código JavaScript malicioso em páginas servidas a outros usuários. O atacante aproveita que a aplicação renderiza input sem sanitizar, executando scripts no contexto do browser da vítima.

## Tipos

| Tipo | Mecanismo |
|---|---|
| **Reflected** | Payload na URL/request; executado na resposta imediata |
| **Stored** | Payload armazenado no banco; executado para todos que visitam a página |
| **DOM-based** | Manipulação do DOM via JavaScript sem passar pelo servidor |

## O Que um Atacante Consegue

- Roubar cookies de sessão (`document.cookie`)
- Fazer requisições autenticadas em nome da vítima (CSRF via XSS)
- Redirecionar para sites de phishing
- Keylogging, captura de formulários

## Como Prevenir

- **Output encoding:** escapar `<`, `>`, `"`, `'`, `&` antes de renderizar no HTML
- **Content Security Policy (CSP):** restringir quais scripts podem executar
- **Frameworks modernos:** React, Vue, Angular escapam por padrão — evitar `dangerouslySetInnerHTML` ou `v-html` com dados externos
- **Sanitização de input:** validar e limpar na fronteira do sistema

## Relação com SQL Injection

XSS e [[sql-injection]] são instâncias do mesmo padrão: input não sanitizado injetado em um contexto interpretável (SQL no caso do SQLi, HTML/JS no caso do XSS). A mitigação também segue o mesmo princípio: separar dados de código, nunca confiar em input externo.

## Roubo de Token Via XSS: Motivo Prático Para Cookie `HttpOnly`

Se um token de autenticação (sessão ou [[wiki/concepts/jwt|JWT]]) está guardado em `localStorage`, um script injetado via XSS lê `localStorage` diretamente e exfiltra o token para um servidor externo. Um cookie `HttpOnly` neutraliza esse vetor específico — o script injetado não consegue ler o valor do cookie, mesmo com execução JS completa na página.

## Relação com Outros Conceitos

- [[attack-surface]] — qualquer ponto que renderiza input do usuário é superfície de ataque para XSS
- [[sql-injection]] — mesma classe de vulnerabilidade (code injection), contexto diferente
- [[sast]] — SAST detecta padrões de XSS estaticamente no código
- [[wiki/concepts/sessoes-http-cookies]] / [[wiki/concepts/jwt]] — flag `HttpOnly` como defesa direta contra roubo de token via XSS
- [[wiki/concepts/cors-misconfiguration]] — falha correlata: ambas exploram confiança excessiva em origem/input não validado

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — mencionado como exemplo de vulnerabilidade detectada por SAST (SonarQube)
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — teste manual de injeção de script como parte de checklist de autopentest assistido por IA
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — roubo de token via localStorage vs. proteção de cookie HttpOnly; CSP como camada de defesa
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — citado, junto de [[sql-injection]], como padrão inseguro comum em projetos públicos usados como dado de treinamento de LLMs de código
