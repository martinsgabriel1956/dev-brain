---
type: concept
title: "Critical Rendering Path"
aliases: ["pipeline de renderização do browser", "caminho crítico de renderização", "URL para pixel"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
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

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
