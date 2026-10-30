---
type: concept
title: "Presigned URL (URL Pré-Assinada)"
aliases: ["presigned url", "URL pré-assinada", "signed url", "URL assinada", "pre-signed URL"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [system-design, s3, upload, download, seguranca, valet-key, presigned-url]
skill: tech-mentor-system-design
status: draft
---

# Presigned URL (URL Pré-Assinada)

URL temporária para um objeto de [[wiki/concepts/object-storage]] (S3) que já carrega a autorização dentro dela: expiração + assinatura (`X-Amz-Signature`). Quem a possui pode fazer **uma operação específica** (PUT, GET, UploadPart) em **uma chave específica** até expirar — sem credencial própria. É a implementação concreta do [[wiki/concepts/valet-key-pattern]].

## Quem gera

O **servidor de aplicação, localmente**, via SDK + credencial secreta — não é preciso chamar o S3 para obtê-la. O S3 só valida a assinatura quando a requisição chega; qualquer parâmetro adulterado → assinatura não bate → negado. Ver [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]].

```typescript
// [skill: tech-mentor-system-design] architecture-ops.md
const uploadUrl = await getSignedUrl(s3, new PutObjectCommand({ Bucket, Key, ContentType }), { expiresIn: 300 })
```

## Usos

| Operação | Quando | Nota |
|---|---|---|
| PUT único | upload < 100 MB | fluxo de [[wiki/concepts/media-upload-pattern]] |
| UploadPart (array numerado) | upload ≥ 100 MB | ver [[wiki/concepts/multipart-upload]] |
| GET | download de arquivo **privado** | checar permissão **antes** de gerar; arquivo público dispensa |

## Limites e cuidados

- **Expiração curta** (minutos) — URL vazada vale até expirar.
- **Tamanho não é imposto** num PUT pré-assinado comum: o cliente pode mandar mais bytes do que declarou. Usar presigned POST com `content-length-range` ou validar no evento de conclusão [external].
- Para conteúdo protegido servido via CDN, existe a variante **CloudFront signed URL** (key pair, servida pelo edge) [skill: tech-mentor-system-design].

## Relacionado

[[wiki/concepts/valet-key-pattern]] · [[wiki/concepts/media-upload-pattern]] · [[wiki/concepts/multipart-upload]] · [[wiki/concepts/amazon-s3]] · [[wiki/concepts/aws-cloudfront]]

## Key Sources

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]] — geração local pelo servidor, PUT vs multipart, download privado via S3 key
