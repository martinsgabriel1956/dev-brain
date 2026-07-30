---
type: concept
title: "JPEG"
aliases: ["jpg", "jpeg", "joint photographic experts group"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [formatos-de-imagem, compressao, jpeg, exif]
skill: cs-fundamentals
status: stub
---

# JPEG

Formato de imagem lançado em 1992, provavelmente o mais utilizado do planeta. Resolve um único problema: reduzir drasticamente o tamanho de uma foto sem perda perceptível de qualidade para o olho humano.

## Como funciona

[[wiki/concepts/compressao-com-perdas-vs-sem-perdas]] — compressão *com perdas*: a imagem é dividida em blocos de 8x8 pixels, cada bloco é transformado (DCT) e os coeficientes de alta frequência (menos perceptíveis ao olho humano) são quantizados/descartados. Huffman coding entra como passo final de compressão sem perdas sobre os coeficientes já quantizados — ver [[wiki/concepts/compactacao-de-texto]].

**Consequência prática:** cada vez que o mesmo arquivo JPEG é reaberto e resalvo, a compressão com perdas é reaplicada, degradando a imagem de forma cumulativa. Por isso o fluxo profissional é trabalhar no arquivo original ([[wiki/concepts/formato-raw-fotografia]] ou TIFF) e exportar para JPEG só na entrega final.

## JPG vs. JPEG

Mesmo formato — a extensão de 3 letras (`.jpg`) existe só porque versões antigas do Windows (FAT) limitavam extensões a 3 caracteres.

## Metadados EXIF

Ver [[wiki/concepts/exif-metadados]] — arquivos JPEG carregam metadados que podem incluir câmera, data e coordenadas GPS da foto.

## Tentativas de sucessor

- **JPEG 2000** (anos 2000): melhor compressão/qualidade, mas nunca ganhou adoção — JPEG tradicional já estava em todo lugar.
- **JPEG XL** (2021): suporta transparência, animação e compressão melhor; tecnicamente superior mas ainda sem adoção ampla em navegadores/programas.

## Ver também

- [[wiki/concepts/formato-png]] — contraparte sem perdas
- [[wiki/concepts/formato-webp]], [[wiki/concepts/formato-heic-avif]] — sucessores modernos com compressão superior

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
