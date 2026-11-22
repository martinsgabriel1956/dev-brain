---
type: concept
title: "Fundamentos da linguagem antes do framework"
aliases: ["linguagem antes do framework", "JavaScript antes do React", "aprender a base antes da biblioteca"]
date_created: 2026-11-17
date_updated: 2026-11-22
source_count: 2
tags: [aprendizado, fundamentos, framework, biblioteca, javascript, react, frontend]
skill: tech-mentor-frontend
status: stub
---

# Fundamentos da linguagem antes do framework

Tese de ensino: aprender a linguagem em que um framework ou biblioteca se apoia antes do próprio framework. Duas justificativas aparecem:

1. **O framework é a linguagem organizada.** Ele "não faz nada além do que aquela linguagem faz"; junta recursos "de maneira organizada, de maneira pensada" para dar produtividade. Quem sabe a linguagem distingue o que é dela e o que é do framework ([[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]).
2. **Frameworks passam, a linguagem fica.** Surge um framework melhor, ou o próximo emprego usa outro; com a base, o próximo se aprende "de forma mais fácil" porque "sempre vai ser a mesma base" (mesma fonte).

## No FrontPUSH

O módulo de JavaScript ES6+ do [[wiki/entities/frontpush]] existe para "nivelar" antes do [[wiki/entities/react]] ([[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]), e a abertura do módulo de React o confirma ([[wiki/sources/frontpush-intro-modulo-reactjs]]). A aula 02 do módulo de React lista o mínimo: objetos, arrow functions, arrays e métodos, DOM, JS assíncrono, requisições e módulos. Foco no "básico e não tudo".

Paralelo no back-end: o JStack monta o servidor com o `http` do Node antes do Express ([[wiki/concepts/framework-web]]).

## Limites

- **O framework também traz um modelo.** Tudo no React é JavaScript, mas UI declarativa, [[wiki/concepts/virtual-dom]], Hooks e JSX são conceitos dele. Saber JS é necessário, não suficiente. `[skill: tech-mentor-frontend]`
- **Parte do fundamento atrapalha.** A manipulação imperativa do [[wiki/concepts/dom]] é o hábito que o React substitui.
- **A ordem pode ser invertida.** [[wiki/concepts/alto-nivel-antes-do-fundamento]] defende construir em alto nível e buscar o fundamento quando a dor aparece. As duas teses concordam que o fundamento é indispensável; divergem na ordem.

## Related

- [[wiki/concepts/framework-web]]
- [[wiki/concepts/alto-nivel-antes-do-fundamento]]
- [[wiki/concepts/fundamentos-e-teoria-na-era-da-ia]]
- [[wiki/entities/javascript]]

## "Nada mais é do que JS" (FrontPUSH, aula 04)

Na [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga|aula 04 do módulo Monetização e Freelancer]], [[wiki/entities/nasser|Násser]] usa o argumento para a carreira: hooks e build são a introdução, "mas quando você abre uma determinada seção de código [...] você continua escrevendo em JavaScript"; quem estudou a linguagem vai para React Native, Node e full-stack com mais facilidade.

## Key Sources

- [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga]]: estudar JS abre React Native, Node e full-stack
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: por que e o que saber de JS antes do React
