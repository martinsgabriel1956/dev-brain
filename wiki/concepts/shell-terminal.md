---
type: concept
title: "Shell / Terminal"
aliases: ["terminal", "shell", "linha de comando", "cli", "prompt de comando"]
date_created: 2026-08-11
date_updated: 2026-09-30
source_count: 2
tags: [shell, terminal, cli, linux, bash, zsh, tech-mentor-infra]
skill: tech-mentor-infra
status: stub
---

# Shell / Terminal

Interface de texto para executar comandos direto na máquina, sem precisar de interface gráfica. O terminal é o programa que lê o que você digita; o shell (`bash`, `zsh`…) é o interpretador que executa os comandos e resolve variáveis.

## Ideia central

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]: **tudo que você faz por interface gráfica — criar pastas, criar/escrever arquivos, rodar softwares — também dá para fazer pelo terminal.** Antigamente os computadores eram baseados nisso; depois a computação caminhou para janelas e ícones, mas a camada de comando continua sendo a forma canônica de operar servidores.

## Onde o terminal é a única/melhor opção

- **[[wiki/concepts/ssh|SSH]] em produção** — geralmente não há interface gráfica (e quando há, é travada).
- **Pipelines de [[wiki/concepts/ci-cd|CI/CD]]** — passos são comandos de shell.
- **[[wiki/concepts/harness|Harnesses]] de IA** — a harness roda comandos de shell para ler/escrever arquivos na máquina (ver [[wiki/concepts/comandos-basicos-linux]]).

## Configuração persistente

Variáveis e ajustes que devem valer sempre que o terminal inicia ficam em arquivos de rc do shell (`.zshrc` para zsh, `.bashrc` para bash) — ver [[wiki/concepts/variaveis-de-ambiente]].

## Terminal ≠ TTY ≠ shell (PTY na prática)

Segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: o "terminal" atual é um [[wiki/concepts/emulador-de-terminal|emulador]] que fala com o master de um [[wiki/concepts/pty-pseudoterminal|PTY]]; o **shell** (Bash, Zsh) é só um processo filho cujo stdin/stdout/stderr foram apontados ao slave ([[wiki/concepts/fork-e-heranca-de-file-descriptors]]). O [[wiki/concepts/tty-teletypewriter|TTY]] físico original segue funcionando.

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — PTY, TTY, emulador e shell distinguidos, com demo em Python
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
