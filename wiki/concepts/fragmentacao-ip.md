---
type: concept
title: "Fragmentação IP"
aliases: ["fragmentação de pacotes","ip fragmentation"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, ip, fragmentacao, mtu, confiabilidade]
skill: tech-mentor-networking
status: stub
---

# Fragmentação IP

Divisão de um pacote maior que o [[wiki/concepts/mtu]] em fragmentos, remontados no destino. Ponto fraco explicado na fonte: **basta perder um fragmento para o sistema operacional de destino descartar os demais**, porque o pacote original não pode ser reconstruído; sem retransmissão ([[wiki/concepts/icmp]] não tem, ao contrário do TCP), perde-se o pacote inteiro. Um download que falha por uma oscilação de Wi-Fi é o exemplo cotidiano dado.

Estratégia de contorno no [[wiki/entities/icmp-browser]]: aplicação divide **antes** do IP (pedaços de 1024 bytes), então cada resposta cabe em um pacote e a perda afeta só um pedaço; a remontagem passa a ser da aplicação ([[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]]).

Ressalva [external, não verificada nesta sessão]: em IPv6 só a origem fragmenta (roteadores intermediários não), diferente do IPv4 — a fonte não distingue os casos.

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — fragmentação, perda de um fragmento invalida o pacote, contorno por fatiamento na aplicação
