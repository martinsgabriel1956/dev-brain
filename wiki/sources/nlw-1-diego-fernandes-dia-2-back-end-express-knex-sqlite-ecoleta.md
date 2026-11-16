---
type: source
title: "NLW #1 com Diego Fernandes, dia 2: back-end do Ecoleta com Express, Knex e SQLite"
aliases: ["NLW 1 Diego dia 2", "Ecoleta back-end Knex", "Ecoleta API Express TypeScript", "NLW 1 trilha Node dia 2"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, typescript, express, knex, sqlite, sql, api-rest, metodos-http, route-params, query-params, request-body, insomnia, migrations, seeds, transactions, chave-estrangeira, muitos-para-muitos, controllers, cors, express-static, backend, rocketseat, ecoleta, iniciante]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1 com Diego Fernandes, dia 2: back-end do Ecoleta com Express, Knex e SQLite

## TL;DR

Segunda aula (cerca de 2h) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #1]], depois do [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native|dia 1]]. Em "uma hora e pouco de código", a [[wiki/concepts/api-rest|API REST]] do Ecoleta fica pronta, menos o upload de imagens. A aula tem duas metades:

1. **Conceitos, com um array de usuários em memória.**
   - Rota x [[wiki/concepts/recurso-rest|recurso]]; [[wiki/concepts/metodos-http|métodos HTTP]] (GET, POST, PUT, DELETE).
   - O [[wiki/entities/insomnia]] para testar o que o navegador não chama pela barra de endereço.
   - Os três [[wiki/concepts/parametros-de-requisicao|tipos de parâmetro]]: route params (`/users/:id`), query params (`?search=on`) e request body (JSON, que exige `app.use(express.json())`).
2. **O back-end de verdade.**
   - SQL em vez de MongoDB, e [[wiki/concepts/sqlite]] para não instalar nada.
   - O [[wiki/concepts/query-builder]] [[wiki/entities/knex]]: `connection.ts`, [[wiki/concepts/database-migration|migrations]] com `up`/`down`, `knexfile.ts` e `knex migrate:latest`.
   - Três tabelas: `points`, `items` e a pivô `point_items`, um [[wiki/concepts/relacionamento-muitos-para-muitos|relacionamento N para N]] com [[wiki/concepts/chave-estrangeira|chaves estrangeiras]].
   - Um [[wiki/concepts/seed-de-banco-de-dados|seed]] com os seis itens de coleta e as imagens servidas por `express.static`.
   - Rotas `GET /items` (com `image_url` montada), `POST /points` numa [[wiki/concepts/database-transactions|transação]] (`trx.commit()`), `GET /points/:id` (com join nos itens) e `GET /points?city&uf&items` (`whereIn` + `distinct`).
   - Por fim, controllers (`index`, `show`, `create`) e [[wiki/concepts/cors]].

O episódio mais instrutivo é um bug ao vivo. O teste de "rollback" com o item 9 parece funcionar, mas o ponto só não foi salvo porque faltava o `trx.commit()`. Ver as tensões.

## Key Claims

### Rotas, recursos e métodos

- **Rota x recurso:** a rota é "o endereço completo da nossa requisição"; o recurso é "qual entidade estamos acessando do sistema". "A rota é muito semântica": `GET /users` lista, `POST /users` cria, `GET /users/5` busca o usuário 5. Entender isso é "mais do que 50% do backend". Ver [[wiki/concepts/recurso-rest]].
- **Métodos:**
  - GET "quando a gente quer buscar uma ou mais informações".
  - POST "quando a gente quer criar uma nova informação".
  - PUT "quando a gente quer atualizar uma informação existente".
  - DELETE "quando eu quero remover".
  - A mesma rota com métodos diferentes não tem problema. Ver [[wiki/concepts/metodos-http]].
- **O navegador só faz GET:** "toda vez que o navegador acessa uma rota, ele sempre utiliza uma requisição do tipo get [...] porque o navegador não sabe fazer outras requisições". Ver as tensões.
- **`return` antes do `response`:** para "forçar que [...] o processamento da requisição, ela pare aqui".

### Insomnia

- Serve para requisições "em todo tipo de rota": é "gratuito, ele é open source" e feito em JavaScript. Para sistemas de 32 bits, o Postman. Workspaces, "new request", duplicar requisição, aba de query e body em JSON. Ver [[wiki/entities/insomnia]].

