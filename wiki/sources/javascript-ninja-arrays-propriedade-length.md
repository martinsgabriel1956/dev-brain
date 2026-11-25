---
type: source
title: "Arrays: a propriedade length (JavaScript Ninja, semana 7, vídeo 02)"
aliases: ["JavaScript Ninja length", "JS Ninja array length", "02 - Arrays - a propriedade length", "percorrer array com while"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, array, length, while, decremento, objetos, off-by-one, undefined]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-arrays-propriedade-length.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Arrays: a propriedade length (JavaScript Ninja, semana 7, vídeo 02)

## TL;DR

Segundo vídeo da semana 7 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), depois de [[wiki/sources/javascript-ninja-operador-modulo|o operador módulo]], que o anunciava. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] (a legenda escreve "array" como "Harry", "rei" e "Harry Potter").

- **Array é objeto embutido:** "não existem arrays, são objetos disfarçados"; como os objetos que já criamos, "eles também têm propriedades e métodos" ([[wiki/concepts/objetos-javascript]]).
- **`length`:** "a quantidade de itens que tem no array" (ele começa dizendo "caracteres" e se corrige) ([[wiki/concepts/array]]).
- **O array do exemplo:** cinco itens de tipos diferentes, índices de 0 a 4: uma string (`'Daciuk'`, inferido), `null`, `true`, um objeto `{ bola: 'azul' }` e "uma função em branco que não faz nada" ([[wiki/concepts/null-e-undefined]]).
- **Revisão do `while` e off-by-one:** de 0 a `< 10` "não mostra o próprio número 10", a não ser com `<= 10` ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
- **Percorrer de trás para frente:** `qtd = array.length` e `while (qtd > 0) console.log(array[qtd--])` mostra `undefined` primeiro ("o quinto não existe") e não chega ao 0; trocar por `>=` não resolve; a versão certa é `while (qtd > 0) console.log(array[--qtd])`, que mostra 4, 3, 2, 1, 0 ([[wiki/concepts/incremento-e-decremento]]).
- **Propriedade do objeto dentro do array:** quando `qtd` vale 3, `array[qtd].bola` mostra "azul" ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).
- **Próximo vídeo:** os métodos do array ([[wiki/concepts/metodos-de-array-javascript]]).

## Key Claims

### Array é um objeto com propriedades e métodos

- "Na verdade não existem arrays, são objetos disfarçados. Como objetos, eles também têm propriedades e métodos."
- "A gente já viu que com objetos a gente pode criar as nossas próprias propriedades e os nossos próprios métodos"; os objetos "embutidos no JavaScript" já vêm com as suas. "Array, ele é um deles."

### length

- "Ele conta a quantidade de caracteres, ou melhor, a quantidade de itens que tem no array."
- Contar à mão ("1, 2, 3, 4 e 5") ou usar a propriedade: "ele vai retornar para mim quantos elementos eu tenho".

### Revisão do while

- O loop roda "em cima de um valor true ou falso", "incrementa esse contador [...] e no momento específico ele sai do loop para que não haja um loop infinito."
- "10 não é menor que 10 [...] Por isso ele não mostra o próprio número 10 aqui, a não ser que eu fizesse num menor igual a 10."

### O array de cinco tipos

- "Eu tenho cinco elementos do array, que vai do zero até o 4." O primeiro é uma string, o segundo `null`, o quarto "um objeto com a propriedade bola, que tem um valor azul", e o quinto "uma função em branco que não faz nada". O terceiro (`true`) só aparece claro na saída final.
- Escrever `array[0]`, `array[1]`... à mão funciona, "só que eu posso também utilizar o [while] para fazer isso".

### Percorrendo com length e while

- "A primeira coisa que eu preciso fazer era saber qual a quantidade de itens"; guarda em `qtd = array.length`, "igual a 5".
- Primeira versão (`qtd > 0`, `array[qtd]` e diminui): "ele tentou imprimir o quinto [...] que o quinto não existe", "por isso que ele retornou undefined", e "ele não chegou a entrar no 0".
- Segunda (`>=`): "aquilo acabou diminuindo e ele acabou retornando menos", então "não precisa ter o igual".
- Terceira (`--` antes): "agora ele mostra correto: a propriedade 4 [...], propriedade 3, o 2 true, 1 que é o null, e o zero."
- "Usando essa propriedade length do array, eu consegui [passar] por todos os elementos, utilizando somente o while, sem precisar colocar manualmente cada um."

### Objeto dentro do array

