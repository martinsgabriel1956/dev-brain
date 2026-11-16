---
type: source
title: "Variáveis no Sass: consistência do style guide e sombra numa variável (FrontPUSH)"
aliases: ["Variáveis Sass FrontPUSH", "módulo de CSS Sass, aula 04", "variáveis SCSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, variaveis, design-tokens, style-guide, consistencia, box-shadow, hover, figma, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-variaveis-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Variáveis no Sass (FrontPUSH)

## TL;DR

Aula 04 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/variaveis-sass]].

- **Sintaxe:** "um dólar, como se fosse em PHP", nome, dois pontos e valor. O slide mostra `$preto: #000; $branco: #FFF; $gray1: #111; $gray2: #555; $box-shadow-blue: [...]`.
- **Para quê:** "organização e consistência no design", "maior fidelidade quando passar o layout para a codificação". Serve para cores, tipografia e propriedades inteiras, "porque literalmente é um copia e cola".
- **Ponte com UI:** no [[wiki/concepts/style-guide]] do projeto Nubank, trocar a matiz de um roxo (277 → 286 no HSB) por descuido quebra a [[wiki/concepts/consistencia-visual]]: "meio que um pecado no design". Variáveis guardam os valores documentados ([[wiki/concepts/design-tokens]]).
- **Demo:** botão `.link` roxo (`inline-block`, padding, `border-radius: 8px`); sombra feita com o plugin Smooth Shadow no [[wiki/entities/figma]], copiada do Inspect para uma variável em `_shadows.scss` e aplicada no `:hover` com `transition: 0.5s` ([[wiki/concepts/sombra-em-interfaces]]).
- **Troca num lugar só:** suavizou a sombra no Figma, recopiou o CSS para a variável, e o botão mudou.

## Key Claims

### O recurso

- "Variáveis, como o próprio nome já diz, permite a criação de variáveis: cores, componentes, propriedades do CSS e etc."
- "Também pode ser utilizado para propriedades de CSS, não só para cores, porque literalmente é um copia e cola. Então, o que estiver dentro dessa variável, se você copiar e colar no lugar certo no seu CSS, vai funcionar perfeitamente."
- "Você define aqui um dólar, como se fosse em PHP [...] você escreve a sua string, dois pontos, e aqui coloca o valor da variável."

### Consistência e style guide

- "Uma das coisas mais fundamentais no design é ter consistência. O que significa ter consistência? É que a mesma cor é aplicada ao longo do meu projeto."
- O erro típico: esquecer a cor e mexer na matiz; "ao longo da minha interface, eu trabalho com tons diferentes de roxo". "Esse aqui está na mesma matiz, é variação de cor, mas aqui eu estou modificando a matiz [...] está em 277. Esse aqui está em 286." Ver [[wiki/concepts/modelo-de-cor-hsb]] e [[wiki/concepts/variacao-de-cores]].
- "Quando eu não tenho variáveis guardando esses valores [...] faz com que eu perca a qualidade [...] na implementação do meu layout."
- O style guide tem "cores primárias, cores secundárias, cores auxiliares, cores brancas e pretas para composição de texto, cores em escala de cinza para poder estabelecer hierarquia textual, gradientes", tudo com hexadecimal.
- Tipografia: no Inspect, `font-family`, `font-style`, `font-weight`, tamanho e `line-height`; H1–H3 e B1–B3 "são todos padronizados" ([[wiki/concepts/escala-tipografica]]). "Até aqui está errado, não é Montserrat, é Sora": o próprio style guide tinha a fonte errada.
- Botões: se o designer achar o `box-shadow` "muito agressivo", troca-se a opacidade de 0.8 para 0.3 na variável.

### Demonstração

