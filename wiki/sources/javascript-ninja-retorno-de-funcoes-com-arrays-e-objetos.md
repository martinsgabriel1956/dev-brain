---
type: source
title: "Retorno de funções com arrays e objetos (JavaScript Ninja, semana 5, vídeo 01)"
aliases: ["JavaScript Ninja retorno de funções", "JS Ninja função retornando array e objeto", "01 - Retorno de funções com arrays e objetos"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, funcoes, return, array, objetos, metodos, tipos-primitivos, escopo]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Retorno de funções com arrays e objetos (JavaScript Ninja, semana 5, vídeo 01)

## TL;DR

Primeiro vídeo da "quinta aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), gravado "após finalizar a revisão do nosso desafio 4". Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). Continua o tema de [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes|escopo de variáveis e funções]].

- **Objetos e funções** são "basicamente as duas partes mais importantes da linguagem" ([[wiki/concepts/funcoes-javascript]], [[wiki/concepts/objetos-javascript]]).
- **Até aqui, só primitivos:** número, string, booleano; sem `return`, a função devolve o valor padrão (a legenda perde a palavra, que deve ser `undefined`) ([[wiki/concepts/tipos-primitivos-javascript]], [[wiki/concepts/null-e-undefined]]).
- **Um `return` só:** o segundo `return` é ignorado; a função "vai sair da função, não vai fazer mais nada".
- **Mais de um valor? Retorne um array:** `return [1, 2, 3]`, e o índice vem direto da chamada, `funcao()[0]` traz 1, `funcao()[2]` traz 3; um índice que não existe dá `undefined` ([[wiki/concepts/array]]).
- **Ou retorne um objeto:** `prop1: 1`, `prop2: 'Fernando'`, mais um método que retorna `prop3`. Lê-se com ponto na chamada ou guardando o retorno numa variável ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **Ligação com escopo:** "eu não preciso criar [...] um objeto no meu escopo global"; dá para criar o escopo dentro da função e expor o retorno ([[wiki/concepts/escopo-javascript]]).
- Próximo vídeo: [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos|parâmetros de funções como arrays e objetos]].

## Key Claims

### Revisão: retorno de primitivos

- "A gente precisa da palavra-chave [function]." A função pode retornar um número, "uma string qualquer" e "valores booleanos".
- Sem retorno: "se uma função [...] não tiver retorno nenhum, não tiver nada, então, automaticamente, aquela função, ela vai [retornar undefined]" (a legenda dá "se tornando diferente").
- "Esses são os valores primitivos do JavaScript, que são também string, boolean, [undefined] e null", usados "nos últimos exercícios [...] para retornar valores de função e de método de objeto".

### Um único `return`

- "Ele só pode ter um tipo de valor." Com dois `return` seguidos, "ele simplesmente vai ignorar a segunda linha [...] vai retornar a primeira linha e vai sair da função, não vai fazer mais nada".

### Retornando array

- "Se eu precisar retornar mais de um valor, que eu posso fazer? [...] Posso retornar um array."
- A vantagem: "eu posso acessar as propriedades do array, porque, como a função está retornando pra mim array, eu consigo acessar, após executar a função".
- Índice 0 traz o primeiro item; índice 2 traz o 3; índice 5 "não existe" (a legenda perde a palavra, deve ser `undefined`).

### Retornando objeto

