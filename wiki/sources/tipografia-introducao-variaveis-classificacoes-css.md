---
type: source
title: "Tipografia (edição \"W7\"): introdução ao módulo, variáveis tipográficas, classificações e CSS"
aliases: ["introdução à tipografia W7", "módulo de tipografia", "variáveis tipográficas", "panorama de tipografia"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, tipografia, escala-tipografica, line-height, largura-de-linha, kerning, tracking, alinhamento, classificacao-tipografica, google-fonts, css, hierarquia-visual, contraste, acessibilidade]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/tipografia-introducao-variaveis-classificacoes-css.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Tipografia (edição "W7"): introdução ao módulo, variáveis tipográficas, classificações e CSS

## TL;DR

Aula de abertura do módulo de [[wiki/concepts/tipografia]] da edição "W7" do curso de UI de [[wiki/entities/nasser|Násser]] (cerca de 11 min). É um panorama, não um aprofundamento: "nas próximas aulas a gente vai trabalhar cada uma dessas variáveis". Definição didática: tipografia é "a maneira correta e melhor possível da gente dispor o texto para o usuário". A justificativa é que "a maioria da web é texto" (Notion, Globo, Google, Wikipedia). Depois ele percorre o roteiro do módulo: **variáveis tipográficas** ([[wiki/concepts/escala-tipografica|escala]], [[wiki/concepts/altura-de-linha|altura de linha]], [[wiki/concepts/largura-do-texto|largura de texto]], alinhamento, [[wiki/concepts/kerning|tracking e kerning]], negrito/itálico/versalete/maiúscula, cores, identidade), **[[wiki/concepts/classificacao-tipografica|classificações]]** (serifada, sem serifa, serifa grossa, script, blackletter, display) e **tipografia no CSS** ([[wiki/entities/google-fonts]], Adobe Fonts, `<link>` x `@import`, `font-family`; ver [[wiki/concepts/webfonts]]). A ferramenta de inspeção é a extensão WhatFont no Chrome, usada sobre uma notícia da morte de Maradona.

## Key Claims

### Por que um módulo inteiro

- **Mesmo tratamento que cores:** "assim como a gente fez com cores, é um dos [[wiki/concepts/elementos-da-interface|elementos da interface]]" e, por ser tão importante e vasto, ganhou um módulo próprio.
- **O que se ganha:** conforto de leitura, agilidade para "encontrar as informações", saber "criar hierarquia e contraste", e "tornar acessível". Ver [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/contraste]].
- **Base para outros conceitos:** identidade visual ("a tipografia vai além disso a texto, ela passa muito mais informações", como na aula de [[wiki/concepts/formas-geometricas-e-organicas|formas]]) e o guia de estilo da parte web.

### "A maioria da web é texto"

- **Exemplos:** o próprio Notion do curso ("é lógico que tem ilustrações, tem banners, mas o foco principal é a informação"), "o Globo, o Google", "o Wikipedia". Vale para "tudo e qualquer interface em maior ou em menor grau, mas sempre em maior grau é texto".
- **Ilustração serve ao texto:** as ilustrações existem "para poder ilustrar o que está dizendo o texto".
- **Site de contraste no Notion:** "um outro site que eu deixei aqui no Notion, que é muito importante também para poder a gente entender um pouco sobre contraste". O nome não é dito; pelo que a aula de imagens contou, é o [[wiki/entities/who-can-use]] (inferência).

### Escala: o tamanho, com consistência

- **"Literalmente escala é o tamanho"**: que tamanho vai no título, no subtítulo, no corpo. Ver [[wiki/concepts/escala-tipografica]].
- **O erro comum é inconsistência:** textos "da mesma hierarquia" com tamanhos diferentes, e destaques em cores diferentes que não batem com o tamanho. Ver [[wiki/concepts/consistencia-visual]].
- **WhatFont:** a extensão do Chrome mostra família, estilo, peso, tamanho e altura de linha. Na notícia "Maradona morre aos 60 anos na Argentina" aparece "Open Sans Bold 400" e a pilha "Open Sans, Arial, Helvetica, Sans Serif". Essas informações "são justamente essas variáveis".

### Altura de linha

- **A caixa azul da seleção** de texto é a altura de linha, "a altura da caixa". Ela é maior que o tamanho da fonte "para poder tornar a leitura mais confortável". Ver [[wiki/concepts/altura-de-linha]].
- **Título tem entrelinha menor que corpo:** nos títulos "uma caixa sobe na outra". O porquê fica para depois.

### Largura de texto

