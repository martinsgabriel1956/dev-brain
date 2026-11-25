---
type: source
title: "Arrays: o método push() e o loop for (JavaScript Ninja, semana 7, vídeo 03)"
aliases: ["JavaScript Ninja push", "JS Ninja loop for", "03 - Arrays - método push() e Loop for", "push e for JavaScript Ninja"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, array, push, for, loops, funcoes-de-primeira-classe, operador-virgula, off-by-one]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-arrays-metodo-push-e-loop-for.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Arrays: o método push() e o loop for (JavaScript Ninja, semana 7, vídeo 03)

## TL;DR

Terceiro vídeo da semana 7 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 10 min), depois de [[wiki/sources/javascript-ninja-arrays-propriedade-length|arrays e a propriedade length]], que anunciava "o método do array". Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]]. A legenda escreve "push" como "pois", "array" como "Harry"/"rei" e "for" como "forte"/"foco".

- **`push`:** "serve para adicionar um item no final do array"; "push significa empurrar". A alternativa, reescrever o array inteiro com o item novo, "não é inteligente" ([[wiki/concepts/metodos-de-array-javascript]]).
- **Retorno:** "o array ponto push, ele já retorna o length do array": de 6 para 7 itens ([[wiki/concepts/array]]).
- **Qualquer valor:** objeto (`{ carro: 'BMW' }`), outro array, `null` e até uma função `soma(x, y)`, chamada depois pelo índice: sem argumentos não dá um número; com 1 e 2, "ele vai retornar três" ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **Prévia de programação funcional:** "eu poder passar uma função [como] parâmetro de um outro método", assunto para "mais para frente" ([[wiki/concepts/programacao-funcional]]).
- **`for`:** "a mesma ideia" do `while`, com "uma sintaxe um pouco diferente": inicialização, condição e expressão final no cabeçalho, "as três condições de uma só vez" ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
- **Várias variáveis na inicialização:** `for (var num = 2, arroz = 3; ...)`, incrementando as duas ([[wiki/concepts/operador-virgula-javascript]]).

## Key Claims

### Reescrever × push

- Para adicionar um item, "a primeira [forma] é você escrever todo o seu array" de novo, já com o item; `length` passa a 6. "Só que isso não é inteligente."
- O array "é um tipo de objeto", "tinha a propriedade length, e ele também tem um método chamado push".
- "Push significa empurrar. Então [...] eu vou empurrar um valor para dentro do meu array."

### O que push devolve e o que entra

- "Você pode ver que o array ponto push, ele já retorna o length do array. Então eu, por exemplo, tinha seis. [...] Agora eu tenho sete itens."
- Depois do push, o objeto novo é lido pelo índice ("sei que ele começa em zero") e pela propriedade, dando "um valor BMW"; o array dentro do array é "a chave 5".
- "Você pode adicionar qualquer tipo de valor": "um nulo no final", "um array que tenha a, b, c".

### Função dentro do array

- "Eu vou criar uma função [...] soma, [que] vai receber um parâmetro x, um parâmetro y, e vai retornar somando x mais y." Com ela, "agora eu tenho oito itens".
- Lida pelo índice 7, mostra a função; invocada sem argumentos não devolve número ("porque eu não passei nenhum parâmetro"); "passar um, dois, ele vai retornar três".
- "A gente está vendo algumas coisas de programação funcional no JavaScript"; passar função por parâmetro fica "mais para frente, mas é legal você saber que isso é bastante possível."

### O for

- "Eles têm basicamente a mesma ideia, que é gerar uma estrutura de repetição, mas ele tem uma sintaxe um pouco diferente."
- "O primeiro parâmetro é o inicializar. O segundo parâmetro é uma condição. O terceiro parâmetro, a expressão final."
- Com o `while`, `num = 0` ficava fora, a condição no cabeçalho e o `++` dentro; com o `for`, "a gente consegue colocar dentro da própria expressão do for todos os nossos parâmetros."
- Revisão do off-by-one: com `< 20`, "ele vai imprimir os números de 0 a 20, além de 0 a 19, no caso [...] Como 20 é igual a 20, não é menor."

### Várias variáveis

- "Aqui você pode inicializar quantas variáveis você precisar": `num` começa em 2 e `arroz` em 3, enquanto `num` for "menor que cinco"; "incrementar o arroz aqui também, se eu quiser", no corpo ou "aqui em cima".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para `push` e `for` no JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base). Os exemplos foram reproduzidos no Node. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push

