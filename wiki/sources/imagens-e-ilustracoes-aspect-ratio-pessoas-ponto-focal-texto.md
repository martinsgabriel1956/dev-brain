---
type: source
title: "Elementos da interface: imagens e ilustrações, parte 2 (formato adequado, distorção, fotos de pessoas, ponto focal e texto sobre imagem)"
aliases: ["aula de imagens parte 2", "imagens e ilustrações parte 2", "como escrever em imagens", "ponto focal em fotografia"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, imagens, fotografia, aspect-ratio, ponto-focal, regra-dos-tercos, contraste, texto-sobre-imagem, gradiente, otimizacao-de-imagens, svg, figma, acessibilidade]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: imagens e ilustrações (parte 2)

## TL;DR

Continuação de [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]], de [[wiki/entities/nasser|Násser]] no curso do [[wiki/entities/frontpush|FrontPUSH]]. Fecha as diretrizes de [[wiki/concepts/imagens-em-interfaces|imagem em interface]] em cinco blocos: (1) a **terceira maneira de [[wiki/concepts/otimizacao-de-imagens|otimizar]]** é usar o formato adequado: ícone em [[wiki/concepts/formato-svg|SVG]], não em [[wiki/concepts/formato-png|PNG]] ("modelo mais arcaico"), e logo de cliente em baixa definição se vetoriza no [[wiki/entities/figma]] com a Pen Tool; cita também o Optimizilla e o TinyPNG; (2) **não distorcer**: preservar o [[wiki/concepts/aspect-ratio]]; o Figma já faz um crop automático para impedir; (3) **fotos de pessoas reais, nunca fake**: [[wiki/concepts/fotos-de-pessoas-reais|gente de verdade]] humaniza ("pessoas negociam com pessoas"), com o site do [[wiki/entities/santa-monica-studio]] mostrando a equipe; contrate um fotógrafo em vez de usar a foto de aperto de mão do Google Imagens; (4) **[[wiki/concepts/ponto-focal-em-fotografia|ponto focal]]**: grade de nove blocos, um único ponto focal, posto nos quatro cruzamentos; (5) **[[wiki/concepts/texto-sobre-imagem|como escrever em imagens]]**: 99% das vezes letra branca, garantida por uma "capa" de gradiente linear sobre a foto (ex.: 50% → 90% de preto), de preferência na cor do background para acoplar a imagem à interface. A regra de fundo é de [[wiki/concepts/contraste]]: "se eu não preciso garantir legibilidade é porque não precisa ler".

## Key Claims

### Recapitulação

- **Quatro formatos para web: "PNG, JPG, WebP para fotos, fotografias mesmo, e o SVG é vetor"** (ilustrações e ícones). A frase agrupa PNG com fotos; ver tensão abaixo.

### Formato adequado como terceira otimização

- **"Existem três maneiras" de otimizar; a terceira, não citada antes, "é utilizar o formato adequado para a proposta".** As duas primeiras eram export multi-escala e compressão (parte 1). Ver [[wiki/concepts/otimizacao-de-imagens]].
- **Ícone em JPG fica com fundo branco**, porque o [[wiki/concepts/formato-jpeg|JPG]] "não tem a propriedade de deixar o fundo transparente"; para transparência, [[wiki/concepts/formato-png|PNG]].
- **Mas ícone em PNG "é um modelo mais arcaico".** O autor usava só PNG nos ícones "em um tempo não muito distante"; hoje exporta em [[wiki/concepts/formato-svg|SVG]], "muito mais escalável, muito mais otimizado".
- **Critério: "bater o olho".** Se dá para ser feito no Figma e não é fotografia realista, vetorize, "principalmente logo".
- **Logo do cliente em baixa definição: traga para o [[wiki/entities/figma]] e vetorize** com a Pen Tool ou outro plugin ou ferramenta.
- **Compressores:** o Optimizilla, "que o pessoal utiliza bastante", e o TinyPNG, que o autor usa "de longe sempre" (nome confirmado pelo usuário em 2026-11-13).
- **Há otimizações de código, como carregamento sob demanda**, "mas já é mais para a área de código". Ver [[wiki/concepts/lazy-vs-eager-loading]].

