---
type: source
title: "Escopo de variáveis e funções (JavaScript Ninja, semana 4, vídeo 03)"
aliases: ["JavaScript Ninja escopo", "JS Ninja escopo global e local", "03 - Escopo de variáveis e funções"]
date_created: 2026-11-24
date_updated: 2026-11-26
source_count: 0
tags: [javascript, escopo, escopo-global, escopo-local, var, variavel-global-implicita, garbage-collection, parametros, memoria]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-escopo-de-variaveis-e-funcoes.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Escopo de variáveis e funções (JavaScript Ninja, semana 4, vídeo 03)

## TL;DR

Terceiro vídeo da "quarta aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 10 min), depois de [[wiki/sources/javascript-ninja-condicional-ternario|condicional ternário]]. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("meu nome, falando das coisas" na legenda). Retoma o escopo da [[wiki/sources/javascript-ninja-funcoes|aula 04]] ("na verdade, já falei de escopo").

- **Dois escopos:** global (declarada "fora de função", "na parte mais alto do meu código") e local (declarada "dentro de uma função"). De dentro se lê o global; de fora não se lê o local, que dá "não está definido" ([[wiki/concepts/escopo-javascript]]).
- **O global "é algo ruim":** "um erro de design da linguagem", contornável "de algumas formas" ([[wiki/concepts/poluicao-do-escopo-global]]).
- **Garbage collection:** a variável local "só vai aparecer [...] quando ele executa essa função"; quando o JavaScript sabe que ela não será mais usada, "elimina da memória o espaço que essa variável está ocupando". A global fica lá ([[wiki/concepts/gerenciamento-de-memoria]]).
- **Sem `var`:** atribuir sem a palavra-chave, mesmo dentro de função, cria a variável "no escopo global", e só a partir do momento em que a função é invocada ([[wiki/concepts/var-let-const]]).
- **Problemas do global:** "conflito de nomes com outras variáveis" e memória que o JavaScript "não vai poder limpar". Por isso, "sempre utilize a palavra-chave var".
- **Parâmetros são locais:** `a`, `b`, `c` de uma função "não estão definidos" fora dela ([[wiki/concepts/funcoes-javascript]]).
- Próximo vídeo: o desafio da semana 4. A semana 5 abre com [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos|retorno de funções com arrays e objetos]].

## Key Claims

### Global × local

- "A gente tem dois tipos de escopo: o escopo global e o escopo local. [...] A diferença [...] é o local onde você declara uma variável."
- "Sempre que eu declaro uma variável fora de função, essa variável está sendo declarada no escopo global. Se eu declaro dentro de uma função, eu crio uma variável no escopo local."
- "Você não consegue acessar essa variável de fora da função." O contrário vale: a global, "em qualquer lugar você consegue acessar".

### Demonstração

- Uma variável global, lida no console e depois de dentro de uma função que a retorna: "Ele consegue acessar essa variável que está no escopo global [...] dentro da função."
- Outra função declara uma variável local e a retorna; invocada, devolve o valor. Fora dela, o interpretador diz que a variável não está definida: "não existe fora da função".
- "Ela vai passar a aparecer a partir do momento que vai executar essa função, ou invocar ela."

### Por que o global é ruim

- "Isso, basicamente, é um erro de design da linguagem [...] Felizmente, a gente consegue, de algumas formas, passar por cima disso e usar somente variáveis [locais]."
- "O escopo global, ele realmente é algo ruim [...] ele pode atrapalhar bastante nosso código."

### Garbage collection

- "O JavaScript, que tem algo chamado garbage collection, que é coleta de lixo."
- A variável local "só vai ficar disponível dentro daquele escopo". O JavaScript, pela "leitura do meu código e a interpretação dele", sabe quando "não vou usar mais essa variável em lugar algum" e "simplesmente elimina da memória o espaço que essa variável está ocupando".
- "A gente não guarda lixo da memória." Vale "tanto com funções, [...] variáveis, [...] objetos", qualquer coisa que não será usada depois.

### Variável sem `var`

- "Você também consegue criar uma variável sem utilizar a palavra-chave." O JavaScript "entende que você está criando aquela variável no escopo global [...] ainda que você cria uma variável dentro de uma função."
- Antes de invocar a função, a variável "ainda não existe" no global; depois, existe e é acessível de fora.
- Consequências: "conflito de nomes com outras variáveis"; conforme o conteúdo, "ela ocupe muito a memória e acabe consumindo muito recurso do seu computador", e o JavaScript "não vai poder limpar aquele espaço de memória [...] porque ela está sendo usada como uma variável global".
- "Se você esquecer de usar o var [...] você cria um escopo global, e isso causa um problema bastante grande."

### Parâmetros

