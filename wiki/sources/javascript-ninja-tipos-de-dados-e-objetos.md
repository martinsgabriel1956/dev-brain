---
type: source
title: "Tipos de dados e objetos (JavaScript Ninja, semana 3, vídeo 01)"
aliases: ["JavaScript Ninja tipos e objetos", "JS Ninja primitivos e objetos", "01 - Tipos de dados e objetos"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, tipos-primitivos, objetos, null, undefined, funcoes, funcao-anonima, primeira-classe]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-tipos-de-dados-e-objetos.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Tipos de dados e objetos (JavaScript Ninja, semana 3, vídeo 01)

## TL;DR

Primeiro vídeo da "terceira aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), depois de [[wiki/sources/javascript-ninja-instrucoes-condicionais-if|instruções condicionais]]. O desafio da semana 2, prometido duas vezes, não está entre as transcrições. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("na fenda do tio" na legenda).

- **Duas categorias de tipo:** "tipos de valores primitivos e tipos de objeto". Primitivos: number (inteiro ou "float"), string, boolean, e os "valores especiais" `null` e `undefined` ([[wiki/concepts/tipos-primitivos-javascript]], [[wiki/concepts/null-e-undefined]]).
- **"Todos os outros tipos de dados, eles são objeto."**
- **Objeto é "um conjunto de propriedades"**, e elas "podem, não, devem receber o nome e um valor"; o valor pode ser primitivo "ou [...] um outro objeto" ([[wiki/concepts/objetos-javascript]]).
- **Sintaxe:** chaves, `nome: valor`, propriedades "separadas por vírgula"; leitura com `objeto.propriedade` ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).
- **Para que serve:** "organizar os seus dados", como objetos "da vida real". Exemplos `pessoa` (nome, idade, peso, altura) e `carro` (cor, motor `'2.0'` como string, quatro portas).
- **Funções também são objetos**, "objetos de primeira classe", "porque eles podem ser atribuídos a variáveis". Demonstra uma função anônima guardada numa variável e invocada pelo nome da variável ([[wiki/concepts/funcoes-de-primeira-classe]], [[wiki/concepts/funcoes-javascript]]).
- Próximo vídeo: mais sobre funções (na pasta, "Métodos de objeto").

Continua em [[wiki/sources/javascript-ninja-metodos-de-objeto]] (semana 3, vídeo 02: métodos de objeto).

## Key Claims

### Duas categorias

- "A gente pode dividi-los em duas categorias principais, que são tipos primitivos, tipos de valores primitivos, e tipos de objeto."
- Number: "um número qualquer, o número decimal, o número inteiro", o decimal "conhecido como float".
- String: "qualquer coisa escrito envolto por aspas duplas ou simples, ou apóstrofo". Boolean: "true ou falso".
- `null` e `undefined` são "os valores especiais". Um "significa que um valor não foi passado ou não existe" para a variável ou o argumento; o `null` é "quando você passa esse valor dizendo a esse cara que não tem [...] valor nenhum", e "você precisa explicitamente [...] atribuir ele".
- "Todos os outros tipos de dados, eles são objeto. Então tudo o que não for [...] string, boolean, [...] null, undefined, ele vai ser um tipo de objeto."

### O que é objeto

- Os objetos "são uma das partes mais importantes dentro de JavaScript", e "tudo que [...] a gente vai fazer" é "em cima de objetos".
- "O objeto, ele é um conjunto de propriedades [...] Elas podem, não, devem receber o nome e um valor." O valor "pode ser tanto um valor primitivo [...] ou ele pode ser um outro objeto".

### Criar e ler

- "A criação do objeto a gente faz utilizando as chaves [...] dá o nome de uma propriedade, dois pontos, o valor da propriedade."
- `var objeto = { propriedade: 'valor', propriedade2: 10, propriedade3: true }`: "as propriedades [...] são separadas por vírgula, e o valor [...] é atribuído a uma propriedade com dois pontos, quando você usa dentro dessa notação de objeto".
- "Eu utilizo [...] objeto ponto propriedade [...] Ele vai me dar o valor da propriedade."

### Para que serve

- "Você vai utilizar ele para organizar os seus dados", como os objetos "da vida real".
- `pessoa` com `nome: 'Fernando'`, `idade: 30`, `peso: 85` ("vou passar com o número") e `altura`. `pessoa.nome` dá "Fernando", `pessoa.idade` dá 30.
- `carro` com `cor: 'vermelho'`, `motor: '2.0'` e quatro portas. O motor vai como string porque, como número, "dois ponto zero" não ficaria assim (ver Precisões, 6). `carro.cor` dá "vermelho".
- "O objeto [...] vai guardar a propriedade para si. Parece bastante simples, mas a gente vai ver que isso vai ter um valor bastante útil."

### Função é objeto

