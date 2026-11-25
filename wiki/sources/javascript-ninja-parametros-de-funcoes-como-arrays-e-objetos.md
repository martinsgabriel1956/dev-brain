---
type: source
title: "Parâmetros de funções como arrays e objetos (JavaScript Ninja, semana 5, vídeo 02)"
aliases: ["JavaScript Ninja parâmetros de funções", "JS Ninja array e objeto como argumento", "02 - Parâmetros de Funções como arrays e objetos"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, funcoes, parametros, argumentos, array, objetos, undefined, typeerror]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Parâmetros de funções como arrays e objetos (JavaScript Ninja, semana 5, vídeo 02)

## TL;DR

Segundo vídeo da semana 5 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 8 min), depois de [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos|retorno de funções com arrays e objetos]]. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). É o espelho do vídeo anterior: em vez de retornar, a função **recebe** array e objeto.

- **Mesma ideia do retorno:** "da mesma forma que [...] conseguem retornar valores de objetos [...], a gente também consegue passar como parâmetro objetos para as nossas funções" ([[wiki/concepts/funcoes-javascript]]).
- **Função que devolve o argumento:** chamada sem nada, retorna o valor padrão (a legenda dá "definitivo", deve ser `undefined`); com o array, devolve o array ([[wiki/concepts/null-e-undefined]]).
- **Índice dentro da função:** `return arg[1]` com `[1, 2, 3]` dá 2, "porque o número 2 é o índice 1" ([[wiki/concepts/array]]).
- **Literal direto na chamada:** `f([1, 5, 7, 8])`, ou um array misto (`'Fernando'`, 1, um terceiro valor, 34), sem variável intermediária.
- **Objeto como argumento:** um objeto com `propriedade: 'Fernando'` e `curso`; a função pode devolver o objeto inteiro ou uma propriedade (`arg.curso`) ([[wiki/concepts/objetos-javascript]]).
- **Sem argumento, erro:** chamar a função que lê `arg.curso` sem parâmetro dá erro, "não conseguiu ler propriedade curso [de] indefinido".
- Próximo vídeo: desafio da semana 5 (fora da pasta); a leva seguinte abre com [[wiki/sources/javascript-ninja-operador-virgula-e-switch|operador vírgula e switch]].

## Key Claims

### Array por parâmetro

- Cria um array com 1, 2, 3 e uma função que "vai receber por parâmetro o array". Troca o nome do parâmetro em relação ao da variável "para não ficar muito complicado de você entender".
- "Eu não passei nada por parâmetro, então o retorno vai ser [undefined], porque ele está retornando o argumento que eu passei." Passando o array, "ele vai retornar o array pra mim".
- "A função, ela consegue retornar [o] objeto, [...] consegue retornar array, só que também ela consegue receber por parâmetro esses caras."

### Acessar o índice do argumento

- Uma segunda função retorna o índice 1 do argumento: "Ele esperava que o argumento que está sendo passado aqui fosse um array, e eu acessei [...] o número 1 do array, que é o 0, 1 [...] e o 2. Então o retorno [...] deveria ser 2, e foi o que aconteceu."

### Literal direto na chamada

- "Eu posso passar direto na função? Claro que eu posso." Passa `[1, 5, 7, 8]` e lê o índice 1.
- Um array com "Fernando", "o número 1", um terceiro item ilegível e "o número 34" volta inteiro.
- "Eu posso colocar [em] uma variável [...] como eu posso passar ele direto aqui na função [...] também isso funciona."

### Objeto por parâmetro

- Objeto com "uma propriedade chamada propriedade, que recebe [...] Fernando", "a propriedade chamada curso" e uma terceira propriedade.
- Função que "vai receber [...] um argumento qualquer" e retorna esse argumento: "Se eu passar o objeto, ela vai retornar o objeto."
- Outra função retorna só `argumento.curso`: "Se você quiser fazer ele retornar uma propriedade específica."
- Sem argumento: "ele vai dar um erro, porque [...] ele não conseguiu ler propriedade curso [de] indefinido, porque aí não foi passado." Com o objeto, devolve "JavaScript Ninja".

