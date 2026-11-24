---
type: entity
title: "JavaScript"
aliases: ["JS", "Javascript"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 31
tags: [linguagem, javascript, ecmascript, frontend, backend, web]
skill: lang-dynamic
status: stub
---

# JavaScript

Linguagem de programação da web: a única que os navegadores executam de forma nativa (além do WebAssembly), e também usada fora deles, no servidor ([[wiki/entities/nodejs]]) e no mobile ([[wiki/entities/react-native]]). A especificação se chama [[wiki/concepts/ecmascript|ECMAScript]] (ECMA-262, mantida pelo comitê TC39 da Ecma International); "JavaScript" é o nome das implementações e marca registrada da Oracle. `[external]` https://tc39.es/ecma262/

- **Papel na página:** HTML dá o conteúdo ([[wiki/concepts/html-hipertexto]]), CSS dá o estilo ([[wiki/concepts/css]]), JavaScript dá o comportamento, manipulando o [[wiki/concepts/dom]] e reagindo a eventos.
- **Versões:** ES5 (2009); ES6/ES2015 (classes, módulos, `let`/`const`, arrow functions, promises); depois uma edição por ano (async/await no ES2017). Ver [[wiki/concepts/ecmascript]].
- **Tipos:** dinâmicos ([[wiki/concepts/tipos-primitivos-javascript]]); o [[wiki/entities/typescript]] acrescenta tipos estáticos e compila para JS.
- **Motores:** V8 (Chrome, Node, Deno), SpiderMonkey (Firefox), JavaScriptCore (Safari, Bun).

## No FrontPUSH

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], [[wiki/entities/nasser|Násser]] abre o módulo de JavaScript ES6+: JS é "linguagem de programação em si", ao contrário do HTML e do CSS, e "torna [...] uma página web dinâmica". Cresce porque a mesma linguagem serve no front-end, no back-end e no mobile. Antes do ES6 era "um pouco arcaico", o que explica o sucesso do [[wiki/concepts/jquery]].

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] dá a primeira aula de código do módulo: variáveis, `var`/`let`/`const`, case sensitive, tipos com `typeof`, concatenação, template string e operadores aritméticos.

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], a aula 03 cobre booleanos, truthy/falsy, comparadores, `==` × `===`, `if / else if / else`, `&&`/`||` e `switch case` ([[wiki/concepts/estruturas-condicionais-javascript]]).

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], a aula 04 cobre funções, parâmetro × argumento, `return` e as três formas de declarar, até a arrow com retorno implícito ([[wiki/concepts/arrow-functions]]).

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], a aula 05 trata objetos: literal com atributos e métodos, acesso por ponto, `this`, shorthand, mutação e a ideia de "tudo é objeto" com os métodos herdados de string e número ([[wiki/concepts/objetos-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], a aula 06 cobre arrays (índices, aninhamento, `pop`, `push`, `length`) e as repetições `for` e `while` ([[wiki/concepts/estruturas-de-repeticao-javascript]]).

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], a aula 07 cobre callbacks, `forEach` e `map` ([[wiki/concepts/metodos-de-array-javascript]]).

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], a aula 08 abre o DOM: definição, eventos, `window`/`document` e `querySelector`, `innerText`, `classList`, `id` ([[wiki/concepts/dom]], [[wiki/concepts/window-e-bom]]).

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], a aula 09 cria elementos com `createElement`, `setAttribute`, `createTextNode` e `appendChild` ([[wiki/concepts/criacao-de-elementos-dom]]).

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], a aula 10 cobre eventos: `addEventListener`, callback por referência, `event.target` × `currentTarget`, `classList.toggle`, `keydown` e `resize` ([[wiki/concepts/propagacao-de-eventos-dom]]).

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], a aula 11 abre o JavaScript assíncrono com o JSON: "o J seja de JavaScript", mas o formato serve a qualquer linguagem; `JSON.parse` e `JSON.stringify` ([[wiki/concepts/json]]).

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], a aula 12 define síncrono ("ideia de ordem") e assíncrono (tarefas "no fundo da aplicação") e lista AJAX, Axios, Promises, Fetch e async/await ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], a aula 13 é conceitual: API, HTTP/HTTPS e os métodos GET, POST, PUT, DELETE e HEAD, preparando o AJAX ([[wiki/concepts/api]]).

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a aula 14 é a primeira prática de requisição: `XMLHttpRequest`, `open`, `send`, `onreadystatechange` e `JSON.parse` contra a API do GitHub ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], a aula 15 cobre Promises: `new Promise`, `resolve`, `reject`, `then`, `catch` e o `pending` no console ([[wiki/concepts/promise-javascript]]).

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], a aula 16 troca a Promise com XHR por `axios.get(url).then(...)`, com o Axios carregado por CDN ([[wiki/entities/axios]]).

