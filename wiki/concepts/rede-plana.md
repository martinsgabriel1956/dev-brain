---
type: concept
title: "Rede Plana"
aliases: ["flat network", "rede única"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [networking, seguranca-de-rede, wifi]
skill: tech-mentor-networking
status: draft
---

# Rede Plana

Uma única rede (um domínio de broadcast / uma faixa de IP) onde clientes, PDV, financeiro, impressoras e câmeras se enxergam. É o padrão do roteador da operadora: um Wi-Fi, uma senha. Quem entra com a senha pode varrer tudo ([[wiki/concepts/pentest]] com Kali/scanner) — vira [[wiki/concepts/attack-surface]] máxima e [[wiki/concepts/blast-radius]] total. Remédio: [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]]. Em escala: o gargalo de AP também pega o sistema da empresa ([[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]]).

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
