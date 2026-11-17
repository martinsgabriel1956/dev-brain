---
type: concept
title: "Framework Web"
aliases: ['web framework', 'framework server-side']
date_created: 2026-10-14
date_updated: 2026-11-17
source_count: 9
tags: [framework, backend, rails, historia]
skill: tech-mentor-frontend
status: draft
---

# Framework Web

Mais que linguagem, fornece **estrutura pré-definida**: segurança, acesso a dados, autenticação/autorização, padrões visuais e **onde colocar cada tipo de código**. Antes, cada app PHP fazia tudo do zero. Popularizado na era Java/J2EE, imitado no PHP, e consagrado pelo [[wiki/entities/ruby-on-rails|Ruby on Rails]] (fim de 2004). Rails também inspirou a 1ª geração de bibliotecas JS/CSS ([[wiki/concepts/biblioteca-javascript-de-compatibilidade]]) e o [[wiki/concepts/pipeline-de-assets]]. Ver [[wiki/concepts/historia-do-front-end]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], o módulo de JavaScript do FrontPUSH existe para "nivelar" antes de "alguma framework, como, por exemplo, o React". A documentação do React o chama de biblioteca, e o próprio Násser passa a usar "biblioteca JavaScript" ao abrir o módulo de React ([[wiki/sources/frontpush-intro-modulo-reactjs]]).

## No JStack, aula 04

Em [[wiki/sources/jstack-criando-o-servidor-http]], framework é o que "só facilita o uso dos recursos que já estão presentes dentro do Node": o Express sobre o módulo `http`. Começar sem ele mostra o que o framework esconde: roteamento, parsing de body e tratamento de erro.

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], arrow functions são ensinadas "para que, quando a gente for lá em frameworks, não te soe estranho esse tipo de sintaxe" (React, Vue).

Em [[wiki/sources/frontpush-modules-js-import-export-default]], `import`/`export` é "tópico importantíssimo para a gente entender a dinâmica de frameworks": no React, por exemplo, cada componente é um módulo com `export default`.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], a desestruturação é ensinada porque é "muitíssimo utilizad[a] quando a gente parte para frameworks como React ou Vue": props, `useState` e imports.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: JS básico antes do framework
- [[wiki/sources/jstack-criando-o-servidor-http]]: Express sobre http; Node puro antes do framework
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: arrow functions antes do framework
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: módulos como base dos frameworks
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: desestruturação como pré-requisito de framework
- [[wiki/sources/frontpush-intro-modulo-reactjs]]: FrontPUSH, React aula 01: "módulo de biblioteca JavaScript"
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: framework "não faz nada além do que aquela linguagem faz"; ver [[wiki/concepts/fundamentos-antes-do-framework]]
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: React.js biblioteca, ecossistema React framework
