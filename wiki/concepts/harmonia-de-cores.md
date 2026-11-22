---
type: concept
title: "Harmonia de cores"
aliases: ["harmonia das cores", "harmonia cromática", "color harmony", "esquemas de cor", "cores análogas", "cores complementares", "monocromática", "complementar", "análoga", "triádica", "paleta monocromática", "paleta triádica", "split complementary", "split-complementary", "complementar dividida", "dividir complementar"]
date_created: 2026-11-14
date_updated: 2026-11-22
source_count: 4
tags: [ui, ui-design, cor, teoria-das-cores, harmonia, harmonia-de-cores, circulo-cromatico, paleta-de-cores, contraste, gradiente]
skill: ux-ui-mentor
status: stub
---

# Harmonia de cores

Regras para escolher cores que funcionam juntas a partir da posição delas no [[wiki/concepts/circulo-cromatico]]: **análogas** (vizinhas), **complementares** (opostas) e os demais esquemas abaixo. É a base para montar uma [[wiki/concepts/paleta-de-cores]] e para explicar por que certas combinações aparecem em todo lugar ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). Na aula de paleta de [[wiki/entities/nasser|Násser]], é o que faz uma paleta "fazer sentido": "como as cores se conectam umas às outras" ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]). Gradientes suaves costumam ligar análogas.

A aula de paleta cita uma aula própria de harmonia como anterior; quando ela foi ingerida, essa aula ainda não estava na wiki. Hoje o tema está em [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] (inferência: provavelmente a mesma aula).

## A natureza como referência

Na abertura do módulo de [[wiki/concepts/teoria-das-cores]] ([[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]):

- **Céu → gradiente suave:** do rosa para o azul, do azul claro para o escuro, do abóbora para o azul; "não acontece uma faixa sólida de uma cor aqui e uma faixa sólida de uma cor aqui".
- **Pássaro → complementares:** "azul tendendo para o ciano" e "cor de abóbora", "facilmente utilizada e aplicada em interfaces".
- **Arara → amarelo e azul**, as cores do Banco do Brasil: "foi por coincidência?".

## Os esquemas

A aula de harmonia apresenta quatro tipos ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]); a aula de paleta usa os mesmos e acrescenta o complementar dividido ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]).

| Esquema | Posição no círculo | Para quê, na aula de harmonia | Uso na aula de paleta |
|---|---|---|---|
| Monocromático | uma matiz, mais clara e mais escura (vários tons) | [[wiki/concepts/hierarquia-visual]], sobretudo no texto; céu do claro ao escuro; verde do slide | contraste por claro x escuro + neutros |
| Complementar | opostas | "ótimo contraste"; guiar o usuário e destacar elementos; arara azul e amarela/laranja; capas de filme azul e laranja | base + enfoque (roxo ↔ amarelo; azul ↔ laranja) |
| Análogo | vizinhas | composição, gradiente, transição suave; céu do rosa ao azul | uma escura, uma clara (azul + turquesa) |
| Triádico | triângulo equidistante | paletas "harmonicamente perfeitas"; Homem-Aranha e Superman (azul, vermelho, amarelo) | uma predominante, duas de destaque |
| Complementar dividido | as duas vizinhas do oposto | (no [[wiki/entities/adobe-color]], como "dividir complementar") | alternativa ao complementar na base + enfoque |

O [[wiki/entities/adobe-color]] tem mais regras: "dividir complementar" (as vizinhas do oposto), a versão "duas vezes", quadrado, composto e sombras. O autor diz usar pouco quadrado e composto ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]).

## Qual círculo: RYB ou RGB

As fontes e as notas não usam o mesmo círculo, e os complementos mudam conforme o círculo:

- `[external]` No círculo de luz (RGB/HSB), laranja (~30°) e azul-ciano (~210°) são opostos, assim como amarelo (60°) e azul (240°). Nessa leitura, o pássaro e a arara da aula de teoria são complementares. No círculo de pintor (RYB), o complemento do amarelo é o violeta. Ver [[wiki/concepts/modelos-de-cor]].
- `[external]` A aula de paleta usa o círculo RYB (o de pintura). Nele, o complemento do violeta é o amarelo, e o complementar dividido do violeta são amarelo-laranja e amarelo-verde. A aula põe o dividido "no vermelho ou no laranja" (vizinhos do próprio violeta); o verde do slide é a leitura que bate com a teoria. Alguns exemplos falados também saem da definição (laranja e roxo como "análoga"; azul e verde como "complementar"). Ver as tensões em [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]].
- `[skill: ux-ui-mentor]` O círculo HSL/OKLCH é o RGB, não o RYB: o complemento do violeta ali é um verde-amarelado, não o amarelo puro.

