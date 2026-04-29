---
type: concept
title: "Media Upload Pattern"
aliases: ["presigned url", "upload direto s3", "media upload", "direct upload"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, s3, upload, cdn, performance, infra]
skill: tech-mentor-system-design
status: stable
---

# Media Upload Pattern

Upload de mídia direto para object storage (S3), sem passar pelo servidor de aplicação. Reduz carga no servidor e escala naturalmente.

## Fluxo

```
1. Client solicita presigned URL ao backend
   → Backend gera URL temporária autorizada: S3.generatePresignedUrl(...)

2. Client faz upload direto para S3 com a presigned URL
   → Não passa pelo Chat Server / API Server

3. S3 notifica backend (event notification) ou client confirma upload
   → Backend retorna CDN URL da mídia ao client

4. Mensagem enviada com referência à mídia:
   { type: "image", media_url: "cdn.whatsapp.com/abc123.jpg" }
```

## Por que Não Passar pelo Servidor

- 48GB/s de upload passando pelo Chat Server = Chat Server vira gargalo
- S3 escala horizontalmente sem limitação prática
- Presigned URL tem TTL curto (ex: 5 min) — segurança sem expor credenciais

## CDN

CloudFront (ou equivalente) serve a mídia aos recipients. Origin é S3. TTL de 1 ano — após expirar, URL quebra (re-upload necessário se compartilhado novamente).

## Compressão no Client

WhatsApp comprime imagens para max 1600px antes do upload. Reduz volume de storage e tempo de upload sem degradar UX significativamente.

## Relacionado

[[concepts/cache-hot-path]] — CDN é o cache de mídia, mesmo princípio de servir do edge.

## Key Sources

- [[sources/case-whatsapp]]
