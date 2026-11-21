---
type: concept
title: "Microinteração"
aliases: ["microinterações", "microinteraction", "micro-interação", "microinteractions"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 2
tags: [microinteracao, motion-design, animacao, feedback, hover, ux, ui-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# Microinteração

Resposta pequena e pontual do sistema a uma ação do usuário. Para [[wiki/entities/nasser|Násser]], microinterações são "as formas de um sistema responder a ação de um usuário": "quando eu clico em algum lugar, quando eu passo o mouse, ele me responde de alguma forma que aquilo ali é um item clicável" ([[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]). É o ponto em que o [[wiki/concepts/motion-design]] encontra o [[wiki/concepts/feedback-do-sistema]].

## Estrutura

`[external]` Dan Saffer, *Microinteractions* (O'Reilly, 2013), divide a microinteração em quatro partes (sem fetch; confiança alta):

1. **Gatilho:** o que a inicia; ação do usuário (clique, hover) ou do sistema (notificação, fim de upload).
2. **Regras:** o que acontece.
3. **Feedback:** como o usuário fica sabendo (movimento, cor, som, vibração).
4. **Loops e modos:** duração, repetição e variações.

## Exemplos do FrontPUSH

- **Botão:** no hover, "ele cresce, ele coloca uma sombra". O design de repouso já diz "clicável"; a microinteração é "mais um indicativo" ([[wiki/concepts/botoes-em-interfaces]], [[wiki/concepts/affordance]]).
- **Links do menu:** uma barrinha cresce sob o link no hover.
- **Erro:** campo vermelho, vibração do celular na senha errada, informação que pisca.

## Cuidados

- **Não pode ser o único sinal.** Hover não existe em tela de toque; cor sozinha não identifica erro (WCAG 1.4.1). `[external]`
- **Animar barato.** `transform` e `opacity` em vez de `width` ou `box-shadow` ([[wiki/concepts/transition-e-transform-css]], [[wiki/concepts/taxa-de-quadros-60fps]]).
- **Curta.** `[skill: tech-mentor-frontend]` Feedback de interação costuma ficar entre ~100 e ~300 ms; mais que isso atrasa a próxima ação. Respeitar `prefers-reduced-motion` ([[wiki/concepts/acessibilidade]]).

## Hover no toque (FrontPUSH, básico CSS aula 02)

Em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]], o giro no `:hover` precisa ser "simulado com o clique" no modo responsivo. `[external]` Em telas de toque o hover gruda até tocar fora; `@media (hover: hover)` restringe o efeito a quem tem mouse.

## Key sources

- [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: FrontPUSH, mini curso de CSS Animations, aula 02: definição, botão e menu do site de Násser
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: hover simulado por clique no modo responsivo
