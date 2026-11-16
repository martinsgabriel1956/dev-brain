---
type: concept
title: "Estruturas de repetição em JavaScript (for, while, for...of, forEach)"
aliases: ["loop", "loops", "for", "while", "do...while", "for...of", "for...in", "forEach", "loop infinito", "off-by-one", "iteração"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [javascript, loops, for, while, iteracao, array, controle-de-fluxo]
skill: lang-dynamic
status: stub
---

# Estruturas de repetição em JavaScript

Repetem um bloco enquanto uma condição for verdadeira ([[wiki/concepts/truthy-e-falsy]]). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration

## for

```js
for (let i = 0; i < frutas.length; i++) {
  console.log(frutas[i])
}
```

Ordem: inicialização (uma vez) → condição → corpo → incremento → condição... As três partes são opcionais; sem condição ou sem incremento, o loop pode não acabar. Bom quando se sabe quantas voltas dar.

## while e do...while

```js
let i = 0
while (i < frutas.length) {
  console.log(frutas[i])
  i++            // esquecer esta linha é o loop infinito clássico
}
```

Só a condição fica no cabeçalho. Bom quando o fim depende de algo calculado no corpo (ler até acabar, tentar até conseguir). `do { } while (cond)` roda o corpo ao menos uma vez.

## Percorrer coleções sem índice

- `for (const fruta of frutas)` (ES2015): valores de array, string, `Map`, `Set`.
- `for (const chave in objeto)`: chaves de objeto (evitar em arrays).
- `frutas.forEach((fruta, i) => ...)`; para transformar ou filtrar, `map` e `filter` devolvem um array novo ([[wiki/concepts/array]]).

## Armadilhas

- **Off-by-one:** índices vão de 0 a `length - 1`; `i <= length` lê um `undefined` no fim.
- **Loop infinito:** trava a aba, porque o código roda numa thread só e nada mais executa enquanto o loop gira ([[wiki/concepts/event-loop-performance-js]]). Um `while` esperando uma variável mudar "em outra parte do código" nunca a verá mudar.
- **`break` e `continue`** saem do loop ou pulam para a próxima volta.
- **`var` no `for` com callbacks** compartilha um `i` só; `let` cria um por volta ([[wiki/concepts/var-let-const]]).

Relacionado: [[wiki/concepts/estruturas-condicionais-javascript]], [[wiki/concepts/logica-de-programacao]], e o equivalente em tempo de compilação, [[wiki/concepts/loops-sass]].

## No FrontPUSH

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], [[wiki/entities/nasser|Násser]] ensina as três partes ("como começa", "como termina", "como modifica"), corrige ao vivo um `for` de 0 a 12 que roda 13 vezes, trava o navegador com um `while` sem `i++` e chega a `i < frutas.length`. Diz que o `while` é "mais aberto" porque o incremento pode ficar dentro de um `if`; o exemplo com um booleano mudado "em outra parte do código" seria um loop infinito.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], o `forEach` substitui o `for` com índice: "ele já faz a estrutura de repetição já verificando o tamanho do array". Não aceita `break` nem espera `await`.

## Key sources

- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: for, while, loop infinito ao vivo, i < length
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach no lugar do for