### Tipos de parâmetros

- **Route params** (o ASR diz "request param"): `/users/:id`, lidos em `request.params.id`.
  - "Identificam um recurso"; "99% das vezes, esse parâmetro é obrigatório".
  - O nome é livre ("se aqui tivesse asd, aqui seria asd").
  - O valor chega como string, então `users[Number(id)]` resolve o "element implicitly has any type" do TypeScript.
  - O índice 4 "não vai existir e ele vai dar um errinho", e o tratamento de erros fica para depois.
- **Query params:** `?search=on`, lidos em `request.query.search`.
  - São "opcionais, para filtros, paginação", e "quem determina o nome do parâmetro é quem está fazendo a requisição".
  - Podem se repetir e virar array, por isso `String(search)` para "dar uma burlada no sistema do TypeScript". O filtro é `users.filter(user => user.includes(search))`, com ternário quando não há busca.
  - "Rob" não acha Robson: o filtro diferencia maiúsculas, e Diego deixa assim "porque é só didático". Ver [[wiki/concepts/query-string]].
- **Request body:** "parâmetros para criação e atualização de informações", em JSON no Insomnia, lidos em `request.body`. Vem vazio até `app.use(express.json())`, porque "o Express não vem, por padrão de fábrica, já entendendo essa linguagem JSON"; o `use` é "como se fosse [...] um plugin". Ver [[wiki/concepts/middleware]].
- **Regra de bolso** (repetida no filtro dos pontos): params para identificar, body para criar ou editar, query para filtro e paginação. Ver [[wiki/concepts/parametros-de-requisicao]].

### Banco: SQL, SQLite e Knex

- **SQL e não MongoDB:** SQL "é o mais tradicional que você vai encontrar no mercado". O MongoDB é "utilizado para aplicações muito específicas" e "um pouquinho mais difícil de se trabalhar". "Muita gente confunde [...] NoSQL como automaticamente sendo bancos mais rápidos", mas ele "pode ser menos performático se você tentar utilizar ele da forma errada". Ver [[wiki/concepts/relational-vs-nosql]].
- **SQLite** "porque [...] a gente não vai precisar instalar nada": o banco é "um arquivo físico mesmo", `database.sqlite`. Ver [[wiki/concepts/sqlite]].
- **[[wiki/entities/knex]]**, "a gente não pronuncia o K":
  - É um [[wiki/concepts/query-builder]] com "linguagem unificada" para Postgres, MSSQL, MySQL, MariaDB, SQLite3, Oracle e Redshift.
  - `knex('users').where('name', 'Diego').select('*')` equivale ao `SELECT * FROM users WHERE name = 'Diego'`.
  - As vantagens: continuar em JavaScript, com IntelliSense, e trocar "do SQLite para o Postgres [...] vai continuar funcionando da mesma forma". Ver as tensões.
  - Diego também diz "select tudo" pelo asterisco, desde que começou a programar.

### Rotas em arquivo próprio e conexão

- **`routes.ts` com `express.Router()`**, que "funciona da mesma forma que o meu app", exportado e montado com `app.use(routes)`. O `./` no import vale para arquivos do projeto; sem ele, o módulo vem do `node_modules`.
- **`src/database/connection.ts`:** `knex({ client: 'sqlite3', connection: { filename: path.resolve(__dirname, 'database.sqlite') } })`, com o pacote `sqlite3`.
  - O `path.resolve` serve porque "no Windows a barra é ao contrário".
  - O `__dirname` "sempre retorna o caminho para o diretório do arquivo que está executando ele".

### Entidades e relacionamento N para N

- **Mapear antes de codar:** "toda informação [...] que ela é mantida pela aplicação, ela vai virar uma tabela". Diego anota no Notion.
- **`points`:** `image`, `name`, `email`, `whatsapp`, `latitude`, `longitude`, `city`, `uf`. O número do endereço fica de fora porque, com "o ponto exatamente no mapa", "fica muito fácil a gente encontrar".
- **`items`:** `title` e `image`.
- **`point_items`:** um ponto coleta vários itens e um item é coletado por vários pontos, logo "muitos para muitos, ou N para N", que "gera uma tabela pivô" com `point_id` e `item_id`. O nome "derivado do nome das outras duas tabelas" deve ser "o mais semântico possível". Ver [[wiki/concepts/relacionamento-muitos-para-muitos]].

