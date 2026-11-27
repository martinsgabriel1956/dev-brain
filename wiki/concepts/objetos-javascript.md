---
type: concept
title: "Objetos em JavaScript (literal, this e protótipo)"
aliases: ["objeto", "object literal", "objeto literal", "this", "protótipo", "prototype chain", "cadeia de protótipos", "method shorthand", "autoboxing"]
date_created: 2026-11-16
date_updated: 2026-11-27
source_count: 26
tags: [javascript, objetos, this, prototipo, metodos, es6]
skill: lang-dynamic
status: stub
---

# Objetos em JavaScript

Coleção de propriedades chave → valor. Uma propriedade cujo valor é função se chama **método**. É o único tipo não primitivo; arrays, funções, datas e o próprio `console` são objetos ([[wiki/concepts/tipos-primitivos-javascript]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects

```js
const retangulo = {
  a: 4,
  b: 8,
  area() { return this.a * this.b },        // method shorthand (ES2015)
  perimetro: function () { return 2 * this.a + 2 * this.b },
}
retangulo.area()      // 32
retangulo['a']        // 4, colchetes aceitam chave variável
retangulo.border = 1  // cria propriedade nova, mesmo com const
```

## this

Dentro de um método chamado como `obj.metodo()`, `this` é `obj`. O valor depende da chamada, não do lugar onde a função foi escrita: `const f = retangulo.area; f()` perde o `this`. Arrow functions não têm `this` próprio; como método, pegam o de fora ([[wiki/concepts/arrow-functions]]).

## Protótipo

Todo objeto aponta para outro, o seu protótipo, de onde herda propriedades. `{}` herda de `Object.prototype` (`toString`, `hasOwnProperty`); arrays, de `Array.prototype` (`map`, `filter`). Primitivos não são objetos, mas `'abc'.length` e `(26).toFixed(1)` funcionam porque o motor embrulha o valor num objeto temporário (`String`, `Number`) que usa `String.prototype` ou `Number.prototype` (*autoboxing*). `class` (ES2015) é sintaxe sobre essa cadeia ([[wiki/concepts/programacao-orientada-a-objetos]]).

## Vários objetos do mesmo formato

Um literal descreve um objeto só. Para criar vários: função fábrica (`const criaRetangulo = (a, b) => ({ a, b, area() { return this.a * this.b } })`) ou `class Retangulo { constructor(a, b) {...} }`.

## Utilidades

- `Object.keys`, `Object.values`, `Object.entries` para percorrer.
- Spread (`{ ...obj, a: 2 }`) para copiar com mudança; `Object.freeze` para impedir mutação ([[wiki/concepts/imutabilidade]]).
- Desestruturação: `const { a, b } = retangulo` ([[wiki/concepts/desestruturacao-javascript]]).
- `JSON.stringify` e `JSON.parse` convertem de e para texto ([[wiki/concepts/json]]).

Relacionado: [[wiki/concepts/objeto-vs-estrutura-de-dados]], [[wiki/concepts/abstracao]].

## No FrontPUSH

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], [[wiki/entities/nasser|Násser]] parte da abstração (a caneta tem características e funções), monta `quadrado` e `retangulo` com atributos e métodos, troca o parâmetro por `this.lado`, mostra o *method shorthand* "do JavaScript 6" e muda e acrescenta propriedades depois de criado. O "filho de outro objeto" é a cadeia de protótipos; o "toda variável já é um objeto" ignora que primitivos só são embrulhados no acesso.

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], o array é "um objeto do tipo array" que "herdou muitas funções e propriedades de forma nativa" (`indexOf`, `join`, `map`, `pop`, `push`): aqui o "tudo é objeto" está certo, via `Array.prototype`.

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o "filho de outro objeto" vira literal: um `h1` é `HTMLHeadingElement` → `HTMLElement` → `Element` → `Node` → `EventTarget`, e daí vêm `innerText`, `classList` e `addEventListener`.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], o `event` é o objeto que o navegador entrega ao listener: "sempre coloca no console para você ver quais são as propriedades", porque cada tipo de evento traz propriedades diferentes. `this` aparece como "o próprio evento" e depois, certo, como "o próprio elemento".

Em [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]], a aula 11 apresenta o JSON como "uma anotação de objeto": chave e valor "como se fosse um atributo e um determinado valor". `JSON.parse` devolve um objeto de dados puro (sem métodos) e `JSON.stringify` descarta funções; o objeto `caneta` da [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this|aula 05]] volta como exemplo de `stringify`.

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a instância de `XMLHttpRequest` "virou um objeto [...] onde agora eu posso acessar os seus métodos, seus atributos": o autocomplete mostra o que veio da cadeia de protótipos (`XMLHttpRequest.prototype` → `EventTarget`).

