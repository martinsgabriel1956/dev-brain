---
type: concept
title: "ICMP (Internet Control Message Protocol)"
aliases: ["icmp","icmpv6","ping","echo request"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, icmp, ping, camada-3, diagnostico]
skill: tech-mentor-networking
status: draft
---

# ICMP

Protocolo da camada de rede (L3), acompanhante do IP, cuja função é **reportar erros e fazer diagnóstico**: se um pacote não chega, o ICMP gera a mensagem de erro para a origem (ex.: pacote grande demais para o roteador — ver [[wiki/concepts/mtu]]). O uso mais conhecido é o `ping` (Echo Request → Echo Reply).

## Estrutura e tipos

- O **primeiro byte** define o **tipo** da mensagem. Em **ICMPv6** ([[wiki/concepts/ipv6]]): **128 = Echo Request**, **129 = Echo Reply** [skill: tech-mentor-networking — `references/ipv6-network-observability.md`; RFC 4443 [external]]. Em ICMPv6 também há mensagens essenciais que não devem ser bloqueadas: NDP (tipos 133–137) e Packet Too Big.
- Depois do cabeçalho vêm identificador, número de sequência e um **campo de dados de conteúdo livre**; é esse campo que [[wiki/concepts/icmp-tunneling]] explora.
- Não há portas, conexão nem garantia de entrega/retransmissão: é **não confiável**, ao contrário do TCP ([[wiki/concepts/tcp-three-way-handshake]]).

## Cuidado prático

Uma interface que escuta ICMP recebe tráfego não solicitado (erros de roteadores, ruído); é preciso **filtrar por tipo**, como faz o [[wiki/entities/icmp-browser]].

Regra de firewall relacionada [skill: tech-mentor-networking — `references/linux-networking.md`]: filtrar ICMP tipo 3 código 4 quebra Path MTU Discovery (conexão abre e a transferência trava).

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — usado como canal de transporte de HTML no ICMP Browser; tipos 128/129 e filtragem por tipo
