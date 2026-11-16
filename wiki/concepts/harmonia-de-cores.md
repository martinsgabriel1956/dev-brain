---
type: concept
title: "Harmonia de cores"
aliases: ["harmonia das cores", "color harmony", "esquemas de cor", "monocromática", "complementar", "análoga", "triádica", "split complementary", "complementar dividida"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, harmonia-de-cores, circulo-cromatico, paleta-de-cores, contraste, gradiente]
skill: ux-ui-mentor
status: stub
---

# Harmonia de cores

Regras para escolher cores que funcionam juntas a partir da posição delas no [[wiki/concepts/circulo-cromatico]]. É a base para montar uma [[wiki/concepts/paleta-de-cores]] e para explicar por que certas combinações aparecem em todo lugar ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]).

## Os quatro tipos da aula

| Tipo | Posição no círculo | Para quê (segundo a aula) | Exemplo da aula |
|---|---|---|---|
| Monocromática | uma matiz, mais clara e mais escura | [[wiki/concepts/hierarquia-visual]], sobretudo no texto | céu do claro ao escuro; verde do slide |
| Complementar | opostas | "ótimo contraste"; guiar o usuário e destacar elementos | arara azul e amarela/laranja; capas de filme azul e laranja |
| Análoga | vizinhas | composição, gradiente, transição suave | céu do rosa ao azul |
| Triádica | triângulo equidistante | paletas "harmonicamente perfeitas" | Homem-Aranha e Superman (azul, vermelho, amarelo) |

O [[wiki/entities/adobe-color]] tem mais regras: "dividir complementar" (as vizinhas do oposto), a versão "duas vezes", quadrado, composto e sombras. O autor diz usar pouco quadrado e composto.

## Princípio, não receita

"A parte de cores em design é muito subjetiva. Ela segue esses princípios aqui, mas tem inúmeras, muitas variações." O mesmo tom de [[wiki/concepts/harmonia-visual]] e de [[wiki/concepts/porque-das-decisoes-de-design]]: entender o porquê antes de aplicar.

## Harmonia de cores × harmonia visual

[[wiki/concepts/harmonia-visual]] é a coerência de mensagem entre forma, tipografia, cor e ilustração. Harmonia de cores é só a parte da cor, e é geométrica: depende de ângulos no círculo, não do público. Uma tríade "perfeita" pode ser desarmônica numa loja de bebês.

## Monocromática não é só mexer no brilho

"Não basta somente tirar brilho ou adicionar brilho para a gente conseguir variações legais." `[skill: ux-ui-mentor]` Em HSL, o mesmo L em matizes diferentes parece mais ou menos claro; OKLCH é perceptualmente uniforme. Escalas boas (50–950) costumam girar um pouco a matiz e baixar o croma nos extremos, o que o Adobe Color mostra: "não é a mesma matiz essa relação".

## Complementar: contraste de matiz não é contraste de luminância

A aula usa o complementar para destacar. `[skill: ux-ui-mentor]` Destaque de matiz não substitui contraste de luminância: complementares saturadas lado a lado vibram, e texto de uma sobre a outra raramente passa em WCAG. Use o complementar como acento escasso (Isolation Effect, ver [[wiki/concepts/contraste]]) e confira o par de texto separadamente.

## Análoga e gradiente

Vizinhas transitam sem passar por tons "sujos", por isso o gradiente análogo é tão comum. `[external]` Em CSS, `linear-gradient(in oklch, …)` interpola num espaço perceptual e evita a faixa acinzentada no meio que o sRGB produz entre cores distantes (CSS Color 4: https://www.w3.org/TR/css-color-4/#interpolation). Gradientes também são [[wiki/concepts/elementos-de-composicao]] de fundo.

## Key Sources

- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — os quatro tipos, exemplos da natureza, super-heróis e cinema; tour pelo Adobe Color
