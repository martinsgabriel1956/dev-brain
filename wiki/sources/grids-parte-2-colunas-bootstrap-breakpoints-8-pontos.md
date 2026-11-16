---
type: source
title: "Grids, parte 2 (edição \"W7\"): colunas do Bootstrap, breakpoints e a regra dos oito pontos"
aliases: ["grids pt.2", "aula de grids parte 2", "grid por dispositivo", "width columns gutter max-width", "regra dos oito pontos"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, grid, grid-de-colunas, grid-de-8-pontos, breakpoints, responsividade, resolucao, bootstrap, figma, consistencia]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Grids, parte 2 (edição "W7"): colunas do Bootstrap, breakpoints e a regra dos oito pontos

## TL;DR

A parte técnica da aula de grids (cerca de 17 min, sem prática). Ele apresenta dois sistemas: o **grid de colunas "baseado no Bootstrap Grid System"** ([[wiki/entities/twitter-bootstrap]]), que é o que ele usa, e o **grid de 8 pontos**, que ele associa a Android e iOS. Para o primeiro, define quatro variáveis: **width** (largura da coluna), **columns**, **gutter** (o espaço entre colunas) e **max-width** (a largura total de ponta a ponta). Depois dá os valores por dispositivo ([[wiki/concepts/grid-de-colunas]]):

| | Colunas | Width | Gutter | max-width |
|---|---|---|---|---|
| Desktop | 12 | 72–96 | 24–36 | 1200–1440 |
| Tablet | 6 | 72–96 | 24–36 | 620–720 |
| Mobile | 4 (6 em paisagem) | 56–72 | 24–36 | 320–396 |

