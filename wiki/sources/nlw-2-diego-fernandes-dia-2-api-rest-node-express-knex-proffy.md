---
type: source
title: "NLW #2 com Diego Fernandes, dia 2: API REST do Proffy com Node.js, TypeScript, Express e Knex"
aliases: ["NLW 2 Diego dia 2", "Proffy API", "Proffy back-end", "NLW 2 trilha React dia 2"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, typescript, express, knex, sqlite, api-rest, json, metodos-http, route-params, query-params, request-body, http-status-code, insomnia, migrations, chave-estrangeira, cascade, transactions, where-exists, subquery, join, controllers, cors, non-blocking-io, ts-node-dev, casos-de-uso, backend, tech-mentor-data, lang-dynamic, rocketseat, proffy, iniciante]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2 com Diego Fernandes, dia 2: API REST do Proffy com Node.js, TypeScript, Express e Knex

## TL;DR

Segunda aula (cerca de 2h22) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #2]]: a API do Proffy. A aula tem três partes:

1. **Conceitos.**
   - Front-end × back-end pela analogia do restaurante (do Mayk). O back-end guarda o que não pode ir para o cliente (credenciais do banco, SMTP, chave de hash; ver [[wiki/concepts/confiar-no-frontend]]).
   - Toda mensagem HTTP tem cabeçalho e corpo ([[wiki/concepts/requisicao-http]]).
   - "Full MVC", que devolve HTML pronto, contra [[wiki/concepts/api-rest]], que devolve [[wiki/concepts/json]] para web e mobile.
   - O [[wiki/entities/nodejs]] pelo [[wiki/concepts/non-blocking-io]], com menção a streams e worker threads.
2. **Infraestrutura.**
   - `yarn init -y`, [[wiki/entities/typescript]] com `tsc --init` (target ES2017) e `ts-node-dev` com `--transpile-only --ignore-watch node_modules --respawn`.
   - [[wiki/entities/express]], `@types/express`, `app.listen(3333)` e a primeira rota em `response.json`.
   - Rotas, [[wiki/concepts/recurso-rest|recursos]], [[wiki/concepts/metodos-http]] e o [[wiki/entities/insomnia]]. Os três [[wiki/concepts/parametros-de-requisicao|parâmetros]]: body, route params e query params.
   - Os casos de uso tirados do layout.
3. **O banco e as rotas.**
   - [[wiki/entities/knex]] ([[wiki/concepts/query-builder]]) + [[wiki/concepts/sqlite]], `knexfile.ts` e [[wiki/concepts/database-migration|migrations]] em TypeScript para `users`, `classes`, `class_schedule` e `connections`. As [[wiki/concepts/chave-estrangeira|FKs]] usam `CASCADE`, e os horários ficam em minutos.
   - `POST /classes` cria usuário, aula e horários numa [[wiki/concepts/database-transactions|transaction]] com `try/catch` e devolve 201 ou 400.
   - `ClassesController` e `ConnectionsController`.
   - `GET /classes?week_day&subject&time` usa join com `users` e `whereExists` com três `whereRaw` sobre `class_schedule`.
   - `POST`/`GET /connections` registra e conta os contatos.
   - Por fim, [[wiki/concepts/cors]].

## Key Claims

### Front-end, back-end e a mensagem HTTP

- **Divisão:** o front-end "é tudo aquilo que o usuário interage"; o back-end, "tudo aquilo que a gente não enxerga". Na analogia do restaurante (atribuída ao Mayk Brito), mesas e garçons são o front, a cozinha é o back.
- **Mensagem:** "toda mensagem enviada entre frontend para backend e backend para frontend, ela tem cabeçalho e corpo". O cabeçalho seria o que define se a mensagem "está querendo criar alguma coisa [...] uma lista [...] editar, deletar"; o corpo, "o real conteúdo". Ver [[wiki/concepts/requisicao-http]], [[wiki/concepts/http-headers]] e as tensões.
- **Por que no back-end:** salvar no banco exige as credenciais, enviar e-mail exige o SMTP, e o hash de senha exige "uma chave secreta". "Tudo que está no frontend, o usuário tem acesso." Ver [[wiki/concepts/confiar-no-frontend]] e [[wiki/concepts/password-hashing]].

