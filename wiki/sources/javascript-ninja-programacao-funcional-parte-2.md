---
type: source
title: "Programação funcional, parte 2: funções que retornam funções (JavaScript Ninja, semana 8, vídeo 03)"
aliases: ["JavaScript Ninja programação funcional parte 2", "JS Ninja adder", "03 - Functional Programming - parte 2", "JavaScript Ninja retorno de funções"]
date_created: 2026-11-25
date_updated: 2026-11-26
source_count: 0
tags: [javascript, programacao-funcional, funcoes-de-primeira-classe, retorno-de-funcao, closure, currying, aplicacao-parcial, ponto-e-virgula, asi]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-programacao-funcional-parte-2.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Programação funcional, parte 2: funções que retornam funções (JavaScript Ninja, semana 8, vídeo 03)

## TL;DR

Terceiro vídeo da semana 8 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 8 min), continuação de [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]], que anunciou o tema. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda).

- **A ideia:** se a função retorna objeto, ela também pode retornar "funções diretamente [de] outras funções", porque funções "são objetos de primeira classe" ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **Função dentro de função:** "você consegue criar uma função dentro de outra função no JavaScript"; sem isso, não daria para retorná-la.
- **O exemplo:** `function adder(x) { return function (y) { return x + y; }; }`. `var add2 = adder(2)` guarda uma função; `add2(3)` dá 5, "a soma dos dois parâmetros passados para as duas funções".
- **Ponto e vírgula:** como a função vem depois de `return`, "não estou criando uma função literal aqui", é uma instrução, e "eu preciso sempre colocar o ponto e vírgula no final" ([[wiki/concepts/pitfalls-de-linguagem]]).
- **Só em linguagens com funções de primeira classe:** nas que "só [permitem] escrever programação imperativa", é preciso "passar os dois parâmetros [...] direto" ou usar abordagens "mais verbal[is]" ([[wiki/concepts/programacao-funcional]]).
- **Duas invocações seguidas:** `adder(5)(8)` dá 13 sem variável intermediária, porque "essa expressão aqui vai me retornar uma outra função" ([[wiki/concepts/expressao-javascript]]).
- **Sem nome:** a aula não chama o mecanismo de [[wiki/concepts/closure-javascript|closure]] nem de [[wiki/concepts/currying|currying]], os dois nomes do que o `adder` faz.
- **Próximo vídeo:** passar funções por parâmetro, como já se passa objeto ([[wiki/concepts/callback-javascript]]).

## Key Claims

### Retornar funções

- "A gente consegue retornar objetos a partir de uma função, e [...] a gente também consegue retornar funções diretamente [de] outras funções. Como assim? Isso a gente não viu ainda."
- "É uma das coisas que o poder de uma linguagem funcional nos permite fazer [...] funções são objetos de primeira classe em JavaScript. [...] Eles podem fazer, ou ser submetidos, às mesmas coisas que os objetos."
- "Eu consigo fazer uma função retornar [o] objeto, eu consigo fazer também uma função retornar [...] outra função. E qual a vantagem disso?"

### Função dentro de função

- "Agora estou criando uma função dentro da outra função. E existe isso? Funciona? [...] Sim, você consegue criar uma função dentro de outra função no JavaScript."
- "Você não consegue [...] retornar uma função [se] você não conseguisse também criar uma função [dentro dela]."
- A função interna é retornada "sem executar", "porque a gente vai chamar ela" depois.

### O adder e o add2

- "Eu crio uma variável chamada add2, ou seja, em que ele vai adicionar dois [...] e passei o 2 aqui, preparando o retorno dela. Nada mais é do que uma função, certo?"
- "Eu executa novamente o add2 e passa por parâmetro [...] o outro número. Eu vou somar 3 com o 2 que eu já tinha passado na primeira vez."
- "Eu passei o primeiro parâmetro e retornei uma função. No segundo parâmetro que eu for passar, [...] a soma dos dois parâmetros que eu passei."
- No teste: "Passei três. [...] Olha só: ele me retorna cinco."

### Ponto e vírgula depois do return

- "Eu não estou criando uma função literal aqui. Eu estou fazendo a minha função [...] ser uma instrução JavaScript, porque eu estou usando o return para retornar [...] ela. Eu preciso sempre colocar o ponto e vírgula no final."

### Primeira classe × imperativo

- "Isso é algo que só linguagens que te dão o poder de utilizar funções de primeira classe você consegue fazer."
- "Algumas linguagens de onde você só consegue escrever programação imperativa, você não consegue fazer algo assim. Você precisa passar os dois parâmetros aqui direto [...] ou [usar] algumas outras abordagens um pouco mais verbal."

### Duas invocações seguidas

- "Ele não precisa necessariamente atribuir [a] uma variável. Posso fazer duas invocações seguidas com JavaScript."
- "Quando eu chamo a minha função e invoco ela, passo o primeiro parâmetro [...] ela me retorna uma outra função. [...] Eu já posso invocar a segunda função aqui direto."
- "Eu vou até usar outros números aqui pra você [não] dizer que estou roubando": `adder(5)(8)` dá 13.

### Próximo vídeo

- "No próximo vídeo [vamos] estar vendo como a gente consegue passar objetos por parâmetros, [a] gente também consegue fazer com funções."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para closures ou currying em JavaScript básico. As precisões vêm da MDN e de conhecimento base, marcadas `[external]`; os exemplos foram reproduzidos no Node 22.23. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