- "Se é o item 3 do meu array, porque ele é um objeto, [...] eu posso tentar pegar [a] bola": `if` com `qtd` igual a 3 e `array[qtd].bola`. Saída: "olha só o azul que ele retornou aqui", e os outros valores normais.
- "Basicamente tudo [...] consegue trabalhar com o objeto"; "a gente vai ver isso mais pra frente também, como as outras coisas funcionam como objetos."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para arrays básicos de JavaScript; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base). Os três loops foram reproduzidos no Node com o array `['Daciuk', null, true, { bola: 'azul' }, function () {}]` e batem com o que a aula descreve. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length

1. **`length` não é contagem.** `[external]` É o maior índice mais 1. Com `var s = []; s[9] = 1`, `s.length` dá 10 com um item só; com arrays sem buracos, os dois coincidem. Também é gravável: `arr.length = 2` corta o array. Por isso o último índice é `length - 1`, a origem do `undefined` na primeira versão.
2. **Por que cada versão falha.** O pós-decremento devolve o valor antigo ([[wiki/concepts/incremento-e-decremento]]):
   - `while (qtd > 0) console.log(array[qtd--])` lê os índices 5, 4, 3, 2, 1: `undefined` primeiro, sem o 0.
   - `while (qtd >= 0) console.log(array[--qtd])` lê 4, 3, 2, 1, 0 e depois -1: o "retornando menos" é o `array[-1]`, `undefined`. A legenda não deixa claro se ele mudou o `--` de lugar já aqui; essa é a combinação que bate com a saída (inferência, média).
   - `while (qtd > 0) console.log(array[--qtd])` decrementa antes de ler: 4 a 0, sem sobra.
3. **`array[-1]` não é o último.** `[external]` Índice negativo é só uma chave de propriedade que não existe, por isso dá `undefined` sem erro. Para o último, `arr[arr.length - 1]` ou `arr.at(-1)` (ES2022) ([[wiki/concepts/null-e-undefined]]).
4. **A forma usual é crescente.** `[external]` `for (var i = 0; i < arr.length; i++)` percorre na ordem, e `i < length` evita o off-by-one que a aula enfrentou. O percurso decrescente com `--i` serve para remover itens durante o loop sem pular índices ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
5. **`.bola` só quando o item é objeto.** `[external]` `array[qtd].bola` funciona porque o `if` garante o índice 3. Nos outros, `'Daciuk'.bola` e `true.bola` dão `undefined` (o primitivo vira objeto temporário), mas `null.bola` lança `TypeError`. Encadear `?.` (`array[i]?.bola`) protege ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).
6. **"Objetos disfarçados" de novo.** É a terceira vez no curso. `typeof []` dá `'object'` e índices são chaves (`arr['3']` funciona), mas o array é um objeto exótico: `length` se atualiza sozinho e os métodos vêm de `Array.prototype` ([[wiki/concepts/array]], [[wiki/concepts/objetos-javascript]]).
7. **Legenda.** Muito ruidosa. Trocas principais: "concursos jovens de biquíni Gilson"→com o curso JavaScript Ninja, eu sou o; "da Silva"→Daciuk; "Harry"/"rei"/"Rei"/"REI" (cerca de 40×)→array; "Harry Potter"→array ponto; "lei"/"Lei"→length; "quê td"/"q td"/"TD"→qtd; "Marco Zero"/"formar"→maior que zero/for maior; "nu"/"ONU"→null; "Tu"/"tu"→true; "andei"→undefined; "áudio"→while; "wi fi"→if. Mantidos literais: "Arrego", "o anel", "o cliente", "o que entender"/"Kennedy"/"o que atender" (provavelmente `qtd`), "forma quisera", "fantochada", "show de bola azul". Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/array]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/notacao-de-ponto-e-colchetes]]
- [[wiki/concepts/metodos-de-array-javascript]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-operador-modulo]].

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]] (semana 7, vídeo 03), com o `push` e o `for`.

## Open Questions

- **Primeiro item do array**: a legenda dá "uma historinha da Chuck" e "o zero da Silva"; como "da Silva" é o ASR de "Daciuk" no curso todo, deve ser a string `'Daciuk'` (média).
- **"Vá lá, array. Arrego."**: provavelmente `var arr = [...]` (média); o nome da variável ficou incerto. O raw mantém "Arrego".
- **"Utilizar o anel" / "o cliente faz"**: devem ser o `while` (média), como "áudio" e "ai" nos vídeos anteriores; literais.
- **"O que entender" / "Kennedy" / "o que atender"**: devem ser `qtd` (média-alta); literais, porque também podem ser outras palavras.
- **"Enquanto Kennedy forma quisera"**: provavelmente "enquanto qtd for maior que zero" (média); literal.
- **"São pessoas jurídicas repetição"**: provavelmente "são estruturas de repetição" (média); literal.

## Raw quotes

- "na verdade não existem arrays, são objetos disfarçados"
- "ele tentou imprimir o quinto [...] que o quinto não existe"
- "olha só o azul que ele retornou aqui"
