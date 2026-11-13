---
type: concept
title: "Família de ícones"
aliases: ["icon family", "icon set", "pacote de ícones", "biblioteca de ícones", "classificação de ícones", "ícone de linha", "ícone preenchido", "outline vs filled"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 6
tags: [ui, ui-design, icones, consistencia, identidade-visual]
skill: ux-ui-mentor
status: stub
---

# Família de ícones

Conjunto de ícones feitos com as mesmas regras (estilo, espessura de traço, cantos, grid), que parecem obra "do mesmo cara [...] com o mesmo traço". É a [[wiki/concepts/consistencia-visual]] aplicada a [[wiki/concepts/icones-em-interfaces|ícones]], igual à família de [[wiki/concepts/ilustracoes-em-interfaces|ilustrações]].

## Exemplo: Feather Icons

[[wiki/entities/feather-icons]]: todos de linha, stroke width 2, cantos arredondados em todos. `[external]` Grid de 24×24, `stroke-linecap` e `stroke-linejoin` `round` (https://github.com/feathericons/feather).

## Classificação: linha x preenchido

- **Vazado (linha, outline):** construído pela stroke. Mais sóbrio; Násser usa "muito" nos projetos dele, como o [[wiki/entities/frontpush]].
- **Preenchido (filled):** construído pelo preenchimento. Destaca mais o ícone e "dá mais cor"; combinado com cantos arredondados, fica amigável, como o [[wiki/entities/iconly]] no [[wiki/entities/creatorpush|Creator Push]].

Pacotes como o Iconly trazem várias famílias (bold, bulk, light...). Escolha uma e não misture.

## Como escolher

1. Conectada à identidade visual, à "essência daquilo que quer ser transmitido" ([[wiki/concepts/harmonia-visual]], [[wiki/concepts/formas-geometricas-e-organicas]]).
2. Usada ao longo de toda a interface.
3. Não é regra rígida: produto amigável pode usar linha.

Biblioteca própria "exige estudo, não recomendo para iniciantes".

## Estilo também é hierarquia

Na parte 2 ([[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]), o mesmo ícone do [[wiki/entities/font-awesome]] aparece preenchido, regular, light, thin e duotone (duas cores), e cada variação "pode transmitir ideias diferentes". O preenchido chama mais atenção; o de linha é "mais neutro, um pouco mais apagado". Dá para destacar um ícone de linha sem trocar de família: cor de destaque e posição. Uma vez escolhida a forma de construir, "construa o resto de todos os seus ícones seguindo essas mesmas linhas". Os ícones da família compartilham um [[wiki/concepts/grid-de-icones|grid]].

## Trazer ícones de fora para a família

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], Násser redesenha logos de terceiros (Instagram, YouTube, [[wiki/entities/github]], [[wiki/entities/hotmart]]) em traços retos para caberem na família do [[wiki/entities/frontpush]]. O custo: as marcas costumam proibir alterar o logo (ver tensões na fonte). Bibliotecas de referência: [[wiki/entities/feather-icons]], [[wiki/entities/eva-icons]]; o Noun Project tem ícones "mais trabalhados", quase ilustrações.

## No máximo duas, com papéis distintos

Na edição "W7" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]), a regra ganha um teto: "utilize só ela na sua interface, no máximo utilize duas, mas com muita consciência". A segunda família vale se for parecida ou de outra categoria: uma para funções, outra "um pouco mais complexa que tenha cores ou [...] preenchimento maior" para destacar módulos. Packs gratuitos citados: [[wiki/entities/feather-icons]], [[wiki/entities/eva-icons]] e Basicons. O preenchido traz "uma noção um pouco mais realista"; o de linha é "mais simplificado" (exemplos do Flaticon).

## Duas famílias no site do autor

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]], as "duas famílias" aparecem em uso: ícones próprios, mais trabalhados e com preenchimento laranja, para os módulos; [[wiki/entities/feather-icons]] para os ícones pequenos. No meio da demo, a regra de estilo: "se for usar ícones de linhas, utilize só ícones de linhas". O arquivo do Piqo ([[wiki/entities/iconly]]) mostra a família como conjunto de estilos: bold, bulk, light, light outline, broken, two-tone.

## Key Sources

- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — família, linha x preenchido, Iconly x Feather, Creator Push x FrontPUSH
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — Feather "filho de uma mesma pessoa"; misturar com Iconify quebra a consistência
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — preenchido x linha como hierarquia; variações do Font Awesome
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — logos de terceiros redesenhados para caber na família; Eva Icons, Flaticon, Noun Project
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — "no máximo duas, com muita consciência"; Feather, Eva e Basicons gratuitos
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — duas famílias em uso (próprios + Feather); só linha ou só preenchido; estilos do Iconly
