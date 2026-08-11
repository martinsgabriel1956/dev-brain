---
type: concept
title: "Shell / Terminal"
aliases: ["terminal", "shell", "linha de comando", "cli", "prompt de comando"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
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

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
