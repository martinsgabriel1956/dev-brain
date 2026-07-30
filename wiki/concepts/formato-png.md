---
type: concept
title: "PNG"
aliases: ["png", "portable network graphics", "apng"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [formatos-de-imagem, compressao, png]
skill: cs-fundamentals
status: stub
---

# PNG

Formato de imagem lançado em 1996 como resposta direta a um problema de licenciamento: a empresa dona da patente do algoritmo LZW usado pelo GIF anunciou cobrança de royalties de desenvolvedores. A comunidade respondeu criando o PNG — gratuito, de código aberto e livre de patentes.

## Características

- **[[wiki/concepts/compressao-com-perdas-vs-sem-perdas]] sem perdas**: nenhum pixel é alterado entre salvar e reabrir. Ideal para logotipos, ícones, screenshots e qualquer imagem com texto/bordas nítidas.
- **Transparência verdadeira** via canal alfa (diferente da transparência binária — um pixel é ou não é transparente — do GIF).
- **Desvantagem**: arquivos bem maiores que JPEG para fotografias, onde a compressão com perdas do JPEG compensa mais.
- **APNG**: variante animada do PNG, existe mas tem adoção quase nula.

## Ver também

- [[wiki/concepts/formato-jpeg]] — contraparte com perdas, melhor para fotografia
- [[wiki/concepts/formato-gif]] — formato que o PNG foi criado para substituir
- [[wiki/concepts/compactacao-de-texto]] — Huffman coding + deflate são a base da compressão sem perdas do PNG

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
