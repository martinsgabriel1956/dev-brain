---
type: source
title: "Browser Security"
aliases: ["browser security", "csp", "cors", "same-origin policy", "spectre browser", "fetch metadata", "coep coop"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/browser-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [browser-security, csp, cors, same-origin-policy, spectre, fetch-metadata, coep, coop, xss, csrf]
skill: tech-mentor-security
status: stable
---

## TL;DR

Browser Security: Same-Origin Policy é a base (scheme+host+port). CORS habilita cross-origin controlado. CSP com nonces previne XSS mesmo após injeção. COEP + COOP habilitam `SharedArrayBuffer` e isolamento cross-origin (mitiga Spectre). SameSite=Strict elimina CSRF. Fetch Metadata (`Sec-Fetch-*`) permite rejeitar requests não esperados no servidor.

## Key Claims

**Claim:** CSP com `strict-dynamic` + nonces é mais robusto que allowlists de URLs — nonces mudam por request.
**Evidence:** Allowlist de domínios (`script-src https://cdn.example.com`) pode ser bypassada se o CDN aceitar uploads. `strict-dynamic` com nonce: apenas scripts com `nonce="abc123"` executam; o nonce é gerado pelo servidor a cada request, impossível de prever. Elimina XSS mesmo com injeção de tags `<script>`.
**Confidence:** alta

**Claim:** COEP + COOP são obrigatórios para usar `SharedArrayBuffer` e habilitam isolamento cross-origin real.
**Evidence:** `Cross-Origin-Embedder-Policy: require-corp` + `Cross-Origin-Opener-Policy: same-origin`: navegador coloca a página em processo isolado, mitigando Spectre (timing side-channel). Requisito para `SharedArrayBuffer`, `performance.measureUserAgentSpecificMemory()`, e precisão de `performance.now()`.
**Confidence:** alta

**Claim:** Fetch Metadata permite rejeitar requests não esperados no servidor antes de processar.
**Evidence:** `Sec-Fetch-Site: cross-site`, `Sec-Fetch-Mode: navigate`, `Sec-Fetch-Dest: document`. Servidor pode rejeitar: "se `Sec-Fetch-Site` é `cross-site` e `Sec-Fetch-Mode` é `no-cors`, rejeita com 403". Defesa em profundidade contra CSRF, clickjacking e requests maliciosos não esperados.
**Confidence:** alta

**Claim:** SameSite=Strict elimina CSRF mas pode quebrar fluxos legítimos de login via link externo.
**Evidence:** Cookie com `SameSite=Strict` não é enviado em requests cross-site, incluindo navegação por link. Usuário clica em link no email → abre o site → cookie não enviado → não está logado. Trade-off: `SameSite=Lax` (default) envia apenas em GET de top-level navigation — proteção parcial mas sem quebrar UX.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/same-origin-policy]]
- [[concepts/csp]]
- [[concepts/cors]]
- [[concepts/coep-coop]]
- [[concepts/fetch-metadata]]
- [[concepts/xss]]
- [[concepts/csrf]]
- [[concepts/spectre-meltdown]]

## Open Questions

- CSP em SPAs com código dinâmico (eval, templates) — como implementar sem `unsafe-eval`?
- COEP com iframes de terceiros (Stripe, Google Maps) — como compatibilizar com isolamento cross-origin?
