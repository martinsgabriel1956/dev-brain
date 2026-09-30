---
type: concept
title: "ICMP Tunneling"
aliases: ["tunelamento icmp","canal encoberto icmp","ping tunnel"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, icmp, tunelamento, covert-channel, gambiarra]
skill: tech-mentor-networking
status: stub
---

# ICMP Tunneling

Técnica de transportar dados arbitrários dentro do **campo de dados** de mensagens [[wiki/concepts/icmp]] (tipicamente Echo Request/Reply), tratando o ping como canal de transporte. Parente de [[wiki/concepts/tunelamento]] (encapsulamento de um protocolo em outro), mas **sem criptografia** por padrão, ao contrário de [[wiki/concepts/vpn]].

## Como o ICMP Browser faz

[[wiki/entities/icmp-browser]]: cliente envia um Echo Request com a URL no campo de dados; o servidor baixa a página, fatia em 1024 bytes e responde com vários Echo Reply, cada um com **4 bytes de total de pedaços + payload**, usando o número de sequência para ordenar ([[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]]). Falta de garantia de entrega obriga a aceitar perdas ([[wiki/concepts/fragmentacao-ip]]).

## Ideia irmã: DNS

A inspiração do autor veio de alguém que rodou Doom sobre [[wiki/concepts/dns]], outro protocolo "auxiliar" reaproveitado como transporte.

## Nota de segurança (inferência, não da fonte)

Canais encobertos sobre ICMP/DNS são conhecidos como forma de contornar controles de saída; por isso firewalls costumam limitar ICMP. Cf. [[wiki/concepts/pentest]] [external, não verificado].

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — ICMP como transporte de HTML; formato de mini-protocolo sobre o campo de dados