### Migrations

- **O que são:** "o histórico, o controle de versão do seu banco de dados". O caso de uso é a equipe: você cria `points`, um colega cria `users`, e "basta executar um comando" para os dois terem o mesmo banco, sem trocar SQL por mensagem. Ver [[wiki/concepts/database-migration]] e [[wiki/concepts/schema-migration]].
- **Arquivos manuais em ordem:** `00_create_points.ts`, `01_create_items.ts`, `02_create_point_items.ts`, porque `point_items` não pode ser criada antes das outras ("senão vai dar erro"). Dá para usar timestamp.
- **`up` e `down`:** o `up` faz a alteração; o `down` "sempre deve fazer exatamente o contrário" ("é um vai e um volta"): `createTable` x `dropTable`.
- **Tipos com TypeScript:** `import Knex from 'knex'` e `knex: Knex` destravam o autocomplete de `knex.schema.createTable`. "Os tipos do TypeScript, eles geralmente começam com letra maiúscula." Ver [[wiki/entities/typescript]].
- **Colunas:**
  - `increments('id').primary()` ([[wiki/concepts/chave-primaria]]).
  - `string('image').notNullable()`: a imagem fica "a referência, o nome do arquivo".
  - `decimal('latitude')`, `decimal('longitude')`, `string('uf', 2)`.
  - Em `point_items`, `integer('point_id').notNullable().references('id').inTable('points')`: "todo point_id [...] precisa ser um id válido dentro da tabela points". Ver [[wiki/concepts/chave-estrangeira]].
- **`knexfile.ts`** na raiz, com `module.exports` porque o Knex "ainda não suporta" `export default` ali ("eu sofri um monte com isso"). Leva o `client`, a `connection` e `migrations.directory`; roda com `npx knex migrate:latest --knexfile knexfile.ts` e depois como script `knex:migrate`.
- **Conferência:** pela extensão SQLite do VS Code (SQLite Explorer, "Show Table"). A tabela `knex_migrations` registra as migrations executadas; da `knex_migrations_lock`, "eu nem lembro pra que serve".
- **Erro de percurso:** as migrations vazias de `items` e `point_items` rodaram e ficaram registradas. A solução foi apagar o `database.sqlite` e rodar de novo.
- **`useNullAsDefault: true`**, no knexfile e na conexão, cala o aviso "SQLite does not support inserting default values".

### Funcionalidades e seeds

- **O que a API precisa** (Diego anota no Notion):
  - Web: cadastrar ponto e listar itens.
  - Mobile: listar pontos filtrados por UF, cidade e itens, e mostrar um ponto específico.
  - Sem update e delete, "como desafio".
- **Seeds:** os itens são "pré-estabelecidos pela nossa própria aplicação". Em `database/seeds/create_items.ts`, a função `seed(knex)` faz `await knex('items').insert([...])` com Lâmpadas, Pilhas e Baterias, Papéis e Papelão, Resíduos Eletrônicos, Resíduos Orgânicos e Óleo de Cozinha, cada um com o seu SVG. Roda com `knex seed:run` (script `knex:seed`). "Os seeds servem para a gente popular a nossa base de dados com alguns dados padrões." Ver [[wiki/concepts/seed-de-banco-de-dados]].

### Arquivos estáticos e listagem de itens

- **`app.use('/uploads', express.static(path.resolve(__dirname, '..', 'uploads')))`** serve "arquivos que vão precisar ser acessíveis de forma direta" (imagem, PDF, Word). No `path.resolve`, "eu não boto barra, eu boto vírgula sempre". Ver [[wiki/entities/express]].
- **`GET /items`:** `await knex('items').select('*')`, que obriga o `async` na rota.
- **Serialização:** um `map` devolve `{ id, title, image_url: \`http://localhost:3333/uploads/${item.image}\` }`, para o React "já ter acesso direto ao URL da imagem". "Esse processo [...] tem o nome de serialização [...] Eu transformo os dados para um novo formato."
- **ts-node-dev lento:** a flag certa é `--ignore-watch node_modules`, não `--ignore` ("eu fui num projeto antigo ver como é que era"). Ele também tenta `--transpile-only`.

### Cadastro de ponto de coleta e transactions

