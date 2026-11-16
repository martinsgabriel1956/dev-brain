---
type: source
title: "NLW #2, dia 4: back-end do Proffy com Node.js, Express e Nunjucks"
aliases: ["NLW 2 dia 4", "Next Level Week 2 dia 4", "Proffy dia 4", "Proffy back-end"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [backend, nodejs, express, nunjucks, template-engine, npm, package-json, json, nodemon, git-bash, terminal, rotas, req-res, express-static, metodos-http, query-string, regra-de-negocio, arrow-function, array, object-keys, redirect, memoria, javascript, rocketseat, proffy, iniciante]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-dia-4-back-end-node-express-nunjucks-proffy.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2, dia 4: back-end do Proffy com Node.js, Express e Nunjucks

## TL;DR

Quarta aula (cerca de 2h04, a transcrição termina cortada) da [[wiki/entities/next-level-week|NLW #2]] com [[wiki/entities/mayk-brito|Mayk Brito]]. É o primeiro back-end do **Proffy** e segue de perto o [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta|dia 4 da NLW #1]]: mesma pilha, mesma analogia do cozinheiro.

- **Conceitos:** o back-end recebe pedidos e aplica [[wiki/concepts/regra-de-negocio|regras de negócio]] que o cliente não pode mexer, como o preço do sapato conferido no servidor.
- **Ambiente:** [[wiki/entities/nodejs|Node.js]] LTS (12.18.3 na época), Git Bash como terminal do VS Code, pastas `src/` (com `views/` e `server.js`) e `public/` (imagens, scripts, estilos). O Live Server é desinstalado.
- **Servidor:** `npm init -y` ([[wiki/concepts/package-json|package.json]], [[wiki/concepts/json|JSON]]), `npm install express`, `require`, `server.listen(5500)`, rotas `get` com arrow function `(req, res)`, `res.send`, `sendFile(__dirname + ...)`, `express.static("public")` e nodemon com `npm run dev`.
- **Dados:** os professores viram um array de objetos no próprio `server.js`; [[wiki/entities/nunjucks]] ([[wiki/concepts/template-engine|template engine]]) renderiza `{{ }}`, `{% for %}` e `{% if %}`, com `loop.index`. Os filtros da página study voltam preenchidos via `req.query`; o cadastro de give-classes chega por [[wiki/concepts/query-string|query string]], ganha o nome da matéria com `getSubject()`, entra no array com `push` (se `Object.keys(data).length` não for zero) e redireciona para `/study`. O botão de WhatsApp vira um link para `api.whatsapp.com/send`.
- **Limite:** tudo some quando o servidor reinicia, porque está em memória; o banco de dados fica para o dia 5. Ver [[wiki/concepts/dados-em-memoria-vs-persistencia]].

## Key Claims

### Por que back-end

- **Sem back-end "não tem jogo":** um YouTube onde não se pede nem se guarda vídeo, um Instagram onde não se posta foto.
- **Responsabilidade:** "receber os pedidos do cliente", prepará-los e devolver; o front-end é o cliente. Ver [[wiki/concepts/arquitetura-cliente-servidor]].
- **Regra de negócio** é a preparação: desconto no Natal, presente para quem mora a 10 km. "Dá para fazer no front-end? Até que dá", mas o JavaScript do navegador pode ser manipulado: quem "entende um pouquinho mais de programação" muda o preço; o back-end "vai verificar se realmente o preço daquele sapato é aquele mesmo". "O cliente não pode meter o pé na porta do cozinheiro." Ver [[wiki/concepts/regra-de-negocio]] e [[wiki/concepts/confiar-no-frontend]].
- **Uma linguagem só:** focar no JavaScript para front e back faz "deslanchar muito mais do que você ficar pegando um monte de linguagens picadinho".

### Node.js, Git Bash e terminal

- **Node:** o JavaScript roda no navegador; no servidor, "o Node nasceu com o intuito de rodar o JavaScript na máquina". Dois cliques num `.js` no Windows dão erro do Windows Script Host. Ver [[wiki/entities/nodejs]].
- **Versão LTS** (12.18.3 no vídeo), "recomendado para a maioria dos usuários"; a Current traz "coisa nova que a comunidade ainda não passou por problema suficiente". No Linux, pelo gerenciador de pacotes; Mac e Linux não precisam do Git Bash.
- **Git Bash** no lugar do CMD e do PowerShell: "uma ideia universal de sistemas Unix". No VS Code: Terminal → Select Default Shell → Git Bash. Ver [[wiki/concepts/emulador-de-terminal]].
- **Comandos:** `cd /c/nlw` ("Change Directory"), `pwd`, Ctrl+L para limpar, Ctrl+C para parar, `node -v` e `npm -v`. Fechar o painel deixa o processo rodando; a lixeira o mata.

### Estrutura do projeto

- **`src/`** com os HTML (depois em `src/views/`) e `server.js`; **`public/`** com `images/`, `scripts/` e `styles/`. "Isso aqui já é o início da [...] reestruturação de pastas." Ver [[wiki/concepts/refatoracao]].
- **Adeus, Live Server:** desinstalar "pra você não cair na tentação". "Não adianta nada eu fazer todo o meu front-end e depender do Visual Studio Code pra funcionar."

### npm, package.json e JSON

- **npm** é o "gerenciador de pacotes do Node", de "sub-aplicações". `npm init -y` cria o `package.json`. Ver [[wiki/concepts/gerenciador-de-pacotes]] e [[wiki/concepts/package-json]].
- **JSON** é "JavaScript Object Notation": chaves e valores entre aspas duplas, vírgula só entre itens, colchetes para listas (array ou vetor). No objeto JavaScript, as aspas nas chaves "são facultativas". Ver [[wiki/concepts/json]].
- **`npm install express`** cria `node_modules` (com as dependências do Express, cada uma "um projeto com suas próprias configurações") e `package-lock.json`, "pra mapear todas as dependências". "A gente só precisa entender como usar o Express, não entender como o Express foi feito." Ver [[wiki/entities/express]].

### Primeiro servidor

- **`require('express')`** devolve uma função; `express()` executa e devolve um objeto com `listen`, `get`, `use`. Ele relembra declarar x chamar função, `return` e objeto (`name`, `age: 33`). Ver [[wiki/concepts/funcoes-javascript]].
- **`listen(5500)`**, "pra homenagear o Live Server"; `node src/server.js`. Sem rota, "Cannot GET /"; com o servidor parado, a página não carrega.
- **Rotas:** `.get("/", (req, res) => res.send("Hi from NLW"))`. A arrow function é "uma função curta"; `req` é "o que acompanha o meu pedido", `res` é "o que ele vai mostrar para a minha tela". `/study` também, como o `/watch` do YouTube.
- **Reiniciar a cada mudança** é chato; nodemon "reinicia o servidor" ao salvar arquivos `.js`, `.mjs` e `.json`. Instalado com `-D` ("só pra quem é desenvolvedor"), rodado por um script `dev` no `package.json` e `npm run dev`; `rs` força o restart.

### HTML pelo servidor

- **`res.sendFile(__dirname + "/views/index.html")`:** `__dirname` é a pasta do arquivo (`src`). O `console.log` agora sai no terminal: "o console do back-end é o terminal".
- **CSS sumiu:** o navegador pede `/styles/main.css` e o servidor não tem essa rota. `server.use(express.static("public"))` serve a pasta `public` "como se fosse a pasta raiz"; arquivos estáticos são "imagens, o script lá do front-end, o CSS". `.use` é "configuração do servidor". `const express = require(...)` e `const server = express()` separam a função do objeto.
- **Rotas no lugar de `.html`:** os botões passam a apontar para `/study` e `/give-classes`.
- **Sem VS Code:** rodando `node src/server.js` no Git Bash, o site continua de pé com o editor fechado; "meu servidor, nesse caso, é a minha própria máquina".

### GET, localhost, IP e porta

- **localhost = 127.0.0.1**, "toda a nossa máquina local [...] tem esse mesmo endereço de IP"; um domínio como youtube.com "é transformado no endereço de IP deles". Ver [[wiki/concepts/endereco-ip]] e [[wiki/concepts/dns]].
- **Porta:** "a porta padrão é a porta 80" (ver Tensões). Ver [[wiki/concepts/porta-de-rede]].
- **GET** é "o padrão desse verbo"; "Cannot GET" diz que não há rota para aquele verbo e caminho. POST fica para o dia 5. Ver [[wiki/concepts/metodos-http]].

### Dados e template engine

- **Array de objetos:** `const profs = [{ name, avatar, whatsapp, bio, subject, cost, weekday: [0], time_from: [720], time_to: [1220] }, ...]`, com Diego Fernandes, Daniele Evangelista e depois o próprio Mayk. "Cada prof é um objeto dentro de uma lista de objetos." Os horários "a gente vai converter em segundos" (valores "chutados"). Aspas duplas dentro da bio quebram a string. Ver [[wiki/concepts/array]].
- **HTML não entende JavaScript:** "o HTML simplesmente apresenta dados [...] Ele não tem a capacidade de entender o dado em JavaScript". A template engine é um "motor" que dá ao HTML "esteroides". Ver [[wiki/concepts/template-engine]].
- **Funções nomeadas** (`pageLanding`, `pageStudy`, `pageGiveClasses`) separam as rotas da lógica: "me parece um pouquinho mais organizado".
- **Nunjucks:** `npm install nunjucks`, `nunjucks.configure('src/views', { express: server, noCache: true })`, `res.render('study.html', { profs })`. `noCache` porque "a gente quer ver a versão sempre mais recente". Ver [[wiki/entities/nunjucks]].
- **`{{ }}`:** `{{ profs }}` mostra "object, object", porque o HTML não sabe o que fazer com o objeto; `{{ title }}`, `{ profs }` é atalho para `{ profs: profs }`; `{{ diego.name }}` mostra o nome.
- **`{% for prof in profs %} ... {% endfor %}`:** "para um prof em profs"; "se vier mil, mil vezes irá aparecer". Cada card usa `prof.avatar`, `prof.name`, `prof.subject`, `prof.bio`, `prof.cost`.
- **WhatsApp:** o botão vira `<a href="https://api.whatsapp.com/send?phone=55{{prof.whatsapp}}&text=Tenho interesse na sua aula de {{prof.subject}} {{prof.name}}">`, com classe `.button` no CSS.

### Ler e devolver os filtros

- **Query string:** o formulário sem `action` envia para a própria página, e a URL mostra `?subject=1&weekday=0&time=`; `%3A` "é a substituição via URL desses dois pontinhos". O Express entrega isso em `req.query`, um objeto, vazio quando não há filtro. Ver [[wiki/concepts/query-string]].
- **Devolver o que veio:** `const filters = req.query` e `value="{{ filters.time }}"` no input de hora.
- **`selected` condicional:** `{% if filters.subject == "4" %}selected{% endif %}`. "Esse igual sozinho é sempre de atribuição"; `==` é comparação.
- **Loop em vez de cópia:** "faz sentido eu ficar fazendo isso aqui? [...] E se eu tiver aqui simplesmente mil aulas?" `const subjects = [...]` e `weekdays = [...]` no servidor, `{% for subject in subjects %}` com `value="{{ loop.index }}"`, que começa em 1, e `loop.index0` para os dias, que começam em 0.
- **O que é um if:** "o se sempre vai observar se alguma coisa é verdadeira"; "a gente consegue ver pelo menos dois caminhos". "Esse se do Nunjucks, ele é um se diferente do que a gente vai ver no JavaScript", mas a ideia é a mesma. Ver [[wiki/concepts/logica-de-programacao]].
- **give-classes** recebe `subjects` e `weekdays` pelo mesmo render, sem o `selected`.

### Receber o cadastro

- **`const data = req.query`** e `console.log(data)`: name, avatar, WhatsApp, bio, subject (número), cost e os horários como texto. "É ruim deixar dados expostos assim", o que o POST do dia 5 vai resolver.
- **`profs.push(data)`:** "push significa empurrar".
- **O vazio que existe:** `if (data)` entra mesmo sem dados, porque um objeto vazio "existe". `Object.keys(data).length != 0` transforma as chaves em array e confere o tamanho; o nome vira `isNotEmpty`. "Isso aqui é a programação [...] é pensar de maneira lógica."
- **Dois caminhos:** com dados, adiciona e faz `res.redirect("/study")`; sem dados, renderiza o formulário. Ver [[wiki/concepts/post-redirect-get]].
- **Bug do `name`:** o custo não chegava porque o input estava sem `name`: "lembra que eu te falei que é obrigatório ter o name".
- **`getSubject(subjectNumber)`:** `const arrayPosition = +subjectNumber - 1` e `return subjects[arrayPosition]`, porque o valor 1 é Artes e o array começa em 0. Ver [[wiki/concepts/funcoes-javascript]].
- **A memória:** depois de salvar o `server.js`, o Clayton cadastrado some. "Toda vez que eu altero esse arquivo [...] a nossa aplicação é simplesmente resetada [...] eu perco todos os dados da memória." Persistir é "guardar no banco de dados", que grava no disco. Ver [[wiki/concepts/dados-em-memoria-vs-persistencia]].
- **Ajuste final:** `label small` com `font-size: 1.2rem`, `padding-left` e `var(--color-small-info)`.

### Revisão

- Variáveis, strings, null, arrays, números, boolean, objetos, funções ("o grande lance da programação"), `if` e repetição (`for` do Nunjucks, `forEach` do JavaScript); GET, query strings, requisição e resposta, arquivos estáticos e Nunjucks. Dia 5: POST, body e banco de dados.
- **"Eu mesmo demorei muitos anos para aprender tudo isso."**

## Tensões e precisões

- **`==` do Nunjucks compara por igualdade frouxa.** `req.query` traz strings ("2"), e `loop.index` é número (2). `{% if filters.subject == loop.index %}` só funciona porque o `==` do Nunjucks é o `==` do JavaScript, que converte os tipos `[external]` (https://mozilla.github.io/nunjucks/templating.html#comparisons). Com `===`, nenhuma opção ficaria selecionada. Ver [[wiki/concepts/igualdade-javascript]]. Confiança alta.
- **`push(req.query)` sem validação.** O que chega na URL vai direto para a lista mostrada a todos: campos faltando, `subject` fora da faixa (`getSubject` devolve `undefined`), chaves extras. O `required` do dia 3 só vale no navegador. A própria aula diz que o back-end é quem confere o preço do sapato, mas não confere o cadastro. Ver [[wiki/concepts/confiar-no-frontend]]. Confiança alta.
- **POST não "esconde" os dados.** O POST tira os campos da URL (histórico, logs, Referer), mas o corpo continua visível no DevTools e em proxies. O que protege em trânsito é o HTTPS. Mesmo ponto do [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|dia 5 da NLW #1]]. Ver [[wiki/concepts/http-vs-https]].
- **Porta padrão 80 é do HTTP.** youtube.com usa HTTPS, cuja porta padrão é 443; em `youtube.com:80` o servidor só redireciona para o HTTPS `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview). Ver [[wiki/concepts/porta-de-rede]]. Confiança alta.
- **`-D` não instala "em outro lugar".** `npm install -D` grava o pacote em `devDependencies` no `package.json`; a pasta é a mesma `node_modules`. A diferença aparece em `npm install --omit=dev` (ou `NODE_ENV=production`), que pula os de desenvolvimento `[external]` (https://docs.npmjs.com/cli/commands/npm-install). Confiança alta.
- **`express.static("public")` é relativo a onde o comando roda.** O caminho é resolvido a partir do diretório de trabalho do processo, não de `server.js`: rodar `node server.js` de dentro de `src/` quebra os estáticos. O mesmo vale para `nunjucks.configure('src/views')`. O seguro é `path.join(__dirname, '..', 'public')` `[external]` (https://expressjs.com/en/starter/static-files.html). E `__dirname + "/views/..."` funciona, mas `path.join` evita barras duplas e separadores do Windows.
- **`noCache: true` fica ligado também em produção.** É útil para desenvolver, mas sem condição faz o Nunjucks recompilar o template a cada requisição. Mesmo ponto anotado na [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta|NLW #1]]. `[skill: tech-mentor-backend]` Condicionar a `NODE_ENV`.
- **Texto da URL do WhatsApp sem codificação.** O Nunjucks escapa HTML, não URL. Nomes com `&`, `#` ou `?` quebram os parâmetros, e acentos e espaços dependem da tolerância do navegador. O correto é passar por `encodeURIComponent` (ou o filtro `urlencode`) `[external]` (https://mozilla.github.io/nunjucks/templating.html#urlencode).
- **"IP sempre é único" e "toda máquina local tem 127.0.0.1".** O loopback é o mesmo em toda máquina, certo. Endereços públicos podem ser compartilhados (NAT, CGNAT), e um mesmo domínio responde por muitos IPs (CDN, anycast). "Protocolo de identificação" mistura o protocolo (IP) com o endereço. Ver [[wiki/concepts/endereco-ip]].
- **Horários "em segundos".** Os valores 720 e 1220 foram chutados na aula; 9:00 em segundos seria 32.400. O formato de armazenamento só se define no dia 5.
- **`express()` devolve uma função** (o app é uma função com métodos `get`, `use`, `listen`), que ele trata como "um objeto". Em JavaScript funções são objetos, então não está errado, só incompleto.
- **Node.js 12 saiu de suporte em abril de 2022**; a versão LTS do vídeo está datada `[external]` (https://github.com/nodejs/release#end-of-life-releases). Mesmo ponto do [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native|Diego na NLW #1]].
- **Estado em memória** some também em qualquer queda, deploy ou com mais de uma instância rodando (cada uma teria sua lista). Ver [[wiki/concepts/dados-em-memoria-vs-persistencia]] e [[wiki/concepts/sistema-de-arquivos-efemero]].

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor (aparece também como professor de exemplo)
- [[wiki/entities/next-level-week]]: NLW #2
- [[wiki/entities/rocketseat]]: organizadora; Clayton Souza, "colaborador da Rocketseat", vira professor de exemplo
- [[wiki/entities/nodejs]]: runtime do back-end
- [[wiki/entities/express]]: servidor, rotas, `static`, `redirect`
- [[wiki/entities/nunjucks]]: template engine
- [[wiki/entities/diego-fernandes]]: primeiro professor do array
- [[wiki/entities/github]]: links dos avatares
- [[wiki/entities/vs-code]]: terminal integrado com Git Bash, split de terminal, Alt + clique

Citados sem página: Git Bash, nodemon, Daniele Evangelista (professora de exemplo), Clayton Souza, WhatsApp, YouTube e Instagram (exemplos), Windows Script Host.

## Conceitos

[[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/regra-de-negocio]] · [[wiki/concepts/confiar-no-frontend]] · [[wiki/concepts/emulador-de-terminal]] · [[wiki/concepts/refatoracao]] · [[wiki/concepts/gerenciador-de-pacotes]] · [[wiki/concepts/package-json]] · [[wiki/concepts/json]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/endereco-ip]] · [[wiki/concepts/dns]] · [[wiki/concepts/porta-de-rede]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/http-vs-https]] · [[wiki/concepts/array]] · [[wiki/concepts/template-engine]] · [[wiki/concepts/query-string]] · [[wiki/concepts/logica-de-programacao]] · [[wiki/concepts/igualdade-javascript]] · [[wiki/concepts/post-redirect-get]] · [[wiki/concepts/dados-em-memoria-vs-persistencia]] · [[wiki/concepts/sistema-de-arquivos-efemero]]

## Open Questions

- O dia 5 vai trocar a query string por POST + body, guardar no SQLite e converter os horários (a aula fala em segundos). Falta ver se haverá validação no servidor.
- O favicon e o theme-color repetidos (dia 3) não voltam a aparecer; os `includes` do Nunjucks são citados na revisão como "ainda não usamos".
- A transcrição termina em "você vai pirar no que a gente vai".

## Raw quotes

- "O cliente não pode meter o pé na porta do cozinheiro lá."
- "Não adianta nada eu fazer todo o meu front-end e depender do Visual Studio Code pra funcionar ele."
- "O console do back-end é o terminal."
- "O HTML simplesmente apresenta dados, ele estrutura e apresenta, só isso."
- "Eu perco todos os dados da memória."
