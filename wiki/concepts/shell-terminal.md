---
type: concept
title: "Shell / Terminal"
aliases: ["terminal", "shell", "linha de comando", "cli", "prompt de comando"]
date_created: 2026-08-11
date_updated: 2026-11-16
source_count: 5
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

## Git Bash no Windows e sudo no Linux

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], o Git Bash é a "janelinha preta" para digitar comandos no Windows "como se estivesse no Linux". No [[wiki/entities/vs-code]], Terminal → New Terminal; quem instalou o Git depois do editor escolhe o Git Bash no "+" e o marca como padrão (a lista também mostra PowerShell, JavaScript Debug Terminal e Ubuntu 20.04 no WSL). No Linux, `sudo` ("me torne super usuário") ou `su` antes do `apt install`. `[external]` `su` é *substitute user*, não "super user": https://man7.org/linux/man-pages/man1/su.1.html.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa o Git Bash no Windows para que os comandos se pareçam com os de Mac e Linux, já que em produção "você vai provavelmente usar um ambiente Linux". Para ele, CMD e PowerShell são "um pouco mais diferentes". `[external]` O Git Bash é um bash sobre o Windows (MSYS2), não um Linux; o WSL roda Linux de verdade (https://learn.microsoft.com/en-us/windows/wsl/about).

## Por que o curso evitou a linha de comando

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], [[wiki/entities/nasser|Násser]] instala o Sass por aplicativo porque a linha de comando "talvez exija de vocês um conhecimento prévio maior" e muda entre Windows, Linux e Mac, embora "não é nenhum bicho de sete cabeças". `[external]` A CLI do Dart Sass via npm é a mesma nos três sistemas.

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — PTY, TTY, emulador e shell distinguidos, com demo em Python
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Git Bash como terminal padrão no VS Code; sudo/su
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: Git Bash no Windows; não é Linux
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: linha de comando evitada na instalação do Sass