- **`POST /points`:** desestrutura `request.body` (name, email, whatsapp, latitude, longitude, city, uf, items) e faz `knex('points').insert({...})` com `image: 'image-fake'` por enquanto. Diego explica a desestruturação e a *shorthand syntax*.
- **Pivô:** `items.map((item_id: number) => ({ item_id, point_id }))` vai para `knex('point_items').insert(...)`. O `point_id` sai de `insertedIds[0]`, porque o insert "retorna os ids dos [...] registros que foram inseridos".
- **Teste no Insomnia:** Mercado Imperatriz, contato@imperatriz.com.br, Rio do Sul/SC ("a cidade aqui da Rocket"), itens `[1, 2, 6]`.
- **Transação:** "se der erro nessa segunda, eu quero que a primeira também não execute". `const trx = await knex.transaction()` troca `knex` por `trx`. O teste com o item 9 inexistente mostra o ponto ausente, e Diego conclui que "a transaction automaticamente fez um rollback". Ver [[wiki/concepts/database-transactions]] e as tensões.
- **O commit esquecido:** depois, o Mercado do Seu Zé não aparece na lista. "Logo que eu parei de gravar eu lembrei o que eu esqueci. Diego Cabeçudo." Faltava `await trx.commit()`: "se eu não boto esse commit aqui, ele nunca vai fazer esses inserts", e "caso falhe alguma coisa, a gente precisa dar o rollback".
- **Retorno:** `{ id: point_id, ...point }` com o spread operator.

### Controllers

- **Por quê:** o `routes.ts` "tá começando a ficar um pouco pesado demais", e o código é "desacoplado" em `src/controllers/PointsController.ts` e `ItemsController.ts`.
- **Classes** com `import { Request, Response } from 'express'`, porque fora do `routes.get` o TypeScript perde o tipo ("parameter request implicitly has an any type"). A rota instancia a classe com `new PointsController()` e passa `pointsController.create`.
- **Convenção de nomes:** `index` (listar), `show` (um registro), `create`, `update`, `delete`; há quem prefira `store` e `destroy`.
- **O resto fica para depois:** service pattern e "repository pattern, que a gente chama também de data mapper", mas "não fique tão preso agora" na estrutura. Ver [[wiki/concepts/repository-pattern]] e as tensões.

### Listar um ponto e listar pontos filtrados

- **`GET /points/:id` (`show`):**
  - `knex('points').where('id', id).first()`; o `first` evita o array.
  - Sem ponto, `response.status(400).json({ message: 'Point not found.' })`, porque o "status code com começo 4 quer dizer que aconteceu um erro, provavelmente por algum erro do usuário". Ver [[wiki/concepts/http-status-code]] e as tensões.
  - Os itens saem de `knex('items').join('point_items', 'items.id', '=', 'point_items.item_id').where('point_items.point_id', id).select('items.title')`.
  - "O desenvolvimento não é uma linha reta": a necessidade dos itens só aparece olhando o layout do mobile.
- **`GET /points` (`index`):**
  - Os filtros vêm do query, "porque quando a gente vai lidar com filtros, a gente sempre pega do query".
  - `items=1,2` vira array com `String(items).split(',').map(item => Number(item.trim()))`.
  - A consulta é `join('point_items', ...)`, `.whereIn('point_items.item_id', parsedItems)`, `.where('city', String(city))`, `.where('uf', String(uf))`, `.distinct()` e `.select('points.*')`.
  - "O query pode vir qualquer coisa. Sério". O `distinct` existe porque um ponto que coleta 1 e 2 apareceria duas vezes.
- **Resultado:** com 1 e 2, só o Imperatriz; com 6, Imperatriz e Seu Zé. Ver [[wiki/concepts/query-string]].

### CORS e imagem provisória

- **[[wiki/concepts/cors]]:** "define na nossa API quais endereços externos vão ter acesso para a nossa aplicação". O React roda em `localhost:3000`, e o React Native "não precisa, porque [...] não é uma aplicação web". Diego instala `cors` e `@types/cors -D` e usa `app.use(cors())` liberando tudo em desenvolvimento; em produção, entra "o domínio da nossa aplicação, do front-end".
- **Imagem fixa do Unsplash:** a URL é reduzida com `w=400` e `q=60`. Os pontos com `image-fake` são apagados com `DELETE FROM point_items` e `DELETE FROM points` pela extensão SQLite ("Run Query"). O upload fica para a parte avançada.
- **Fechamento:** "eu nunca tinha falado sobre seeds [...] sobre transaction [...] a gente nunca tinha usado TypeScript em nenhum evento da Rocketseat".

