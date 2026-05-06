---
type: source
title: "Infraestrutura Global da AWS"
aliases: ["AWS Global Infrastructure"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/aws-infraestrutura-global.md"
source_url: "https://aws.amazon.com/pt/about-aws/global-infrastructure/"
author: "Amazon Web Services"
date_published: 2024
date_ingested: 2026-05-06
source_count: 0
tags: ["aws", "infraestrutura", "cloud", "regiões", "zonas-de-disponibilidade", "cdn", "edge"]
skill: tech-mentor-infra
status: stable
---

# Infraestrutura Global da AWS

## TL;DR

A AWS opera a maior infraestrutura de nuvem do mundo: 39 regiões geográficas, 123 Zonas de Disponibilidade, 750+ POPs CloudFront e 43 zonas de borda (Local Zones + Wavelength). O backbone privado de fibra óptica com mais de 9 milhões de km garante baixa latência, alta segurança e desempenho consistente globalmente.

---

## Principais Afirmações

| Claim | Evidência | Confiança |
|---|---|---|
| AWS tem 39 regiões lançadas | Página oficial AWS (2025) | Alta |
| 123 Zonas de Disponibilidade globais | Página oficial AWS (2025) | Alta |
| Backbone de 9+ milhões de km de fibra | Página oficial AWS | Alta |
| Mais de 750 POPs do CloudFront | Página oficial AWS | Alta |
| Mínimo de 3 AZs por região | Documentação arquitetural AWS | Alta |
| Expansão planejada: +7 AZs, +2 regiões (Arábia Saudita e Chile) | Página oficial AWS | Alta |

---

## Conceitos Introduzidos ou Aprofundados

- [[regiao-aws]] — unidade geográfica isolada com múltiplas AZs
- [[zona-de-disponibilidade]] — data center isolado dentro de uma região
- [[zona-local-aws]] — extensão de região em centros metropolitanos
- [[aws-wavelength]] — infraestrutura embutida em redes 5G de operadoras
- [[aws-outposts]] — rack AWS instalado on-premises no cliente
- [[zona-local-dedicada]] — infraestrutura dedicada para soberania digital
- [[aws-cloudfront]] — CDN global com 750+ POPs
- [[backbone-de-rede-aws]] — rede privada de fibra óptica global
- [[soberania-digital]] — controle de dados dentro de fronteiras jurisdicionais
- [[alta-disponibilidade]] — resiliência por redundância geográfica

---

## Entidades

- [[amazon-web-services]] — provedor da infraestrutura descrita

---

## Números-Chave (snapshot 2025)

```
39  regiões lançadas
123  zonas de disponibilidade
750+  POPs CloudFront
13  caches de borda regionais
43  zonas de borda (Local Zones + Wavelength)
9M km  cabeamento de fibra óptica privado
+2  regiões anunciadas (Arábia Saudita, Chile)
+7  AZs anunciadas
```

---

## Questões em Aberto

- Qual o SLA contratual por serviço e como ele varia entre regiões?
- Quais regiões possuem conformidade com LGPD brasileira de forma certificada?
- Como a latência real se compara entre backbone AWS vs. internet pública para casos Brasil → EUA?

---

## Quotes Relevantes

> "A infraestrutura global da AWS maximiza a resiliência, o desempenho e a inovação. Usando mais de 9 milhões de quilômetros de cabeamento de fibra óptica, o backbone de rede global da AWS permite uma transferência de dados mais rápida, latência reduzida e desempenho aprimorado do aplicativo."
