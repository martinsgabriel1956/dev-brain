---
type: concept
title: "Tipografia"
aliases: ["fonte", "módulo de tipografia", "typeface", "serifa", "sem serifa", "sans-serif", "escala tipográfica"]
date_created: 2026-11-13
date_updated: 2026-11-16
source_count: 23
tags: [ui, ui-design, tipografia, fonte, serifa, elementos-da-interface]
skill: ux-ui-mentor
status: draft
---

# Tipografia

Um dos [[wiki/concepts/elementos-da-interface]]; o curso de [[wiki/entities/nasser|Násser]] promete um módulo próprio por ser "tão denso". A wiki tem o papel da tipografia na [[wiki/concepts/harmonia-visual|harmonia]] com as formas e, do módulo próprio, a aula de [[wiki/concepts/altura-de-linha|altura de linha]] e [[wiki/concepts/largura-do-texto|largura do texto]].

## Tipografia comunica

Na aula de formas ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]):

- **Amigável:** fonte neutra e arredondada; a Poppins "pode encaixar muito bem". Pampers e Lego usam letras redondas.
- **Meio-termo:** a Saira do [[wiki/entities/frontpush]], quadrada com traços retos e arredondados.
- **Exato:** sites de arquitetura com fontes serifadas, "fontes de leitura, que tem um tracinho a mais"; a sem serifa é "um pouco mais genérica".

A tipografia "harmoniza com as formas, harmoniza com as cores". Ver [[wiki/concepts/formas-geometricas-e-organicas]].

`[skill: ux-ui-mentor]` A skill trata pares serif e sans-serif (por exemplo Noto Serif com Inter, DM Serif Display com DM Sans) como escolha de sensação, e põe a família tipográfica em token (`--font-family-heading`) ao lado do raio de borda.

## Mesma fonte, mensagem diferente

O [[wiki/entities/creatorpush]] usa a mesma fonte do FrontPUSH, mantida "mais por correria", e fica mais amigável só por arredondar elementos, cards e ícones ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]). Caso único, mas sugere que forma pode pesar tanto quanto a fonte na predominância.

## Contraste do título além da cor

Na parte 3 das aulas de imagens, o link do [[wiki/entities/who-can-use]] fica na seção de tipografia do Notion do curso; para título, peso tipográfico e tamanho maiores são "outros mecanismos" de contraste ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]).

## "90% da web"

"Tipografia compõe 90% da web, praticamente tudo é texto": por isso a hierarquia textual pesa tanto, sobretudo em sites de notícia como o G1 ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). `[external]` A ideia ecoa "Web Design is 95% Typography" (Oliver Reichenstein, iA, 2006): https://ia.net/topics/the-web-is-all-about-typography-period. É argumento, não medição.

## Line-height engana a medição

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]], o Alt do [[wiki/entities/figma]] mostra 17 entre título e descrição porque a caixa de texto inclui o espaço do line-height; "muito cuidado ao aplicar essa distância em textos". O tema fica para a aula de tipografia.

## Serifa, sem serifa e letra de mão

Na versão "W7" da aula de formas ([[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]): sem serifa é "mais reta, mais simples"; serifada tem "detalhezinhos a mais, mais curvas". O Madero usa sem serifa, "mais limpa", como contraste geométrico à foto de comida; o Coco Bambu usa uma letra cursiva, como se escrita à mão, para reforçar o slogan "mais perto de você"; um site de arquitetura usa serifa "para contrastar" com formas regulares. `[external]` Tecnicamente serifa é o traço no fim das hastes; cursiva (script) é outra categoria, que a aula junta com a serifada.

## Serifa no logo, sem serifa no resto

Em [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]], "a tipografia do Madero é com serifa" e o restante do site usa "uma tipografia um pouco mais limpa", sem serifa. O site de arquitetura usa letras sem serifa "buscando o minimalismo", com mais espaçamento entre letras no título. Na aula de formas "W7" o mesmo site de arquitetura aparecia com serifa: ver Tensões da fonte.

## Tamanho de texto no botão

O botão usa texto de 16, "meio que esquematizado"; os padrões de tamanho de texto ficam para a seção de tipografia e para o style guide ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]). A escolha entre texto branco e preto no botão também é adiada para tipografia.

## Tipografia no style guide

O [[wiki/concepts/style-guide]] traz "tipografia no desktop, tipografia no mobile, para poder garantir acessibilidade e legibilidade" ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]).

## Tipografia no style guide

O style guide define títulos e corpo (h1, h2, h3, h4, p, span) para desktop e mobile, e o que muda de tamanho e peso no responsivo. No style guide do [[wiki/entities/nubank]], 48, 36, 24; no que ele mostra, os tamanhos ainda estão iguais ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). `[skill: ux-ui-mentor]` Esses tamanhos viram tokens de size (xs a 3xl), weight e line-height. Ver [[wiki/concepts/design-tokens]].