Ou seja: o par roxo ↔ amarelo da aula de paleta é complementar no RYB, e o par amarelo ↔ azul da arara é complementar no RGB. As páginas de origem não registram qual círculo a aula de teoria usa.

## Princípio, não receita

"A parte de cores em design é muito subjetiva. Ela segue esses princípios aqui, mas tem inúmeras, muitas variações" ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). Na aula de paleta, a combinação "é tão vasta" que parece subjetiva, mas segue os esquemas ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]). O mesmo tom de [[wiki/concepts/harmonia-visual]] e de [[wiki/concepts/porque-das-decisoes-de-design]]: entender o porquê antes de aplicar.

## Harmonia de cores × harmonia visual

[[wiki/concepts/harmonia-visual]] é a coerência de mensagem entre forma, tipografia, cor e ilustração. Harmonia de cores é só a parte da cor, e é geométrica: depende de ângulos no círculo, não do público. Uma tríade "perfeita" pode ser desarmônica numa loja de bebês.

## Monocromática não é só mexer no brilho

"Não basta somente tirar brilho ou adicionar brilho para a gente conseguir variações legais" ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). `[skill: ux-ui-mentor]` Em HSL, o mesmo L em matizes diferentes parece mais ou menos claro; OKLCH é perceptualmente uniforme. Escalas boas (50–950) costumam girar um pouco a matiz e baixar o croma nos extremos, o que o Adobe Color mostra: "não é a mesma matiz essa relação".

## Complementar: contraste de matiz não é contraste de luminância

Complementares geram [[wiki/concepts/contraste]] forte, e a aula usa o complementar para destacar. `[skill: ux-ui-mentor]` Destaque de matiz não substitui contraste de luminância: complementares saturadas lado a lado vibram, e texto de uma sobre a outra raramente passa em WCAG. Contraste (WCAG) não depende do esquema: duas cores complementares de mesma luminosidade podem falhar 4.5:1. Use o complementar como acento escasso (Isolation Effect, ver [[wiki/concepts/contraste]]) e confira o par de texto separadamente.

## Análoga e gradiente

Análogas dão continuidade e [[wiki/concepts/harmonia-visual]]. Vizinhas transitam sem passar por tons "sujos", por isso o gradiente análogo é tão comum. `[external]` Em CSS, `linear-gradient(in oklch, …)` interpola num espaço perceptual e evita a faixa acinzentada no meio que o sRGB produz entre cores distantes (CSS Color 4: https://www.w3.org/TR/css-color-4/#interpolation). Gradientes também são [[wiki/concepts/elementos-de-composicao]] de fundo, e o gradiente sobre imagem (capa para texto branco) já aparece na wiki em fontes de imagens.

## Olhar de dev

`[skill: ux-ui-mentor]` Em HSL ou OKLCH, os esquemas viram aritmética de matiz (H): complementar = H + 180°, dividido = H + 150° e H + 210°, triádico = H + 120° e H + 240°, análogo = H ± 30°. Como dito acima, esse círculo é o RGB, não o RYB das aulas.

## Gradiente tem página própria

As regras de gradiente da mentoria de identidade visual (bad gradient vermelho → ciano, vizinhas, mesma matiz) estão em [[wiki/concepts/gradiente]]. A mesma aula usa as análogas na leitura da paleta de Nina Talks (rosa + azul, "por mais que tenha um roxo aqui no meio").

## Key Sources

- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — céu, pássaro e arara como guias para análogas, gradientes e complementares
- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — os quatro tipos, exemplos da natureza, super-heróis e cinema; tour pelo Adobe Color
- [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]] — círculo cromático (RYB) aplicado a quatro tipos de paleta e ao complementar dividido; exemplos falados sobre telas
- [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]: gradiente pelo círculo cromático; Nina Talks análoga
