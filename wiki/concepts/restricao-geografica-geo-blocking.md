---
type: concept
title: "Restrição Geográfica (Geo-blocking)"
aliases: ["geo-blocking", "geoblocking", "bloqueio geográfico", "restrição geográfica de conteúdo"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [networking, vpn, geo-blocking, censura, streaming]
skill: tech-mentor-networking
status: stub
---

# Restrição Geográfica (Geo-blocking)

Prática de bloquear ou liberar acesso a um recurso de rede com base na localização geográfica inferida do usuário — tipicamente via IP de origem. Usada tanto por governos (censura de conteúdo, como o bloqueio de serviços ocidentais na China) quanto por empresas (licenciamento de conteúdo por região em serviços de streaming).

## Bypass via VPN

Uma [[wiki/concepts/vpn]] permite contornar geo-blocking: o tráfego do usuário sai pelo IP do servidor do provedor de VPN, que pode estar localizado numa região sem a restrição. Do ponto de vista do serviço bloqueado, o acesso parece vir do provedor de VPN, não do usuário real.

**Trade-off não coberto pela fonte introdutória que originou esta página:** serviços de streaming e alguns governos mantêm listas de IPs conhecidos de provedores de VPN e os bloqueiam ativamente — uma corrida armamentista entre detecção de IP de VPN e rotação de IPs pelos provedores.

## Relação com outros conceitos

- [[wiki/concepts/vpn]] — mecanismo mais comum de bypass

## Key sources

- [[wiki/sources/vpn-conceito-tunelamento-acesso-remoto]] — exemplo do uso de VPN para acessar recursos bloqueados geograficamente (caso China)
