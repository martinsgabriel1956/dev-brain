---
type: concept
title: "Espaço em Branco"
aliases: ["whitespace", "espaço negativo", "negative space", "respiro", "micro espaço", "macro espaço", "micro e macro espaço"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 8
tags: [ui, ui-design, layout, espaco-em-branco, simplicidade, hierarquia-visual, espacamento, grid-de-8-pontos]
skill: ux-ui-mentor
status: draft
---

# Espaço em Branco

Espaço vazio **entre** ou **ao redor** dos elementos, também chamado de whitespace ou espaço negativo ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). "É literalmente vazio, pode ser espaço preto": a cor não importa, importa não ter nada ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]). Ferramenta principal de [[wiki/concepts/simplicidade-visual]] e primeiro dos [[wiki/concepts/elementos-da-interface]] estudados no módulo.

## Macro espaço: foco

Na aula de whitespace, macro é o espaço ao redor de um elemento. Ele dá foco e ênfase: numa tela toda preta com uma bolinha de destaque no centro, o olhar vai direto para a bolinha ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). A aula de imagens retoma a ideia para fotos: um único [[wiki/concepts/ponto-focal-em-fotografia|ponto focal]], "assim como a gente conversou lá em white space" ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

Na home do [[wiki/entities/google]] sobram logo, barra de busca e dois botões; o resto dos produtos está atrás de "mais do Google" e dos links no canto. A chance de errar como pesquisar é "muito pequena". O site do iPhone 12 Pro abre com só a foto, o nome e uma frase, embora a página tenha uma rolagem enorme ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]).

Também cria [[wiki/concepts/hierarquia-visual]]: um elemento isolado por espaço se destaca, o mesmo efeito do [[wiki/concepts/contraste]] por cor escassa.

## Micro espaço: agrupar e separar

Micro é o espaço entre elementos. Pequeno, indica grupo; grande, indica coisas diferentes. É a [[wiki/concepts/lei-da-proximidade-gestalt]] ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]):

- **Menu de [[wiki/concepts/wireframe]]:** links Home/Sobre/Contato próximos e equidistantes formam um grupo de mesma hierarquia; vãos grandes separam logo, links e CTA. Três elementos diferentes, "somente com o espaçamento".
- **Resultados de busca do Google:** sem bordas de card, o anúncio fica junto do título por estar mais perto; um bloco recuado à esquerda é lido como parte do bloco de cima, mesmo mais distante; o mesmo recuo do principal com distância maior marca outro grupo.
- **Título, descrição e CTA:** título e descrição conectados (4 a 8 px, porque o line-height do título já dá espaço); espaço maior (40 ou 48) até o call to action, que é outra função.

## Quanto espaço: o grid de 8

Para que os vãos não sejam arbitrários, a aula usa o [[wiki/concepts/grid-de-8-pontos]]: uma escala de múltiplos de 8 (16, 32, 40, 48...) aplicada com bom senso (18, 28, 36 também valem). Liga o espaço em branco à [[wiki/concepts/consistencia-visual]].

## Dois cortes de "macro" e "micro"

A aula define pela posição: macro = ao redor (foco), micro = entre (agrupar/separar). `[skill: ux-ui-mentor]` A skill define pela escala: **macro** entre seções e blocos grandes, **micro** entre elementos, padding interno e line-height. Espaçamento relacional: 8 a 16 px entre elementos relacionados, 24 a 32 px dentro do mesmo grupo, 48 a 64 px entre grupos diferentes. Os dois cortes concordam no efeito (pouco espaço agrupa, muito espaço separa). O vão entre logo, links e CTA do próprio exemplo da aula é "entre" e age como macro, o que favorece o corte da skill. Regra prática: na dúvida, mais espaço; design de iniciante costuma ser denso demais.

## Benefícios ainda não explicados

O slide da aula de whitespace lista também pausa no conteúdo (respiro), personalidade, hierarquia e legibilidade, deixados para a parte 2.

## Ilustração no espaço vazio

Numa tela de onboarding só com texto e botão, a ilustração complementa o espaço em branco e deixa a tela "mais dinâmica" ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). Não contradiz o whitespace: o vazio a preencher é o de uma "tela grandona" sem ênfase, não o respiro entre elementos. Ver [[wiki/concepts/ilustracoes-em-interfaces]].

## Margem no ícone

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: o Material pede "um espaço, uma margenzinha, espaço em branco" dentro do frame do ícone, para ele ter um ponto focal; Násser deixa ainda mais folga que a diretriz ("eu gosto de ser clean"). Ver [[wiki/concepts/grid-de-icones]].

## Quando a linha entra

Espaço é o recurso padrão para separar. A linha aparece quando é preciso "um enfoque maior na divisão", para reforçar que são produtos ou informações diferentes ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Espaçamento interno (padding)

Na aula de espaçamento e linhas, o espaço dentro do elemento é o **padding** do CSS. Num card, afastar o conteúdo da borda deixa o design "mais clean"; o autor faz isso em todos os cards do site dele. A mesma aula diz que o tamanho do espaço depende do meio: conteúdo simples aceita espaços grandes, conteúdo denso pede espaços menores com linhas e cards ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]). Ver [[wiki/concepts/densidade-de-informacao]] e [[wiki/concepts/escala-de-espacamento]].

## Key Sources

- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — espaço em branco como ferramenta de simplicidade
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — definição, micro e macro espaço, grid de 8 pontos
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — citado como referência para ter um só ponto focal na imagem
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — ilustração preenche o vazio do onboarding
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — margem dentro do frame do ícone
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — linha como reforço quando o espaço não basta
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — padding no card; tamanho do espaço depende do meio
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — prática no Figma: vãos de 16, 32 e 128 medidos com Alt
