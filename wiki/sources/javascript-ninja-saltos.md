---
type: source
title: "Saltos: return, break e continue (JavaScript Ninja, semana 11, vídeo 02)"
aliases: ["JavaScript Ninja saltos", "JS Ninja break e continue", "JavaScript Ninja jump statements", "02 - Saltos"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [javascript, return, break, continue, early-return, switch, fall-through, loops, jump-statements]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-saltos.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-27
---

# Saltos: return, break e continue (JavaScript Ninja, semana 11, vídeo 02)

## TL;DR

Segundo vídeo da semana 11 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 12,5 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], depois de [[wiki/sources/javascript-ninja-lacos-loops|laços]]. Abre com uma piada: "não é sobre sapatos de salto alto", são as instruções que "você usa para pular algumas partes [...] do teu código" ([[wiki/concepts/break-e-continue-javascript]]).

- **return como salto:** "só pode ser usado dentro de funções". Com `if (num === 10) return true`, a função "vai pular todo o restante" ([[wiki/concepts/funcoes-javascript]]).
- **Early return × variável de retorno:** a mesma lógica com uma variável, `if`/`else` e um `return` no fim "vai funcionar exatamente do mesmo jeito"; sem o `else`, "uma variável a menos" e "muito mais visibilidade da função" ([[wiki/concepts/estruturas-condicionais-javascript]]).
- **break no switch:** "serve pra sair [de] uma instrução". Sem ele, com `num` 10, imprime o `case 10`, o `case 2` e o `default` (fall-through).
- **break no for:** com `if (i === 5) break`, imprime de 0 a 4 e cai no `console.log` depois do laço. Serve para "não precisa testar todos" num array grande.
- **continue:** "ao invés de ele sair da instrução, ele continua para a próxima" volta; com `i === 5`, imprime 0 a 4 e 6 a 9.
- **Ímpares com continue:** `if (i % 2 === 0) continue` deixa só 1, 3, 5, 7, 9; o contrário dá os pares ([[wiki/concepts/operadores-aritmeticos-javascript]]).
- O vídeo não anuncia o próximo.

## Key Claims

### O que é um salto

- "São saltos [...] algumas instruções [...] que você usa para pular algumas partes [...] do teu código."
- O primeiro "já conhecido por nós: return". "Só pode ser usado dentro de funções."

### return no meio da função

- Função com `var num` e "se o número for igual a 10, então vou [...] retornar". Com 10, retorna; com 5, "ele vai me retornar falso".
- "Aqui eu estou usando o return como um salto. Eu estou pulando o restante das instruções dessa função aqui."
- Depois do `if`, declara outra variável com "Fernando Daciuk" e devolve o nome com o número: com 5, a saída é "Fernando Daciuk" e 5; com 10, "ele vai retornar o valor da função [...] vai pular todo o restante".
- "Isso é uma expressão de salto. [...] Porque você pode utilizar ele no meio da [...] função."

### Variável de retorno × retorno direto

- Alternativa: "criar uma variável de retorno", um valor padrão, atribuir dentro do `if`, outro valor no `else`, e "no final de tudo eu simplesmente retornar. Ele vai funcionar exatamente do mesmo jeito."
- A diferença: em vez de "toda a função passar no if, passar no else", o retorno direto "acaba ficando mais ligeiro".
- "Se você não utilizar o else, melhor ainda. Não que seja um problema, mas [...] muito mais visibilidade da função. Você sabe o que está acontecendo aqui. [...] Você precisa de uma variável a menos."

### break

