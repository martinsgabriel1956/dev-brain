---
type: concept
title: "TTY (Teletypewriter)"
aliases: ['tty', 'teletype', 'teleprinter', 'console', 'dumb terminal']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [tty, terminal, historia-da-computacao, unix, tech-mentor-infra]
skill: tech-mentor-security
status: draft
---

# TTY (Teletypewriter)

Dispositivo físico que precede o computador: teclado que emite um sinal, que vira dados, que uma impressora imprime à distância (teleprinter do telégrafo de ~1940). No Unix, um teletype conectava-se a um computador "do tamanho de uma parede" com suporte a várias sessões ([[wiki/entities/ken-thompson]], [[wiki/concepts/unix]]); várias TTYs podiam estar ligadas ao mesmo servidor. Era um **dumb terminal**: só digita a tecla e imprime/exibe os dados, sem sistema próprio.

Nomes correlatos segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: Teletype/TTY, **console** e **terminal** (a "telinha preta"). O TTY real continua funcionando em Linux moderno; os terminais atuais são [[wiki/concepts/emulador-de-terminal|emuladores]] que fingem esse dispositivo através de um [[wiki/concepts/pty-pseudoterminal|PTY]].

Ver também [[wiki/concepts/shell-terminal]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
