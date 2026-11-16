---
type: concept
title: "Variação de cores"
aliases: ["Variação tonal de cor", "variação tonal de cor", "variação tonal", "tints and shades", "tint", "shade", "tons mais claros e mais escuros", "escala de cor", "color scale", "rampa de cor", "variação no HSB"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 5
tags: [ui, ui-design, cor, paleta, paleta-de-cores, hsb, saturacao, brilho, matiz, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Variação de cores

Gerar tons mais claros e mais escuros de uma mesma cor da [[wiki/concepts/paleta-de-cores]] sem quebrar a [[wiki/concepts/harmonia-visual|harmonia]]. É o que alimenta estados (hover, ativo), hierarquia, paletas monocromáticas, fundos e neutros tingidos. Duas aulas de [[wiki/entities/nasser|Násser]] tratam disso: uma teórica, com a regra ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]), e uma prática no [[wiki/concepts/modelo-de-cor-hsb]], com os números ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]).

## Para que serve

Em [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]], Násser lista os usos:

- **Mudança de estado:** o botão no hover "vai ficar ou mais escuro ou mais claro" sem sair da paleta ([[wiki/concepts/feedback-do-sistema]]).
- **Hierarquia** e **paleta monocromática**, que depende de contraste entre claro e escuro do mesmo matiz.
- **Fundos e ilustrações** no mesmo matiz deixam o ambiente "mais harmonizado".
- **Neutros tingidos:** um pouco da cor de base no preto e no branco. O preto do Facebook "tem um pingo de azul" ([[wiki/entities/meta]]). Ver [[wiki/concepts/neutros-tingidos]].

## A regra no HSB

| Direção | Brilho (B) | Saturação (S) | Matiz (H) |
|---|---|---|---|
| Mais claro | aumenta | diminui | opcional: girar para um matiz mais luminoso |
| Mais escuro | diminui | aumenta | opcional: girar para um matiz menos luminoso |

O slide chama isso de "variação diagonal": S e B andam em sentidos opostos. Mexer só no brilho "acontece", mas o resultado fica pior. Girar a matiz depende do [[wiki/concepts/luminosidade-das-cores|padrão de luminosidade]], e o autor não recomenda: "sem mudar a matiz, já é sucesso" ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]).

## Os números da aula prática

A receita em [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]], partindo de uma base com B78:

| Direção | Brilho | Saturação | Exemplo da aula (base B78) |
|---|---|---|---|
| Mais escuro | −10 a 15 pontos | sobe, "não necessariamente na mesma proporção" | B62; depois B50 com S67–68 |
| Mais claro | sobe | cerca de −10 pontos | B90; depois B96–97 com S30 |
| Neutros | passos de ~3 | ±1 por passo | branco 98 → 95 → 92; 99/S3, 100/S2 |

## Por que mexer nos dois

Só baixar o brilho dá um tom "próximo" demais, quase imperceptível; baixar o brilho e subir a saturação "fica mais natural" e mais distinto. No branco, os passos são menores porque "qualquer mudança no branco, a diferença é bem mais acentuada" ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]], [[wiki/concepts/neutros-tingidos]]).

`[external]` No HSB, misturar com branco já baixa S e sobe B; misturar com preto baixa só B. Subir a saturação no escuro é escolha para evitar tons "sujos", a mesma receita de guias como Refactoring UI e o "Color in UI Design" de Erik Kennedy.

## Ferramentas

- Ferramentas geram a escala a partir de uma cor. Násser usa poucos passos ("4 e 4", ou "3, 2"), com rotação de matiz perto de 0 ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]).
- Na aula prática, a escala manual foi posta ao lado da gerada por uma ferramenta (não nomeada, de uma aula anterior) e ficou "muito próxima". O processo manual ensina o conceito; a ferramenta acelera. "Isso tudo galera é muito, muito, muito de um teste" ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]).

## Sombras

Sombras não devem ser pretas: sobre fundo colorido, a sombra é a mesma cor mais escura (artigo citado em [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]). Ver também a sombra de hover na cor do botão em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]].

## Olhar de dev

`[skill: ux-ui-mentor]` Escala de primitivos (50–950, ou `purple-100…900`) separada de tokens semânticos (`color-brand-hover`, `color-surface`). Em **OKLCH**, mudar só o L dá passos de brilho perceptualmente iguais entre matizes, o que a receita em HSB não garante e o que resolve no espaço de cor o que a aula faz girando matiz.

## Na aula de variáveis do Sass

Em [[wiki/sources/frontpush-variaveis-sass]]: "esse aqui está na mesma matiz, é variação de cor, mas aqui eu estou modificando a matiz". Variáveis evitam que a cor "derive" pelo projeto.

## Variações no Figma × no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-funcoes-sass]]: `darken`/`lighten` existem, mas "eu não preciso muito disso, porque, quando eu faço a variação de cores aqui no Figma, a gente já faz a versão mais escura, a versão mais clara, então eu passo como variável no próprio Sass". `[external]` `darken(x, 50%)` tira 50 pontos absolutos de luminosidade; `color.scale` é proporcional.

## Key Sources

- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — usos, regra brilho x saturação, girar o Hue, ferramenta geradora, sombra na cor do fundo
- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — números da receita (base B78), neutros em passos de 3, conferência com ferramenta
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — sombra de hover na cor do botão
- [[wiki/sources/frontpush-variaveis-sass]]: variação × matiz diferente
- [[wiki/sources/frontpush-funcoes-sass]]: variações vêm do Figma; `darken`/`lighten` quase não usados
