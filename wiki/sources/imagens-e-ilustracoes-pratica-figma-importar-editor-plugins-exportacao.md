---
type: source
title: "Imagens e ilustrações na prática no Figma (edição \"W7\"): importar, editor de imagem, plugins de ilustração e exportação"
aliases: ["prática de imagens no Figma", "plugins de ilustração no Figma", "aula prática de imagens W7", "isometria no Figma"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, figma, imagens, ilustracoes, plugins, isometria, texto-sobre-imagem, contraste, otimizacao-de-imagens, compressao, export, svg, unsplash, wireframe]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Imagens e ilustrações na prática no Figma (edição "W7")

## TL;DR

Aula prática (cerca de 13 min) que fecha a seção de imagens e ilustrações da edição "W7" e demonstra no [[wiki/entities/figma]] o que [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] prometeu: (1) **três jeitos de importar imagem**: arrastar o arquivo, Place Image ou Ctrl Shift K; (2) **instalar plugin** pela Community (exemplo: [[wiki/entities/unsplash]], que puxa fotos direto para o canvas); (3) **editor de imagem nativo** (exposição, contraste, saturação, temperatura; fit, crop, fill); (4) **[[wiki/concepts/texto-sobre-imagem|texto sobre imagem]]**: em vez de mexer na foto, um retângulo preto a 20% de opacidade atrás do título branco; (5) **plugins de ilustração**: Blobs (bolhas aleatórias para composição e [[wiki/concepts/wireframe|wireframes]]), dois de isometria, um de ondas em SVG e o "skill-depth"; (6) **[[wiki/concepts/ilustracao-isometrica|isometria]] "raiz"** sem plugin: retângulo arredondado, rotação de 45°, Ctrl G e altura a 50%; (7) **TinyImage Compressor** para escolher a relação peso x qualidade; (8) **export**: pôr a imagem ou o ícone dentro de um frame e exportar o frame (PNG, SVG e escalas). Ver [[wiki/concepts/otimizacao-de-imagens]].

## Key Claims

### Importar e instalar plugins

- **Importar:** clicar e arrastar o arquivo para o Figma; ou, no menu do quadradinho, **Place Image** (caixa de diálogo, Abrir ou Place All); ou **Ctrl Shift K**, que abre a mesma caixa.
- **App desktop.** Ele usa a versão desktop por acreditar que consome menos RAM que o navegador: "eu posso estar errado". Não verificado.
- **Instalar plugin:** ícone do Figma → Community → busca → aba de plugins → instalar; depois aparece na setinha, na aba de plugins.
- **[[wiki/entities/unsplash]] como plugin:** "aquele site, só que de maneira mais direta", clicando nas fotos e colocando direto no arquivo. Ver [[wiki/concepts/banco-de-imagens]].
- **Vídeo bônus sobre todos os plugins** prometido; aqui o foco é ilustração.

### Editor de imagem e texto sobre imagem

- **O Figma tem editor de imagem:** exposição, contraste, saturação e temperatura, para "um maior contraste", algo "mais dramático, mais frio" ou "mais quente".
- **Modos:** fit "mantém ela dentro de um quadrado, sem modificar a resolução original da foto"; crop corta o trecho escolhido (Enter); fill (preenchimento).
- **Título sobre a foto, "sempre branco".** Se o contraste está ruim, dá para baixar a exposição da foto; o que ele "costuma fazer" é deixar a foto original, desenhar um retângulo, trazer o texto para frente (bring to front), pintar o retângulo de preto com **opacidade de 20%**. Ver [[wiki/concepts/texto-sobre-imagem]] e [[wiki/concepts/contraste]].

### Plugins de ilustração

- **Blobs:** gera bolhas aleatórias por complexidade e contraste ("contraste 10" deixa mais espaçado); ele usa como bolhas na composição dos wireframes. Ver [[wiki/concepts/ilustracoes-em-interfaces]].
- **Plugin isométrico** ("open isometric"): todos os itens isométricos do site dele foram feitos com ele. Ver [[wiki/concepts/ilustracao-isometrica]].
- **Método "raiz" sem plugin:** retângulo "com resolução de desktop", bordas arredondadas (todas ou só uma, selecionando o ponto), rotação de 45° (arrastando perto do eixo ou digitando 45 no painel), **Ctrl G** e altura do grupo a **50%**: "meio que ele já vira uma forma isométrica".
- **Ondas:** escolhe a onda e a profundidade, um dado para modo aleatório, e gera "SVGs de ondas" para compor interfaces com curvas. O nome do plugin caiu numa lacuna da legenda. Ver [[wiki/concepts/formato-svg]].
- **Segundo plugin "isometric":** precisa de uma forma com quatro pontos, aplica perspectiva de 45° e deixa mudar o ângulo (exemplo: 35°).
- **"skill-depth":** usa a propriedade transform na vertical e na horizontal e dá "mais liberdade" para criar formas isométricas.

