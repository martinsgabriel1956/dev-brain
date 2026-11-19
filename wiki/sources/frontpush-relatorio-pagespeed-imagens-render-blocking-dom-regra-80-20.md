---
type: source
title: "Relatório do Google PageSpeed: imagens, render-blocking, payload, fontes, DOM e a regra 80-20 (FrontPUSH)"
aliases: ["FrontPUSH otimização aula 06", "Relatório Google Page Speed", "módulo de otimização, aula 06", "PageSpeed parte 2"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 0
tags: [performance, pagespeed, lighthouse, diagnosticos, imagens, webp, avif, render-blocking, defer, network-payload, video, font-display, dom-size, svg, pareto, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-19
---

# Relatório do Google PageSpeed: imagens, render-blocking, payload, fontes, DOM e a regra 80-20 (FrontPUSH)

## TL;DR

Aula 06 do módulo de otimização do [[wiki/entities/frontpush|FrontPUSH]], cerca de 4,5 min. É a segunda das duas aulas sobre o PageSpeed Insights (a primeira é [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags|a aula 05]]). [[wiki/entities/nasser|Násser]] diz o próprio nome numa pergunta retórica. Ele lê os avisos de diagnóstico do relatório, "bater em teclas das quais eu já falei":

- **Formatos de última geração:** "ele quer em WebP, ele não quer em PNG e JPEG"; a ferramenta cita "WebP ou AVIF" ([[wiki/concepts/formato-webp]], [[wiki/concepts/formato-heic-avif]]).
- **Tamanho adequado:** "4K num celular de resolução 320p", o assunto da aula 04 ([[wiki/concepts/otimizacao-de-imagens]]).
- **Recursos que impedem a renderização:** ele explica como "JavaScript que não tá sendo utilizado" e que bloqueia a "primeira exibição". A recomendação é deixar só o JS e o CSS críticos e jogar o resto "lá pra baixo" ([[wiki/concepts/critical-rendering-path]]).
- **Payloads de rede muito grandes:** "as áreas mais vermelhas são fotos e vídeos".
- **Texto visível:** "um probleminha aqui de acessibilidade". Na verdade é o carregamento de [[wiki/concepts/webfonts]].
- **DOM muito grande:** muitos ícones, "um SVG que está com mil camadas de gradiente" ([[wiki/concepts/dom]], [[wiki/concepts/formato-svg]], [[wiki/concepts/icones-em-interfaces]]).
- **Regra 80-20:** "você consegue resolver 80% das coisas fazendo 20%", e "grande parte disso é mídia". O resto rende "30 milissegundos" e "não vale a pena mais" ([[wiki/concepts/principio-de-pareto]]).

## Key Claims

- **O relatório repete o que já foi dito.** "Eu só vou estar comprovando pra vocês o que que o Google tá querendo dizer pra gente." Cada aviso traz "uma breve descrição e um link pra poder você ler mais".
- **Formato de última geração é WebP.** "Traduzindo, ele quer em WebP, ele não quer em PNG e JPEG." E: "WebP ou AVIF costuma ter uma compensação melhor, por favor, transforme todas essas imagens".
- **Resolução maior que a tela é desperdício.** "Eu detectei que aqui é uma resolução muito grande, que tá sendo carregada pro celular sem necessidade. Tá com uma resolução, sei lá, 4K num celular de resolução 320p."
- **Render-blocking é JavaScript sem uso na primeira exibição.** "Quando tem algum JavaScript que não tá sendo utilizado, que ele verificou que estão bloqueando a primeira exibição da sua página"; "inclua somente um JavaScript, um CSS que seja crítico"; "se não for crítico, você joga esse JavaScript lá pra baixo".
- **Payload grande é foto e vídeo.** "Coloquei alguns vídeos, mais algumas fotos. Você tá vendo que as áreas mais vermelhas são fotos e vídeos, tá? Sempre assim."
- **Texto visível é acessibilidade.** "Garanta que o texto continue visível. Então, um probleminha aqui de acessibilidade." Ele não explica o aviso.
- **DOM grande vem de ícones e SVG.** "Geralmente quando a gente utiliza de muitos ícones dentro de uma página, ele reclama disso"; "um SVG que está com mil camadas de gradiente [...] Ele vê aquele tanto de elementos na árvore DOM".
- **Seguindo as práticas do curso, "vai ficar quase nada"** no relatório.
- **80-20 e retorno decrescente.** "Você consegue resolver 80% das coisas fazendo 20%. Grande parte disso é mídia"; outras práticas rendem "30 milissegundos", "chega um ponto que você fazer esse tanto de coisa não vale a pena mais". Mas é bom conhecê-las para "saber pesar". A próxima aula comenta os artigos de otimização (o Notion da [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin|aula 04]]).

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome ("Ah, Násser, eu tenho mais dúvidas").
- [[wiki/entities/frontpush]]: curso; aula 06 do módulo de otimização.
- [[wiki/entities/google]]: PageSpeed Insights e os avisos do Lighthouse.

