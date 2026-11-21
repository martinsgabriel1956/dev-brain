---
type: source
title: "Propriedade animation, parte 1: keyframes e as propriedades de animação (FrontPUSH)"
aliases: ["FrontPUSH motion, básico CSS aula 03", "Propriedade animation pt.1", "animation parte 1", "CSS Animations, básico CSS, aula 03"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [css, animation, keyframes, animation-fill-mode, animation-direction, animation-iteration-count, easing, w3schools, motion-design, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-20
---

# Propriedade animation, parte 1: keyframes e as propriedades de animação (FrontPUSH)

## TL;DR

Terceira aula do módulo "Básico CSS" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 20 minutos, com slide, código e as páginas do [[wiki/entities/w3schools|W3Schools]]. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência. "A tão esperada e tão aclamada propriedade de animação": `@keyframes` e as subpropriedades de `animation` ([[wiki/concepts/keyframes-css]]).

- **animation × transition:** os dois transitam entre estados; `transition` só tem dois (inicial e final), `animation` tem N, "mas é o mesmo princípio" ([[wiki/concepts/transition-e-transform-css]]).
- **`@keyframes box`** com `from`/`to` (dois estados) ou porcentagens (três ou mais). Anima "toda e qualquer propriedade do CSS"; o foco em `transform` é porque ela faz o que as básicas não fazem.
- **Subpropriedades:** `name`, `duration` (s ou ms), `direction` (`normal`, `reverse`, `alternate`, `alternate-reverse`), `iteration-count` (número ou `infinite`), `fill-mode` (`forwards`, `backwards`, `both`), `delay`, `timing-function` (curvas e `cubic-bezier`, próxima aula) e `play-state` (`running`/`paused`), demonstradas nos exemplos "Play it" do W3Schools.
- **O shorthand:** "eu não faço desse jeito": `animation: box 3s ease infinite alternate`. "Na grande maioria das minhas animações eu deixo infinite e alternate."

## Key Claims

### O slide

"Básico CSS" → "Animation": `animation-name` — "nome do @keyframes"; `animation-duration` — "tempo em s ou ms"; `animation-direction` — `normal | reverse | alternate | alternate-reverse`; `animation-fill-mode` — `none | forwards | backwards | both`; `animation-iteration-count` — `number | infinite`; `animation-delay` — "tempo em s ou ms"; `animation-timing-function` — `linear, ease, ease-in, ease-out, ease-in-out, ...` com estrela em "cubic.bezier"; `animation` — "resumo de todas as propriedades". Abaixo, uma linha do tempo 0% / 50% / 100% com uma curva.

### animation e transition

- Volta à aula de princípios: "nós temos uma linha do tempo, o CSS é de 0% até 100%, onde você define o tempo dela", e o keyframe é "o ponto-chave" ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]).
- "A tag animation simplesmente estabelece uma transição entre n estados, assim como a propriedade transition", usada no hover da aula anterior ([[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]). "A limitação do transition é que eu consigo utilizar apenas dois estados, um inicial e um final", com curva e tempo. "No animation eu consigo fazer essas configurações do transition e um pouco mais."

### @keyframes

- Antes, a "impressão de animação" vinha de mudar valores no console; agora "propriamente dito utilizando o keyframes". O nome `box` é "o mesmo nome da classe, não tem problema nenhum".
- O navegador "vai ver o que muda dentre as propriedades que você estabeleceu e vai fazer essa transição de forma suave e não abrupta".
- "Quando eu tenho apenas dois estados eu posso colocar from e to"; "se eu precisar de colocar três pontos ou mais, eu vou colocar por cento". `from`/`to` = `0%`/`100%`.
- "Eu posso moldar absolutamente toda e qualquer propriedade do CSS": "cor, largura, padding, altura, box model". Demo: `width` de 0 a 100 px. O foco em `transform` existe "porque com ela a gente vai conseguir fazer efeitos que com as propriedades básicas do CSS talvez a gente não consiga" ([[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]).

### As subpropriedades

- **`animation-name`**: "pega essa tag aqui box e segue o keyframe box".
- **`animation-duration`**: "literalmente o tempo da nossa linha do tempo", em segundos ou milissegundos.
- **`animation-direction`**: `normal` (0% → 100%, o padrão), `reverse` (100% → 0%), `alternate` (vai e volta) e `alternate-reverse` (volta e vai). `alternate` "faz sentido" com mais de uma repetição.
- **`animation-iteration-count`** (dito "interaction", corrigido na hora: "é iteration"): número fixo ou infinito. "Você tem que tomar cuidado para colocar um alternate de forma que não fique abrupto."
- **`animation-fill-mode`**: "normal, como o valor padrão" (o slide diz `none`). Com `width: 100` na classe e keyframe até 150, sem fill-mode "ele vai de 0 até 150 e quando acabar [...] ele vai voltar para 100"; `forwards` fica no estado final; `backwards` "começa com as características do frame inicial"; `both`, visto no W3Schools, faz os dois.
- **`animation-delay`**: "um tempo para você deixar meio que em standby"; padrão 0 s.
- **`animation-timing-function`** (dito "time function"): "é a forma, é a curva"; quatro curvas-padrão e `cubic-bezier` para "criar sua própria curva", na próxima aula. "Na maioria das vezes eu utilizo o ease" ([[wiki/concepts/easing]]).
- **`animation-play-state`**: "tipo um play-pause, literalmente": `running` (padrão) ou `paused`.

### Os exemplos do W3Schools

- "Nessas mesmas propriedades do W3Schools [...] tem vários exemplos e falam o valor padrão da propriedade"; "você basta vir aqui em Play It". Ver [[wiki/entities/w3schools]].
- `both`: div vermelha, primeiro keyframe amarelo, último azul, delay de 2 s; com `both` "ele já vai começar, independente do delay, nas configurações do primeiro keyframe". `backwards`: começa amarelo durante o delay. `forwards`: termina e fica "200 pixels [...] e o background blue".
- `ease` "é mais rápido no começo e mais devagar no final"; o exemplo do `ease-in` "está ruim", com promessa de um melhor na próxima aula.

### O shorthand

- "Essa tag animation aqui é um resumo de todas as outras propriedades [...] eu não faço desse jeito": nome `box`, "três segundos", "a forma da curva, que é ease", "infinity" e `alternate`, "tudo isso em uma tag só". Ver [[wiki/concepts/shorthand-css]].

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; módulo "Básico CSS" do mini curso.
- [[wiki/entities/w3schools]]: agora chamado pelo nome certo; exemplos "Play it".
- [[wiki/entities/w3c]]: o "W3C" das aulas anteriores era este W3Schools.

## Concepts

- [[wiki/concepts/keyframes-css]]: `@keyframes` e as subpropriedades de `animation`.
- [[wiki/concepts/transition-e-transform-css]]: transition (dois estados) × animation (N).
- [[wiki/concepts/easing]]: `animation-timing-function`, `ease` como padrão dele.
- [[wiki/concepts/shorthand-css]]: o atalho `animation`.
- [[wiki/concepts/taxa-de-quadros-60fps]]: animar `width` refaz layout a cada quadro.
- [[wiki/concepts/acessibilidade]], [[wiki/concepts/wcag]]: loops infinitos e pausa.
- [[wiki/concepts/motion-design]].

## Precisões e tensões com a wiki

Todas `[skill: tech-mentor-frontend]` ou `[external]` sem fetch, por conhecimento prévio da especificação CSS Animations Level 1 (w3.org/TR/css-animations-1), do MDN e das WCAG 2.2.

- **O "W3C" era o W3Schools.** Aqui ele diz "W3Schools" e usa o "Play it" do site, confirmando a leitura das aulas anteriores ([[wiki/entities/w3c]]). Confiança alta.
- **`animation` é propriedade; `@keyframes` é at-rule.** "Tag" é lapso, e `from`/`to` não são tags. Confiança alta.
- **"Toda e qualquer propriedade" vale para as animáveis.** Propriedades discretas (`display`, `visibility`, `font-family`) trocam de golpe no meio do intervalo; `display` só ganhou animação suave com `transition-behavior: allow-discrete` e `@starting-style` (2023–2024). Confiança média-alta.
- **A demo anima `width`**, o caso que a aula 07 de otimização desaconselha: refaz layout a cada quadro. Para "crescer", `transform: scaleX()` faz o mesmo no compositor ([[wiki/concepts/taxa-de-quadros-60fps]]). Confiança alta.
- **Keyframes faltando:** sem `0%`/`from` ou `100%`/`to`, o navegador usa o estilo atual do elemento. "Quando eu tenho apenas 2%" é lapso de "dois pontos". Confiança alta.
- **O padrão do fill-mode é `none`, não "normal"**, como o próprio slide diz. Confiança alta.
- **`forwards` guarda o último keyframe *executado*.** Com `reverse`, ou com `alternate` e número par de repetições, o último é o `0%`. E o valor mantido pela animação vence as declarações normais na cascata: depois de um `forwards`, um `:hover` que mude a mesma propriedade não tem efeito. Confiança alta.
- **`infinity` não é valor de `animation-iteration-count`; o certo é `infinite`.** No shorthand, `infinity` seria lido como um segundo nome e invalidaria a declaração inteira. Como "executa normalzinho", o código provavelmente tinha `infinite` (autocompletar) e só a fala trocou. Confiança alta na regra, média no que estava na tela.
- **Iteration-count aceita fração** (`0.5` = metade da linha do tempo). **Delay aceita negativo:** `-1s` começa a animação já no meio, útil para defasar loops iguais. Confiança alta.
- **A timing function vale por intervalo, não para a animação inteira.** Com `0%`, `50%` e `100%`, o `ease` se aplica de 0 a 50 e de novo de 50 a 100. Também pode ser trocada dentro de um keyframe ([[wiki/concepts/easing]]). Confiança alta.
- **`ease`** começa um pouco lento, acelera rápido e desacelera longamente (`cubic-bezier(0.25, 0.1, 0.25, 1)`); "mais rápido no começo" é aproximação. Confiança alta.
- **Ordem no shorthand:** o primeiro tempo é `duration`, o segundo é `delay`; o resto é reconhecido pelo tipo. Evite nomes de keyframes iguais a palavras-chave (`ease`, `none`, `infinite`). Confiança alta.
- **`play-state`** é o gancho para pausar no hover ou via JS (trocando uma classe); o "DefaultFollowing" da legenda deve ser o "Default value: running" do W3Schools. Confiança média.
- **Loop infinito e acessibilidade.** "Infinite e alternate" como padrão bate na WCAG 2.2.2 (Pausar, parar, ocultar): movimento automático com mais de 5 s ao lado de outro conteúdo precisa de um jeito de pausar. `prefers-reduced-motion` segue ausente ([[wiki/concepts/acessibilidade]], [[wiki/concepts/wcag]]). Confiança alta.
- A aula 03 de princípios já tinha mostrado `fill-mode` como "como terminar" e o conflito de duas animações de `transform` ([[wiki/concepts/keyframes-css]]).

## Open Questions

- "O from é tipo assim desde aqui ou então fato inicial": provável "ponto inicial" ou "fator"; deixado literal.
- "Apertar aqui o Runner": provável botão "Run" do W3Schools; deixado literal.
- "Aqui é o DefaultFollowing": ver Precisões; deixado literal.
- "Fill mode, o direction, delay" é reconstrução de "Filmou o direction delay" (confiança média).

## Continuação

A próxima aula promete as curvas de `animation-timing-function` e `cubic-bezier` e "de fato botar essa nossa animação aqui para rodar".

## Raw quotes

- "a tão esperada e tão aclamada propriedade de animação"
- "a limitação do transition é que eu consigo utilizar apenas dois estados"
- "eu posso moldar absolutamente toda e qualquer propriedade do CSS"
- "na grande maioria das minhas animações eu deixo infinite e alternate"
- "tipo um play-pause, literalmente"
