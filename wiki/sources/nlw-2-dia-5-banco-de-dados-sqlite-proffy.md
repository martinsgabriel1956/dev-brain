---
type: source
title: "NLW #2, dia 5: banco de dados do Proffy com SQLite"
aliases: ["NLW 2 dia 5", "Next Level Week 2 dia 5", "Proffy SQLite", "Proffy banco de dados"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [banco-de-dados, sqlite, sql, create-table, insert, select, join, exists, chave-primaria, chave-estrangeira, normalizacao, promise, async-await, promise-all, try-catch, desestruturacao, nodejs, express, nunjucks, post, req-body, sql-injection, tech-mentor-backend, lang-dynamic, rocketseat, proffy, iniciante]
skill: tech-mentor-data
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-dia-5-banco-de-dados-sqlite-proffy.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2, dia 5: banco de dados do Proffy com SQLite

## TL;DR

Última aula (cerca de 2h47) da [[wiki/entities/next-level-week|NLW #2]] da [[wiki/entities/rocketseat]], com [[wiki/entities/mayk-brito]]. O Proffy do [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|dia 4]] guardava os professores num array que sumia a cada reinício ([[wiki/concepts/dados-em-memoria-vs-persistencia]]); agora eles vão para um arquivo [[wiki/concepts/sqlite|SQLite]]. A aula tem cinco partes:

1. **Por que um banco e o que é SQL.** Dados fora da aplicação, tabelas como planilhas, SQLite porque "reside na própria aplicação".
2. **O esquema em `src/database/db.js`.** O pacote `sqlite-async`, `Database.open(__dirname + "/database.sqlite").then(execute)` e três tabelas criadas com `CREATE TABLE IF NOT EXISTS`: `proffys`, `classes` e `class_schedule`, ligadas por `proffy_id` e `class_id`. A divisão evita repetir os dados do professor em cada aula e horário ([[wiki/concepts/normalizacao-de-dados]]).
3. **Inserir e consultar num arquivo de teste.**
   - `createProffy.js` exporta uma função `async` que faz `await db.run(INSERT ...)` e usa o `lastID` de cada inserção no próximo passo ([[wiki/concepts/async-await]]).
   - Os horários viram um array de `db.run` com `map` e são esperados com `Promise.all`.
   - As consultas são `SELECT * FROM proffys`, um `JOIN` entre classes e proffys e o filtro de horário: `time_from <= x AND time_to > x`, com o tempo guardado "em minutos".
4. **Integração com o servidor.**
   - Refatoração: os dados fake vão para `fake-data.js`, as listas para `utils/format.js` e as rotas para `pages.js`.
   - A página de estudo só consulta o banco se os três filtros vierem preenchidos. A consulta usa `WHERE EXISTS (SELECT ... FROM class_schedule ...)`, e a hora passa por `convertHoursToMinutes`.
   - Lista vazia mostra "Nenhum professor encontrado com a sua pesquisa".
5. **Cadastro por POST.** O formulário passa a `method="post"` para `/save-classes`, com `express.urlencoded({ extended: true })` e `req.body`. Os valores são montados (`proffyValue`, `classValue`, `classScheduleValues` com `map` e `index`), gravados com `createProffy` dentro de `try/catch` e redirecionados para `/study` já filtrado pela primeira aula cadastrada.

Fecha com ajustes de CSS da landing, três desafios (página de sucesso com `setTimeout`, apagar ou impedir campos de horário vazios, a versão 2.0 do layout) e o aviso de que não haverá turma do Launchbase.

Toda a SQL da aula é montada por interpolação de template string, e isso abre [[wiki/concepts/sql-injection|SQL injection]] no cadastro e na busca. A conversão de horas tem um bug de concatenação de strings. Os dois estão em "Tensões e precisões".

## Key Claims

### Por que um banco de dados

- **Os dados fora da aplicação.** "Os dados não fazem parte, eles não devem ficar na aplicação." Se ficam no código, um dev "desavisado" pode sobrescrever ou apagar, e "a gente tem uma segurança falha ou fraca". É a mesma abertura do [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|dia 5 da NLW #1]].
- **Senha "criptografada".** Mesmo criptografada, a lista de usuários fica acessível "de uma maneira muito fácil". Criptografada é "uma senha que você não tem um acesso fácil", e você "precisa fazer uma lógica para poder desvendar". Ver as tensões e [[wiki/concepts/password-hashing]].
- **Responsabilidades.** A aplicação faz a [[wiki/concepts/regra-de-negocio|regra de negócio]], "como eu falei ontem"; o banco "é o cara que vai ser responsável em guardar os dados".
- **SQL.** "Structured Query Language", "uma linguagem estruturada de busca, de consulta". "Ele não é uma linguagem de programação": serve para criar, consultar, atualizar e deletar dados.
- **Tabelas.** Os dados ficam em tabelas, que ele também chama de "entidades ou de relações", como uma planilha do Excel, com colunas e linhas.
- **Por que SQLite.** É open source, fácil de configurar e "vai residir na própria aplicação, ele guarda no arquivo específico da aplicação". Para quem vai seguir na área, "tem outras tecnologias mais avançadas". Ver [[wiki/concepts/sqlite]].

### db.js: abrir o banco

- **Instalação:** `npm install sqlite-async`. O arquivo é `src/database/db.js`, com `const Database = require("sqlite-async")`.
- **Abrir:** `Database.open(__dirname + "/database.sqlite")`. Na primeira vez o arquivo não existe, e o SQLite o cria.
- **Por que `then`:** abrir leva "milissegundos, eu não sei quanto tempo". Como o JavaScript executa "linha a linha, sem parar", um `console.log` logo abaixo roda antes de o banco terminar de abrir. O `.then(execute)` registra uma função que roda depois e recebe o objeto `db`. A função é passada pelo nome, sem ser chamada. Ver [[wiki/concepts/promise-javascript]] e [[wiki/concepts/callback-javascript]].
- **Testando:** `node src/database/db.js` imprime "Cheguei aqui" e cria o `database.sqlite`. O `console.log(db)` mostra um objeto com `filename`, `mode` e métodos como `exec`.

### CREATE TABLE: três tabelas

- **`db.exec` com crases.** Dentro de uma template string vão as instruções SQL, que rodam "todas as vezes que eu chamar esse arquivo DB".
- **`CREATE TABLE IF NOT EXISTS proffys`:**
  - `id INTEGER PRIMARY KEY AUTOINCREMENT`, mais `name`, `avatar`, `whatsapp` e `bio` como `TEXT`.
  - O `id` é "o identificador de cada professor": "se eu tenho o prof 1 de id 1, eu não posso ter outro prof com id 1". O `AUTOINCREMENT` deixa o banco gerar o id, e assim ele "nunca vai se repetir". Ver [[wiki/concepts/chave-primaria]].
  - "O último [campo] não leva vírgula. Senão a gente vai ter problemas."
- **`classes`:** `id`, `subject`, `cost` e `proffy_id INTEGER`. Um professor "pode estar relacionado a quantas classes ele quiser"; cada aula "está sempre referenciando, esse é o nome que a gente usa", um professor. Ver [[wiki/concepts/chave-estrangeira]].
- **`class_schedule`:** `id`, `class_id`, `weekday`, `time_from` e `time_to`, todos `INTEGER`. Uma aula de Química pode ser na segunda ao meio-dia e na quinta às 3 da manhã.
- **Erros de sintaxe SQL.** "Errou sintaxe aqui, dificilmente a gente vai conseguir achar os erros", mesmo com print no Discord: o banco "dá uma sugestão", mas "não fala exatamente onde tá o erro". Ver [[wiki/concepts/debugging]].

### Por que separar em tabelas

- **A pergunta:** "por que eu não cadastro tudo numa tabela só?"
- **A resposta:** com tudo junto, nome, avatar, WhatsApp e biografia se repetiriam em cada aula e em cada horário, "mais de 10, 20, 30 vezes". Para "atualizar o nome do professor só", seria preciso atualizar tudo.
- **Banco relacional.** "SQL é um tipo de banco de dados chamado de banco de dados relacional, porque ele consegue relacionar uma tabela com a outra." As relações não são obrigatórias. O caminho de consulta é professor → aula → agenda, "imagina que você tá escrevendo isso numa agenda". Ver [[wiki/concepts/normalizacao-de-dados]], [[wiki/concepts/modelagem-de-dados]] e [[wiki/concepts/relational-vs-nosql]].
- **Conferindo:** a extensão SQLite do VS Code abre o arquivo ("Open Database") e mostra as três tabelas e suas colunas no SQLite Explorer.

### module.exports e o arquivo de teste

- **Exportar a promessa.** `module.exports = Database.open(...).then(execute)`. O `execute` faz `return db`, e "esse return [...] vai fazer com que essa função retorne para esse then". O `test.js` faz `const Database = require("./db")` e continua com outro `.then(async (db) => { ... })`. O `db` que importa é o que o `then` passa, "não pego esse aqui que está aqui fora".
- **`require` é o mesmo mecanismo** que o `server.js` já usa: "o Node é danado, ele manja das coisas aqui". O `.js` no fim é opcional.

### Organizando os dados

- **Três objetos para três tabelas:**
  - `proffyValue`: name, avatar, whatsapp e bio. Ele reaproveita os dados do Diego Fernandes que estavam no `server.js`.
  - `classValue`: subject e cost. Não pode se chamar `class`, porque "class é uma palavra reservada do JavaScript". O `proffy_id` "virá pelo banco de dados".
  - `classScheduleValues`: um array de objetos com `weekday`, `time_from` e `time_to`, porque "a gente pode ter mais de um".
- **Os números:** `weekday` "começa do 0" (domingo). Os horários ficam "em formato numérico, em minutos" para facilitar a consulta, por exemplo `time_from: 720`.
- **Por que organizar:** "não dá pra pegar o formulário, jogar tudo de uma vez no banco sem o banco entender aonde que tem que guardar cada dado".

### createProffy.js: promessas, await e async

- **A assinatura:** `module.exports = async function (db, { proffyValue, classValue, classScheduleValues })`. Os nomes têm de ser os mesmos na chamada; a ordem "não importa", porque "se for o mesmo nome, ele sabe identificar". Ver [[wiki/concepts/desestruturacao-javascript]].
- **"A palavra do momento chama-se espera."** Cada inserção demora, e as aulas só podem entrar com o id do professor. O `db.run` devolve uma promessa: "eu vou tentar. Se eu conseguir, então eu vou fazer o restante". "Pode ser que não dê certo."
- **`await`:** "aguarde uma promessa". Com ele, "essa linha aqui, ela vai aguardar antes de ir para a próxima linha", o que dispensa o `then`. Encadear `then` dentro de `then` vira "uma bagunça"; o `await` é "muito mais elegante".
- **`async`:** "não consigo [usar o await] se essa função não tiver na frente dela uma palavra chamada async". Ver [[wiki/concepts/async-await]].

### INSERT INTO e o lastID

- **O comando:** `INSERT INTO proffys (name, avatar, whatsapp, bio) VALUES ("${proffyValue.name}", ...)`, numa template string ("template literals"), que deixa quebrar linha e pôr variável com `${}`. Aspas simples não quebram linha: "o próprio programa tá falando, cara, tem erro aí".
- **O id gerado:** `const insertedProffy = await db.run(...)` e `const proffy_id = insertedProffy.lastID`, "o último id inserido".
- **A aula:** `INSERT INTO classes (subject, cost, proffy_id)` com `classValue.subject`, `classValue.cost` e o `proffy_id`; de novo se guarda o `lastID` como `class_id`.

### Os horários: map e Promise.all

- **Quantos horários?** "Vai saber quantos ele vai colocar aqui, eu nunca vou saber." Por isso uma estrutura de repetição.
- **`map` x `forEach`:** os dois passam "elemento por elemento" para uma função. O `map` usa o retorno de cada chamada para montar "um novo array". Ver [[wiki/concepts/array]].
- **O array de promessas:** cada volta retorna `db.run(INSERT INTO class_schedule ...)` sem `await`, porque "eu não quero rodar ele agora. Eu quero guardar ele no array para executar depois".
- **`await Promise.all(insertedAllClassScheduleValues)`:** "ele vai um por um, a promessa de todos, ele vai pegar um primeiro, aí ele vai aguardar, vai pegar o outro". As duas explicações estão erradas: ver as tensões.
- **A ajuda do editor:** o VS Code deixa cinza uma variável não usada, e foi assim que ele achou o `insertedClass` trocado por `insertedProffy`. "A gente precisa das ferramentas para nos ajudar."

### Rodando o teste e lendo os erros

- **Primeiro erro:** `SQLITE_ERROR: near "Fernandes": syntax error`. O nome entrou sem aspas no `VALUES`, e ele corrige com aspas duplas em volta de cada `${}` (usa múltiplos cursores com Alt+clique).
- **Segundo erro:** uma vírgula depois do último campo do `class_schedule`.
- **Lição:** "erros fazem parte da nossa vida [...] pra sempre", "o seu trabalho é resolver erros". Os testes com erro deixaram Diegos repetidos nas tabelas, e ele apaga o `database.sqlite` para recomeçar.
- **Mostrar o código:** com o editor dividido, para quem quiser pausar e copiar. Ele conta que tirava prints das aulas do GoStack e guardava no Notion.

### SELECT, JOIN e WHERE

- **Tudo:** `await db.all("SELECT * FROM proffys")`. O `*` "significa tudo", e "tudo" são as colunas. O resultado vem "como um array", mesmo com um só registro.
- **Aulas com o professor:** `SELECT classes.*, proffys.* FROM proffys JOIN classes ON (classes.proffy_id = proffys.id) WHERE classes.proffy_id = 1`. "União em inglês chama-se join"; "pode pegar o j de juntar". O primeiro erro, "no such column", vinha de escrever `proffy.id` em vez de `proffys.id`: "identificar, entender, resolver".

### Filtrando por dia e horário

- **O problema.** Encontrar professores de Química aos domingos às 8 da manhã com um único horário digitado no filtro.
- **A regra:** quem dá aula das 8 às 18 aparece para quem procura às 10. Não aparece para 7 nem para 20, e também não para 18, porque ele não começaria uma aula às 18. Então `time_from` tem que ser menor ou igual ao horário pedido, e `time_to` tem que ser maior. "Eu mesmo não entendi muito de primeira."
- **A consulta:** `SELECT class_schedule.* FROM class_schedule WHERE class_schedule.class_id = "1" AND class_schedule.weekday = "0" AND class_schedule.time_from <= "520" AND class_schedule.time_to > "520"`. Ele testa os limites: 420 e 1300 dão resultado vazio. "Comendo o elefante de parte em parte".
- **`subject` vira `INTEGER`**, porque a matéria será guardada como número, como na lista do servidor ("vou guardar no banco de dados depois via número"). Ver a tensão sobre `IF NOT EXISTS`.

### Refatoração

- **O que sai do `server.js`:**
  - os dados fake vão para `database/fake-data.js`, "só para você ter mais tarde";
  - `subjects`, `weekdays` e `getSubject` vão para `utils/format.js`, exportados num objeto;
  - as funções de página vão para `pages.js`: `pageLanding`, `pageStudy`, `pageGiveClasses` e depois `saveClasses`.
- **Desestruturação:** `const { subjects, weekdays, getSubject } = require("./utils/format")`. Os nomes "tem que ser exato os mesmos". Ver [[wiki/concepts/desestruturacao-javascript]] e [[wiki/concepts/refatoracao]].
- **Ritmo.** "Eu tô indo bem devagar porque eu tive um feedback aí do pessoal que disse que eu tava meio rápido nessa refatoração."
- **O erro esperado.** "proffys is not defined" na página de estudo, porque os professores saíram do arquivo.

### A busca da página de estudo

- **Só com filtros.** `if (!filters.subject || !filters.weekday || !filters.time)` renderiza a página sem professores. "Se um deles está vazio, ele só vai mostrar a página." O campo de busca se chama `time`, não `time_from` nem `time_to`, que são "para cadastrar no banco de dados".
- **A consulta.** O `JOIN` anterior ganha um `WHERE EXISTS (SELECT class_schedule.* ... WHERE class_schedule.class_id = classes.id AND ...)`, uma "sub-busca": se ela não achar nada, "não tem nem porque ele trazer nada". Os valores fixos viram `${filters.weekday}` e `${timeToMinutes}`, e `classes.subject = '${filters.subject}'` fecha a consulta.

### Horas em minutos, try/catch e o render

- **Por que minutos.** Com "09:00" não dá para fazer a matemática de maior e menor: "eu não consigo usar matemática num número que tem dois pontos no meio".
- **`convertHoursToMinutes(time)` em `utils/format.js`:**
  - `time.split(":")` separa "hora de um lado, minutos de outro", testado no console do navegador.
  - `const [hour, minutes] = ...` é a desestruturação de array, mais limpa do que `time.split(":")[0]`.
  - O retorno é `Number((hour * 60) + minutes)`, que "vai me retornar isso aqui formatado em formato de número, pra não ser strings". Ver a tensão sobre o bug.
- **`try/catch`.** "Você vai tentar o código daqui de dentro. Se der algum erro aqui dentro, você vai capturar." O `catch` faz `console.log(error)`. Ver [[wiki/concepts/error-handling-estruturado]].
- **No banco.** `const db = await Database` espera a abertura e a criação das tabelas. `const proffys = await db.all(query)` busca os professores, e `res.render("study.html", { proffys, filters, subjects, weekdays })` mostra a página. A função de página vira `async`.
- **O primeiro erro.** `filter is not defined`, um erro de digitação.

### Nenhum professor encontrado

- **Estado vazio.** O Figma tem um estado vazio, e ele o implementa com `{% if proffys == "" %} <p class="no-results">Nenhum professor encontrado com a sua pesquisa.</p> {% else %} {% for ... %} {% endif %}`. "A pesquisa deu certo, mas não tem nenhum professor nesse dia e hora." Ver [[wiki/entities/nunjucks]].
- **O CSS:** `max-width` em `rem`, margem automática e `text-align: center`, conferido no mobile ([[wiki/concepts/mobile-first]]).

### POST, req.body e save-classes

- **Os dados saem da URL.** Antes o cadastro chegava por `req.query`, e a URL "ficava gigante"; agora vem em `req.body`, "uma escondida nesses dados".
- **Configuração:** `server.use(express.urlencoded({ extended: true }))`, porque "por padrão, o meu Express [...] não vai aceitar esses dados".
- **O formulário:** `method="post"` e `action="/save-classes"`. A rota nova é `server.post("/save-classes", saveClasses)`, porque não existia rota POST para o `give-classes`.
- **Verbos HTTP.**
  - "Post sempre vai querer significar [...] eu vou entrar num lugar que eu vou criar um conteúdo pra você."
  - "Eu não conseguiria acessar a rota POST por aqui [pela barra]", "mas o formulário consegue acessar essa rota escondida, entre aspas".
  - Ver [[wiki/concepts/metodos-http]] e as tensões.
- **O erro de rota.** "Cannot POST /save-classes": ele tinha escrito `save-class` no servidor. Ele corrige e reenvia o formulário com Ctrl+R.

### Salvando e redirecionando

- **Montar os valores:** `proffyValue` sai de `req.body.name`, `avatar`, `whatsapp` e `bio`; `classValue` sai de `subject` e `cost`.
- **Os horários:** `req.body.weekday.map((weekday, index) => ({ weekday, time_from: convertHoursToMinutes(req.body.time_from[index]), time_to: convertHoursToMinutes(req.body.time_to[index]) }))`. "Múltiplos campos [...] vêm no formato de lista"; o segundo argumento do `map` "é a posição do array".
- **Gravar:** `const db = await Database` e `await createProffy(db, { proffyValue, classValue, classScheduleValues })`, dentro de `try/catch`: "toda vez que eu entrar num await da vida, [...] try catch faz muito sentido".
- **Redirecionar filtrado:** `let queryString = "?subject=" + req.body.subject` e `queryString += "&weekday=" + req.body.weekday[0] + "&time=" + req.body.time_from[0]`, para "visualmente ele ver que o cadastro dele está no nosso sistema". O fim é `res.redirect("/study" + queryString)`. Ver [[wiki/concepts/post-redirect-get]] e [[wiki/concepts/query-string]].
- **A matéria.** O `subject` volta do banco como número, e `proffys.map((proffy) => { proffy.subject = getSubject(proffy.subject) })` o troca pelo nome. Um espaço solto na query dá "SQLITE_ERROR"; ele deixa o erro no vídeo "para que você veja que esses erros são comuns".
- **Teste.** Clayton Souza, Educação Física, R$ 67, quinta, das 12 às 15. Aparece na quinta e não na quarta. Às 15 não acha, às 14:59 acha.

### Desafios e encerramento

- **Ajustes:** a media query da landing passa de 699 para 1100 px e a imagem hero vai para `10rem`: "a gente vai muito no feeling".
- **Desafio 1, página de sucesso** (versão 2.0 do Figma): mostrar "cadastro salvo", esperar dois segundos com `setTimeout` e redirecionar com `location.href`, de preferência já com o filtro.
- **Desafio 2, correção de bugs.** Um campo de horário extra vazio, que é `required`, bloqueia o envio. A saída é um botão de remover ("como remover um elemento HTML com o JavaScript") ou não clonar se o último campo estiver vazio. Ele pede também uma lista própria de bugs e o layout avançado.
- **"Não fique triste se você não conseguir."** "Já fique muito feliz e celebre porque você terminou a semana", a trilha Discovery.
- **Sem Launchbase desta vez:** "estamos preparando uma tonelada de mudanças e melhorias". Ele anuncia uma "novidade incrível [...] totalmente de graça" sem dar detalhes e marca um encontro ao vivo no domingo.

## Tensões e precisões

- **Toda a SQL da aula é injetável.**
  - **Onde:** o `INSERT` coloca `"${proffyValue.name}"`, `bio`, `avatar` etc. direto na string. Os valores vêm de `req.body`. A busca faz o mesmo com `filters.subject`, `filters.weekday` e o horário vindos de `req.query`.
  - **O efeito:** uma biografia com aspas duplas já quebra o cadastro (`near "...": syntax error`), que é o mesmo erro que Mayk viu com "Diego Fernandes". Um texto montado de propósito muda o comando. Na busca, um `subject` como `1' OR '1'='1` traz todos os professores.
  - **A comparação:** pior que a [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|NLW #1]], cujo `INSERT` usava placeholders `?`.
  - **A correção:** `db.run("INSERT INTO proffys (name, avatar, whatsapp, bio) VALUES (?, ?, ?, ?)", [name, avatar, whatsapp, bio])` e o mesmo com a busca. Ver [[wiki/concepts/sql-injection]] e [[wiki/concepts/validacao-de-entrada]] `[external]` (https://owasp.org/www-community/attacks/SQL_Injection).
- **Aspas duplas não são texto em SQL.** No SQL padrão, `"..."` é nome de coluna ou tabela, e texto vai entre aspas simples, como a própria aula faz em `classes.subject = '...'`. O SQLite aceita aspas duplas como texto por compatibilidade, quando não acha uma coluna com aquele nome. A documentação chama isso de *misfeature* e recomenda não depender dela `[external]` (https://www.sqlite.org/quirks.html#double_quoted_string_literals_are_accepted).
- **`convertHoursToMinutes` concatena em vez de somar.**
  - **O bug:** `hour * 60` converte a string em número, mas `540 + "00"` vira a string `"54000"`, e o `Number` só transforma isso em 54000. "09:30" vira 54030, e não 570.
  - **Por que a aula não percebe:** cadastro e busca passam pela mesma função, e como os minutos têm dois dígitos a ordem é preservada. O filtro continua certo, mas o banco não guarda minutos, ao contrário do que a aula diz, e mistura escalas com os 720 e 1220 do teste.
  - **A correção:** `Number(hour) * 60 + Number(minutes)`. Ver [[wiki/concepts/tipos-primitivos-javascript]] e [[wiki/concepts/string]] `[skill: lang-dynamic]`.
- **`Promise.all` não executa nem espera "um por um".**
  - **O que acontece:** uma promise começa a trabalhar quando é criada. Os `db.run` do `map` já disparam ali, não são "guardados para executar depois".
  - **O que o `Promise.all` faz:** espera todas ao mesmo tempo e rejeita na primeira falha.
  - **Por que a ordem dá certo:** quem enfileira as escritas é o SQLite, que aceita uma por vez.
  - **Para executar em sequência:** usar `for...of` com `await` dentro. Ver [[wiki/concepts/async-await]] `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all).
- **Sem transação, o cadastro pode ficar pela metade.** Se a inserção dos horários falhar, o professor e a aula já foram gravados. Os testes com erro da própria aula deixaram "outros Diego Fernandes" nas tabelas. `BEGIN`/`COMMIT` (ou `ROLLBACK` no `catch`) faz as três tabelas entrarem juntas ou nenhuma. Ver [[wiki/concepts/database-transactions]] e [[wiki/concepts/acid]] `[skill: tech-mentor-data]`.
- **A relação é só convenção.**
  - `proffy_id INTEGER` e `class_id INTEGER` não têm `REFERENCES`. "A classe só cadastra no banco de dados se eu tiver um professor" não é garantido por nada.
  - Mesmo com `REFERENCES`, o SQLite só valida chaves estrangeiras com `PRAGMA foreign_keys = ON` em cada conexão.
  - Ver [[wiki/concepts/chave-estrangeira]] `[skill: tech-mentor-data]` `[external]` (https://www.sqlite.org/foreignkeys.html).
- **`IF NOT EXISTS` não altera tabela.** Trocar `subject TEXT` por `INTEGER` no `CREATE TABLE` não muda um `database.sqlite` que já existe; a tabela velha continua como estava. Só deu certo porque o arquivo tinha sido apagado, ou porque o SQLite compara `'1'` e `1` pela afinidade de tipo. Mudança de esquema em banco com dados pede migration. Ver [[wiki/concepts/database-migration]] e [[wiki/concepts/schema-migration]].
- **O erro no `catch` deixa o usuário esperando.**
  - Em `pageStudy` e `saveClasses`, o `catch` só faz `console.log`. A requisição nunca recebe resposta, e o navegador fica carregando.
  - A NLW #1 respondia "Erro no cadastro"; aqui caberia `res.status(500).send(...)` ou uma página de erro.
  - Ver [[wiki/concepts/error-handling-estruturado]].
- **POST "escondido", de novo.**
  - O corpo aparece no DevTools e trafega em texto puro sem HTTPS, e não só formulário acessa POST: `curl`, `fetch` e qualquer cliente HTTP também acessam.
  - A vantagem real é que os dados saem da URL, do histórico e dos logs.
  - Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/http-vs-https]].
- **Nenhuma validação no servidor.** `req.body` entra como chegou. Um `weekday` que não é array, como o de alguém que manda o POST fora do formulário, faz o `map` lançar erro, e o servidor não responde. É o mesmo problema do [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|dia 4]]: a regra de negócio é anunciada para o back-end, mas não é aplicada. Ver [[wiki/concepts/confiar-no-frontend]].
- **Senha se guarda com hash, não criptografada.** Criptografia é reversível com a chave. Senha deve passar por um hash lento e com sal (bcrypt, scrypt, Argon2), que não se "desvenda", só se compara. Ver [[wiki/concepts/password-hashing]] e [[wiki/concepts/criptografia]].
- **O banco está dentro da aplicação.** O argumento de abertura ("dentro da aplicação [...] segurança fraca") convive com um `database.sqlite` em `src/database/`, ao lado do código. Sem um `.gitignore`, ele vai para o repositório. O que protege o arquivo é a permissão de acesso a ele, não o fato de ser banco.
- **"Relacional porque relaciona tabelas."** Na teoria, "relação" é a própria tabela, como Mayk diz antes ("entidades ou relações"). O nome não vem de ligar uma tabela à outra `[external]` (https://en.wikipedia.org/wiki/Relational_model). A NLW #1 tem a mesma confusão.
- **"SQL não é linguagem de programação."** É uma linguagem declarativa: você diz o que quer, não como buscar. Com CTEs recursivas, o SQL padrão é Turing-completo. A frase serve para iniciante, mas é imprecisa.
- **"Não consigo usar await sem async."** Isso valia para CommonJS, como o código da aula. Em módulos ES, o `await` no topo do arquivo é suportado desde o Node 14.8 `[external]` (https://nodejs.org/api/esm.html#top-level-await).
- **`proffys == ""` funciona pelo `==`.** Um array vazio convertido em string é `""`, e por isso a comparação dá verdadeiro. É a mesma coerção do [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|dia 4]]. O `{% for %}...{% else %}` do Nunjucks trata lista vazia sem truque. Ver [[wiki/concepts/igualdade-javascript]].
- **O filtro olha só o começo da aula.** `time_from <= x AND time_to > x` aceita uma aula às 14:59 com quem sai às 15:00. A consulta não sabe a duração da aula, e a interface não diz isso.
- **O `map` que troca a matéria** muda os objetos e não usa o array devolvido; ali cabia um `forEach`. A própria aula tinha acabado de explicar a diferença.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento, a trilha Discovery e o Launchbase (sem turma desta vez)
- [[wiki/entities/express]]: `server.post`, `express.urlencoded`, `req.body`, `res.redirect`
- [[wiki/entities/nunjucks]]: `if/else` com `for` para o estado vazio
- [[wiki/entities/nodejs]]: `require`, `module.exports`, `__dirname`
- [[wiki/entities/vs-code]]: extensão SQLite, aviso de variável não usada, múltiplos cursores
- [[wiki/entities/diego-fernandes]]: dados de exemplo do primeiro professor; professor do GoStack
- [[wiki/entities/figma]]: estado vazio e versão 2.0 do layout
- [[wiki/entities/github]]: avatar do Mayk usado como imagem

Citados sem página: pacote `sqlite-async`, SQLite Explorer, Excel, Discord, Notion, GoStack, Launchbase, Clayton Souza (professor de teste).

## Conceitos

[[wiki/concepts/sqlite]] · [[wiki/concepts/normalizacao-de-dados]] · [[wiki/concepts/modelagem-de-dados]] · [[wiki/concepts/relational-vs-nosql]] · [[wiki/concepts/chave-primaria]] · [[wiki/concepts/chave-estrangeira]] · [[wiki/concepts/sql-alem-do-basico]] · [[wiki/concepts/sql-injection]] · [[wiki/concepts/database-transactions]] · [[wiki/concepts/database-migration]] · [[wiki/concepts/async-await]] · [[wiki/concepts/promise-javascript]] · [[wiki/concepts/callback-javascript]] · [[wiki/concepts/desestruturacao-javascript]] · [[wiki/concepts/array]] · [[wiki/concepts/tipos-primitivos-javascript]] · [[wiki/concepts/error-handling-estruturado]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/post-redirect-get]] · [[wiki/concepts/query-string]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/confiar-no-frontend]] · [[wiki/concepts/password-hashing]] · [[wiki/concepts/dados-em-memoria-vs-persistencia]] · [[wiki/concepts/regra-de-negocio]] · [[wiki/concepts/refatoracao]] · [[wiki/concepts/igualdade-javascript]] · [[wiki/concepts/debugging]]

## Open Questions

- O Proffy termina sem edição, exclusão, login e deploy. A "novidade de graça" anunciada no fim fica sem nome.
- A data provável é agosto de 2020, o quinto dia da NLW #2 `[external, não verificado]`.
- As tabelas e variáveis aparecem na transcrição como "profi", "profis" e "profits". O vocabulário da aula ("Proffy", a tabela "com S") indica `proffys`/`proffyValue`/`createProffy`, e é essa a grafia desta página. Os trechos em que a legenda deu "prof"/"profs"/`createProf` ficaram literais no raw.
- A mesma semana teve outra trilha (Diego Fernandes: API com Knex, React, React Native). Comparação em [[wiki/questions/nlw-2-duas-trilhas-proffy-comparacao]].
- Comparação das duas aulas de banco de dados (NLW #1 com `sqlite3` e callbacks; NLW #2 com `sqlite-async` e `await`) ainda sem página em `questions/`.

## Raw quotes

- "Os dados não fazem parte, eles não devem ficar na aplicação."
- "A palavra do momento chama-se espera."
- "Eu não consigo usar matemática num número que tem dois pontos no meio."
- "O seu trabalho é resolver erros."
- "Não fique triste se você não conseguir."
