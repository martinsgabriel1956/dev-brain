---
type: concept
title: "PNG"
aliases: ["png", "portable network graphics", "apng"]
date_created: 2026-07-29
date_updated: 2026-11-13
source_count: 5
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

## Na prática de UI

Na aula de imagens de [[wiki/entities/nasser|Násser]], PNG fica para fotos com transparência que não dá para vetorizar (recortes aplicados sobre outros artboards); para fotografia realista ele indica JPG, mais leve. A afirmação de que JPG e PNG são "muito parecidos em qualidade" vale para foto; em texto e bordas nítidas o PNG sem perdas ganha ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). Para ícones, PNG resolvia a transparência, mas hoje é "um modelo mais arcaico" diante do [[wiki/concepts/formato-svg|SVG]] ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — regra de uso em UI: só quando precisa de transparência
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — PNG para ícone com transparência virou "modelo mais arcaico" diante do SVG
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": "não vai sumir" por causa da transparência; um pouco mais pesado que o JPG
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — export do frame em PNG pelo painel do Figma
