---
type: concept
title: "MTU (Maximum Transmission Unit)"
aliases: ["mtu","unidade máxima de transmissão","path mtu"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, mtu, camada-2, camada-3, pmtud]
skill: tech-mentor-networking
status: draft
---

# MTU

**Unidade Máxima de Transmissão**: maior tamanho de pacote que um enlace/rota aceita sem dividi-lo. Em Ethernet o valor típico é **1500 bytes**; pode ser menor conforme a rede (túneis e VPN têm overhead: WireGuard ~1420, VXLAN ~1450) [skill: tech-mentor-networking — `references/linux-networking.md`].

## Por que importa

- Um payload maior que o MTU precisa ser dividido — ver [[wiki/concepts/fragmentacao-ip]] — ou o pacote é descartado com aviso [[wiki/concepts/icmp]] ("Packet Too Big" / "Fragmentation Needed").
- Mesmo que o campo de dados permita ~65 KB (limite de [[wiki/concepts/ipv6]] sem jumbograms), na prática o MTU é o teto real por pacote. É o "grande vilão" do vídeo de [[wiki/entities/michel-leonardo]], que fatia o HTML em 1024 bytes ([[wiki/concepts/icmp-tunneling]]).
- Bloquear ICMP quebra o **Path MTU Discovery** (PMTUD); sintoma clássico: conexão abre mas a transferência trava. Mitigação: TCP MSS clamping [skill: tech-mentor-networking].

Nota: a transcrição fonte diz "10000 bytes"; corrigido para ~1500 (ver raw).

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — MTU como limite que motiva o fatiamento em 1024 bytes
