---
type: source
title: "Imagens e ilustrações (edição \"W7\"): introdução da seção, SVG, bancos de imagens, texto branco, resoluções e formatos"
aliases: ["introdução imagens e ilustrações W7", "aula de imagens W7", "SVG manipulável por CSS", "texto branco como coringa"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, imagens, ilustracoes, svg, motion, banco-de-imagens, licenca, texto-sobre-imagem, contraste, aspect-ratio, design-responsivo, otimizacao-de-imagens, png, jpeg, figma, unsplash, shutterstock]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Imagens e ilustrações (edição "W7"): introdução, SVG, bancos, texto branco, resoluções e formatos

## TL;DR

Abertura da seção "Imagens & Ilustrações" da edição "W7" do curso de [[wiki/entities/nasser|Násser]], a mesma de [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] ("da mesma forma que eu fiz com o espaçamento e linhas", teoria e prática misturadas). Cores e tipografia foram puladas de propósito: cada uma terá módulo próprio. A seção ganha "mais veemência" porque é a base do que ele faz em motion: quase todas as suas ilustrações são [[wiki/concepts/formato-svg|SVG]], com cada elemento num caminho separado que o CSS consegue manipular, e esse caminho já sai traçado do [[wiki/entities/figma]]. A aula cobre: (1) **o que a imagem comunica**: precisa ter relação com o conteúdo, e foto genérica de banco ("pessoas conversando", "imagens de gringos") está "se tornando brega"; para mostrar o time, contrate fotógrafo ([[wiki/concepts/fotos-de-pessoas-reais]]); (2) **[[wiki/concepts/banco-de-imagens|bancos de imagens]]**: [[wiki/entities/unsplash]] "de disparado", Gratisography, Pexels, Foodiesfeed, Pixabay e [[wiki/entities/shutterstock]] (este para referência de branding), sempre conferindo free x pago e uso pessoal x comercial; (3) **[[wiki/concepts/texto-sobre-imagem|texto sobre imagem]] em branco** como "coringa", baixando saturação ou brilho ou pondo uma capa preta com opacidade para garantir [[wiki/concepts/contraste]]; (4) **não esticar imagens** ([[wiki/concepts/aspect-ratio]]); (5) **resoluções diferentes**: exportar tamanhos por dispositivo e carregar por media query ([[wiki/concepts/otimizacao-de-imagens]], [[wiki/concepts/design-responsivo]]); (6) **três formatos**: SVG "só alegria", [[wiki/concepts/formato-jpeg|JPG]] para fotografia, [[wiki/concepts/formato-png|PNG]] para transparência. Diferente da edição FrontPUSH ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]), não cita WebP.

## Key Claims

### Por que a seção tem mais peso

- **Cores e tipografia ficaram de fora de propósito**: são "gigantescos" e terão um módulo cada.
- **Estrutura anunciada:** uma aula só de imagens, outra de ilustrações, depois prática no Figma (o slide reforça: "Terá prática com Figma").
- **"Como é que faz as suas criações?" Resposta: SVG.** "A maioria das ilustrações [...] elas são baseadas em SVGs." Ver [[wiki/concepts/formato-svg]].
- **SVG separa os elementos no código.** A seta com o nome Násser é um caminho que ele manipula com CSS; o quadradinho ao lado é outro caminho, também manipulável. Promete mostrar na prática.
- **A sacada do motion está no design.** "A grande sacada dessas criações, elas se dão no design, não tem como, o UI é muito importante nessa primeira parte de criação." Ele já pensa a animação ao desenhar e "deixo o caminho traçado dos elementos no Figma". Por isso a aula é complementar para quem quer motion.
- **Exemplos citados:** ilustrações isométricas em perspectiva do site dele; landing page do curso (SVG que cresce no hover); "o meu site inteiro é composto de SVG"; no Instagram, quase todas as criações do [[wiki/entities/frontpush|FrontPUSH]] são SVG, "menos o Sharingan, o camaleão".

### Imagens: o que comunica

