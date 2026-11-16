---
type: concept
title: "Emulador de Terminal"
aliases: ['emulador de terminal', 'terminal emulator', 'xterm.js']
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 2
tags: [terminal, tty, pty, xterm-js, tech-mentor-infra]
skill: tech-mentor-security
status: draft
---

# Emulador de Terminal

O que hoje se chama de "terminal" é um emulador: uma janela que fala com o **master** de um [[wiki/concepts/pty-pseudoterminal|PTY]], envia teclas (Enter → `\r`, Backspace, Ctrl+C) e **renderiza** os bytes que voltam. Segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]], "o maior trabalho do emulador é renderizar" — um terminal ingênuo (Tkinter com um `Text`) mostra lixo ao abrir `htop`, pois não interpreta as sequências de controle.

Na web, o emulador é o [[wiki/entities/xterm-js]], que conversa por WebSocket com um broker em vez de um PTY local ([[wiki/concepts/terminal-web-broker-websocket-ssh]]). Ver [[wiki/concepts/tty-teletypewriter]], [[wiki/concepts/line-discipline]], [[wiki/concepts/shell-terminal]].

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o Windows usa o Git Bash em vez de CMD e PowerShell ("uma ideia universal de sistemas Unix"), dentro do VS Code; Mac e Linux não precisam. Comandos: `cd /c/nlw`, `pwd`, Ctrl+L, Ctrl+C.

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: Git Bash no Windows
