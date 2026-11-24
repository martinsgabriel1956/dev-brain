---
type: source
title: "Operadores de igualdade e relacionais (JavaScript Ninja, aula 03)"
aliases: ["JavaScript Ninja aula 03", "JS Ninja igualdade e relacionais", "03 - Operadores de igualdade e relacionais"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, operadores, igualdade, igualdade-estrita, coercao, tipagem-fraca, tipagem-dinamica, operadores-relacionais, comparacao, boolean, nodejs, repl]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-operadores-de-igualdade-e-relacionais.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Operadores de igualdade e relacionais (JavaScript Ninja, aula 03)

## TL;DR

Terceiro vídeo da primeira aula do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), depois de [[wiki/sources/javascript-ninja-operadores-aritmeticos|operadores aritméticos]], no REPL do [[wiki/entities/nodejs|Node]]. O instrutor se apresenta ("Fernando da Silva" na legenda), o que firma a autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]].

- **`=` atribui, `==` e `!=` comparam.** A comparação "vai me retornar sempre true ou false" ([[wiki/concepts/igualdade-javascript]], [[wiki/concepts/logica-booleana]]).
- **Strings também:** `nome == 'Fernando'` dá true; `nome == pessoa` (Fernando × Maria) dá falso.
- **Conversão de tipos:** `'1' == 1` dá true, "porque JavaScript, ele faz conversão de tipos": é "uma linguagem com tipagem fraca, dinâmica" ([[wiki/concepts/sistema-de-tipos]]).
- **`===` e `!==`** "testam também o tipo": `'1' === 1` é falso. "A gente vai usar sempre a notação com três igual [...] porque isso é mais seguro."
- **Relacionais:** `>`, `<`, `>=`, `<=`, "como a matemática". Para não confundir os sinais, "imagina que [é] um jacaré [...] a boca do jacaré sempre come o maior" ([[wiki/concepts/operadores-relacionais-javascript]]).
- Exemplos: `1 > 2` falso, `2 < 3` true, `1000 > 1000` falso, `1000 >= 1000` true, `40 < 40` falso, `40 <= 40` true.
- Próximo vídeo: funções ([[wiki/concepts/funcoes-javascript]]).

## Key Claims

### Atribuição × igualdade

- "O sinal de igual, ele serve para atribuir um valor a uma variável [...] o operador de atribuição." "Mas os operadores de igualdade, ele servem pra você testar se os valores são iguais a outros ou se valores são diferente de outros."
- `==` "significa 'igual a'"; "sinal de exclamação igual, que significa 'diferente'".
- Resultado: "vai me retornar sempre true ou false". `1 == 2` é falso, "porque não é igual a 2"; `1 != 2` é true; `2 != 2` é falso, "ele é a mesma coisa que 2".
- Com variável: `x == 0` dá true, porque o interpretador "vai pegar o valor de x, 0, e vai verificar".

### Strings

- `'Fernando' == 'Fernando'` dá true "porque a variável Fernando é igual a variável Fernando".
- `var nome = 'Fernando'`, `var pessoa = 'Maria'`: `nome == pessoa` "é falso, porque o nome que está atribuído [é] Fernando, pessoa está atribuído Maria".

### Conversão de tipos

- Uma variável com `'1'`: "eu sei que não é um número, porque ele está entre [...] apóstrofo [...] ou aspas simples". Outra com o número 1.
- Comparadas com `==`, dão true. "Porque JavaScript, ele faz conversão de tipos [...] ele é uma linguagem com tipagem fraca, dinâmica." O detalhe fica "mais pra frente".
- "O JavaScript, quando ele tenta testar algum tipo de valor, ele vai tentar converter [...] para verificar se aquele valor vai ser igual ao outro."

### `===` e `!==`

- "Se eu quiser saber quando [...] realmente é uma string e quando realmente é o número, eu preciso testar o tipo." "O três igual, para testar se é igual a do mesmo tipo, ou um sinal de exclamação e dois sinais [de] igual, que significa diferente, mas o mesmo tipo."
- `'1' === 1` é falso, "porque o número é string, isto não é número". `'1' !== 1` é true.
- "A gente vai usar sempre a notação com três igual, ou o sinal é diferente testando também o tipo, porque isso é mais seguro. Você vai ter certeza [...] que é aquilo que você está testando realmente é aquilo que você quer."

### Relacionais

