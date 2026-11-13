---
type: source
title: "Elementos da interface: imagens e ilustrações (bancos de imagens, formatos para web, resolução e otimização)"
aliases: ["aula de imagens", "imagens e ilustrações", "imagens em UI", "formatos de imagem para web"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, imagens, ilustracoes, formatos-de-imagem, png, jpeg, svg, webp, otimizacao-de-imagens, performance, unsplash, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-formatos-bancos-otimizacao.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: imagens e ilustrações (parte 1)

## TL;DR

Aula do módulo "elementos da interface" do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]], sobre **imagens** (ilustrações ficam para depois). A tese: o ser humano é visual e a fotografia comunica rápido, por isso [[wiki/concepts/imagens-em-interfaces|a imagem]] chama atenção, transmite a ideia de um produto, expressa a linguagem visual da marca, informa e conta histórias; uma foto de hambúrguer ou um thumbnail são construídos para despertar algo. A aula cobre quatro blocos: (1) [[wiki/concepts/banco-de-imagens|bancos de imagens]], com o [[wiki/entities/unsplash]] como favorito por ser livre de uso, e o aviso de sempre conferir a licença; (2) **formatos para web**: [[wiki/concepts/formato-png|PNG]] para imagens com transparência que não dá para vetorizar, [[wiki/concepts/formato-jpeg|JPG]] para toda fotografia realista (mais leve), [[wiki/concepts/formato-svg|SVG]] para ícones, ilustrações e backgrounds (escalável e pesa bytes) e [[wiki/concepts/formato-webp|WebP]] como formato mais novo e mais otimizado; (3) **alta qualidade e alta resolução**: melhor pegar grande e diminuir do que pegar pequeno e aumentar; (4) [[wiki/concepts/otimizacao-de-imagens]]: exportar no [[wiki/entities/figma]] em vários tamanhos por dispositivo (2x/1x desktop, 0,5x/0,3x mobile) e comprimir no TinyImage, que pode cortar até 80% do peso. O argumento de fundo é de acessibilidade: imagem pesada prejudica quem tem internet lenta ou plano móvel.

## Key Claims

### Por que imagem

- **A imagem é ótima para chamar atenção, transmitir ideias de produto ou serviço, expressar a linguagem visual de uma marca, informar e contar histórias** (slide e fala).
- **O ser humano é uma criatura visual; a fotografia transmite sensação ou ideia "só de olhar".** Exemplos: a empresa de culto minimalista mostra fundo clean, fotos bem tiradas e escala de cores controlada; o hambúrguer do McDonald's ou do Burger King é "construído" para despertar algo. Ver [[wiki/concepts/imagens-em-interfaces]].
- **Sem um bom thumbnail, um vídeo do YouTube "dificilmente" performa bem** (afirmação do autor, sem dado).

### Bancos de imagens

- **O autor guarda os links no Notion do curso** (seção "ilustrações e imagens"). Ver [[wiki/concepts/banco-de-imagens]].
- **Free Food Pictures:** imagens de alimentação para criativos e folders; "acredito que são gratuitas".
- **Sempre verificar o tipo de uso**: comercial, totalmente free, apenas pessoal (slide: "quais tipos de usos?").
- **[[wiki/entities/unsplash]] é o que ele mais usa, "de disparado"**: ao submeter fotos, os fotógrafos já concordam que o uso é livre ("The Internet's Source of Freely Usable Images"). Ver a tensão abaixo sobre "não ter direitos autorais".
- **Freepik também é citado como "muito bom"**; o autor promete adicionar mais links.

### Formatos para web