### Full MVC × API REST

- **"Full MVC":** o back-end devolve "o HTML completo da página". O problema maior não é o peso da resposta ("a internet está cada vez mais rápida"), e sim que "o único dispositivo na Terra capaz de entender HTML é o navegador". Kotlin, Swift, React Native e Flutter exigiriam "uma gambiarra danada".
- **API REST:** o back-end, "não interessa se ele é feito com Node, com Ruby, com PHP", devolve "apenas os dados" em JSON, e "é o front-end que determina como que a interface vai ser construída". REST × RESTful fica para um vídeo do Mayk: "não se prenda aos termos". Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/json]].
- **JSON:** "um objeto escrito da mesma forma que a gente escreve no JavaScript", lista como array de objetos, e "todas as linguagens [...] conseguem entender".

### Por que Node.js

- **O mesmo JavaScript** do front e do mobile no back-end; o Node é plataforma, "a gente não pode falar que é linguagem". O Deno aparece como "o irmão do Node".
- **Non-blocking I/O:** em Ruby e PHP, "a próxima linha nunca executa antes da linha anterior ser finalizada". No Node é possível "salvar o usuário no banco de dados, enviar um e-mail e criptografar a senha do usuário tudo ao mesmo tempo". Go, Elixir e PHP recente também têm. Ver [[wiki/concepts/non-blocking-io]] e as tensões.
- **Para estudar:** streams ("ler um arquivo de texto linha por linha") e worker threads ("trabalhar com todos os cores da CPU").

### Projeto, TypeScript e ts-node-dev

- **Estrutura do zero,** sem boilerplate: `server/`, `src/server.ts`. No Windows, PowerShell em vez do Command Prompt.
- **`tsc --init`** e `"target": "ES2017"`, "as funcionalidades que o Node entende" (Node 12.18 LTS). O TypeScript converte o resto "como se o Node fosse um browser". Para o IE8, seria ES3. Ver [[wiki/concepts/transpilador]].
- **`ts-node-dev`** (script `start`: `tsnd --transpile-only --ignore-watch node_modules --respawn src/server.ts`):
  - O `--transpile-only` só converte, "não vai verificar se tem erros", para acelerar.
  - O `--ignore-watch` deixa o `node_modules` de fora, por ser "códigos de terceiros".
  - O `--respawn` reinicia a cada alteração.
- **Dev dependencies:** TypeScript, ts-node-dev e os `@types/*` "não vão ser utilizados em produção". Ver [[wiki/concepts/package-json]] e [[wiki/concepts/arquivo-de-declaracao-de-tipos]].

### Express e a primeira rota

- **Express** é "micro framework": traz "poucas funcionalidades só para [...] dar um start". O erro do import some com `@types/express`, porque alguns pacotes "não vêm com as informações que o TypeScript precisa". Ver [[wiki/entities/express]].
- **`app.listen(3333)`:** "quando nós não temos a porta, quer dizer que a porta é 80", e no desenvolvimento se usa outra porta porque haverá "várias aplicações rodando". Ver [[wiki/concepts/porta-de-rede]] e as tensões.
- **`app.get('/users', (request, response) => ...)`:** sem resposta, o navegador fica esperando (o log aparece a cada F5). Depois vêm `response.send('Hello World')` e `response.json(users)`. A extensão JSON Viewer formata a saída.

### Rotas, recursos, métodos e parâmetros