São 12 colunas porque 12 divide por 2, 3, 4 e 6: "quando fica oito de um lado, eu sei que sobra quatro do outro". Ele confere as faixas na calculadora: 72 × 12 + 24 × 11 = 1.128, perto de 1.200. O tablet é o desktop "dividido por 2". Os **breakpoints** do slide são <576 (smartphones), 720 (tablets), 960 (notebooks) e 1200 (PCs e desktops); ver [[wiki/concepts/breakpoint]]. Ele lembra que **resolução não é tamanho de tela** (iMac de 27" com Retina 5K) e que 1600 serve para TV, mas que **teto de 1440** resolve a maioria dos projetos ([[wiki/concepts/design-responsivo]]). Fecha com a **regra dos oito pontos** ([[wiki/concepts/grid-de-8-pontos]]): 8, 16, 24... 64 e depois 72, 96, 112... 288, com intermediários como 12, 18 e 36. O mesmo jogo de números vale para espaçamento, tipografia, colunas e tamanhos, o que dá [[wiki/concepts/consistencia-visual|consistência]]: "quando eu chuto algum valor, é algum desses".

## Key Claims

### Escopo e ligação com a parte 1

- **A parte 1 é pré-requisito:** responsividade e "a diferença do fixo, do fluido, do adaptativo, do responsivo, que o responsivo engloba esses outros". A parte 1 não está na wiki.
- **Grids servem a [[wiki/concepts/wireframe|wireframes]]:** alinhamento, consistência e organização "quando a gente está projetando e fazendo os protótipos de média fidelidade ou até baixa fidelidade". "Os módulos e os tópicos se misturam muito."
- **Plugins de grid prometidos**, mas não aparecem nesta aula. "Nas próximas aulas a gente vai estar aplicando tudo isso."

### Dois sistemas

- **Bootstrap (colunas):** "muitíssimo utilizado hoje em dia", "é o que eu utilizo". Ver [[wiki/entities/twitter-bootstrap]].
- **8 pontos:** "eu também utilizo para poder projetar, por exemplo, em apps como Android e iOS". "O Android e o iOS diferem um pouquinho, mas é uma boa regra para todos."
- **Não são os únicos:** "existem outras variações", mas são os que passam "a essência do que é o grid de forma melhor".

### As quatro variáveis

- **No Bootstrap, grid é coluna**, em número diferente por dispositivo, "justamente para a gente conseguir essa adaptação, essa responsividade".
- **width** é a largura da coluna, **columns** são as colunas, **gutter** "é o espacinho entre as colunas", **max-width** é "a largura total, desde uma ponta até outra". "Eu vou mexendo nessas variáveis de forma a conseguir contemplar as resoluções dos dispositivos."

### Por que 12 colunas

- **Padrão do desktop:** há sites com 15 ou mais, mas 12 "é um bom padrão para você estar se guiando, pelo menos no começo".
- **Divisibilidade:** "12 e dividir por três, dá quatro", "por quatro, dá três", "por seis, dá dois". Elementos de 3, 4 e 8 colunas cabem juntos: "quando fica oito de um lado, eu sei que sobra quatro do outro".
- **Design fluido:** no [[wiki/entities/frontpush|FrontPUSH]], "blocos de informações que estão na horizontal e que vão ter que quebrar na vertical". "Essa é a técnica do design fluido." Ver [[wiki/concepts/design-responsivo]].
- **Post no Instagram** sobre grid em interfaces web: nomenclaturas e vantagens "para o usuário, para o design e para o desenvolvedor".

### Desktop e tablet

- **Coluna de 72 a 96, gutter de 24 a 36.** "Geralmente eu utilizo 72." Coluna e gutter maiores para max-width de 1440, "aqueles desktop muito grandes para poder colocar em um Mac que tem resoluções de 2K".
- **Contas:** 72 × 12 = 864; 24 × 11 = 264 ("12 menos 1" gutters); total 1.128, "próximo do max-width de 1.200". No outro extremo, 96 × 12 + 36 × 11 = 1.548, "próximo desse máximo aqui".
- **O que ele usa:** "a maioria das vezes eu coloco 72 de width e 36 ou então 32 de gutter".
- **Tablet:** 6 colunas, coluna e gutter quase iguais aos do desktop, max-width dividido por 2: 1.200 → 600, 1.440 → 720.
- **Fazer as contas:** "sempre fazer as contas para ver se você não está errando ou se eu mesmo errei". "São padrões que eu também fui descobrindo."

### Mobile

- **4 colunas em pé, 6 em paisagem**; coluna de 56 a 72; max-width de 320 ("uma das menores telas que tem") a 396.
- **Contas:** 56 × 4 + 24 × 3 = 296 ("peguei as duas menores"); com gutter de 36, 56 × 4 + 36 × 3 = 332, "lá no meio aqui ficaria legal esse grid".
- **São chutes:** "isso aqui são chutes, são padrões"; "não se surpreenda se tiver números acima desses aqui". "O que importa é você entender a essência do negócio."
- **Três ou duas colunas?** Ele já viu grids de celular com três; prefere quatro ou seis. Com duas "eu acho meio ruim"; "quando tem mais subdivisões eu acho melhor de projetar".

### Breakpoints e resolução

- **Faixas (slide):** small <576 (smartphones), medium 720 (tablets), large 960 (notebooks, "telas de 15 polegadas"), extra-large 1200 (PCs e desktops; na fala, "compreende até 1440"). Ver [[wiki/concepts/breakpoint]].
- **"Muita coisa se deve à resolução, não só a tamanho de tela":** monitores de 24 a 26 polegadas em Full HD. O recomendado é "a resolução acompanhar o tamanho da tela". O iMac de 27 polegadas da [[wiki/entities/apple]] tem "tela Retina 5K"; "o mínimo é 2K" nesses monitores.
- **Telas grandes:** 1440 fica "entre 1200 e 1600"; 1600 "é muito colocado para televisores". "Colocando como teto o desktop a 1440, acredito que vai satisfazer."

### A regra dos oito pontos

- **Somar de 8 em 8, "mas não só isso, vai somando múltiplos":** "não necessariamente escalas lineais sejam boas, às vezes é legal escalas geométricas", com "variação pequena em tamanhos pequenos" e variações maiores em tamanhos maiores. Ver [[wiki/concepts/escala-de-espacamento]].
- **Ilustração do slide:** linha de cima 8, 16, 24, 32, 40, 48, 56, 64, com intermediários 12, 18, 36, 52. Linha de baixo 72, 88, 96, 104, 112, 120, 136, 144, 288.
- **No [[wiki/entities/figma]]:** Preferences, Nudge Amount, Big Nudge de 8: "quando você segura Shift, ele vai dando espaços de oito pontos".
- **Na tipografia:** o menu de tamanhos (14, 18, 24, 36, 48) "é muito próximo da regra dos oito pontos". 36 fica fora (32 + 8 = 40), mas "se você não quiser nem o 32 e nem o 40, você pode usar o 36". Ver [[wiki/concepts/tipografia]].
- **Consistência por hábito:** "é muito difícil eu vou colocar [...] 55 pixels, [...] 53". "Sempre quando eu penso em algum valor, eu já penso nesses valores aqui", "e aí eu criei consistência no meu design". Ver [[wiki/concepts/consistencia-visual]].
- **Também nas colunas:** "72 vai para o 96"; ele já viu Android com 88, 96 e 104; dá para usar 112, 120, 136, 144, 288. Os mesmos valores servem a grids, espaçamentos, tipografia e tamanho de objeto.

## Entities

- [[wiki/entities/nasser]]: autor (inferido: pasta FrontPush do curso, logo "W7" no slide, "um post meu" e "meu post do Instagram", como nas outras aulas da edição; a aula de espaçamento prática dele já usava 72 + gutter 32 e o big nudge de 8).
- [[wiki/entities/twitter-bootstrap]]: "Baseado no Bootstrap Grid System" (slide).
- [[wiki/entities/figma]]: Nudge Amount e Big Nudge; menu de tamanhos de texto.
- [[wiki/entities/apple]]: iMac de 27" com Retina 5K como exemplo de resolução acompanhando o tamanho.
- [[wiki/entities/frontpush]]: blocos horizontais que quebram na vertical.
- Sem página própria: Android, iOS (citados como usuários do grid de 8 pontos).

## Concepts

- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/grid-de-8-pontos]]
- [[wiki/concepts/breakpoint]] (novo)
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/escala-de-espacamento]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/wireframe]]
- [[wiki/concepts/tipografia]]

