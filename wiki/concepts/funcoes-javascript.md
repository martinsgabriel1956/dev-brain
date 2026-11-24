---
type: concept
title: "Funções em JavaScript"
aliases: ["função", "function", "arrow function", "função anônima", "callback", "argumento", "parâmetro", "return"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 24
tags: [javascript, funcoes, arrow-function, callback, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# Funções em JavaScript

Bloco de código com nome (ou anônimo) que recebe parâmetros e pode devolver um valor com `return`; sem `return`, devolve `undefined`. Em JavaScript funções são valores: podem ser guardadas em variáveis, passadas como argumento (*callback*) e retornadas. A *arrow function* (`(x) => x * 2`) é a forma curta, com `this` léxico. Ver [[wiki/concepts/logica-de-programacao]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]:

- **Para que serve:** "atalhos pra executar um monte de código", "reuso de código". Registrar (`function sayMyName(name) {...}`) é diferente de executar (`sayMyName("Douglas")`).
- **Argumento:** entra como pela "boca de um funil" e vira uma variável dentro da função; "todos esses valores que a gente vai passando dentro de função chama-se argumento ou parâmetro".
- **Anônima e arrow:** `function (res) {...}` dentro do `then` e a versão curta `res => res.json()`: um parâmetro dispensa parênteses, uma expressão dispensa `return` e chaves.
- **Por referência:** `addEventListener("change", getCities)` sem parênteses, porque "se eu abrir e fechar ela aqui, eu estou falando para executar ela imediatamente". Ver [[wiki/concepts/event-listener-javascript]].
- **Métodos:** função dentro de objeto (`pessoa.correr()`); sem `return`, `document.write(pessoa.correr())` escreve "undefined".

## Precisões

- Parâmetro é o nome na declaração; argumento é o valor passado na chamada. A aula usa os dois como sinônimos.
- Arrow functions não têm `this` próprio nem `arguments`; não servem como método que depende de `this` `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] passa uma função anônima para `findIndex` e `filter` e mostra a forma curta, `item => item == itemId`, sem chaves nem `return`. Depois volta à versão explícita: "eu acho legal para a gente que está começando deixar ele de uma maneira muito mais explícita". Para o ouvidor de clique, registra `handleSelectedItem` por referência.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] conta a analogia da irmã: a função é "uma caixinha mágica" que recebe um argumento e "vai contra-argumentar te devolvendo alguma resposta". Lembra que a arrow function com dois parâmetros precisa de parênteses (`(req, res) =>`), e recomenda `return res.render(...)`.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] define método ("função, quando [...] ela reside dentro de um objeto a gente dá o nome método") e mostra `new` com constructor ou classe. Diferencia passar uma função por referência (`afterInsertData`) de executá-la (`afterInsertData()`). Explica que com `this` "nós não usamos a arrow function". Ver [[wiki/concepts/callback-javascript]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: componentes como arrow functions em `const`, funções dentro de componentes (`handleButtonClick`) e retorno implícito com parênteses no `map`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], Diego diz que "map é uma palavra reservada do JavaScript". Não é: `map` é método de array e `Map` é um global.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], função é "uma caixinha mágica" que recebe algo e devolve algo, como o pedal do acelerador. `function cloneField() {}` é declarada com nome; dentro do `forEach`, uma função anônima recebe "o field do momento".

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], `require('express')` devolve uma função, e `express()` a executa; a arrow function `(req, res) => {}` é "uma função curta"; `getSubject(subjectNumber)` faz `+subjectNumber - 1` e `return subjects[arrayPosition]`. "Função é o grande lance da programação."

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], funções `async` que retornam promessas, `return db` dentro do `then` para encadear, `module.exports = async function (db, {...})` e `convertHoursToMinutes`, testada antes no console do navegador. A arrow function aparece no `then` e no `map`.

## Funções no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-funcoes-sass]]: "um bloco que retorna sempre um valor", "na grande maioria das linguagens"; parâmetros com padrão (`$total: 12`) como no JS; concatenação de strings com `+`, "muito parecido com o JavaScript". Ver [[wiki/concepts/funcoes-sass]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], as arrow functions entram na lista de novidades do ES6+ que o módulo vai "esmiuçar". `[external]` São do ES2015 ([[wiki/concepts/ecmascript]]).

## No JStack, aula 03

Em [[wiki/sources/jstack-o-que-sao-modulos]], `module.exports` pode ser a própria função (`module.exports = printName`), e `exports.printName = (name) => ...` declara e exporta de uma vez, "um pouco mais enxuto" com arrow function. Chamar a função sem importá-la dá `is not defined`; importar sem exportar dá `is not a function`.

## No FrontPUSH, módulo de JavaScript, aula 04 (Násser)

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], [[wiki/entities/nasser|Násser]]: funções são "blocos de códigos que são reaproveitados" (`areaRetangulo` num programa de polígonos); "quando eu escrevo aqui é parâmetro, quando eu passo diretamente é argumento", a distinção que a NLW #1 não fez; `helloWorld` "não me retorna nada" (devolve `undefined`); e `return a * b` só aparece no console dentro de um `console.log`. Declaração, expressão e arrow são "exatamente a mesma coisa" na aula, o que não vale para hoisting e `this` ([[wiki/concepts/arrow-functions]]). A "regrinha" de que o tipo que entra é o tipo que sai não é regra; a boa prática é devolver sempre o mesmo tipo.

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], funções como valor de propriedade (métodos), o *method shorthand* `area() {}` "do JavaScript 6", e a regra "sempre que for uma função, eu preciso executar": `quadrado.area` mostra a função, `quadrado.area(4)` a executa. No console, a função exibe `[[Scopes]]`, `arguments` e `length`, sinal de que também é objeto.

## No JStack, aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: função como valor numa propriedade (`handler: UserController.listUsers`), chamada depois. Cuidado anunciado pela própria aula (classes no próximo módulo): método de classe passado como referência perde o `this`; `bind`, arrow function como propriedade ou um wrapper `(req, res) => c.listUsers(req, res)` resolvem.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], referência × execução no listener: `addEventListener('click', callback)` passa a função; `callback()` a executaria na hora.

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], `minhaPromise` é uma função atribuída a variável que devolve `new Promise(function (resolve, reject) {...})`: função que recebe função, dentro de função. "É muito comum isso em JavaScript."

Em [[wiki/sources/frontpush-modules-js-import-export-default]], as funções `areaRetangulo`, `perimetroRetangulo` e `upperName` saem do `app.js` para módulos próprios com `export function`.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], a desestruturação vai para a lista de parâmetros: `function mouseMove({ clientX, clientY })`. Chamada sem argumento, uma função assim lança `TypeError`.

## No JavaScript Ninja, aula 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-funcoes]], função é "um bloco de código JavaScript nomeado e que pode ser invocado usando o operador abre e fecha parênteses". Mostra no REPL: `soma()` executa, `soma` mostra a função sem executar; sem `return`, `undefined`; funções "criam um escopo" ([[wiki/concepts/escopo-javascript]]); `return` devolve valor (`y + cinco()` = 9); `soma(x, y)` sem argumentos dá `NaN`. Chama de "argumentos" os parâmetros da declaração e não mostra função anônima.

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], "o function, na verdade, ele é um tipo de objeto", de primeira classe porque pode ser atribuído a variáveis. Mostra a função anônima que faltava na aula 04: `var f = function () { return '...' }`, invocada pelo nome da variável; "não é obrigatório" nome quando a função é atribuída ([[wiki/concepts/funcoes-de-primeira-classe]]). `[external]` Desde o ES2015, ela herda o nome da variável em `f.name`.

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], a função vira método ao ser valor de propriedade. `aniversario` muda estado e "não vai retornar nada" (devolve `undefined`); `nomeCompleto` "não vai modificar nada. Simplesmente vou retornar": a distinção comando × consulta, dita pela aula.

## No JavaScript Ninja, semana 3, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]], a função criada dentro do objeto "acaba se tornando o método desse objeto"; `pessoa.andar` sem parênteses é só a função, e "eu vou precisar invocar ela para ver o resultado".

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: registrar x executar, argumento, anônima, arrow, referência
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: callback de findIndex/filter; arrow enxuta x explícita
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: caixinha mágica; arrow com dois parâmetros
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: método, new, referência x execução, this
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: arrow functions como componentes; retorno implícito
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: "map é reservada" (não é)
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: caixinha mágica; função anônima no forEach
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: arrow function, return, getSubject
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: async function, return no then
- [[wiki/sources/frontpush-funcoes-sass]]: paralelo com funções do Sass
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: arrow functions como novidade do ES6
- [[wiki/sources/jstack-o-que-sao-modulos]]: função exportada; arrow function em exports.printName
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: parâmetro × argumento, return, três formas
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: métodos, shorthand e referência × execução
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: referência de função; this em métodos de classe
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: passar a função, não o resultado
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: função que devolve Promise
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: funções exportadas
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: desestruturação no parâmetro
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: function, const + function e const + arrow como três formas de componente
- [[wiki/sources/javascript-ninja-funcoes]]: JavaScript Ninja, aula 04: declarar, invocar, escopo, return, parâmetros e NaN
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: função como objeto de primeira classe; função anônima em variável
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: função como método; com efeito × só retorno
- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: JavaScript Ninja, semana 3, vídeo 03: função dentro do objeto vira método
