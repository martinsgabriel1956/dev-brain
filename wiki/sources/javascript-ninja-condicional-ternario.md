---
type: source
title: "Condicional ternário (JavaScript Ninja, semana 4, vídeo 02)"
aliases: ["JavaScript Ninja ternário", "JS Ninja operador ternário", "02 - Condicional Ternário"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, operador-ternario, condicionais, expressoes, truthy-falsy, legibilidade]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-condicional-ternario.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Condicional ternário (JavaScript Ninja, semana 4, vídeo 02)

## TL;DR

Segundo vídeo da "quarta aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), depois de [[wiki/sources/javascript-ninja-truthy-e-falsy|truthy e falsy]]. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda, a deformação de sempre). Legenda muito deformada; as demos foram reconstruídas pelo contexto.

- **O que é:** o ternário "substitui o if": "uma forma mais fácil, mais prática ou menor [...] de criar o if", que em alguns casos deixa o código "mais legível" ([[wiki/concepts/operador-ternario-javascript]]).
- **Sintaxe:** "condição, interrogação, o resultado se [verdadeiro], dois pontos, o resultado [se] falso". A condição pode ser "um valor de uma variável", testado como truthy ou falsy ([[wiki/concepts/truthy-e-falsy]]).
- **Demo:** `1 === 2 ? true : false` dá `false`; com `2`, `true`. O `if` equivalente ocupa "uma, duas, três, quatro, cinco linhas" e "cheio de chaves".
- **Atribuição direta:** o exemplo do desafio 3, o artigo "o"/"a" conforme `pessoa.sexo`, vira `sexo = pessoa.sexo === 'feminino' ? 'a' : 'o'`: "isso aqui vai ser avaliado, eu vou pegar o resultado e já vou colocar direto" na variável ([[wiki/concepts/expressao-javascript]]).
- **Só para verificações pequenas:** com condições longas "vai ficar ruim de ler, as pessoas vão bater em você". Economiza "três ou quatro linhas".
- **Com truthy e falsy:** `var carro = 'sim' ? 'porta' : 'janela'` dá `'porta'`, porque string preenchida é truthy; com `false`, `'janela'`.
- Sobre ensinar o ternário só agora: "as coisas têm que ser na hora certa". Próximo vídeo: escopo de variáveis.

Continua em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]] (semana 4, vídeo 03: escopo de variáveis e funções).

## Key Claims

### Definição

- "O condicional ternário [...] ele substitui o if." "Ele vai criar uma forma mais fácil, mais prática ou menor, assim, de criar o if."
- "Em alguns momentos vai ter alguns códigos que ficarão mais legíveis utilizando-se o operador ternário."
- "A condição pode ser um valor de uma variável", e então vale o truthy/falsy do vídeo anterior.
- "Eu vou colocar o sinal de interrogação, [...] se o valor é truthy, [...] ele vem logo após o sinal de interrogação. Se [...] for falso, vou colocar [...] dois pontos, e vou adicionar o valor."

### Demonstração

- "Tem lá: um igual a dois. Se isso for [verdadeiro], vou retornar true; se não, [...] falso. Então, um não é igual a dois, então ele retornou direto falso."
- "Ele avaliou essa instrução aqui. Ele já conseguiu retornar o resultado." Com `2` no lugar do `1`, retorna `true`.
- "Olha só a diferença de tamanho que fica quando eu uso o if ou quando eu uso o ternário": cinco linhas com chaves contra uma.

### O exemplo do desafio 3

