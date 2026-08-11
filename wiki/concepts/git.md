---
type: concept
title: "Git"
aliases: ["git", "git init", ".git", "controle de versão"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [git, controle-de-versao, cli, tech-mentor-leadership]
skill: tech-mentor-infra
status: stub
---

# Git

Sistema de controle de versão distribuído. Página guarda-chuva para os fluxos e comandos Git já documentados em detalhe em páginas específicas.

## git init e a pasta `.git`

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]], `git init` não cria nada visível, mas gera a pasta **oculta `.git`** (um diretório — `ls -l` mostra o `d`). É onde o Git guarda o estado do repositório: branch atual, arquivos staged, etc. Deletar `.git` obriga a reconfigurar o repositório do zero.

## Páginas relacionadas

- [[wiki/concepts/git-flow]] · [[wiki/concepts/trunk-based-development]]
- [[wiki/concepts/rebase-vs-merge]] · [[wiki/concepts/atomic-commits]]
- [[wiki/concepts/comandos-basicos-linux]]

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
