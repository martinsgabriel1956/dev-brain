---
type: concept
title: "Object Storage (Blob Storage)"
aliases: ["object storage", "blob storage", "BLOB", "binary large object", "armazenamento de objetos"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [system-design, storage, object-storage, s3, infra]
skill: tech-mentor-system-design
status: draft
---

# Object Storage (Blob Storage)

Armazenamento de **objetos estáticos** (vídeos, imagens, PDFs, backups) endereçados por chave, separado do banco transacional e dos servidores de aplicação. "Blob storage" é sinônimo — *blob* = *binary large object*. Exemplos: [[wiki/concepts/amazon-s3]], Google Cloud Storage, Azure Blob Storage; S3 é o nome padrão em entrevistas.

## Por que não guardar arquivos em outro lugar

| Onde | Problema |
|---|---|
| Banco (coluna binária) | queries pesadas, backup/restore de horas, cada [[wiki/concepts/read-replicas\|réplica]] copia os arquivos |
| Disco do servidor | quebra com [[wiki/concepts/load-balancer]] e [[wiki/concepts/auto-scaling]] — viola [[wiki/concepts/stateless]] |
| Volume compartilhado | funciona, mas é ponto único de falha e exige time de infra (ver [[wiki/concepts/nas-network-attached-storage]]) |

Padrão resultante: banco guarda só metadados + **chave do objeto** (S3 key); bytes ficam no object storage; acesso via [[wiki/concepts/presigned-url]]. Ver [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]].

## Relacionado

[[wiki/concepts/amazon-s3]] · [[wiki/concepts/presigned-url]] · [[wiki/concepts/multipart-upload]] · [[wiki/concepts/media-upload-pattern]] · [[wiki/concepts/cdn]] · [[wiki/concepts/storage-tiering]]

## Key Sources

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]] — evolução banco → disco local → volume compartilhado → object storage