- "Uma palavra-chave chamada break, que faz o quê? Ele serve pra sair [de] uma instrução."
- No `switch` com `num` 10: com `break` em cada `case`, só o 10. No `default`, "eu não preciso do break aí".
- Sem o `break`: "mostrou dez, e olha só", e os outros corpos e o `default` "independente de qualquer coisa, se é igual ou não". "Qualquer outro valor aqui embaixo, ele vai imprimir."
- "O switch [...] passa [...] de cima até embaixo [...] e, quando ele encontra [o caso verdadeiro], ele vai executar [...], ele vai parar no break, e o break vai [...] jogar para fora do switch."
- "Ele funciona também com laços." No `for (i = 0; i < 10; i++)`, `if (i === 5) break` imprime 0 a 4 e "saiu do for. Aí já caí direto [...] na próxima instrução, que é esse console.log ao fim do for".
- Uso: "Você está testando um número que é muito gigante; você não precisa testar todos." Com `i < array.length` num array de dez itens, o `break` faz "sair do meu loop".

### continue

- "A diferença é que, ao invés de ele sair da instrução, ele continua para a próxima instrução válida."
- "Ele não executa nada que [...] está dentro do for [abaixo dele]. Ele volta para o início do for", incrementa e "passa o próximo valor".
- Com `i === 5`: "0, 1, 2, 3, 4, [...] ele pulou [...] mostrou 6, 7, 8, 9".
- "Se o i for divisível por 2 [...] não quero que ele mostre [...] ele vai mostrar só os ímpares": 1, 3, 5, 7, 9. "Se eu fizer o contrário", os pares.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para *jump statements*. As precisões vêm da MDN e da especificação, marcadas `[external]`, sem fetch. As demos foram reproduzidas no Node 22.23.

1. **`return` fora de função é erro de sintaxe.** Verificado: `SyntaxError: Illegal return statement`. Sem `return`, a função devolve `undefined` (verificado). `[external]` Em módulo ES também não há `return` no topo ([[wiki/concepts/funcoes-javascript]]).
2. **"Mais ligeiro" é legibilidade, não velocidade.** O early return evita passar pelo `else`, mas a diferença de desempenho é desprezível; o ganho que a aula descreve depois ("uma variável a menos", "visibilidade") é o que importa. A wiki registra o padrão como *early return* / *guard clause* em [[wiki/concepts/estruturas-condicionais-javascript]] e [[wiki/concepts/kiss]]. Tensão leve com a regra "retorne sempre na última linha da função" do vídeo de [[wiki/sources/javascript-ninja-hoisting|hoisting]], que já abria exceção para "um return dentro do if".
3. **Fall-through confirmado.** Verificado: `switch (10)` sem `break` imprime 10, 2 e `default`. Ele executa os corpos seguintes sem testar os `case`, como já registrado em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]. A aula agora descreve certo ("qualquer outro valor aqui embaixo, ele vai imprimir").
4. **`break` não serve "em qualquer lugar do teu programa".** `[external]` Sem rótulo, `break` só vale dentro de laço ou `switch`; fora deles é `SyntaxError` (verificado num `if`). Num callback de `forEach` também (verificado: `Illegal break statement`). Para parar cedo numa busca em array, `find`, `some`, `every` ou um `for` comum ([[wiki/concepts/array]]).
5. **`continue` no `while` pode virar loop infinito.** Verificado: no `while`, o `continue` pula o resto do corpo, inclusive o `j++`, se ele estiver depois. No `for`, a expressão final roda mesmo com `continue`, por isso a demo funciona ([[wiki/concepts/estruturas-de-repeticao-javascript]], [[wiki/concepts/incremento-e-decremento]]).
6. **`return` num `forEach` é um `continue`.** Verificado: dentro do callback, `return` só encerra aquela volta (`[1,2,3]` com `return` no 2 imprime 1 e 3).
7. **Rótulos ficaram de fora.** `[external]` `break rotulo` e `continue rotulo` saem ou avançam um laço externo a partir de um interno (verificado com `outer:`). Na classificação do Flanagan, `throw` também é um salto.
8. **A demo do array imprime índices.** Com `i < array.length` num array de 1 a 10, a saída 0 a 9 (sem o 5) é o `i`, não `array[i]` (verificado).
9. **Correção do ingest anterior.** A piada da abertura ("não é sobre moda, não é sobre sapatos de salto alto") mostra que "Já falei de moda" no fim de [[wiki/sources/javascript-ninja-lacos-loops]] era literal: o anúncio brincava com "saltos". E "wi fi" aqui é `if` (3×), o que sugere que "wi fi" naquele vídeo também era `if`.
10. **Legenda.** Trocas principais: "Fininho"→Ninja, "da Silva" (3×)→Daciuk, "Wittmann"/"Bitcoin"→return, "Black to Buy"/"banho"/"Wei"/"beijo"/"Branquinho"/"brega"/"bem"/"banco"/"buraco"/"brinquedo"→break, "contínuo"/"cantinho"/"eu continuo"→continue, "sítio"/"suíte"→switch, "de foto"→default, "wi fi"→if, "L5"→else, "forte"/"fora"/"foco"/"Fórum"→for, "Rei"/"Rui"/"Harry"→array, "Harry Potter lei"→array.length, "laptop"/"Lupi"/"Cup"→loop(s), "IP"/"wi"→i, "sexo"→seis, "pai"→par. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/break-e-continue-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/kiss]]
- [[wiki/concepts/array]]
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/pitfalls-de-linguagem]]

