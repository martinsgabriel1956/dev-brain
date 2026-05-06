---
type: concept
title: "Backbone de Rede AWS"
aliases: ["AWS Network Backbone", "Rede Privada AWS", "AWS Global Network"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "rede", "performance", "fibra-óptica", "infraestrutura"]
skill: tech-mentor-infra
status: stub
---

# Backbone de Rede AWS

Rede privada de fibra óptica da AWS que interconecta todas as [[regiao-aws|Regiões]], [[zona-de-disponibilidade|AZs]], [[aws-cloudfront|POPs CloudFront]] e data centers globalmente. O tráfego entre componentes AWS trafega nessa rede privada — não pela internet pública.

## Números

- **9+ milhões de quilômetros** de cabeamento de fibra óptica
- Conecta 39 regiões, 123 AZs e 750+ POPs globalmente

## Vantagens vs. Internet Pública

| Aspecto | Backbone AWS | Internet Pública |
|---|---|---|
| Latência | Menor e previsível | Variável (roteamento dinâmico) |
| Segurança | Tráfego não exposto | Atravessa múltiplos ASes |
| Largura de banda | Dedicada e consistente | Compartilhada, sujeita a congestionamento |
| Confiabilidade | SLA controlado pela AWS | Sem garantias de rota |

## Serviços que Usam o Backbone

- **CloudFront** — conteúdo vai da origem até o POP pelo backbone, só o último trecho é internet
- **Global Accelerator** — roteia tráfego de usuários pelo backbone desde o POP de entrada
- **Direct Connect** — conecta rede on-prem diretamente ao backbone AWS (sem internet)
- **Transit Gateway** — roteamento inter-VPC e inter-região pelo backbone

## AWS Global Accelerator vs. CloudFront

| | Global Accelerator | CloudFront |
|---|---|---|
| Propósito | Roteamento de tráfego TCP/UDP | Cache e entrega de conteúdo HTTP |
| Cache | Não | Sim |
| Protocolo | Qualquer (TCP/UDP) | HTTP/HTTPS |
| Casos | APIs, jogos, IoT | Web, vídeo, assets |

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
