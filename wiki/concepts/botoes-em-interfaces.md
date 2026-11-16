---
type: concept
title: "Botões em interfaces"
aliases: ["botões", "botões e links", "button", "botão primário", "botão secundário", "primary button", "secondary button", "CTA"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 5
tags: [ui, ui-design, botoes, links, hierarquia-visual, consistencia, acessibilidade, design-system]
skill: ux-ui-mentor
status: stub
---

# Botões em interfaces

Elemento interativo que **guia o usuário na jornada**: leva de um ponto A a um ponto B e mostra os principais caminhos, funcionalidades e ações da interface, ou a finalidade de um formulário ("cadastre-se") ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). É um dos [[wiki/concepts/elementos-da-interface]]; "link é diferente de botão" ([[wiki/sources/elementos-da-interface-introducao-ui-design]]).

## O botão nasce do objetivo

Primeiro vem o [[wiki/concepts/objetivo-da-interface|objetivo]], depois o botão. No [[wiki/entities/frontpush]], o aluno quer a grade (botão "grade do curso") e o dono quer a inscrição ("inscreva-se"). No [[wiki/entities/sketch]], preço ("See pricing") e teste ("tente de graça"). Na [[wiki/entities/apple]], o botão está onde ela quer que se veja o preço ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).

## Primário e secundário

- **Primário:** preenchido, na cor de [[wiki/concepts/contraste]] da paleta; o "ímã" da tela.
- **Secundário:** "vazio, entre aspas, sem background" (só borda).
- A diferença cria [[wiki/concepts/hierarquia-visual]] entre ações. "Cinco tipos de botão [...] nunca é uma decisão legal" ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).
- `[skill: ux-ui-mentor]` Design systems costumam ter primary, secondary, ghost e destructive, com no máximo um primary por seção. Estados: default, hover, focus, active, disabled, loading.

## Anatomia

| Parte | Regra da aula |
|---|---|
| Altura | Fixa; mínimo de 44 px (ele usa 56). Ver [[wiki/concepts/area-clicavel]] |
| Largura | Varia com o texto |
| Padding | Igual em todos, tirado da [[wiki/concepts/escala-de-espacamento]] |
| Radius | O mesmo em todos ([[wiki/concepts/border-radius]]; 16 px no slide) |
| Label | Curto e objetivo; nunca "clique aqui para ir para tal seção" |
| Fundo | Cor de contraste da paleta |
| Hover | Cresce, ganha sombra da cor do botão ou muda a opacidade ([[wiki/concepts/feedback-do-sistema]]) |

## Consistência

"Escolheu um botão para sua interface, utilize o mesmo botão do mesmo jeito durante toda a sua interface" ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). Ver [[wiki/concepts/consistencia-visual]].

## Olhar de dev

`[skill: ux-ui-mentor]` `<button>` para ação, `<a href>` para navegação. A anatomia vira tokens (altura, padding, radius, cor, sombra) e um componente com variantes (`variant="primary" | "secondary"`). Hover pede par: focus visível para teclado e active para toque.

## Formas

A forma do botão comunica: retangular (seriedade), arredondado (amigável, "coringa"), circular (cativante, aproxima), chanfrado (futurista), diagonal (movimento) e hexagonal (gamificado). Catálogo em [[wiki/concepts/formas-de-botoes]] ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]).

## Na prática no Figma

Na aula prática ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]): altura de 56 px, padding lateral de 64 (depois 96) medido à mão, fundo com o gradiente da marca, texto branco ou preto pela legibilidade (preto no amarelo), radius 16 e texto 16. O hover é uma [[wiki/concepts/sombra-em-interfaces|sombra]] suave na cor da marca: offset para baixo, blur igual ou o dobro, no máximo 40% de opacidade, spread negativo para cobrir cerca de 80% do elemento. "No CSS é muito fácil", porque o padding acompanha o conteúdo.

## No style guide

Documentar o estado normal, o hover (sombra ou crescer) e "como é que vai ser a transição entre esses dois estados" ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). `[skill: ux-ui-mentor]` Faltam focus visível, active, disabled e loading. Ver [[wiki/concepts/style-guide]].

## Documentar o padding, não a largura

Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: no botão, "esse tipo de dimensão é importante", mas "não necessariamente eu preciso estabelecer o tamanho fixo total, porque depende do conteúdo do texto". O [[wiki/concepts/style-guide]] registra o padding (48 px de cada lado no exemplo). Ver [[wiki/concepts/handoff-design-dev]].

## Primary button no hero de cadastro

No catálogo de wireframes Hero, a variante de cadastro leva um primary button ao lado do campo, para "cadastrar ou simplesmente informar"; o protótipo do FrontPUSH já tinha "os botões de quero me inscrever" ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]).

## CTA no começo e no fim da página

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], o hero leva "botões com call to action" e a página fecha com a mesma chamada ("solicitar proposta", "get in touch"), porque ela "é o objetivo principal do seu site". Ver [[wiki/concepts/page-map]].

## No esboço e no wireframe

No papel, o botão é "um quadradinho qualquer" que simboliza o call to action; o tamanho "dá para você se preocupar também em wireframes", e cada decisão de botão e comportamento fecha no protótipo final ([[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]]). Ver [[wiki/concepts/fidelidade-de-prototipo]].

## Guiar pela cor complementar

Na aula de harmonia das cores, guiar o usuário "para a jornada que ele tem que prosseguir" também se faz com cor: "utilizar as cores complementares como guia, para poder a gente destacar elementos" ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). Ver [[wiki/concepts/harmonia-de-cores]].

## Key Sources

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — aula teórica de botões e links (edição "W7")
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — "link é diferente de botão"
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — botão preenchido acima do vazio
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — formas: reto, arredondado, circular, chanfrado, diagonal, hexagonal
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — aula prática no Figma: 56 px, padding 64/96, gradiente, sombra suave de hover
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — estados normal e hover e a transição no style guide
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]] — documentar o padding (48 px) em vez da largura fixa
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — primary button no wireframe de cadastro; "quero me inscrever"
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — CTA no hero e repetido no fim do portfólio
- [[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]] — botão como quadradinho no papel, decidido no protótipo final
- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — complementar como guia da jornada
