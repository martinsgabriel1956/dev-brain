---
type: entity
title: "anime.js"
aliases: ["Anime.js", "anime JS", "animejs"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 1
tags: [biblioteca, javascript, animacao, open-source, frontend]
skill: tech-mentor-frontend
status: stub
---

# anime.js

Biblioteca JavaScript de animação, open source (MIT), criada por Julian Garnier. Anima propriedades CSS, transforms, atributos SVG, propriedades do DOM e objetos JavaScript, com timelines, stagger (atraso escalonado entre elementos) e easings próprios. A versão 4 (2025) reescreveu a API em módulos ES importáveis por função e acrescentou um modo sobre a Web Animations API. `[external]` https://animejs.com/, sem fetch; confiança média-alta nos detalhes da v4.

## No FrontPUSH

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], [[wiki/entities/nasser|Násser]] abre o anime.js no Notion do curso como "uma das minhas preferidas de cara": documentação "por sinal muito boa", "uma das que tem melhor codificação". Usa a biblioteca também como exemplo do custo: "olha só o tanto de recurso que ela tem", tudo carregado ao colocar o script. Precisão: com os módulos da v4 e [[wiki/concepts/tree-shaking]], só o que é importado vai para o bundle. Ver [[wiki/concepts/css-puro-vs-biblioteca-de-animacao]].

Como o [[wiki/entities/gsap|GSAP]], calcula os quadros em `requestAnimationFrame`, na thread principal, no modo padrão.

## Key sources

- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: biblioteca preferida, documentação, peso
