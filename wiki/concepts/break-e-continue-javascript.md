---
type: concept
title: "break, continue e return como saltos (JavaScript)"
aliases: ["break", "continue", "jump statements", "instruções de salto", "saltos", "break label", "rótulo", "labeled statement", "sair do loop", "pular iteração"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [javascript, break, continue, return, loops, switch, controle-de-fluxo, jump-statements]
skill: lang-dynamic
status: stub
---

# break, continue e return como saltos

Instruções que tiram a execução do fluxo normal ("saltos"). `[external]` https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break

| Instrução | Onde vale | O que faz |
|---|---|---|
| `return` | dentro de função | sai da função, devolvendo o valor (ou `undefined`) |
| `break` | laço ou `switch` (ou bloco rotulado) | sai do laço/`switch` e segue na instrução seguinte |
| `continue` | só em laço | pula o resto do corpo e vai para a próxima volta |
| `throw` | qualquer lugar | sobe até o `catch` mais próximo |

```js
for (var i = 0; i < 10; i++) {
  if (i === 5) break        // 0 1 2 3 4
}
for (var i = 0; i < 10; i++) {
  if (i % 2 === 0) continue // 1 3 5 7 9
  console.log(i)
}
```

## Armadilhas

- **`continue` no `while`** pula o incremento que estiver depois dele, e o laço não acaba. No `for`, a expressão final roda mesmo assim ([[wiki/concepts/estruturas-de-repeticao-javascript]], [[wiki/concepts/incremento-e-decremento]]).
- **`break` esquecido no `switch`** executa os corpos seguintes sem testar os `case` (*fall-through*) ([[wiki/concepts/estruturas-condicionais-javascript]]).
- **Dentro de `forEach`** não há `break` nem `continue` (`SyntaxError`); `return` no callback só encerra aquela volta. Para parar cedo: `for`, `for...of`, `some`, `find` ([[wiki/concepts/array]]).
- **Laço aninhado:** `break` sai só do laço mais interno. Para sair do externo, rótulo: `outer: for (...) { for (...) { break outer } }`. Raro; muitas vezes extrair uma função e usar `return` é mais claro ([[wiki/concepts/funcoes-javascript]]).
- **`return` antecipado** (*early return*, *guard clause*) troca `if`/`else` aninhado por saídas no começo da função ([[wiki/concepts/kiss]]).

## No JavaScript Ninja, semana 11, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-saltos]], os três aparecem como saltos, instruções "que você usa para pular algumas partes [...] do teu código". O `return` "só pode ser usado dentro de funções" e pula "todo o restante da função"; sem `else`, "uma variável a menos". O `break` sai do `switch` (sem ele, o fall-through imprime 10, 2 e `default`) e do `for` (`i === 5` para em 4). O `continue` "continua para a próxima instrução válida": sem o 5, e depois só os ímpares com `i % 2 === 0`. A aula diz que o `break` pode ser usado "em qualquer lugar do teu programa"; sem rótulo, só em laço e `switch`.

## Key sources

- [[wiki/sources/javascript-ninja-saltos]]: JavaScript Ninja, semana 11, vídeo 02: return, break no switch e no for, continue, ímpares