1. **É closure.** `[external]` O `add2` "lembra" o 2 porque a função interna captura a variável `x` do escopo onde foi criada e a mantém viva depois que `adder` termina. Cada chamada cria um escopo novo: `add10 = adder(10)` dá `add10(1) === 11` e `add2(1)` continua 3 (verificado). A aula descreve o efeito ("o 2 que eu já tinha passado na primeira vez") sem nomear o mecanismo ([[wiki/concepts/closure-javascript]], [[wiki/concepts/escopo-javascript]]).
2. **É currying.** `[external]` Transformar `soma(a, b)` em `adder(a)(b)`, um argumento por vez, é currying; fixar o primeiro (`add2`) é aplicação parcial. A versão com arrow, `const adder = x => y => x + y`, dá o mesmo 13 (verificado) ([[wiki/concepts/currying]], [[wiki/concepts/arrow-functions]]).
3. **"Só com primeira classe" não é "contra imperativo".** `[external]` Retornar função com estado capturado exige funções de primeira classe **e** closures. Isso não depende do paradigma: JavaScript, Python, C# e Java 8+ são imperativos e têm as duas coisas. C não tem: ponteiro de função existe, mas não captura variáveis. O eixo da aula mistura paradigma com recurso de linguagem ([[wiki/concepts/programacao-funcional]], [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]).
4. **O ponto e vírgula não é "sempre" necessário.** `[external]` A função depois de `return` é uma *function expression*, e o `;` fecha a instrução `return`. Sem ele, a ASI insere o ponto e vírgula e funciona igual (verificado). A armadilha de verdade é quebrar a linha logo depois do `return`: a ASI fecha a instrução ali e a função devolve `undefined` (verificado). A aula 04 e a [[wiki/concepts/pitfalls-de-linguagem]] já registravam isso.
5. **A função interna não tem nome.** Dois vídeos antes, a regra do curso passou a ser nomear toda função ([[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]). Aqui a função retornada é anônima, e a inferência do ES2015 não ajuda: `add2.name` dá `''` (verificado), porque o nome só é inferido na atribuição direta da função, não no `return`. É o caso em que nomear (`return function addY(y) {...}`) melhora o stack trace (inferência da wiki).
6. **Duas invocações seguidas.** `[external]` `adder(5)(8)` funciona pelo mesmo motivo que `f()[0]` e `f().prop` da semana 5: a chamada é uma expressão que vale o retorno, e o retorno é uma função ([[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]], [[wiki/concepts/expressao-javascript]]).
7. **A vantagem que a aula pergunta e não responde.** `[external]` Pré-configurar uma função para entregar a quem só passa um argumento: `[1, 2, 3].map(adder(10))` dá `[11, 12, 13]` (verificado depois, no ingest do vídeo 04), handlers com o id já fixado, validadores com o limite fixado. A resposta vem com o vídeo seguinte, quando a função vira parâmetro ([[wiki/concepts/callback-javascript]]).
8. **Legenda.** Trocas principais: "INI Gilson"→Ninja, e eu sou; "da Silva"→Daciuk; "soluções"→funções; "nos livros escritos"/"um script"→no JavaScript/em JavaScript; "TSU"/"de dois"/"e de dois"/"iPad 2"→add2; "Ed"/"éder"→adder; "Titanic"→return; "conselho logo"→console.log (2×); "separamos"→parâmetros; "vocal"/"vou com"→invocar/invoco; "entornar três mais"→retornar treze. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/closure-javascript]]
- [[wiki/concepts/currying]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/programacao-funcional]]
- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/naming]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]] (semana 8, vídeo 02).

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]] (semana 8, vídeo 04), o de função como parâmetro que este anuncia.

## Open Questions

- **"O X mas o tipo B"**: deve ser "o x mais o y" (média); literal.
- **"Ela só cria uma função e deu certo" / "quando eu chamo a função, é, certo"**: provavelmente "criei uma função adder, certo" (média); literais.
- **"Chamada de poder" / "Essa idiota vai ser um retorno da EDP"**: o nome da função interna no slide e "essa daí vai ser o retorno do adder"? (baixa). Literais.
- **"Isso vai retornar para 25"**: deve ser "retornar pra mim 5" (média); literal.
- **"No final do ano"**: fim da frase sobre o ponto e vírgula, talvez "no final do return" (baixa).
- **"Vai tu" / "ele tirou três"**: talvez `var add2` e `add2(3)` (média); literais.
- **"Cinco, vocábulo oito"**: `adder(5)(8)` (alta pelo resultado 13); literal.
- **"Quem te viu mais" / "uma força" / "nossa equipa" / "que eu chamei web" / "de mídia"**: ilegíveis (baixa).
- **"No lugar do titânio"** (vídeo 02): pelo "Titanic"→return deste vídeo, provavelmente "no lugar do return"; o raw do vídeo 02 continua literal.

## Raw quotes

- "Você consegue criar uma função dentro de outra função no JavaScript."
- "Eu vou somar 3 com o 2 que eu já tinha passado na primeira vez."
- "Posso fazer duas invocações seguidas com JavaScript."

Retomado em [[wiki/sources/javascript-ninja-escopo-de-funcoes]] (semana 9, vídeo 01): a função dentro de função volta como tema de escopo; ali a aula diz que a interna "só existe enquanto" a externa existe, o que o `adder` deste vídeo já contraria.
