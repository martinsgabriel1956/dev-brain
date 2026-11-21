---
type: entity
title: "Chrome DevTools"
aliases: ["DevTools", "Inspecionar", "console do Chrome", "editor de cubic-bezier do Chrome"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 3
tags: [ferramenta, chrome, devtools, css, debug, frontend]
skill: tech-mentor-frontend
status: stub
---

# Chrome DevTools

Ferramentas de desenvolvedor do Google Chrome (botão direito → Inspecionar). No FrontPUSH, [[wiki/entities/nasser|Násser]] chama tudo de "console", inclusive o painel Elements/Styles.

## No mini curso de CSS Animations

- Testar valores de `transform` ao vivo, mudando o ângulo pelas setas do teclado no painel de estilos ([[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]): "clicar com o botão direito no Chrome, vir em inspecionar [...] você clica no objeto e ele vai aparecer aqui o CSS do objeto". O modo responsivo emula toque, e o hover vira clique.
- **Editor de curvas:** um ícone ao lado de valores de `transition`/`animation-timing-function` abre o "Open cubic bezier editor", com presets (`ease`, `ease-in-out`, *out sine*, *out back*...), pontos de controle arrastáveis e uma prévia em movimento ([[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]], [[wiki/concepts/easing]]).

`[external]` O painel Animations (Mais ferramentas → Animations) grava, desacelera e reproduz animações CSS da página, útil para inspecionar keyframes e curvas ([[wiki/concepts/keyframes-css]]). Confiança alta.

## Do console ao keyframe (FrontPUSH, básico CSS aula 05)

Em [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]], os giros que antes eram testados "pelo próprio console" viram `@keyframes`.

## Key sources

- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: inspecionar e editar o CSS ao vivo
- [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 04: editor de cubic-bezier
- [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 05: do teste no console ao @keyframes
