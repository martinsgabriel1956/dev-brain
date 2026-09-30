---
type: entity
title: "ICMP Browser"
aliases: ["icmp browser"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [icmp, go, proxy, prova-de-conceito, gambiarra]
skill: tech-mentor-networking
status: stub
---

# ICMP Browser

Projeto de [[wiki/entities/michel-leonardo]] (Go, IPv6): proxy que carrega páginas via [[wiki/concepts/icmp]] Echo Request/Reply. Duas partes: servidor ICMP (filtra tipo 128, baixa o HTML, fatia em 1024 B e responde) e cliente (escuta tipo 129, remonta e serve por um web server Go com templates). Limitações: sem imagens/fontes, lento, sem retransmissão; código na descrição do vídeo (não acessado). Conceitos: [[wiki/concepts/icmp-tunneling]], [[wiki/concepts/forward-proxy]], [[wiki/concepts/mtu]], [[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]].

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — descrição do projeto
