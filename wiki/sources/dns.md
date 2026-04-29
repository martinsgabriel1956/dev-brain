---
type: source
title: "DNS — Domain Name System"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/dns.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [dns, rede, infraestrutura, system-design]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

DNS traduz nomes legíveis em IPs. O fluxo percorre cache local → resolver recursivo → root NS → TLD NS → authoritative NS, cacheando cada nível pelo TTL. Entender TTL e tipos de registro é o que separa "funciona" de "funciona sem downtime em migrações".

## Claims Principais

| Claim | Confiança |
|---|---|
| O caminho completo só é percorrido na primeira resolução; subsequentes usam cache por TTL | Alta |
| Reduzir TTL 7 dias antes de trocar IP é a única forma segura de migrar sem downtime | Alta |
| CNAME não pode ser usado na raiz do domínio por conflito com registros NS/SOA; use ALIAS/ANAME | Alta |
| ISPs podem ignorar o TTL e cachear mais tempo — propagação não é garantida | Alta |
| Route 53 suporta failover, weighted, latency-based e geolocation routing via DNS | Alta |
| DNS não é load balancer confiável: sem health check nativo, IP morto continua sendo retornado | Alta |
| SPF, DKIM e DMARC são configurados via registros TXT e controlam autenticidade de email | Alta |

## Conceitos Abordados

- [[dns]]
- [[dns-ttl]]
- [[dns-record-types]]
- [[dns-routing-policies]]
- [[email-deliverability]]
- [[failover]]
- [[load-balancer]]
