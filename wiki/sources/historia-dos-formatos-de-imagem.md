---
type: source
title: "A História dos Formatos de Imagem"
aliases: ["formatos de imagem", "image formats history", "tga png jpeg gif svg webp heic avif"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/historia-dos-formatos-de-imagem.md"
source_url: ""
author: "desconhecido (canal YouTube)"
date_published: "desconhecido"
date_ingested: 2026-07-29
source_count: 0
tags: [formatos-de-imagem, compressao, computacao-grafica, jpeg, png, gif, svg, webp, heic, avif, raw, tiff, huffman-coding]
skill: cs-fundamentals
status: stable
---

## TL;DR

Percurso cronológico pelos principais formatos de imagem (TGA 1984 → PDF), mostrando que cada um resolveu um problema específico de compressão, transparência ou fidelidade: TGA trouxe o canal alfa para texturas de games; PCX introduziu RLE; BMP não comprime nada; GIF trouxe animação e paleta de 256 cores; JPEG usa compressão com perdas em blocos 8x8 (DCT) e nunca deveria ser resalvo repetidamente; PNG nasceu como resposta livre de patente ao licenciamento do GIF, com compressão sem perdas; TIFF e RAW priorizam fidelidade total para uso profissional; SVG é o único formato vetorial da lista (instruções matemáticas em vez de pixels); WebP, HEIC e AVIF são a geração mais recente, todos reaproveitando avanços de compressão originalmente feitos para vídeo (HEIC/AVIF literalmente usam codecs de vídeo — HEVC e AV1 — para comprimir uma única imagem); PDF não é formato de imagem, é um contêiner de documento.

## Key Claims

**Claim:** Formatos de imagem raster antigos (TGA, PCX, BMP) mapeiam diretamente a evolução dos problemas de hardware/software dos anos 80: paleta de cores limitada, ausência de compressão, necessidade de transparência para composição de camadas.
**Evidence:** TGA (1984) introduziu canal alfa para texturas 3D e ainda é usado hoje em jogos como Counter-Strike; PCX (1985) introduziu RLE (run-length encoding) para comprimir áreas de cor sólida; BMP (1986) não usa compressão nenhuma — grava cada pixel literalmente, gerando arquivos até 25× maiores que o equivalente em JPEG.
**Confidence:** média (fonte é vídeo popular sem citação de especificação formal, mas os fatos são verificáveis e consistentes com conhecimento de domínio)

**Claim:** JPEG (1992) é compressão *com perdas* (lossy) baseada em blocos de 8x8 pixels, e resalvar o mesmo arquivo repetidamente degrada a imagem progressivamente — por isso fotógrafos preservam o arquivo original (RAW/TIFF) e só exportam para JPEG na entrega final.
**Confidence:** alta — consistente com o funcionamento documentado do JPEG (DCT por bloco + quantização com perda de informação a cada recompressão).

**Claim:** PNG (1996) nasceu como reação da comunidade ao anúncio de royalties sobre a patente do algoritmo LZW usado no GIF — resultando num formato livre, de código aberto, com compressão *sem perdas* (todos os pixels idênticos ao original after round-trip) e suporte a transparência verdadeira (canal alfa, ao contrário da transparência binária do GIF).
**Confidence:** alta.

**Claim:** HEIC e AVIF não são algoritmos de compressão de imagem desenvolvidos do zero — são contêineres que reaproveitam codecs de vídeo (HEVC/H.265 para HEIC, AV1 para AVIF) para comprimir um único frame, herdando ferramentas de compressão muito mais sofisticadas do que as usadas por JPEG/PNG.
**Evidence:** a lógica citada na fonte — "se um vídeo é uma sequência de imagens, por que não usar a mesma tecnologia para comprimir uma única imagem" — bate com a tabela de codecs já registrada em [[wiki/concepts/video-transcoding]] (H.264, HEVC, VP9, AV1), que mostra AV1 com a melhor compressão do grupo e adoção crescente (YouTube já usa AV1 para conteúdo popular).
**Confidence:** alta.

**Claim:** SVG (2001) é estruturalmente diferente de todos os outros formatos da lista porque não armazena pixels — armazena instruções matemáticas (linhas, curvas, formas geométricas), o que permite escalar infinitamente sem perda de nitidez.
**Confidence:** alta — é a definição central de formato vetorial vs. raster.

## Entities & Concepts Touched

- [[wiki/concepts/formato-jpeg]]
- [[wiki/concepts/formato-png]]
- [[wiki/concepts/formato-gif]]
- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/formato-webp]]
- [[wiki/concepts/formato-heic-avif]]
- [[wiki/concepts/formato-raw-fotografia]]
- [[wiki/concepts/exif-metadados]]
- [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]]
- [[wiki/concepts/compactacao-de-texto]] — mesma base teórica (Huffman coding) aparece como passo final da compressão do JPEG e do PNG, generalizando o que essa página já documentava só para texto/HTTP
- [[wiki/concepts/video-transcoding]] — HEIC e AVIF reaproveitam os mesmos codecs de vídeo (HEVC, AV1) já catalogados nessa página

## Open Questions

- A fonte não cita specs formais (ISO/IEC, RFCs) para nenhum formato — os fatos batem com conhecimento de domínio geral, mas para uso técnico rigoroso (ex.: decidir formato de output de uma pipeline de imagens) vale checar a especificação oficial de cada formato antes de decisão de produção.
- A fonte não detalha o funcionamento interno do DCT (Discrete Cosine Transform) usado no JPEG nem do algoritmo de predição usado no AV1/HEVC — fica como lacuna para uma fonte futura mais técnica sobre codecs de imagem/vídeo.
- Skill `cs-fundamentals` foi carregada via `references/discrete-math.md` (seção Shannon/Huffman) por analogia de domínio — o path de skills usado neste ambiente é `/home/gabriel-martins/Documentos/skills/`, não `/home/nemomartins/Documentos/new/skills/` referenciado no CLAUDE.md (mesma discrepância já registrada em [[wiki/sources/por-que-letras-minusculas-economizam-dados]]).
