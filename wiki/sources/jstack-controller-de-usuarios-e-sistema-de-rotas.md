---
type: source
title: "JStack, aula 06: controller de usuários e sistema de rotas"
aliases: ["JStack aula 06", "UserController e routes.js", "sistema de rotas com Node puro"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, http, roteamento, routes, handler, controller, crud, regra-de-negocio, separation-of-concerns, array-find, referencia-de-funcao, this, require-caminho-relativo, mvc, jstack, iniciante, lang-dynamic]
skill: tech-mentor-backend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-controller-de-usuarios-e-sistema-de-rotas.md"
source_url: ""
author: "Mateus Silva"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 06: controller de usuários e sistema de rotas

## TL;DR

Sexta aula (cerca de 7 min) do [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]]. Refatora o `if` da [[wiki/sources/jstack-criando-a-primeira-rota-da-api|aula 05]] para resolver dois problemas: cada rota nova pediria outra condicional, e "a regra de negócio [...] está toda aqui dentro".

1. **Controller.** `src/controllers/UserController.js` exporta um objeto (classes "a partir do próximo módulo") com `listUsers(request, response)`, que importa o mock e responde o JSON. Para ele, o controller "é o responsável por armazenar toda a regra de negócio" e guarda as funções do [[wiki/concepts/crud]] de usuários. Ver [[wiki/concepts/controller]].
2. **Caminho do `require`.** Ao mover o código, `./mocks/users` quebra, e passa a ser `../mocks/users`, "porque agora a gente está dentro de controllers".
3. **Tabela de rotas.** `src/routes.js` exporta um array de `{ endpoint, method, handler }`, com `handler: UserController.listUsers`: "eu não estou executando a função [...] só estou passando a referência".
4. **Despacho.** No `index.js`, `const route = routes.find((routeObject) => routeObject.endpoint === request.url && routeObject.method === request.method)`. Se achar, `route.handler(request, response)`; senão, o 404 "Cannot GET". Ver [[wiki/concepts/roteamento-http]].
5. **Ganho.** Rota nova é só mais um objeto: `/produtos` apontando para `listUsers` passa a funcionar, sem "aquele mundaréu de if else".

O roteamento evolui bem, do `if` para uma tabela de rotas. O ponto fraco é chamar o controller de lugar de "toda a regra de negócio": na arquitetura em camadas ele é a borda HTTP, e regras como "e-mail já cadastrado" vão para um service ou use case. Também ficam pendentes a perda de `this` quando o handler virar método de classe e o `/users/:id`, que a comparação exata não suporta. Ver "Tensões e precisões".

## Key Claims

### Os dois problemas

- **Rotas.** "Cada nova rota [...] a gente vai ter que fazer essa condicional de URL e método. Então, assim, imagina como é que vai ficar esse negócio."
- **Regra de negócio no `index`.** Hoje é simples, mas ao cadastrar usuário "a gente precisaria verificar se o email [...] já não está inserido no banco de dados", e "isso aqui vai ficando muito grande e insustentável". Ver [[wiki/concepts/regra-de-negocio]] e [[wiki/concepts/separation-of-concerns]].

### Controller e CRUD

- **Definição dada.** "Um controlador é o responsável por armazenar toda a regra de negócio da nossa aplicação." Ver [[wiki/concepts/controller]].
- **CRUD.** "Create, read, update e delete": criar usuário, ler todos ou um "a partir do ID", atualizar e remover. "Todas as funções que vão armazenar essas regras de negócio aqui, elas ficam dentro do nosso Controller." Ver [[wiki/concepts/crud]].
- **Objeto por enquanto.** `module.exports = { listUsers(request, response) { ... } }`; "a gente vai trabalhar com classes a partir do próximo módulo".
- **Mover o mock.** O `require` dos usuários vai para o controller. Rodar dá erro em `./mocks`: "a gente tem que voltar uma pasta, porque agora a gente está dentro de controllers". Ver [[wiki/concepts/modulos-nodejs]].

### routes.js

- **Array de rotas.** `src/routes.js` exporta um array, e "cada um desses objetos vai representar uma rota da nossa API".
- **Identificação.** "As duas propriedades que identificam uma rota [...] são o endpoint, [...] barra users, e o método, para a gente identificar qual é a ação". Ele antecipa `POST /users` e "o get para pegar o usuário por ID".
- **Handler.** "A função que eu quero executar toda vez que essa rota for chamada": `handler: UserController.listUsers`.
- **Referência, não chamada.** "Preste atenção, eu não estou executando a função, tá? Eu só estou passando a referência da função", como se depois fizesse `routes[0].handler(request, response)`. Ver [[wiki/concepts/callback-javascript]] e [[wiki/concepts/funcoes-javascript]].

### Encontrando a rota