- **Definição:** "a quantidade de palavras que tem uma linha", contando só palavras de duas letras ou mais. No exemplo da Globo dá 9. Ver [[wiki/concepts/largura-do-texto]].
- **Wikipedia como contraexemplo:** "deixa muito extenso", "muitas palavras em uma linha", "mais cansativo para ler". A Globo "se preocupa com isso": poderia esticar o texto, mas "com estudos, percebe-se que deixar assim mais curtinho [...] fica mais confortável de se ler".

### Alinhamento, tracking e kerning

- **Alinhamento:** na web o texto é quase sempre alinhado à esquerda ou centralizado; justificado e à direita são raros, "e isso tem um porquê" (adiado).
- **Kerning:** "literalmente o espaçamento entre as letras". Demonstra na ferramenta de texto e cita o logo da Tesla, "bem espaçada": é um recurso "para criar branding, para criar coisa de logo", que "traz uma ideia também por trás". Ver [[wiki/concepts/kerning]] (a definição dita é a de tracking; ver Tensões).

### Ênfase, cor e identidade

- **Quando usar** negrito, itálico, versalete e maiúscula, e como usar cor no texto ("contraste maior, com contraste menor") para criar hierarquia.
- **Identidade:** "dependendo do que eu escrevo, e como eu escrevo, com qual fonte eu escrevo, eu consigo transparecer muito na identidade sobre aquele projeto". É a ponte para as classificações.

### Classificações tipográficas

- **Seis categorias** no roteiro: "serifadas, sem serifas, serifas grossas, script, blackletter, display". Ver [[wiki/concepts/classificacao-tipografica]].
- **Onde vê-las:** [[wiki/entities/google-fonts]] e Adobe Fonts, "a principal referência que eu tenho", com os filtros serif, sans serif, display, handwriting e monospace.

### Tipografia no CSS

- **Escolher a fonte e os pesos:** no Google Fonts se escolhe a família (a Lato no exemplo) e os estilos: "light, que é a mais fininha", normal e bold; "black, bold, 700" como pesos. Ver [[wiki/concepts/webfonts]].
- **`<link>` ou `@import`:** "a gente vai discutir também qual é o melhor desses dois [...] eu já adianto que é esse link aqui, deixa mais performático o seu site".
- **`font-family`** e as demais propriedades CSS para "traduzir isso tudo para o nosso website". Ver [[wiki/concepts/css]].

## Slides (imagens anexadas pelo usuário na ingestão)

Duas telas do slide da aula, fora da transcrição:

- **Roteiro do módulo:** O que é tipografia? (a importância, maioria da web é texto, hierarquia textual); Variáveis tipográficas (escala, altura de linha e largura de texto; alinhamento, tracking e kerning; negrito, itálico, versaletes e maiúsculas; cores; identidade); Classificações tipográficas (serifadas, sem serifas, serifas grossas, script, blackletter, display); Tipografia CSS (propriedades de texto; Google Fonts e Adobe Fonts).
- **Definição e exemplo:** "A tipografia (do grego typos, 'forma', e graphein, 'escrita') é a arte e o processo de criação na composição de um texto, física ou digitalmente." Duas placas "PARE", uma em sem serifa e outra em serifada, e duas colunas: **letras maiúsculas** (imponente, grandioso, elegante, épico, sóbrio) e **letras minúsculas** (amigável, próximo, simpático, descontraído, jovem). A fala não comenta esse slide.

## Entities

- [[wiki/entities/nasser]]: autor (o aluno imaginário diz "Ah, Násser" duas vezes; logo "W7" no slide).
- [[wiki/entities/google-fonts]] (nova): principal referência para baixar fontes; filtros por classificação; `<link>` x `@import`.
- [[wiki/entities/google]]: um dos exemplos de interface que é "a maior parte texto"; o Chrome hospeda a extensão WhatFont.
- [[wiki/entities/who-can-use]]: provável "site de contraste" deixado no Notion (inferido).
- Sem página própria: WhatFont, Adobe Fonts, Notion, Globo/G1, Wikipedia, Tesla, Open Sans, Lato, Maradona.

## Concepts

- [[wiki/concepts/tipografia]]
- [[wiki/concepts/escala-tipografica]] (novo)
- [[wiki/concepts/altura-de-linha]] (novo)
- [[wiki/concepts/largura-do-texto]] (novo)
- [[wiki/concepts/kerning]] (novo)
- [[wiki/concepts/classificacao-tipografica]] (novo)
- [[wiki/concepts/webfonts]] (novo)
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/formas-geometricas-e-organicas]]
- [[wiki/concepts/css]]

## Tensões com a wiki

