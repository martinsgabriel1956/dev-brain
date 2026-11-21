---
type: source
title: "Propriedade animation na prática: keyframes no parent e no box e várias animações (FrontPUSH)"
aliases: ["FrontPUSH motion, básico CSS aula 05", "Propriedade animation: Prática", "animation prática", "CSS Animations, básico CSS, aula 05"]
date_created: 2026-11-20
date_updated: 2026-11-21
source_count: 0
tags: [css, animation, keyframes, shorthand, rotatex, rotatey, preserve-3d, cubic-bezier, background-color, motion-design, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-20
---

# Propriedade animation na prática: keyframes no parent e no box e várias animações (FrontPUSH)

## TL;DR

Quinta aula do módulo "Básico CSS" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 9 minutos, só código. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência. Junta "tudo que a gente disse nas duas últimas aulas" e anima a estrutura `.parent`/`.box` com `preserve-3d` da [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d|transform parte 2]], que antes só mudava pelo console ([[wiki/concepts/keyframes-css]]).

- **Dois keyframes:** `box` gira `rotateX` de 0 a 360deg; `parent` gira `rotateY` de 0 a 360. `.box` com `animation: box 3s ease infinite alternate`, "a configuração que eu mais utilizo"; `.parent` igual, com 10 s, "mais devagar". Depois 5 s e 15 s ([[wiki/concepts/perspective-css]]).
- **Shorthand:** "aqui é sempre a duração, aqui é sempre o delay"; "no máximo, eu coloco também um forwards".
- **Contagem finita:** com 3 repetições, para e "vai voltar para o estado inicial".
- **Várias animações na mesma classe**, separadas por vírgula: `changeColor` de `background-color` red a blue, "totalmente independente". O `linear-gradient` do fundo "está meio que me atrapalhando" e sai ([[wiki/concepts/background-css]]).
- **Curva própria:** troca `ease` por um `cubic-bezier` "muito rápido [...] e no final, muito devagar" ([[wiki/concepts/easing]], [[wiki/entities/cubic-bezier-com]]).
- **Fecho:** criar "uma biblioteca de efeitos na sua cabeça" ([[wiki/concepts/repertorio]]).

## Key Claims

### Keyframes box e parent

- Retoma "aqueles efeitos que a gente colocou lá naquele primeiro momento, onde a gente estava mudando as configurações aqui pelo próprio console" ([[wiki/entities/chrome-devtools]]).
- `@keyframes box`: "transform rotateX [...] de 0deg até 360deg". "Eu quero que ele faça essa transição juntamente com o meu parent": `@keyframes parent` com rotação no eixo Y "também de 0 a 360".

### O shorthand

- `.box`: nome `box`, "três segundos", "a curva ease", "infinita" e "de maneira alternada". "Essa aqui de cara é a configuração que eu mais utilizo."
- "Se eu quisesse colocar algum tipo de delay, eu colocaria o delay aqui, dois segundos. Ele já identifica isso aqui como dois segundos. Aqui é sempre a duração, aqui é sempre o delay." Ver [[wiki/concepts/shorthand-css]].
- "No máximo, eu coloco também um forwards aqui no final para poder fixar [...] no último frame que foi estabelecido."
- `.parent`: "exatamente a mesma coisa", com `parent` e 10 s, "porque eu quero que essa bichinha gire mais devagar do que o do box". Depois, 5 s no box e 15 s no parent. "Como ele é infinito, ele nunca acaba."

### Contagem finita

- Com `iteration-count` 3, "ele vai fazer três vezes esse movimento, depois vai parar e vai voltar para o estado inicial que está aqui na div .parent e na div .box". Com 2 s e 1 s, "rodou, rodou [...] voltou para o estado inicial. O que eu estava falando não estava mentindo."

### Várias animações

- "Eu posso emendar vários keyframes ao mesmo estilo, [...] a mesma tag, a mesma classe." `changeColor`: "background-color red para um background-color blue", com "uma outra linha do tempo".
- "Eu separo uma linha da outra por uma vírgula." "Esse linear-gradiente aqui está meio que me atrapalhando, deixa eu apagar." Depois disso, "ela também é totalmente independente"; com 1 s, "infinite alternate vai ficar mudando para sempre".

### Curva própria

- "Eu quero que ele mude uma curva que eu vou criar": no cubic-bezier, "muito rápido [...] e no final, muito devagar [...] quase pararam"; "copy e no lugar do ease, você coloca essa cubic-bezier, você vai ver que agora o flow vai mudar". Com 15 s e 5 s a diferença some; com 2 s no box "ficou mais acentuada".

### Fecho