Em [[wiki/sources/frontpush-modules-js-import-export-default]], a aula 17 cobre ES Modules no navegador: `type="module"`, `export`, `import` e `export default` ([[wiki/concepts/modulos-nodejs]]).

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], a aula 18 cobre desestruturação de objeto, de parâmetro e de array ([[wiki/concepts/desestruturacao-javascript]]).

## Motion para web (FrontPUSH, motion aula 01)

Em [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], JavaScript é uma das três tecnologias do motion para web, e as bibliotecas JavaScript de animação têm módulo próprio no mini curso ([[wiki/concepts/motion-design]]).

## "Consegue mandar no CSS" (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: JS é "linguagem propriamente dita de programação" e, pelo DOM, "consegue mandar no CSS", com condições, laços e matemática. Lapso: diz que JS "já não é só uma linguagem de marcação ou de estilo". Precisão: JS anima também o que o CSS não alcança (canvas, WebGL, física, controle de reprodução) ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## Manipula o SVG pelo DOM (FrontPUSH, propriedades SVG aula 01)

Em [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: como o SVG "possui árvore no DOM", "eu posso manipular ele com JavaScript também" (só inline).

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], curso [[wiki/entities/javascript-ninja|JavaScript Ninja]], de [[wiki/entities/fernando-daciuk|Fernando Daciuk]]: variáveis com `var` e os tipos de dados no REPL do Node.

## No JavaScript Ninja, aula 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], expressões, os quatro aritméticos, `++`/`--` e `+=`, no REPL do Node.

## No JavaScript Ninja, aula 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]], igualdade com e sem tipo, conversão de tipos e os relacionais.

## No JavaScript Ninja, aula 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], funções: declaração, invocação, escopo, `return` e parâmetros.

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], operadores lógicos `&&`, `||` e `!` ([[wiki/concepts/operadores-logicos-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], operadores unários `+`, `-`, `++` e `--`, e o `+` como concatenação ([[wiki/concepts/operadores-unarios-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], estrutura léxica: case sensitive, comentários, literais, identificadores e palavras reservadas ([[wiki/concepts/estrutura-lexica-javascript]], [[wiki/concepts/identificadores-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], `if`, `else` e `else if` ([[wiki/concepts/estruturas-condicionais-javascript]]).

## Key sources

- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, módulo de JavaScript, aula 01: o que é JS e o que é ES6+
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: variáveis, tipos e operadores
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: condicionais
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: funções e arrow functions
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: objetos
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: arrays e loops
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach e map
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: DOM parte 1
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: criar elementos
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: eventos
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: JSON
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: JavaScript assíncrono
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: API e HTTP
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: AJAX com XHR
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: Promises
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: Axios
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: Modules JS
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: desestruturação
- [[wiki/sources/frontpush-intro-modulo-reactjs]]: FrontPUSH, React aula 01: o módulo de JS como base do de React
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: o mínimo de JS para o React; "sempre vai ser a mesma base"
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: bibliotecas JS de animação no mini curso
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: JS manda no CSS; o que só JS faz
- [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 01: JS manipula o SVG inline
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: variáveis e tipos de dados
- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: JavaScript Ninja, aula 02: operadores aritméticos
- [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]]: JavaScript Ninja, aula 03: igualdade e relacionais
- [[wiki/sources/javascript-ninja-funcoes]]: JavaScript Ninja, aula 04: funções
- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: operadores lógicos
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: operadores unários
- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: estrutura léxica
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: instruções condicionais