Em [[wiki/sources/frontpush-modules-js-import-export-default]], um objeto `retangulo` com as funções de área e perímetro é exportado como `default`, "porque é muito comum que essas exportações aqui sejam feitas por objetos". Com o shorthand `{ areaRetangulo, perimetroRetangulo }`, as chaves ficam com os nomes completos, e `retangulo.perimetro` seria `undefined`.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], o objeto do evento `mousemove` ("o tanto de características": `clientX`, `pageX`, `offsetX`, `detail`...) é o exemplo de onde tirar só duas propriedades com desestruturação ([[wiki/concepts/desestruturacao-javascript]]).

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], o objeto é "um dos temas mais importantes em JavaScript": literal `{ altura: 1.87, peso: 90 }`, leitura com ponto e escrita pela "própria notação de objeto" (`pessoa.altura = 1.90` muda só aquela propriedade). `pessoa['altura']` também funciona, e é a prova de que arrays "nada mais são do que objetos" ([[wiki/concepts/notacao-de-ponto-e-colchetes]]). Método não aparece.

## No JavaScript Ninja, semana 2, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], o objeto literal "formado pela chave", com "chave, 2 pontos, valor", e o array literal aparecem como literais da linguagem. Literal não é imutável: cada `{}` cria um objeto novo e alterável ([[wiki/concepts/estrutura-lexica-javascript]]).

## No JavaScript Ninja, semana 3, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]], o objeto é "um conjunto de propriedades" que "podem, não, devem receber o nome e um valor", e "todos os outros tipos de dados", além dos primitivos, "são objeto". Literal com chaves, `nome: valor` separados por vírgula, leitura com ponto; serve para "organizar os seus dados" (`pessoa`, `carro`). A função entra como "outro tipo de objeto" que pode ser valor de propriedade ([[wiki/concepts/funcoes-de-primeira-classe]]). Método e `this` ainda não aparecem; o próximo vídeo é "Métodos de objeto".

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], o método entra pela definição: "quando nós atribuímos a uma propriedade de um objeto uma função, nós chamamos essa propriedade de método". Reatribuir a variável (`pessoa = { sexo: 'masculino' }`) troca o objeto inteiro; acrescentar é com ponto (`pessoa.cor = ...`). Os métodos `andar`, `aniversario` (`pessoa.idade++`) e `nomeCompleto` leem `pessoa` pelo nome da variável, não por `this`, o que quebra se a variável for reatribuída ou o método copiado.

## No JavaScript Ninja, semana 3, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]], a revisão por analogia: fora do objeto, variável e função; dentro, "ao invés de variável, você tem uma propriedade" e a função "não se chama função, ele se chama método". A analogia tem limite: propriedade não tem escopo nem declaração e só existe pelo objeto. O desafio da semana 3 é criar objetos, propriedades e métodos.

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], objeto vazio e array vazio entram no `if`: todo objeto é truthy, inclusive `{}`, `[]` e `new Boolean(false)` `[external]`. Para saber se uma lista está vazia, `lista.length === 0`.

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], o desafio 3 volta: `pessoa.sexo` decide o artigo "o"/"a" da frase, agora com ternário. Ao vivo, o objeto `pessoa` ainda não existia no console ("está dizendo que a pessoa não existe") e foi criado com `sexo: 'masculino'`.

## No JavaScript Ninja, semana 5, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]], a função retorna "direto" um objeto literal (`prop1`, `prop2: 'Fernando'` e um método que retorna `prop3`); lê-se com ponto na chamada ou na variável que guardou o retorno. `[external]` Para o método ler `prop3` do próprio objeto, precisa de `this.prop3`.

## No JavaScript Ninja, semana 5, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]], um objeto com `propriedade: 'Fernando'` e `curso` vai como argumento; a função devolve o objeto inteiro ou só `arg.curso`. Chamada sem argumento, dá "não conseguiu ler propriedade curso [de] indefinido" (`TypeError`).

## No JavaScript Ninja, semana 7, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-modulo]], o fecho anuncia que arrays "são objetos disfarçados"; `typeof []` é `'object'`, mas o array tem `length` automático e `Array.prototype` ([[wiki/concepts/array]]).

