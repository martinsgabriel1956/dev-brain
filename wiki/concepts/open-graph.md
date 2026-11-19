---
type: concept
title: "Open Graph e Twitter Cards"
aliases: ["og:image", "og:title", "meta og", "Twitter Card", "pré-visualização de link", "link preview"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
tags: [html, meta-tags, open-graph, compartilhamento, seo, frontend]
skill: tech-mentor-frontend
status: stub
---

# Open Graph e Twitter Cards

Meta tags que dizem a redes sociais e apps de mensagem o que mostrar quando um link é colado: título, descrição, imagem. O protocolo Open Graph foi criado pelo Facebook ([[wiki/entities/meta]]) em 2010 e é lido também por WhatsApp, LinkedIn, Slack, Discord e Telegram. O X/Twitter tem o seu (Twitter Cards), mas cai no Open Graph quando falta.

```html
<meta property="og:title" content="Solten | Energia solar">
<meta property="og:description" content="Projetos de energia solar residencial.">
<meta property="og:image" content="https://exemplo.com.br/og.png">
<meta property="og:url" content="https://exemplo.com.br/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
```

- Open Graph usa `property`; Twitter Cards usam `name`.
- `og:image` com URL absoluta, cerca de 1200×630 px, PNG ou JPG, leve.
- Os apps guardam a prévia em cache; para atualizar, o Sharing Debugger do Facebook força uma nova leitura.
- Não é fator de ranking no Google ([[wiki/concepts/seo]]); o `<title>` e a `meta description` são os do buscador ([[wiki/concepts/head-html-metadados]]).

## No FrontPUSH

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]], [[wiki/entities/nasser|Násser]] repete título, descrição e imagem PNG "com diferentes propriedades [...] pelo Facebook ou pelo Twitter", "só mudando essa propriedadezinha aqui, property", e compara com a prévia de um vídeo do YouTube num chat.

## Key sources

- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: meta tags de compartilhamento
