---
type: source
title: "Introdução à programação funcional (JavaScript Ninja, semana 8, vídeo 02)"
aliases: ["JavaScript Ninja programação funcional", "JS Ninja functional programming", "02 - Introdução à Functional Programming", "cidadãos de primeira classe JavaScript Ninja"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, programacao-funcional, funcoes-de-primeira-classe, objeto-literal, funcao-literal, retorno-de-objeto, imperativo, java]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-introducao-a-programacao-funcional.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# Introdução à programação funcional (JavaScript Ninja, semana 8, vídeo 02)

## TL;DR

Segundo vídeo da semana 8 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), o que [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]] anunciou. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). Mais conversa que código: a definição de [[wiki/concepts/programacao-funcional|programação funcional]] e o paralelo entre objetos e funções.

- **Definição da aula:** "uma forma de você programar" em que os programas "são baseados em funções, ou nas características que as funções têm"; a linguagem precisa oferecer recursos para isso.
- **Cidadãos de primeira classe:** funções "têm o mesmo tratamento dos objetos": "tudo aquilo que você consegue fazer com objetos em JavaScript [...] você também consegue fazer com funções" ([[wiki/concepts/funcoes-de-primeira-classe]]).
- **Por que importa:** "para você se tornar um ninja de verdade"; "vai modificar bastante a forma de você pensar em lógica". Contrasta com Java, de "instruções [...] executando linha a linha" ([[wiki/concepts/programacao-procedural]]).
- **Três paralelos objeto × função:** (1) literal: `{}` cria objeto literal, `function nome() {}` cria função literal; (2) ambos podem ser atribuídos a variáveis, a função anônima ou nomeada; (3) função pode retornar objeto, direto ou guardado numa `var` antes ([[wiki/concepts/objetos-javascript]]).
- **No editor:** troca o console por um arquivo `.js`, cria uma função que retorna `{ name: 'Fernando', lastName: 'Daciuk' }` e mostra que sem executar a função "eu não vou conseguir pegar o objeto [...] retornado".
- **Construtores** de objeto e de função "a gente vai ver mais para frente".
- **Próximo vídeo:** "você também pode retornar funções" ([[wiki/concepts/funcoes-javascript]]).

## Key Claims

### O que é programação funcional

- "A programação funcional, na verdade, nada mais é do que uma forma de você programar, e até o formato que você escreveu seus programas, eles são baseados em funções, ou nas características que as funções têm."
- "Para você usar o estilo de programação funcional numa linguagem, a linguagem precisa disponibilizar algumas coisas para você [...] que as funções, na verdade, no JavaScript, eles são objetos de primeira classe."
- "Eles podem ser conhecidos também como cidadãos de primeira classe. [...] São melhores que alguém? [...] Significa que [...] as funções, na verdade, elas têm o mesmo tratamento dos objetos no JavaScript."
- "Tudo aquilo que você consegue fazer com objetos em JavaScript, digamos que é a parte mais importante do JavaScript, você também consegue fazer com funções. E isso permite a gente trabalhar de forma funcional."

### Por que aprender

- "Para você se tornar um ninja de verdade, você precisa conhecer esse tipo de formato de programação funcional, que isso vai modificar bastante a forma de você pensar [...] em lógica."
- "Muitas linguagens de programação hoje não te dão essa liberdade de programar nesse formato funcional. [...] Java, por exemplo, [...] tem uma pegada [...] onde você vai passando as instruções [...] e eles vão executando linha a linha, e a programação funcional [...] uma programação um pouco mais dinâmica."

### Objeto literal e função literal

- Objeto literal: "você usa simplesmente as chaves [...] o formato final do objeto, exatamente como ele é apresentado para a gente na linguagem em si, é objeto literal."
- Função literal: a "que você cria com a palavra-chave function. Você dá um nome para ela, [...] você passa parâmetros, que são opcionais [...] abre as chaves e [...] coloca a sua instrução dentro". É o formato usado "na maioria dos nossos exercícios".
- "A gente nunca falou sobre construtores de objetos e construtores de funções [...] Os construtores [a] gente vai ver mais para frente."

### Atribuir a variáveis

- "Da mesma forma [que objetos], você pode atribuir também funções [...] Ela pode ser uma função anônima, ou ela pode ser uma função nomeada."
- A função sem `return` "é executável e não retorna nada"; a anônima "não tem nome, e ele não retorna a propriedade name" (no Node da gravação).

### Função que retorna objeto

- "Você cria [...] uma função [...] e você retorna um objeto [...] com uma propriedade name com o teu nome, lastName com o sobrenome. E quando você invocar essa função, você vai retornar esse objeto."
- "Numa segunda abordagem bem parecida, atribuir o objeto a uma variável e [...] retornar esse objeto." "O resultado é o mesmo."
- Um primeiro erro ao vivo: "eu coloquei uma máscara simples aqui, por isso que ele deu errado" (aspas, provavelmente); passa então para um arquivo, "fica mais fácil manipular".
- "Se eu não executar ela, eu não vou conseguir pegar o objeto [...] retornado. Vou ter as propriedades e métodos do objeto JavaScript. [...] A partir do momento em que [eu] executo ela, aí eu tenho acesso a esse objeto."

