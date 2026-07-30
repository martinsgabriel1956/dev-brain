---
type: concept
title: "Compressão Com Perdas vs. Sem Perdas (Lossy vs. Lossless)"
aliases: ["lossy compression", "lossless compression", "compressão com perdas", "compressão sem perdas"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [compressao, cs-fundamentals, jpeg, png, information-theory]
skill: cs-fundamentals
status: stub
---

# Compressão Com Perdas vs. Sem Perdas

Duas estratégias opostas para reduzir o tamanho de um arquivo.

**Sem perdas (lossless):** nenhuma informação é descartada — o arquivo original é reconstruído bit a bit ao descomprimir. [[wiki/concepts/compactacao-de-texto]] (Huffman coding + LZSS/deflate) é a base teórica: reduz redundância estatística sem jogar dado fora. PNG, TIFF, BMP (sem compressão nenhuma) e RAW seguem essa filosofia — essencial quando qualquer perda de fidelidade é inaceitável (texto, ícones, arquivamento profissional, imagem-fonte antes de edição).

**Com perdas (lossy):** descarta deliberadamente informação considerada pouco perceptível para o receptor (o olho humano, no caso de imagem). JPEG é o exemplo canônico: divide a imagem em blocos de 8x8 pixels, aplica DCT (Discrete Cosine Transform) e quantiza os coeficientes de alta frequência — a parte que o olho humano menos percebe. Cada recompressão do mesmo arquivo aplica esse descarte de novo, degradando a imagem progressivamente (efeito cumulativo, diferente de lossless onde reabrir e resalvar não perde nada).

## Por que a escolha importa

- **Lossless** quando o arquivo será editado repetidamente (fonte de trabalho) ou quando bordas/texto nítido importam mais que tamanho (PNG para ícones e screenshots).
- **Lossy** quando o arquivo é a entrega final e o tamanho importa mais que fidelidade perfeita (JPEG/WebP/AVIF para fotografias na web).
- Formatos modernos (WebP, AVIF, JPEG XL) oferecem os dois modos no mesmo contêiner — a escolha lossy/lossless vira um parâmetro de encode, não uma decisão de formato.

## Fundamento teórico

A entropia de Shannon define o limite teórico de quanto uma fonte pode ser comprimida sem perda (`H(X) = -Σ p(x)·log₂p(x)`) — nenhuma técnica lossless consegue ir além desse limite. Compressão com perdas contorna esse teto descartando informação de propósito, trocando fidelidade por uma taxa de compressão que lossless jamais atingiria sozinho.

## Ver também

- [[wiki/concepts/formato-jpeg]] — exemplo canônico de compressão com perdas em imagem
- [[wiki/concepts/formato-png]] — exemplo canônico de compressão sem perdas em imagem
- [[wiki/concepts/compactacao-de-texto]] — Huffman coding, o passo final tanto em JPEG quanto em PNG

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
