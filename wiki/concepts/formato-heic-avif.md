---
type: concept
title: "HEIC e AVIF"
aliases: ["heic", "heif", "avif", "high efficiency image container", "av1 image file format"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [formatos-de-imagem, compressao, heic, avif, codec, hevc, av1]
skill: cs-fundamentals
status: stub
---

# HEIC e AVIF

Os dois formatos de imagem mais recentes da linhagem JPEG/PNG/WebP compartilham a mesma ideia central: **reaproveitar codecs de vídeo para comprimir um único frame**. Se um vídeo é apenas uma sequência de imagens, a mesma tecnologia de compressão desenvolvida para vídeo pode comprimir uma imagem isolada — e essa tecnologia é bem mais sofisticada que a usada por JPEG (1992).

## HEIC (~2015)

Criado pelo MPEG (o grupo por trás de vários codecs de vídeo). Usa o codec **HEVC/H.265** — ver tabela de codecs em [[wiki/concepts/video-transcoding]]. Ganhou fama em 2017 quando a Apple adotou como formato padrão de fotos do iPhone, motivado pelo crescimento do volume de fotos por usuário e pressão sobre armazenamento interno. Suporta HDR e faixa de cor maior que JPEG. Principal limitação: **compatibilidade** — nem todo dispositivo/programa abre HEIC, por isso o iPhone frequentemente converte para JPEG ao compartilhar (mas nem sempre, causando o clássico "não consigo abrir essa imagem").

## AVIF

Usa o codec **AV1** — o mais recente e mais eficiente da tabela em [[wiki/concepts/video-transcoding]], já usado pelo YouTube para conteúdo popular. Gera arquivos ainda menores que JPEG/PNG com qualidade comparável, suporta transparência, HDR, maior profundidade de cor e produz menos artefatos de compressão que HEIC. Assim como HEIC, sofreu adoção lenta por parte de navegadores e editores, mas hoje já tem suporte nos principais navegadores e uso silencioso em grandes plataformas.

## Ver também

- [[wiki/concepts/video-transcoding]] — mesma tabela de codecs (HEVC, AV1) usada tanto para vídeo quanto para imagem estática
- [[wiki/concepts/formato-webp]] — geração anterior, adoção mais madura

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