### Compressão e exportação

- **TinyImage Compressor:** seleciona a imagem (a do Homem-Aranha, ver [[wiki/entities/spider-man-projeto-nasser]]), escolhe a qualidade num controle deslizante pela relação "peso e compressão" e clica em Compress Image; a fala diz que exporta também PDF e GIF. Atenção: na demo ele comprimiu todas as imagens de uma vez sem querer. Ver [[wiki/concepts/otimizacao-de-imagens]] e [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]].
- **Exportar pelo frame.** Ele "sempre" põe a imagem ou o ícone dentro de um frame ("para poder ficar bonitinho no SVG") e exporta o frame: formatos (PNG "e tudo"), escalas prontas do Figma, preview, Export frame. Ver [[wiki/concepts/formato-png]] e [[wiki/concepts/formato-svg]].

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário).
- [[wiki/entities/figma]]: ferramenta da aula toda.
- [[wiki/entities/unsplash]]: plugin usado como exemplo de instalação.
- [[wiki/entities/spider-man-projeto-nasser]]: a imagem do Homem-Aranha comprimida na demo (inferência).
- Sem página própria: TinyImage Compressor, Blobs, os dois plugins "isometric", o plugin de ondas, "skill-depth".

## Concepts

- [[wiki/concepts/ilustracao-isometrica]] (novo)
- [[wiki/concepts/texto-sobre-imagem]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/otimizacao-de-imagens]]
- [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]]
- [[wiki/concepts/ilustracoes-em-interfaces]]
- [[wiki/concepts/banco-de-imagens]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/formato-png]]
- [[wiki/concepts/wireframe]]

## Tensões com a wiki

- **Fecha as promessas da aula anterior.** [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] prometeu plugins de isometria e a demo do TinyImage; os dois aparecem aqui. A licença dos plugins e dos bancos, também prometida, não é retomada.
- **Terceira técnica de capa.** A wiki já tinha capa de gradiente (edição FrontPUSH) e "capa preta com opacidade" (abertura "W7"); aqui o número aparece: preto a 20%. `[skill: ux-ui-mentor]` A regra é medir o contraste (4,5:1 para texto normal) no pior ponto da foto atrás do texto; 20% pode não bastar numa foto clara, então o valor é ponto de partida, não regra. Ver [[wiki/concepts/texto-sobre-imagem]].
- **50% não é isometria "verdadeira".** `[external]` Girar 45° e achatar a altura para 50% dá a projeção 2:1 (bordas a cerca de 26,57°), a "isometria de jogo" ou dimetria. A isométrica de 30° pede altura a cerca de 57,7% (tan 30°). Para ilustração de interface as duas servem, desde que todas as peças usem a mesma ([[wiki/concepts/consistencia-visual]]). Ver [[wiki/concepts/ilustracao-isometrica]].
- **Export pelo frame vs. export multi-escala.** A edição FrontPUSH ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]) mostra as escalas 0,5x–3x; aqui o foco é o frame como caixa do ícone. `[skill: ux-ui-mentor]` Na entrega, reservar `aspect-ratio` e usar `loading="lazy"` fora da viewport inicial seguem valendo.
- **"Tem como eu criar PDF, GIF".** A frase está no bloco do compressor, mas, pelo contexto, pode ser do painel de export. Não conferido.

## Open Questions

- ~~**Autoria inferida.**~~ **Resolvido (2026-11-13):** o usuário confirmou que a aula é de [[wiki/entities/nasser|Násser]].
- **Quais plugins?** O de ondas caiu na lacuna 00:08:50–00:09:00 (candidato `[external]`: Get Waves, que tem botão de aleatório em forma de dado, https://www.producthunt.com/products/get-waves/alternatives). "skill-depth" mantido literal; candidatos `[external]`: SkewDat (ajusta profundidade, altura e largura da perspectiva, https://alternativeto.net/software/skewdat/about) ou um plugin de skew (https://www.samolevsky.com/blogs/figma-plugins/skew-objects). Os dois "isometric" não têm autor dito.
- **"Decreto ele a 50%"**: provável "decresço"; mantido literal.
- **Lacunas da legenda** sem fala: 00:08:50–00:09:00, 00:10:46–00:10:51, 00:11:13–00:11:21 (onde o compressor é apresentado).
- `date_published` vazio.

## Raw Quotes

> "Coloco ele na cor preta e eu aplico opacidade de 20%, e eu consigo um maior contraste para poder colocar os meus textos nas imagens."

> "Essa forma é a forma raiz de construir formas isométricas, se a gente ter um plugin que facilita a nossa vida, vamos utilizá-la."

> "Eu sempre costumo criar um frame [...] onde a imagem está aqui dentro, e aí eu consigo vir aqui em export."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — aula seguinte: o SVG no Figma por dentro (unDraw editável, mockup de iPhone, código do SVG)