### Próximo vídeo

- "Só que você também pode retornar funções, e [...] retorno de funções a gente vai ver no próximo vídeo."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência sobre programação funcional em JavaScript básico nem sobre funções de primeira classe. As precisões vêm da MDN e de conhecimento base, marcadas `[external]`; os exemplos foram reproduzidos no Node 22.23. https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function

1. **Duas definições de programação funcional.** A aula define o paradigma por "ser baseado em funções". A página [[wiki/concepts/programacao-funcional]] o define por funções puras, [[wiki/concepts/imutabilidade|imutabilidade]] e [[wiki/concepts/efeitos-colaterais|efeitos colaterais]] explícitos. As duas se encaixam: funções de primeira classe são o pré-requisito da linguagem, e pureza e imutabilidade são a disciplina do estilo. JavaScript dá o primeiro e não impõe o segundo (`var`, objetos mutáveis). A aula só cobre o pré-requisito (leitura da wiki).
2. **"Tudo que se faz com objetos".** `[external]` Vale porque função é objeto chamável: `f instanceof Object` dá `true` e `f.prop = 1` funciona (verificado). O termo "cidadão de primeira classe" é de Christopher Strachey, nos anos 1960 (de memória, não verificado).
3. **Java.** `[external]` "Não te dão essa liberdade" vale para Java até a versão 7. Java 8 (2014) trouxe lambdas e streams, e a wiki já registra essa influência funcional ([[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]]). O contraste "linha a linha" é imperativo × declarativo, e não estático × "dinâmico": JavaScript também executa linha a linha ([[wiki/concepts/programacao-procedural]]).
4. **`.name` da função × `.name` do objeto.** É a confusão que a demonstração esbarra. Com `function retornaObjeto() { return { name: 'Fernando', lastName: 'Daciuk' } }`, `retornaObjeto.name` dá `'retornaObjeto'`, a propriedade da própria função, e `retornaObjeto().name` dá `'Fernando'`; `retornaObjeto.lastName` dá `undefined` (verificado). Por isso "eu preciso executar a função" ([[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]).
5. **Cada chamada, um objeto novo.** `[external]` `retornaObjeto() === retornaObjeto()` dá `false` (verificado). Função que monta e devolve objeto é a *factory function* do JavaScript, sem `new` nem classe ([[wiki/concepts/factory-pattern]]). A semana 5 já mostrava o retorno de objeto ([[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]).
6. **"Construtores de funções".** `[external]` Existe `new Function('a', 'b', 'return a + b')`, mas compila texto em tempo de execução, como `eval`, e quase não se usa. Os "construtores de objetos" devem ser funções chamadas com `new` (inferência, média).
7. **Retornar funções.** `[external]` O anúncio é a outra metade de primeira classe: `function somaDe(n) { return function (x) { return x + n } }` e `somaDe(2)(3)` dá 5 (verificado), a base de closures e funções de ordem superior ([[wiki/concepts/funcoes-de-primeira-classe]]).
8. **`name` da anônima.** A fala de que a anônima "não retorna a propriedade name" repete o vídeo anterior e também é anterior ao ES2015 ([[wiki/concepts/ecmascript]]).
9. **Legenda.** Trocas principais: "INI realçou"→Ninja, e eu sou; "da Silva" (2×)→Daciuk; "soluções"→funções; "nível"→ninja; "falante"→function; "material"→literal; "consultores"→construtores; "ou BJ"→obj; "nem"/"nele"→name (5×); "lesionei me conta"/"o lance nem"/"no lance"→lastName; "tornar"/"me tornei"/"se tornou"→retornar/retornei/retornou; "bar"→var; "apontou logo"/"logo"→console.log; "profissão"→função. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/programacao-funcional]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/programacao-procedural]]
- [[wiki/concepts/factory-pattern]]
- [[wiki/concepts/null-e-undefined]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]] (semana 8, vídeo 01).

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]] (semana 8, vídeo 03), o de retorno de funções que este anuncia.

## Open Questions

- **Nome da função do exemplo**: "minha teoria objeto [...] como o próprio nome da função" sugere `retornaObjeto` (média); "uma função peça" e "uma reflexão sobre" ficam ilegíveis. Literais.
- **"Uma máscara simples"**: provavelmente aspas simples mal fechadas (média); literal.
- **"Pegada um pouco mais sim está"**: o adjetivo para Java (talvez "sistemática" ou "imperativa"); baixa. Literal.
- **"Estado é uma delas" / "dentro dos navios" / "interagir com os clientes"**: trechos ilegíveis; o último talvez seja "funções literais" (baixa). Literais.
- **"Eu não vou no torneio" / "propriedades de Dilma" / "no lugar do titânio" / "Vitor Belfort"**: ruído de legenda (talvez "não botei nenhum retorno" e "no lugar do return"); baixa. Literais.
- **"A mídia JS" / "o meu amigo js"**: o nome do arquivo `.js` criado no editor; baixa.

## Raw quotes

- "Eles são especiais e são melhores que alguém?"
- "Para você se tornar um ninja de verdade, você precisa conhecer esse tipo de formato de programação funcional"
- "Se eu não executar ela, eu não vou conseguir pegar o objeto de dentro"
