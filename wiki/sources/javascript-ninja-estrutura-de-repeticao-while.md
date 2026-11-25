---
type: source
title: "Estrutura de repetição while (JavaScript Ninja, semana 6, vídeo 02)"
aliases: ["JavaScript Ninja while", "JS Ninja loop while", "02 - Estrutura de repetição While"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, while, loops, estruturas-de-repeticao, loop-infinito, truthy-falsy, decremento, desafio]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-estrutura-de-repeticao-while.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Estrutura de repetição while (JavaScript Ninja, semana 6, vídeo 02)

## TL;DR

Segundo e último vídeo da semana 6 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9,5 min), depois de [[wiki/sources/javascript-ninja-operador-virgula-e-switch|operador vírgula e switch]]. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). Primeira estrutura de repetição do curso ([[wiki/concepts/estruturas-de-repeticao-javascript]]).

- **Sintaxe:** `while (expressão) { ... }`. A expressão é convertida em booleano; se `true`, executa o corpo; se `false`, "vai continuar o programa normalmente, a partir da próxima linha" ([[wiki/concepts/truthy-e-falsy]]).
- **Diferença para o `if`:** "enquanto esse valor for verdadeiro, ele vai executar"; depois de cada volta, "ele vai voltar lá para cima".
- **Contador de 0 a 9:** `while (counter < 10) { console.log(counter); counter++ }` (o nome da variável ficou ilegível na legenda; deve ser `counter`).
- **Loop infinito:** `while (true)` "nunca vai ser falso"; "nunca faça isso [...] porque você vai travar o seu navegador" ([[wiki/concepts/event-loop-performance-js]]).
- **Falsy na condição:** `0 == false` é verdadeiro e `0 === false` não; com 0 na condição o `while` "simplesmente não vai entrar".
- **Contador descendente:** de 10 a 1 com `console.log(counter--)` e a condição corrigida ao vivo para "diferente de zero ou [...] maior que zero"; depois, o decremento na própria condição, `while (counter--)`, imprime de 9 a 0 ([[wiki/concepts/incremento-e-decremento]]).
- **Desafio da semana 6:** mesmo fluxo de antes, atualizar a master, criar a branch do desafio 06 e abrir pull request no repositório principal ([[wiki/concepts/fork-e-upstream]]).

## Key Claims

### O que é estrutura de repetição

- "Estruturas de repetição, ou mais conhecidas como loop." Vêm depois das "instruções condicionais, que são o if e o switch".

### Sintaxe e condição

- "Você vai passar [...] uma expressão. Vai avaliar essa expressão. Se essa expressão for true, ele vai entrar [...] e vai executar as linhas que estiverem aqui dentro. Se essa expressão retornar false, simplesmente vai ignorar."
- "Ele converte esse valor aqui em um valor booleano."

### Enquanto for verdadeiro

- "A diferença basicamente [...] das estruturas condicionais [...] é assim: enquanto esse valor for verdadeiro, ele vai executar essa instrução."
- "Por isso ele chama uma estrutura de repetição, porque ele fica se repetindo [...] até que essa instrução seja falsa."
- Passo a passo: imprime 0, soma 1, volta; "quando ele chegar a 9 [...] ele imprime [...] 9 e ele soma mais um", vale 10, a condição falha e "ele simplesmente sai da instrução". "Ela vem de 0 a 9."
- "Aqui ele só deu o último retorno para a gente": o console mostra um valor no fim do loop.

### Loop infinito

- "Você consegue fazer o que chamo de loop infinito, fazendo um while true [...]. Mas nunca faça isso no seu código, no seu navegador, porque você vai travar o seu navegador. Você vai ter que reiniciar."

### Valores falsy na condição

- "Eu sei que zero ele é falso"; com `===` "não é igual a false", "mas se eu não testar o tipo, ele é igual a falso". Com zero na condição, "ele simplesmente não vai entrar aqui"; "ele não imprimiu valores [...] porque era falso".

### Contador descendente

- `var counter = 10`, "um contador descendente [...] de trás para frente". `console.log(counter--)`: "ele imprime o valor [...] e daí atribui menos um".
- Primeira condição errada (algo como "igual a zero", que "é falso"); corrige: "diferente de zero, ou [...] maior que zero". Imprime 10, 9, 8, 7, 6, 5, [4,] 3, 2, 1.
- Segunda versão: o `--` vai para a condição. "Ele imprimiu o valor 9 [...] aí diminui um, já vale 8 [...] até chegar em zero."

