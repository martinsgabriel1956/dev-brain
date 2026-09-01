---
type: concept
title: "Base64 / Base64URL"
aliases: ["base64", "base64url", "codificacao base64", "binary-to-text encoding"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_count: 1
tags: [encoding, base64, url, http, binary]
skill: tech-mentor-security
status: draft
---

# Base64 / Base64URL

Codificação binary-to-text: transforma bytes arbitrários (que podem conter qualquer valor, inclusive não-imprimível) num conjunto restrito de 64 caracteres alfanuméricos seguros para transportar em canais que só aceitam texto — o alfabeto padrão usa `A-Z`, `a-z`, `0-9`, `+`, `/`, com `=` como padding. Não é compressão: o resultado é ~33% maior que o binário original (cada 3 bytes viram 4 caracteres).

## Por que Base64 puro quebra em URLs

`+`, `/` e `=` são caracteres com significado estrutural dentro de uma URL (`+` costuma virar espaço, `/` delimita path, `=` separa chave/valor de query string). Colocar Base64 padrão direto numa URL corrompe o link.

## Base64URL

Variante desenhada especificamente para ser segura dentro de URLs: troca `+` por `-` e `/` por `_`, e descarta o padding `=`. Resolve o problema de estrutura sem inventar um alfabeto novo do zero — é o mesmo mapeamento de bits, só com um alfabeto de saída diferente nos pontos de conflito.

## Uso documentado nesta wiki

[[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]] usa Base64URL para transportar o binário comprimido em [[wiki/concepts/brotli]] dentro do [[wiki/concepts/fragment-identifier-url]] de uma URL. Colocar bytes crus (não-Base64) diretamente na URL faria o navegador aplicar percent-encoding em cada byte especial, inflando cada byte problemático para até 3 caracteres — Base64URL evita esse inchaço ao já restringir a saída a caracteres seguros de URL desde o início.
