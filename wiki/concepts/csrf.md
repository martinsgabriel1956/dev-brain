---
type: concept
title: "CSRF (Cross-Site Request Forgery)"
aliases: ['csrf', 'xsrf', 'cross-site request forgery']
date_created: 2026-09-30
date_updated: 2026-11-03
source_count: 2
tags: [csrf, seguranca, cookies, owasp, tech-mentor-security]
skill: tech-mentor-security
status: draft
---

# CSRF (Cross-Site Request Forgery)

Um site malicioso aproveita os cookies de um usuário logado na aplicação para executar ações em nome dele, se a aplicação não estiver protegida ([[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]).

## Mecanismo

O ataque junta dois comportamentos legítimos do navegador ([[wiki/sources/csrf-cross-site-request-forgery]]):

1. A [[wiki/concepts/same-origin-policy|same-origin policy]] bloqueia leitura entre origens, mas geralmente permite escrita, como o envio de um formulário.
2. O navegador anexa os cookies de sessão por conta própria ([[wiki/concepts/sessoes-http-cookies]]).

A política nunca é violada: a requisição autenticada basta, e o atacante não precisa ler a resposta.

## Exemplos

- **Banco:** a vítima abre um link recebido por e-mail. A página tem um iframe com formulário invisível, enviado por script no carregamento, que faz uma transferência para o atacante.
- **Laboratório da [[wiki/entities/portswigger|PortSwigger]]:** o POST de troca de e-mail leva só o novo valor, sem o e-mail antigo nem token. O HTML do ataque é hospedado no servidor de exploit e entregue à vítima.

[external] A [PortSwigger](https://portswigger.net/web-security/csrf) exige três condições: ação relevante, sessão baseada só em cookie e nenhum parâmetro imprevisível.

## Defesas

- [[wiki/concepts/csrf-token]] — valor imprevisível exigido nas ações sensíveis.
- [[wiki/concepts/samesite-cookie]] — `SameSite=Strict` foi a mitigação demonstrada em [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]], junto de `HttpOnly` e `Secure`. `[skill: tech-mentor-security]` `Lax` mitiga a maioria dos casos. Tem bypasses conhecidos.

[external] O [cheat sheet da OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) manda começar pela proteção do framework e usar tokens em todas as requisições que alteram estado. Aceita Fetch Metadata para software que só atende navegadores modernos, com fallback obrigatório. `SameSite` e a verificação de origem ficam em defesa em profundidade. [[wiki/concepts/xss]] derruba todas essas mitigações.

## Correlatos

[[wiki/concepts/cross-site-websocket-hijacking]], [[wiki/concepts/xss]], [[wiki/concepts/cors-misconfiguration]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
- [[wiki/sources/csrf-cross-site-request-forgery]] — mecanismo completo, cenário do banco, laboratório e duas defesas
