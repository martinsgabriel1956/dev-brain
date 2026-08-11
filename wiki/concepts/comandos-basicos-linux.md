---
type: concept
title: "Comandos Básicos de Linux"
aliases: ["comandos linux", "comandos de shell", "cli linux", "ls cd mkdir cat"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [linux, shell, cli, comandos-linux, cs-fundamentals, tech-mentor-infra, harness]
skill: tech-mentor-infra
status: draft
---

# Comandos Básicos de Linux

Conjunto mínimo de comandos de shell que todo dev deve **reconhecer** (não decorar) para operar máquinas Linux/Unix — localmente, via [[wiki/concepts/ssh|SSH]] em produção, ou dentro de pipelines de [[wiki/concepts/ci-cd|CI/CD]]. O mesmo conjunto é o que uma [[wiki/concepts/harness|harness]] de IA executa por baixo dos panos para manipular arquivos (ver [[wiki/concepts/tool-call]]).

## Por que importa na era dos agentes

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]], a principal razão para conhecer esses comandos hoje não é só administrar servidores: **é assim que as IAs manipulam o seu computador**. Um [[wiki/entities/claude-code|Claude Code]] não abre editor gráfico — ele roda `cat`, `echo`, `grep`, `sed` nativos, e envia o output ao servidor da [[wiki/entities/anthropic|Anthropic]]. Reconhecer o comando numa pipeline ou num log de agente é o objetivo prático.

## Referência rápida

| Comando | O que faz |
|---|---|
| `pwd` | print working directory — mostra o diretório atual |
| `ls` / `ls -l` | lista arquivos / lista com detalhes (tipo, permissões, dono) |
| `cd dir` / `cd ..` / `cd ~` / `cd -` | muda de diretório / sobe um / vai à home / volta ao anterior |
| `mkdir dir` / `mkdir -p a/b/c` | cria diretório / cria pais e aninhados de uma vez |
| `touch arquivo` | cria arquivo vazio |
| `echo txt > f` / `echo txt >> f` | escreve sobrescrevendo / faz **append** no final |
| `cat f` | imprime o conteúdo do arquivo |
| `cp a b` / `mv a dir/` | copia / move (some da origem) |
| `rm f` / `rm -rf dir` | remove arquivo / remove diretório recursivo + force |
| `chmod +x f` | adiciona permissão de execução — ver [[wiki/concepts/permissoes-unix]] |
| `sudo cmd` | executa como super user/admin |
| `export VAR=v` / `echo $VAR` | define / lê variável — ver [[wiki/concepts/variaveis-de-ambiente]] |
| `grep -inr termo` | busca (case-insensitive, nº de linha, recursivo) — ver [[wiki/concepts/codigo-grepavel]] |
| `cmd1 \| cmd2` | pipe: output de um vira input do outro — ver [[wiki/concepts/pipe-operator]] |
| `sed 's/A/B/' f` | substitui texto |
| `git init` | inicializa repo (cria a pasta oculta `.git`) — ver [[wiki/concepts/git]] |

## Cuidados

- **`rm -rf` não pede confirmação** e deleta recursivamente — rodar em pasta core do sistema quebra tudo rápido.
- Arquivos que começam com ponto (`.env`, `.git`, `.zshrc`, `.DS_Store`) são **ocultos** por padrão.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
