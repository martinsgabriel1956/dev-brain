---
type: concept
title: "var, let e const (JavaScript)"
aliases: ["var", "let", "const", "declaração de variável", "variáveis em JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 7
tags: [javascript, variaveis, escopo, lang-dynamic]
skill: tech-mentor-frontend
status: stub
---

# var, let e const (JavaScript)

Três formas de declarar variável. `var` tem escopo de função e é içada (*hoisting*) com valor `undefined`. `let` tem escopo de bloco e não pode ser lida antes da declaração. `const` também tem escopo de bloco e impede reatribuição, mas não torna o valor imutável: um objeto em `const` aceita novas propriedades. Prática comum: `const` por padrão, `let` quando o valor precisa mudar, `var` nunca em código novo.

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] define variável como "guardar em memória alguma coisa para usar mais tarde"; declarada sem valor, é `undefined`. Sobre as três: "com o JavaScript mais moderno, ao invés de a gente ficar usando var, a gente acaba usando aqui a palavra-chave let", "mas também poderia ser var, tanto faz"; ele usa muito `const` "porque eu quero fazer algumas coisas que não mudam o seu valor".

## Precisões

- Não é "tanto faz": a diferença de escopo muda o comportamento de laços e closures (o clássico `for (var i...)` com callbacks) `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let).
- `const` impede reatribuição, não mutação `[external]` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica por que `selectedItems` é `let`: "se eu deixasse ele como const, eu não ia conseguir sobrescrever esses valores. Porque const é uma constante. Let é uma variável." O dia 2 dizia "tanto faz". No dia 3 o `push` muda o array e o `filter` reatribui, e só a reatribuição exige `let`.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], `const newFieldContainer` e `const fields`: "eu não gostaria que [...] fosse trocado"; "como uma variável pode ser constante?". `const` impede reatribuir o nome, não alterar o objeto, e é recriado a cada chamada da função.

## No FrontPUSH, módulo de JavaScript, aula 02 (Násser)

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], [[wiki/entities/nasser|Násser]] mostra a diferença com um bloco solto: `var nome = 'Yousef'` dentro de `{}` sobrescreve o `nome` de fora ("caráter mais global"), e com `let` cada bloco tem o seu (`Yousef` dentro, `Násser` fora). O `const` é "uma constante" e reatribuir dá erro, "esse é o escopo". `var` é de função, não global: o bloco "como se fosse uma função" engana, porque numa função o `var` não vazaria. Também aqui o `const` aparece como "não alterar o conteúdo", sem a diferença entre reatribuir e mutar.

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], `const areaRetangulo = function (a, b) {}` é dada como "exatamente igual" à declaração `function areaRetangulo`. A declaração é içada inteira; a `const` só existe depois da linha (chamar antes dá `ReferenceError`).

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], [[wiki/entities/fernando-daciuk|Daciuk]] só usa `var`: "sempre que você for declarar uma variável em JavaScript, você precisa utilizar a palavra-chave". No REPL do Node, `var x` imprime `undefined`, que é o valor de conclusão da declaração, não o de `x`. Sem `let` nem `const`, a aula é da era ES5.

## No JavaScript Ninja, aula 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-aritmeticos]], `var x = 0` é dado como exemplo de expressão. É uma instrução de declaração, que não produz valor (o REPL ecoa `undefined`); `x = 0` é a expressão ([[wiki/concepts/expressao-javascript]]).

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: variável como memória; var, let e const "tanto faz" (impreciso)
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: let porque reatribui; const não impede push
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: const no cloneField
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: var vaza do bloco, let respeita, const sem reatribuição
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: função em const × declaração (hoisting)
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: só `var`; variável como "nome simbólico" para um valor
- [[wiki/sources/javascript-ninja-operadores-aritmeticos]]: JavaScript Ninja, aula 02: var x = 0 chamado de expressão (é instrução)