- **Rota** é "o endereço da nossa aplicação"; **recurso** é "o que vem [...] depois [...] dessa URL base" (`users`, `contacts`). Ver [[wiki/concepts/recurso-rest]].
- **Métodos:** GET busca ou lista, POST cria, PUT atualiza, DELETE apaga. O navegador "sempre" faz GET, daí o [[wiki/entities/insomnia]] (workspace "NLW02"). O mesmo recurso com métodos diferentes são rotas diferentes. Recursos ficam no plural: "padrão é padrão". Ver [[wiki/concepts/metodos-http]].
- **Os três parâmetros** ([[wiki/concepts/parametros-de-requisicao]]):
  - O **body**, para criar ou atualizar, chega `undefined` até `app.use(express.json())`.
  - Os **route params** (`/users/:id`, `request.params`) servem "para identificar [o] recurso" a atualizar ou deletar.
  - Os **query params** (`request.query`) servem para paginação, filtro e ordenação ([[wiki/concepts/query-string]]).

### Casos de uso

- **"Identificar os casos de uso"** pelo layout, num `readme.md`. Ficaram quatro: rota para listar o total de conexões ("Total de 285 conexões"), criar uma aula, listar aulas filtradas por matéria, dia da semana e horário, e criar uma conexão ao clicar em "entrar em contato".
- **Fora do back-end:** o WhatsApp abre direto, e os favoritos do mobile ficam no "storage do celular", porque "a gente não vai ter autenticação nessa aplicação ainda".
- **A conexão** é só uma tentativa: "a gente não vai saber realmente se houve a conexão [...] a gente sempre inicia aí com o MVP".

### Knex, SQLite e migrations

- **Banco relacional,** porque é o que "tu vai estar utilizando [...] nas empresas". SQLite "porque você não precisa instalar nada", e o código "vai funcionar também" em Postgres ou MySQL (ver as tensões). Ver [[wiki/concepts/sqlite]] e [[wiki/concepts/relational-vs-nosql]].
- **Knex** é um query builder: em vez de `SELECT * FROM users`, `knex('users').select('*')`, com "developer experience melhor". Ver [[wiki/entities/knex]] e [[wiki/concepts/query-builder]].
- **`database/connection.ts`:** `knex({ client: 'sqlite3', connection: { filename: path.resolve(__dirname, 'database.sqlite') }, useNullAsDefault: true })`. O `path.resolve` evita as barras diferentes entre Windows e Unix, e o `useNullAsDefault` diz ao SQLite o que gravar quando o campo não vem.
- **Por que migrations:** copiar o banco entre colegas falha quando dois mexem no esquema ao mesmo tempo, e as migrations são "a mesma coisa que o Git faz [...] no código dentro do banco de dados". O Knex compara a pasta com a tabela `knex_migrations` e "vai executar só as migrations que ainda não foram executadas". Ver [[wiki/concepts/database-migration]].
- **`knexfile.ts`** com `module.exports` ("não pode ser com export default, porque senão o Knex não entende"), script `knex:migrate` (`knex --knexfile knexfile.ts migrate:latest`) e a sugestão de um `knex:migrate:rollback`.
- **Migrations à mão, em TypeScript,** numeradas (`00_`, `01_`...), porque "a ordem dos arquivos aqui é bem importante": uma tabela que depende de outra vem depois. Cada arquivo exporta `async function up(knex: Knex)` e `down`; o down é "se deu merda, o que eu faço pra voltar". "Eu jamais vou decorar isso aqui [...] eu olho na documentação."
- **Erro no esquema antes de compartilhar:** "deleta o SQLite inteiro", ajusta e roda de novo. Ver [[wiki/concepts/imutabilidade-de-migration]].

### As quatro tabelas

