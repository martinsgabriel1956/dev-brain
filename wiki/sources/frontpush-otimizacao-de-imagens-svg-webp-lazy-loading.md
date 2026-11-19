---
type: source
title: "Otimização de imagens, parte 1: SVG, WebP e lazy loading (FrontPUSH)"
aliases: ["FrontPUSH otimização aula 03", "Otimização de Imagens pt.1", "módulo de otimização, aula 03"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 0
tags: [performance, web-performance, imagens, svg, webp, lazy-loading, compressao, vetorizacao, can-i-use, pagespeed, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-19
---

# Otimização de imagens, parte 1: SVG, WebP e lazy loading (FrontPUSH)

## TL;DR

Aula 03 do módulo de otimização do [[wiki/entities/frontpush|FrontPUSH]], cerca de 11,5 min. [[wiki/entities/nasser|Násser]] ("Ah, Násser, eu não sei como vetorizar") segue o post das "sete dicas" com a terceira: imagens. Três passos, na ordem:

- **Dá para vetorizar?** Logo, ilustração, ícone: [[wiki/concepts/formato-svg|SVG]], "é texto, texto é muito mais leve", estica sem perder resolução e "é manipulável pelo CSS". Demonstração: logo da Adidas buscado no Google e vetorizado pelo plugin Image Tracer do [[wiki/entities/figma|Figma]] ([[wiki/concepts/vetorizacao-com-pen-tool|ou na Pen Tool]]). Foto até "tem" como, em [[wiki/concepts/base64-encoding|base64]], mas fica "estrondoso de gigantesco".
- **Foto: comprimir e converter.** Passar PNG e JPG no "TinyImage, que é o do panda"; imagens "resolve coisa de 60%, 70%" da performance. Depois, [[wiki/concepts/formato-webp|WebP]], que o PageSpeed pede em "disponibilize imagens em formatos de última geração".
- **Carregar sob demanda.** O antigo: JavaScript medindo a distância da imagem ao topo e trocando o `src` vazio a ~1500 px. O de hoje: `loading="lazy"` em `<img>` e `<iframe>`, conferido no [[wiki/entities/can-i-use|Can I Use]]; "sai colocando essa clausulazinha em todas as tags". Demonstração na aba Network da página de energia solar (Solten): vídeos e PNGs chegam conforme o scroll ([[wiki/concepts/lazy-vs-eager-loading]]).
- **Anunciados:** imagem específica para mobile e desktop ("já já") e o site do drone, cheio de 3D em iframes e "tags viewers".

## Key Claims

- **Primeira pergunta: vetor.** "Primeira coisa que você tem que se perguntar, você tem como transformar isso aí em um vetor?" Logo, ilustração: "Vetorize, utiliza SVGs." Foto: "utiliza o PNG ou o JPG" e otimiza.
- **Foto em vetor não compensa.** "Até tem, mas às vezes você transforma em base64, não vale a pena, porque fica um código tão estrondoso de gigantesco."
- **Comprimir sempre.** No site "do panda", "você vai conseguir dropar os seus arquivos WebP, PNG ou JPG [...] e aí ele vai fazer a compressão para você". Erro comum: usar a imagem exportada do Figma sem otimizar nem adaptar para mobile e desktop ([[wiki/concepts/otimizacao-de-imagens]]).
- **Imagens são o grosso.** "Se você resolver isso aqui, já resolve coisa de 60%, 70%, de verdade." Evidência: experiência dele, sem medição.
- **SVG é leve, escalável e estilizável.** "São trechos de códigos que definem os elementos, cores e gradientes, ou seja, é texto"; "você pode esticar, ele não perde resolução"; "por ser código, ele é manipulável pelo CSS". "Eu sou da época que [...] eu utilizava PNG quando era ícone." ([[wiki/concepts/icones-em-interfaces]])
- **Image Tracer vetoriza um logo em segundos.** Logo da Adidas do Google Imagens: "Pei, transformei isso aqui de forma rápida, simples, maravilhosa [...] olha os pontinhos aí". Evidência: demonstração no Figma.
- **WebP é o melhor formato hoje.** "Que o melhor hoje em dia é o WebP"; "o próprio Google vai recomendar isso aí para você" no "Page Insights". Ele ainda está convertendo a página Solten num conversor online e diz que ainda não terminou ("eu falei ainda não").
- **Lazy loading antigo.** "A gente tinha que, literalmente, pedir para o JavaScript verificar a distância da imagem para o topo da página": tela de 1080 px, imagem a 2000 px; "renderizar com SRC vazio" e passar o caminho quando o scroll chegava "ali em 1500 pixels".
- **Lazy loading nativo.** "Você só vai aplicar o termo loading lazy nas suas imagens"; "Loading via attribute for images and iframes" no Can I Use, "que são as mais pesadas". "O browser vai fazer todo esse cálculo e vai ver se vale a pena carregar ou não." Aplicado na demonstração a "um determinado logo".
- **Para todas as imagens.** "Você faz isso, pessoal, para todas as imagens do seu site."
- **3D pede o mesmo cuidado.** O site do drone (nasseryousef.com.br/drone) vai "usar e abusar dos elementos 3D, utilizando de iframes ou então dos elementos viewers"; ele está "fazendo um estudo bem maior" de otimização para isso. Liga com [[wiki/entities/axlepush]] e [[wiki/entities/spline]].

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome; domínio nasseryousef.com.br.
- [[wiki/entities/frontpush]]: curso; aula 03 do módulo de otimização; remete às aulas de Figma.
- [[wiki/entities/figma]]: plugin Image Tracer e Pen Tool para vetorizar.
- [[wiki/entities/can-i-use]]: suporte do `loading="lazy"`.
- [[wiki/entities/google]]: PageSpeed Insights recomenda formatos modernos.
- [[wiki/entities/axlepush]], [[wiki/entities/spline]]: o site do drone com 3D.

## Concepts

- [[wiki/concepts/otimizacao-de-imagens]]: a ordem vetor → compressão → formato → sob demanda.
- [[wiki/concepts/formato-svg]]: texto, escalável, estilizável.
- [[wiki/concepts/formato-webp]], [[wiki/concepts/formato-heic-avif]]: formatos modernos.
- [[wiki/concepts/formato-png]], [[wiki/concepts/formato-jpeg]]: os formatos a substituir.
- [[wiki/concepts/base64-encoding]]: a "foto em vetor".
- [[wiki/concepts/vetorizacao-com-pen-tool]]: vetorizar à mão.
- [[wiki/concepts/lazy-vs-eager-loading]]: `loading="lazy"`.
- [[wiki/concepts/core-web-vitals]]: LCP e CLS, que o lazy loading mal aplicado piora.
- [[wiki/concepts/design-responsivo]]: imagem por dispositivo, anunciada.
- [[wiki/concepts/icones-em-interfaces]]: ícone em SVG, não em PNG.
- [[wiki/concepts/compatibilidade-entre-navegadores]]: conferir no Can I Use.

## Precisões e tensões com a wiki

- **Base64 não vetoriza.** Converter uma foto em base64 só escreve o mesmo bitmap como texto (dentro de um SVG ou de um `data:`), cerca de 33% maior e sem cache próprio. Vetorizar foto é outra coisa: um tracer aproxima a foto em milhares de formas, perde detalhe e fica pesado. As duas não compensam, por motivos diferentes ([[wiki/concepts/base64-encoding]]). Confiança alta.
- **SVG nem sempre é mais leve.** É texto, mas o tamanho depende da quantidade de pontos. Um tracer gera mais pontos que o necessário; um SVG traçado de imagem complexa pode pesar mais que um WebP. Passar o SVG por um otimizador (SVGO, SVGOMG) e servir com gzip/brotli. Para logo de marca, o melhor é o SVG oficial, que é exato e leve (e uso de marca tem regras próprias). `[skill: tech-mentor-frontend]` Confiança alta.
- **"Manipulável pelo CSS" só inline.** O CSS da página estiliza o SVG quando ele está no HTML (`<svg>` inline ou `<use>`). Num `<img src="logo.svg">` o SVG é uma imagem fechada: o CSS de fora não alcança `fill` e `stroke`. Confiança alta.
- **"60%, 70%".** Imagens costumam ser a maior fatia dos bytes de uma página, segundo o Web Almanac do HTTP Archive; a porcentagem exata varia por site, e "performance" não é só bytes (JavaScript pesa mais no INP). Leia como ordem de grandeza (sem fetch nesta sessão). Confiança média.
- **"O do panda" é o TinyPNG.** O mascote panda é do tinypng.com, que hoje comprime PNG, JPEG, WebP e AVIF. Na wiki, "TinyImage" é o nome usado nas aulas de UI para o plugin do Figma ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]]); a fala desta aula provavelmente mistura os dois. Confiança média.
- **WebP não é mais "o melhor".** AVIF comprime mais que WebP e tem suporte nos navegadores atuais ([[wiki/concepts/formato-heic-avif]]). O padrão robusto é `<picture>` com AVIF, WebP e JPEG de reserva, ou um serviço/framework que negocia o formato (Next.js Image, CDNs de imagem). `[skill: tech-mentor-frontend]` Converter um a um em site online, como na aula, funciona mas não escala; o build ou a CDN fazem sozinhos. Confiança alta.
- **A auditoria mudou de nome.** "Disponibilize imagens em formatos de última geração" (Serve images in next-gen formats) é a auditoria antiga do Lighthouse; as versões de 2025 juntaram as de imagem num insight único de entrega de imagens (inferência por conhecimento prévio, sem fetch). Confiança média.
- **Não é para "todas as imagens".** Lazy loading na imagem que aparece na primeira tela atrasa o LCP, porque o navegador espera o layout para decidir baixar. A própria demonstração aplica `loading="lazy"` "a um determinado logo", que costuma estar no topo. Regra: `loading="lazy"` abaixo da dobra; a imagem principal acima da dobra sem lazy e com `fetchpriority="high"` ([[wiki/concepts/core-web-vitals]]). `[skill: tech-mentor-frontend]` Confiança alta.
- **Faltam `width` e `height`.** Imagem lazy sem dimensões ocupa 0 px até chegar e empurra o conteúdo (CLS). Com `width` e `height` (ou `aspect-ratio`), o espaço fica reservado. Confiança alta.
- **O browser decide a distância, mas não "se vale a pena".** O Chrome começa a baixar a imagem lazy antes de ela entrar na tela, a uma distância que depende da conexão (cerca de 1250 px em 4G e 2500 px em redes lentas, segundo o web.dev; sem fetch nesta sessão). Confiança média.
- **O jeito antigo tinha meio-termo.** Entre medir `offsetTop` no evento de scroll e o atributo nativo, houve o `IntersectionObserver` (2016–2019), que avisa quando o elemento se aproxima da tela sem calcular no scroll. Ainda é o caminho para lazy de fundo em CSS, de vídeo e de componentes. Confiança alta.
- **`loading` não vale para `<video>`.** O atributo só existe em `<img>` e `<iframe>`. Os vídeos que "carregaram agora" na demonstração usam outro mecanismo (JavaScript, `preload="none"` ou biblioteca); a aula não mostra qual. Confiança alta.
- **"Está sendo implementado".** O Chrome tem desde 2019 e o Firefox desde 2020; o Safari, desde 2022 em imagens e 2023 em iframes. Hoje é suporte amplo (Baseline). Confiança alta.
- **"Page Insights"** é o PageSpeed Insights das aulas anteriores ([[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]).
- **"Solten" e o endereço da aula 01.** O site de energia solar se chama Solten (ou Solstheim, na legenda), e o domínio do instrutor é nasseryousef.com.br. O "nasausef.com.br.sosten" ilegível da aula 01 provavelmente é nasseryousef.com.br/solten (inferência). Confiança média.

## Open Questions

- "A NASA não tem como fazer otimização": provável "Ah, não, se não tem como [...]" ou "Ah, nossa"; deixado literal.
- "Elementos viewers, das tags viewers": provável `<model-viewer>` do Google, já citado na wiki ([[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]); a aula não mostra.
- Como os vídeos da página Solten são carregados sob demanda? Ver próximas aulas.
- **Respondida em [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]:** a parte 2 faz imagem por dispositivo com classes e `display: none`, sem `srcset`, `sizes` nem `<picture>`.

## Raw quotes

- "isso aqui a gente dá para transformar em um vetor?"
- "fica um código tão estrondoso de gigantesco"
- "se você resolver isso aqui, já resolve coisa de 60%, 70%"
- "é texto, texto é muito mais leve"
- "Eu utilizava PNG quando era ícone."
- "Hoje em dia, mão na roda."
- "Sai colocando essa clausulazinha em todas as tags de imagem"
