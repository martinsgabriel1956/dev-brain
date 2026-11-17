---
type: entity
title: "Node.js"
aliases: ["Node", "node"]
date_created: 2026-11-12
date_updated: 2026-11-16
source_count: 18
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

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o Node "nasceu com o intuito de rodar o JavaScript na máquina"; a aula instala a LTS 12.18.3 (fora de suporte desde abril de 2022), confere com `node -v`/`npm -v` e roda `node src/server.js`. "O console do back-end é o terminal."

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], `module.exports` exporta a promessa do banco e objetos de funções (`utils/format.js`, `pages.js`), e `require` os recupera com desestruturação. `__dirname` monta o caminho do `database.sqlite`, o que evita o problema de caminho relativo da NLW #1.

## No JStack, aula 01 (Mateus Silva)

Em [[wiki/sources/jstack-como-funciona-o-nodejs]], o Node "não é uma linguagem de programação", é "uma plataforma, ou [...] runtime": o [[wiki/entities/v8|V8]] do Chrome (2008) levado ao servidor por [[wiki/entities/ryan-dahl|Ryan Dahl]] (2009), sobre a [[wiki/entities/libuv|libuv]]. Single thread ("apenas uma Call Stack"), mas [[wiki/concepts/non-blocking-io|non-blocking I/O]] graças ao [[wiki/concepts/thread-pool]] e ao [[wiki/concepts/event-loop-performance-js|event loop]]. A wiki corrige: I/O de rede não passa pelo pool, e o V8 compila com JIT.

## Na NLW #2, dia 2 (Diego Fernandes)

Defendido pelo mesmo JavaScript do front e do mobile e pelo non-blocking I/O; streams e worker threads como "as coisas mais legais"; Deno como "o irmão do Node". Node 12.18 LTS na gravação. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], o Node é instalado na aula 02 do módulo de JavaScript, e a aula 01 diz que o JS serve "tanto no front-end como no back-end", sem nomear o runtime.

## No JStack, aula 03 (Mateus Silva)

Em [[wiki/sources/jstack-o-que-sao-modulos]]: `node index.js` roda um arquivo (a extensão pode ser omitida); três tipos de módulo (próprios, nativos como `http`, `os`, `dns`, `v8`, e pacotes do npm); `require` e `module.exports` (CommonJS); `require('os')` e `os.type()` → `Darwin`. Ver [[wiki/concepts/modulos-nodejs]].

## No JStack, aula 04 (Mateus Silva)

Em [[wiki/sources/jstack-criando-o-servidor-http]]: `http.createServer((request, response) => ...)`, `writeHead(200, {'Content-Type': 'text/html'})`, `end('<h1>...')` e `listen(3000, callback)`, rodando com `node src/index.js`. O Node não recarrega o código sozinho; a aula reinicia à mão e cita o nodemon, mas o `node --watch` nativo (estável desde o 22) resolve sem pacote `[skill: lang-dynamic]`.

## No JStack, aula 05 (Mateus Silva)

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: `request.method` e `request.url` no handler do `createServer`, `GET /users` respondendo `JSON.stringify(users)` com `application/json`, e 404 de fallback. `request.url` inclui a query string; o caminho limpo vem de `new URL(request.url, base).pathname`. Ver [[wiki/concepts/roteamento-http]].

## No JStack, aula 06 (Mateus Silva)

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: tabela de rotas em `src/routes.js` com `find` e handlers em `src/controllers/UserController.js`, ainda com o `http` puro. Ver [[wiki/concepts/roteamento-http]] e [[wiki/concepts/controller]].

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], o back-end "pode ser Node, que é JavaScript, ou pode ser, por exemplo, PHP": com JSON, a linguagem do servidor não importa para o front.

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]
- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: JavaScript fora do navegador; versão LTS
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: LTS 12.18, REPL, node src/server.js, nodemon
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: Node 12 LTS por gerenciador de pacotes, npx, ts-node
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: crypto e path no upload
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: LTS 12, node -v, console no terminal
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: module.exports, require, __dirname
- [[wiki/sources/jstack-como-funciona-o-nodejs]]: JStack aula 01: runtime, V8, call stack, libuv, thread pool, event loop
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: por que Node; streams e worker threads
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: JS no back-end
- [[wiki/sources/jstack-o-que-sao-modulos]]: JStack aula 03: node index.js, módulos, require, os
- [[wiki/sources/jstack-criando-o-servidor-http]]: JStack aula 04: servidor com http, sem reload
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: JStack aula 05: primeira rota GET /users
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: JStack aula 06: routes.js e controller
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: Node como exemplo de back-end