## Tensões e precisões

- **O teste de rollback não provou nada.**
  - O `trx.commit()` faltou durante toda a demonstração. Sem commit, *nenhum* ponto daquela transação seria gravado, com ou sem erro, e foi por isso que o terceiro registro "sumiu".
  - O item 9 provavelmente nem gerou erro: o SQLite vem com as chaves estrangeiras **desligadas** e só as verifica com `PRAGMA foreign_keys = ON` `[external]` (https://www.sqlite.org/foreignkeys.html#fk_enable). No Knex, isso vai no `pool.afterCreate`.
  - A transação também ficou aberta, segurando o arquivo do SQLite. É a explicação provável para a requisição seguinte demorar até o timeout ("ele demorou um montão").
  - A forma segura é a de callback, `await knex.transaction(async trx => { ... })`, que faz commit no sucesso e rollback em qualquer exceção `[external]` (https://knexjs.org/guide/transactions.html). Ver [[wiki/concepts/database-transactions]] e [[wiki/concepts/chave-estrangeira]].
- **"Trocar de banco e continuar funcionando" tem exceções.**
  - O `insertedIds[0]` só funciona no SQLite e no MySQL. No Postgres, o `insert` não devolve ids sem `.returning('id')`, que devolve objetos `[{ id }]` nas versões recentes `[external]` (https://knexjs.org/guide/query-builder.html#insert).
  - `decimal()` sem argumentos assume precisão 8 e escala 2 `[external]` (https://knexjs.org/guide/schema-builder.html#decimal). No SQLite não faz diferença, porque o tipo vira NUMERIC/REAL. No Postgres ou no MySQL, a latitude seria cortada em duas casas (cerca de 1 km). O certo é `decimal('latitude', 9, 6)` ou `double`.
  - O query builder abstrai a sintaxe, não o comportamento de cada banco. Ver [[wiki/concepts/query-builder]].
- **O navegador faz mais que GET.** A barra de endereço só faz GET, mas `<form method="post">` faz POST (como no [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|dia 5 de Mayk]]), e `fetch` ou `XMLHttpRequest` usam qualquer método. É assim que o front-end em React vai chamar o `POST /points`. Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/fetch-api]].
- **PUT não é "atualizar" em geral.** PUT substitui o recurso inteiro e é idempotente; a atualização parcial é PATCH `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH).
- **"Não encontrado" é 404, não 400.** 400 é requisição malformada; 404 é recurso inexistente `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404). Ver [[wiki/concepts/http-status-code]].
- **`String(x)` e `Number(x)` não validam nada.**
  - `String(['on', 'off'])` vira `"on,off"`, e `Number('abc')` vira `NaN`. Os dois só calam o TypeScript.
  - `Number(item.trim())` aceita `items=` e gera `[0]`.
  - Sem `city` ou `uf`, o filtro procura a cidade `"undefined"`.
  - `[skill: lang-dynamic]` O caminho é validar o `request.query` e o `request.body` com um schema (Zod, Valibot, ou o JSON Schema do Fastify) e responder 400 quando não bate. Ver [[wiki/concepts/validacao-de-entrada]].
