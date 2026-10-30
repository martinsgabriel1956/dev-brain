---
type: concept
title: "Bucket de Quarentena"
aliases: ["quarantine bucket", "quarentena de upload", "staging bucket de validação"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [system-design, seguranca, upload, s3, malware, appsec]
skill: tech-mentor-system-design
status: stub
---

# Bucket de Quarentena

Upload de usuário cai primeiro num **bucket temporário isolado**; uma máquina efêmera de validação escaneia o arquivo (ex.: malware); só depois de aprovado ele é movido para o bucket final. Se o arquivo for malicioso, o dano fica contido na máquina de validação — mesma lógica de [[wiki/concepts/sandbox]]. Resposta sugerida quando o entrevistador exige "validar antes de disponibilizar". Ver [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]].

## Lacunas

A fonte não detalha o gatilho nem o estado intermediário. Opções [external]: evento do S3 → worker de scan; GuardDuty Malware Protection for S3; status `PROCESSING` visível ao usuário até a aprovação.

## Relacionado

[[wiki/concepts/upload-arbitrario-rce]] · [[wiki/concepts/sandbox]] · [[wiki/concepts/presigned-url]] · [[wiki/concepts/amazon-s3]]

## Key Sources

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]]