## No JavaScript Ninja, semana 7, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-propriedade-length]], o array entra como objeto embutido: "como objetos, eles também têm propriedades e métodos", como os que o curso já criava à mão. O objeto `{ bola: 'azul' }` guardado no array é lido com `array[3].bola` ([[wiki/concepts/array]]).

## No JavaScript Ninja, semana 8, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], funções "são um tipo de objeto [...] elas podem ter propriedades e elas podem ter métodos também", com alguns "embutidos" (built-in). O exemplo é `name`, que a aula chama de método mas é propriedade somente leitura (`writable: false`, verificado).

## No JavaScript Ninja, semana 8, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]], o objeto literal é a base do paralelo com funções: "você usa simplesmente as chaves", e "o formato final do objeto, exatamente como ele é apresentado [...] na linguagem em si, é objeto literal". Uma função pode devolver o objeto direto ou guardá-lo numa `var` antes: "o resultado é o mesmo". `[external]` Cada chamada cria um objeto novo (`f() === f()` dá `false`). Construtores de objeto ficam "mais para frente".

## No JavaScript Ninja, semana 8, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]], o objeto `car` com `color: 'yellow'` vai como argumento para uma função que devolve `car.color`. Erro ao vivo: "coloquei um ponto e vírgula dentro do objeto [...] dentro do objeto não pode ter". `[external]` `{ color: 'yellow'; }` dá `SyntaxError: Unexpected token ';'` (verificado): propriedades se separam por vírgula.

## No JavaScript Ninja, semana 9, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-iife]], uma propriedade cujo valor é uma função anônima é uma das formas de invocar uma função sem nome (`objeto.prop()` dá 3). `[external]` Desde o ES2015, essa função recebe `name` igual ao da propriedade (verificado).

## No JavaScript Ninja, semana 10, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-wrapper-objects]], o critério de objeto é "se esse cara, ele tem propriedades e métodos". Construtores são "objetos, ou funções [...] que criam novos objetos", com `new`; `new String('Daciuk')` é objeto, com `valueOf()` para o primitivo. Detalhe em [[wiki/concepts/wrapper-objects-javascript]].

## No JavaScript Ninja, semana 10, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-typeof]], "qualquer outro objeto que não seja uma função" dá `'object'` no [[wiki/concepts/typeof-javascript|typeof]], inclusive array e `null`; por isso, "não testar o objeto usando o typeof". Para objeto não nulo: `x !== null && typeof x === 'object'` `[external]`.

## Key sources

- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: literal, ponto, this, method shorthand, mutação, "filho de outro objeto"
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: array como objeto que herda de Array.prototype
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: elementos do DOM e a cadeia de protótipos
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: event como objeto a explorar
- [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]: FrontPUSH, JavaScript aula 11: JSON como notação de objeto
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: instância herdando métodos
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: objeto como export default
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: evento como objeto desestruturado
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: objetos como primeiro item do checklist; "praticamente tudo [...] é objeto"
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: literal, ponto para ler e escrever, colchetes com string
- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: objeto e array literais
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: conjunto de propriedades; tudo que não é primitivo; função como objeto
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: método como propriedade-função; reatribuir × acrescentar; métodos sem this
- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: JavaScript Ninja, semana 3, vídeo 03: propriedade como variável dentro do objeto, método como função; desafio 3
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: objeto e array vazios são truthy
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: `pessoa.sexo` no ternário
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: função retorna objeto literal com propriedades e método
- [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 02: objeto como argumento; devolver o objeto ou `arg.curso`
- [[wiki/sources/javascript-ninja-operador-modulo]]: JavaScript Ninja, semana 7, vídeo 01: arrays como "objetos disfarçados"
- [[wiki/sources/javascript-ninja-arrays-propriedade-length]]: JavaScript Ninja, semana 7, vídeo 02: array como objeto embutido; objeto dentro de array
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: função como objeto; name embutido
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: JavaScript Ninja, semana 8, vídeo 02: objeto literal; função que retorna objeto
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: JavaScript Ninja, semana 8, vídeo 04: objeto como argumento; ; dentro do literal é SyntaxError
- [[wiki/sources/javascript-ninja-iife]]: JavaScript Ninja, semana 9, vídeo 03: função anônima como propriedade, invocada pelo objeto
- [[wiki/sources/javascript-ninja-wrapper-objects]]: JavaScript Ninja, semana 10, vídeo 01: objeto = propriedades e métodos; construtores com new
- [[wiki/sources/javascript-ninja-typeof]]: JavaScript Ninja, semana 10, vídeo 02: typeof de objeto, array e null é object