### Dúvidas

- Canais: e-mail, resposta ao e-mail do curso, "abra issue no GitHub". "Assista quantas vezes você precisa"; funções e objetos são "primordial no aprendizado JavaScript".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para passagem de parâmetros no JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **Objeto e array chegam por referência compartilhada.** `[external]` O JavaScript passa tudo por valor, mas o valor de um objeto é uma referência. A função que faz `arg.push(4)` ou `arg.curso = 'x'` altera o objeto de quem chamou; a que faz `arg = {}` só troca a variável local. A aula não toca no assunto, que é a diferença prática entre passar primitivo e passar objeto ([[wiki/concepts/imutabilidade]]).
2. **O erro exato é `TypeError`.** `[external]` `undefined.curso` lança `TypeError: Cannot read properties of undefined (reading 'curso')` (texto do V8 atual; versões antigas diziam "Cannot read property 'curso' of undefined", que é o que a aula lê). Já ler um índice ou propriedade que não existe num objeto válido dá `undefined` sem erro ([[wiki/concepts/null-e-undefined]]).
3. **Hoje há como se defender do argumento ausente.** `[external]` Parâmetro padrão (`function f(arg = {})`, ES2015), encadeamento opcional (`arg?.curso`, ES2020) ou desestruturação com padrão (`function f({ curso } = {})`). É a mesma armadilha do `mouseMove({ clientX })` chamado sem argumento ([[wiki/concepts/desestruturacao-javascript]]).
4. **Parâmetro × argumento de novo.** A aula usa as duas palavras como sinônimos ("o primeiro parâmetro, argumenta o primeiro, o primeiro argumento"), como nas aulas anteriores ([[wiki/sources/javascript-ninja-funcoes]]). Parâmetro é o nome na declaração; argumento, o valor na chamada.
5. **Nome do parâmetro diferente da variável.** `[external]` A troca de nome é didática; mesmo com o mesmo nome, o parâmetro é uma variável local nova que sombreia a de fora ([[wiki/concepts/escopo-javascript]]).
6. **Legenda.** Trocas principais: "concursos jovens de biquíni"→com o curso JavaScript Ninja, "da Silva"→Daciuk, "para muitas"→parâmetros de, "rei"/"a rei"/"Harry"→array (alta), "fundação"/"soluções"→função/funções, "Custo"→curso, "tinha"→Ninja, "meio"→e-mail, "isso no vídeo"→issue no GitHub. Os nomes das funções ("fantástica", "funk show", "infantil", "fantochada", "Funchal 2", provavelmente `myFunction`/`myFunction2`) e do array ("Rui", "R", provavelmente `arr`) ficaram ilegíveis. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/array]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/desestruturacao-javascript]]
- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/imutabilidade]]

## Open Questions

- **"O retorno vai ser definitivo"**: provavelmente "undefined" (média-alta); literal.
- **"Como terceiro porteiro"**: o terceiro item do array misto; talvez um booleano ou `null` (baixa).
- **"Um ano inteiro"**: provavelmente "um array inteiro" (média); literal.
- **"Mais de um milhão de inscritos"** como valor de `curso`, que depois aparece como "JavaScript Ninja": a primeira leitura deve ser "JavaScript Ninja" mal transcrita (média); literal.
- **"Ponto Lívia" / "o seu próprio bilhete"**: a passagem em que acessa uma propriedade do objeto sem passá-lo; provavelmente `.propriedade` e "o seu próprio objeto" (baixa).
- **"Funções de objeto são algo, e não é algo primordial"**: o sentido deve ser "funções e objetos são algo primordial"; literal.

## Raw quotes

- "a gente também consegue passar como parâmetro objetos para as nossas funções"
- "ela consegue retornar array, só que também ela consegue receber por parâmetro esses caras"
- "ele não conseguiu ler propriedade curso [de] indefinido, porque aí não foi passado"
