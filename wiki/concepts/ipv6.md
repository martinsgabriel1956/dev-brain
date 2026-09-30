---
type: concept
title: "IPv6"
aliases: ["ipv6","ip versão 6"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, ipv6, camada-3, endereçamento]
skill: tech-mentor-networking
status: stub
---

# IPv6

Versão 6 do protocolo IP. Na fonte, é escolhido para o [[wiki/entities/icmp-browser]] por dois motivos: campo de dados de até ~65 KB e **facilidade de obter endereço IPv6 liberado num servidor** para expor o proxy. O ICMP correspondente é o **ICMPv6** (Echo Request tipo 128, Echo Reply 129) — ver [[wiki/concepts/icmp]].

Detalhes de operação (dual-stack, SLAAC, NAT64, regras ICMPv6 que não podem ser bloqueadas) estão em [skill: tech-mentor-networking — `references/ipv6-network-observability.md`]; a fonte não os aprofunda.

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — IPv6 como base do ICMP Browser (payload ~65 KB, endereço fácil em servidor)
