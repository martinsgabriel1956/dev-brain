---
type: concept
title: "Instalação Global vs. Local de Pacotes"
aliases: ["npm install -g", "dependência global", "devDependencies"]
date_created: 2026-11-12
date_updated: 2026-11-12
source_count: 1
tags: [npm, dependencias, gerenciador-de-pacotes, tooling]
skill: tech-mentor-frontend
status: stub
---

# Instalação Global vs. Local de Pacotes

`npm install -g` instala o pacote na máquina, fora de qualquer projeto, e expõe o comando no terminal. É o uso típico de CLIs ([[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]). Sem `-g`, o pacote vai para o `node_modules` e para o `package.json` do projeto, como `dependencies` (vai para a aplicação) ou `devDependencies` (só ferramenta de build e teste).

## Trade-off

Pacote global não entra no `package.json` nem no lockfile, então cada máquina pode ter uma versão diferente. Por isso o caminho atual prefere rodar a ferramenta sob demanda: `npm create vue@latest` baixa e executa o `create-vue` sem deixar nada global. Ver [[wiki/concepts/scaffolding-de-projeto]]. Em Linux com Node do apt, o `-g` grava em diretório do sistema e pode exigir `sudo`, problema que gerenciadores de versão (nvm, fnm) evitam `[skill: tech-mentor-frontend]`.

Ver [[wiki/concepts/gerenciador-de-pacotes]].

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