### Não distorça as imagens

- **Preservar o [[wiki/concepts/aspect-ratio]]**, "a relação entre a dimensão horizontal e a dimensão vertical".
- **O Figma previne a distorção:** ao puxar só um lado, "ela faz meio que um crop automático"; mesmo agrupando, "ela não deixa".
- **Mas dá para distorcer:** num post do Instagram o autor conseguiu, e num trecho de imagem "não ficou tão ruim"; na foto mostrada em seguida, a distorção é evidente. Conclusão: "nada de distorção de imagem".

### Fotos de pessoas, não fakes

- **"Sempre use fotos de pessoas e não use fotos de pessoas fakes."** Ver [[wiki/concepts/fotos-de-pessoas-reais]].
- **Foto de gente "humaniza e traz a sua audiência mais para perto."** A sensação é de que "pessoas negociam com pessoas": por trás de um CNPJ há um grupo de pessoas, e isso deixa o cliente mais à vontade para comprar ou negociar.
- **É tendência, "muito presente nas empresas maiores"**, que mostram quem trabalha nelas (afirmação do autor, sem dado).
- **Exemplo: [[wiki/entities/santa-monica-studio]].** Na seção inicial do site, fotos reais de desenvolvedores e designers da equipe que fez os jogos.
- **Contraexemplo: buscar "negócios pessoas" no Google Imagens** e usar o aperto de mão em volta da mesa: "essa imagem é extremamente fake", "você percebe que essas imagens você tirou do Google".
- **Recomendação: contratar um fotógrafo, "por mais simples que seja"**, e fotografar o pessoal, os funcionários e o espaço da empresa.

### Ponto focal em fotografia

- **Câmeras têm "grades ou grids que geralmente dividem a sua foto em nove blocos".** Ver [[wiki/concepts/ponto-focal-em-fotografia]].
- **"Toda imagem é interessante que ela tenha um ponto focal, não dois"**, como na aula de [[wiki/concepts/espaco-em-branco|white space]]: dar ênfase a uma coisa.
- **Os pontos focais são "o cruzar desses grids"**: quatro pontos. A pessoa (a "cabecinha", na demonstração com uma elipse cinza no Figma) deve ficar dentro ou ao redor deles.
- **Mais pontos focais, ou fugir dessa "regrinha da fotografia", "pode prejudicar a experiência".**
- **É "noção de fotografia"**, mas vale saber o conceito para aplicar na interface.

### Como escrever em imagens

- **Retoma o princípio de [[wiki/concepts/contraste]].** Demonstração: "PS5, o novo console da nova geração" escrito direto sobre uma foto, sem tratamento. Ver [[wiki/concepts/texto-sobre-imagem]].
- **"99% das vezes vai ser letra branca em cima de imagem."** Outra cor só por contraste: num fundo "super amarelo", um cinza mais escuro. "Salvo se o fundo não for muito claro da sua imagem, utilize branco."
- **Como garantir o contraste do branco: "uma capa de gradiente em cima da sua imagem"**: cor preta com transparência, posicionada conforme onde está o texto ("régua de contraste").
- **A ponta clara não precisa ir a zero:** pode ficar em 30%, 40%; na demonstração, 50% em cima e 90% embaixo, e "o contraste aumentou demais".
- **"Eu preciso garantir a legibilidade daquilo que está sendo escrito em cima da imagem, porque senão não faz sentido."**
- **Nos posts, o gradiente é da "mesmíssima cor do background"**: o mesmo azul do fundo, a 100% na base, para a imagem "ir revelando aos poucos" e ficar "bem mais acoplada" à interface. O início do gradiente fica "um pouquinho para cima" para abrir espaço ao texto.
- **Só onde precisa:** em imagens de fundo muito claro aplicou "com certeza"; nas já escuras, com bom contraste, "deixei passar".

## Entities

