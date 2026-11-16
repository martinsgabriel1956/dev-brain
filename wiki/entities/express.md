---
type: entity
title: "Express"
aliases: ["Express.js", "express", "ExpressJS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [nodejs, backend, framework, http, javascript]
skill: lang-dynamic
status: stub
---

# Express

Framework HTTP minimalista para o [[wiki/entities/nodejs|Node.js]]. O básico:
- `const app = express()` cria o servidor.
- `app.get/post(rota, (req, res) => ...)` define rotas.
- `app.use(...)` encadeia middlewares, como `express.static`, `express.json()` e `express.urlencoded()`.
- `app.listen(porta)` liga o servidor.

`[skill: lang-dynamic]` O Express 5 é a versão `latest` do npm (Node 18 ou mais novo). Ele repassa rejeições de handlers async para o `next(err)`, usa curingas nomeados nas rotas e deixa `req.body` como `undefined` sem parser. A skill compara: o Express tem o maior ecossistema, e o Fastify é 2 a 3 vezes mais rápido, com validação nativa. Para projetos novos, a skill recomenda Fastify.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] cria o servidor do Ecoleta:
- **Instalar e ligar:** `npm install express`, `require("express")`, `const server = express()` e `server.listen(3000)`. "Acredita que você criou um servidor com apenas três linhas de código?"
- **Rotas GET:** `server.get("/", (req, res) => ...)` para `/`, `/create-point` e `/search`, com `res.send`, depois `res.sendFile(__dirname + ...)` e por fim `res.render` do [[wiki/entities/nunjucks]].
- **Estáticos:** `server.use(express.static("public"))` serve CSS, scripts e imagens "como se as pastas já estivessem disponíveis aqui na raiz".
- **Alternativa:** dava para fazer o servidor "com o Node puro", mas "seria um arquivo muito grande".

Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/requisicao-http]].

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] adiciona `server.post("/savepoint", ...)`, `server.use(express.urlencoded({ extended: true }))` (sem ele, `req.body` vem `undefined`), `req.query.search` para a busca e respostas dentro dos callbacks do banco. `[skill: lang-dynamic]` No Express 5, `urlencoded` passa a ter `extended: false` por padrão.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o Express é "um micro framework para lidar com rotas", agora em TypeScript: `@types/express -D`, `app.get('/users')`, `response.json([...])` e `app.listen(3333)`.

Na API de [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]): `express.Router()` em `routes.ts`, `app.use(express.json())` para ler o body, `express.static` para `/uploads`, `cors()`, e handlers `async` em controllers. `[skill: lang-dynamic]` No Express 4, erro em handler async não chega ao tratador e deixa a requisição pendurada; o Express 5 resolve.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: `upload.single('image')` (Multer) e `celebrate(...)` como middlewares encadeados na rota `POST /points`, mais `app.use(errors())` para devolver 400 com as mensagens do Joi.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o Proffy usa `const server = express()`, `server.use(express.static("public"))`, rotas `get` com `(req, res)`, `res.send`, `res.sendFile(__dirname + ...)`, `res.render` e `res.redirect("/study")`, `req.query` para os filtros e `listen(5500)`. Tensão: `express.static("public")` é relativo ao diretório de onde o processo roda.

## Key sources

- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: servidor, rotas GET, `express.static` e integração com Nunjucks (Express 4, 2020)
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: POST, urlencoded, req.body, req.query
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: Express com TypeScript e @types/express, response.json
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: Router, express.json, express.static, cors, controllers
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: Multer e celebrate como middlewares de rota
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: static, rotas, req.query, redirect
