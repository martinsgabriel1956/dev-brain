---
type: source
title: "typeof (JavaScript Ninja, semana 10, vídeo 02)"
aliases: ["JavaScript Ninja typeof", "JS Ninja testar tipos de valores", "02 - typeof"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [javascript, typeof, tipos-primitivos, null, validacao-de-argumentos, operador-unario, coercao, truthy-falsy]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-typeof.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-27
---

# typeof (JavaScript Ninja, semana 10, vídeo 02)

## TL;DR

Segundo vídeo da semana 10 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 14 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], depois de [[wiki/sources/javascript-ninja-wrapper-objects|wrapper objects]]. Apresenta o [[wiki/concepts/typeof-javascript|operador typeof]] e o usa para validar os argumentos de uma função.

- **Operador unário:** recebe um operando e devolve "o tipo desse operando" ([[wiki/concepts/operadores-unarios-javascript]]).
- **A tabela:** `undefined`, `function`, `boolean`, `number` (inclusive `NaN`), `string`; "qualquer outro objeto que não seja uma função" dá `object`, inclusive array e `null` ([[wiki/concepts/tipos-primitivos-javascript]]).
- **`typeof null` é `object`:** "um erro da implementação do JavaScript, que já está documentado" ([[wiki/concepts/null-e-undefined]]).
- **Regra:** "Você pode confiar no typeof se você for utilizar ele para valores primitivos", "de preferência número, string e Boolean". Para array e objeto, "outros tipos de teste", que o curso promete para depois ([[wiki/concepts/array]]).
- **O porquê da validação:** `sum('JS', 2)` concatena; `sum({}, [])` "está tentando somar dois objetos". Em `subtract`, o `-` "não tem essa sobrecarga", espera dois números e devolve `NaN` ([[wiki/concepts/operadores-aritmeticos-javascript]]).
- **A guarda:** `typeof num1 === 'number' && typeof num2 === 'number'` antes da conta; senão, `undefined` ou uma mensagem personalizada ([[wiki/concepts/validacao-de-entrada]]).
- **Testar `null`:** `!valor` pega "todos os tipos de valores falsos"; para `null` especificamente, "o operador de igualdade estrito" ([[wiki/concepts/truthy-e-falsy]], [[wiki/concepts/igualdade-javascript]]).

## Key Claims

### O operador

- "Nós temos um operador unário, typeof [...] ele funciona só [com] um operando [...] Ele vai te dar o resultado, ou o tipo desse operando."
- A motivação: saber se "um parâmetro passado na função [...] é uma string, [...] um número, [...] um Boolean".

### Os retornos

- `undefined` dá `undefined`; uma função dá `function`; "valor true ou false" dá `boolean`; número e `NaN` dão `number`; `'JS Ninja'` dá `string`.
- "Qualquer outro objeto que não seja uma função, ele vai retornar [...] objeto." "Objeto vazio, objeto preenchido", array: todos `object`.
- O `NaN` "é também o número", "para tirar a prova real, a gente pode utilizar o typeof".

### typeof null

- "Se eu tiver null, ele vai retornar como objeto. [...] Como assim? [...] Na verdade, isso é um erro na implementação [...] de JavaScript."
- "Já está documentado [...] foi feito nas primeiras implementações de JavaScript [...]. Na versão 6, eu acredito, ele vai vim já com essa versão já corrigida."
- "Não testar o objeto usando o typeof." "Você pode confiar no typeof se você for utilizar ele para valores primitivos."

### Por que validar

- `sum(10, 2)` dá 12. `sum('JS', 2)`: "ele vai concatenar os valores". `sum({}, [])`: "ele vai retornar, na verdade, é um objeto, porque ele está tentando somar dois objetos".
- O `+` "tem uma sobrecarga"; o `-` "não tem essa sobrecarga [...] ele espera que sejam dois números". Com objeto e array, "ele retorna NaN [...] ele está dizendo que não é um número".
- As conversões do `+` com objetos ficam "nas próximas aulas".

### A guarda com typeof

- Verifica antes da conta que o tipo de `num1` e o de `num2` são `number`; se forem, "ele vai retornar a diminuição dos dois"; senão, `undefined`.
- `subtract(10, 2)` dá 8; o caso inválido dá `undefined`. Com mensagem personalizada, a função devolve algo como "[entre] com dois números" (texto ilegível na legenda).

### Testar null

- `typeof x === 'object'` não separa `null` de objeto.
- "Se eu quiser testar se o valor foi entrado [...] é falso [...] posso colocar um not aqui na frente." O `!` testa "se o valor não é igual a zero, se o valor não é uma string vazia", `NaN`, `false`, e assim por diante.
- "Se eu quiser testar explicitamente pelo valor null, aí eu tenho que utilizar [...] o operador de igualdade estrito." Na demo, `num1 === null` devolve "não entra com valores nulos".
- "A forma mais correta [...] você testar se aquele valor é realmente nulo, ou, então, [...] se você testar com a exclamação [...] ele testa todos os tipos de valores falsos."

### A dica