- **Quatro formatos para web**; o slide só lista três (PNG, JPG, SVG) e o autor diz que vai incluir o quarto (WebP) antes de exportar o PDF.
- **[[wiki/concepts/formato-png|PNG]]: foto com transparência que não pode virar SVG.** Uso típico: recorte com fundo transparente para aplicar em outros artboards.
- **[[wiki/concepts/formato-jpeg|JPG]]: "toda e qualquer fotografia realista".** Motivo: qualidade parecida com PNG, mas arquivo mais leve, e suporte universal ("até hoje eu não vi um software que não aceita JPG ou PNG"). Bom custo-benefício entre qualidade e peso.
- **Peso é acessibilidade.** "Ser acessível também é não ser tão pesado": nem todo mundo tem internet de 400 MB, 500 MB ou 1 GB, e no plano móvel um site pesado consome o pacote do usuário.
- **[[wiki/concepts/formato-svg|SVG]] (Scalable Vector Graphics) para ícones, ilustrações e backgrounds**; não serve para fotografia realista. O autor diz que no clone de estudo do Nubank que ele fez e no próprio FrontPUSH "todas as animações, tudo foi SVG"; no blog não, porque tem fotografias. O SVG volta na seção de animações CSS do curso.
- **Por que SVG:** é vetor, logo escalável (mobile ou desktop, "se adapta conforme o tamanho"), e é "meio que um comando de linhas em um plano cartesiano", portanto extremamente leve.
- **Demonstração no [[wiki/entities/figma]]:** um ícone de 64×64 do FrontPUSH escalado para 96 mantém as proporções; exportado como SVG e aberto no VS Code, é "somente alguns números", um arquivo de bytes.
- **[[wiki/concepts/formato-webp|WebP]]: mais novo, mesma qualidade de JPG e PNG, "bem mais otimizado" em tamanho de arquivo.**

### Alta qualidade, alta resolução

- **Alta resolução "transmite aquele esmero"**; imagem pixelada ou de baixa resolução estraga a interface. Slide: "Alta qualidade, alta resolução >> thumbnails, heros, propagandas…".
- **"É melhor a gente pegar uma imagem em alta resolução e diminuir do que pegar uma em baixa resolução e aumentar."** Ligado ao item do slide "Não distorça as imagens".
- **Exemplo do Unsplash:** uma busca por "minimalist" devolve fotos com tamanho original de 3285×4800.
- **Exemplo do blog pessoal do autor:** imagens de 1920×1100, todas do Unsplash, puxadas pelo plugin do Unsplash no Figma, que já entrega uma versão um pouco otimizada (menor que o original do site).

### Otimização de imagens

Ver [[wiki/concepts/otimizacao-de-imagens]].

- **Duas maneiras, que podem ser usadas juntas.**
- **Primeira: exportar para vários tamanhos de dispositivo** (o autor confessa que "não costuma fazer muito"). Resoluções maiores para telas maiores; no mobile a mesma imagem grande seria redimensionada de qualquer jeito, gastando peso à toa. Receita: 2x ou 1x para desktop, 0,5x ou 0,3x para mobile. O Figma oferece os multiplicadores no export (0,5x, 0,75x, 1,5x, 2x, 3x).
- **No código, "a gente avisa para o CSS"** qual imagem carregar em cada resolução. Para o designer, isso vira documentação de padrões de imagem no style guide. `[skill: ux-ui-mentor]` Na prática isso costuma ser HTML (`<picture>` com `<source media>` ou `srcset`/`sizes` no `<img>`), não só CSS; ver [[wiki/concepts/design-responsivo]].
- **Segunda: compressão.** A legenda pula de "vai otimizar o processo" (00:17:27) para "Dentre eles" (00:17:42); o anúncio da segunda maneira não ficou registrado, mas o contexto e o slide ("Otimização de imagens: TinyImage, Optmizila") mostram que é a compressão por ferramenta.
- **TinyImage:** aceita WebP, PNG e JPEG; "dependendo da imagem" pode salvar 80% do peso. O autor passa **todas** as imagens de todos os projetos por ele, "sem exceção".
- **Plugin do Figma TinyImage Compressor:** comprime, gera PDF e GIF, e deixa escolher a qualidade (90%, 80%) quando a qualidade extrema não é necessária.
- **WebP "não é muito conhecida hoje em dia"** (ver tensão abaixo).

### O que fica para a próxima aula

- Como escrever em imagens (contraste), não distorcer imagens, usar fotos de pessoas e não usar fake, ponto focal em fotografia, e ilustrações.
- Coberto (exceto ilustrações) em [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]].

## Entities

- [[wiki/entities/nasser]]: autor; "Násser aqui" na abertura e "O que significa isso, Násser?".
- [[wiki/entities/frontpush]]: ícones e animações em SVG; "parte de UI do FrontPUSH" no Figma.
- [[wiki/entities/unsplash]] (novo): banco de imagens favorito do autor; plugin no Figma.
- [[wiki/entities/figma]]: export multi-escala, plugin do Unsplash e do TinyImage, demonstração do SVG.
- [[wiki/entities/nubank]]: citado de passagem como projeto do autor feito todo em SVG: um clone de estudo, não o produto oficial (confirmado pelo usuário em 2026-11-13).
- Sem página própria: Free Food Pictures, Freepik, TinyImage, Optimizilla, Notion, YouTube, McDonald's, Burger King, VS Code.

