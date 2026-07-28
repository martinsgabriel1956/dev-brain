---
type: concept
title: "Script async e defer"
aliases: ["async vs defer", "parser blocking script"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, javascript, async, defer, parser-blocking, rendering-pipeline]
skill: tech-mentor-frontend
status: draft
---
# Script async e defer

Quando o parser de HTML encontra uma tag `<script>` sem atributos especiais, ele **para de construir o [[wiki/concepts/dom]]** para baixar e executar o script — porque o script pode mutar o DOM (`document.write`, `appendChild`, `removeChild`) e o parser não tem como prever isso.

Enquanto o parser principal está bloqueado, o browser usa o **preload scanner**: um parser mais leve que escaneia o HTML adiante procurando recursos (imagens, stylesheets) e antecipa os downloads em paralelo, sem construir o DOM.

Dois atributos resolvem o bloqueio:
- **`async`**: baixa o script em paralelo, executa assim que o download termina — sem garantia de ordem entre múltiplos scripts.
- **`defer`**: baixa em paralelo, mas só executa depois que o DOM está completo, respeitando a ordem em que aparece no HTML. É o mais usado na maioria dos casos, já que roda depois do DOM pronto sem bloquear o parsing. `<script type="module">` se comporta como defer por padrão.

**Cadeia de bloqueio CSS → JS → HTML**: se um script acessa estilos computados (`getComputedStyle`), o browser precisa que o [[wiki/concepts/cssom]] esteja pronto antes de rodar o script — então CSS ainda carregando bloqueia JS síncrono, que bloqueia o parser de HTML.

**Eventos**: `DOMContentLoaded` dispara quando o HTML foi parseado e os scripts `defer` executaram (CSS/imagens podem ainda estar carregando); `load` só dispara quando tudo terminou de carregar (imagens, fontes, iframes).

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
