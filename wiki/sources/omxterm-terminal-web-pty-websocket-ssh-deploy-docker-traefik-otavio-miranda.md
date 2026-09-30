---
type: source
title: "OMXTerm: Como Funciona o Terminal (TTY, PTY, Shell), Terminal Web com WebSocket + SSH, Deploy com Docker + Traefik e Segurança"
aliases: []
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [terminal, tty, pty, shell, websocket, ssh, xterm-js, traefik, docker, seguranca, csrf, dns-rebinding, agentes-ia, comprehension-debt, vibe-coding]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda.md
source_url: ""
author: "Otávio Miranda (inferido do cupom/domínio; título do vídeo não informado)"
date_published: ""
date_ingested: 2026-09-30
---

## TL;DR

Vídeo PT-BR em três blocos. **(1) Como o terminal funciona:** o "terminal" de hoje é um [[wiki/concepts/emulador-de-terminal|emulador]] que finge um [[wiki/concepts/tty-teletypewriter|TTY]] físico via [[wiki/concepts/pty-pseudoterminal|PTY]] (master/slave) + [[wiki/concepts/line-discipline]] no [[wiki/concepts/kernel]]; o shell é ligado ao slave por [[wiki/concepts/fork-e-heranca-de-file-descriptors|fork + redirecionamento de stdin/stdout/stderr]]; SSH repete o desenho com o `sshd` no lado remoto. **(2) Terminal na web:** [[wiki/entities/omxterm]] = xterm.js → WebSocket → broker → SSH, com autenticação em duas fases, cookies rígidos e [[wiki/concepts/ticket-de-uso-unico-websocket|ticket de uso único]] ([[wiki/concepts/terminal-web-broker-websocket-ssh]]); deploy em VPS Hostinger com Docker + [[wiki/entities/traefik]] + Let's Encrypt, rate limit em duas camadas e [[wiki/concepts/allowlist-de-destino-ssh|allowlist de destino]]. **(3) Lição sobre IA:** o código foi escrito por agentes num fluxo elaborado ([[wiki/concepts/auditoria-de-issue-por-agente-de-contexto-limpo]]), mas o autor levou ~2 meses para *entender* as 10 mil linhas e só percebeu ao tentar explicar — alerta de [[wiki/concepts/comprehension-debt]].

## Key Claims

1. **Terminais atuais são emuladores**; o TTY real ainda funciona no Linux moderno. *Evidência: afirmação do autor + demo em Python com `os.openpty`.* → [[wiki/concepts/tty-teletypewriter]], [[wiki/concepts/emulador-de-terminal]]
2. **PTY tem duas pontas (master/slave)**, ambas arquivos especiais; entre elas há a line discipline no kernel. *Evidência: demo de código.* → [[wiki/concepts/pty-pseudoterminal]]
3. **Line discipline** faz echo, buffer de linha e edição de linha; `stty -echo` demonstra o efeito. → [[wiki/concepts/line-discipline]]
4. **O shell é um processo filho com stdin/out/err apontados ao slave**; `ls` herda os mesmos descritores. *Evidência: demo de fork contando 1–10 e redirecionando stdout a arquivo.* → [[wiki/concepts/fork-e-heranca-de-file-descriptors]], [[wiki/concepts/processo]]
5. **SSH reutiliza o modelo**: cliente SSH local, `sshd` no master remoto. → [[wiki/concepts/ssh]]
6. **Terminal web = broker entre WebSocket e SSH**; cada tecla e cada resize viram mensagens (debounce no servidor). *Evidência: DevTools/Network.* → [[wiki/concepts/terminal-web-broker-websocket-ssh]]
7. **Cookies de sessão `HttpOnly` + `Secure` + `SameSite=Strict`** (device token, session id, session token) autenticam o HTTP; o WebSocket **não usa cookies**. → [[wiki/concepts/sessoes-http-cookies]], [[wiki/concepts/csrf]]
8. **Ticket de 60 s, uso único, apagado ao usar** — também previne CSWSH. → [[wiki/concepts/ticket-de-uso-unico-websocket]], [[wiki/concepts/cross-site-websocket-hijacking]]
9. **DNS rebinding:** resolve o domínio uma vez e usa só o IP. → [[wiki/concepts/dns-rebinding]]
10. **Allowlist de destino por IP** (não `/24`), replicada no UFW; IPs fixos na rede Docker. → [[wiki/concepts/allowlist-de-destino-ssh]]
11. **Rate limit em duas camadas** (Traefik + app: 10 tentativas/60 s bloqueiam o IP); timing attack fica mitigado por rate limit. → [[wiki/concepts/rate-limiting]], [[wiki/concepts/timing-attack]]
12. **Zero persistência**: só hashes de tokens são mantidos. → [[wiki/concepts/design-efemero-zero-persistencia]]
13. **Sem** RBAC, sem proteção DoS/DDoS própria (depende de borda: Hostinger/Cloudflare), sem `known_hosts`, sem WebGL addon. → [[wiki/entities/omxterm]]
14. **Fluxo com agentes:** PRD → 34 issues → auditoria com contexto limpo → orquestrador/writer/reviewer. Gasta muitos tokens. → [[wiki/concepts/auditoria-de-issue-por-agente-de-contexto-limpo]], [[wiki/concepts/revisao-por-agente-independente]]
15. **Entender ≠ ter gerado:** só ao tentar gravar uma explicação o autor viu que não entendia o próprio código; única saída achada: fazer/revisar o código. *Evidência: relato pessoal.* → [[wiki/concepts/comprehension-debt]], [[wiki/concepts/vibe-coding]]

