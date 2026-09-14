---
type: concept
title: "Tunelamento (Tunneling)"
aliases: ["tunneling", "túnel virtual", "vpn tunnel"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [networking, vpn, criptografia, tunelamento]
skill: tech-mentor-networking
status: stub
---

# Tunelamento (Tunneling)

Processo de encapsular tráfego de rede criptografado dentro de uma conexão que trafega sobre uma infraestrutura de rede pública (como a internet), criando um "túnel virtual" lógico isolado do restante do tráfego que passa pela mesma infraestrutura física.

É o mecanismo que torna uma [[wiki/concepts/vpn]] "virtual": a rede continua privada (acesso restrito) mas não precisa de um link físico dedicado — o túnel é uma abstração sobre a rede pública.

## Exemplo prático (WireGuard)

Em implementações modernas como WireGuard, o túnel é uma interface de rede (`wg0`) com endereço próprio; cada peer define `AllowedIPs`, que funciona como tabela de roteamento — determinando que tráfego entra e sai pelo túnel. `PersistentKeepalive` mantém o túnel ativo através de NAT.

## Relação com outros conceitos

- [[wiki/concepts/vpn]] — o produto final que o tunelamento viabiliza
- [[wiki/concepts/criptografia]] — os dados dentro do túnel trafegam cifrados, tipicamente com criptografia simétrica (AES) após um handshake assimétrico inicial

## Key sources

- [[wiki/sources/vpn-conceito-tunelamento-acesso-remoto]] — definição introdutória do túnel virtual como mecanismo central da VPN
