---
type: concept
title: "XSS (Cross-Site Scripting)"
aliases: ["xss", "cross-site scripting", "injeção javascript", "script injection"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
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

## Relação com Outros Conceitos

- [[attack-surface]] — qualquer ponto que renderiza input do usuário é superfície de ataque para XSS
- [[sql-injection]] — mesma classe de vulnerabilidade (code injection), contexto diferente
- [[sast]] — SAST detecta padrões de XSS estaticamente no código

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — mencionado como exemplo de vulnerabilidade detectada por SAST (SonarQube)