1. **`push` muda o array e aceita vários itens.** `[external]` Ele altera o array no lugar (não devolve cópia) e recebe vários argumentos: `arr.push(a, b)`. Devolver o novo `length` (e não o array) é a pegadinha clássica: `var b = arr.push(x)` guarda um número ([[wiki/concepts/imutabilidade]]).
2. **Array empurrado vira um item só.** `[external]` `arr.push([1, 2])` aumenta o `length` em 1 e aninha o array. Para juntar os itens, `arr.push(...outro)` (ES2015) ou `arr.concat(outro)` (cópia) ([[wiki/concepts/array]]).
3. **Outra forma sem push.** `[external]` `arr[arr.length] = x` também acrescenta no fim, porque `length` é o próximo índice livre. Reescrever o literal inteiro, a "primeira forma" da aula, cria outro array; quem tinha referência ao antigo não vê a mudança.
4. **Sem argumentos, `NaN`.** `[external]` `soma()` faz `undefined + undefined`, que dá `NaN`; a legenda ("o retorno menor não nada") deve ser isso (média). Função guardada em array é o mesmo que função guardada em variável: valor de primeira classe ([[wiki/concepts/funcoes-de-primeira-classe]]).
5. **Não são "parâmetros".** As três partes do `for` são expressões, separadas por `;`, e todas opcionais: `for (;;)` é um loop infinito. Ordem: inicialização uma vez, depois condição → corpo → expressão final ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
6. **"Ele imprimiu 20".** Com `< 20`, o `while` imprime de 0 a 19; o "imprimiu 20" contradiz a frase anterior. Pode ser lapso ou o valor que o console ecoa no fim (baixa).
7. **A vírgula do cabeçalho.** Em `var num = 2, arroz = 3` a vírgula separa declarações; incrementar as duas na expressão final (`num++, arroz++`) usa o operador vírgula, o mesmo da semana 6 ([[wiki/concepts/operador-virgula-javascript]]).
8. **`var` no `for` vaza.** `[external]` O `num` declarado com `var` no cabeçalho continua existindo depois do loop, no escopo da função; `let` limita ao loop e cria um por volta ([[wiki/concepts/var-let-const]]).
9. **O par natural.** O curso ainda não junta `for` e `length`: `for (var i = 0; i < arr.length; i++)` é o percurso crescente que o vídeo anterior fez de trás para frente com `while`.
10. **Legenda.** Trocas principais: "na índia"→Ninja; "da Silva"→Daciuk; "pois"/"Patch" (cerca de 12×)→push; "Harry"/"rei"/"Rei"/"rainha"/"Rio" (cerca de 50×)→array; "Harry Potter"→array ponto; "lei"→length; "Livro"→length; "fantasia"→função; "forte"/"foi"/"fora"/"foco"/"Belfort"→for; "Caio"/"áudio"→while; "vai"→var; "nunca"→num. Mantidos literais: "Agostinho da Silva" (o quarto item, talvez a string `'Daciuk'`), "o tamanho do Boa Esporte", "o valor de me adaptar", "uma foto show", "essa fama no chão", "esse futuro tinha pressão", "rounds", "arroz" (nome da segunda variável, mantido). Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/metodos-de-array-javascript]]
- [[wiki/concepts/array]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/programacao-funcional]]
- [[wiki/concepts/operador-virgula-javascript]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/imutabilidade]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-arrays-propriedade-length]].

## Open Questions

- **O quarto item do array**: "Agostinho da Silva"; como "da Silva" é o ASR de "Daciuk", deve ser a string `'Daciuk'` do vídeo anterior (média). Literal no raw.
- **"Uma outra array local, array de 2 a 3"**: o sexto item da primeira forma; pela saída ("lá, lá, dois laterais", "0, 1 e o 2"), um array de três itens (baixa).
- **"Formada a soma"**: provavelmente "chamada soma" (média); literal.
- **"Rounds" / "arroz"**: o nome da segunda variável do `for`; "arroz" aparece 4 vezes e foi mantido (média de que seja outro nome).
- **"Lá no ar [...] fora do Rio" / "dentro do eu e mais mais"**: deve ser "lá no while [...] fora do while" e "dentro do while" (média); literais.
- **"Do pai"**: provavelmente "do while" (média); literal.

## Raw quotes

- "push significa empurrar"
- "o array ponto push, ele já retorna o length do array"
- "você já declarou as três condições de uma só vez"
