---
type: concept
title: "Name server e delegação DNS"
aliases: ["name server", "nameserver", "servidor DNS autoritativo", "registro NS", "delegação de domínio", "servidores DNS do domínio"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [dns, name-server, delegacao-dns, propagacao-dns, dominio, hospedagem, networking]
skill: tech-mentor-networking
status: stub
---

# Name server e delegação DNS

**Name server autoritativo** é o servidor que responde, com autoridade, pelos registros de uma zona (A, AAAA, CNAME, MX, TXT...). **Delegar** um domínio é dizer ao registro do TLD quais servidores são esses: a Registro.br grava, na zona `.br`, registros NS como `frontpush.com.br NS nspro34.hostgator.com.br` `[skill: tech-mentor-networking]`. Na resolução, o resolver desce raiz → TLD → name server delegado e só ali encontra o IP ([[wiki/concepts/dns]]).

## Na prática da hospedagem

| Caminho | O que se faz no registrador | Onde se edita a zona |
|---|---|---|
| Delegar ao host | troca os name servers pelos do host (ex.: `nspro34`/`nspro35.hostgator.com.br`) | no painel do host ([[wiki/entities/cpanel]]) |
| Manter o DNS do registrador | cria um registro A com o IP do servidor | no próprio registrador |

O [[wiki/entities/frontpush|FrontPUSH]] usa o primeiro ([[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]): "eu peguei esses carinhas aqui, nspro34.hostgator.com.br e o 35 e coloquei como servidores DNS"; trocou de host, troca de novo. O autor chama o name server de "meio que um IP"; é um nome, que resolve para um IP.

## Dois servidores

Primário e secundário ("master e slave" na aula) dão redundância: se um cai, o outro responde. O TLD exige pelo menos dois.

## Propagação

Trocar os NS é instantâneo no registrador; o atraso ("algumas horas") é o cache dos resolvers que guardaram a delegação antiga até o [[wiki/concepts/ttl]] vencer. Antes de trocar, a zona já deve existir no novo servidor, senão o site some no intervalo.

Ver também [[wiki/concepts/dominio]], [[wiki/entities/registro-br]], [[wiki/concepts/hospedagem-de-sites]].

## FrontPUSH, hospedagem aula 05

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: "um precisa combinar com o outro. Não adianta nada eu digitar www.frontpush.com.br e ele não apontar para os servidores do HostGator". A delegação à HostGator é também o que faz o e-mail `@frontpush.com.br` funcionar (o DNS dela publica o MX).

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]], FrontPUSH e CreatorPUSH "apontam também para esse mesmo servidor DNS", pré-requisito para o domínio adicional e para o AutoSSL validar o domínio.

## Key sources

- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: name servers da HostGator na Registro.br; "master e slave"; "demora algumas horas"
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: "um precisa combinar com o outro"
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: delegação como pré-requisito do domínio adicional
