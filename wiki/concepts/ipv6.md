---
type: concept
title: "IPv6"
aliases: ["ipv6","ip versão 6"]
date_created: 2026-09-30
date_updated: 2026-11-21
source_count: 2
tags: [networking, ipv6, camada-3, endereçamento]
skill: tech-mentor-networking
status: stub
---

# IPv6

Versão 6 do protocolo IP. Na fonte, é escolhido para o [[wiki/entities/icmp-browser]] por dois motivos: campo de dados de até ~65 KB e **facilidade de obter endereço IPv6 liberado num servidor** para expor o proxy. O ICMP correspondente é o **ICMPv6** (Echo Request tipo 128, Echo Reply 129) — ver [[wiki/concepts/icmp]].

Detalhes de operação (dual-stack, SLAAC, NAT64, regras ICMPv6 que não podem ser bloqueadas) estão em [skill: tech-mentor-networking — `references/ipv6-network-observability.md`]; a fonte não os aprofunda.

## FrontPUSH, hospedagem aula 02

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]], o IPv6 existe por causa da "internet das coisas", "muito dispositivo para pouco endereço", "mas a gente sempre está utilizando o IPv4". Duas ressalvas: o pool central de IPv4 esgotou em 2011 (não é só futuro), e boa parte dos acessos ao Google já chega por IPv6 `[external]` (https://www.google.com/intl/en/ipv6/statistics.html; média). Formato: 8 grupos de 16 bits em hexadecimal (slide: `3002:0bd6:0000:0000:0000:ee00:0033:6778`).

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — IPv6 como base do ICMP Browser (payload ~65 KB, endereço fácil em servidor)
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: IoT como motivo; "a gente não utiliza" envelheceu
