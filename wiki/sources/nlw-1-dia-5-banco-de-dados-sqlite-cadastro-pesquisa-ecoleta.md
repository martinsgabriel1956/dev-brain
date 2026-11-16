---
type: source
title: "NLW #1, dia 5: banco de dados SQLite, cadastro e pesquisa no Ecoleta"
aliases: ["NLW 1 dia 5", "Next Level Week 1 dia 5", "Ecoleta SQLite", "Ecoleta banco de dados"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [banco-de-dados, sqlite, sql, crud, chave-primaria, callback, nodejs, express, nunjucks, post, query-string, req-body, like, sql-injection, lang-dynamic, backend, rocketseat, ecoleta, iniciante]
skill: tech-mentor-data
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1, dia 5: banco de dados SQLite, cadastro e pesquisa no Ecoleta

## TL;DR

Última aula (cerca de 2h02) da [[wiki/entities/next-level-week|Next Level Week #1]] da [[wiki/entities/rocketseat]], com [[wiki/entities/mayk-brito]]. Depois do servidor do [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta|dia 4]], o Ecoleta ganha um banco de dados e fica completo de ponta a ponta. A aula tem quatro partes:

1. **Por que um banco.** Dados no código ou no HTML se perdem e ficam expostos; "guardar esses dados, persistir [...] é responsabilidade do banco de dados".
2. **O CRUD no `src/database/db.js`.**
   - SQL, tabelas e uma explicação de relacionamento (clientes e estados).
   - O [[wiki/concepts/sqlite|SQLite]] pelo pacote `sqlite3`, com `new sqlite3.Database("./src/database/database.db")` e `db.serialize`.
   - `CREATE TABLE IF NOT EXISTS places` com `id INTEGER PRIMARY KEY AUTOINCREMENT` ([[wiki/concepts/chave-primaria]]).
   - `INSERT` com placeholders `?` e um array de valores.
   - `SELECT` com `db.all`.
   - `DELETE ... WHERE id = ?`.
   - [[wiki/concepts/callback-javascript|Callbacks]], `this` e por que não usar arrow function aqui.
3. **Integração com o servidor.**
   - `module.exports = db` e `require("./database/db")` no `server.js`.
   - A rota `/search` lista os pontos com `{% for %}` e `{% if total > 0 %}` no [[wiki/entities/nunjucks]].
   - O formulário de cadastro primeiro manda os dados por GET, como [[wiki/concepts/query-string|query strings]] lidas em `req.query`. Depois passa a `method="post"` para `/savepoint`, com `express.urlencoded({ extended: true })` e `req.body`.
   - O cadastro termina num modal "Cadastro concluído" que redireciona para a home com `setTimeout`, ou num "Erro no cadastro".
4. **Pesquisa por cidade.** A busca vazia mostra "Nenhum local encontrado"; a busca usa `WHERE city LIKE '%${search}%'`, o que abre uma [[wiki/concepts/sql-injection|SQL injection]] (ver a seção de tensões).

Fecha com um ajuste do fundo (`position: absolute`, `16rem`), o convite para o encontro ao vivo e a venda do Launchbase (oito semanas, R$ 960, 30 dias de garantia).

## Key Claims

### Abertura: a milha extra

- **Para se destacar:**
  - ler a documentação das ferramentas da semana;
  - compartilhar o que aprende no LinkedIn;
  - organizar as redes "para que eles possam ser mais profissionais";
  - participar de comunidades e ajudar outros devs;
  - criar projetos pessoais.

### Por que um banco de dados

- **Dados fora da aplicação.** "Os dados não deveriam, não devem ficar na aplicação", porque "a gente pode perder ou corromper esses dados". Uma senha no HTML ou no JavaScript fica aberta a qualquer um; "tem que ter uma segurança a mais".
- **Responsabilidades:** a aplicação organiza e apresenta os dados; "guardar esses dados, persistir [...] é responsabilidade do banco de dados".
- **SQL** é a "Structured Query Language": "uma linguagem que não é bem de programação", usada para criar, consultar, atualizar e deletar dados. Ver [[wiki/concepts/sql-alem-do-basico]].
- **Tabelas, entidades, relações:** os dados ficam em tabelas, como no Excel, com colunas e linhas (rows). "Todos esses nomes significam as mesmas coisas"; o SQL é relacional "porque ele faz relações". Ver as tensões e [[wiki/concepts/relational-vs-nosql]].
- **O exemplo do relacionamento:**
  - Dois mil clientes de São Paulo não precisam repetir "São Paulo".
  - Cada cliente guarda o número do estado (1), e a tabela `estados` diz que 1 é São Paulo.
  - Trocar o estado do cliente é trocar um número.
  - O Ecoleta não usa isso "nessa semana", mas "você um dia vai lidar como desenvolvedor com um banco de dados com 5, 10, 15, 20, 30 tabelas".
- **Por que SQLite:**
  - É open source, "muito facinho de configurar" e "reside na própria aplicação", num arquivo.
  - Mayk aponta dois pontos fracos: a segurança ("você não faz um login e senha pra entrar no banco de dados") e "alguns conflitos".
  - Mesmo assim, "para quem está começando, ele é excelente". Ver [[wiki/concepts/sqlite]].

### db.js: criar o banco

- **Instalação:** `npm install sqlite3`, com "um monte de warnings": "Warnings são só mensagens de alerta".
- **Conexão:**
  - `const sqlite3 = require("sqlite3").verbose()`: o `verbose` faz o pacote dar "mais informações" no terminal.
  - De passagem: "função, quando [...] ela reside dentro de um objeto a gente dá o nome método".
- **`new`:** `const db = new sqlite3.Database("./src/database/database.db")` cria o objeto que "irá fazer operações no banco de dados". O `new` funciona com "um constructor ou uma classe".
- **Teste isolado:** `node src/database/db.js` cria o arquivo `database.db`, "com essas duas linhas". O `.gitignore` que aparece no projeto é configuração do Git do próprio Mayk.

### O CRUD

- **`db.serialize(function () { ... })`** "vai rodar uma sequência de código", em ordem. O plano fica em comentários:
  1. criar a tabela;
  2. inserir;
  3. consultar;
  4. deletar, este "de quebra", porque o Ecoleta não terá exclusão.
- **CREATE TABLE.** `db.run` com uma template string (crases), que permite quebrar linha.
  - O comando é `CREATE TABLE IF NOT EXISTS places (...)` (places = "locais"). Se a tabela já existe, não faz nada.
  - Colunas: `id INTEGER PRIMARY KEY AUTOINCREMENT`, mais `image`, `name`, `address`, `address2`, `state`, `city` e `items` em `TEXT`. Ele esquece o `name` e volta para corrigir.
  - "O último carinha aqui não tem vírgula"; "o SQL é muito bom de dar erro de sintaxe" e não diz bem onde.
- **Por que um id:**
  - Buscar pelo nome falha se dois locais tiverem o mesmo nome.
  - A chave primária é "o campo principal que essa tabela aqui vai usar para identificar". O `AUTOINCREMENT` começa em 1 e não reaproveita números apagados: depois de deletar o 5, o próximo é o 6, e a listagem mostra "1, 2, 3, 4, 6".
  - Ver [[wiki/concepts/chave-primaria]].
- **INSERT.** `INSERT INTO places (image, name, address, address2, state, city, items) VALUES (?,?,?,?,?,?,?);` deixa as interrogações para serem trocadas "de uma maneira dinâmica" por um array `values`. Os primeiros dados são a Colectoria (Rio do Sul, SC) com imagem do [[wiki/entities/unsplash]]. A query e os valores ficam em constantes "para que fique mais visual".
- **Callback.** O terceiro argumento do `run` é uma função "do estilo callback", "chame de volta":
  - **O que caracteriza:** é passada como parâmetro e chamada "depois de um certo tempo". "A sua aplicação não pode ficar travada 10 segundos esperando isso cadastrar no banco".
  - **Analogia da loja de roupas:** você pede uma cor ao vendedor e continua olhando outras roupas até ele voltar do depósito.
  - **Erro:** a função recebe `err`, e se houver erro faz `return console.log(err)`.
  - **Passagem por referência:** a função vira `afterInsertData`, passada sem `()`, porque "se eu coloco assim [com parênteses], eu já estou imediatamente executando ela".
  - Ver [[wiki/concepts/callback-javascript]].
- **`this` e arrow function:** dentro do callback, `this` é o resultado do `run` (um `Statement` com `lastID` e `changes`). "Quando você tem a palavra-chave [...] this, nós não usamos a arrow function", por "uma lógica muito grande por trás disso" que fica para um vídeo do canal. Ver [[wiki/concepts/funcoes-javascript]].
- **SELECT.** `db.all("SELECT * FROM places", function (err, rows) {...})`:
  - `*` é "todos os campos".
  - `rows` vem "no formato de Array" mesmo com um registro só.
  - `SELECT name` traz só a coluna nome.
  - O VS Code deixa opacos os trechos comentados e avisa "is declared, but its value is never read".
- **DELETE.** `db.run("DELETE FROM places WHERE id = ?", [1], ...)`. "Se eu rodasse só isso aqui [sem o WHERE], ele ia deletar tudo da tabela". No SQL, `=` compara, e não é o `==` do JavaScript. Depois de apagar, o novo registro vem com id 2. A Papersider entra como id 3.

### Banco no servidor

- **`module.exports = db`** no `db.js` e `const db = require("./database/db")` no `server.js`, com ou sem `.js`. O nome da constante é livre, porque "ele está exportando um objeto". Sempre que há `require`, "o Express está usando o módulo export em algum lugar".
- **Listar.** Na rota `/search`, `db.all("SELECT * FROM places", ...)` chama `res.render("search-results.html", { places: rows })` dentro do callback. Fora dele, `rows` não existe: "essa função nem foi chamada ainda".
- **`{% for place in places %}`** repete o card e usa `place.image`, `place.name`, `place.items`, `place.city`, `place.state`, `place.address` e `place.address2`. O `{{ places }}` cru mostra `[object Object]`. A analogia é uma caixa `places` de onde sai um `place` por vez. Ver [[wiki/entities/nunjucks]] e [[wiki/concepts/array]].
- **`const total = rows.length`**, enviado com a forma curta `{ places: rows, total }` e exibido como `{{ total }}` pontos encontrados.
- **`{% if total > 0 %} ... {% else %}`** mostra "Nenhum local encontrado", testado apagando os registros.

### Do formulário ao banco

- **GET e query strings:** o envio padrão do formulário monta `/create-point?name=...&image=...&uf=15&state=Pará&city=...&items=...`. "O nome disso aqui é query strings", e o servidor as lê em `req.query`. O valor de cada campo vem do atributo `name` de cada input. Ver [[wiki/concepts/query-string]] e [[wiki/concepts/formulario-html]].
- **Itens por nome:** os `data-id` dos itens passam de 1–6 aos nomes ("Lâmpadas", "Pilhas e Baterias"...). Antes de confiar, ele rastreia os dados com `console.log("item id", itemId)`. "O console.log no front-end [aparece] aqui [no DevTools]" e "no back-end [...] aqui no terminal". O "Preserve log" do DevTools mantém o log depois do reload. Ver [[wiki/concepts/debugging]].
- **"Choque de realidade":** "não é assim que a gente faz, que a gente envia formulários pela internet". O POST "envia os dados de uma maneira um pouco mais escondida". Ver [[wiki/concepts/metodos-http]] e as tensões.
- **A rota POST:**
  - `server.post("/savepoint", (req, res) => ...)`. Mayk explica que a mesma rota poderia ter GET e POST, mas usa `/savepoint` "para a gente treinar mais".
  - Digitar `/savepoint` na barra dá "Cannot GET", porque "sempre que a gente digitar, só será o verbo get".
  - O form ganha `method="post"` e `action="/savepoint"`.
- **`req.body`:** com POST, `req.query` vem vazio e `req.body` vem `undefined`, porque o Express não lê o corpo "por padrão". A linha `server.use(express.urlencoded({ extended: true }))` "habilita o uso do req.body".
- **Salvar:**
  - Os `values` passam a ser `req.body.image`, `req.body.name` e assim por diante. Um array JavaScript aceita vírgula no fim; o SQL, não.
  - O `res.render` fica dentro do callback, porque fora dele "já vai querer retornar [...] muito rápido".
- **Página de sucesso:**
  - `res.render("create-point.html", { saved: true })` e `{% if saved %}{% include "partials/point-created.html" %}{% endif %}` no bloco `modal`.
  - No partial, o ícone `check.svg`, o "Cadastro concluído" e `setTimeout(() => window.location = "/", 2000)`, seguindo a nota do layout do Thiago: "delay automático de dois segundos para a homepage".
  - Primeiro ele põe o modal no bloco errado (`content`) e corrige; o `modal.css` é incluído na página.
- **Erro visível:** com `return res.send("Erro no cadastro")` no caminho do erro, o usuário também é avisado. Para provar, ele escreve `INSERT INT` de propósito. Outros erros possíveis: falha de conexão ou arquivo de banco corrompido. "É assim que funciona nas aplicações que a gente cria, a gente trata erros." O desafio é uma página de erro que volte para `/create-point`.
- **A aba Network** mostra o waterfall de requisições, incluindo a busca de municípios no IBGE.

### Pesquisa

- **`const search = req.query.search`.** Se a busca for vazia, a página renderiza com `total: 0` e o `return` encerra a função.
- **`SELECT * FROM places WHERE city = '${search}'`** é interpolado na template string, com aspas simples "porque no SQL [...] uma string no SQL vai ser aspas simples". "Rio" não acha "Rio do Sul".
- **`LIKE '%${search}%'`:** o `%` é "qualquer coisa antes" e "qualquer coisa depois". Mayk testa com "Sul", que acha Rio do Sul e Chapadão do Sul (MS).

### Ajustes e encerramento

- **O fundo da página de resultados:**
  - O `body::after` sai de `fixed` para `absolute` com `height: 16rem`.
  - As cores se invertem: o body fica branco, e a faixa, `#f0f0f5`.
  - O ajuste veio de uma observação de um colega.
- **"O aprendizado é gradativo, é um processo"**. Há encontro ao vivo no domingo às 20h.
- **Launchbase:**
  - Bootcamp de oito semanas, 100% online, a R$ 960 com "30 dias de garantia incondicional"; Mayk diz que "o risco é todo meu".
  - Argumento de aprendizado: "só existe uma coisa que vai potencializar ainda mais o seu aprendizado. Além da prática, é ensinar os outros". Ver [[wiki/concepts/aprender-ensinando]].

## Tensões e precisões

- **A pesquisa tem SQL injection.**
  - **O problema:** `WHERE city LIKE '%${search}%'` cola na query, sem tratamento, um texto vindo da URL (`req.query.search`). Uma busca como `%' OR 1=1 --` muda o comando. Com outras construções, dá para ler ou apagar dados.
  - **A contradição:** o próprio INSERT da aula usa placeholders `?`, que são a defesa.
  - **A correção:** `db.all("SELECT * FROM places WHERE city LIKE ?", [`%${search}%`], ...)`. Isso não impede que o usuário digite os curingas `%` e `_`, mas impede que ele mude o comando.
  - Ver [[wiki/concepts/sql-injection]] `[external]` (https://owasp.org/www-community/attacks/SQL_Injection).
- **"Vamos usar o SQL como nosso banco de dados."** SQL é a linguagem; o banco (SGBD) é o SQLite.
- **"Relacional porque faz relações."** Na teoria, "relação" é a própria tabela, um conjunto de tuplas; não vem de ligar uma tabela à outra `[external]` (https://en.wikipedia.org/wiki/Relational_model). A lista de sinônimos de Mayk chega perto disso. Já "entidade" é um termo de modelagem (diagrama entidade-relacionamento), não exatamente um sinônimo de tabela.
- **Os itens ficam numa coluna de texto.**
  - `items` guarda "Lâmpadas,Pilhas e Baterias" como texto, o que fere a primeira forma normal.
  - É justamente o problema que a explicação de clientes e estados resolve, com uma tabela de itens e uma de ligação (`place_items`).
  - Do jeito atual, filtrar por item exige `LIKE` no texto, e renomear um item obriga a reescrever todos os registros.
  - Ver [[wiki/concepts/relational-vs-nosql]] e [[wiki/concepts/database-index]].
- **POST não esconde nada.** O corpo do POST aparece no DevTools e trafega em texto puro sem HTTPS; quem protege é o TLS. A vantagem real é que o dado não fica no histórico, nos logs de URL nem no `Referer`. Sem HTTPS, a senha do exemplo de abertura também viaja exposta. Ver [[wiki/concepts/http-vs-https]].
- **Recarregar duplica o cadastro.**
  - Depois do POST, a página é renderizada direto (`saved: true`). Um Ctrl+R pede "resubmeter o formulário" e insere o registro de novo; o próprio Mayk usa isso como atalho.
  - O padrão certo é [[wiki/concepts/post-redirect-get]]: responder com `res.redirect("/create-point?saved=1")` (status 303).
- **Nenhuma validação no servidor.** `req.body` entra no banco do jeito que chegou. `required` e `type="url"` só valem no navegador. Ver [[wiki/concepts/validacao-de-entrada]].
- **O caminho do banco depende de onde se roda o comando.** `"./src/database/database.db"` é relativo ao diretório atual do processo, não ao arquivo. Rodar o servidor de outra pasta cria outro banco vazio. `path.join(__dirname, "database.db")` resolve. `[skill: lang-dynamic]`
- **SQLite em produção.** `[skill: tech-mentor-data]`
  - Os "conflitos" que Mayk cita são de concorrência: o SQLite aceita uma escrita por vez.
  - Em servidor, ative o modo WAL (`PRAGMA journal_mode=WAL`) e um `busy_timeout`.
  - Não faça backup copiando o arquivo aberto.
  - Hoje há opções síncronas (`better-sqlite3`) e o módulo nativo `node:sqlite` (`[skill: lang-dynamic]`, verificar a estabilidade na versão).
- **`AUTOINCREMENT` é opcional.** No SQLite, `INTEGER PRIMARY KEY` já gera ids sozinho. O `AUTOINCREMENT` só garante que ids apagados não voltem, que é o comportamento que Mayk descreve, e custa um pouco mais. A documentação recomenda evitá-lo quando essa garantia não é necessária `[external]` (https://www.sqlite.org/autoinc.html).
- **`LIKE`, maiúsculas e acentos.** O `LIKE` do SQLite ignora maiúsculas e minúsculas só em letras ASCII: "sul" acha "Sul", mas "sao" não acha "São". Um `LIKE '%x%'` também não usa índice. Ver [[wiki/concepts/database-index]] `[external]` (https://www.sqlite.org/lang_expr.html#like).
- **`rem` não muda com a tela.** `16rem` é 16 vezes a fonte da raiz, em geral 16 px. Ela só muda se o `font-size` do `html` mudar, por media query ou unidade de viewport. "Quando a página muda o seu tamanho [...] mudando o root element" está errado: quem resolve o fundo é a troca de `fixed` por `absolute`. Ver [[wiki/concepts/unidades-de-medida-css]].
- **`{% for %}` aceita `{% else %}`.** O Nunjucks tem `{% for %}...{% else %}...{% endfor %}` para lista vazia, o que dispensa o `total > 0` `[external]` (https://mozilla.github.io/nunjucks/templating.html#for).
- **Redirecionamento automático.** Os dois segundos do `setTimeout` podem não dar tempo para quem usa leitor de tela. A WCAG pede que o usuário controle limites de tempo (critério 2.2.1). Uma mensagem com um link "voltar" seria mais acessível. Ver [[wiki/concepts/acessibilidade]].
- **Venda no fim.** O argumento de "ensinar os outros" é legítimo (ver [[wiki/concepts/aprender-ensinando]]), mas vem embalado com urgência ("as vagas são limitadas"), preço e garantia. É a mesma estrutura da abertura do dia 4.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento, o Ecoleta e o Launchbase
- [[wiki/entities/express]]: `server.post`, `express.urlencoded`, `req.query` e `req.body`
- [[wiki/entities/nunjucks]]: `for`, `if/else` e `include` condicional
- [[wiki/entities/unsplash]]: imagens dos pontos cadastrados
- [[wiki/entities/ibge]]: aparece na aba Network (municípios)

Citados sem página: pacote `sqlite3`, Excel, Notion (roteiro das aulas), Thiago (designer do layout), LinkedIn, Discord.

## Conceitos

[[wiki/concepts/sqlite]] · [[wiki/concepts/sql-alem-do-basico]] · [[wiki/concepts/relational-vs-nosql]] · [[wiki/concepts/chave-primaria]] · [[wiki/concepts/database-index]] · [[wiki/concepts/sql-injection]] · [[wiki/concepts/callback-javascript]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/array]] · [[wiki/concepts/query-string]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/post-redirect-get]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/http-vs-https]] · [[wiki/concepts/template-engine]] · [[wiki/concepts/debugging]] · [[wiki/concepts/unidades-de-medida-css]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/aprender-ensinando]]

## Open Questions

- O Ecoleta termina sem edição, sem exclusão pela interface, sem autenticação e sem deploy. O "de quebra" do DELETE só roda pelo terminal.
- A tabela de itens normalizada, que o exemplo de clientes e estados prepara, fica sem implementação.
- Data provável: 5 de junho de 2020, o quinto dia da NLW #1 `[external, não verificado]`. Mayk se refere a ela como "a última aula".

## Raw quotes

- "Os dados não deveriam, não devem ficar na aplicação."
- "Callback significa chame de volta."
- "Se eu coloco assim, eu já estou imediatamente executando ela."
- "É assim que funciona nas aplicações que a gente cria, a gente trata erros."
- "O aprendizado é gradativo, é um processo."