- **Kerning ou tracking?** A aula define kerning como "o espaçamento entre as letras" e mostra o logo espaçado da Tesla. `[external]` Na terminologia padrão, **tracking** (CSS `letter-spacing`) é o espaçamento uniforme de um trecho inteiro; **kerning** é o ajuste entre pares específicos (AV, To), que a fonte já traz e o CSS controla com `font-kerning` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-kerning; https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing). O logo da Tesla é exemplo de tracking aberto. Confiança alta. O slide lista os dois termos; as próximas aulas podem separar.
- **"Open Sans Bold 400"** é contraditório: `[external]` no CSS 400 é `normal` e bold é 700 (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). Provável leitura de dois campos do WhatFont (estilo e peso) em sequência. Mantido literal.
- **"90% da web" e "a maioria da web é texto".** Mesma tese da aula de visão geral ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). `[skill: ux-ui-mentor]` A skill atribui "~95%" a Jeffrey Zeldman; a frase conhecida é "Web Design is 95% Typography", de Oliver Reichenstein (iA, 2006), https://ia.net/topics/the-web-is-all-about-typography-period `[external]`. A atribuição da skill parece errada. Em todo caso é argumento, não medição.
- **Wikipedia já não é o contraexemplo.** `[external]` A skin Vector 2022, padrão na Wikipedia em inglês desde janeiro de 2023, limita a largura do conteúdo justamente para melhorar a leitura (https://www.mediawiki.org/wiki/Reading/Web/Desktop_Improvements). A aula é de novembro de 2020 (ver abaixo), antes da mudança.
- **Largura em palavras x caracteres.** A aula conta palavras (9 na Globo). `[skill: ux-ui-mentor]` A métrica usual é 45–75 caracteres por linha no corpo, em CSS `max-width: 65ch`; `[external]` a WCAG 1.4.8 (AAA) pede no máximo 80 caracteres (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html). Nove palavras de duas letras ou mais dão algo perto desse intervalo, mas a conta em palavras é instável.
- **Justificado raro tem razão de acessibilidade.** `[external]` A mesma WCAG 1.4.8 pede texto não justificado, porque o justificado cria "rios" de espaço que atrapalham leitores com dislexia. `[skill: ux-ui-mentor]` Também evitado em colunas estreitas no mobile.
- **Entrelinha do título menor:** `[skill: ux-ui-mentor]` confirma: título 1.1–1.2, corpo 1.5–1.6; "quanto maior o texto, menor a entrelinha". `[external]` A WCAG 1.4.12 exige que o conteúdo aguente entrelinha de 1.5 sem quebrar (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).
- **`<link>` é mais performático: correto.** `[external]` `@import` dentro de um CSS só é descoberto depois que esse CSS baixa, o que encadeia requisições; o `<link>` no `<head>` (com `preconnect`) começa antes (https://web.dev/articles/font-best-practices). A aula promete detalhar.
- **Maiúsculas imponentes, minúsculas amigáveis** (slide): mesma lógica de [[wiki/concepts/formas-geometricas-e-organicas]] (geométrico afasta, arredondado aproxima), agora no caixa da letra. Sem fonte além do slide.

## Open Questions

- **Data de gravação inferida:** "Maradona morre aos 60 anos na Argentina, notícia de hoje". `[external]` Maradona morreu em 25 de novembro de 2020; a aula foi gravada nesse dia, com confiança alta. `date_published` fica vazio porque a publicação pode ser posterior.
- **"Meu próprio master file, o Notion"**: "master file" parece o nome da página do curso. Mantido literal.
- **"As ilustrações estão aqui em os olhos"**: provavelmente "enchem os olhos". Mantido literal.
- **"O que significa serifa"** na leitura da pilha de fontes: talvez "o que significa sem serifa", explicando `sans-serif`. Mantido literal.
- **"Serifas grossas"**: provável slab serif (serifa egípcia/quadrada). A aula de classificações deve confirmar.
- **Versalete** (small caps) aparece só no roteiro; a explicação fica para depois.
- As aulas de cada variável, das classificações e do CSS ainda não foram ingeridas.

## Raw Quotes

> "Tipografia meio que colocando aqui de forma bem didática é a maneira correta e melhor possível da gente dispor o texto para o usuário."

> "As ilustrações estão aqui em os olhos, sim, mas é para poder ilustrar o que está dizendo o texto."

> "Dependendo do que eu escrevo, e como eu escrevo, com qual fonte eu escrevo, eu consigo transparecer muito na identidade sobre aquele projeto."

## Ver também

- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]: "tipografia compõe 90% da web"; hierarquia textual no G1
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: line-height engana a medição de distâncias no Figma
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]: serifa, sem serifa e letra de mão como comunicação
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]: Who Can Use na seção de tipografia do Notion
