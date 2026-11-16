---
type: source
title: "JStack, aula 04: criando o servidor HTTP"
aliases: ["JStack aula 04", "servidor HTTP com Node puro", "http.createServer"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, http, createserver, writehead, res-end, listen, porta, localhost, status-code, content-type, charset, express, framework, nodemon, node-watch, src, eslint, prettier, editorconfig, jstack, iniciante, tech-mentor-backend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-criando-o-servidor-http.md"
source_url: ""
author: "Mateus Silva"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 04: criando o servidor HTTP

## TL;DR

Quarta aula (cerca de 6 min) do [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]]. Começa o primeiro projeto, uma API REST em [[wiki/entities/nodejs|Node]] "puro", antes do [[wiki/entities/express|Express]], que "não implementa nada de novo dentro do Node. Ele é só um framework". A aula cobre:

1. **`src/`.** O código vai em `src/index.js` porque a raiz "começa a ficar muito poluída" com configs de git, ESLint, Prettier e EditorConfig.
2. **Servidor.** `const http = require('http')` e `http.createServer((request, response) => {...})`, os mesmos request e response "que a gente viu lá na aula teórica".
3. **Resposta.** `response.writeHead(200, { 'Content-Type': 'text/html' })` e `response.end('<h1>Hello World</h1>')`.
4. **Subir.** `server.listen(3000, () => console.log('... Server started at http://localhost:3000'))` e `node src/index.js`.
5. **Sem reload.** Trocar para "olá mundo" e atualizar o navegador não muda nada: "o node não fica ouvindo por alterações". É preciso Ctrl+C e rodar de novo. O nodemon automatiza, mas fica de fora para mostrar "o node raiz".

O que a aula não diz está em "Tensões e precisões". O `node --watch`, nativo e estável desde o Node 22, recarrega sem pacote externo. E `text/html` sem `charset` pode mostrar o "olá" como "olÃ¡". O handler também responde igual a qualquer método e caminho, inclusive ao `/favicon.ico` que o navegador pede sozinho.

## Key Claims

### Por que Node puro

- **Express é açúcar.** "Ele é só um framework, ou seja, ele só facilita o uso dos recursos que já estão presentes dentro do Node. [...] Tudo o que a gente faz com o Express a gente conseguiria fazer também com o Node puro. Obviamente, com mais trabalho." Ver [[wiki/concepts/framework-web]] e [[wiki/entities/express]].
- **Escopo.** "A gente não vai desenvolver uma mega API super complexa", só mostrar "como trabalhar com o módulo HTTP do Node".

### A pasta src

- **Organização.** A raiz junta "arquivos e pastas de configuração de git, de ESLint, de Prettier, de editor config", e "misturar esses arquivos de configuração com o código da nossa aplicação [...] fica um negócio muito bagunçado". Por isso o código vai para `src/`, e o nome do arquivo é livre.

### createServer, request e response

- **Importar.** "É só passar o require e o nome do pacote, do módulo." Ver [[wiki/concepts/modulos-nodejs]].
- **Três métodos no IntelliSense.** `createServer` para criar o servidor; `get` e `request` "servem para fazer requisições HTTP", e ficam de fora.
- **Handler.** Recebe uma função, "na sintaxe de function normal ou [...] arrow function que é como eu prefiro", com `(request, response)`: "exatamente aqueles request e response que a gente viu lá na aula teórica" ([[wiki/sources/jstack-http-e-apis-rest]]).

### writeHead e end

- **`writeHead`.** O primeiro argumento é o status code. "Como aqui a gente não tem regra de negócio nenhuma [...] a requisição sempre vai ser bem sucedida, logo a gente usa o código 200." O segundo é um objeto com "todos os headers que a gente quer", aqui só `Content-Type: text/html`. Ver [[wiki/concepts/http-status-code]] e [[wiki/concepts/http-headers]].
- **`end`.** "A gente passa qual é o HTML [...] que a gente quer enviar dentro do nosso corpo": `<h1>Hello World</h1>`.

### listen

- **Criar não é subir.** "A gente só criou o servidor, a gente precisa erguê-lo agora, [...] fazer ele ficar ouvindo alguma porta." `server.listen(3000, callback)`, com a porta à escolha e um [[wiki/concepts/callback-javascript|callback]] que loga "server started at http://localhost:3000", com emoji "só para não perder o costume". Ver [[wiki/concepts/porta-de-rede]].
- **Rodar.** `node src/index.js`; Cmd+clique no link do terminal abre o "Hello World".

### O Node não recarrega o código

