---
type: concept
title: "AWS CloudFront"
aliases: ["CloudFront", "CDN AWS", "AWS CDN"]
date_created: 2026-05-06
date_updated: 2026-08-17
source_count: 4
tags: ["aws", "cdn", "edge", "performance", "cache"]
skill: tech-mentor-infra
status: stub
---

# AWS CloudFront

Rede de Entrega de Conteúdo (CDN) global da AWS. Distribui conteúdo (estático, dinâmico, streaming) para usuários finais com baixa latência, servindo a partir do Ponto de Presença (POP) mais próximo do usuário — sem que a requisição precise chegar até a [[regiao-aws|Região AWS]] de origem.

## Números Atuais (2025)

- **750+ POPs** (Pontos de Presença) globalmente
- **13 caches de borda regionais** (camada intermediária entre POPs e origem)

## Arquitetura em Camadas

```
Usuário
└── POP mais próximo (Edge Location)
    ├── Cache hit → resposta imediata
    └── Cache miss → Regional Edge Cache
        └── Cache miss → Origem (S3, ALB, API Gateway, servidor)
```

## Casos de Uso

| Tipo | Exemplo |
|---|---|
| Assets estáticos | JS, CSS, imagens de um SPA |
| Vídeo on-demand | HLS/DASH com cache por segmento |
| APIs dinâmicas | Cache de respostas + geo-routing |
| WAF integrado | Proteção contra DDoS e OWASP Top 10 |
| Lambda@Edge / CloudFront Functions | Lógica na borda (rewrite, auth, A/B) |

## Benefícios vs. Servir da Região

- Latência: POPs a < 20ms dos usuários finais em grandes cidades
- Custo: menos requisições chegam à origem → menos compute
- Segurança: absorve DDoS na borda antes de chegar à origem
- Disponibilidade: conteúdo cacheado continua servindo mesmo com origem fora

## Diferença: CloudFront vs. Zona Local

| | CloudFront | Local Zone |
|---|---|---|
| Propósito | Cache e entrega de conteúdo | Compute/DB próximo ao usuário |
| Stateless | Sim (cache) | Não (workloads com estado) |
| Programabilidade | Lambda@Edge, CF Functions | EC2, ECS, RDS completos |

## Cache Behaviors, Origin Access Control e WAF

**Cache behaviors** definem como cachear por path (ex.: `/api/*` com cache curto, `/static/*` com cache longo). **Origin Access Control (OAC)** garante que só o CloudFront acessa o bucket S3 de origem, não o usuário diretamente — mecanismo de segurança independente do fluxo HTTPS já documentado acima. **WAF** integrado protege contra SQL Injection, XSS e bots maliciosos, além da proteção DDoS já registrada nesta página. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — cache behaviors por path, Origin Access Control e WAF como camada de proteção na borda
- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]] — combinação CloudFront + [[wiki/concepts/amazon-s3|S3]] citada como forma comum de hospedar um site inteiro só a partir de um arquivo estático (`index.html`) no bucket
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — CloudFront como caminho para servir um site estático do S3 via **HTTPS**: distribuição com origem no bucket (website endpoint), viewer "Redirect HTTP→HTTPS", Custom SSL do [[wiki/concepts/certificado-ssl-acm|ACM]] e alternate name = domínio; apontado pelo [[wiki/concepts/aws-route-53|Route 53]] via registro A/Alias. (Backend em Lambda/EC2 usaria [[wiki/concepts/load-balancer|Load Balancer]] no lugar.)
