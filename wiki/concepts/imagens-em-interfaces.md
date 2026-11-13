---
type: concept
title: "Imagens em interfaces"
aliases: ["imagem em UI", "fotografia em interfaces", "imagens na interface", "imagens e ilustrações"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 7
tags: [ui, ui-design, elementos-da-interface, imagens, fotografia, ilustracoes]
skill: ux-ui-mentor
status: stub
---

# Imagens em interfaces

Um dos [[wiki/concepts/elementos-da-interface]]. A imagem chama a atenção, transmite a ideia de um produto ou serviço, expressa a linguagem visual de uma marca, informa e conta histórias. Funciona porque o ser humano é visual e a fotografia passa uma sensação "só de olhar" ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]).

## Fotografia é construída

A foto de um hambúrguer de fast-food ou o fundo clean de uma marca minimalista não são acaso: são montados para despertar algo. O mesmo vale para thumbnails, heros e propagandas, onde alta qualidade "transmite esmero".

Liga com [[wiki/concepts/formas-geometricas-e-organicas]]: a fotografia é a forma orgânica por excelência, e comida depende dela ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]).

## Diretrizes (Násser)

| Diretriz | Página |
|---|---|
| Usar bons bancos de imagens e conferir a licença | [[wiki/concepts/banco-de-imagens]] |
| Escolher o formato certo: foto → JPG, transparência → PNG, ícone/ilustração → SVG, WebP como versão otimizada | [[wiki/concepts/formato-jpeg]], [[wiki/concepts/formato-png]], [[wiki/concepts/formato-svg]], [[wiki/concepts/formato-webp]] |
| Alta resolução: pegar grande e diminuir, nunca pequeno e aumentar | esta página |
| Não distorcer: preservar o aspect ratio | [[wiki/concepts/aspect-ratio]] |
| Contraste para escrever sobre imagem: letra branca + capa de gradiente | [[wiki/concepts/texto-sobre-imagem]], [[wiki/concepts/contraste]] |
| Fotos de pessoas reais, não fake | [[wiki/concepts/fotos-de-pessoas-reais]] |
| Um ponto focal, nos cruzamentos da grade de nove blocos | [[wiki/concepts/ponto-focal-em-fotografia]] |
| Otimizar o peso, começando pelo formato adequado | [[wiki/concepts/otimizacao-de-imagens]] |

## Peso é acessibilidade

"Ser acessível também é não ser tão pesado": internet lenta e plano móvel pagam a conta de imagens grandes. `[skill: ux-ui-mentor]` A hero image costuma ser o LCP da página (bom < 2,5 s); reservar espaço com `aspect-ratio` evita CLS.

## Fotografia puxa para o orgânico

Num site de fotógrafo, a fotografia é inevitável e "automaticamente vai elencar a realidade": sozinha, já leva a interface para o lado orgânico. Nos próprios projetos, Násser prefere ilustração vetorial "porque gosta de otimização" ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]).

## Bom senso e padronização

Na parte 3 ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]): a imagem "precisa acompanhar o entendimento e aquilo que é passado ao lado dela", para ambientar ou para complementar uma ação (biometria, app em língua desconhecida). Imagens que vão de ponta a ponta pedem banco em alta resolução (até 4K) e todas no mesmo [[wiki/concepts/aspect-ratio]]. Para compor imagens no próprio Figma, [[wiki/concepts/blend-modes]].

## Ilustrações

Na parte 4 ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]), o bloco fecha com ilustrações: SVG, uma família de traço único, cores da marca e mascotes no onboarding. "Muitos dos conceitos que eu falei para imagens se aplicam também a ilustrações." Ver [[wiki/concepts/ilustracoes-em-interfaces]]. Também pede [[wiki/concepts/texto-alternativo]] em toda imagem e recomenda as diretrizes do [[wiki/entities/material-design]].

## Precisa de um porquê

Na edição "W7", [[wiki/entities/nasser|Násser]] resume a regra: "você não pode pegar uma imagem e jogar ela na interface sem ter um porquê". O erro típico é espalhar foto genérica de "pessoas conversando" achada no Google; isso "está se tornando brega" e não traduz a essência da instituição ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — aula de imagens (parte 1): bancos, formatos, resolução, otimização
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — fotografia leva a interface para o orgânico; preferência por ilustração vetorial
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — parte 2: formato adequado, não distorcer, fotos reais, ponto focal, texto sobre imagem
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — parte 3: bom senso, Who Can Use, padronização, blend modes
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — parte 4: ilustrações, mascotes, consistência, Material Design, alt text
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": imagem precisa de um porquê; foto genérica ficando brega
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — edição "W7": a ilustração, como a imagem, precisa de um porquê
