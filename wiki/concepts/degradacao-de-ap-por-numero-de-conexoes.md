---
type: concept
title: "Degradação de AP por Número de Conexões"
aliases: ["limite de clientes por AP", "AP saturado"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [networking, wifi, resiliencia, dominio-de-falha]
skill: tech-mentor-networking
status: draft
---

# Degradação de AP por Número de Conexões

Roteadores/APs domésticos e de pequeno porte funcionam bem até ~50 conexões simultâneas (regra prática do autor, 'não importa o preço'); acima disso o sinal oscila e o tráfego degrada. Em rede única ou AP multi-SSID, o pico de clientes derruba também o sistema da empresa → prejuízo operacional. Por isso: **um AP para clientes, outro para a empresa** — separa o domínio de falha, não só a segurança ([[wiki/concepts/blast-radius]]). [external, skill `wireless-mobile-networking.md`] Wi-Fi 6 (OFDMA) melhora densidade, mas o limite varia por modelo; para salões cheios usam-se APs gerenciados em número maior. Ver [[wiki/concepts/rede-plana]].

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
