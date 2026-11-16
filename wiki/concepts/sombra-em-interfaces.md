---
type: concept
title: "Sombra em interfaces"
aliases: ["sombra", "drop shadow", "box-shadow", "elevação", "sombra suave", "smooth shadow", "sombra em camadas", "layered shadow"]
date_created: 2026-11-14
date_updated: 2026-11-16
source_count: 7
tags: [ui, ui-design, sombra, drop-shadow, elevacao, botoes, hover, design-system, css]
skill: ux-ui-mentor
status: stub
---

# Sombra em interfaces

Sombra projetada (drop shadow, `box-shadow` no CSS) dá profundidade e elevação a um elemento. Nos botões do curso, serve de resposta ao hover ([[wiki/concepts/feedback-do-sistema]]). Uma sombra tem quatro parâmetros e uma cor: offset (x, y), blur, spread e cor com opacidade.

## Parâmetros, como a aula define

| Parâmetro | Definição na aula | Regra prática |
|---|---|---|
| Offset | "Literalmente o deslocamento da sombra" | "Deixar deslocada para baixo" |
| Blur | "O quão desfocado está a sombra" | Igual ou o dobro do offset |
| Spread | Cresce ou encolhe a sombra | Negativo, para ela ficar só embaixo |
| Cor / alpha | Opacidade da sombra | "Bem pouquinho"; cor da marca a no máximo 40% |

Fonte: [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]].

## Sombra suave: embaixo, não em volta

"Não é para ficar ao redor de tudo, é para ficar na parte de baixo, compreendendo aqui mais ou menos 80%." O spread negativo encurta a sombra até ela ocupar cerca de 80% do elemento ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]). O slide da aula teórica já usava `box-shadow: 0px 4px 25px -10px` em repouso e a cor do botão a 0.8 no hover ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).

## Três formas de chegar lá

1. **Camadas (plugin Smooth Shadow):** quatro a seis layers de drop shadow; a mais perto tem mais opacidade e as afastadas ficam mais transparentes, "dando aquela sensação de penumbra". `[external]` É a técnica de empilhar `box-shadow` com opacidade decrescente (https://shadows.brumm.af/).
2. **Copiar um design system:** o [[wiki/entities/pegasus-design-system]] usa y 32, blur 64 e 8% de um cinza escuro nos cards.
3. **O "curinga":** y 16, blur 32, cor da marca a 25–40%, spread de −10 a −16.

```css
/* curinga da aula, com a cor da marca a 25% */
.button:hover {
  box-shadow: 0 16px 32px -12px rgb(252 189 56 / 0.25);
}
```

O valor `rgb(252 189 56)` vem da cor de hover do slide da aula teórica. O CSS é ilustração, não foi mostrado na aula.

## Olhar de dev

`[skill: ux-ui-mentor]` A sombra vira token (`shadow-sm`, `shadow-md`, `shadow-lg`, cada uma com finalidade clara), com o tipo `shadow` (offsetX, offsetY, blur, spread, color) no formato de design tokens. No dark mode as sombras somem: a elevação passa para superfícies mais claras ou bordas sutis. Hover precisa de par em focus e active. `[external]` Animar `box-shadow` repinta a cada frame; para hover frequente, animar a `opacity` de um pseudo-elemento que já tem a sombra é mais barato.

## No style guide

A sombra do card no hover precisa estar escrita, com o CSS, porque o dev pode não abrir o Figma. `box-shadow` é um dos valores da aba inspect que "sempre agregam", e a sombra vira um grupo de estilo no Figma ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). Ver [[wiki/concepts/style-guide]].

## Sombra como estilo

Sombras viram effect styles com grupo e nome (`Shadow / Shadow purple 2`), reordenáveis e editáveis em um lugar ([[wiki/concepts/estilos-no-figma]]). Na mesma aula, o Smooth Shadow é ajustado com offset "o mais centralizado possível", ao contrário da regra "deslocada para baixo" da aula de botões; os estilos shadow purple e shadow black seguem a regra antiga ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Documentar a sombra

Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: "para o desenvolvedor é muito complicado dizer quais são as sombras do CSS". O Inspect do [[wiki/entities/figma]] entrega o `box-shadow` pronto, com as quatro camadas de drop shadow, o RGBA e as opacidades; basta copiar para o [[wiki/concepts/style-guide]]. Ver [[wiki/concepts/handoff-design-dev]].

## text-shadow x box-shadow

Em [[wiki/sources/principais-propriedades-css-color-background-font]]: `text-shadow` aplica sombra no texto e `box-shadow` "sombra em caixa". `[external]` `text-shadow` não tem spread nem `inset`; as várias camadas do Smooth Shadow só funcionam em `box-shadow` com valores separados por vírgula (https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow).

## Sombra numa variável

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], o `box-shadow` de várias camadas usado no arquivo todo é o exemplo de variável: muda num lugar só. Vale também para custom properties ([[wiki/concepts/variaveis-css]]).

## Key Sources

- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: Smooth Shadow, Pegasus, o "curinga", spread negativo, 80% do elemento
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: sombra de hover da cor do botão; valores do slide
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — sombra de hover documentada; box-shadow do inspect; grupo de estilo de sombra
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]: sombras como effect styles; Smooth Shadow com offset centralizado (tensão)
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]] — copiar o box-shadow de quatro camadas do Inspect para o style guide
- [[wiki/sources/principais-propriedades-css-color-background-font]]: text-shadow no texto, box-shadow na caixa
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: introdução ao Sass: box-shadow de várias camadas numa variável
