---
type: source
title: "Laços: do...while, for e for...in (JavaScript Ninja, semana 11, vídeo 01)"
aliases: ["JavaScript Ninja laços", "JS Ninja loops", "JavaScript Ninja do...while", "JavaScript Ninja for...in", "01 - Laços (Loops)"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [javascript, loops, while, do-while, for, for-in, operador-in, objetos, notacao-de-colchetes]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-lacos-loops.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-27
---

# Laços: do...while, for e for...in (JavaScript Ninja, semana 11, vídeo 01)

## TL;DR

Primeiro vídeo da semana 11 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], gravado "após fazer a revisão do desafio da semana 10". Depois de [[wiki/sources/javascript-ninja-typeof|typeof]]. Volta às [[wiki/concepts/estruturas-de-repeticao-javascript|estruturas de repetição]] para mostrar "outros tipos de loops que tem no JavaScript".

- **while × do...while:** o `while` "primeiro vai verificar o valor antes de entrar no laço"; se for falso, "ele nem entra". O `do...while` "passa sempre uma vez e depois ele vai verificar".
- **A prova:** com o contador em 10, o `while (counter < 10)` não imprime nada; o `do...while` imprime 10, incrementa para 11 e só então para.
- **Ponto e vírgula:** o `do...while` "vem seguido de ponto e vírgula", ao contrário dos outros loops. É estilo, não obrigação: a inserção automática resolve (verificado).
- **for:** revisão rápida das três partes (variável contador, verificação, incremento), de 0 a 9 ([[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]).
- **for...in:** "serve pra você percorrer propriedades de um objeto". Com `car = { brand: 'VW', model: 'Gol', year: 2013 }`, imprime as chaves e, com `car[prop]`, os valores ([[wiki/concepts/for-in-javascript]], [[wiki/concepts/notacao-de-ponto-e-colchetes]]).
- **Alerta:** "ele é mais lento do que o for normal. Então use bastante cautela." Não medido na aula.
- **Operador `in`:** "testar se uma propriedade também existe em um objeto"; devolve true ou false. `2 in car` é falso.
- **Próximo vídeo:** "saltos": `return`, `break` e `continue` ([[wiki/sources/javascript-ninja-saltos]]).

## Key Claims

### while: testa antes

- "Ele primeiro vai verificar o valor antes de entrar no laço. [...] Ele verifica se é verdadeiro; se for falso, ele nem entra."
- Demo: contador começa em 1, `while (counter < 10)`, `console.log(counter)` e incremento. Imprime de 1 a 9; depois, um `console.log` fora do laço mostra "counter não é mais menor que 10".
- "Se essa instrução for verdadeira, ele entra aqui; se ela for falsa, ele simplesmente sai e continua rodando o programa." Com o contador em 10, nada é impresso dentro do laço.

### do...while: executa antes

- "Eu vou criar lá o do, ou seja, faça. Ele vai fazer alguma coisa." Embaixo, "entre parênteses, o meu while [...] enquanto [...] for menor que dez".
- "Essa instrução aqui, ela vem seguida de ponto e vírgula [...] os outros loops [...] você não coloca ponto e vírgula no final. Mas, no caso do do...while, você vai colocar."
- Com o contador em 10: "ele vai mostrar o dez [...] porque a diferença é que a primeira instrução ele sempre vai fazer". Incrementa para 11, a condição falha, "não faz mais nada".
- Resumo da aula: o `while` "só vai entrar se a instrução for verdadeira", e o `do...while` "sempre vai entrar na primeira instrução e depois [...] vai verificar".

### for

- "Para fazer um for, só preciso fazer aqui uma variável [...] contador. A segunda instrução é a verificação [...]. E a terceira instrução, eu faço um incremento." Mostra de 0 a 9, "exatamente o que" o `while` fez.

### for...in

- "Ela serve pra você percorrer propriedades de um objeto." Objeto da demo: marca (`brand`) VW, modelo Gol, ano 2013.
- "O for...in é um for que aqui dentro [tem] uma variável chamada qualquer coisa [...] de propriedade [...] a propriedade no objeto carro." Provavelmente `for (var prop in car)`.
- "Aqui dentro do for...in eu consigo imprimir o nome dessas propriedades."
- Para o valor: "você pode simplesmente utilizá-lo no formato de array [...]. Quando você tem uma variável que você vai passar com uma string para você pegar uma propriedade de um objeto". Saída: "VW, Gol e 2013".
- "Ele é mais lento do que o for normal. Então use bastante cautela aqui."

### O operador in

- "Ele pode ser usado para testar se uma propriedade também existe em um objeto." Retorna true ou false.
- "Tem a propriedade 2 no objeto o carro? Não, vai ser falso, porque o carro, ele só tem" as três propriedades.
- "Com o in você consegue tanto testar propriedades como você consegue utilizar dentro de um" `for` "pelas propriedades".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para loops. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **O `;` depois do `do...while` é opcional.** Verificado: `do { ... } while (false) console.log('ok')` roda sem erro. `[external]` Desde o ES2015 a inserção automática de ponto e vírgula vale depois do `)` de um `do...while`, mesmo sem quebra de linha (https://tc39.es/ecma262/#sec-rules-of-automatic-semicolon-insertion). O conselho da aula continua bom como estilo: o `;` deixa claro que o `while` fecha o `do` e não abre outro laço ([[wiki/concepts/estrutura-lexica-javascript]]).
2. **O `while` sai quando o contador vira 10, não "quando chegou em 9".** A própria narração corrige em seguida ("chegou em counter 9, ele somou, 10 [...] não, é igual a 10. Então ele sai"). Verificado: começando em 1, imprime de 1 a 9.
3. **`for...in` percorre também propriedades herdadas.** Verificado: num objeto criado com `Object.create({ herdada: 1 })`, o laço devolve a própria e a herdada. `[external]` Ele lista as chaves enumeráveis da cadeia de [[wiki/concepts/objetos-javascript|protótipos]]. Para ficar só com as próprias, `Object.hasOwn(obj, chave)` dentro do laço, ou `Object.keys(obj)` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in). O ESLint tem a regra `guard-for-in`.
4. **`for...in` em array é armadilha.** Verificado: as chaves vêm como strings (`'0'`, `'1'`) e um método acrescentado a `Array.prototype` aparece no laço. `[external]` Para valores de array, `for` com índice, `forEach` ou `for...of` (ES2015, fora do recorte ES5 do curso) ([[wiki/concepts/array]], [[wiki/concepts/pitfalls-de-linguagem]]).
5. **A ordem não é só a de inserção.** Verificado: `{ b, 2, a, 1 }` dá `['1', '2', 'b', 'a']`. `[external]` Desde o ES2020 a ordem do `for...in` é definida: chaves que são índices inteiros em ordem crescente, depois strings na ordem de inserção. No objeto da aula, sem chaves numéricas, a ordem coincide com a escrita.
6. **`in` também enxerga o protótipo.** Verificado: `'toString' in car` dá `true`, embora `car` não declare `toString`. `'brand' in car` dá `true` e `2 in car` dá `false`, como na aula. Para "esta propriedade é do objeto", `Object.hasOwn(car, 'brand')` `[external]`. Em array, `in` testa índice, não valor: `2 in ['a', 'b', 'c']` é `true`.
7. **"Mais lento que o for normal" compara coisas diferentes.** `[external]` O `for` com índice percorre posições de array; o `for...in` percorre chaves de objeto, inclusive as herdadas, o que custa mais. A aula não mostra medição, e esta ingestão não fez benchmark (confiança média). O motivo mais forte para não usar `for...in` em array são os itens 3 e 4, não a velocidade.
8. **"Saltos" deve ser *jump statements*.** Inferência: o próximo vídeo deve tratar de `break`, `continue`, `return` (e talvez `throw`), agrupados como *jump statements* ("saltos") em *JavaScript: The Definitive Guide*, de David Flanagan `[external]`. Confirmado no vídeo 02, [[wiki/sources/javascript-ninja-saltos]]: são `return`, `break` e `continue` (`throw` não aparece).
9. **Legenda.** Trocas principais: "já vi escrever China e índia"→JavaScript Ninja, "da Silva"→Daciuk, "posso"→após, "Caio"/"eu"/"quarto"/"hotel"/"melhor"/"Wii U"/"áudio"→while, "Dubai"/"Dual"/"do eu"→do...while, "foco"/"Ford"→for...in, "fora"/"foi"→for, "golpes"/"grupos"/"up"→loops/loop, "Calder"/"cautela" (2×)→counter, "DS"/"desce"→dez, "hino"→in, "Band c"→brand, "Rui"/"Harry"→array, "estilingue"→string, "lojas"→aulas. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/for-in-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/notacao-de-ponto-e-colchetes]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/array]]
- [[wiki/concepts/estrutura-lexica-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]

## Open Questions

- **Semana.** O vídeo se apresenta como posterior à "revisão do desafio da semana 10"; por isso semana 11, vídeo 01 (média-alta). O arquivo da legenda só diz `01 - Laços (Loops)`.
- **"Tudo o que ele faz"**: provavelmente "o do, o que ele faz", começo da explicação do `do...while` (média). Literal no raw.
- **"Um arquivo Bonilha"**, **"que marque o nível baixo"**, **"vou procurar um plano"**, **"existe até um plano"**: ilegíveis; talvez "um arquivo vazio" e "vou criar um while" (baixa).
- **"Vou soma incremental"**: "vou somar, incrementar" (média). **"Ele tenha do"**: "ele saia do while" (média). **"Saiu do estado"**: "saiu do laço" (média).
- **"O contador como tal, uma coisa"**: talvez "com o valor 1" (baixa).
- **"Os laços hindus e dos formatos"**, **"wi fi é o sentido, não funcionam literal Sweet é o wi fi"**: provavelmente "os laços while e for [...] o while e o for" (média); "Sweet" talvez switch (baixa).
- **"Vai ficar até meia noite dez"**: provavelmente "verificar se é menor que dez" (média). **"O de incremento"**: "o dez, incremente" (média).
- **"Esse Wind é um formador de dados"**: talvez "se i é menor que dez" (baixa). **"Mostrar que sou daqui"**: talvez "mostrar o i aqui" (média).
- **"Modelo dele, Se"**: deve ser Gol, pela saída (média). **"Propriedade da Ferrari"**: talvez `prop in car` (média). **"Na mídia do carro"**: "dentro do carro" (baixa).
- **"Estar na moda"**, **"as propriedades de moda"**, **"Já falei de moda, não tinha uma fora de moda"**: as duas primeiras devem ser "marca, modelo e ano" (média); a terceira é literal: o vídeo seguinte abre com a piada "não é sobre moda, não é sobre sapatos de salto alto" ([[wiki/sources/javascript-ninja-saltos]]). O "wi fi" daquele vídeo traduz `if` (3×), o que sugere que "wi fi" aqui também era `if`.
- **"Se bem que"**, **"para Mito"**, **"no encarte"**: provavelmente `'brand' in car` e "true ou false" (média).
- **"Um repertório específico"**: talvez "um for específico" (média). **"Sobre perseguir esse"**, **"o clube tem"**: talvez "sobre percorrer [...] que o JavaScript tem" (baixa).
- **O código exato do `for...in`** não aparece na fala; a forma `for (var prop in car) { console.log(prop, car[prop]) }` é reconstrução (média-alta).

## Raw quotes

- "a diferença é que a primeira instrução ele sempre vai fazer"
- "ela serve pra você percorrer propriedades de um objeto"
- "ele é mais lento do que o for normal"
