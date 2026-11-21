---
type: entity
title: "Registro.br"
aliases: ["registro.br", "registro br", "NIC.br"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [registrador, dominio, dns, br, nic-br]
skill: tech-mentor-networking
status: stub
---

# Registro.br

Serviço do NIC.br que registra e mantém os [[wiki/concepts/dominio|domínios]] sob `.br` (`.com.br`, `.app.br`, `.art.br`, `.blog.br` etc.) `[external]` (https://registro.br). Não vende `.com` nem outros TLDs genéricos; para esses, um registrador como a [[wiki/entities/godaddy]] ou a [[wiki/entities/hostinger]].

No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]) é "o órgão para poder a gente registrar o domínio no Brasil": a busca por frontpush.com.br mostra que "já está registrado no meu nome", e creatorpush.com.br e o domínio do autor também. O domínio fica "fixo apontando para um IP" via [[wiki/concepts/dns]].

## FrontPUSH, hospedagem aula 04

Em [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: "eu prefiro sempre pagar o meu domínio na Registro.br"; R$ 40 por um ano e R$ 76 por dois na tela; titularidade por CPF ou CNPJ; em domínios → DNS, os name servers da HostGator. O domínio grátis dos hosts passa por ela "no background" só para `.br`.

## FrontPUSH, hospedagem aula 05

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: "eu, Násser, prefiro deixar separado, porque quando eu vou modificar alguma coisa, eu vou modificar direto pelo Registro.br": registrar fora do host deixa a troca de host a uma edição de name servers.

## Key sources

- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: registro de domínios `.br`; FrontPUSH, CreatorPUSH e domínio do autor
- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: FrontPUSH, hospedagem aula 04: preços, titularidade e troca de servidores DNS
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: domínio separado do host