- "Os operadores relacionais [...] como a matemática": maior que, menor que, "maior igual e menor é igual", "para saber se um número é maior que o outro, é menor que o outro".
- `>=` é "um sinal de maior e um sinal de igual"; `<=`, "um sinal de menor [e] sinal de igual".
- Dica: "imagina que [é] um jacaré [...] jacaré guloso, e a boca do jacaré sempre come o maior"; quando "a boca de jacaré tá indo pro lado contrário", é o sinal de menor.
- `1 > 2` falso; `2 < 3`, `1 < 2`, `10 < 100`, `1000 > 2` true.
- `1000 > 1000` falso, `1000 >= 1000` true, "porque o mil é igual a mil"; `40 < 40` falso, `40 <= 40` true, "porque o 40 não é menor que 40, mas é igual a 40".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para operadores de JavaScript; as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **A recomendação bate com a wiki.** `===` por padrão, `==` só quando a conversão é intencional (o caso clássico é `x == null`), como já está em [[wiki/concepts/igualdade-javascript]]. Os exemplos da NLW (Nunjucks com `==` frouxo) mostram o outro lado.
2. **`==` não "tenta converter" de qualquer jeito.** `[external]` Segue o algoritmo *IsLooselyEqual*: string com número vira número (`'1' == 1`), booleano vira número (`true == 1`, `'1' == true`), objeto vira primitivo (`[] == ''`), e `null` só é igual a `undefined`. Por isso `0 == ''` dá true e `null == 0` dá false (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness).
3. **`!==` não é "diferente, mas o mesmo tipo".** Dá true se o tipo **ou** o valor diferem: `'1' !== 1` é true justamente por serem de tipos diferentes, como a própria demonstração mostra.
4. **`'Fernando'` não é variável.** "A variável Fernando é igual a variável Fernando" descreve dois literais string. Strings se comparam pelo conteúdo; objetos, por referência: `{} === {}` e `[1] === [1]` são falsos (não aparece na aula).
5. **Relacionais também convertem, e de outro jeito.** `[external]` Com duas strings, comparam caractere a caractere (unidades UTF-16): `'10' < '9'` é true. Com tipos mistos, convertem para número: `'10' < 9` é false. `null >= 0` é true enquanto `null == 0` é false, e qualquer comparação com `NaN` dá false. Não existe "`<==`" estrito ([[wiki/concepts/operadores-relacionais-javascript]], [[wiki/concepts/pitfalls-de-linguagem]]).
6. **"Tipagem fraca, dinâmica"** está certo e são dois eixos: dinâmica = o tipo está no valor e é checado em execução; fraca = há conversão implícita. A wiki já separa os dois em [[wiki/concepts/sistema-de-tipos]].
7. **`NaN !== NaN`.** O único valor diferente de si mesmo; para testar, `Number.isNaN` ou `Object.is(NaN, NaN)` ([[wiki/concepts/tipos-primitivos-javascript]]).
8. **Legenda.** Trocas: "Lá"→Olá, "Fernando da Silva"→Fernando Daciuk (alta: o curso e as aulas anteriores), "de script"→JavaScript, "tornar"→retornar (10×), "tudo"/"tu"/"útil"→true, "lamentou"→retornou (5×), "suingue"/"estilingue"→string, "sou mais Turing"→é uma string (média), "quero trecho"/"preço"→três (média-alta), "votação"→notação, "nacionais"/"irracionais"→relacionais, "marca"→maior, "como"→come. Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (se apresenta).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/nodejs]]: REPL das demonstrações.

## Concepts

- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/operadores-relacionais-javascript]] (criado neste ingest)
- [[wiki/concepts/sistema-de-tipos]]
- [[wiki/concepts/logica-booleana]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/funcoes-javascript]]

## Open Questions

- "O número um é igual a nenhum erro na minha história", "ato falho de lei", "o que me tornei Eletro", "diferente da União": a legenda perdeu as expressões da demo do `===`; o resultado (falso, depois true) é claro.
- "Ele vai retornar o nome do BIG": provavelmente "true", mas não é seguro.
- "Minha mãe 2, sim, meu marido 2" é quase certamente "mil maior que 2"; ficou literal.

## Raw quotes

- "porque JavaScript, ele faz conversão de tipos"
- "a gente vai usar sempre a notação com três igual [...] porque isso é mais seguro"
- "a boca do jacaré sempre come o maior"
