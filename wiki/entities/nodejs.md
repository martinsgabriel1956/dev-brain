---
type: entity
title: "Node.js"
aliases: ["Node", "node"]
date_created: 2026-11-12
date_updated: 2026-11-16
source_count: 8
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

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] apresenta o Node como quem entende JavaScript fora do navegador: "o meu computador vai precisar do Node.js", que "usa o motor de JavaScript do Chrome".
- **Instalação:** baixa a LTS ("mais estável") e não a Current. A versão mostrada é a 12.18.
- **No terminal:** testa com `node -v` e entra no REPL com `node` (sai com `.exit`).
- **No Ecoleta:** roda `node src/server.js` e depois o nodemon. `[skill: lang-dynamic]` Hoje a LTS de produção é o 24, e `node --watch` substitui o nodemon. Ver [[wiki/entities/express]].

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o Node 12 LTS é instalado por gerenciador de pacotes (Homebrew, Chocolatey, NodeSource), com npm e npx, e roda TypeScript via `ts-node`. `[skill: lang-dynamic]` Hoje o Node 26 é Active LTS (desde 28/10/2026) e roda `.ts` nativamente por type stripping.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], `crypto.randomBytes(6).toString('hex')` gera nomes únicos de arquivo, e `path.resolve(__dirname, '..', '..', 'uploads')` monta o destino.

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]
- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: JavaScript fora do navegador; versão LTS
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: LTS 12.18, REPL, node src/server.js, nodemon
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: Node 12 LTS por gerenciador de pacotes, npx, ts-node
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: crypto e path no upload
