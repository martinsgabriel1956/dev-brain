---
type: concept
title: "Otimização de imagens para web"
aliases: ["otimização de imagens", "image optimization", "compressão de imagens", "imagens responsivas"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 7
tags: [performance, imagens, web, compressao, responsivo, figma, core-web-vitals]
skill: ux-ui-mentor
status: stub
---

# Otimização de imagens para web

Reduzir o peso das imagens sem perda visível, para carregar rápido e não gastar o plano de dados do usuário. Násser trata isso como parte da acessibilidade ("ser acessível também é não ser tão pesado") e aponta duas maneiras que se somam ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). Na parte 2 ele completa: "existem três maneiras", e a terceira é o formato adequado ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## 1. Um tamanho por dispositivo

Exportar a mesma imagem em várias escalas e servir cada uma conforme a tela: 2x ou 1x para desktop, 0,5x ou 0,3x para mobile. O [[wiki/entities/figma]] tem os multiplicadores no painel de export (0,5x, 0,75x, 1,5x, 2x, 3x). O autor admite que "não costuma fazer muito".

`[skill: ux-ui-mentor]` No código, a escolha fica com o navegador via `srcset`/`sizes` no `<img>`, ou com `<picture>` e `<source media>` quando o recorte muda por breakpoint:

```html
<picture>
  <source media="(min-width: 768px)" srcset="hero-desktop.jpg">
  <source media="(min-width: 480px)" srcset="hero-tablet.jpg">
  <img src="hero-mobile.jpg" alt="...">
</picture>
```

Ver [[wiki/concepts/design-responsivo]].

## 2. Compressão

Passar toda imagem por um compressor antes de publicar. O autor usa o TinyImage (site e plugin "TinyImage Compressor" no Figma), que aceita WebP, PNG e JPEG e, "dependendo da imagem", corta até 80% do peso; o plugin deixa escolher a qualidade (90%, 80%). O slide cita também o Optimizilla, que a parte 2 menciona como "o pessoal utiliza bastante". Na parte 2 ele também diz que usa "de longe sempre" o TinyPNG, outro compressor (confirmado pelo usuário em 2026-11-13). Ver [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]].

## 3. Formato adequado

A terceira maneira, e a primeira a decidir: [[wiki/concepts/formato-svg|SVG]] para ícone e ilustração (pesa bytes), [[wiki/concepts/formato-jpeg|JPG]] para foto, [[wiki/concepts/formato-png|PNG]] só quando precisa de transparência, [[wiki/concepts/formato-webp|WebP]] como alternativa menor aos dois. Ícone em PNG "é um modelo mais arcaico"; logo de cliente em baixa definição se vetoriza no [[wiki/entities/figma]] com a Pen Tool ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## O que a aula não cobre

A parte 2 cita "carregamento sob demanda" como otimização de código e não detalha. `[skill: ux-ui-mentor]` Lazy loading (`loading="lazy"`, mas nunca na viewport inicial, onde piora o LCP), `aspect-ratio` para evitar CLS e hero image como LCP (< 2,5 s). Ver [[wiki/concepts/lazy-vs-eager-loading]].

## Edição "W7": tamanhos por dispositivo

A edição "W7" justifica pela acessibilidade (mobile, tablet, desktop) e manda exportar tamanhos diferentes e carregar "por Media Query lá no CSS"; o slide resume em "@1x, @2x, @3x" e cita o plugin TinyImage no Figma, que a fala não comenta ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]). Duas ressalvas: reduzir imagem no navegador não pixela, o custo é peso; e `[skill: ux-ui-mentor]` o "@2x" é densidade de pixel (`srcset` com descritor `x`), não tamanho de tela.

## Demonstração no Figma

Na prática "W7", o TinyImage Compressor tem um controle deslizante de qualidade para achar o "custo-benefício" entre peso e compressão; cuidado, porque na demo ele comprimiu todas as imagens de uma vez. Para exportar, ele põe a imagem ou o ícone dentro de um frame e exporta o frame (formato, escalas, preview) ([[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — parte 2: formato adequado como terceira maneira; Optimizilla e TinyPNG; carregamento sob demanda fica para o código
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": acessibilidade, media query, @1x/@2x/@3x; ressalva sobre "pixelada"
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — TinyImage no Figma para imagens e ilustrações
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — demo do TinyImage Compressor e export pelo frame
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG leve: ilustração do unDraw com 9KB, mockup exportado com 2KB
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — menos pontos no vetor = caminho SVG mais curto (nota do agente em [[wiki/concepts/vetorizacao-com-pen-tool]])
