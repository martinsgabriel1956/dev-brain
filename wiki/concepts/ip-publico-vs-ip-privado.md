---
type: concept
title: "IP público × IP privado (RFC 1918 e NAT)"
aliases: ["ip publico", "ip privado", "rede privada", "rede pública", "rfc 1918", "nat", "network address translation"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 1
tags: [ip, ipv4, ip-publico, ip-privado, nat, cgnat, rfc-1918, networking]
skill: tech-mentor-networking
status: stub
---

# IP público × IP privado (RFC 1918 e NAT)

**IP privado** é um endereço das faixas reservadas pela RFC 1918, que nenhum roteador da internet encaminha: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` `[external]` (https://www.rfc-editor.org/rfc/rfc1918). Milhões de casas usam o mesmo `192.168.1.x` sem conflito, porque cada rede é isolada. **IP público** é roteável na internet e único no mundo naquele momento.

## NAT: como a casa sai para a internet

O roteador troca o IP privado de cada aparelho pelo IP público da conexão e anota a porta para devolver a resposta (NAT/PAT). Saída funciona; entrada não chega a ninguém sem regra de redirecionamento (*port forwarding*). Com **CGNAT**, o próprio provedor faz outro NAT e a casa nem tem IP público próprio `[skill: tech-mentor-networking]`. Na aula do FrontPUSH, isso aparece como "demodulação de uma rede privada para uma rede pública".

## Público ≠ fixo

Público × privado = roteável ou não. Fixo × dinâmico = muda ou não. A conexão de casa costuma ter IP público dinâmico; o servidor de hospedagem tem IP estável, que é o que o registro [[wiki/concepts/dns]] aponta. A aula junta os dois ("o IP público é fixo").

## Por que isso pede hospedagem

Site rodando em `192.168.1.92:5500` só é visto por quem está "no mesmo Wi-Fi". Para o mundo, falta IP público, porta aberta e máquina sempre ligada; a [[wiki/concepts/hospedagem-de-sites|hospedagem]] entrega os três. Ver [[wiki/concepts/localhost]], [[wiki/concepts/endereco-ip]].

## "Classes" no slide

O slide do FrontPUSH chama as faixas de "Classe A, B, C". As faixas estão certas, mas classes são do endereçamento anterior ao CIDR (1993) e cobrem blocos bem maiores; as privadas são só uma fatia de cada `[external]` (https://www.rfc-editor.org/rfc/rfc4632). Usar faixas diferentes para separar redes: [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]].

## Key sources

- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: rede privada × pública, "demodulação" (NAT), faixas como "classes", "o IP público é fixo"