- **`find`.** `routes.find(...)` "para procurar um elemento dentro da minha lista"; a função recebe cada item (`routeObject`) numa "iteração, passando item por item". Ver [[wiki/concepts/metodos-de-array-javascript]].
- **Condição.** `routeObject.endpoint === request.url && routeObject.method === request.method` quer dizer que "a rota que o usuário está tentando bater, a gente registrou aqui dentro do nosso array de rotas".
- **Despacho e fallback.** Se existe, `route.handler(request, response)`; se não, "esse 404 que a gente já tinha".
- **Demonstração.** `/produtos` dá "Cannot GET" até ganhar uma entrada no array; depois funciona (chamando `listUser[s]`, só de exemplo). "Fica muito mais fácil, né?"

## Tensões e precisões

- **Controller não é "toda a regra de negócio".** Em MVC e na arquitetura em camadas, o controller é o adaptador de entrada: lê a request, chama a lógica e formata a response. A regra (e-mail único, cálculo de preço, permissões) fica num service ou use case e no domínio, e não deve depender de `request`/`response`; assim dá para testar sem HTTP e reaproveitar na CLI ou numa fila `[skill: tech-mentor-backend]` (`architecture-foundations.md`: controllers como *primary adapters*). O próprio exemplo de "verificar se o email já está no banco" é de service. Juntar tudo no controller é o *fat controller*. Ver [[wiki/concepts/controller]], [[wiki/concepts/camada-de-aplicacao-vs-modelo]] e [[wiki/concepts/arquitetura-em-3-camadas]].
- **A referência perde o `this`.** Passar `UserController.listUsers` funciona porque o objeto literal não usa `this`. Com classes (anunciadas para o próximo módulo), um método que use `this.algo` vai receber `this === undefined` quando chamado como `route.handler(...)`. A saída é `.bind(controller)`, arrow function como propriedade de classe ou envolver numa arrow: `handler: (req, res) => controller.listUsers(req, res)`. Ver [[wiki/concepts/funcoes-javascript]].
- **Comparação exata não suporta `/users/:id`.** `endpoint === request.url` não casa parâmetros de caminho, e ainda quebra com query string e barra final ([[wiki/sources/jstack-criando-a-primeira-rota-da-api]]). A rota "get para pegar o usuário por ID" vai exigir regex, split por `/` ou `URLPattern`. Ver [[wiki/concepts/roteamento-http]].
- **Ainda 404 para método errado.** `POST /users` continua caindo em "não encontrado"; com a tabela, dá para distinguir: caminho existe com outro método = 405.
- **`require` é relativo ao arquivo, não ao terminal.** Por isso `../mocks` funciona de qualquer pasta onde se rode `node`. Já `fs.readFile('./x')` é relativo ao diretório de trabalho (cwd), e por isso se usa `__dirname` ([[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]). Ver [[wiki/concepts/caminho-relativo]].
- **Nome de arquivo × nome da variável.** O arquivo é `UserController.js` e o `require` usa `userController`. No macOS e no Windows (sistemas de arquivos que ignoram maiúsculas) funciona; no Linux, como num servidor ou container, `require('./controllers/userController')` não acha `UserController.js`.
- **Busca linear.** `find` percorre o array a cada requisição. Com dezenas de rotas é irrelevante; roteadores de framework usam árvores para casar em tempo proporcional ao tamanho do caminho.

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor
- [[wiki/entities/nodejs]]: `require` relativo, handler do `createServer`

## Concepts

- [[wiki/concepts/controller]]
- [[wiki/concepts/crud]]
- [[wiki/concepts/roteamento-http]]: tabela de rotas com `find`
- [[wiki/concepts/regra-de-negocio]]
- [[wiki/concepts/separation-of-concerns]]
- [[wiki/concepts/camada-de-aplicacao-vs-modelo]]
- [[wiki/concepts/arquitetura-em-3-camadas]]
- [[wiki/concepts/metodos-de-array-javascript]]: `find`
- [[wiki/concepts/callback-javascript]]: passar a referência do handler
- [[wiki/concepts/funcoes-javascript]]: referência × execução; `this`
- [[wiki/concepts/modulos-nodejs]]: `require('../mocks/users')`
- [[wiki/concepts/caminho-relativo]]

## Open Questions

- Quando o curso passar a classes, os handlers vão usar `bind` ou arrow functions?
- Vai aparecer uma camada de service/repository, ou a regra continua no controller?
- Como `GET /users/:id` vai ser casado nessa tabela de rotas?

## Raw quotes

> "Eu não estou executando a função, tá? Eu só estou passando a referência da função aqui."

> "Um controlador é o responsável por armazenar toda a regra de negócio da nossa aplicação."

> "E a gente não precisa mais ficar fazendo aquele mundaréu de if else."