- **`users`:** `increments('id').primary()`, e `name`, `avatar`, `whatsapp` e `bio` como `string().notNullable()`. Ficam separados das aulas porque "se depois a gente for implementar login [...] é bom que os usuários estejam numa tabela só". Ver [[wiki/concepts/chave-primaria]].
- **`classes`:** `subject` em string ("não vou fazer um relacionamento por enquanto"), `cost` em `decimal` e `user_id` com `.references('id').inTable('users').onUpdate('CASCADE').onDelete('CASCADE')`. Diego usa CASCADE "praticamente 99,9% das vezes". Ver [[wiki/concepts/chave-estrangeira]].
- **`class_schedule`:** `week_day` (0 = domingo, 6 = sábado), `from` e `to` em inteiro, e `class_id` → `classes`.
- **`connections`:** `user_id` → `users` e `timestamp('created_at').defaultTo(...)`.
- **Horário em minutos:** "na grande maioria [dos bancos] não existe um campo do tipo time", então 8:00 vira 480 (depois de um "6 vezes 8, 48" corrigido no ar). O `convertHourToMinutes(time)` faz `time.split(':').map(Number)`, `[hour, minutes]` e `hour * 60 + minutes`.

### POST /classes

- **`routes.ts` com `express.Router()`,** montado com `app.use(routes)`. "Não pense isso aqui como o que eu vou criar no banco de dados. É o que eu vou criar como entidade": a rota é `POST /classes`, mesmo criando três registros.
- **Corpo:** `name`, `avatar`, `whatsapp`, `bio`, `subject`, `cost` e `schedule: [{ week_day, from: '8:00', to: '12:00' }, ...]`. Uma vírgula sobrando no fim é erro em JSON.
- **Inserts:**
  - Desestruturação e *shorthand syntax* ([[wiki/concepts/desestruturacao-javascript]]).
  - `await db('users').insert({...})` devolve um array de ids, e `user_id = insertedUsersIds[0]` "porque eu só estou inserindo um". O mesmo vale para `class_id`.
  - `schedule.map((scheduleItem: ScheduleItem) => ({ class_id, week_day, from: convertHourToMinutes(...), to: ... }))` vai num insert só.
  - A `interface ScheduleItem` resolve o "implicitly has an any type", porque o `any` "é muito aberto".
  - Ver [[wiki/concepts/async-await]].
- **Duplicação percebida:** o segundo envio cria outro Diego, "até porque eu não pedi e-mail, ou CPF".
- **Transaction:** `const trx = await db.transaction()`, `trx` nos três inserts, `await trx.commit()` no fim e `await trx.rollback()` no `catch`, "que é basicamente fazer todas as operações do banco ao mesmo tempo, e se uma delas falhar, desfazer". Ver [[wiki/concepts/database-transactions]].
- **Respostas:** `status(201).send()` ("criado com sucesso") e, no `catch`, `status(400).json({ error: 'Unexpected error while creating new class' })` com a mensagem vaga de propósito. Ver [[wiki/concepts/http-status-code]] e [[wiki/concepts/error-handling-estruturado]].

### Controllers

- **`ClassesController`** com `create` e `index` ("dentro do padrão MVC [...] a gente chama o método de index"). O `Request` e o `Response` precisam vir do Express, porque fora do `routes.post` a tipagem "perde a referência".
- **Abstração deliberadamente curta:** "o controller na verdade ele não deveria ter a responsabilidade de fazer as inserções no banco", mas "não tem porque a gente ficar também otimizando de forma prematura [...] sendo que a aplicação nem tem vida ainda". Ver [[wiki/concepts/otimizacao-prematura]].

### GET /classes com filtros

- **Sem `week_day`, `subject` ou `time`:** `400` com `error: 'Missing filters to search classes'`.
- **`as string`:** `filters.time as string`, que "vai meio que dizer pro TypeScript que isso aqui eu tenho certeza que é uma string". Diego diz que "não quer dizer que é a melhor".
- **A query:**