- **Demonstração.** Troca para "olá mundo", salva, atualiza o navegador e "ele continuou com o hello world", porque "o código que está executando [...] é o código que estava no momento em que a gente executou o comando". "Ctrl C aqui para parar o servidor, executa de novo." Na fala, ele diz "hello world" de novo no final, mas é o "olá mundo" que aparece.
- **nodemon.** "Fica ouvindo alterações nos nossos códigos e [...] para o servidor e sobe de novo." Fica de fora porque "o intuito desse módulo aqui é te mostrar como é que o node funciona em sua essência, o node raiz"; os pacotes entram no próximo capítulo. Ver [[wiki/concepts/setup-live-reload-debug-testes]].
- **Dica.** Se uma alteração "acaba não surtindo efeito, pode ser que seja isso".

## Tensões e precisões

- **`node --watch` é Node puro.** Desde o Node 22.0 (e 20.13) o watch mode nativo é estável: `node --watch src/index.js` reinicia ao salvar, sem instalar nada `[skill: lang-dynamic]` `[external]` https://nodejs.org/api/cli.html#--watch. Então dá para cumprir o objetivo de "não usar pacotes" sem reiniciar à mão. O nodemon segue útil para casos com mais configuração.
- **Falta `charset`.** `Content-Type: text/html` sem `charset=utf-8` deixa o navegador adivinhar a codificação. O "olá mundo" da própria demonstração pode aparecer como "olÃ¡ mundo". O certo é `text/html; charset=utf-8` ou `<meta charset="utf-8">` no HTML. Ver [[wiki/concepts/charset]] e [[wiki/concepts/utf-8]].
- **Um handler para tudo.** O callback do `createServer` roda para qualquer método e qualquer caminho: `POST /qualquer-coisa` também recebe 200 e o `<h1>`. O navegador ainda pede `/favicon.ico` a cada carregamento, então cada F5 chama o handler duas vezes. Roteamento por `request.method` e `request.url` (ou um framework) resolve; é o próximo passo natural do curso.
- **"Sempre bem sucedida" é verdade só porque não há nada que possa falhar.** Com leitura de arquivo ou banco, um erro não tratado dentro do handler derruba o processo inteiro. Ver [[wiki/concepts/error-handling-estruturado]].
- **Por que o processo não termina.** O `listen` registra um handle ativo na [[wiki/entities/libuv|libuv]], e o [[wiki/concepts/event-loop-performance-js|event loop]] só sai quando não há mais handles. Por isso `node src/index.js` fica rodando, ao contrário dos scripts da aula 03 ([[wiki/sources/jstack-como-funciona-o-nodejs]]).
- **`listen(3000)` escuta em todas as interfaces.** Sem host, o Node escuta em `::`/`0.0.0.0`, e outras máquinas da rede conseguem acessar. Para só a máquina local: `listen(3000, '127.0.0.1')` `[external]` https://nodejs.org/api/net.html#serverlistenport-host-backlog-callback.
- **O módulo `http` tem mais que três métodos.** `createServer`, `get` e `request` são as funções principais, mas também há `METHODS`, `STATUS_CODES`, `Agent`, `Server` e outros. E o cliente HTTP moderno do Node é o `fetch` global (undici), não `http.get`.
- **"O Express não implementa nada de novo."** Não expõe recurso novo do runtime, mas implementa em JavaScript roteamento, middleware, parsing de body e de query, e respostas como `res.json`. É o "mais trabalho" que a aula admite.

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor
- [[wiki/entities/nodejs]]: módulo `http`, `node src/index.js`
- [[wiki/entities/express]]: framework que vem depois
- [[wiki/entities/libuv]]: o handle do `listen` mantém o processo vivo

## Concepts

- [[wiki/concepts/framework-web]]
- [[wiki/concepts/modulos-nodejs]]: `require('http')`
- [[wiki/concepts/http-status-code]]: 200 no `writeHead`
- [[wiki/concepts/http-headers]]: objeto de headers no `writeHead`
- [[wiki/concepts/charset]]: `text/html` sem charset
- [[wiki/concepts/porta-de-rede]]: `listen(3000)`
- [[wiki/concepts/callback-javascript]]: callback do `listen` e do `createServer`
- [[wiki/concepts/setup-live-reload-debug-testes]]: nodemon × `node --watch`
- [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]
- [[wiki/concepts/event-loop-performance-js]]: processo vivo enquanto há handle

## Open Questions

- A próxima aula roteia por `request.url` e `request.method` com `if` ou com um objeto de rotas?
- O curso vai usar `res.setHeader` + `res.statusCode` em algum momento, ou só `writeHead`?

## Raw quotes

> "O Express não implementa nada de novo dentro do Node. Ele é só um framework."

> "O node não fica ouvindo por alterações aqui dentro do nosso código."