### Desafio da semana 6

- "O desafio da semana de 6 está lançado. O esquema é o mesmo do desafio passado": atualizar a master, fazer o merge, criar a branch, fazer o desafio, pull request "[n]um repositório principal".
- Dúvidas por e-mail ou, "melhor até", issue no GitHub, para que a resposta sirva a outros alunos.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para `while` no JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **O "último retorno" é o valor de conclusão.** `[external]` O `while` não retorna nada; o REPL do Node (e o console do navegador) mostra o *completion value* da instrução, que é o valor da última expressão executada no corpo. No contador de 0 a 9, `counter++` devolve 9 na última volta, e é esse 9 que aparece ([[wiki/concepts/expressao-javascript]]).
2. **Por que trava.** O loop infinito trava a aba porque o JavaScript da página roda numa thread só: enquanto o loop gira, nada mais executa (nem render, nem cliques, nem timers). O navegador oferece encerrar o script; não é preciso reiniciar o navegador inteiro ([[wiki/concepts/event-loop-performance-js]]). `while (true)` com `break` é um padrão legítimo; o problema é não haver saída.
3. **`while (counter)` × `while (counter > 0)`.** `[external]` Com inteiros a partir de 10 os dois dão o mesmo resultado. Se o contador começar negativo ou pular o zero (passo 0,3, por exemplo), `!== 0` e a forma truthy nunca falham e o loop fica infinito; `> 0` é a condição defensiva ([[wiki/concepts/truthy-e-falsy]]).
4. **`while (counter--)` testa o valor antigo.** O pós-decremento devolve o valor antes de subtrair: a condição vê 10 e o corpo imprime 9, até a condição ver 0 com o corpo já tendo impresso 0. No fim, `counter` vale -1, não 0. A aula acerta a saída (9 a 0), mas não explica por que começa em 9 ([[wiki/concepts/incremento-e-decremento]]).
5. **O que ficou de fora.** `do...while` (o corpo roda ao menos uma vez), `for`, `break` e `continue`. O `break` apareceu no vídeo anterior, mas só no `switch` ([[wiki/concepts/estruturas-condicionais-javascript]]).
6. **Branch do desafio.** A legenda diz "cria tablets gera em 06"; pelo fluxo da semana 3 (`challenge-03`), deve ser a branch `challenge-06` (inferência, média-alta). O curso ainda usa `master`; repositórios novos no GitHub usam `main` desde 2020 ([[wiki/concepts/fork-e-upstream]]).
7. **Legenda.** Trocas principais: "coisas jovens de biquíni Gilson"→o curso JavaScript Ninja, eu sou o; "da Silva"→Daciuk; "áudio" (4×)→while; "Lupi"/"grupo"→loop; "tu"→true; "eu tu"→while true; "Wi-Fi"→if; "suíte"→switch; "massa"→master; "por reconhece"→pull request; "amigo"→e-mail; "mais no vídeo"→issue no GitHub; "javali"→já vale. O nome da variável ("caldo", "cautela", "cautelar", "Caltech", "cauda", "conter", "falta"; provavelmente `counter`) ficou literal. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/event-loop-performance-js]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/fork-e-upstream]]

## Open Questions

- **Nome da variável**: "cautela" e variantes; provavelmente `counter` (média), talvez `count`. Mantido literal no raw.
- **"Conta na noite desta" / "vou fechar o meu tio"**: a montagem do primeiro `while` (talvez "o console" e "fechar o meu while" ou "o bloco"); baixa.
- **"Era lema de meus valores fui Fauci"**: provavelmente "é um dos meus valores falsy" (média); literal.
- **"Se eu contestar no Haiti valor zero"**: provavelmente "se eu testar no while o valor zero" (média); literal.
- **"Menos igual de Búzios"**: a condição da segunda versão descendente; ilegível (baixa).
- **"A estrutura de repetição suíte"**: a primeira ocorrência deve ser "while" (média); literal, porque a segunda "suíte" é o switch.
- **"Faz o site lá na sua master" / "faz como tipo de repositório"**: provavelmente "faz o fetch" e "faz commit, push pro repositório" (baixa).

## Raw quotes

- "enquanto esse valor for verdadeiro, ele vai executar essa instrução aqui"
- "nunca faça isso no seu código, no seu navegador, porque você vai travar o seu navegador"
- "o desafio da semana de 6 está lançado"
