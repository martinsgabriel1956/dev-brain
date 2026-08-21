---
type: concept
title: "XSS (Cross-Site Scripting)"
aliases: ["xss", "cross-site scripting", "injeção javascript", "script injection"]
date_created: 2026-06-10
date_updated: 2026-08-19
source_count: 5
tags: [security, xss, owasp, appsec, input-sanitization, attack-surface, dvwa, csp]
skill: tech-mentor-security
status: draft
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

## Blocklist de Tag é Frágil — Demonstração Prática em [[wiki/concepts/dvwa]]

Um filtro que remove só a substring `<script>` não neutraliza XSS: qualquer tag com atributo de evento (`<img src=x onerror=alert(1)>`, `<body onload=alert(1)>`, `onmouseover`) executa JavaScript sem nunca usar a palavra "script". Em [[wiki/sources/xss-cross-site-scripting-luiz-viana]], esse padrão se repete nos níveis "medium" e "high" do DVWA (Damn Vulnerable Web Application) — reflected, stored e DOM-based — mesmo com o filtro de servidor ativo, porque ele foi escrito como blocklist de uma tag específica, não como allowlist/output encoding. Só no nível "impossible" a sanitização de fato funciona, porque o navegador passa a receber texto encodado em vez de HTML interpretável.

## Restrição Client-Side Não é Defesa

O DVWA nível "medium"/"high" do Stored XSS ilustra um caso concreto do princípio de [[wiki/concepts/confiar-no-frontend]]: o campo de nome tem `maxlength="10"` no HTML, mas isso é só uma restrição de UI — removendo o atributo via DevTools, um payload maior é digitado normalmente e segue para validação real (do lado do servidor). O `maxlength` nunca foi a defesa; era apenas conveniência de formulário.

## DOM-Based XSS Não Passa Pelo Servidor — Nem Logs, Nem WAF Veem

No DOM-based XSS, o JavaScript client-side lê dados (ex.: `location.hash`, um parâmetro de URL) e escreve isso direto no DOM sem nenhum salto pelo servidor. Isso tem uma implicação defensiva relevante: um [[wiki/concepts/waf]] inspeciona tráfego HTTP entre cliente e servidor — se o payload nunca é enviado ao servidor (por exemplo, indo depois de uma hashtag `#` na URL, que por definição do protocolo nunca é transmitida na requisição), o WAF não tem nada para inspecionar. A defesa nesse caso tem que estar no próprio código client-side (usar `textContent` em vez de `innerHTML`, nunca montar HTML a partir de `location.hash` sem sanitizar).

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
- [[wiki/concepts/dvwa]] — laboratório usado para demonstrar bypass de blocklist e restrição client-side na prática
- [[wiki/concepts/confiar-no-frontend]] — `maxlength` de formulário é o mesmo anti-padrão de validação só no cliente
- [[wiki/concepts/waf]] — não detecta DOM XSS quando o payload nunca passa pelo servidor
- [[wiki/concepts/bug-bounty]] — XSS é uma das falhas mais comuns reportadas em programas de bug bounty

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — mencionado como exemplo de vulnerabilidade detectada por SAST (SonarQube)
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — teste manual de injeção de script como parte de checklist de autopentest assistido por IA
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — roubo de token via localStorage vs. proteção de cookie HttpOnly; CSP como camada de defesa
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — citado, junto de [[sql-injection]], como padrão inseguro comum em projetos públicos usados como dado de treinamento de LLMs de código
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — motivo central de excluir `localStorage` como opção de armazenamento do refresh token
- [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — demonstração prática no DVWA: bypass de blocklist de tag, restrição client-side (`maxlength`) contornável, e limite do WAF contra DOM XSS
