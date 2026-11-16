---
type: source
title: "NLW #1, dia 4: back-end com Node.js, Express e Nunjucks no Ecoleta"
aliases: ["NLW 1 dia 4", "Next Level Week 1 dia 4", "Ecoleta back-end", "Ecoleta Express Nunjucks"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [backend, nodejs, express, nunjucks, template-engine, npm, package-json, nodemon, rotas, http, localhost, porta, git-bash, sqlite, lang-dynamic, frontend, rocketseat, ecoleta, iniciante]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta.md"
source_url: ""
author: "Mayk Brito"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1, dia 4: back-end com Node.js, Express e Nunjucks no Ecoleta

## TL;DR

Quarta aula (cerca de 1h55) da [[wiki/entities/next-level-week|Next Level Week #1]] da [[wiki/entities/rocketseat]], com [[wiki/entities/mayk-brito]]. Depois de três dias de front-end ([[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta|dia 3]]), o Ecoleta ganha um back-end. A aula tem cinco partes:

1. **O que o back-end faz.** Mayk volta à analogia do restaurante: o back-end recebe o pedido, aplica regras de negócio, guarda dados e responde. Ver [[wiki/concepts/arquitetura-cliente-servidor]].
2. **O ambiente.**
   - O [[wiki/entities/nodejs|Node.js]] LTS, porque fora do navegador "a nossa máquina não tem" quem entenda JavaScript.
   - O Git Bash como terminal padrão do [[wiki/entities/vs-code]] no Windows.
   - O SQLite, anunciado para o dia seguinte.
3. **Como uma página chega até você.** O Live Server já era um servidor. Mayk explica localhost, 127.0.0.1, [[wiki/concepts/endereco-ip|IP]] e [[wiki/concepts/porta-de-rede|portas]] (5500, 3000, 80).
4. **O servidor.**
   - O projeto é reorganizado em `public/` (estilos, scripts, imagens) e `src/` (`server.js` e `views/`).
   - `npm init -y` cria o [[wiki/concepts/package-json|package.json]], e o [[wiki/entities/express]] cria o servidor "com apenas três linhas de código".
   - Depois vêm o script `start`, o nodemon, as rotas `GET` com `req` e `res`, o `sendFile` com `__dirname` e o `express.static("public")`.
5. **O [[wiki/concepts/template-engine|template engine]] [[wiki/entities/nunjucks]].**
   - `{{ variável }}` nos templates.
   - `include` de partials (o cabeçalho e o modal).
   - Um `layout.html` com `extends` e `block`, onde cada página preenche estilos, título, conteúdo, modal e scripts.
   - `set` para o id da página.

No fim, Mayk resolve pendências do formulário (o texto "Selecione um ou mais itens abaixo", um campo `type="url"` para a imagem e a responsividade) e anuncia o Launchbase.

## Key Claims

### Abertura: tempo até o mercado

- **"O tempo médio que você vai precisar é de 2 a 6 meses"**, "desde que você tenha o método certo". Quem leva dois anos fica assim porque "falta foco, falta prática, falta um grupo". A base citada é "depois de treinar quase 2 mil alunos nos nossos bootcamps". Ver a seção de tensões.
- **Sem atalho:** "pular etapas parece ser uma forma fácil [...] mas é justamente o contrário". O aprendizado é como a academia: "você precisa ter paciência, confiar no processo e praticar todos os dias". Ver [[wiki/concepts/pratica-deliberada]].

### O que o back-end faz

- **De volta ao restaurante:** antes a xícara de café representava o front-end; agora é o "chefzinho". O back-end "tem a responsabilidade de receber os pedidos do cliente", preparar e "enviar as respostas". Ver [[wiki/concepts/arquitetura-cliente-servidor]].
- **Regras de negócio no meio do caminho.** No exemplo do cozinheiro, lavar as mãos, pegar a comida e fritar. No login com CPF e senha:
  1. Validar se o CPF está cadastrado.
  2. Ver se a senha bate.
  3. Responder positiva ou negativamente.
- **Guardar os dados:** "eu não tenho como comparar um CPF cadastrado no sistema, se eu não tiver esse CPF cadastrado no sistema". Por isso o back-end também armazena. Ver [[wiki/concepts/sqlite]].
- **Uma linguagem só.** Existem PHP, Python e outras, mas JavaScript nos dois lados faz o caminho ser "muito mais bem aproveitado".

### O ambiente

- **Quem roda JavaScript:** no front-end é o navegador, que "tem um motor aqui por trás". No computador é o Node.js, que "usa o motor de JavaScript do Chrome". Ver [[wiki/entities/nodejs]].
- **LTS, não Current.** A Current, "por ser muito mais nova [...] pode vir com alguns bugs". LTS é "Long Term Support", "uma versão mais estável". A instalação é "next, next, next, next e install". A versão mostrada no `node -v` é a 12.18; no npm, a 6.14.
- **Git Bash no Windows**, como "Select Default Shell" do terminal do VS Code. CMD e PowerShell "são terminais um pouco mais diferentes de se trabalhar". Com o Git Bash, os comandos se parecem com os de Mac e Linux, e em produção "você vai provavelmente usar um ambiente Linux". Ver [[wiki/concepts/shell-terminal]].
- **SQLite** é o banco do projeto, "amanhã eu explico melhor". Ver [[wiki/concepts/sqlite]].
- **O REPL:** `node` sozinho abre "um ambiente onde eu posso executar JavaScript", como o console do navegador, e `.exit` sai dele. Ctrl+L limpa o terminal.

### Localhost, IP e portas

- **Abrir o HTML com dois cliques não funciona mais:** a página abre "estragada", porque os caminhos com `/` foram feitos "para funcionar com o servidor". Ver [[wiki/concepts/caminho-relativo]].
- **O Live Server era um servidor:** "Server significa servidor, servidor está relacionado ao back-end". Ele "abriu uma porta de número 5500". Com o VS Code fechado, a página não carrega mais.
- **Nome → número.** `youtube.com` "é convertido para números depois, e esses números nós chamamos de endereço de IP", endereços que "mostram a localização do servidor", uma máquina "em algum lugar do mundo". `localhost` e `127.0.0.1` são a própria máquina. Ver [[wiki/concepts/endereco-ip]] e [[wiki/concepts/dns]].
- **Portas:** "temos inúmeras portas para entrar no servidor". `youtube.com` equivale à porta 80, "que ela já existe aqui escondidinha"; a 81 fica carregando "para sempre". Ver [[wiki/concepts/porta-de-rede]].

### Estrutura de pastas e npm

- **`public/`** recebe `assets`, `scripts` e `styles`, "coisas que ficam públicas na nossa aplicação": qualquer um acessa `/styles/main.css` ou `/assets/logo.svg`.
- **`src/`** recebe `server.js` e `views/` com os HTML ("views significa visualizar").
- **Copie exatamente, depois mude.** "Mesmo nome, não coloca maiúscula, não coloca minúscula, não coloca espaço." E também: "a aula não é feita para te ensinar [...] É feita para você entender". Aprender é "hora, bunda, cadeira". Ver [[wiki/concepts/entender-vs-aprender]].
- **Módulos** ("dependências", "packages") são "programas, aplicações feitas por terceiros". Dava para fazer o servidor "com o Node puro", mas "seria um arquivo muito grande".
- **npm é o "Node Package Manager"**, o "gerenciador de dependências do Node". Ver [[wiki/concepts/gerenciador-de-pacotes]].
- **`npm init -y`** cria o `package.json`, um [[wiki/concepts/json|JSON]] com "todas as propriedades [...] com aspas duplas". Por enquanto importam o `name` e os `scripts`. O `main` vira `src/server.js`. Ver [[wiki/concepts/package-json]].
- **`npm install express`** cria o `node_modules` (com todas as dependências do Express) e o `package-lock.json`, e registra o Express em `dependencies`. Por isso o `node_modules` não vai para o repositório: quem baixa o projeto roda `npm install` e "sozinho o npm já baixa de novo todas as dependências".
- **Calma:** "nada disso é para você memorizar". "O tempo vai te trazer resultados."

### O servidor com Express

- **`const express = require("express")`**. Aqui entra uma analogia que a irmã sugeriu a Mayk para funções: uma "caixinha mágica" que recebe um argumento e "vai contra-argumentar te devolvendo alguma resposta". Ver [[wiki/concepts/funcoes-javascript]].
- **`const server = express()`** dá "um objeto de servidor". `server.listen(3000)` liga o servidor: "listen é ouvir".
- **Executar:** `node server.js` falha porque o arquivo está em `src/`. O comando certo é `node src/server.js`. "Cannot GET /" já prova que a porta 3000 responde; a 3001, não. "Acredita que você criou um servidor com apenas três linhas de código?" Ver [[wiki/entities/express]].
- **O script `start`:** `"start": "node src/server.js"` no `package.json`, rodado com `npm start`. Ctrl+C para o servidor.

### Rotas, GET, req e res

- **"Cannot GET /"** significa, na voz do servidor, "eu não achei uma rota, eu não achei um caminho". O `/` é a página inicial: `youtube.com` e `youtube.com/` são o mesmo endereço.
- **`server.get("/", (req, res) => { ... })`** traz arrow function com dois argumentos e parênteses obrigatórios.
- **GET "é um verbo HTTP"**, uma das regras do protocolo; "a gente vai trabalhar depois no verbo post", o do envio de formulário. Ver [[wiki/concepts/metodos-http]].
- **`req` e `res`:** "Req é uma requisição. Requisição é um pedido. Res é uma resposta." O `res.send("cheguei aqui")` foi a primeira resposta. "Lembra que tudo é dado, gente." Ver [[wiki/concepts/requisicao-http]].
- **nodemon:**
  - Cada mudança no servidor exigia reiniciá-lo.
  - `npm install nodemon -D` instala como dependência de desenvolvimento, "isso aqui só vai funcionar enquanto eu estiver desenvolvendo".
  - O `start` passa a ser `nodemon src/server.js`; `rs` reinicia na mão, e ele vigia `.js`, `.mjs` e `.json`.
  - O navegador continua precisando de Ctrl+R.

### Servindo as páginas

- **`res.sendFile(__dirname + "/views/index.html")`:** `__dirname` é "uma variável global" com o caminho da pasta do arquivo atual (`.../nlw/src`).
- **Estilos e imagens somem:** o console mostra os arquivos "não encontrados". A solução é `server.use(express.static("public"))`: o conteúdo de `public/` aparece "como se as pastas já estivessem disponíveis aqui na raiz do meu projeto". `use` é configuração do servidor, à parte das rotas e do `listen`.
- **Rotas, não arquivos:** `/create-point` serve `create-point.html` "sem o .html", porque "eu não estou mais chamando arquivos [...] Eu estou chamando rotas". Os links do HTML também passam a apontar para as rotas.
- **Produção, um dia:** comprar um domínio (ecoleta.com.br) apontando para o IP de um servidor físico rodando o Node.

### Nunjucks: template engine

- **O que é:** um "motor" que transforma o HTML, "que simplesmente servia para marcação de texto", em um arquivo com variáveis, if/else e laços. Serve para trocar trechos "por dados que vão vir do servidor", como os cards da busca: "eu não posso ficar colocando na mão". Antes estático, "não tinha vida"; agora, dinâmico. Ver [[wiki/concepts/template-engine]] e [[wiki/entities/nunjucks]].
- **Configuração:** `nunjucks.configure("src/views", { express: server, noCache: true })`. O cache serve versões velhas dos templates, por isso `noCache` "enquanto eu estiver desenvolvendo".
- **`return res.render("index.html")`:** `render` passa o arquivo "pelo motor do Nunjucks" e devolve "o HTML puro". Mayk recomenda sempre o `return`: "chega o momento da nossa aplicação, que se não tivesse return aqui, a gente pode encontrar alguns bugs".
- **Variáveis:** `res.render("index.html", { title: "Um título" })` e `{{ title }}` no HTML. Sem o servidor, o arquivo mostra o `{{ title }}` cru. O exemplo dinâmico é o YouTube: a tela de cada pessoa é diferente porque "tem uma regra de negócio". Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **`include`:** o cabeçalho "voltar para home" de duas páginas vai para `views/partials/page-header.html` e entra com `{% include "partials/page-header.html" %}`. O modal da home também vira partial. "E se fossem cem? E se fossem mil páginas?" Ver [[wiki/concepts/dry]].
- **Primeiro bug do template:** "template not found" porque a pasta se chama `partials`, não `partial`: "o bom e velho typo".
- **A rota `/search`** serve `search-results.html`, e o `action` do modal passa a ser `/search`. O envio por GET põe a busca na URL.

### Layout com extends e block

- **Por que um layout:** `html`, `head`, `body`, `main.css` e `responsive.css` "se repetem" em todas as páginas. O `include` "serve pra pedaços pequenos". O `layout.html` é a "casca"; cada página começa com `{% extends "layout.html" %}` e "vai pegar e herdar" essa estrutura.
- **Blocos:**
  - `{% block styles %}{% endblock %}` no layout é "substituído pelo mesmo bloco" da página.
  - Página sem o bloco "está tudo bem", e o conteúdo fora de blocos é jogado fora.
  - `block title` com um título padrão no layout (Ecoleta; "e coleta" na transcrição).
  - `block content`, `block modal` (fora do conteúdo, onde o modal já ficava) e `block scripts`.
- **`set`:** `{% set pageId = "page-home" %}` na página e `id="{{ pageId }}"` no layout. Ele começa com `bodyId` e troca porque "page id, muito mais sentido". Sem a variável, sai `id=""`, o que "está tudo bem".
- **Pensar caminhos alternativos:** como no xadrez, pensar jogadas à frente. "E se isso daqui não existir? E se eu errar isso daqui?"
- **Indentação:** "uma boa prática que seu código sempre esteja bem identado" (sic), feita com Format Document (Ctrl+Shift+P).
- **Comentário Nunjucks:** `{# ... #}`.

### VS Code para Nunjucks

- **A extensão Nunjucks Template** colore a sintaxe e traz snippets (`n-extends`, `n-block`, `n-if`, `n-for`, `n-set`).
- **Ajustes no `settings.json`:**
  - `"files.associations": { "*.html": "njk" }` faz o HTML ser lido como Nunjucks.
  - Isso quebra o Emmet, consertado com `"emmet.includeLanguages": { "njk": "html" }`.
  - Com a extensão vscode-icons, mais uma associação traz os ícones de volta.
- Mayk chama tudo isso de "perfumaria", mas que "faz uma diferença danada". Ver [[wiki/entities/vs-code]].

### Full MVC, full stack e pendências

- **"Full MVC":** Mayk chama assim o projeto, um sistema que "envolve o front-end e o back-end na mesma aplicação"; "você está sendo um desenvolvedor full stack aqui". Ver as tensões.
- **Fica para amanhã:** banco de dados, POST e como o servidor recebe dados do front-end.
- **Pendências:**
  - Um `span` "Selecione um ou mais itens abaixo" na `legend`, em `display: flex` com `space-between`, `width: 100%` e fonte de 14 px.
  - Um campo "Imagem da entidade" com `type="url"`, `name="image"` e `required`, que barra "ddddd" com "please enter a URL"; `placeholder="http://"`.
  - Abaixo de 900 px, o `.field-group` vira coluna e o `.field + .field` perde a `margin-left`. O resto do mobile "ficam os desafios".

### Encerramento

- "É impossível dominar tudo o que você precisa e que você tem que saber em apenas uma semana."
- Anúncio da próxima turma do Launchbase, "treinamento 100% online intensivo" da Rocketseat.

## Tensões e precisões

- **"De 2 a 6 meses" é um número sem método.** A afirmação vem de quem vende o bootcamp anunciado no fim da mesma aula. Não há definição de "pronto", de amostra nem de taxa de colocação. Trate como discurso de venda, não como dado. Ver [[wiki/concepts/pratica-deliberada]].
- **Porta 80 e HTTPS.** `youtube.com` digitado no navegador vai para HTTPS, que usa a porta 443. A 80 é a do HTTP sem TLS, que o YouTube só usa para redirecionar `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview). Ver [[wiki/concepts/http-vs-https]].
- **O Live Server é um servidor de arquivos estáticos.** Ele serve arquivos e recarrega a página; não tem regra de negócio, banco ou rotas. "Servidor está relacionado ao back-end" vale no sentido amplo. Ver [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]].
- **O Git Bash não é Linux.** Ele traz um bash com utilitários Unix sobre o Windows (MSYS2). O WSL roda um Linux de verdade, e é a opção mais próxima de produção `[external]` (https://learn.microsoft.com/en-us/windows/wsl/about).
- **"Esse lugar específico de Git."** Git é o sistema de controle de versão; o lugar onde o projeto fica "à disposição de outros" é um repositório remoto, como o GitHub. Ver [[wiki/concepts/git]].
- **O `package-lock.json` deve ir para o repositório.** Não é um "pode até enviar": é ele que garante as mesmas versões em todas as máquinas e no CI, com `npm ci` `[external]` (https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json). O `node_modules` fica de fora via `.gitignore`. Ver [[wiki/concepts/package-json]].
- **O nodemon virou opcional.** `[skill: lang-dynamic]` `node --watch` faz o mesmo nativamente desde o Node 18/20, e `node --run` roda scripts do `package.json`.
- **Versões de 2020:** Node 12 e Express 4. `[skill: lang-dynamic]`
  - Hoje a LTS de produção é o Node 24, e o 26 vira LTS em 28/10/2026.
  - O Express 5 é a versão `latest` do npm. Ele repassa erros de handlers async para o `next(err)` e muda a sintaxe de curingas nas rotas.
  - Para projetos novos, a skill recomenda Fastify.
  - O `require` é CommonJS. Em ESM (`"type": "module"`) usa-se `import` e `import.meta.dirname` no lugar de `__dirname`.
- **`__dirname + "/views/index.html"`** funciona, mas `path.join(__dirname, "views", "index.html")` monta o caminho certo em qualquer sistema. `[skill: lang-dynamic]`
- **`noCache: true` sem condição** também vai para produção se ninguém mudar. O certo é ligá-lo só em desenvolvimento, por exemplo `noCache: process.env.NODE_ENV !== "production"` `[external]` (https://mozilla.github.io/nunjucks/api.html#configure).
- **O Nunjucks escapa HTML por padrão.** Em `{{ variavel }}`, o `autoescape` já vem ligado. Isso protege contra XSS quando os dados vierem do banco no dia 5; o filtro `| safe` desliga a proteção `[external]` (https://mozilla.github.io/nunjucks/api.html#configure). É o contrário do `innerHTML` do dia 2 ([[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]).
- **O `return` antes de `res.render`** não é obrigatório para o Express. Ele evita que algum código depois da resposta tente responder de novo ("headers already sent"). "Alguns bugs" é exatamente esse caso.
- **"Full MVC" não é um termo usual.** O que a aula monta é um monólito com renderização no servidor (SSR) e um template engine, o V do MVC. Ainda não há model nem controller separados. Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **`type="url"` só valida no navegador.** O back-end precisa validar de novo, porque qualquer um pode enviar o formulário sem passar pela página.
- **"Ítens" ou "itens"?** Mayk pergunta: "Eu acho que Itens não tem acento, depois você me ajuda aí". Ele está certo: paroxítonas terminadas em -ens não levam acento.

## Entidades

- [[wiki/entities/mayk-brito]]: instrutor
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento, o Ecoleta e o Launchbase
- [[wiki/entities/nodejs]]: runtime, LTS, REPL e motor do Chrome
- [[wiki/entities/express]]: servidor, rotas e `express.static`
- [[wiki/entities/nunjucks]]: template engine
- [[wiki/entities/vs-code]]: Git Bash como shell padrão, extensões Nunjucks Template e vscode-icons, `settings.json`

Citados sem página: nodemon, Git Bash (Git for Windows), YouTube, Google Chrome, Edge, PHP, Python, Launchbase.

## Conceitos

[[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/endereco-ip]] · [[wiki/concepts/dns]] · [[wiki/concepts/porta-de-rede]] · [[wiki/concepts/metodos-http]] · [[wiki/concepts/requisicao-http]] · [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]] · [[wiki/concepts/http-vs-https]] · [[wiki/concepts/package-json]] · [[wiki/concepts/gerenciador-de-pacotes]] · [[wiki/concepts/json]] · [[wiki/concepts/template-engine]] · [[wiki/concepts/renderizacao-ssr-vs-csr]] · [[wiki/concepts/dry]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/shell-terminal]] · [[wiki/concepts/sqlite]] · [[wiki/concepts/caminho-relativo]] · [[wiki/concepts/git]] · [[wiki/concepts/entender-vs-aprender]] · [[wiki/concepts/pratica-deliberada]]

## Open Questions

- O dia 5 deve trazer o SQLite, o POST do cadastro e a busca real por cidade; os cards de `search-results.html` ainda são fixos.
- Faltam o recebimento do formulário no servidor (corpo do POST) e a página "cadastro concluído". Feitos em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]] (POST para `/savepoint`, `req.body`, SQLite e modal de sucesso).
- A transcrição automática cortou o início: "let's go! [...] dos seus objetivos". A legenda também repete trechos por sobreposição, e as repetições foram mantidas.
- Data provável: 4 de junho de 2020, o quarto dia da NLW #1 `[external, não verificado]`.

## Raw quotes

- "A aula não é feita para te ensinar. É feita para você entender."
- "Acredita que você criou um servidor com apenas três linhas de código?"
- "Lembra que tudo é dado, gente."
- "Os vencedores aqui na programação são aqueles que tem paciência e persistência."
- "Eu não estou mais chamando arquivos, ok? Eu estou chamando rotas."
