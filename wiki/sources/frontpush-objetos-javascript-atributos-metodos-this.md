---
type: source
title: "Objetos em JavaScript: atributos, métodos e this (FrontPUSH)"
aliases: ["FrontPUSH objetos", "módulo de JavaScript ES6, aula 05", "Objetos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, objetos, orientacao-a-objetos, abstracao, atributos, metodos, this, prototipo, string, number, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-objetos-javascript-atributos-metodos-this.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Objetos em JavaScript (FrontPUSH)

## TL;DR

Aula 05 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (diz o nome). "De longe é uma das aulas mais importantes": "praticamente tudo em JavaScript é objeto", e "um dos segredos de JavaScript é justamente conhecer bons objetos que já estão criados".

- **Abstração:** programar é "resolver problemas" do mundo real (o app de banco que evita a fila), e a abstração transforma coisas reais em objetos. A caneta tem características (azul, comprimento, corpo triangular, ponta) e funções (rabiscar, traço fino ou grosso). Ver [[wiki/concepts/abstracao]] e [[wiki/concepts/programacao-orientada-a-objetos]].
- **Objeto:** "um conjunto de variáveis [...] atributos [...] e funções, que eles se transformam em métodos". Nasce com `{}`; `typeof` dá `object`. Ver [[wiki/concepts/objetos-javascript]].
- **Quadrado:** `lado: 4`, mais `area` e `perimetro` com `function (lado)`, separados por vírgula. Acesso com ponto: `quadrado.lado` dá 4, `quadrado.area` mostra a função, e `quadrado.area(4)` executa ("sempre que for uma função, eu preciso executar").
- **`this`:** `this.lado` usa "a variável que já existe dentro desse objeto"; com ele, os métodos dispensam parâmetro.
- **Retângulo:** `a: 4, b: 8`, `area` = `this.a * this.b` (32) e perímetro 24. "Outra notação [...] do JavaScript 6": `area() {}` sem `function`.
- **Mutável:** `retangulo.a = 2; retangulo.b = 4` muda a área para 8, e `retangulo.border = 1` cria um atributo novo.
- **Tudo é objeto:** um objeto "já é filho de outro objeto"; uma string "já carrega funções" (`length`, `indexOf`, `matchAll`), e um número tem `toFixed`, `toString`. No autocomplete do editor, azul é propriedade e roxo é método. Isso "é o que a gente chama de API".

## Key Claims

### Programação e abstração

- "Programação é um jeito de resolver problemas [...] São problemas da vida real." Aplicativos de banco servem para "diminuir o problema que era a gente ir presencialmente aos bancos, perder tempo em filas".
- "Muita coisa precisou ser abstraída do mundo real para o mundo computacional [...] a gente faz essa abstração transformando em objetos."
- Caneta: características (azul; comprimento; diâmetro, "porque ele não é exatamente redondo [...] ele é triangular"; ponta grossa ou fina) e funções ("rabiscar", traço fino ou grosso, desenhar círculos, figuras, letras). "Características que viram atributos ou propriedades e funções que a gente transforma em métodos."
- "Um objeto é um conjunto de variáveis que eu posso chamar de atributos, que são características, variáveis e funções, que eles se transformam em métodos."

### Literal, acesso e execução

- "Lembra como é que eu transformo uma variável em um objeto? Simplesmente eu faço essa anotação [...] a gente abre e fecha chaves." `typeof quadrado` mostra `object`.
- "Tem a propriedade lado, então ele tem quatro lados." `area: function (lado) { return lado * lado }`; `perimetro: function (lado) { return 4 * lado }`.
- "Sempre eu separo por vírgula [...] como essa aqui é a última, não foi necessário."
- "Eu declaro primeiro o nome do objeto e eu acesso essas características por meio do ponto." `console.log(quadrado)` mostra o objeto inteiro: lado 4 e as funções marcadas "com um F", com "escopo, argumento, length" que não foram declarados.
- `quadrado.area` sem parênteses mostra a função: "Porque eu não coloquei nada, não executei a função [...] Colocando parênteses." `area(4)` e `perimetro(4)` dão 16.

### this

- "O objeto pode utilizar nas suas funções os seus próprios atributos [...] por mais que eu tenha escrito lado aqui, é diferente desse lado, porque esse lado aqui é o parâmetro da função, não é a variável lado que foi criada aqui."
- "Eu simplesmente vou utilizar a clausulazinha this [...] quando eu faço this.lado, o que eu estou dizendo para o JavaScript? Utilize a variável que já existe dentro desse objeto."
- `perimetro` vira `this.lado * 4`, "sendo que é a própria quantidade de lados", e `area` vira `this.lado * this.lado`: "a área nesse caso é igual ao perímetro" (16).

### Retângulo, notação curta e mutação

- `retangulo = { a: 4, b: 8, area: this.a * this.b, perimetro: 2a + 2b }`: área 32, perímetro 24.
- "Uma outra notação, porque isso já vem com o JavaScript 6 também [...] simplesmente tirando a notação function [...] funciona exatamente da mesma forma."
- A objeção "está muito fixo" responde-se com mutação: "você pode acessar as variáveis e os atributos e modificar, adicionar novas variáveis". `a = 2`, `b = 4` → área 8, perímetro 12. `border` adicionada depois "agora existe". "Isso também dá para fazer com novas funções."

### Tudo é objeto, protótipo e "API"

- "Quando você cria um objeto, ele já é filho de outro objeto, só de você declarar isso aqui, ele já é filho de um outro objeto."
- "Dá para fazer função dentro de função, utilizando, por exemplo, addEventListener é uma função dentro de outra função [...] ponto alguma coisa, ponto alguma coisa [...] é simplesmente função dentro de função, então objeto dentro de objeto."
- `let nome = 'Násser'`: "só de eu declarar isso aqui, ele já é um objeto no final das contas." O autocomplete mostra `length`, `lastChild`, `indexOf`, `link`, `matchAll`; "quando é azulzinho é uma variável, é um atributo, quando é roxinho é um método". `nome.length` dá 6.
- "Quando você define um objeto, ele já vira filho de um outro objeto maior, qual é o objeto maior? String [...] basicamente isso é o que a gente chama de API, porque é uma conversa entre o JavaScript e o browser."
- `let idade = 26`: `toExponential`, `toFixed`, `toLocaleString`, `toPrecision`, `toString` ("se eu quiser transformar [...] um dado numérico em string").
- "O JavaScript se dá muito no aprendizado do que já existe, dos métodos e objetos que já existem."

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/objetos-javascript]] (criado neste ingest)
- [[wiki/concepts/programacao-orientada-a-objetos]]
- [[wiki/concepts/abstracao]]
- [[wiki/concepts/objeto-vs-estrutura-de-dados]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/string]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/event-listener-javascript]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/ecmascript]]
- [[wiki/concepts/imutabilidade]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para objetos e protótipos; as precisões vêm do MDN (`[external]`).

- **`lado: 4` mistura dois números.** A aula diz "tem a propriedade lado, então ele tem quatro lados" e calcula a área como `lado * lado` e o perímetro como "4 vezes o lado", "a própria quantidade de lados". Com `lado = 4`, o comprimento do lado e o número de lados coincidem, e por isso área e perímetro dão 16. Num quadrado de lado 5, `this.lado * 4` continua certo só porque o 4 do perímetro é fixo; a propriedade é o comprimento, não a contagem.
- **"Filho de outro objeto" é a cadeia de protótipos.** `[external]` Um literal `{}` tem como protótipo `Object.prototype`, de onde vêm `toString` e `hasOwnProperty`; uma string usa `String.prototype` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain). A imagem de "filho" serve, mas "o objeto maior" não é "String" e sim `String.prototype`. Ver [[wiki/concepts/objetos-javascript]].
- **Primitivo não "já é um objeto".** `[external]` `'Násser'` continua primitivo; ao fazer `nome.length`, o motor embrulha o valor num `String` temporário (*autoboxing*). Terceira aula seguida com a mesma imprecisão ([[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript|aula 02]], [[wiki/sources/frontpush-functions-e-arrow-functions-javascript|aula 04]]; [[wiki/concepts/tipos-primitivos-javascript]]).
- **Métodos de string não são "API do browser".** `length`, `indexOf`, `toFixed` são da linguagem ([[wiki/concepts/ecmascript]]) e existem igual no Node. As APIs do navegador são outra camada: [[wiki/concepts/dom]], `fetch`, `localStorage`. "Nativas do próprio JavaScript, do próprio browser" junta as duas.
- **`lastChild` não existe em string.** É propriedade de nó do DOM. Na lista do autocomplete, o item é quase certamente `lastIndexOf` (erro da legenda ou da fala; ficou literal no raw). `link` existe, mas é um método HTML legado e obsoleto.
- **`addEventListener` não é "função dentro de função".** É um método de `EventTarget` que recebe uma função como argumento (callback) ([[wiki/concepts/event-listener-javascript]]). `a.b.c` é acesso a propriedades de objetos aninhados; chamada de função dentro de função é outra coisa.
- **`this` depende de como o método é chamado.** `[external]` `retangulo.area()` usa `retangulo`; `const f = retangulo.area; f()` perde o vínculo (`undefined` em strict mode). E um método escrito como arrow não tem `this` próprio, o que liga esta aula à [[wiki/concepts/arrow-functions|aula 04]].
- **A resposta para "está muito fixo" é um molde, não só a mutação.** Para ter vários retângulos, usa-se uma função fábrica (`criaRetangulo(a, b)`) ou uma `class Retangulo` com `constructor`; mudar `retangulo.a` muda o único objeto que existe. Ver [[wiki/concepts/programacao-orientada-a-objetos]].
- **Objetos são mutáveis mesmo em `const`.** `retangulo.border = 1` funciona com `const retangulo`; para impedir, `Object.freeze` ([[wiki/concepts/imutabilidade]]).
- **Outras formas de acesso:** colchetes (`retangulo['a']`, `obj[chave]` com chave variável) e desestruturação (`const { a, b } = retangulo`; [[wiki/concepts/desestruturacao-javascript]]).
- **Vírgula final** é permitida em literais de objeto (ES5), e formatadores como o Prettier a acrescentam.
- **"Escopo, argumento, length" no console** são os detalhes internos de uma função (`[[Scopes]]`, `arguments`, `length`, `name`, `prototype`): mostram que funções também são objetos. O "já, já vou explicar" não volta na legenda.
- **"Notação do JavaScript 6"** é o *method shorthand* do ES2015 (`area() {}`); está certo.

## Open Questions

- Há 12 s sem legenda (00:20:52–00:21:04) antes de ".js para transformar, por exemplo, número em string": provavelmente uma busca no Google ("número em string js") ou na [[wiki/entities/mdn-web-docs|MDN]].
- Na aula 02 a idade de exemplo era 25; aqui é 26. Sugere que as aulas foram gravadas com meses de diferença (inferência).
- "Não sei se está focando": a caneta aparece na câmera, mas a aula é de tela; a legenda não diz quando ele volta a aparecer.

## Raw quotes

- "praticamente tudo em JavaScript é objeto"
- "a grande magia do JavaScript está em a gente descobrir quais são eles"
- "quando é azulzinho é uma variável, é um atributo, quando é roxinho é um método"
