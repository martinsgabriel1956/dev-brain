---
type: concept
title: "Fork e Herança de File Descriptors"
aliases: ['fork', 'herança de file descriptors', 'redirecionamento de stdout', 'dup2']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [unix, processo, fork, file-descriptor, shell, tech-mentor-infra]
skill: tech-mentor-security
status: draft
---

# Fork e Herança de File Descriptors

`fork()` **duplica** um [[wiki/concepts/processo]]: o retorno é `0` no filho e diferente de 0 (o PID do filho) no pai. O filho **herda** `stdin` (0), `stdout` (1) e `stderr` (2) de quem o iniciou (o shell, cujo PID é `$$`), e pode **repontá-los** para outro lugar (um arquivo, o slave de um [[wiki/concepts/pty-pseudoterminal|PTY]]). Depois, a substituição do processo por outro programa (`exec`) transforma o clone em `bash`.

É assim que um shell funciona ([[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]): ao rodar `ls`, o shell faz fork e o `ls` herda os mesmos descritores, então sua saída cai no mesmo PTY e volta ao emulador. O mesmo vale para o cliente SSH ([[wiki/concepts/ssh]]). Ver [[wiki/concepts/shell-terminal]], [[wiki/concepts/kernel]], [[wiki/concepts/line-discipline]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