## Concepts

- [[wiki/concepts/core-web-vitals]]: os avisos são diagnósticos; LCP, CLS e INP não aparecem pelo nome.
- [[wiki/concepts/otimizacao-de-imagens]], [[wiki/concepts/formato-webp]], [[wiki/concepts/formato-heic-avif]]: formato e tamanho.
- [[wiki/concepts/critical-rendering-path]]: recursos que bloqueiam a renderização, `defer`/`async`.
- [[wiki/concepts/code-splitting]]: o "JavaScript não utilizado", que é outro aviso.
- [[wiki/concepts/webfonts]]: `font-display` e o texto invisível.
- [[wiki/concepts/acessibilidade]]: a categoria a que o aviso de fonte *não* pertence.
- [[wiki/concepts/dom]], [[wiki/concepts/formato-svg]], [[wiki/concepts/icones-em-interfaces]]: tamanho da árvore.
- [[wiki/concepts/lazy-vs-eager-loading]]: vídeo pesado fora da dobra.
- [[wiki/concepts/principio-de-pareto]]: a regra 80-20 aplicada à performance.

## Precisões e tensões com a wiki

- **Render-blocking não é "JavaScript não utilizado".** São dois avisos diferentes no Lighthouse. "Eliminar recursos que impedem a renderização" lista o `<link rel="stylesheet">` e o `<script>` síncrono no `<head>`, usados ou não, porque o navegador para de pintar até baixá-los. Já "Reduza o JavaScript não usado" mede bytes que nunca executam (resolve-se com [[wiki/concepts/code-splitting]] e [[wiki/concepts/tree-shaking]]). Um script 100% usado ainda bloqueia se não tiver `defer`. Confiança alta.
- **"Jogar lá pra baixo" é a técnica antiga; `defer` é a atual.** Um `<script>` no fim do `<body>` só começa a baixar quando o parser chega nele. Com `<script defer>` no `<head>`, o download corre em paralelo com o parse e a execução vem depois, na ordem do documento. `async` serve para scripts independentes (analytics). `type="module"` já é `defer`. É a mesma discussão da NLW #2, dia 3 ([[wiki/concepts/critical-rendering-path]]). Confiança alta.
- **CSS também bloqueia, e a saída é outra.** Não dá para "jogar o CSS para baixo" sem causar flash de conteúdo sem estilo. A receita é CSS crítico inline e o resto carregado sem bloquear (com `media` que não casa e é trocado depois, ou `rel="preload"`), mais `media="print"` e similares para folhas condicionais. É o contraponto da [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo|aula 02]]. Confiança alta.
- **"Texto continue visível" é webfont, não acessibilidade.** O aviso ("Ensure text remains visible during webfont load") fica na categoria de desempenho. Ele aparece quando uma `@font-face` usa o padrão do navegador: o texto fica invisível até a fonte chegar (FOIT, até cerca de 3 s). A correção é `font-display: swap` (mostra a fonte de reserva e troca) ou `optional` (troca só se chegar a tempo; evita o pulo de layout). No Google Fonts basta `&display=swap` na URL ([[wiki/concepts/webfonts]]). Texto invisível atrapalha qualquer pessoa, mas não é auditoria do axe-core. Confiança alta.
- **Limites de DOM do Lighthouse.** O aviso aparece acima de cerca de 800 nós no `<body>` e falha acima de cerca de 1.400. Também acusa profundidade acima de 32 níveis e mais de 60 filhos num nó (por conhecimento prévio, sem fetch; confiança média-alta). O custo não é de download: cada nó pesa no cálculo de estilo, no layout e na memória, e atrasa interações (INP) ([[wiki/concepts/dom]]).
- **SVG só entra no DOM se for inline.** Cada `<path>`, `<g>` e `<stop>` de gradiente de um SVG colado no HTML vira nó. O mesmo arquivo em `<img src="icone.svg">` ou em `background-image` é um nó só. Para muitos ícones repetidos, um sprite com `<symbol>` + `<use>` evita repetir o markup. Otimizar com SVGO também corta camadas ([[wiki/concepts/formato-svg]], [[wiki/concepts/icones-em-interfaces]]). Confiança alta para `<img>`; média para a contagem de `<use>` pelo Lighthouse.
- **Payload: o limite e o vídeo.** O Lighthouse avisa quando o total transferido passa de cerca de 5.000 KiB (sem fetch; confiança média). Vídeo é o caso que mais pesa e que o curso ainda não tratou. Ajudam `preload="none"` ou `metadata` com `poster`, compressão (H.264/VP9/AV1), troca de GIF por vídeo, e carregar vídeo fora da dobra por `IntersectionObserver`, porque `loading="lazy"` não vale para `<video>` (já anotado na [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading|aula 03]]; [[wiki/concepts/lazy-vs-eager-loading]]). Confiança alta.
- **AVIF apareceu, lido da ferramenta.** Na aula 03 o AVIF não foi citado ([[wiki/concepts/formato-heic-avif]]); aqui ele só lê "WebP ou AVIF" do relatório e segue pedindo WebP. AVIF costuma comprimir mais que WebP, com `<picture>` e WebP/JPEG de reserva. "Compensação melhor" é a tradução do Google para *compression*. Confiança alta.
- **"4K num celular 320p" é exagero ilustrativo.** Celular não tem "320p": o viewport CSS fica em 360–430 px e a tela física passa de 1.000 px de largura (densidade 2–3×). A auditoria compara os pixels da imagem com o tamanho exibido × densidade, e a resposta é `srcset`/`sizes` ([[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin|aula 04]]). Confiança alta.
- **Os nomes dos avisos mudaram.** Desde as versões de 2024–2025 o Lighthouse e o PageSpeed passaram a mostrar "insights" no lugar das auditorias antigas: formato, tamanho e compressão de imagem viraram um só, "Melhorar a entrega de imagens"; render-blocking virou "Solicitações que bloqueiam a renderização" (sem fetch; confiança média). A aula mostra a interface anterior.
- **80-20 é heurística, e mídia é bytes, não tudo.** Mídia é a maior fatia de *bytes* na mediana do HTTP Archive (Web Almanac; sem fetch; confiança média), por isso domina LCP e payload. Mas o JavaScript pesa mais em *CPU*: em celular lento, os "30 milissegundos" do laboratório viram centenas no campo e pesam no INP. O retorno decrescente vale para landing pages, o foco do curso; em web app o gargalo costuma ser JS ([[wiki/concepts/principio-de-pareto]]). Confiança alta.
- **A aula 05 perguntava se LCP, CLS e INP apareceriam pelo nome.** Não aparecem: a aula só lê os avisos de diagnóstico, que alimentam essas métricas sem nomeá-las ([[wiki/concepts/core-web-vitals]]).
- **ASR:** "Nassa" virou Násser.

## Open Questions

- Que página está no relatório? Ela tem vídeos e fotos pesados; talvez o site do drone ([[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading|aula 03]]) ou a Solten.
- Quais artigos a aula 07 vai comentar? Provavelmente os do Notion ("11 dicas, 35 dicas, 8"), citados na aula 04.
- O curso vai tratar de `defer`/`async` e de vídeo em algum momento, ou para no "joga lá pra baixo"?

## Raw quotes

- "Traduzindo, ele quer em WebP, ele não quer em PNG e JPEG."
- "4K num celular de resolução 320p"
- "um SVG que está com mil camadas de gradiente"
- "você consegue resolver 80% das coisas fazendo 20%"
- "saber pesar essas características"
