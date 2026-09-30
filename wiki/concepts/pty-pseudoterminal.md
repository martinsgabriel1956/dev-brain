---
type: concept
title: "PTY (Pseudoterminal)"
aliases: ['pty', 'pseudoterminal', 'pseudo-tty', 'openpty', 'master e slave']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [pty, terminal, unix, kernel, tech-mentor-infra]
skill: tech-mentor-security
status: draft
---

# PTY (Pseudoterminal)

**PTY** (*pseudoteletype*) é um terminal **virtual** que o kernel Unix-like entrega sob demanda para "fingir" o [[wiki/concepts/tty-teletypewriter|TTY]] físico. Tem **duas pontas**, ambas tratadas como arquivos especiais:

- **master** — usado pelo [[wiki/concepts/emulador-de-terminal]] (a janela): ele lê e escreve aqui.
- **slave** — aparece como `/dev/pts/N` (comando `tty`); o shell o usa como se fosse um teletype normal.

Entre master e slave, dentro do [[wiki/concepts/kernel]], fica a [[wiki/concepts/line-discipline]]. Ver o mecanismo de ligar o shell ao slave em [[wiki/concepts/fork-e-heranca-de-file-descriptors]].

Segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]], o autor abre o PTY com o módulo `os` do Python (`openpty`) para provar que qualquer linguagem (C incluída) consegue fazer o mesmo; é a base de [[wiki/concepts/emulador-de-terminal|emuladores]], de [[wiki/concepts/ssh]] (o `sshd` ocupa o lado master no servidor remoto) e do [[wiki/concepts/terminal-web-broker-websocket-ssh|terminal web]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
