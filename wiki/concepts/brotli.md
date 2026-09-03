---
type: concept
title: "Brotli"
aliases: ["brotli", "compressão brotli", "content-encoding br"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_count: 1
tags: [compressao, brotli, http, performance, gzip]
skill: tech-mentor-security
status: draft
---

# Brotli

Algoritmo de compressão sem perdas (lossless) desenvolvido pelo Google, sucessor mais agressivo do [[wiki/concepts/compactacao-de-texto]] (deflate/gzip) para conteúdo web. Combina três estratégias:

1. **Dicionário estático embutido:** vem de fábrica com um dicionário pré-carregado dos termos mais comuns da web (tags HTML, palavras frequentes em CSS/JS/inglês) — substitui essas sequências por códigos curtos sem precisar aprendê-las do zero a cada arquivo, diferente do deflate puro.
2. **Eliminação de repetições (mesmo princípio de LZ77/LZSS):** ocorrências repetidas de uma sequência viram uma referência de volta à ocorrência anterior, em vez de serem reescritas — ver [[wiki/concepts/compactacao-de-texto]] para o mecanismo formal (sliding window, triplet offset/length/caractere).
3. **Codificação por frequência (parente do Huffman coding):** símbolos que aparecem com mais frequência recebem representações menores; símbolos raros recebem representações maiores — mesma lógica de fundo do Huffman coding descrito em [[wiki/concepts/compactacao-de-texto]].

## Onde normalmente é ativado

Em uso normal na web, Brotli é ativado via negociação HTTP: o servidor detecta que o cliente aceita Brotli (header `Accept-Encoding: br` do request) e responde com o conteúdo comprimido mais o header `Content-Encoding: br`. É esse header que avisa o motor de descompressão nativo do navegador para descomprimir automaticamente antes de entregar o conteúdo à página.

## O caso sem servidor

Sem um servidor HTTP no meio — por exemplo, dados Brotli-comprimidos entregues inteiramente dentro do [[wiki/concepts/fragment-identifier-url]] de uma URL — não existe handshake `Accept-Encoding`/`Content-Encoding`, e o motor nativo do navegador se recusa a descomprimir o conteúdo. [[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]] documenta essa limitação e a solução: implementar o próprio descompressor Brotli e rodá-lo via [[wiki/concepts/webassembly]] (não em JavaScript puro, por causa do custo computacional em thread única), decodificando manualmente o payload transportado em Base64URL.