- **Toda imagem precisa de um porquê**: "você não pode pegar uma imagem e jogar ela na interface sem ter um porquê, então precisa ter relação com o conteúdo." Ver [[wiki/concepts/imagens-em-interfaces]].
- **Erro de iniciante:** buscar "pessoas conversando" no [[wiki/entities/google]] e espalhar pelo site. São genéricas, não traduzem "a essência da sua instituição" e, com o tempo, ficam "brega": "imagens de gringos [...] que não transmitem muito a realidade".
- **Foto do time = fotógrafo** contratado, para "passar essa realidade". Ver [[wiki/concepts/fotos-de-pessoas-reais]].

### Bancos de imagens

- **Duas vias:** contratar fotógrafo ou recorrer a banco de imagens. Os links ficam no "Master File", o Notion do curso, com uma seção de bancos gratuitos. Ver [[wiki/concepts/banco-de-imagens]].
- **[[wiki/entities/unsplash]] é o mais usado "de disparado"**: "free", "0800", uso pessoal e comercial; ao submeter a foto, o fotógrafo já concorda com essa política. Tem plugin no Figma.
- **Cuidado com a licença:** quais são free, quais são pagos, quais liberam uso pessoal, comercial "ou vice-versa"; há imagens "liberadas só para uso pessoal".
- **Outros citados:** Gratisography, Pexels, Foodiesfeed (só comida; a página diz "uso pessoal e comercial grátis" nas letras miúdas), Pixabay e "Victiz" (nome incerto, ver Open Questions).
- **[[wiki/entities/shutterstock]] para branding:** é "um dos que eu mais utilizo", mas como referência ao criar marca: busca "Letter B Logo" para um cliente que quer a inicial. Faz parte do briefing; detalhes ficam para o módulo de identidade visual.

### Regras gerais

- **Texto sobre imagem: branco como "coringa".** Vermelho, azul ou verde são exceções; desde que haja bom contraste, "sempre encaixe texto branco". Ver [[wiki/concepts/texto-sobre-imagem]].
- **Imagem clara demais:** diminuir saturação, diminuir brilho ou "adicionar uma capa preta com opacidade na frente da imagem". Ver [[wiki/concepts/contraste]].
- **Não esticar imagens.** Uma 1920×1080 (Full HD) não deve ser esticada ou espremida para caber num banner. O Figma "não deixa você fazer essa cagada": mantém a proporção e centraliza a foto. Ver [[wiki/concepts/aspect-ratio]].

### Diferentes resoluções e otimizações

- **Motivo declarado: acessibilidade.** Um site é acessado de mobile, tablet e desktop, em muitos tamanhos e resoluções.
- **A imagem de desktop no mobile é desperdício.** A tela do mobile é menor nas duas dimensões; a imagem maior "vai ser mais pesada". Ver tensão sobre "pixelada" abaixo.
- **Exportar tamanhos diferentes e carregar "por Media Query lá no CSS".** O slide resume como "@1x, @2x, @3x" e "Acesso Mobile, Tablets, Desktop". Ver [[wiki/concepts/otimizacao-de-imagens]] e [[wiki/concepts/design-responsivo]].

### Formatos

- **Três principais na web e no export do Figma: PNG, JPG e SVG.**
- **SVG é "o grande queridinho"**: vetorial, não perde resolução ao esticar ou diminuir porque "a resolução dele é definida por código", é mais leve e permite manipulação no CSS. "SVG só alegria." Indica para ícones e "tudo que é coisa". Ver [[wiki/concepts/formato-svg]].
- **JPG para fotografia e ilustração realista**: o mais difundido, boa relação entre qualidade e peso. Ver [[wiki/concepts/formato-jpeg]].
- **PNG "não vai sumir"** por causa da transparência, que o JPG não tem; "geralmente um pouquinho mais pesado que o JPG, mas também é otimizado para web". Ver [[wiki/concepts/formato-png]].

### O que o slide traz e a fala não cobre

- **Ilustrações:** ajudar na compreensão do conteúdo, consistência, plugins do Figma, licença. Ficam para a próxima aula (na edição FrontPUSH: [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]; ver [[wiki/concepts/ilustracoes-em-interfaces]]).
- **Otimização: "Plugin: TinyImage no Figma".** Não é citado na fala; o mesmo compressor aparece na edição FrontPUSH.

## Entities

