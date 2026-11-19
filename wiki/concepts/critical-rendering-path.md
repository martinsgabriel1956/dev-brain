---
type: concept
title: "Critical Rendering Path"
aliases: ["pipeline de renderização do browser", "caminho crítico de renderização", "URL para pixel"]
date_created: 2026-07-28
date_updated: 2026-11-19
source_count: 8
tags: [browser, rendering-pipeline, critical-rendering-path, performance, dom, cssom]
skill: tech-mentor-frontend
status: draft
---
# Critical Rendering Path

Sequência de etapas que o browser executa entre receber a URL e pintar o primeiro pixel na tela. Duas fases: rede (cache → [[wiki/concepts/dns]] → [[wiki/concepts/tcp-three-way-handshake]] → [[wiki/concepts/tls-handshake]] → request/response HTTP) e renderização (HTML→[[wiki/concepts/dom]], CSS→[[wiki/concepts/cssom]], combinação em [[wiki/concepts/render-tree]], [[wiki/concepts/reflow-layout|layout]], [[wiki/concepts/paint-composite|paint e composite]]).

## Fase de rede

1. **Cache**: se a página já foi visitada e o cache é válido, o browser pula toda a navegação de rede.
2. **DNS**: resolve o domínio para IP.
3. **TCP**: handshake de três vias (SYN → SYN-ACK → ACK) abre a conexão.
4. **TLS** (se HTTPS): negociação de certificados/chaves adiciona round trips antes do primeiro byte.
5. **HTTP**: `GET` da página, resposta com o documento HTML.

## Fase de renderização

O HTML e o CSS passam por pipelines de parsing paralelos e simétricos (bytes → caracteres → tokens → nós → árvore), gerando DOM e CSSOM respectivamente. As duas árvores são combinadas na render tree (só nós visíveis), que alimenta o layout (geometria) e depois o paint (pixels) e composite (GPU combina camadas).

CSS é bloqueante para renderização: nada é pintado até o CSSOM estar completo, para evitar FOUC (flash of unstyled content). JavaScript síncrono bloqueia o parser de HTML, porque o parser não sabe se o script vai mutar o DOM — ver [[wiki/concepts/script-async-defer]].

## Por que otimizações clássicas funcionam

Cada otimização ataca uma etapa específica do pipeline:
- Minificar HTML/CSS → reduz tempo de parsing.
- `defer` nos scripts → evita bloqueio do parser.
- CSS raso (seletores simples) → acelera layout.
- `transform`/`opacity` em vez de `top`/`left`/`width` → pula layout e paint, vai direto pro compositing.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], o `<script>` no começo do body falha porque o HTML é lido "linha a linha" e o elemento ainda não existe; no head, `defer` resolve para scripts externos. Ver [[wiki/concepts/carregamento-de-scripts]].

## CSS num arquivo só (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-import-e-partials-sass]], o Sass junta os arquivos num `style.css`. `[skill: tech-mentor-frontend]` Como CSS bloqueia a renderização, o que pesa é o tamanho do CSS necessário para a primeira tela e evitar `@import` nativo (download em série), não só o número de arquivos. Ver [[wiki/concepts/import-e-partials-sass]].

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o painel Elements é apresentado como "a árvore DOM de elementos" com HTML, estilos e layout; são etapas diferentes deste pipeline (DOM, CSSOM, layout) mostradas na mesma tela.

## CSS e JS do head primeiro (FrontPUSH, otimização aula 01)

Em [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]], na aba Network, os primeiros arquivos são o CSS e o JS do head: o browser "vai dar prioridade para o style.css, para o JavaScript" para não mostrar "aquele site todo quebrado". É o CSS bloqueando a renderização (e o script sem `defer` bloqueando o parser), sem o nome. Por isso um CSS único gigante atrasa o FCP ([[wiki/concepts/core-web-vitals]]).

## CSS crítico inline × "evite incorporado" (FrontPUSH, otimização aula 02)

Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], a regra é evitar CSS inline e incorporado porque não cacheia. Tensão: o bloco `<style>` com o CSS crítico no `<head>` é técnica recomendada, porque tira a requisição bloqueante da primeira tela; o resto vai num arquivo externo cacheável. O que a aula condena com razão é o atributo `style=""` espalhado e o código acumulado por geradores e page builders.

## Recursos que bloqueiam a renderização (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]], o aviso é explicado como "JavaScript que não tá sendo utilizado" e resolvido jogando o JS "lá pra baixo". No Lighthouse são dois avisos: render-blocking é todo `<link rel="stylesheet">` e `<script>` síncrono no `<head>`, usado ou não; código sem uso é outro aviso ([[wiki/concepts/code-splitting]]). Para JS, `defer` no `<head>` supera o fim do `<body>` (baixa em paralelo, executa na ordem); para CSS, CSS crítico inline e o resto sem bloquear.

## Pipeline por quadro na animação (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], o mesmo pipeline aparece por quadro: estilo, layout, pintura e composição (falta a etapa de JavaScript antes). Cada mudança só refaz as etapas a partir da que afeta ([[wiki/concepts/taxa-de-quadros-60fps]]).

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: script no começo do body x defer
- [[wiki/sources/frontpush-import-e-partials-sass]]: Sass: um CSS só × CSS crítico
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: DOM, estilos e layout no painel Elements
- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: FrontPUSH, otimização aula 01: CSS e JS do head chegam primeiro
- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: CSS crítico inline como contraponto
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: render-blocking × JS sem uso; `defer` × fim do body
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: pipeline a cada quadro de animação
