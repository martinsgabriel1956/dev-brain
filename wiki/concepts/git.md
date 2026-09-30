---
type: concept
title: "Git"
aliases: ["git", "git init", ".git", "controle de versão"]
date_created: 2026-08-11
date_updated: 2026-09-29
source_count: 3
tags: [git, controle-de-versao, cli, tech-mentor-leadership]
skill: tech-mentor-infra
status: stub
---

# Git

Sistema de controle de versão distribuído. Página guarda-chuva para os fluxos e comandos Git já documentados em detalhe em páginas específicas.

## git init e a pasta `.git`

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]], `git init` não cria nada visível, mas gera a pasta **oculta `.git`** (um diretório — `ls -l` mostra o `d`). É onde o Git guarda o estado do repositório: branch atual, arquivos staged, etc. Deletar `.git` obriga a reconfigurar o repositório do zero.

## Git ≠ GitHub

Segundo [[wiki/entities/andre-casciotti]] ([[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]]), **Git** é o sistema de versionamento em si — funciona mesmo só localmente, sem nenhum servidor remoto. **GitHub** é um repositório **descentralizado** onde uma empresa guarda seus fontes (às vezes on-premises, via GitHub Enterprise; o mecanismo por trás pode também ser GitLab, Bitbucket ou outro). Recomendação para quem está começando: aprender o *porquê* o Git funciona como funciona (o que cada comando realmente faz ao estado do repositório), não só decorar comandos.

## Páginas relacionadas

- [[wiki/concepts/git-flow]] · [[wiki/concepts/trunk-based-development]]
- [[wiki/concepts/rebase-vs-merge]] · [[wiki/concepts/atomic-commits]]
- [[wiki/concepts/comandos-basicos-linux]]

## Atomic commits e cherry-pick

[[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]] usa o Git como ferramenta de planejamento via commits atômicos ([[wiki/concepts/atomic-commits]]) e cita `cherry-pick` como motivo para o menor commit possível.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
- [[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]] — distinção Git (versionamento local) vs. GitHub (repositório descentralizado)
- [[wiki/sources/como-ser-otimo-programador-sem-usar-o-cerebro]] — commits atômicos e cherry-pick como motivo
