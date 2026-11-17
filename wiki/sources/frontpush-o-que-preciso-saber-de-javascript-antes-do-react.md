---
type: source
title: "O que preciso saber de JavaScript antes do React (FrontPUSH)"
aliases: ["FrontPUSH O que preciso saber de JS?", "módulo de ReactJS, aula 02", "JavaScript antes do React"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 0
tags: [react, javascript, es6, objetos, arrow-functions, array, json, dom, javascript-assincrono, es-modules, spa, biblioteca, framework, curso, frontend, lang-dynamic]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-o-que-preciso-saber-de-javascript-antes-do-react.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-17
---

# O que preciso saber de JavaScript antes do React (FrontPUSH)

## TL;DR

Aula 02 do módulo de ReactJS do [[wiki/entities/frontpush|FrontPUSH]] (ele a chama de "primeira aula"; a 01 é a [[wiki/sources/frontpush-intro-modulo-reactjs|intro]]), cerca de 8 min, sem código, com um slide de checklist. [[wiki/entities/nasser|Násser]] (autoria pela sequência; não diz o nome) defende estudar [[wiki/entities/javascript|JavaScript]] antes do [[wiki/entities/react|React]] e lista o que estudar.

- **Por quê:** framework ou biblioteca "sempre vai ser baseada em uma determinada linguagem" e "não faz nada além do que aquela linguagem faz"; só junta recursos "de maneira organizada" para dar produtividade ([[wiki/concepts/fundamentos-antes-do-framework]], [[wiki/concepts/framework-web]]).
- **Frameworks mudam:** pode surgir algo "melhor que o React", ou o próximo emprego usar outro. Quem sabe a base aprende o próximo "de forma mais fácil", porque "sempre vai ser a mesma base".
- **O básico, não tudo:** "tudo não tem como saber". Os conceitos do módulo de [[wiki/concepts/ecmascript|JavaScript ES6]].
- **Checklist (slide):** [[wiki/concepts/objetos-javascript|objetos]]; sintaxe de [[wiki/concepts/arrow-functions|arrow functions]]; [[wiki/concepts/array|arrays]] e [[wiki/concepts/metodos-de-array-javascript|seus métodos]] ("Filter, map, Index, ..."); manipulação do [[wiki/concepts/dom|DOM]]; [[wiki/concepts/javascript-assincrono|JS assíncrono]]; requisições; [[wiki/concepts/modulos-nodejs|Modules JS]].
- **Arrays por causa do JSON:** o front consome "várias APIs múltiplas" e todas falam [[wiki/concepts/json|JSON]], que é "basicamente [...] objetos e arrays" ([[wiki/concepts/api]]).
- **Módulos levam à SPA:** importar arquivos "para uma SPA", conceito das próximas aulas ([[wiki/concepts/single-page-application]]).
- **Saber o que é JS e o que é React:** quem só conhece a biblioteca não distingue "o que é JavaScript naquilo e o que é, propriamente dito, o React".

## Key Claims

### Por que a linguagem antes da biblioteca

- "O framework ou então a biblioteca sempre vai ser baseada em uma determinada linguagem [...] Essa framework ou então essa biblioteca não faz nada além do que aquela linguagem faz, só que com a biblioteca, ele juntou os recursos de maneira organizada, de maneira pensada, criou funções, funcionalidades." Fazer o mesmo "com o JavaScript puro [...] te exigiria um conhecimento considerável dessa linguagem". O ganho é "maior produtividade".
- "Framework e biblioteca estão sempre sendo atualizados, estão sempre mudando [...] vai que aparece, por exemplo, um framework que é melhor [...] que o React [...] ou então você mudou de emprego e eles utilizam uma outra framework." Saber a base permite "partir para outras e aprender essas novas tecnologias de forma mais fácil".
- O JavaScript "vem se destacando, principalmente depois das atualizações do ECMAScript". Investir nele é investir para "expandir a sua área de conhecimento".
- "É de suma importância que você saiba o básico e não tudo, porque tudo não tem como saber." Mesma postura da aula 01 de JS ([[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]).
- Tom: "Não é que você não vai entender nada, mas ele vai te ajudar na compreensão plena do que é a biblioteca ReactJS." É recomendação forte, não bloqueio.

### O que estudar

O slide "O que preciso saber de JS?" lista: "Assista ao módulo de JSES6+", "O que são objetos?", "Sintaxe de Arrow Functions", "Arrays e seus métodos (Filter, map, Index, ...)", "Manipulação de elementos DOM", "JS Assíncrono", "Requisições", "Modules JS". Na fala:

- **Objetos:** sintaxe, atributos, métodos, como acessá-los; "praticamente tudo, ou se não tudo, em JavaScript é objeto". Remete a "uma aulinha de cinco minutos" ([[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]).
- **Arrow functions:** o React tem "pouquíssima verbosidade"; em vez de `function`, nome, parênteses, chaves e `return`, "uma linha só". Saber a sintaxe "para você bater o olho" ([[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]).
- **Arrays e métodos:** "pegar esse JSON, transformar ele em um objeto e saber extrair as informações dele por meio de métodos de array, seja o filter, seja o map, seja o index, seja o forEach [...] e apresentar eles na nossa tela" ([[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back]]).
- **DOM:** a árvore, selecionar um elemento, acessar propriedades e atributos "para poder causar mais interação com o usuário" ([[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]).
- **Assíncrono e requisições:** "como é que funciona esse mundo de requisições e os seus principais métodos" ([[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]).
- **Modules JS:** um arquivo com funções de um tópico, exportado, e um `import` no arquivo principal, "importando para uma SPA" ([[wiki/sources/frontpush-modules-js-import-export-default]]).

### O que é JavaScript e o que é React

- "Às vezes você, conhecendo apenas a framework [...] não vai saber, às vezes, distinguir o que é JavaScript naquilo e o que é, propriamente dito, o React."
- "A gente vai continuar estudando JavaScript, não pense que a gente vai parar por aqui só porque a gente está vendo agora o React". O objetivo inclui entender "como ela utiliza os recursos do JavaScript para poder construir todo esse ambiente".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido; não diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de ReactJS.
- [[wiki/entities/react]]: a biblioteca do módulo.
- [[wiki/entities/javascript]]: o pré-requisito.

## Concepts

- [[wiki/concepts/fundamentos-antes-do-framework]] (criado neste ingest)
- [[wiki/concepts/framework-web]]
- [[wiki/concepts/alto-nivel-antes-do-fundamento]] (contraponto)
- [[wiki/concepts/ecmascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/array]]
- [[wiki/concepts/metodos-de-array-javascript]]
- [[wiki/concepts/json]]
- [[wiki/concepts/api]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/javascript-assincrono]]
- [[wiki/concepts/modulos-nodejs]]
- [[wiki/concepts/single-page-application]]

## Precisões e tensões com a wiki

- **"Não faz nada além do que aquela linguagem faz" vale para o código, não para o modelo.** Tudo o que o React faz é JavaScript, sim. Mas ele traz um modelo próprio que não existe no JS puro: UI declarativa (`UI = f(state)`), [[wiki/concepts/virtual-dom]] e [[wiki/concepts/reconciliacao]], regras dos Hooks, JSX (que nem é JavaScript: é compilado para chamadas de função). `[skill: tech-mentor-frontend]` Saber JS é necessário, mas não basta para "ler" React; o modelo mental é o segundo pré-requisito. Confiança alta.
- **"Index" não é um método de array.** O slide e a fala dizem "Index". Os candidatos são `indexOf` e `findIndex` ([[wiki/concepts/metodos-de-array-javascript]]). No React, o que pesa mesmo é `map` (listas no JSX), `filter` e, em estado imutável, spread e `reduce`; e o `index` que aparece é o 2º parâmetro do `map`, que não deve virar `key` quando a lista muda de ordem (https://react.dev/learn/rendering-lists) `[external]`. Confiança alta.
- **A manipulação do DOM é justamente o que o React esconde.** No React você não faz `querySelector` + `classList`; descreve o estado e ele atualiza o DOM. Saber o DOM ajuda a entender eventos, atributos (`className`, `htmlFor`) e o `ref` para casos de escape, mas o hábito imperativo do JS puro é o que mais atrapalha quem chega ao React ([[wiki/concepts/dom]]). A NLW #2 diz o mesmo: "a gente não vai no HTML [...] e adiciona uma nova div" ([[wiki/entities/react]]).
- **Faltam itens que o React usa o tempo todo.** [[wiki/concepts/desestruturacao-javascript|Desestruturação]] (`const [count, setCount] = useState(0)`, props), spread/rest, [[wiki/concepts/template-literals|template literals]], ternário e `&&` para renderização condicional, `const`/`let`. A desestruturação foi a aula 18 do módulo de JS, apresentada como preparo para React, mas não entrou no slide. `[skill: tech-mentor-frontend]` Confiança alta.
- **"Tudo em JavaScript é objeto" de novo.** Primitivos não são objetos; o autoboxing dá a impressão de que são. Já registrado em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]] e [[wiki/concepts/objetos-javascript]]. Ele próprio suaviza: "praticamente tudo, ou se não tudo".
- **JSON é texto, não "objetos e arrays".** O JSON chega como string e vira objetos e arrays depois do `JSON.parse` (ou `response.json()`); ele mesmo diz "pegar esse JSON, transformar ele em um objeto" ([[wiki/concepts/json]]). E nem toda API fala JSON (GraphQL fala JSON, mas gRPC, XML/SOAP e streams não).
- **Modules JS × SPA.** Módulos organizam o código; SPA é renderizar tudo numa página só e trocar o conteúdo pelo JavaScript. Estão ligados pelo bundler, que junta os módulos em um pacote para a SPA, mas um não implica o outro ([[wiki/concepts/single-page-application]], [[wiki/concepts/modulos-nodejs]]).
- **Contraponto: a ordem inversa.** [[wiki/concepts/alto-nivel-antes-do-fundamento]] registra a tese de começar pelo alto nível e puxar o fundamento pela dor. Násser fica no meio: recomenda fortemente o JS antes, mas "não é que você não vai entender nada" e "a gente vai continuar estudando JavaScript" durante o React.
- **"Primeira aula".** Ele chama esta de primeira aula do módulo; o arquivo é o 02, depois da intro. Sem conflito, só numeração.

## Open Questions

- "Requisições" está no slide e na fala, mas ele não diz se o módulo usa `fetch` ou o [[wiki/entities/axios|Axios]] da aula 16 de JS.
- "Pense daquela frase que eu sempre digo": a frase "o framework [...] sempre vai ser baseada em uma determinada linguagem" não aparece antes nas aulas ingeridas.
- "Nós vamos aprofundar um pouco mais nesse módulo ainda" sobre front, back e APIs: em que aula?

## Raw quotes

- "não faz nada além do que aquela linguagem faz"
- "porque sempre vai ser a mesma base"
- "distinguir o que é JavaScript naquilo e o que é, propriamente dito, o React"