## Estilos de texto

Os headings viram text styles (`Heads / H1`, `H2`), com grupos desktop e mobile. No exemplo: Sora 48, 36 e 24, pesos 600, 400, 400 e line-height 110 em todos, "um peso [...] um pouco maior nas fontes maiores". Ele chama 600 de "medium"; no CSS, medium é 500 `[skill: ux-ui-mentor]` ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]). Ver [[wiki/concepts/estilos-no-figma]].

## Tamanhos de texto e a regra dos oito

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]: o menu de tamanhos do Figma (14, 18, 24, 36, 48) "é muito próximo da regra dos oito pontos". 36 fica fora (32 + 8 = 40), mas é válido quando nem 32 nem 40 servem. Ver [[wiki/concepts/grid-de-8-pontos]].

## Tipografia e cor em sites de notícia

Em plataformas de notícia, "basicamente é texto" e "a tipografia é muito, muito trabalhada": títulos maiores com mais contraste, informação secundária com contraste menor. Com o mesmo peso tipográfico, só a cor separa os níveis ([[wiki/concepts/hierarquia-visual]]; [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]).

## Cor no texto: variação monocromática

A hierarquia textual também se faz com tons da mesma matiz: maior contraste destaca, menor fica em segundo plano ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]). Ver [[wiki/concepts/hierarquia-visual]].

## Tipografia e cores

Aula 06 do módulo de tipografia do FrontPUSH ([[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]]): o objetivo da tipografia é acessibilidade, "tem que ter contraste". A hierarquia textual sai de escala, peso (bold acima da fininha), caixa alta e, com cor, da escala de cinza. A cor também informa ([[wiki/concepts/cor-semantica]]). Para texto de botão que não passa, aumentar peso e escala antes de inverter as cores. Ver [[wiki/concepts/razao-de-contraste]].

## Panorama do módulo (aula de abertura "W7")

A aula de abertura do módulo ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]) define tipografia como "a maneira correta e melhor possível da gente dispor o texto para o usuário"; o slide traz a etimologia (grego *typos*, "forma", e *graphein*, "escrita"). O roteiro:

- **Variáveis tipográficas:** [[wiki/concepts/escala-tipografica|escala]], [[wiki/concepts/altura-de-linha|altura de linha]] e [[wiki/concepts/largura-do-texto|largura de texto]]; alinhamento (esquerda ou centro na web, justificado raro), [[wiki/concepts/kerning|tracking e kerning]]; negrito, itálico, versalete e maiúscula; cores; identidade.
- **[[wiki/concepts/classificacao-tipografica|Classificações]]:** serifadas, sem serifas, serifas grossas, script, blackletter, display.
- **Tipografia no CSS:** [[wiki/entities/google-fonts]] e Adobe Fonts, `<link>` em vez de `@import`, `font-family`. Ver [[wiki/concepts/webfonts]].

Ferramenta: a extensão WhatFont, que mostra família, peso, tamanho e altura de linha de qualquer texto. Slide: maiúsculas passam "imponente, grandioso, elegante, épico, sóbrio"; minúsculas, "amigável, próximo, simpático, descontraído, jovem". O módulo também alimenta identidade visual e guia de estilo.

## Escala e tamanho

Na aula de escala ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]): seguir uma [[wiki/concepts/escala-tipografica|escala]] por consistência; primeira preocupação é [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade e leiturabilidade]]; corpo de 14 a 21 px como regra geral, ajustado por tamanho versus espaço (NYT com 14 px, Framer com 32 px no corpo). Até 6 variações (h1–h6), ele usa 4. O slide esquecido da aula anterior: a placa "PARE" serifada "não combina"; maiúsculas passam imponência e elegância, minúsculas são amigáveis; em um par de fontes, a de maiúsculas tem hierarquia maior. Etimologia: *týpos* (forma) + *graphein* (escrita).

## Altura de linha e largura do texto

A aula 03 do módulo de tipografia ([[wiki/sources/altura-de-linha-e-largura-do-texto]]) trata as duas propriedades que deixam o texto "mais confortável ao ler": [[wiki/concepts/altura-de-linha]] (140% a 160% no corpo, 90% a 120% nos títulos; "quanto menor o texto, maior a altura de linha") e [[wiki/concepts/largura-do-texto]] (60 a 90 caracteres, 9 a 15 palavras por linha). Ela também fecha a pendência acima: line-height é "a caixa que circunda o texto".

## Classificações: serifa, sem serifa e o resto

A aula própria do módulo ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]) abre pelas [[wiki/concepts/classificacao-tipografica|classificações]]. Serifada (clássica, elegante, Times New Roman) e sem serifa (neutra, moderna, Helvetica e Arial) dominam a web; a sem serifa é a indicada "principalmente para corpo de texto". Serifadas grossas, script, blackletter e display ficam em títulos, anúncios e botões, por [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade]]; a monoespaçada serve a código. Script é classificação própria, o que fecha a ressalva `[external]` da seção "Serifa, sem serifa e letra de mão". Aqui serifa em site de leitura é "incomum" (exceção: [[wiki/entities/new-york-times]]), enquanto a aula de formas chamava serifadas de "fontes de leitura": tensão registrada na fonte.

