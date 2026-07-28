---
type: source
title: "Pipeline de Renderização do Browser — da URL ao Pixel"
aliases: ["critical rendering path", "browser rendering pipeline", "URL para pixel"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/pipeline-de-renderizacao-do-browser-url-ate-pixel.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [browser, rendering-pipeline, dns, tcp, tls, dom, cssom, render-tree, layout, reflow, paint, composite, critical-rendering-path, javascript-blocking, async, defer]
skill: tech-mentor-frontend
status: stable
---

## TL;DR

Entre apertar enter numa URL e o primeiro pixel aparecer, o browser passa por seis fases: (1) cache check, (2) resolução DNS, (3) handshake TCP de três vias, (4) handshake TLS (se HTTPS), (5) request/response HTTP, (6) transformação do HTML recebido em pixels na tela via um pipeline de parsing em duas frentes (HTML→DOM, CSS→CSSOM) que convergem na render tree, passam por layout (reflow) e paint, e terminam em composite na GPU. O JavaScript pode interromper esse pipeline porque o parser não sabe se um `<script>` vai mutar o DOM — daí `async`/`defer` existirem. Cada otimização de performance clássica (minificar HTML/CSS, `defer`, CSS raso, `transform`/`opacity` em animações) ataca uma etapa específica desse pipeline.

## Key Claims

**Claim:** O browser só inicia a navegação de rede se a página não estiver em cache válido; havendo cache válido, ele pula DNS/TCP/TLS/HTTP inteiramente.
**Evidence:** Descrito como primeira checagem antes de qualquer etapa de rede — "se essa página já foi visitada e o cache ainda é válido, o browser pula tudo e usa a versão salva, sem precisar de rede nem espera".
**Confidence:** alta — consistente com o comportamento documentado de HTTP caching (Cache-Control, ETag) e bfcache descrito em `references/frontend-performance-deep.md` (skill `tech-mentor-frontend`), embora a fonte não distinga cache HTTP normal de bfcache.

**Claim:** A conexão TCP usa handshake de três vias (SYN → SYN-ACK → ACK) e, se HTTPS, o TLS adiciona round trips extras de negociação de certificado/chave antes do primeiro request HTTP.
**Evidence:** Sequência descrita explicitamente na fonte e confirmada pela waterfall documentada na skill: `DNS → TCP → TLS → HTTP Request → Server processing → First Byte (TTFB)` (`references/frontend-performance-deep.md`, seção "DOMContentLoaded vs FCP vs LCP — Waterfall").
**Confidence:** alta

**Claim:** O parsing de HTML é incremental (o browser constrói o DOM conforme os bytes chegam, sem esperar o documento inteiro) e tolerante a erros (tags não fechadas são fechadas automaticamente; nunca falha).
**Evidence:** Explica por que páginas grandes "renderizam de cima para baixo". Não há refutação disso na skill consultada; é comportamento padrão de parsers de HTML5 (error-recovery é parte da spec do HTML5 parsing algorithm), tratado aqui como conhecimento de base do domínio.
**Confidence:** alta

**Claim:** O CSSOM é bloqueante para renderização — o browser não pinta nada até o CSSOM estar completo, para evitar renderizar HTML sem estilo e depois redesenhar tudo (evitar FOUC).
**Evidence:** Alinhado ao conceito de "render-blocking CSS" citado implicitamente na waterfall da skill (`CSS download + Parse → Render Blocking resolved → First Contentful Paint`).
**Confidence:** alta

**Claim:** A render tree só contém nós visíveis — `display: none`, `<head>` e `<script>` ficam de fora, mas `visibility: hidden` entra (ocupa espaço, só não é pintado).
**Confidence:** alta — distinção clássica e correta entre as duas propriedades CSS.

**Claim:** Mudanças de CSS têm custo hierárquico: alterar layout (ex. `width`) dispara reflow; alterar aparência sem geometria (ex. `color`) dispara só repaint; alterar `transform`/`opacity` vai direto para compositing, sem reflow nem repaint — por isso são as propriedades recomendadas para animação performática.
**Evidence:** Confirmado quase literalmente pela skill em `references/frontend-performance-deep.md`: `transform: translateX(0)` e `opacity: 1` comentados como "GPU: sem reflow", enquanto `left`, `top`, `width` são marcados como "provoca reflow" na mesma seção ("Animações que só usam compositor").
**Confidence:** alta

**Claim:** Ler propriedades de layout (ex. `offsetHeight`) dentro de um loop que também escreve estilos força reflow síncrono repetido ("layout thrashing"); a correção é separar todas as leituras de todas as escritas em fases.
**Evidence:** Não estava explícito na transcrição original, mas é a consequência direta do modelo de reflow que ela descreve — confirmado e detalhado pela skill em `references/frontend-performance-deep.md` (seção "Avoid Forced Synchronous Layout (Layout Thrashing)") e `references/frontend-devtools.md`. Adicionado aqui como extensão `[skill: tech-mentor-frontend]` do raciocínio da fonte.
**Confidence:** alta

**Claim:** O parser de HTML para ao encontrar `<script>` (sem `async`/`defer`) porque o script pode mutar o DOM via `document.write`, `appendChild`, `removeChild`; `async` baixa e executa assim que pronto (sem ordem garantida), `defer` baixa em paralelo mas executa só após o DOM completo, na ordem do documento — e é o mais recomendado na maioria dos casos.
**Evidence:** Consistente com `references/frontend-devtools.md`, que lista `<script defer>` ou `<script type="module">` (que é defer por padrão) como prática recomendada para não bloquear o parser.
**Confidence:** alta

**Claim:** Existe uma cadeia de bloqueio CSS → JS → HTML: se um script acessa estilos computados (`getComputedStyle`), o browser precisa que o CSSOM esteja pronto antes de rodar o script, e o script (se não for async/defer) bloqueia o parser de HTML — logo, CSS ainda carregando pode atrasar indiretamente o parsing do HTML.
**Confidence:** média-alta — mecanismo coerente com o funcionamento de CSSOM/scripts síncronos, mas a fonte não cita esse encadeamento com uma referência formal (é uma consequência lógica bem conhecida do critical rendering path, não uma medição).

**Claim:** `DOMContentLoaded` dispara quando o HTML foi parseado e os scripts `defer` executaram (CSS/imagens podem ainda estar carregando); `load` só dispara quando absolutamente tudo carregou (imagens, fontes, iframes).
**Evidence:** Confirmado literalmente pela skill: "DOMContentLoaded: Quando o HTML foi parseado e DOM está pronto. CSS e imagens ainda podem estar carregando. NÃO é métrica de performance de usuário" (`references/frontend-performance-deep.md`).
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/dns]]
- [[wiki/concepts/tcp-three-way-handshake]]
- [[wiki/concepts/tls-handshake]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/cssom]]
- [[wiki/concepts/render-tree]]
- [[wiki/concepts/critical-rendering-path]]
- [[wiki/concepts/reflow-layout]]
- [[wiki/concepts/paint-composite]]
- [[wiki/concepts/script-async-defer]]
- [[wiki/concepts/layout-thrashing]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/http-caching]]

## Open Questions

- A fonte não distingue cache HTTP comum (Cache-Control/ETag) de bfcache (back/forward cache) — ambos aparecem sob o rótulo genérico "cache". Vale uma página dedicada a bfcache já que a skill tem material rico sobre isso (`references/frontend-performance-deep.md`, seção bfcache) para diferenciar dos dois mecanismos.
- A fonte não menciona HTTP/2 ou HTTP/3 (multiplexing, QUIC) nem preconnect/prefetch como otimizações adicionais às citadas — possível ângulo complementar para uma fonte futura.
- Não há menção a Web Workers ou main thread scheduling (`scheduler.yield`, INP) — a cadeia de bloqueio descrita é toda single-thread; útil conectar com [[wiki/concepts/inp-interaction-to-next-paint]] se essa página existir.

## Fontes Relacionadas

_(nenhuma fonte anterior na wiki cobre o pipeline DOM/CSSOM/render tree/layout/paint/composite — esta é a primeira fonte sobre o critical rendering path do browser.)_