## Concepts

- [[wiki/concepts/imagens-em-interfaces]] (novo)
- [[wiki/concepts/banco-de-imagens]] (novo)
- [[wiki/concepts/otimizacao-de-imagens]] (novo)
- [[wiki/concepts/formato-png]]
- [[wiki/concepts/formato-jpeg]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/formato-webp]]
- [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/elementos-da-interface]]

## Tensões com a wiki

- **"Unsplash não tem direitos autorais."** `[external]` As fotos continuam protegidas por direito autoral; o que o Unsplash dá é uma licença ampla: uso gratuito, comercial e não comercial, sem exigir atribuição, mas proibindo vender a foto sem alteração significativa e montar um serviço concorrente com elas (https://unsplash.com/license). Além disso, desde 2022 existe o Unsplash+, com imagens pagas misturadas na busca. "Sem medo de ser feliz" vale para as fotos gratuitas, dentro dessas regras.
- **"JPG e PNG são muito parecidos em qualidade."** Simplificação. [[wiki/concepts/formato-png]] é sem perdas e [[wiki/concepts/formato-jpeg]] é com perdas ([[wiki/concepts/compressao-com-perdas-vs-sem-perdas]]); em foto a diferença não se vê e o JPG fica bem menor, mas em texto, ícone e borda nítida o JPG borra. A regra da aula (foto → JPG, transparência → PNG) bate com [[wiki/sources/historia-dos-formatos-de-imagem]].
- **"WebP não é muito conhecida hoje em dia."** Datado. [[wiki/concepts/formato-webp]] (Google, 2010) tem suporte praticamente universal nos navegadores, e a wiki já registra AVIF como geração seguinte ([[wiki/concepts/formato-heic-avif]]). `[skill: ux-ui-mentor]` O checklist de performance da skill pede hero image em WebP e no tamanho correto.
- **"Avisar para o CSS."** A troca por resolução é feita sobretudo em HTML (`srcset`/`sizes`, `<picture>`); CSS só cobre background (`image-set()`, media queries). Não muda a ideia da aula.
- **Formatos na skill:** `[skill: ux-ui-mentor]` a skill liga imagem a Core Web Vitals: a hero costuma ser o LCP (bom < 2,5 s), e reservar espaço com `aspect-ratio` evita CLS. Também recomenda não usar `loading="lazy"` na viewport inicial. A aula não fala de métricas, mas o argumento (peso piora a experiência) é o mesmo.

## Open Questions

- **Fala x legenda em "Quando você estiver em uma resolução maior, carregue essa outra imagem aqui [...] em uma resolução menor".** A segunda ocorrência de "maior" deve ser "menor" (ato falho ou ASR); mantido literal no raw.
- **"Tem a Freepik, forajador de imagens"**: provavelmente "o gerador de imagens" (o Freepik tem gerador por IA), mas ambíguo; mantido literal.
- **"O seu banco de dados da sua operadora"**: quis dizer pacote de dados; mantido literal.
- ~~**"TinyImage"**~~ **Resolvido (2026-11-13):** a legenda diz "thin image"; o usuário confirmou que é TinyImage, como no slide. A semelhança do texto do site ("Drop your WebP, PNG or JPEG files here") com o do TinyPNG não muda isso. Na parte 2 o autor cita outro compressor, o TinyPNG, e o Optimizilla aparece na fala ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).
- **Os 80% de economia** são "dependendo da imagem", sem medição na aula.
- `date_published` vazio.

## Raw Quotes

> "O ser humano por si só já é uma criatura visual."

> "Ser acessível também é não ser tão pesado, porque nem todo mundo tem uma internet, sei lá, 400, 500, 1GB."

> "É melhor a gente pegar uma imagem em alta resolução e diminuir do que pegar uma em baixa resolução e aumentar."

> "Todas as imagens de todos os meus projetos eu, sem exceção, sempre passo pelo TinyImage."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — versão "W7" da mesma aula: três formatos (sem WebP), Shutterstock para branding, texto branco