## Tensões com a wiki

- **Breakpoints do slide x Bootstrap.** `[external]` No Bootstrap 5, os breakpoints são 576, 768, 992, 1200 e 1400, e os containers têm max-width de 540, 720, 960, 1140 e 1320 (https://getbootstrap.com/docs/5.3/layout/breakpoints/ e https://getbootstrap.com/docs/5.3/layout/containers/). O 576 e o 1200 do slide batem com breakpoints; o 720 e o 960 batem com **larguras de container**, não com breakpoints. O slide parece misturar as duas tabelas. Confiança alta na tabela do Bootstrap; a mistura é inferência.
- **Coluna fixa x coluna fluida.** `[external]` No Bootstrap, a coluna é porcentagem do container e o gutter padrão é 1.5rem (24 px) (https://getbootstrap.com/docs/5.3/layout/gutters/). Width de 72 a 96 é convenção de projeto no Figma, não do framework. No código, a coluna cresce e encolhe; só o max-width trava.
- **1.548 passa do teto.** Com 96 e 36, o total (1.548) é maior que o max-width de 1.440 que ele mesmo dá; "próximo desse máximo" só vale de longe. Com 72 e 36, dá 1.260; com 72 e 32, 1.216 (a configuração de [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]). Contas do agente.
- **Mobile: 296 fica abaixo de 320.** A combinação mínima (56 e 24) não chega ao menor max-width. O teto bate exatamente: 72 × 4 + 36 × 3 = 396. Contas do agente.
- **Tablet: 6 colunas x skill.** `[skill: ux-ui-mentor]` A tabela da skill dá 8 colunas no tablet e gutter de 16 no mobile; a aula usa 6 e 24–36. Os breakpoints da skill também são outros (480, 768, 1024, 1280, 1536), e a regra dela é pôr o breakpoint "quando o conteúdo pede, não para cobrir todos os devices". Ver [[wiki/concepts/breakpoint]].
- **Geométrica, mas a lista é linear.** Ele defende a escala geométrica e ilustra com 8, 16, 24... 64, que é linear (passo 8). A segunda linha (72 → 96 → ... → 288) cresce mais rápido. A mesma tensão está em [[wiki/concepts/escala-de-espacamento]].
- **Tamanhos de texto fora da regra.** 14 e 18 não são múltiplos de 8; com o sub-grid de 4 da skill, 36 e 52 entram, mas 14 e 18 não.
- **"Android e iOS utilizam" o grid de 8.** `[external]` O Material 3 mede espaçamento em incrementos de 4 dp (https://m3.material.io/foundations/layout/understanding-layout/spacing). A Apple não fixa uma escala de 8 nas HIG. "Diferem um pouquinho" é o que se sustenta.

## Open Questions

- **Parte 1 da aula de grids** (fixo, fluido, adaptativo, responsivo; "as variáveis"): citada, não ingerida.
- **"[medium,]"**: a legenda pula a faixa medium ("que são os smartphones, que são os tablets"); inserida a partir do slide.
- **"Ou então de 3 polegadas"**: provavelmente 13 polegadas (notebook). Mantido literal.
- **"Então sete sim"**, **"eu deixo de conhecer outros sistemas"**, **"a gente se ative"**: mantidos literais; ambíguos.
- **Plugins de grid**: prometidos, não mostrados.
- **Post do Instagram** sobre grid em interfaces web: não consultado.
- `date_published` vazio.

## Raw Quotes

> "Quando fica oito de um lado, eu sei que sobra quatro do outro."

> "Isso aqui são chutes, são padrões."

> "Quando eu chuto algum valor é algum desses."

## Ver também

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: 12 colunas de 72 + gutter 32 e big nudge de 8 na prática
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]: escala linear x geométrica
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]: o grid de 8 como escala de consistência
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: grid em escala de ícone