- **O filtro de itens é "qualquer um", não "todos".** `whereIn` + `distinct` devolve pontos que coletam *pelo menos um* dos itens. Para "todos", é preciso `GROUP BY` com `HAVING COUNT(DISTINCT item_id) = n`.
- **A pivô sem chave composta aceita duplicatas.** `point_items` não tem `primary(['point_id', 'item_id'])` nem `unique`, então o mesmo par pode entrar duas vezes. Ver [[wiki/concepts/relacionamento-muitos-para-muitos]].
- **CORS não controla acesso à API.** É o navegador que aplica a regra, e só para a leitura da resposta em páginas de outra origem. Insomnia, curl, um servidor ou o app React Native chamam a API do mesmo jeito. Proteção de acesso é autenticação e autorização. Ver [[wiki/concepts/cors]] e [[wiki/concepts/same-origin-policy]].
- **O `knex_migrations_lock`** impede que dois processos rodem migrations ao mesmo tempo, como dois deploys simultâneos `[external]` (https://knexjs.org/guide/migrations.html). Migration já executada não se edita; cria-se outra ([[wiki/concepts/imutabilidade-de-migration]]). Apagar o `.db`, como na aula, só serve em desenvolvimento.
- **Repository não é Data Mapper.** No catálogo de Fowler, o Data Mapper move dados entre objetos e banco, e o Repository é uma camada acima, com interface de coleção para o domínio `[external]` (https://martinfowler.com/eaaCatalog/repository.html). Ver [[wiki/concepts/repository-pattern]] e [[wiki/concepts/orm]].
- **`http://localhost:3333` fixo no código** quebra em qualquer outro ambiente. A URL base vem de configuração. Ver [[wiki/concepts/variaveis-de-ambiente]].
- **Ferramentas de 2020.** `[skill: lang-dynamic]`
  - No Express 4, um erro dentro de handler `async` vira rejeição não tratada, e a requisição fica pendurada; o Express 5 repassa ao `next(err)`.
  - O Knex segue mantido, mas para TypeScript a skill aponta Kysely (query builder tipado), Drizzle ou Prisma. Ver [[wiki/concepts/drizzle-orm]].
  - O `ts-node-dev --ignore-watch` virou `tsx watch` ou `node --watch`.
  - O `sqlite3` pode dar lugar ao `better-sqlite3` ou ao `node:sqlite` nativo.
- **MongoDB "difícil" e "menos de mercado"** é opinião. A parte sobre desempenho está certa: NoSQL não é mais rápido por definição, depende do padrão de acesso. Ver [[wiki/concepts/relational-vs-nosql]].
- **O telefone de 250 dígitos.** A legenda repetiu o 9 centenas de vezes no WhatsApp do Mercado Imperatriz; no raw, o número ficou como veio.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento, Rio do Sul como "cidade aqui da Rocket"
- [[wiki/entities/express]]: Router, `express.json`, `express.static`
- [[wiki/entities/knex]]: query builder, migrations, seeds, transactions
- [[wiki/entities/insomnia]]: cliente HTTP para testar a API
- [[wiki/entities/typescript]]: tipos `Knex`, `Request`, `Response`; `Number` e `String` para calar o compilador
- [[wiki/entities/vs-code]]: extensão SQLite, `material-icon-theme.folders.associations`, Copy Line Down
- [[wiki/entities/unsplash]]: imagem provisória dos pontos

Citados sem página: Postman, Notion, MongoDB, CouchDB, Redis, Postgres, MySQL, SQL Server, MariaDB, Oracle, Amazon Redshift, pacote `cors`, `sqlite3`, `ts-node-dev`, Microsoft Edge.

## Conceitos

[[wiki/concepts/recurso-rest]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/parametros-de-requisicao]] · [[wiki/concepts/query-string]] · [[wiki/concepts/middleware]] · [[wiki/concepts/api-rest]] · [[wiki/concepts/json]] · [[wiki/concepts/relational-vs-nosql]] · [[wiki/concepts/sqlite]] · [[wiki/concepts/query-builder]] · [[wiki/concepts/orm]] · [[wiki/concepts/database-migration]] · [[wiki/concepts/schema-migration]] · [[wiki/concepts/imutabilidade-de-migration]] · [[wiki/concepts/seed-de-banco-de-dados]] · [[wiki/concepts/relacionamento-muitos-para-muitos]] · [[wiki/concepts/chave-primaria]] · [[wiki/concepts/chave-estrangeira]] · [[wiki/concepts/database-transactions]] · [[wiki/concepts/http-status-code]] · [[wiki/concepts/repository-pattern]] · [[wiki/concepts/cors]] · [[wiki/concepts/same-origin-policy]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/variaveis-de-ambiente]]

## Open Questions

- O upload de imagens (multer, provavelmente) e a validação ficaram para a parte de "funcionalidades um pouquinho mais avançada" (dia 5?).
- A aula não mostra se o projeto final liga `PRAGMA foreign_keys`.
- O dia 3 (React) consome `GET /items` e `POST /points` em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]. Os dias 3 (React) e 4 (React Native) devem consumir `GET /items`, `POST /points`, `GET /points` e `GET /points/:id`.
- Data provável: 2 de junho de 2020 `[external, não verificado]`.
