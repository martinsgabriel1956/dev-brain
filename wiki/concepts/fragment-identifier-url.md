---
type: concept
title: "Fragment Identifier (Hash da URL)"
aliases: ["fragment identifier", "url fragment", "location.hash", "hashtag da url", "#fragment"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_count: 2
tags: [browser, url, http, xss, dom, javascript]
skill: tech-mentor-security
status: draft
---

# Fragment Identifier (Hash da URL)

A parte de uma URL depois do `#`. Nasceu para rolar a tela até uma seção específica de um documento (`pagina.html#secao-3`), mas sua propriedade definidora é outra: **o navegador nunca envia o fragment identifier para o servidor**. Ele é resolvido inteiramente no cliente, depois que a resposta HTTP já chegou.

## Por que isso importa

Diferente de query parameters (`?busca=...`), que trafegam na requisição HTTP e passam por qualquer camada de servidor no caminho (proxy, WAF, [[wiki/concepts/waf]], logs de acesso), o fragment:

- Nunca aparece em logs de servidor.
- Nunca passa por filtros de sanitização server-side.
- Só é lido por JavaScript client-side (`location.hash` ou `window.location.hash`).
- Não conta para o limite de tamanho de payload de query string imposto por servidores web (ex.: Nginx limita 4–8 KB nesse parâmetro justamente para mitigar DDoS) — o fragment não é uma requisição, então esse limite simplesmente não se aplica a ele.
- Aguenta um volume de dados muito maior no cliente antes de o navegador reclamar — em torno de 2 MB em navegadores modernos como o Firefox, contra os poucos KB tolerados por parâmetro de query.

## Duas implicações opostas do mesmo mecanismo

**Superfície de ataque (DOM XSS):** como o fragment nunca passa pelo servidor, um filtro de sanitização que roda apenas no backend é inútil contra um payload entregue via fragment — o JavaScript do cliente lê e processa o valor diretamente, sem qualquer camada de defesa server-side no meio. É exatamente o vetor de [[wiki/concepts/xss]] do tipo DOM-based descrito em [[wiki/sources/xss-cross-site-scripting-luiz-viana]]: um filtro que bloqueia `<script>` só no servidor é irrelevante se o payload nunca visita o servidor.

**Canal de armazenamento sem servidor:** a mesma propriedade — grande capacidade + zero tráfego de rede — permite usar o fragment como um "disco" improvisado: dá para colocar um site HTML/CSS/JS inteiro, comprimido, ali dentro, e reconstruí-lo inteiramente no navegador sem nenhum servidor envolvido. É a base da técnica documentada em [[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]], que combina o fragment com [[wiki/concepts/brotli]] (compressão) e [[wiki/concepts/webassembly]] (descompressão) para hospedar uma página inteira só no link, sem custo de servidor.

## Nota de nomenclatura

O termo técnico correto é "fragment identifier" (RFC 3986); "hashtag" ou "hash da URL" são apelidos coloquiais para a mesma coisa.