- No desafio 3 ([[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]), a frase precisava de "o" para masculino e "a" para feminino. A solução com `if` criava `var sexo` com um padrão e trocava se `pessoa.sexo` fosse feminino.
- Com ternário: "Se for [...], eu já estou fazendo atribuição. Olha só: isso aqui vai ser avaliado, eu vou pegar o resultado e já vou colocar direto" na variável `sexo`. "Olha que legal, já fiz direto aqui atribuição."

### Quando usar

- "Você vai utilizar bastante [...] quando você for fazer verificações, verificações pequenas."
- Verificações grandes, com vários `===` e `||`, "vai ficar ruim de ler, as pessoas vão bater em você, não vai ser legal".
- "Algumas vezes ele pode dificultar para você, se você foi tentar fazer a utilização do ternário [...] com um valor muito grande."

### Com truthy e falsy

- `var carro = 'sim' ? 'porta' : 'janela'` (string reconstruída; a legenda diz "a palavra Tim"): "isso aqui é uma palavra [...] entre aspas simples. Então isso aqui é um valor [...] verdadeiro", e `carro` recebe `'porta'`.
- Com `false` na condição, "ele vai colocar a janela".

### Didática

- Antecipando a queixa "você tivesse falado isso antes, tinha resolvido vários problemas quando estava fazendo os desafios": "as coisas têm que ser na hora certa". A informação está na internet, "mas você precisa ter o momento certo para aprender essas coisas".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para o operador condicional; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **O ternário é expressão, não "instrução".** `[external]` A aula diz "isso aqui é uma instrução", mas é justamente por ser expressão (produz valor) que cabe numa atribuição, num argumento ou num template literal. O `if` é que é instrução. A source do vídeo 04 da semana 2 já antecipava isso ([[wiki/concepts/expressao-javascript]], [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]).
2. **Substitui só o `if`/`else` que escolhe um valor.** O ternário exige os dois ramos e devolve um valor; não serve para `if` sem `else`, para vários comandos por ramo nem para `else if` longo sem perder legibilidade ([[wiki/concepts/estruturas-condicionais-javascript]]).
3. **`cond ? true : false` é redundante.** `[external]` `1 === 2` já é booleano; o ternário não acrescenta nada. A regra `no-unneeded-ternary` do ESLint aponta esse padrão. Para converter um valor qualquer, `Boolean(x)` ou `!!x` ([[wiki/sources/javascript-ninja-truthy-e-falsy]]).
4. **A condição usa *ToBoolean*, como o `if`.** Por isso `'sim' ? 'porta' : 'janela'` dá `'porta'` e `'' ? ...` daria `'janela'` ([[wiki/concepts/truthy-e-falsy]]).
5. **Nome oficial: operador condicional.** `[external]` "Ternário" vem de ser o único operador do JavaScript com três operandos (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator).
6. **Precedência e associatividade.** `[external]` O ternário tem precedência baixa (só atribuição, `yield` e vírgula são menores) e associa à direita: `a ? b : c ? d : e` é `a ? b : (c ? d : e)`. Ternários aninhados são o caso típico do "ruim de ler" da aula.
7. **No JSX, ternário é a forma segura.** `cond ? <A /> : null` evita o `0` renderizado que `cond && <A />` produz quando `cond` é `0` ([[wiki/concepts/renderizacao-condicional]], [[wiki/concepts/operadores-logicos-javascript]]).
8. **Legenda.** Trocas principais: "Tininha"→Ninja, "da Silva"→Daciuk, "tornaria"/"alternar"/"cenário"→ternário, "juiz"/"hit"/"Wi-Fi"/"iPhone"→if, "forte"→truthy, "entornar tudo"→retornar true, "app"→'a', "variava o"→a variável, "aponta o"→ponto, "suingue"→string, "Fauci"→false, "Vietname"→GitHub, "esse corpo de variados"→escopo de variáveis. Trechos como "sou gay", "sexo anal serviu por padrão", "sem ser viado" e "o canalha" são artefatos do reconhecimento de voz sobre o código do desafio (`'a'`, `'o'`, `undefined`, "ternário"), não fala do instrutor; ficaram literais no raw pela regra de não adivinhar. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/operador-ternario-javascript]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/operadores-logicos-javascript]]
- [[wiki/concepts/renderizacao-condicional]]

## Open Questions

- **Código do desafio 3.** A reconstrução `sexo = pessoa.sexo === 'feminino' ? 'a' : 'o'` sai de "colocaria o 'a'", "pessoa lá ponto sexo" e "se for feminino vai se beijar [ser 'a'?], se não [...] vai ser o certo ['o'?]" (média). O valor padrão do `if` ("pô difícil", "sexo anal serviu por padrão") pode ser `'o'` ou `undefined`.
- **A string do exemplo do carro.** "A palavra Tim" pode ser `'sim'` ou outra palavra; o resultado (`'porta'`) não muda.
- **"Se um igual time B" e "meus valores era falso":** provavelmente `a === b` e "os valores truthy e falsy"; literais.
- **"Ele está dizendo que a pessoa não existe":** provavelmente um `ReferenceError` ao vivo, porque o objeto `pessoa` não tinha sido criado no console; ele cria `pessoa` com `sexo: 'masculino'` e repete.

## Raw quotes

- "uma forma mais fácil, mais prática ou menor, assim, de criar o if"
- "isso aqui vai ser avaliado, eu vou pegar o resultado e já vou colocar direto"
- "as coisas têm que ser na hora certa"
