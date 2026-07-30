---
type: concept
title: "Metadados EXIF"
aliases: ["exif", "exchangeable image file format", "metadados de imagem"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [formatos-de-imagem, exif, privacidade, jpeg]
skill: cs-fundamentals
status: stub
---

# Metadados EXIF

Bloco de metadados embutido em arquivos [[wiki/concepts/formato-jpeg|JPEG]] (e outros formatos) contendo informações sobre a captura da imagem: modelo da câmera, data/hora e, quando o dispositivo tem GPS ativo, as coordenadas de onde a foto foi tirada.

## Implicação de privacidade

Compartilhar um JPEG sem remover o EXIF pode revelar involuntariamente a localização de quem tirou a foto — a informação viaja junto com o arquivo, invisível na visualização normal da imagem, mas legível por qualquer ferramenta que leia metadados.

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
