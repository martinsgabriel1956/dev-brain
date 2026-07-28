---
type: concept
title: "Layout Thrashing"
aliases: ["forced synchronous layout"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [browser, layout-thrashing, performance, reflow, javascript]
skill: tech-mentor-frontend
status: draft
---
# Layout Thrashing

Padrão de código que força [[wiki/concepts/reflow-layout|reflow]] síncrono repetido: ler uma propriedade de geometria (ex. `el.offsetHeight`) e escrever um estilo alternadamente, dentro de um loop, sobre múltiplos elementos. Cada leitura força o browser a recalcular o layout pendente antes de responder, porque o valor lido depende da geometria atualizada.

```js
// ❌ Layout thrashing: lê e escreve alternadamente
elements.forEach(el => {
    const height = el.offsetHeight; // LEITURA → força reflow
    el.style.height = height + 10 + 'px'; // ESCRITA
});

// ✅ Separar leituras de escritas em fases
const heights = elements.map(el => el.offsetHeight); // Fase 1: todas as leituras
elements.forEach((el, i) => el.style.height = heights[i] + 10 + 'px'); // Fase 2: escritas
```

Correção: separar a fase de leitura da fase de escrita, batendo todas as leituras primeiro (um único reflow) e depois todas as escritas.

Fonte: extensão `[skill: tech-mentor-frontend]` do raciocínio sobre custo de reflow descrito em [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] — a fonte original explica o mecanismo do reflow mas não nomeia o anti-padrão; confirmado por `references/frontend-performance-deep.md` e `references/frontend-devtools.md` da skill.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