- "Além de funções, pode ser array e podem ser objeto também." A função retorna "direto" um objeto literal com `prop1`, `prop2` ("Fernando") e um método que retorna `prop3`.
- Executar a função "me traz o objeto [...] com todas as propriedades que eu preciso". Leitura com ponto: "Ponto, porque eu estou no objeto."
- Guardando numa variável: depois de `var x = funcao()`, "eu não preciso passar de novo os parênteses", e `x.prop2` traz o valor.
- "É uma função que está dentro de um objeto, então ele chama de método"; executado, "vai trazer o retorno daquele método".
- "Eu posso criar um escopo dentro de uma função e usar o retorno dessa função como as minhas propriedades, como um objeto [...] com método."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para `return` e valores de retorno no JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **"Só pode ter um tipo de valor" quer dizer um valor.** `[external]` Um `return` devolve um único valor, mas a mesma função pode devolver tipos diferentes em ramos diferentes; não há checagem. O que a aula mostra é que o primeiro `return` encerra a execução, e o código seguinte vira código morto.
2. **Array e objeto são o jeito de devolver vários valores.** `[external]` O JavaScript não tem tuplas nem retorno múltiplo (como o Go). Desde o ES2015 se lê o retorno com desestruturação: `const [a, b] = f()` ou `const { prop1 } = f()` ([[wiki/concepts/desestruturacao-javascript]]). Array serve quando a ordem importa (o padrão do `useState` do React); objeto, quando nomes importam e a ordem pode mudar.
3. **Índice inexistente dá `undefined`, sem erro.** `[external]` `f()[5]` em array de três itens é `undefined`; já ler propriedade de `undefined` (`f()[5].x`) lança `TypeError` ([[wiki/concepts/null-e-undefined]]).
4. **Cada chamada cria um objeto novo.** `[external]` `funcao().prop1` executa a função e joga o objeto fora; duas chamadas devolvem dois objetos diferentes (`f() !== f()`). Por isso a aula guarda o retorno numa variável. É o germe da *factory function*.
5. **"Método que retorna prop3" depende de como foi escrito.** `[external]` Dentro do objeto literal, o método precisa de `this.prop3` (ou de uma variável local que o objeto capture); `prop3` solto daria `ReferenceError`. A legenda não deixa ver qual forma foi usada. A semana 3 já tinha escrito métodos com o nome do objeto em vez de `this` ([[wiki/sources/javascript-ninja-metodos-de-objeto]]).
6. **"Criar um escopo dentro de uma função e usar o retorno" é o module pattern.** `[external]` Na era ES5, função (em geral IIFE) com variáveis locais que devolve um objeto com métodos, que as enxergam por closure, era o jeito de ter encapsulamento sem poluir o global ([[wiki/concepts/poluicao-do-escopo-global]], [[wiki/concepts/stale-closure]]). A aula não usa o nome nem mostra closure; o curso promete voltar ao assunto.
7. **Lista de primitivos incompleta de novo.** A fala lista string, boolean, [undefined] e null (number vem antes como "número"); faltam `symbol` e `bigint`, como na [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos|semana 3]] ([[wiki/concepts/tipos-primitivos-javascript]]).
8. **Legenda.** Trocas principais: "na índia"→Ninja, "da Silva"→Daciuk, "rei"/"Harry"→array (alta), "estilingue"/"distingue"/"tirinhas"→string, "bolha"→boolean, "nu"→null, "permitiu o uso"→primitivos, "próprio um"/"top 2"/"top 3"/"próprio trecho"→`prop1`/`prop2`/`prop3`, "parentes"→parênteses. O nome da função da demo ("fantochada", "infantil", "uma fonte", "uma Photoshop") ficou ilegível (provavelmente `myFunction`); a variável do retorno ("velhos") também (provavelmente `value`). Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/array]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/desestruturacao-javascript]]
- [[wiki/concepts/poluicao-do-escopo-global]]

## Open Questions

- **"Funções de Estado"** na abertura: pode ser "funções de novo" (média-baixa); literal.
- **"Eterno retorno falso", "possa retornar no próximo", "se tornando diferente"**: provavelmente `return true`, `return false`, `return null` e "retornar undefined" (média). Literais.
- **"De parede"** na lista de primitivos: provavelmente `undefined` (média-baixa); literal.
- **"Vai me olhando e fala isso, porque não existe"**: provavelmente "vai me retornar undefined" (média).
- **"Prop3 vai receber outro método"**: talvez seja `prop3` com outro valor e um `prop4` (ou `method`) que retorna `prop3`; "você chama para três, ele vai trazer a fala no chão" não decifra o valor de `prop3`.
- **"As propriedades do Sr. Estão"**: provavelmente "do array. Então" (média); literal.

## Raw quotes

- "objetos e funções são basicamente as duas partes mais importantes da linguagem"
- "se eu precisar retornar mais de um valor, que eu posso fazer? Eu posso retornar [...] um array"
- "eu posso criar um escopo dentro de uma função e usar o retorno dessa função como as minhas propriedades"
