---
type: concept
title: "AWS Route 53"
aliases: ["Route 53", "Route53", "AWS Route 53", "hosted zone"]
date_created: 2026-08-12
date_updated: 2026-08-17
source_count: 2
tags: [aws, dns, route-53, hosted-zone, rede, infra]
skill: tech-mentor-networking
status: stub
---

# AWS Route 53

Serviço da [[wiki/entities/amazon-web-services|AWS]] para **gerenciamento de domínios e DNS**, usado para rotear um [[wiki/concepts/dominio|domínio]] para aplicações rodando na AWS. É a implementação AWS dos conceitos gerais de [[wiki/concepts/dns|DNS]].

## Hosted zone (zona hospedada)

Um mapeamento do domínio, criado com o nome **exato** do domínio registrado (nome personalizado + TLD corretos). Ao criar, o Route 53 gera **registros NS (Name Server)** — os servidores para os quais o tráfego DNS deve ser roteado.

- **Pública** — domínio acessível por qualquer um na internet.
- **Privada** — acessível só de dentro de uma rede (ex.: VPN da empresa); é o padrão dos sites internos que só abrem conectado à VPN.

## Fluxo de apontamento

1. Criar hosted zone → obter os 4 name servers da AWS.
2. No **registrador** ([[wiki/entities/godaddy]] / [[wiki/entities/hostinger]]) trocar os name servers do domínio pelos da AWS. Isso exige **propagação DNS** (minutos, replicando para os DNS do mundo).
3. Criar registros dentro da zona:
   - **Alias → site do S3** para apontar direto ao [[wiki/concepts/amazon-s3|bucket]] (só HTTP).
   - **CNAME** para cadastrar o valor de validação do [[wiki/concepts/certificado-ssl-acm|certificado do ACM]].
   - **Registro A → Alias → distribuição [[wiki/concepts/aws-cloudfront|CloudFront]]** para servir via HTTPS.

> O registro **Alias** do Route 53 existe justamente para permitir apontar o apex do domínio (`exemplo.com`) para um recurso AWS — algo que um CNAME comum não pode no apex. `[skill: tech-mentor-networking — references/dns-advanced.md]`

## Roteamento Inteligente

Além de resolver domínio em IP, Route 53 suporta roteamento por **latência** (direciona o usuário ao endpoint mais rápido para ele), **localização geográfica**, e **failover automático** — se um endpoint cair, o tráfego é redirecionado sem intervenção manual. Complementa o fluxo de apontamento já documentado nesta página. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — hosted zone pública/privada, geração de name servers, registros Alias/CNAME/A para S3 e CloudFront
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — roteamento por latência, localização e failover automático
