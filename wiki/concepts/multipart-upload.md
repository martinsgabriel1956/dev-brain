---
type: concept
title: "Multipart Upload"
aliases: ["multipart", "upload em partes", "chunked upload", "upload resumível", "resumable upload"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [system-design, s3, upload, resiliencia, presigned-url, multipart-upload]
skill: tech-mentor-system-design
status: draft
---

# Multipart Upload

Upload de um objeto grande em **partes independentes** (chunks), cada uma por uma [[wiki/concepts/presigned-url]] própria, depois montadas pelo storage num objeto único. Ganhos: paralelismo e **retomada** do ponto exato em que a conexão caiu.

## Quando usar

Regra da AWS: a partir de **100 MB**. Abaixo disso, PUT único (limite do PUT: 5 GB). Usar multipart em arquivo de 10–15 MB é red flag de entrevista — sinal de resposta decorada. Ver [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]].

## Fluxo (S3)

```
1. Cliente → servidor: nome, tipo, tamanho
2. Servidor → S3: CreateMultipartUpload → uploadId (salvo no banco, status=pendente)
3. Servidor calcula nº de partes (tamanho / 5 MB) e devolve array de URLs numeradas
4. Cliente envia partes (em paralelo); S3 devolve uma ETag por parte
5. Cliente → servidor: array ordenado de {partNumber, ETag}
6. Servidor → S3: CompleteMultipartUpload → S3 valida ETags e monta o objeto
7. S3 event → SQS → worker marca upload como completo
```

## Números (S3)

- Parte mínima: **5 MB** (exceto a última).
- Máximo **10.000 partes**, até 5 GiB cada.
- Objeto máximo: **50 TB** desde dez/2025 (≈ 48,8 TiB reais) [external: [anúncio AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-maximum-object-size-50-tb/)].

## Papel do `uploadId`

- **Retomada:** servidor pergunta ao S3 quais partes já chegaram (`ListParts`) → cliente continua dali.
- **Limpeza:** partes órfãs custam armazenamento. Cron job ou, nativamente, lifecycle rule `AbortIncompleteMultipartUpload` [external].
- **Reconciliação:** cron que acha uploads pendentes > 24h com todas as partes no S3 e finaliza por conta própria (cliente caiu antes de avisar).

## ETag como prova

O cliente não pode declarar "terminei" sem ter terminado: precisa apresentar as ETags que o próprio S3 gerou. No browser, o bucket precisa expor `ETag` via CORS [external].

## Alternativa

**tus**: protocolo aberto de upload resumível, com cliente/servidor prontos; o multipart do S3 não tem protocolo padronizado de retomada no browser [skill: tech-mentor-system-design].

## Relacionado

[[wiki/concepts/presigned-url]] · [[wiki/concepts/media-upload-pattern]] · [[wiki/concepts/amazon-s3]] · [[wiki/concepts/aws-sqs]] · [[wiki/concepts/processamento-assincrono]]

## Key Sources

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]]
