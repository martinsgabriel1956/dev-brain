---
type: concept
title: "Endereço IP (IPv4 / IPv6)"
aliases: ["IP", "endereço IP", "IPv4", "IPv6", "IP address"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [rede, endereco-ip, ipv4, ipv6, tcp-ip, cs-fundamentals]
skill: tech-mentor-networking
status: stub
---

# Endereço IP (IPv4 / IPv6)

**Sequência numérica que identifica um dispositivo dentro de uma rede** — que pode ser uma rede privada (computadores que só conversam entre si) ou a internet. Analogia clássica: o IP é como a rua + número de uma casa, dizendo *onde* está o dispositivo na topologia da rede. Complementa a [[wiki/concepts/porta-de-rede|porta de rede]]: o IP diz *qual host*, a porta diz *qual serviço dentro daquele host* (`IP:porta`). E é o alvo da resolução feita pelo [[wiki/concepts/dns|DNS]] — o [[wiki/concepts/dominio|domínio]] existe só para não precisarmos decorar o IP.

## IPv4

Versão 4 do protocolo da internet. Seu maior padrão é o **formato do endereço**:

```
192.168.1.1
└── 4 octetos separados por ponto, cada um de 0 a 255 (8 bits) ──┘

Total = 2³² ≈ 4,3 bilhões de endereços
```

Como o espaço é finito e já existem ~bilhões de dispositivos conectados, os endereços IPv4 estão se **esgotando** (IANA esgotou o pool central em 2011 `[skill: tech-mentor-networking]`). Ainda é a versão dominante — suportada por todos os servidores.

> Nota: a fonte [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] fala em "0 a 256"; o intervalo correto de cada octeto é **0 a 255**. O teto de ~4,3 bilhões que ela cita, esse sim, está correto (2³²).

## IPv6

Versão 6, criada para resolver o esgotamento. Novo formato: 128 bits (2¹²⁸ endereços), 8 grupos de 4 hexadecimais separados por `:` (ex.: `2001:db8::ff00:42:8329`). Adoção **gradual** por provedores de nuvem e de internet — hoje há **coexistência (dual-stack)** com IPv4, e "endereço IP" no dia a dia ainda quase sempre significa IPv4. `[skill: tech-mentor-networking — references/ipv6-network-observability.md]`

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — IP como sequência que identifica dispositivo; IPv4 (4 octetos, ~4,3 bi) vs IPv6; coexistência