- O objeto pode receber como valor "um outro objeto. Outro tipo de objeto [...] são as funções. Então o function, na verdade, ele é um tipo de objeto."
- "Funções são objetos de primeira classe [em] JavaScript. E por que [...]? Porque eles podem ser atribuídos a variáveis."
- Uma variável recebe "uma função sem nome [...] uma função anônima" que retorna uma string. "Não é obrigatório a função tem um nome" quando é atribuída a uma variável; "eu vou utilizar o próprio nome trabalhado [o da variável, pelo contexto] para chamar essa função", com "o operador de invocação".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para tipos e objetos do JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **Faltam dois primitivos.** `[external]` Desde o ES2015 há `symbol` e, desde o ES2020, `bigint`: sete primitivos ao todo (https://developer.mozilla.org/en-US/docs/Glossary/Primitive). A lista da aula é a do ES5, como a da [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados|aula 01]]. "Esses são basicamente dois tipos" fala das duas categorias, não da quantidade de primitivos ([[wiki/concepts/tipos-primitivos-javascript]]).
2. **"Tudo o que não for primitivo é objeto" está certo.** Arrays, funções, datas e expressões regulares são objetos. `[external]` `typeof function(){}` dá `"function"`, mas é um objeto chamável: aceita propriedades (`f.x = 1`) e tem `f.name` e `f.length`.
3. **Inteiro e "float" são o mesmo tipo.** `[external]` Todo number é double IEEE 754; não existe int separado (fora `bigint`).
4. **`undefined` × variável inexistente, de novo.** A descrição do trecho "o nu é uma falha de quando uma propriedade, um argumento de função não existe, uma variável não existe" é a do `undefined` (a legenda provavelmente trocou o nome). Para propriedade e argumento ausentes está certa; para variável não declarada, não: lê-la lança `ReferenceError` ([[wiki/concepts/null-e-undefined]], mesma tensão da aula 01).
5. **Nomes de propriedade.** `[external]` São strings ou symbols; `{ 1: 'a' }` guarda a chave `'1'`. Nomes que não são identificadores válidos pedem aspas e colchetes (`obj['meu nome']`) ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).
6. **O motor como string está certo.** `[external]` `2.0` é o literal do número 2; o REPL mostraria `motor: 2`. Para guardar o rótulo "2.0", string. Confiança média na leitura do trecho ("se eu colocar dois pontos zero, ele vai colocar como no meu entender").
7. **"Linguagem orientada a objetos" precisa de ressalva.** `[external]` JavaScript é multiparadigma e a orientação a objetos dele é por protótipo, não por classe; o objeto literal da aula não tem classe nenhuma ([[wiki/concepts/programacao-orientada-a-objetos]]).
8. **Primeira classe é mais que atribuir.** `[external]` Uma função de primeira classe pode ser atribuída, passada como argumento, retornada por outra função e guardada em estruturas de dados (https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function). A aula só mostra a atribuição ([[wiki/concepts/funcoes-de-primeira-classe]]).
9. **A função "anônima" ganha nome.** `[external]` Desde o ES2015, `var f = function () {}` infere `f.name === 'f'`; Node recente mostra `[Function: f]`. Ela continua anônima na sintaxe (sem nome próprio para recursão), mas a pilha de erro já mostra o nome da variável.
10. **Legenda.** Trocas principais: "na fenda do tio"→Fernando Daciuk (média), "tinindo"→Ninja (média-alta), "NAMA"→number, "fonte"→float, "bule"→bool, "útil"→true, "não indefinidos"→null e undefined (média-alta), "estilingue Bulent"→string, boolean, "Twingo" (2×)→string, "bolha"→boolean, "se tu"→ser true (média), "ou entidade" (2×)→ponto idade, "Funchal"→function (alta), "soluções"→funções. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/notacao-de-ponto-e-colchetes]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/programacao-orientada-a-objetos]]

## Open Questions

- "Gerando um número inteiro, mas que na verdade é qualquer coisa escrito envolto por aspas": pelo contexto, a string; o começo da frase se perdeu.
- "Numa fase de web", na lista de valores primitivos: provavelmente "null ou undefined"; ficou literal.
- "Uma lei permitindo": provavelmente "um valor primitivo"; ficou literal.
- O nome da variável da função anônima sai como "me", "Mãe", "mais", "Mano" e "Malta"; o nome real não se recupera.
- "Pessoa ponto a altura, 85": 85 é o peso; pode ser erro ao vivo ou da legenda. A altura sai como "um metro", seguido de "eu tenho muito tempo" (talvez "um metro e [...]").
- A legenda escreve "motor de 11 pontos" antes de "motor 12 pontos zero" (corrigido para "dois ponto zero"); o primeiro ficou literal.

## Raw quotes

- "Elas podem, não, devem receber o nome e um valor."
- "todos os outros tipos de dados, eles são objeto"
- "funções são objetos de primeira classe [em] JavaScript"