- "Treinem muito, fucem muito e exercitem a criatividade"; "desenvolver uma biblioteca de efeitos na sua cabeça". Repete a "biblioteca de exemplos" da aula 01 ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], [[wiki/concepts/repertorio]]).

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso.
- [[wiki/entities/cubic-bezier-com]]: de onde vem a curva copiada.
- [[wiki/entities/chrome-devtools]]: o "console" das aulas anteriores.

## Concepts

- [[wiki/concepts/keyframes-css]]: dois `@keyframes`, várias animações por vírgula, contagem finita.
- [[wiki/concepts/perspective-css]]: `preserve-3d` animado.
- [[wiki/concepts/shorthand-css]]: ordem duração/delay.
- [[wiki/concepts/easing]]: `ease` → `cubic-bezier`; `linear` para giro contínuo.
- [[wiki/concepts/background-css]]: o gradiente esconde a cor animada.
- [[wiki/concepts/taxa-de-quadros-60fps]]: `background-color` repinta a cada quadro.
- [[wiki/concepts/repertorio]]: "biblioteca de efeitos na sua cabeça".
- [[wiki/concepts/acessibilidade]], [[wiki/concepts/motion-design]].

## Precisões e tensões com a wiki

Todas `[skill: tech-mentor-frontend]` ou `[external]` sem fetch, por conhecimento prévio da especificação CSS Animations Level 1 e do MDN.

- **`ease` + `alternate` num giro de 0 a 360 dá um pêndulo, não um giro.** A caixa gira uma volta, desacelera, volta girando para trás. Para rotação contínua o usual é `linear` com direção `normal` e `infinite`: como 360deg e 0deg são a mesma posição, o recomeço não aparece. A wiki já registra essa regra em [[wiki/concepts/easing]]. Confiança alta.
- **A contagem finita também esconde o "voltar".** Sem `fill-mode`, a animação acaba e o elemento volta ao estilo da classe. Mas com rotação de 360 o fim e o começo coincidem: com 3 repetições alternadas, a última termina em 360deg, visualmente igual a 0. O "voltou" aparece porque os dois elementos param em momentos diferentes. Confiança média-alta.
- **Várias animações só convivem se mexem em propriedades diferentes.** `box` (`transform`) e `changeColor` (`background-color`) não brigam. Duas animações de `transform` no mesmo elemento brigariam e a última venceria, como registrado na aula 03 ([[wiki/concepts/keyframes-css]]). Confiança alta.
- **Por que o gradiente "atrapalha".** `linear-gradient` é `background-image` e fica por cima de `background-color`; a cor animada estava escondida. Gradientes não interpolam por padrão; para animar um, é preciso registrar as cores com `@property` ([[wiki/concepts/background-css]]). Confiança alta.
- **`background-color` não roda no compositor.** Cada quadro repinta a caixa: mais barato que layout, mais caro que `transform`/`opacity`. Num quadrado tanto faz; em áreas grandes ou muitos elementos, sim ([[wiki/concepts/taxa-de-quadros-60fps]]). Confiança alta.
- **As listas do shorthand se pareiam por posição.** `animation: box 3s ease infinite alternate, changeColor 1s ease infinite alternate`: cada item tem sua própria linha do tempo. Com as longhands, `animation-duration: 3s, 1s` casa com `animation-name: box, changeColor` pela ordem. Confiança alta.
- **A curva "muito rápido e no final muito devagar"** é um `ease-out` forte (família *expo-out*), o carro freando da aula anterior. Confiança alta.
- **Três animações infinitas, uma trocando de cor a cada segundo.** WCAG 2.2.2 pede pausa para movimento automático acima de 5 s; a troca vermelho↔azul em 1 s fica abaixo do limite de três clarões por segundo da 2.3.1, mas é o tipo de efeito que `prefers-reduced-motion` deve parar. Segue ausente ([[wiki/concepts/acessibilidade]]). Confiança alta.

## Open Questions

- O `forwards` "no máximo" contradiz o hábito de `infinite`: `forwards` só tem efeito em animações finitas.
- "O flow vai mudar": provável "o fluxo" no sentido de ritmo; deixado literal.
- "Quase pararam": plural pelos dois elementos? Deixado literal.

## Continuação

Fecha a sequência de `animation` do módulo "Básico CSS". A grade da parte 1 de transform ainda promete `opacity` e `position`.

A aula seguinte abre o módulo de SVG: [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]].

## Raw quotes

- "essa aqui de cara é a configuração que eu mais utilizo"
- "aqui é sempre a duração, aqui é sempre o delay"
- "eu separo uma linha da outra por uma vírgula"
- "desenvolver uma biblioteca de efeitos na sua cabeça"