## Variáveis tipográficas (aula 05)

Primeira aula do módulo de tipografia na wiki ([[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]]): negrito e itálico como [[wiki/concepts/contraste]] ([[wiki/concepts/peso-tipografico]]), [[wiki/concepts/tracking]] (distância igual entre todas as letras), [[wiki/concepts/kerning]] (distância entre um par, coisa de marca) e [[wiki/concepts/texto-em-maiusculas|maiúsculas]], que sobem a hierarquia no mesmo tamanho. De passagem: o justificado deixa distâncias de "X" e de "3, 4X" entre palavras, por isso "quase não usa". `[skill: ux-ui-mentor]` A skill também manda evitar justificado ("rios de espaço"). As aulas 03 (altura de linha e largura) e 04 (alinhamento e espaçamento) ainda não foram ingeridas.

## Escolher e combinar

A aula que fecha a parte de tipografia ([[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]]) dá o método. **Escolher:** pesquisa com quatro perguntas (qual a mensagem, o que empresas similares usam, qual o público, pago ou gratuito; ver [[wiki/concepts/licenca-de-fontes]]). Placa de pare pede sem serifa; restaurante italiano, "orgânico", tende à serifada; público mais velho pede escala e contraste maiores. **Combinar** ([[wiki/concepts/combinacao-de-fontes]]): duas typefaces, contraste visível, título "mais temático", corpo sem serifa com família ampla de pesos, consistência. O site do autor usa Ubuntu + Mukta, todos os pares sugeridos vêm do [[wiki/entities/google-fonts]], e a pesquisa por tema passa pela [[wiki/concepts/classificacao-tipografica]] (country → serifas grossas, festa alemã → blackletter).

`[external]` A regra "corpo sempre sem serifa" é princípio da aula: em telas de alta resolução não há diferença consistente de legibilidade (https://www.nngroup.com/articles/serif-vs-sans-serif-fonts-hd-screens/).

## Alinhamento e espaçamento de parágrafo

Na aula 4 do módulo de tipografia ([[wiki/sources/alinhamento-e-espacamento-de-texto]]), alinhamento e espaçamento entram como "variáveis tipográficas" ao lado de altura de linha e largura de texto (aula 3, ainda fora da wiki). Esquerda é o padrão, centralizado só em títulos e cards curtos, justificado nunca: ver [[wiki/concepts/alinhamento-de-texto]]. Parágrafos de 4 a 8 linhas, separados por um vão do tamanho do line-height: ver [[wiki/concepts/espacamento-entre-paragrafos]]. O line-height vira unidade de espaçamento, não só de entrelinha.

## Key Sources

- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — Creator Push mantém a fonte e muda a mensagem pelas formas
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — Who Can Use no módulo de tipografia; peso e tamanho como contraste
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — "tipografia compõe 90% da web"; hierarquia textual
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — caixa de texto inclui o line-height ao medir distâncias
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — serifa x sem serifa; letra de mão do Coco Bambu; sem serifa do Madero
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — Madero serifado + corpo sem serifa; arquitetura sem serifa (tensão)
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — texto de 16 no botão; padrões de tamanho adiados para tipografia
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — tipografia desktop e mobile no style guide
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — h1 a span, desktop x mobile; 48/36/24 no Nubank
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]] — text styles Heads/H1, H2; Sora 48/36/24, line-height 110; "medium" = 600 (tensão)
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — tamanhos 14/18/24/36/48 perto da regra dos oito; 36 entre 32 e 40
- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — sites de notícia: tipografia trabalhada, contraste de cor por nível
- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — tons monocromáticos para hierarquia de texto
- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — hierarquia textual por escala, peso, caixa alta e cinza; contraste como objetivo
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]] — abertura do módulo (edição "W7"): definição, variáveis, classificações, CSS
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]] — escala, 14–21 px, maiúsculas x minúsculas, h1–h6, escala do Figma + 8pt
- [[wiki/sources/altura-de-linha-e-largura-do-texto]] — altura de linha e largura do texto; primeira aula do módulo de tipografia na wiki
- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]] — classificações tipográficas; sem serifa no corpo, decorativas no título; Google Fonts e Adobe Fonts
- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — negrito, itálico, tracking, kerning, maiúsculas; estilo falso; justificado
- [[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]] — método de escolha (mensagem, similares, público, licença) e de combinação (duas typefaces, contraste, consistência)
- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — alinhamento (esquerda padrão, justificado nunca) e vão de parágrafo = line-height
- [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]: `align-items: baseline` alinha itens de tamanhos de fonte diferentes pela linha de base