```ts
const classes = await db('classes')
  .whereExists(function () {
    this.select('class_schedule.*')
      .from('class_schedule')
      .whereRaw('`class_schedule`.`class_id` = `classes`.`id`')
      .whereRaw('`class_schedule`.`week_day` = ??', [Number(week_day)])
      .whereRaw('`class_schedule`.`from` <= ??', [timeInMinutes])
      .whereRaw('`class_schedule`.`to` > ??', [timeInMinutes])
  })
  .where('classes.subject', '=', subject)
  .join('users', 'classes.user_id', '=', 'users.id')
  .select(['classes.*', 'users.*'])
```

  - `function` em vez de arrow, porque esta "não cria um novo escopo" e o `this` some.
  - Crase em tabela e coluna, e `??` para parâmetro.
  - O `from <=` garante que o professor já começou; o `to >` é estrito porque "se eu paro de trabalhar às 12 horas, as pessoas podem marcar horário comigo somente antes das 12".
  - O primeiro erro, "no such column matemática", vinha de um `week_day` que recebia `subject`.
  - O join é um "inner join", e trazer o usuário serve porque a listagem precisa de nome e foto.
  - Ver [[wiki/concepts/sql-injection]] e as tensões.

### Conexões e CORS

- **`POST /connections`** faz `db('connections').insert({ user_id })` e devolve `201`. O `GET /connections` faz `db('connections').count('* as total')` e lê `totalConnections[0]`, porque o Knex "sempre é múltipla" mesmo com uma linha só.
- **`defaultTo('now')` não funciona no SQLite**, que grava o texto. `'CURRENT_TIMESTAMP'` como string também falha, e a solução de uma issue foi `knex.raw('CURRENT_TIMESTAMP')`. Cada correção exigiu apagar o banco e migrar de novo. "Programação é isso. Tem que errar até acertar."
- **`cors`** permite que o front em `localhost:3000` acesse a API em `localhost:3333`, porque "por padrão, ele permite apenas que aplicações no mesmo endereço" acessem. Leva `app.use(cors())` e `@types/cors -D`. Ver [[wiki/concepts/cors]].
- **Fechamento:** "foi a primeira NLW que a gente fez uma query no banco mais complexa".

## Tensões e precisões

