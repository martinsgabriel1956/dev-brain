---
type: concept
title: "Alinhamento de Texto"
aliases: ["text-align", "alinhamento à esquerda", "texto centralizado", "texto justificado", "alinhamento tipográfico"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 2
tags: [ui, ui-design, tipografia, alinhamento, alinhamento-de-texto, legibilidade, css, design-responsivo]
skill: ux-ui-mentor
status: stub
---

# Alinhamento de Texto

Eixo em que as linhas de um texto se alinham: esquerda, centro, direita ou justificado. Variável da [[wiki/concepts/tipografia]] que pesa no conforto de leitura ([[wiki/sources/alinhamento-e-espacamento-de-texto]]). É o uso "alinhamento" do [[wiki/concepts/eixo-visual]] aplicado a linhas de texto.

## Quando usar cada um

| Alinhamento | Uso na aula | Por quê |
|---|---|---|
| **Esquerda** | Padrão; "o coringa", cerca de 90% da web | Leitura da esquerda para a direita; padrão do CSS; borda esquerda fixa no responsivo |
| **Centralizado** | Títulos e trechos curtos em cards | Trecho curto não cansa; o autor centraliza só uma seção de cards do próprio site |
| **Direita** | Pequenas ações (link no canto direito), ao lado de ilustração | Raro; "meio que é feio", o autor prefere a esquerda mesmo assim |
| **Justificado** | Nunca | Sem hifenização, os espaços entre palavras ficam irregulares e a leitura piora |

## Por que a esquerda vence

A borda esquerda dá ao olho um ponto fixo para voltar a cada linha. A aula soma o argumento do [[wiki/concepts/design-responsivo]]: ao mudar a largura da tela, a esquerda fica e a direita se move, então texto à esquerda não muda de lugar. Referência: o [[wiki/entities/new-york-times]] alinha tudo à esquerda.

## Olhar de dev

`[external]` O valor inicial de `text-align` no [[wiki/concepts/css]] é `start`, não `left`: segue a direção do idioma (esquerda em LTR, direita em RTL). Preferir `start`/`end` a `left`/`right` mantém a regra válida em interfaces bilíngues. https://developer.mozilla.org/en-US/docs/Web/CSS/text-align

`[external]` Justificado em coluna estreita forma "rios" de espaço; `hyphens: auto` com `lang` correto ameniza, mas a WCAG 1.4.8 (AAA) pede texto não justificado: https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html. `[skill: ux-ui-mentor]` A skill manda evitar justificado no mobile pelo mesmo motivo.

## Armadilha comum

Centralizar parágrafos longos por estética: cada linha começa num ponto diferente e o olho perde a volta. Centralizado é para poucas linhas.

## text-align e vertical-align

Em [[wiki/sources/principais-propriedades-css-color-background-font]], `text-align` faz o "ajuste horizontal" e `vertical-align` o vertical. `[external]` `vertical-align` só age em elementos inline, inline-block e células de tabela; centralizar um bloco na vertical pede flexbox ou grid (https://developer.mozilla.org/en-US/docs/Web/CSS/vertical-align).

## Key Sources

- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — esquerda como padrão, centralizado em cards, direita rara, justificado nunca
- [[wiki/sources/principais-propriedades-css-color-background-font]]: text-align horizontal; vertical-align só em inline e células