- Função com "três parâmetros: a, b e c", que retorna um deles. "Se eu tentasse [acessar] fora, [...] não está definido." "Argumentos são sempre locais também."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para escopo e coleta de lixo no JavaScript básico; as precisões vêm da MDN, da especificação e de Crockford, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **Hoje são três escopos, mais o de módulo.** `[external]` A aula é do ES5: global e de função. Desde o ES2015 há escopo de bloco (`let`, `const`, `class`) e cada módulo ES tem o seu, o que tira do global o topo do arquivo ([[wiki/concepts/escopo-javascript]], [[wiki/concepts/var-let-const]]).
2. **A global implícita só existe fora do modo estrito.** `[external]` Com `'use strict'`, padrão em módulos ES e classes, `x = 1` sem declaração lança `ReferenceError`. Ferramentas como a regra `no-undef` do ESLint pegam o erro antes de rodar. As "formas de passar por cima" da era ES5 eram o modo estrito e a IIFE (`(function () { ... })()`), que criava um escopo de função só para não vazar nomes ([[wiki/concepts/poluicao-do-escopo-global]]).
3. **"Erro de design" é posição conhecida.** `[external]` Crockford põe as variáveis globais no topo das "partes horríveis" da linguagem (*JavaScript: The Good Parts*, 2008, apêndice A). Confiança alta.
4. **O coletor não lê o código para prever uso; ele mede alcance.** `[external]` Os coletores do JavaScript (mark-and-sweep, geracional no V8) liberam o que não é mais **alcançável** a partir das raízes (global, pilha). Uma variável local deixa de ser alcançável quando a função retorna, **a menos que uma closure a capture**, caso em que vive enquanto a closure viver ([[wiki/concepts/gerenciamento-de-memoria]], [[wiki/concepts/stale-closure]]). "Saber que eu não vou usar mais" é uma aproximação didática.
5. **O que se coleta são valores, não "variáveis".** `[external]` Primitivos locais costumam viver na pilha ou em registradores; o coletor trabalha sobre objetos no heap. A ideia da aula (o global vive o programa inteiro, o local não) está certa.
6. **Global não é "impossível de limpar".** `[external]` Atribuir `null` à global, ou trocar o objeto, torna o valor antigo inalcançável e coletável. O problema real é que ninguém faz isso, e o valor fica vivo até o fim do processo ou da aba.
7. **"Não está definido" é `ReferenceError`, não `undefined`.** Ler de fora uma variável local lança `ReferenceError: x is not defined`; já `var x;` declarada e não atribuída vale `undefined` ([[wiki/concepts/null-e-undefined]]).
8. **No navegador, `var` global vira propriedade de `window`.** `[external]` `var nome = 'x'` no topo de um script sobrescreve `window.nome`; `let`/`const` no topo ficam no escopo global léxico, mas não viram propriedade. É uma das fontes do "conflito de nomes" da aula.
9. **Parâmetro é o nome; argumento é o valor.** A aula usa os dois como sinônimos ("argumentos de função", "três parâmetros"), como na aula 04 ([[wiki/sources/javascript-ninja-funcoes]]). A conclusão vale: ambos são locais.
10. **Legenda.** Trocas principais: "falando das coisas"→Fernando Daciuk, "capital"→quarta aula, "jogo escrito"/"dia escrito"→JavaScript, "fonte"/"faixa"/"fantasia"→função, "Game Collection"→garbage collection, "vai"/"embaixo"/"bar"→var, "à Copa"→ao escopo, "vídeo"→GitHub. Os nomes das variáveis e funções da demo ficaram ilegíveis. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/poluicao-do-escopo-global]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/gerenciamento-de-memoria]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/stale-closure]]
- [[wiki/concepts/estado-global-inofensivo]]

## Open Questions

- **Nomes da demo.** "Uma variável chamada mas vai", "uma mãe vai", "Honey vai", "chamada vai estar" e as funções "infantil", "moda infantil", "mil falantes", "do Flash" e "outra função boa" parecem ser `myvar`/`myvar2`/`myvar3` e `myFunction`/`myFunction2`/`myFunction3` (média-baixa). Ficaram literais.
- **"O JavaScript não vai conseguir utilizar alguém para escolher um time dessa variável"** e **"você tem que fazer login e coleta"**: provavelmente o garbage collector agindo sobre a variável e "fazer a coleta"; literais.
- **"Ela vai usar o interpretador onde ele escrito que vai dizer que ele vai estar definido"**: provavelmente "o interpretador do JavaScript vai dizer que ela não está definida".
- **"Na verdade, já falei de escopo"**: confirma que o tema apareceu na aula 04, mas pode ser "vamos falar de escopo de variáveis e funções" (média).

## Raw quotes

- "isso, basicamente, é um erro de design da linguagem"
- "a gente não guarda lixo da memória, se a gente não vai precisar usar futuramente"
- "se você esquecer de usar o var [...] você cria um escopo global, e isso causa um problema bastante grande"

Continuação na wiki: [[wiki/sources/javascript-ninja-escopo-de-funcoes]] (semana 9, vídeo 01) leva o escopo para funções dentro de funções e apresenta o hoisting.
