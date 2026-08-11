---
type: concept
title: "Pipe Operator (|)"
aliases: ["pipe", "pipe operator", "|", "pipeline de shell", "encadear comandos"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [linux, shell, pipe-operator, cli, composicao, tech-mentor-infra]
skill: tech-mentor-infra
status: stub
---

# Pipe Operator (|)

O operador `|` conecta comandos: pega o **output** (stdout) de um comando e o usa como **input** (stdin) do próximo. É a base da composição de comandos no shell — fazer duas (ou várias) coisas juntas.

## Exemplo

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]:

```bash
cat agents.md | grep "erro"
```

O `cat` imprime o arquivo; o `|` passa esse output como input para o `grep`, que filtra e imprime só a linha com `erro`. Dá para encadear vários pipes, e combinar com [[wiki/concepts/codigo-grepavel|grep]] e `sed` para transformações mais elaboradas.

## Uso prático relacionado

Um padrão comum citado (não demonstrado): matar um processo que ocupa a porta 3000 — pegar o output de listagem de processos, filtrar com `grep` via pipe e passar o PID para `kill`.

## Relação com outros conceitos

- [[wiki/concepts/comandos-basicos-linux]] — pipe no conjunto básico.
- [[wiki/concepts/pipeline-de-ci]] — analogia distinta: "pipeline" de CI é fluxo de estágios; aqui é composição de stdout→stdin no shell.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
