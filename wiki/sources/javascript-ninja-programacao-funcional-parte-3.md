---
type: source
title: "Programação funcional, parte 3: funções como parâmetro (JavaScript Ninja, semana 8, vídeo 04)"
aliases: ["JavaScript Ninja programação funcional parte 3", "JS Ninja showFunction", "04 - Functional Programming - parte 3", "JavaScript Ninja função como parâmetro"]
date_created: 2026-11-25
date_updated: 2026-11-26
source_count: 0
tags: [javascript, programacao-funcional, funcoes-de-primeira-classe, callback, funcao-de-ordem-superior, objeto-como-parametro, funcao-anonima, ponto-e-virgula]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-programacao-funcional-parte-3.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Programação funcional, parte 3: funções como parâmetro (JavaScript Ninja, semana 8, vídeo 04)

## TL;DR

Quarto vídeo da semana 8 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), que fecha a série de programação funcional aberta em [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("da Silva" na legenda). O próximo vídeo é o desafio da semana.

- **Recapitulação:** funções são objetos de primeira classe: dá para criá-las como literal, atribuí-las a variáveis e retorná-las de outras funções, "da mesma forma que você faz essas três coisas com objetos" ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **Objeto como parâmetro:** `var car = { color: 'yellow' }` e uma função que recebe o objeto e retorna `car.color`. Primeiro erro ao vivo: um ponto e vírgula dentro do objeto literal, "dentro do objeto não pode ter" ([[wiki/concepts/objetos-javascript]]).
- **Função como parâmetro:** `showFunction(fn)` recebe uma função "como um parâmetro normal [que] poderia ser qualquer tipo de valor" e retorna a invocação dela, `return fn()` ([[wiki/concepts/callback-javascript]], [[wiki/concepts/funcao-de-ordem-superior]]).
- **Primeiro formato:** criar antes uma segunda função e passá-la pelo nome, "sem invocar", sem os parênteses.
- **Segundo formato:** passar a função "direto aqui no parâmetro". Pode ter nome "ou não, tanto faz"; ele usa anônima "só para ficar menos coisa escrita" ([[wiki/concepts/naming]]).
- **Lugar no curso:** "oitav[a] aula", de "mais ou menos umas 30 aulas"; programação funcional volta muitas vezes ([[wiki/concepts/programacao-funcional]]).

## Key Claims

### Recapitulação

- "A gente já viu que [...] funções [...] são objetos de primeira classe de JavaScript: que você consegue criar funções literais [...], atribuir funções a variáveis, que você consegue retornar funções de outras funções, da mesma forma que você faz essas três coisas com objetos."
- No início da lista ele diz também "passar funções por parâmetros" e se corrige; o parâmetro é o tema deste vídeo.

### Objeto como parâmetro

- "Da mesma forma que você consegue passar objetos por parâmetros para funções": uma função que "vai receber [...] um objeto" e "vai retornar [...] a color do objeto. Bem simples, coisa que a gente já fez [em] alguns exercícios anteriores."
- "Ele deve retornar a cor do meu carro."
- O erro: "coloquei um ponto e vírgula dentro do objeto. Então ele disse que ele não esperava isso. [...] Dentro do objeto não pode ter [...] um ponto e vírgula." Corrigido, o console mostra "yellow".

### Função como parâmetro

- "Da mesma forma que você consegue passar um objeto por parâmetro para uma função e manipulá-lo dentro da função, da mesma forma você também consegue fazer com funções."
- "Eu recebo ela aqui como um parâmetro normal. Poderia ser qualquer tipo de valor. Poderia ser um array, poderia ser uma variável, poderia ser um objeto [...]. Mas eu posso passar uma função, e como é uma função, eu posso invocar."
- "O retorno dessa função aqui vai ser a invocação da função passando por parâmetro."

### Duas formas de passar

- "A gente poderia criar uma segunda função aqui, passar. Ou [...] pode passar diretamente ela. Não preciso passar um parâmetro, colocar uma variável, ou passar o nome da função, não."
- Primeiro formato: "eu posso criar uma segunda função, que eu vou usar para retornar", e no `console.log` invoca `showFunction` passando-a "sem invocar". "Esse é o primeiro formato."
- Segundo formato: "vou passar a função [...] direto aqui no parâmetro. Eu posso nomear ela, como não, tanto faz. Vou usar a função anônima aqui, só para ficar menos [...] coisa escrita para você, para facilitar a visualização."
- "Isso é pra você ver o poder que a gente tem utilizando o formato de programação funcional."

### O curso

- "A gente vai falar muito sobre isso no curso [...]. [Essa é a] oitav[a] aula, e ele vai ter mais ou menos umas 30 aulas, um total do curso."
- "Até o próximo vídeo, onde nós vamos mostrar o desafio da semana."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para callbacks ou funções de ordem superior em JavaScript básico. As precisões vêm da MDN e de conhecimento base, marcadas `[external]`; os exemplos foram reproduzidos no Node 22.23. https://developer.mozilla.org/en-US/docs/Glossary/Callback_function

1. **Os nomes que faltam.** `[external]` A função passada é um *callback*, e `showFunction`, que recebe função, é uma *função de ordem superior*. O `adder` do vídeo anterior também é de ordem superior, porque devolve função. A aula não usa nenhum dos dois termos ([[wiki/concepts/callback-javascript]], [[wiki/concepts/funcao-de-ordem-superior]]).
2. **Passar a função, não o resultado.** `[external]` "Sem invocar" é o ponto central: `showFunction(fn)` passa a função; `showFunction(fn())` passa o que ela devolve, e `return fn()` lá dentro estoura com `TypeError: fn is not a function` (verificado). A wiki já registrava a distinção referência × execução em listeners ([[wiki/concepts/funcoes-javascript]]).
3. **Ponto e vírgula no objeto.** `[external]` `{ color: 'yellow'; }` dá `SyntaxError: Unexpected token ';'` (verificado). No objeto literal as propriedades se separam com vírgula; o `;` termina instruções, e o objeto literal é uma expressão ([[wiki/concepts/pitfalls-de-linguagem]], [[wiki/concepts/expressao-javascript]]).
4. **"Tanto faz" o nome.** Três vídeos antes, o curso passou a exigir nome em toda função ([[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]). Aqui o callback é anônimo "só para ficar menos coisa escrita". `[external]` O callback passado direto é justamente o caso em que a inferência do ES2015 não dá nome, e o stack trace sai sem nome ([[wiki/concepts/naming]]).
5. **O uso de todo dia.** `[external]` `map`, `filter`, `forEach`, `addEventListener`, `setTimeout` e `then` são funções de ordem superior: `[1, 2, 3].map(function dobro(x) { return x * 2 })` dá `[2, 4, 6]` (verificado). Com isso, a pergunta "qual a vantagem disso?" do vídeo anterior fica respondida: `[1, 2, 3].map(adder(10))` entrega a função curried como callback ([[wiki/concepts/metodos-de-array-javascript]], [[wiki/concepts/currying]]).
6. **"Manipulá-lo dentro da função".** `[external]` O objeto chega por referência compartilhada; mudar `car.color` dentro da função muda o `car` de fora. A semana 5 já registrava isso ([[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]).
7. **Arrow.** `[external]` `showFunction(() => 'arrow')` dá `'arrow'` (verificado). É o formato mais comum hoje para o callback anônimo ([[wiki/concepts/arrow-functions]]).
8. **Duração do curso.** "Mais ou menos umas 30 aulas" no total; esta é a oitava, o que confirma que no curso "aula" e "semana" coincidem ([[wiki/entities/javascript-ninja]]).
9. **Legenda.** Trocas principais: "na EU SOU O da Silva"→Ninja. Eu sou o [Fernando] Daciuk; "gente antiga viu"→a gente já viu; "cola"→color (3×); "e ela"→yellow (2×); "show infantil"/"show do infantil"→showFunction (6×); "uma rei"→um array; "ponto de vila"→ponto e vírgula; "Sei que vou catar"→Sem invocar; "paredes"/"Paraná"→parâmetro; "Conselho logo"/"Fotolog"→console.log. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/funcao-de-ordem-superior]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/programacao-funcional]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/metodos-de-array-javascript]]
- [[wiki/concepts/currying]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]] (semana 8, vídeo 03). O desafio da semana 8, anunciado no fecho, não está na wiki.