- [[wiki/entities/nasser]]: autor; "Násser aqui" na abertura e "Como assim, Násser?" / "Então, Násser, eu recebi lá do meu cliente...".
- [[wiki/entities/frontpush]]: curso em que a aula está; os "posts" com gradiente azul não são identificados (ver open questions).
- [[wiki/entities/figma]]: crop automático contra distorção, vetorização de logo com Pen Tool, demonstração do grid e do gradiente.
- [[wiki/entities/santa-monica-studio]] (novo): site com fotos reais da equipe como exemplo de humanização.
- Sem página própria: Optimizilla, TinyPNG, Instagram, Google Imagens, PlayStation/PS5, Notion.

## Concepts

- [[wiki/concepts/aspect-ratio]] (novo)
- [[wiki/concepts/fotos-de-pessoas-reais]] (novo)
- [[wiki/concepts/ponto-focal-em-fotografia]] (novo)
- [[wiki/concepts/texto-sobre-imagem]] (novo)
- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/otimizacao-de-imagens]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/formato-png]]
- [[wiki/concepts/formato-jpeg]]
- [[wiki/concepts/banco-de-imagens]]
- [[wiki/concepts/lazy-vs-eager-loading]]

## Tensões com a wiki

- **"PNG, JPG, WebP para fotos."** Na parte 1, PNG é só para imagem com transparência que não vira SVG, e JPG é para "toda e qualquer fotografia realista" ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). A recapitulação agrupa os três formatos raster contra o SVG; não é regra nova.
- **"Não use fotos fake" x [[wiki/concepts/banco-de-imagens|bancos de imagens]].** A parte 1 recomenda o [[wiki/entities/unsplash]]; esta diz para não usar gente de banco para representar a empresa. Leitura conciliada (inferência): banco serve para cenário, produto e textura; para "quem somos" e equipe, foto própria.
- **"Um ponto focal, não dois"** bate com [[wiki/concepts/hierarquia-visual]] (dois elementos com o mesmo peso confundem o olho) e com o macro espaço como foco em [[wiki/concepts/espaco-em-branco]]. Aqui o princípio vai para dentro da foto.
- **"99% das vezes letra branca."** Heurística do autor. `[skill: ux-ui-mentor]` WCAG AA pede 4.5:1 para texto normal e 3:1 para texto grande; sobre foto, o contraste varia pixel a pixel, por isso o gradiente: ele uniformiza o fundo atrás do texto. A skill avisa que passar no número não basta e pede teste com texto real.
- **"O Figma previne a distorção."** No navegador não há essa proteção: um `<img>` com largura e altura fixas fora da proporção estica. `[external]` `object-fit: cover` faz no CSS o mesmo crop automático (https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit). `[skill: ux-ui-mentor]` Reservar a proporção com `aspect-ratio` também evita CLS.

## Open Questions

- ~~**TinyImage x TinyPNG.**~~ **Resolvido (2026-11-13):** o usuário confirmou que são dois compressores: TinyPNG nesta aula e TinyImage na parte 1 ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). Fica uma tensão leve: na parte 1 o TinyImage é "dos que eu mais utilizo"; aqui, "de longe eu utilizo sempre o TinyPNG".
- **"Os posts" e "a imagem oficial"** com gradiente azul: não fica claro se são posts do Instagram do autor, do blog ou do FrontPUSH. A fala cita "algum post do Instagram" na parte de distorção.
- **"É o último ponto antes da gente falar de imagens e ilustrações"**: provavelmente "antes de falar de ilustrações"; mantido literal. Ilustrações ficam para a próxima aula. A parte 3 ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]) saiu, mas é "mais focado em imagens" (bom senso, Who Can Use, padronização, blend modes); ilustrações seguem pendentes. **Fechado:** a parte 4 ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]) é a aula de ilustrações.
- **"Formatos para o web"** e "o cruzar desses grids": mantidos literais.
- **Sem dado** para "tendência em empresas grandes" e "99% das vezes".
- `date_published` vazio.

## Raw Quotes

> "Utilizar foto de pessoas na sua interface humaniza e traz a sua audiência mais para perto."

> "Toda imagem é interessante que ela tenha um ponto focal, não dois, mas um ponto focal."

> "99% das vezes vai ser letra branca em cima de imagem."

> "Se eu não preciso garantir legibilidade é porque não precisa ler."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — a Pen Tool em detalhe: vetorizar um ícone de telefone passo a passo
