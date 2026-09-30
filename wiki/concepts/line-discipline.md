---
type: concept
title: "Line Discipline"
aliases: ['line discipline', 'disciplina de linha', 'icanon', 'stty']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [terminal, kernel, tty, pty, tech-mentor-infra]
skill: tech-mentor-security
status: draft
---

# Line Discipline

Componente do [[wiki/concepts/kernel]] entre o master e o slave de um [[wiki/concepts/pty-pseudoterminal|PTY]]. Segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]:

- **Echo:** a tecla digitada vai ao kernel e volta para a tela (`echo` ativo). `stty -echo` desliga: passa a haver input sem output (útil para senhas em terminais de papel).
- **Buffer de linha (modo canônico, `icanon`):** segura as teclas até o Enter, para que nenhum processo receba cada tecla isoladamente (o que não seria prudente).
- **Edição de linha:** digitar `ls`, apagar e corrigir sem acionar programa algum.

`stty -a` lista as flags (`icanon`, `echo`…; `-flag` = desativada). Programas de tela cheia como `htop` colocam o terminal em modo diferente `[external, não detalhado na fonte]`. Ver [[wiki/concepts/tty-teletypewriter]] e [[wiki/concepts/emulador-de-terminal]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
