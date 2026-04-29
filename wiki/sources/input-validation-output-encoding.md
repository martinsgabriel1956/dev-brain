---
type: source
title: "Input Validation & Output Encoding"
aliases: ["input validation", "output encoding", "sanitization", "zod validation", "dompurify", "allowlist denylist", "prototype pollution"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/input-validation-output-encoding.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [input-validation, output-encoding, sanitization, zod, dompurify, xss, allowlist, prototype-pollution, unicode-normalization]
skill: tech-mentor-security
status: stable
---

## TL;DR

Input Validation (rejeita o que não deveria existir) ≠ Sanitização (remove partes problemáticas). Validar com Zod na fronteira do sistema. Sanitizar HTML com DOMPurify (allowlist, não denylist). Output encoding por contexto: HTML (`&lt;`), URL (`encodeURIComponent`), SQL (parameterized queries). Allowlist > denylist. Atenção a prototype pollution (`Object.hasOwn`) e Unicode homoglyph attacks (normalizar para NFD/NFKC antes de comparar).

## Key Claims

**Claim:** Validação com Zod na borda é a defesa mais eficiente — rejeita inputs inválidos antes de entrar no sistema.
**Evidence:** Validar no controller: `z.object({ email: z.string().email(), amount: z.number().positive() })`. `parse()` lança erro se inválido; `safeParse()` retorna `{ success: false, error }`. `.transform()` para sanitizar inline: `z.string().transform(v => v.toLowerCase().trim())`. Sem validação de entrada: SQL injection, XSS, buffer overflow chegam ao core da aplicação.
**Confidence:** alta

**Claim:** Allowlist é sempre mais seguro que denylist para sanitização — o que não é permitido é bloqueado.
**Evidence:** Denylist de tags HTML: `<script>` na lista → bloquer. `<object>`, `<embed>`, `<svg onload>` — fora da lista → passa. Allowlist: apenas `p`, `strong`, `em`, `ul`, `li`, `a[href]` são permitidos. Tudo o mais é removido. DOMPurify usa allowlist configurável. Denylist requer conhecimento completo de todos os vetores — impossível de manter.
**Confidence:** alta

**Claim:** Prototype pollution é um vetor crítico em Node.js — `Object.hasOwn` previne acesso à cadeia de protótipos.
**Evidence:** `const obj = JSON.parse('{"__proto__": {"isAdmin": true}}')`. Em Node.js legado: `{}.isAdmin === true` para todos os objetos. Prevenção: `JSON.parse` com `Object.create(null)` como reviver, ou `Object.hasOwn(obj, key)` em vez de `key in obj`, ou usar `Map` para dados não confiáveis.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/input-validation]]
- [[concepts/output-encoding]]
- [[concepts/sanitization]]
- [[concepts/allowlist]]
- [[concepts/xss]]
- [[concepts/prototype-pollution]]
- [[concepts/unicode-normalization]]
- [[entities/dompurify]]
- [[entities/zod]]

## Open Questions

- Sanitização de SVG em editores rich text — como permitir SVG seguro sem abrir XSS via `<svg onload>`?
- Unicode normalization em sistemas de autenticação — quando NFD vs NFKC é a escolha correta?
