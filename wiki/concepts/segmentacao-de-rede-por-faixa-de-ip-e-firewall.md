---
type: concept
title: "Segmentação de Rede por Faixa de IP e Firewall"
aliases: ["rede de convidados", "guest network", "isolamento de rede de clientes"]
date_created: 2026-10-02
date_updated: 2026-11-21
source_count: 2
tags: [networking, seguranca-de-rede, firewall, segmentacao, mikrotik]
skill: tech-mentor-networking
status: draft
---

# Segmentação de Rede por Faixa de IP e Firewall

Separar redes em faixas distintas (ex.: clientes 10.0.0.x, funcionários 172.16.0.x, empresa 192.168.0.x) com um ponto comum de saída — o [[wiki/entities/mikrotik]] — onde o firewall decide quem fala com quem. **A faixa de IP sozinha não protege; a regra de firewall protege.** Regra mínima: `/ip firewall filter add chain=forward src-address=<clientes> dst-address=<interna> action=drop` (`forward` = tráfego que atravessa o roteador). Versão com VLANs/SSID no mesmo AP é a alternativa ao 2º AP físico, mas perde a separação de [[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]]. [external, skill tech-mentor-networking `networking-infra-containers.md`] VLANs + firewall L3 entre elas é a forma padrão; em nuvem o análogo são subnets + Security Groups. Ver [[wiki/concepts/protecao-unidirecional-vs-bidirecional]], [[wiki/concepts/rede-plana]], [[wiki/concepts/defense-in-depth]].

## Faixas privadas no FrontPUSH

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]], o slide lista as três faixas privadas (RFC 1918) como "Classe A/B/C"; as mesmas 10.x, 172.16.x e 192.168.x usadas aqui para separar redes. Ver [[wiki/concepts/ip-publico-vs-ip-privado]].

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: faixas privadas no slide
