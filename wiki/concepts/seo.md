---
type: concept
title: "SEO (Search Engine Optimization)"
aliases: ["otimização para buscadores", "SEO técnico", "indexação", "ranqueamento"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 2
tags: [seo, google, indexacao, html-semantico, meta-tags, core-web-vitals, frontend]
skill: tech-mentor-frontend
status: stub
---

# SEO (Search Engine Optimization)

Tornar páginas fáceis de encontrar, entender e preferir num buscador. São três etapas, que a aula de PageSpeed do FrontPUSH trata como uma só ("indexar"):

1. **Rastreamento (crawl):** o Googlebot descobre URLs por links e pelo `sitemap.xml`, e respeita o `robots.txt`. É contínuo, mas a frequência varia por site.
2. **Indexação:** a página é lida, renderizada (inclusive o JavaScript, com atraso) e guardada. `noindex`, conteúdo duplicado e páginas vazias ficam de fora.
3. **Ranqueamento:** relevância do conteúdo para a busca vem primeiro; experiência de página ([[wiki/concepts/core-web-vitals]], HTTPS, sem intersticial intrusivo) pesa como critério secundário.

`[external]` https://developers.google.com/search/docs/fundamentals/how-search-works (sem fetch nesta sessão; confiança alta).

## O que o front-end controla

- `<title>` único e descritivo e `meta description` (o trecho do resultado, que o Google pode reescrever) ([[wiki/concepts/head-html-metadados]]).
- [[wiki/concepts/html-semantico]]: `h1`–`h6` em ordem, `nav`, `main`, `article`; ajuda a entender a página, mas não é fator forte de ranking.
- Links rastreáveis (`<a href>`, não `onclick`), URLs limpas, `canonical`.
- Renderização: conteúdo que só aparece depois do JavaScript demora mais a ser indexado ([[wiki/concepts/renderizacao-ssr-vs-csr]]).
- Dados estruturados (JSON-LD, schema.org) para resultados ricos.
- [[wiki/concepts/open-graph]] não é SEO de busca, mas controla a pré-visualização ao compartilhar.

`meta keywords` é ignorada pelo Google desde 2009.

## No FrontPUSH

- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: SEO como consequência das otimizações; "o Google vai melhor indexar a sua página de acordo com a experiência do usuário" (confunde indexação e ranking).
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: o Google "baixa a internet todos os dias"; links em `header`/`nav`/`menu`; `meta keywords` geradas no ChatGPT.

## Key sources

- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: FrontPUSH, otimização aula 01: SEO como consequência
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: HTML semântico e meta tags
