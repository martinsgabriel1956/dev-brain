---
type: entity
title: "GoDaddy"
aliases: ["GoDaddy", "Go Daddy"]
date_created: 2026-08-12
date_updated: 2026-11-21
source_count: 2
tags: [registrador, dominio, dns, hosting]
skill: tech-mentor-networking
status: stub
---

# GoDaddy

Registrador de [[wiki/concepts/dominio|domínios]] (domain registrar). Além de vender o domínio, oferece o painel de **gerenciamento de DNS** onde se configuram os **name servers** — decidindo para qual DNS/servidor o domínio aponta.

## Contraste com a Registro.br

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]], o registro de domínio aparece pela [[wiki/entities/registro-br]], que só cuida de `.br`; para `.com` e outros TLDs genéricos, o caminho é um registrador como a GoDaddy.

## FrontPUSH, hospedagem aula 04

Em [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]], citada com a Locaweb entre as alternativas de hospedagem: "dá uma olhada lá e aí decide".

## Fontes na wiki

- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — registrador onde [[wiki/entities/fernanda-kipper]] comprou seu domínio antigo (`fernandakipper.com`, há 3+ anos). No painel da GoDaddy os name servers foram configurados para encaminhar ao servidor da [[wiki/entities/vercel]] (onde o site está hospedado); na demo AWS, os name servers são trocados pelos do [[wiki/concepts/aws-route-53|Route 53]].
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: Registro.br para .br; GoDaddy para TLDs genéricos (contraste)
- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: FrontPUSH, hospedagem aula 04: alternativa de hospedagem

*Nota de desambiguação:* não confundir com [[wiki/entities/hostinger]] (VPS/hosting), o outro provedor citado na mesma fonte, onde a autora mantém domínios mais novos.