## Open Questions

- **Nome da função do objeto**: "de caracol" (4×) e "Guedes cola" sugerem `getCarColor` ou `getColor` (média); "marcar ponto" deve ser `mycar.` ou `o car.` antes de `color` (média). Literais.
- **Nomes do segundo exemplo**: "Xô xô xô", "choldra" e "show chão" devem ser `showFunction` (média); "elefante", "fantochada", "fantoche" e "rede internet"/"na internet" são o callback e o texto que ele devolve (baixa). Literais.
- **"Fantoche controlado com sucesso"**: provavelmente a string devolvida, algo como "função executada com sucesso" (média); literal.
- **"Que monitora a função já está definido"**: talvez "que no momento a função já está definida" (média); literal.
- **"O que a função tiver jantar"**: talvez "tiver para retornar" (baixa); literal.
- **"O gato de Cartola" / "à noite" / "chamam de mídia" / "Bonilha" / "ao fórum profissional"**: ruído de legenda (baixa).
- **"Em seu oitavo aula"**: deve ser "essa é a oitava aula" (alta pelo contexto).

## Raw quotes

- "Dentro do objeto não pode ter, não pode ter um ponto e vírgula."
- "Eu recebo ela aqui como um parâmetro normal. Poderia ser qualquer tipo de valor."
- "Eu posso nomear ela, como não, tanto faz."

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-escopo-de-funcoes]] (semana 9, vídeo 01), depois da correção do desafio 8: escopo de funções e hoisting.
