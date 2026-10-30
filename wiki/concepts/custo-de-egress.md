---
type: concept
title: "Custo de Egress"
aliases: ["egress", "data transfer out", "transferência de saída", "egress cost"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_count: 1
tags: [finops, cloud, aws, cdn, rede, custo]
skill: tech-mentor-system-design
status: draft
---

# Custo de Egress

Quanto o provedor de nuvem cobra para **transferir dados de dentro dele para a internet** (ou entre regiões). Entrada (ingress) costuma ser grátis; saída é cobrada por GB — em sistemas que servem arquivos grandes, vira linha relevante da fatura ([[wiki/concepts/finops]]).

## Números de referência (AWS, primeiros 10 TB/mês, EUA/Europa)

| Caminho | US$/GB |
|---|---|
| [[wiki/concepts/amazon-s3\|S3]] → internet | 0,09 |
| S3 → [[wiki/concepts/aws-cloudfront\|CloudFront]] | 0 (grátis) |
| CloudFront → internet | 0,085 |

Fontes: [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]]; conferido em fontes secundárias [external: [awsfundamentals](https://awsfundamentals.com/blog/amazon-cloudfront-pricing), [redresscompliance](https://redresscompliance.com/aws-cloudfront-vs-direct-egress-cost.html)]. Preços mudam — confirmar na página oficial antes de usar em decisão.

## CDN reduz egress — mas não "90%" por GB

A fonte afirma "economia de 90%" ao pôr CloudFront na frente do S3; pelos próprios números ela é ~**5,6%** por GB. O ganho real de custo vem de: cache hit (a origem não é lida de novo), redução de requisições GET no S3, free tier do CloudFront (1 TB/mês) e faixas de volume/flat-rate [external]. Argumento correto para entrevista: "S3→CloudFront é grátis e o cache tira carga e requisições da origem". Ver [[wiki/concepts/cdn]].

## Relacionado

[[wiki/concepts/finops]] · [[wiki/concepts/cdn]] · [[wiki/concepts/aws-cloudfront]] · [[wiki/concepts/amazon-s3]]

## Key Sources

- [[wiki/sources/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s]] — egress S3 vs. CloudFront como argumento de custo para CDN (com erro de cálculo apontado)
