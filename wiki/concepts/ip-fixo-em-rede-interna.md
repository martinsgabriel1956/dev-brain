---
type: concept
title: "IP Fixo na Rede Interna"
aliases: ["IP estático", "endereçamento estático interno"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [networking, seguranca-de-rede, firewall]
skill: tech-mentor-networking
status: draft
---

# IP Fixo na Rede Interna

Atribuir IPs fixos aos equipamentos internos (ex.: .10 PDV, .20 financeiro, .30 impressora, .40 DVR, .50+ câmeras) permite regras de firewall **por host** e deixa a rede previsível. **Ressalva** [inferência, não dita no vídeo]: não impede quem já está na mesma LAN de escolher um IP manualmente — o ganho real vem de a rede de clientes estar em outra faixa e atrás do firewall ([[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]]); o equivalente forte é reserva DHCP + filtro por MAC/porta. Ver [[wiki/concepts/least-privilege]].

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
