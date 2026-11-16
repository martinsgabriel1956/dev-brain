---
type: entity
title: "Node.js"
aliases: ["Node", "node"]
date_created: 2026-11-12
date_updated: 2026-11-16
source_count: 5
tags: [nodejs, javascript, runtime, v8, backend, tooling]
skill: tech-mentor-frontend
status: stub
---

# Node.js

Runtime JavaScript sobre o V8. No front end aparece como pré-requisito de ferramentas: traz o npm embutido e roda bundlers, CLIs e o servidor de desenvolvimento ([[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]). No back end, ver [[wiki/concepts/event-loop-performance-js]] e [[wiki/concepts/cpu-profiling]].

## Instalação

Instalador do site (Windows, Mac), Homebrew (`brew install node`, que instala o npm à parte) ou apt no Linux (pacote `nodejs`, que costuma vir em versão antiga). Ferramentas como o `create-vue` declaram versão mínima em `engines` (`^22.18.0 || >=24.12.0`), então a versão do repositório da distribuição pode não servir. Ver [[wiki/concepts/gerenciador-de-pacotes]].

## No FrontPUSH: JavaScript fora do navegador e versão LTS

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], [[wiki/entities/nasser|Násser]] explica o Node como o jeito de rodar JavaScript "fora do ambiente do browser" e de instalar pacotes como o [[wiki/entities/react]]; para HTML, CSS e JavaScript puros não é preciso. Recomenda a versão LTS, "mais estável", contra a mais atual, que "pode conter bugs". `[external]` LTS = *Long Term Support*; as versões pares do Node viram LTS e recebem correções por cerca de 30 meses: https://nodejs.org/en/about/previous-releases.

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]
- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: JavaScript fora do navegador; versão LTS