- [[wiki/entities/nasser]]: autor; "Násser" e a seta "com o nome Násser" (legenda: "Nácia", "Nácer"), como nas outras aulas "W7".
- [[wiki/entities/frontpush]]: criações do Instagram feitas em SVG.
- [[wiki/entities/figma]]: onde o caminho do SVG é traçado; plugin do Unsplash; proteção contra distorção; export em tamanhos.
- [[wiki/entities/unsplash]]: banco favorito.
- [[wiki/entities/shutterstock]] (novo): referência de branding.
- [[wiki/entities/google]]: busca de "pessoas conversando", o exemplo do erro.
- Sem página própria: Notion ("Master File"), Instagram, Gratisography, Pexels, Foodiesfeed, Pixabay, "Victiz", TinyImage.

## Concepts

- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/formato-jpeg]]
- [[wiki/concepts/formato-png]]
- [[wiki/concepts/banco-de-imagens]]
- [[wiki/concepts/fotos-de-pessoas-reais]]
- [[wiki/concepts/texto-sobre-imagem]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/aspect-ratio]]
- [[wiki/concepts/otimizacao-de-imagens]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/ilustracoes-em-interfaces]]

## Tensões com a wiki

- **Três formatos aqui, quatro na edição FrontPUSH.** [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] acrescenta [[wiki/concepts/formato-webp|WebP]] como "mais otimizado". `[skill: ux-ui-mentor]` O checklist de performance da skill pede hero image em WebP e no tamanho correto; a omissão aqui é a lacuna maior da aula.
- **"Diminuir no mobile vai ficar muito pixelada."** `[external]` Reduzir uma imagem no navegador não pixela; o que pixela é ampliar uma imagem pequena. O custo real de mandar a imagem de desktop para o mobile é peso (bytes e decodificação). A outra edição diz o contrário do risco: "é melhor [...] pegar uma imagem em alta resolução e diminuir do que pegar uma em baixa resolução e aumentar". O argumento de peso da aula está certo; o de pixelização, não.
- **"Por Media Query lá no CSS."** `[skill: ux-ui-mentor]` Para imagem de conteúdo o mecanismo nativo é HTML: `<picture>` com `<source media>` ou `srcset`/`sizes` no `<img>`; media query em CSS serve para `background-image`. O "@1x, @2x, @3x" do slide é densidade de pixel (descritor `x` no `srcset`), não tamanho de tela. Mesma ressalva já registrada na edição FrontPUSH.
- **SVG manipulável por CSS.** `[external]` Só quando o SVG está inline no HTML (ou num `<object>`/`<use>` com acesso ao DOM); um SVG carregado por `<img>` ou `background-image` não expõe os `<path>` ao CSS da página. `[skill: ux-ui-mentor]` A skill lista o trade-off "SVG inline vs img": inline renderiza e é estilizável; `img` ganha cache.
- **Shutterstock na lista de "bancos de imagens".** `[external]` Shutterstock é banco pago por licença; não entra na seção de gratuitos. A aula o usa para referência visual de marca, não para publicar a foto, e isso é coerente com o próprio alerta de "free x pago".
- **Texto branco "sempre".** Consistente com a parte 2 da edição FrontPUSH ("letra branca 99% das vezes", [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]); lá a capa é gradiente, aqui é capa preta com opacidade ou ajuste de saturação e brilho.

## Open Questions

- **"Victiz"**: nome incerto; pode ser Vecteezy (banco de vetores e fotos), mas mantido literal no raw.
- **"buscar essas fotos de étnofigma"**: provável "de dentro do Figma" (o plugin do Unsplash), mas ambíguo; mantido literal.
- **Foodiesfeed** (legenda "Foods Feed") e **Sharingan** (legenda "xaringan") são correções de confiança média.
- **Edição "W7":** o que o logo significa segue em aberto (ver log das aulas de espaçamento e formas).
- `date_published` vazio.

## Raw Quotes

> "Você não pode pegar uma imagem e jogar ela na interface sem ter um porquê."

> "A grande sacada dessas criações, elas se dão no design."

> "Vai escrever na imagem texto branco, meio que é uma regra legal, um coringa."

> "Então SVG só alegria."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — aula de ilustrações da edição "W7": compreensão, consistência (cinza + cor da marca), unDraw, plugins de isometria, TinyImage
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — o SVG aberto em código: gradiente, filtros e caminhos que o CSS manipula