- "Sempre que você utilizar o typeof, procure utilizar ele com valores primitivos, de preferência número, string e Boolean. Só esses três tipos de valores, você pode ter garantido que você nunca vai ter problemas com ele."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para `typeof`. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **O ES6 não corrigiu `typeof null`.** `[external]` Houve uma proposta para `typeof null === 'null'` no ES6 (harmony), que foi rejeitada porque quebraria código existente. Continua `'object'` até hoje (verificado). A origem é o tag de tipo `0` dos valores na primeira implementação, o mesmo tag dos objetos (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null). A wiki já registrava o "erro histórico" em [[wiki/concepts/null-e-undefined]] e [[wiki/concepts/operadores-unarios-javascript]].
2. **`{} + []` não dá objeto: dá a string `'[object Object]'`.** Verificado: `sum({}, [])` devolve `'[object Object]'`, uma string. O `+` converte os dois operandos para primitivo (`{}` vira `'[object Object]'`, `[]` vira `''`) e concatena. O que a aula vê no terminal é texto, não um objeto. `subtract({}, [])` dá `NaN`, como dito.
3. **A tabela completa tem oito resultados.** `[external]` Além dos seis da aula (`undefined`, `boolean`, `number`, `string`, `function`, `object`), existem `symbol` e `bigint` (verificados). Classe dá `'function'`. Wrapper dá `'object'`: `typeof new String('a')` ([[wiki/concepts/wrapper-objects-javascript]]).
4. **`typeof` não dá erro em variável não declarada.** `[external]` `typeof naoDeclarada` devolve `'undefined'` em vez de `ReferenceError` (verificado); era assim que se testava se uma global existia. A exceção é a zona morta temporal: `typeof y` antes de `let y` dá `ReferenceError` (verificado; [[wiki/concepts/hoisting-javascript]]).
5. **A guarda deixa `NaN` passar.** Verificado: com `typeof num1 === 'number' && typeof num2 === 'number'`, `subtract(NaN, 1)` passa na guarda e devolve `NaN`, porque `typeof NaN` é `'number'`. `[external]` Para exigir número válido, `Number.isFinite(x)` (falso para `NaN`, `Infinity` e não números, sem converter) ([[wiki/concepts/validacao-de-entrada]]).
6. **O `!` como teste de ausência rejeita `0`.** Verificado: `!0`, `!''`, `!NaN`, `!null`, `!undefined` dão `true`. Num `subtract`, `0` é argumento válido e seria barrado. Para "faltou o valor", `x == null` (pega `null` e `undefined`) ou `x === undefined` são mais precisos ([[wiki/concepts/truthy-e-falsy]], [[wiki/concepts/igualdade-javascript]]).
7. **Os "outros tipos de teste" prometidos.** `[external]` Para array, `Array.isArray(x)` ([[wiki/concepts/array]]). Para objeto não nulo, `x !== null && typeof x === 'object'`. Para o tipo exato, `Object.prototype.toString.call(x)` (`'[object Null]'`, verificado), já registrado em [[wiki/concepts/tipos-primitivos-javascript]] por outra fonte.
8. **Validar tipo é a versão de dentro da função.** `[external]` Em TypeScript, o tipo dos parâmetros barra `sum('JS', 2)` na compilação, e `typeof` dentro de `if` vira *type guard*, estreitando o tipo no bloco. Em fronteiras do sistema (entrada de usuário, JSON), a checagem em tempo de execução continua necessária.
9. **Legenda.** Trocas principais: "que já vi escrever"/"Já vi clipes"→JavaScript, "da Silva"→Daciuk, "take off"/"tape off"/"tipo off"/"tapa olho"/"Taipei Office"/"Temple of"/"it off"/"escutar off"/"teclado"/"pior"→typeof, "o nariz"/"no navio"→unário, "Note não"/"nota"→NaN, "nu"→null, "Rui"/"rei"/"rede"/"Harry"→array, "samba Tech"/"subject"/"de súbito"/"se está tocando"→subtract, "ação"→sum, "pela alfândega"/"que eu defendi"/"eu não define"→undefined, "bilhete"→object, "lote"→not, "Muller"/"bolha"→Boolean. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/typeof-javascript]]
- [[wiki/concepts/operadores-unarios-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/array]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/validacao-de-entrada]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/wrapper-objects-javascript]]
- [[wiki/concepts/hoisting-javascript]]

## Open Questions

- **O código exato da guarda.** "Não está off é igual a um estado que está typeof num2 e igual número, se eu até ao final muito typeof num2 foi igual": provavelmente `if (typeof num1 === 'number' && typeof num2 === 'number')` (média-alta). Literal no raw.
- **A mensagem personalizada.** "Com dois números" aparece sem o começo; talvez "Entre com dois números" (média). A de `null` aparece como "não entrei"/"não entro"/"não entra com valores nulos"; talvez "Não entre com valores nulos" (média). Literais.
- **"Se o está typeof do que no ano"**: talvez `typeof num1 === 'object'` contrastado com `num1 === null` (baixa).
- **"Ele vai entrar naquele mercado"**, **"vai entrar na câmera"**: provavelmente "vai retornar number" (média). **"Com mais string"**: "como string". **"Uma falante"**, **"uma fantochada"**, **"a mão no chão"**: provavelmente *function*/"uma função", como em vídeos anteriores (média).
- **"O tempo todo"**, **"um tempo novo"**, **"o tempo de passar"**: provavelmente "o typeof" (média). **"Ficou"** depois de typeof: talvez "com". **"Mais literal"**/**"mais tarde"**: talvez "string literal"/"string" (baixa).
- **"Quando eu achar humanoide ninja"**, **"um kit ninja"**, **"achar uma aqui no inimigo"**: talvez "rodar o node ninja.js" (baixa).
- **"Um bilhetinho rei"**: talvez "um objeto e um array" (média). **"Mas tinha"**: talvez "uma string".
- **"Ele vai me retornar para os dois"**: provavelmente `NaN` (média). **"Ele disse que o não faria"**: o erro ao chamar a função com o nome antigo (`sum` is not defined?), baixa.
- **"Está construindo e Boolean"**: talvez "string, number e Boolean" (média).
- O vídeo não anuncia o próximo assunto; é o último arquivo da pasta de transcrições.

## Raw quotes

- "você pode confiar no typeof se você for utilizar ele para valores primitivos"
- "o operador menos [...] ele não tem essa sobrecarga"
- "se você testar com a exclamação [...] ele testa todos os tipos de valores falsos"