- **`select('classes.*', 'users.*')` sobrescreve o `id`.** As duas tabelas têm `id`, e no objeto devolvido o último vence: o `id` da aula vira o do usuário. O front que usar `id` para a aula pega o professor. O correto é dar alias, como `select('classes.*', 'users.name', 'users.avatar', ...)` ou `users.id as user_id`.
- **`whereRaw` com `??` é parametrização de identificador, não de valor.** No Knex, `??` é binding de identificador (tabela ou coluna) e `?` é de valor `[external]` (https://knexjs.org/guide/raw.html#raw-parameter-binding). Com `??`, `[540]` vira um identificador entre crases, e no SQLite um identificador que não existe como coluna pode cair em literal de string (o *quirk* de aspas duplas/crases), o que só funciona por acaso `[external, não verificado nesta sessão]`. O certo seria `?`. Mesmo assim, ninguém interpola entrada no SQL, ao contrário do [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy|dia 5 do Mayk]], que interpolava `req.query`. Ver [[wiki/concepts/sql-injection]] e [[wiki/concepts/query-builder]].
- **CASCADE que não roda.** O SQLite deixa as chaves estrangeiras desligadas até `PRAGMA foreign_keys = ON` `[external]` (https://www.sqlite.org/foreignkeys.html#fk_enable). Sem isso no `pool.afterCreate`, `onDelete('CASCADE')` e `references` não fazem nada, e um `user_id` inexistente em `/connections` é aceito. É a mesma lacuna registrada no [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta|dia 2 da NLW #1]]. Ver [[wiki/concepts/chave-estrangeira]].
- **400 para "erro inesperado".** 4xx é erro do cliente; uma falha do servidor ao gravar é 500. O 400 cabe na falta de filtros, e o 201 poderia levar `Location` `[skill: tech-mentor-backend]`. Ver [[wiki/concepts/http-status-code]].
- **Async sem `try/catch` no Express 4.** O `index` de classes e as rotas de conexões não têm `try/catch`. No Express 4, uma promise rejeitada num handler `async` não chega ao middleware de erro: a requisição fica pendurada, e o processo registra *unhandled rejection*. O Express 5 encaminha a rejeição sozinho `[external]` (https://expressjs.com/en/guide/error-handling.html). Ver [[wiki/concepts/error-handling-estruturado]].
- **A transaction manual** está correta (commit e rollback), mas a forma de callback, `db.transaction(async trx => ...)`, não deixa esquecer nenhum dos dois. Ver [[wiki/concepts/database-transactions]].
- **"Na grande maioria não existe um campo do tipo time"** vale para SQLite e Oracle. Postgres, MySQL e SQL Server têm `TIME`. Minutos inteiros continuam sendo uma escolha simples e boa para intervalos dentro de um dia (comparação barata, sem fuso), mas não cobrem aula que cruza a meia-noite nem fuso horário do professor. A conversão de Diego (`map(Number)`) está certa; a do [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy|dia 5 do Mayk]] concatenava texto.
- **`decimal` no SQLite** é só afinidade numérica: o valor é guardado como inteiro ou float, com os arredondamentos do float. Para dinheiro, centavos em inteiro são mais seguros `[skill: tech-mentor-backend]`.
- **"Funciona também em Postgres ou MySQL" com ressalvas.** O `insert` só devolve ids no SQLite e no MySQL (o Postgres pede `.returning('id')`), crases são do MySQL/SQLite (o Postgres usa aspas duplas), e o `CURRENT_TIMESTAMP` em raw é portável, mas `knex.fn.now()` é a forma idiomática `[external]` (https://knexjs.org/guide/schema-builder.html#timestamp).
- **`as string` mente para o compilador.** `request.query` pode trazer array (`?subject=a&subject=b`) ou objeto aninhado. O cast esconde isso, e a validação deveria checar o tipo em tempo de execução (Zod ou equivalente). Também não há validação no `POST /classes`: `cost` negativo, `week_day` 9 ou `from > to` passam. Ver [[wiki/concepts/validacao-de-entrada]].
- **O método não está no cabeçalho.** Criar, listar ou apagar vem do método na linha de requisição (`POST /classes HTTP/1.1`). Os cabeçalhos levam metadados como `Content-Type`, `Authorization` e `Accept`. Ver [[wiki/concepts/http-headers]] e [[wiki/concepts/requisicao-http]].
- **REST não é "devolver JSON".** REST é um estilo arquitetural (Fielding, 2000) com recursos, representações, interface uniforme e ausência de estado. Uma resposta HTML pode ser REST, e um JSON por RPC não é. A comparação útil da aula é "servidor renderiza × cliente renderiza". Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **Porta 80 é a do HTTP.** Sites em HTTPS usam 443 por padrão. É a mesma imprecisão do [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|dia 4 do Mayk]]. Ver [[wiki/concepts/porta-de-rede]].
- **Non-blocking I/O não paraleliza hashing.** Banco e e-mail esperam I/O, e o loop atende outras requisições enquanto isso. Hash de senha é CPU: o `bcrypt` assíncrono só não trava o loop porque roda no [[wiki/concepts/thread-pool|thread pool]] da libuv, e um hash em JavaScript puro bloquearia. "A próxima linha nunca executa antes" também vale para o Node: o que muda é que a operação de I/O devolve o controle e o resultado chega por callback ou promise. Ver [[wiki/concepts/non-blocking-io]] e [[wiki/sources/jstack-como-funciona-o-nodejs]].
- **CORS é do navegador.** O servidor não bloqueia a requisição: o navegador aplica a same-origin policy e só entrega a resposta ao JavaScript se os cabeçalhos `Access-Control-Allow-*` permitirem. Insomnia, curl e o app React Native não passam por isso. `cors()` sem opções libera qualquer origem (`*`), o que em produção deve virar uma lista de origens. Ver [[wiki/concepts/cors]] e [[wiki/concepts/cors-misconfiguration]].
- **`--transpile-only` sem checagem em outro lugar** deixa o erro de tipo chegar à produção. O padrão é um `tsc --noEmit` no CI ou no pre-commit `[skill: tech-mentor-backend]`.
- **"Apaga o banco e migra de novo"** só vale antes de a migration sair da máquina. Depois, a correção é uma migration nova. Ver [[wiki/concepts/imutabilidade-de-migration]].
- **Positivos:** casos de uso derivados do layout, separar `users` de `classes` pensando em login, `whereExists` em vez de join com `class_schedule` (que duplicaria linhas por horário), `to` exclusivo, `interface` em vez de `any` e transaction no cadastro composto.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/nodejs]]: plataforma
- [[wiki/entities/typescript]]: tsconfig, interfaces, `@types`
- [[wiki/entities/express]]: servidor, Router, `express.json`
- [[wiki/entities/knex]]: query builder, migrations, transaction, `whereExists`/`whereRaw`
- [[wiki/entities/insomnia]]: cliente HTTP
- [[wiki/entities/vs-code]]: extensão SQLite (SQLite Explorer), auto import, Material Icon Theme
- [[wiki/entities/mayk-brito]]: dono da analogia do restaurante e do vídeo sobre REST × RESTful
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: Whimsical, Notion, Deno, ts-node-dev, sqlite3 (driver), JSON Viewer, Vivaldi, phpMyAdmin, PowerShell, Go, Elixir, Kotlin, Swift, Flutter, MongoDB, Postgres, MySQL, Vini e Dani (nomes de exemplo).

