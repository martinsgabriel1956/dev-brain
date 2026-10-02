---
type: concept
title: "Segmentação de Rede por Faixa de IP e Firewall"
aliases: ["rede de convidados", "guest network", "isolamento de rede de clientes"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [networking, seguranca-de-rede, firewall, segmentacao, mikrotik]
skill: tech-mentor-networking
status: draft
---

# Segmentação de Rede por Faixa de IP e Firewall

Separar redes em faixas distintas (ex.: clientes 10.0.0.x, funcionários 172.16.0.x, empresa 192.168.0.x) com um ponto comum de saída — o [[wiki/entities/mikrotik]] — onde o firewall decide quem fala com quem. **A faixa de IP sozinha não protege; a regra de firewall protege.** Regra mínima: `/ip firewall filter add chain=forward src-address=<clientes> dst-address=<interna> action=drop` (`forward` = tráfego que atravessa o roteador). Versão com VLANs/SSID no mesmo AP é a alternativa ao 2º AP físico, mas perde a separação de [[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]]. [external, skill tech-mentor-networking `networking-infra-containers.md`] VLANs + firewall L3 entre elas é a forma padrão; em nuvem o análogo são subnets + Security Groups. Ver [[wiki/concepts/protecao-unidirecional-vs-bidirecional]], [[wiki/concepts/rede-plana]], [[wiki/concepts/defense-in-depth]].

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
