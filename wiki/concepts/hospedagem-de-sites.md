---
type: concept
title: "Hospedagem de sites"
aliases: ["hospedagem", "web hosting", "hosting", "hospedagem de websites"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 6
tags: [hospedagem, deploy, cloud, paas, site-estatico, networking]
skill: tech-mentor-networking
status: stub
---

# Hospedagem de sites

Serviço que mantém os arquivos (ou o processo) de um site num servidor ligado o tempo todo, com IP público e, em geral, domínio e certificado TLS. É o que faltava ao site que "roda no seu computador" e "ninguém consegue acessar": a máquina de casa tem IP privado atrás do NAT e não fica sempre ligada (ver [[wiki/concepts/localhost]], [[wiki/concepts/endereco-ip]]).

## Três famílias (pela grade do FrontPUSH)

| Família | Exemplos | Serve | Como sobe |
|---|---|---|---|
| Tradicional / compartilhada | [[wiki/entities/hostgator]], [[wiki/entities/hostinger]], Locaweb | estático e PHP; VPS à parte | painel, FTP/SFTP |
| Plataformas de front-end e PaaS | GitHub Pages ([[wiki/entities/github]]), [[wiki/entities/netlify]], [[wiki/entities/vercel]], [[wiki/entities/heroku]] | Pages: só estático; Netlify/Vercel: estático + funções; Heroku: processos | push no Git |
| Grandes clouds | [[wiki/entities/amazon-web-services]], [[wiki/entities/google-cloud-platform]], Azure ([[wiki/entities/microsoft]]) | qualquer coisa, peça a peça | console, CLI, IaC |

O slide da aula classifica GitHub, Netlify e Heroku como "Gratuitos*"; o free da Heroku acabou em 2022 `[external]` (https://blog.heroku.com/next-chapter).

## Site × aplicação web

"O website você upa ele e ele vai funcionar"; "a aplicação web necessita de mais configurações" ([[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]). Na prática a linha passa entre servir arquivos e executar código no servidor: ver [[wiki/concepts/site-estatico-vs-dinamico]] e [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]].

## Peças que acompanham

[[wiki/concepts/dominio]] e [[wiki/concepts/dns]] (nome → IP), [[wiki/concepts/http-vs-https]] (certificado), [[wiki/concepts/cdn]] (plataformas de front-end publicam em CDN), [[wiki/concepts/deploy-strategies]].

## FrontPUSH, hospedagem aula 02

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: "precisa de um IP público, porque senão a gente não consegue, de fato, hospedar na internet"; FrontPUSH, CreatorPUSH e o domínio do autor apontam para o mesmo servidor da HostGator (`162.241.61.29`). Ver [[wiki/concepts/ip-publico-vs-ip-privado]].

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], o tipo de projeto define a hospedagem: estático é "copiar e colar [...] em uma determinada pasta"; aplicação web pede instalar, configurar e, "na maioria das vezes", terminal; PHP vem pronto em HostGator e Hostinger "configurado na porta 80". Um build de React também sobe como estático.

## FrontPUSH, hospedagem aula 04

Em [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]], o fluxo tradicional: escolher host e plano (Turbo da HostGator), guardar o e-mail técnico (name servers, IP, acesso ao [[wiki/entities/cpanel]]), registrar o domínio na [[wiki/entities/registro-br]] e delegá-lo ([[wiki/concepts/name-server]]); arquivos na parte 2.

## FrontPUSH, hospedagem aula 05

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]], a hospedagem compartilhada como pacote pronto: banco, arquivos, FTP, e-mail, SSL e instalador de WordPress no [[wiki/entities/cpanel]], contra o "servidor cru" em que "você teria que instalar tudo isso na mão". Indicada para PHP/WordPress.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]], o fluxo completo na compartilhada: arquivos em `public_html` (gerenciador ou FTP), outros projetos em subpastas, outros domínios como domínios adicionais ([[wiki/concepts/virtual-host]]) e HTTPS por AutoSSL.

## Key sources

- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: definição, grade do módulo, slide dos principais sites
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: hospedar exige IP público
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: o que o projeto exige do host
- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: FrontPUSH, hospedagem aula 04: plano, e-mail técnico, domínio, delegação
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: compartilhada pronta × servidor cru
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: upload, subpastas, domínios adicionais, AutoSSL