- `body` com `flex-direction: column` para o link descer ([[wiki/concepts/flexbox]]).
- `.link`: `text-decoration: none`, `font-size: 24px`, `color: $branco`, fundo no roxo do Nubank, `display: inline-block` "para poder virar o elemento de caixa" ([[wiki/concepts/display-css]]), padding 12/24, `border-radius: 8px`, `margin-top: 24px`.
- Hover: "ele cresça um box-shadow, indicando que isso é um elemento clicável, para poder melhorar a experiência do usuário" ([[wiki/concepts/affordance]], [[wiki/concepts/pseudo-classe-css]]).
- Smooth Shadow: "é sempre bom utilizar as sombras da mesma cor do elemento [...] deixa as minhas sombras mais realistas". Ajusta camadas (layers), alpha e blur; exagerado de propósito, "colocaria bem mais sutil em projetos reais".
- Do Inspect, copia só os valores do `box-shadow` para a variável "box-shadow purple" em `shadows`, importa o arquivo e usa no hover. Deu erro: "é porque eu coloquei o shadows sem o nosso querido underline" ([[wiki/concepts/import-e-partials-sass]]). "O Sass também tem esse recurso de mostrar para nós os erros."
- `transition` de 0.5 s "para que essa transição seja suave" ([[wiki/concepts/transition-e-transform-css]]).

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 04 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: style guide do projeto do curso; roxo do botão.
- [[wiki/entities/figma]]: Inspect e plugin Smooth Shadow.
- [[wiki/entities/live-sass-compiler]]: mostrou o erro de compilação.

## Concepts

- [[wiki/concepts/variaveis-sass]]
- [[wiki/concepts/variaveis-css]]
- [[wiki/concepts/design-tokens]]
- [[wiki/concepts/style-guide]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/modelo-de-cor-hsb]]
- [[wiki/concepts/variacao-de-cores]]
- [[wiki/concepts/escala-tipografica]]
- [[wiki/concepts/sombra-em-interfaces]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/pseudo-classe-css]]
- [[wiki/concepts/transition-e-transform-css]]
- [[wiki/concepts/display-css]]
- [[wiki/concepts/import-e-partials-sass]]
- [[wiki/concepts/pre-processador-css]]

## Precisões e tensões com a wiki

- **Não é bem "copia e cola".** `[external]` O valor de uma variável do Sass é uma expressão avaliada: `$x: 10px + 6px` vale `16px`, e listas, mapas e cores podem ser manipulados (https://sass-lang.com/documentation/variables/). Para o uso da aula (guardar um `box-shadow` inteiro), o efeito é o mesmo de colar o texto.
- **O nome não é string.** É um identificador: `$box-shadow-purple`. No Sass, hífen e underline são equivalentes nos nomes (`$box_shadow_purple` é a mesma variável). O slide usa `$gray1`/`$gray2` em inglês, ao lado de `$preto`/`$branco`, a mistura que a [[wiki/sources/frontpush-import-e-partials-sass|aula 03]] chamou de "não é legal".
- **Variável do Sass × custom property.** `[skill: tech-mentor-frontend]` A `$variável` some na compilação; o CSS final só tem o valor. Para tema escuro ou troca em tempo de execução, é preciso custom property (`--cor`). Prática comum hoje: tokens em Sass ou JSON gerando `:root { --... }` ([[wiki/concepts/variaveis-css]], [[wiki/concepts/design-tokens]]).
- **O underline não corrige erro de compilação.** Sem `_`, o `shadows.scss` só ganharia um `shadows.css` vazio a mais; `@import "shadows"` acha o arquivo com ou sem underline. O erro mostrado deve ter tido outra causa (nome da variável, arquivo apagado no meio). A explicação dele não fecha; confiança média.
- **Onde vai a `transition`.** `[external]` Na regra base (`.link`), não só no `:hover`; senão a sombra some de uma vez ao tirar o mouse. A legenda não mostra onde ele pôs. Ver [[wiki/concepts/transition-e-transform-css]].
- **Animar `box-shadow` custa repaint.** `[skill: tech-mentor-frontend]` Com várias camadas, cada quadro repinta. A técnica barata é pôr a sombra num `::after` e animar só a `opacity`. Para um botão isolado, tanto faz.
- **Hover não chega ao teclado nem ao toque.** O mesmo realce deveria valer em `:focus-visible` ([[wiki/concepts/pseudo-classe-css]]).
- **"Style guide do Nubank"** é o do projeto de estudo do curso (o clone com a fonte Sora), não um documento oficial do Nubank ([[wiki/entities/nubank]]).
- **Matiz diferente ≠ variação.** Bate com [[wiki/concepts/variacao-de-cores]]: variar é mexer em brilho e saturação mantendo a matiz.

## Open Questions

- Qual era o hexadecimal do roxo usado no botão? A legenda não diz.
- Qual foi o erro de compilação de verdade? Ver as precisões acima.

## Raw quotes

- "literalmente é um copia e cola"
- "meio que um pecado no design eu ficar fugindo da paleta de cores"
- "é sempre bom utilizar as sombras da mesma cor do elemento"