## Conceitos

[[wiki/concepts/api-rest]] · [[wiki/concepts/recurso-rest]] · [[wiki/concepts/json]] · [[wiki/concepts/requisicao-http]] · [[wiki/concepts/http-headers]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/http-status-code]] · [[wiki/concepts/parametros-de-requisicao]] · [[wiki/concepts/query-string]] · [[wiki/concepts/porta-de-rede]] · [[wiki/concepts/cors]] · [[wiki/concepts/cors-misconfiguration]] · [[wiki/concepts/confiar-no-frontend]] · [[wiki/concepts/password-hashing]] · [[wiki/concepts/non-blocking-io]] · [[wiki/concepts/thread-pool]] · [[wiki/concepts/transpilador]] · [[wiki/concepts/package-json]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/query-builder]] · [[wiki/concepts/sqlite]] · [[wiki/concepts/relational-vs-nosql]] · [[wiki/concepts/database-migration]] · [[wiki/concepts/imutabilidade-de-migration]] · [[wiki/concepts/chave-primaria]] · [[wiki/concepts/chave-estrangeira]] · [[wiki/concepts/database-transactions]] · [[wiki/concepts/sql-injection]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/error-handling-estruturado]] · [[wiki/concepts/async-await]] · [[wiki/concepts/desestruturacao-javascript]] · [[wiki/concepts/otimizacao-prematura]] · [[wiki/concepts/renderizacao-ssr-vs-csr]]

## Open Questions

- O front do [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy|dia 1]] consome esta API em [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]] (cadastro com estado, listagem com filtros, contador de conexões).
- O `??` do `whereRaw` funcionou na gravação: vale confirmar se é o *quirk* de identificador do SQLite ou se o Knex trata o caso. Até lá, a recomendação é `?`.
- A NLW #1 e a NLW #2 do Diego usam a mesma pilha (Express + Knex + SQLite). Uma comparação das duas, e das duas trilhas da NLW #2, fica como questão aberta.
- Data provável: 4 de agosto de 2020 `[external, não verificado]`.