## Open Questions

- **O código da função.** Pela fala, algo como `function example(num) { if (num === 10) return true; var name = 'Fernando Daciuk'; return name + ' ' + num }` (média). "Vou me retornar filme sendo a melhor guarda", "ele retorna outro", "Nem me importo, Fernando Daciuk", "retornar que unem mais um espaço de mais uma noite": literais no raw. "Nem me" deve ser `name` e "mais um espaço" deve ser `+ ' ' +` (média).
- **A versão com variável de retorno.** "Uma variável de retorno eterno, vai ser viria um default aqui, fazer um retorno vai receber true; no else, passar esses caras aqui. Era só fazer o White": talvez `var retorno = false; if (num === 10) { retorno = true } else { ... } return retorno` (baixa). "Usar um sim" e "o White" ilegíveis.
- **"Vou criar filmes"**, **"uma função exemplar"**, **"vou dar oito anos sem usar um console.log, que meu filho é executado"**: talvez "função example" e "vou dar um return [...] sem usar um console.log" (baixa).
- **O valor padrão do `switch`.** "Ele mostrou o falso também" sugere um `default` que imprime "falso" (média). "O desenho de fotos" talvez "o default" (média). "Deu falta" talvez "default" (média). "Ele entra no carro" talvez "no case" (baixa).
- **"Você tem um forte, você pode utilizar em qualquer lugar"**: talvez "você tem o break" (baixa). Ver a precisão 4.
- **"Eu for posso, posso fazer no ar, e eu posso fazer tudo"**: provavelmente "no for posso, no while, no do...while" (média).
- **"Uma vaga igual a zero"**: `var i = 0` (média). **"No Estado"**, **"pula um Estado"**, **"vai ser um Estado"**: talvez "o i" e "pula uma volta" (baixa).
- **"Um menu do for: enquanto o uniforme do array.length"**: `for (var i = 0; i < array.length; i++)` (média). **"Um array Barreiro"**: o nome do array, ilegível.
- **"Somar 1 a 500, o dobro do loop"**: "somar 1 ao i [...] do loop" (baixa).
- **"Isso que eu faço"** (3×): provavelmente "isso que o break faz" (média). Literal.
- **"Quando Rei os números já desembarcaram"**, **"os números para ele"**, **"os números pois"**: provavelmente "os números ímpares/pares" (média).
- **"Na última noite, Meu Rio não conhece sobre moda"**: "no último vídeo, [...] não é sobre moda" (média).

## Raw quotes

- "não é sobre sapatos de salto alto, mas são sobre [...] saltos no JavaScript"
- "se você não utilizar o else, melhor ainda"
- "ao invés de ele sair da instrução, ele continua para a próxima instrução válida"
