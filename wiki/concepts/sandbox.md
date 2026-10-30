---
type: concept
title: "Sandbox"
aliases: ['sandboxing']
date_created: 2026-10-14
date_updated: 2026-10-30
source_count: 2
tags: [seguranca, isolamento, java]
skill: tech-mentor-security
status: stub
---

# Sandbox

Container que executa código com **baixos privilégios** (sem acesso a arquivos ou rede). Criado para os applets Java no navegador ([[wiki/concepts/plugin-de-navegador]]); o conceito segue em navegadores modernos e agentes.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]

## Caso: Máquina de Validação de Upload

[[wiki/concepts/bucket-de-quarentena]]: arquivo enviado é escaneado numa máquina temporária isolada; malware pode "explodir" ali sem atingir o bucket final. Ver [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]].

## Key sources (adição 2026-10-30)

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]] — quarentena de upload como sandbox descartável
