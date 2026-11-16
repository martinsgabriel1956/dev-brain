---
type: concept
title: "Endereço IP (IPv4 / IPv6)"
aliases: ["IP", "endereço IP", "IPv4", "IPv6", "IP address"]
date_created: 2026-08-12
date_updated: 2026-11-16
source_count: 6
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

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: nomes como youtube.com são "convertidos para números depois, e esses números nós chamamos de endereço de IP", endereços únicos que mostram onde está o servidor. `localhost` e `127.0.0.1` são a própria máquina. Ver [[wiki/concepts/dns]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: "localhost na verdade ele não existe para o seu celular". O app e as URLs de imagem passam a usar o IP local (`192.168.1.13`), e o emulador Android usa `10.0.2.2`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], o IP local mudou de .13 para .12 entre os dias, e foi preciso editar a `image_url` no código.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], localhost é 127.0.0.1, igual em toda máquina, e um domínio "é transformado no endereço de IP deles". A aula diz que o IP "sempre é único"; endereços públicos podem ser compartilhados (NAT) e um domínio responde por vários IPs.

## Na NLW #2, dia 5 (Diego Fernandes)

`baseURL` com o IP local (`192.168.x.x:3333`) em vez de `localhost`, que no emulador e no aparelho aponta para o próprio dispositivo; no emulador Android, `10.0.2.2` também serve. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — IP como sequência que identifica dispositivo; IPv4 (4 octetos, ~4,3 bi) vs IPv6; coexistência
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: nome → IP; localhost/127.0.0.1
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: localhost x IP da máquina no app
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: IP mudou durante a semana
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: localhost e domínio
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: IP local no app