## Entidades

- [[wiki/entities/omxterm]], [[wiki/entities/otavio-miranda]], [[wiki/entities/xterm-js]], [[wiki/entities/traefik]]
- Tocadas: [[wiki/entities/hostinger]] (bloco patrocinado, KVM2/KVM4, cupom), [[wiki/entities/ken-thompson]] (imagem do computador dos primeiros Unix)

## Conceitos

- Novos: [[wiki/concepts/pty-pseudoterminal]], [[wiki/concepts/tty-teletypewriter]], [[wiki/concepts/line-discipline]], [[wiki/concepts/emulador-de-terminal]], [[wiki/concepts/fork-e-heranca-de-file-descriptors]], [[wiki/concepts/terminal-web-broker-websocket-ssh]], [[wiki/concepts/ticket-de-uso-unico-websocket]], [[wiki/concepts/cross-site-websocket-hijacking]], [[wiki/concepts/csrf]], [[wiki/concepts/dns-rebinding]], [[wiki/concepts/allowlist-de-destino-ssh]], [[wiki/concepts/design-efemero-zero-persistencia]], [[wiki/concepts/auditoria-de-issue-por-agente-de-contexto-limpo]]
- Existentes: [[wiki/concepts/shell-terminal]], [[wiki/concepts/ssh]], [[wiki/concepts/kernel]], [[wiki/concepts/processo]], [[wiki/concepts/unix]], [[wiki/concepts/websocket-vs-polling]], [[wiki/concepts/sessoes-http-cookies]], [[wiki/concepts/xss]], [[wiki/concepts/waf]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/timing-attack]], [[wiki/concepts/reverse-proxy]], [[wiki/concepts/hardening-de-servidor]], [[wiki/concepts/vpn]], [[wiki/concepts/dns]], [[wiki/concepts/owasp]], [[wiki/concepts/comprehension-debt]], [[wiki/concepts/vibe-coding]], [[wiki/concepts/revisao-por-agente-independente]]

## Open Questions / Ressalvas

- **Nada foi verificado no código.** Repositório do OMXTerm e das skills do autor não foram acessados; "bastante seguro" é presunção do autor ("não posso garantir nada").
- **O broker recebe a chave privada SSH** do usuário (e passphrase) em trânsito; a garantia é só a política de descarte — não há como o usuário auditar isso `[inferência]`. Não confundir "não salvo" com "não vejo".
- **Reprodutibilidade do modelo mental:** o autor não define "entender"; a proposta de gravar-se explicando é heurística, não método validado.
- **Artigo de Linus Åkesson (2008)** só citado pelo ano; título não dito (provável "The TTY demystified") `[external, não verificado]`.
- Descrição do `sshd` "invertido" e do master/slave é simplificada pelo próprio autor ("vou simplificar aqui").
- Não há mitigação citada de `Origin` check para CSWSH; o ticket cobre o caso, mas é escolha de design, não garantia geral.
- Sem contradições com a wiki; complementa [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]] (timing attack), [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] (Traefik/DDoS) e as fontes de comprehension debt ([[wiki/sources/cognitive-debt-margaret-storey]]).
- Patrocínio Hostinger (KVM4, cupom) tratado como publicidade, sem avaliação técnica independente.

## Citações que valem guardar

> "O que a gente chama de terminal hoje... não são terminais reais; são emuladores de terminal."

> "Não salvo nada no servidor nem no computador do cliente. Tudo que eu recebo, eu descarto assim que possível."

> "Mesmo achando que você entendeu alguma coisa perfeitamente, tenta explicar essa coisa para alguém... você vai perceber que talvez não tenha entendido nada daquilo que é seu."
