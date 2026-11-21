---
type: entity
title: "cPanel"
aliases: ["cpanel", "painel de controle da hospedagem"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [hospedagem-compartilhada, painel, dns, ssl, ftp, ferramenta]
skill: tech-mentor-networking
status: stub
---

# cPanel

Painel de controle comercial usado por boa parte da hospedagem compartilhada (HostGator, entre outras): domínios adicionais, zona DNS, certificados (AutoSSL), bancos MySQL, contas FTP, e-mail e instaladores como o de WordPress `[external]` (https://docs.cpanel.net; alta). Cada plano tem um usuário cPanel, cujas credenciais chegam no e-mail de boas-vindas.

No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]) é "meio que o painel geral para você adicionar um novo domínio, instalar o certificado, instalar um banco de dados, ou então instalar o WordPress". O e-mail técnico da [[wiki/entities/hostgator]] traz "o IP do servidor [...] e o usuário e a senha" dele. Com o domínio delegado aos [[wiki/concepts/name-server|name servers]] do host, a zona DNS também é editada aqui.

## FrontPUSH, hospedagem aula 05: o tour

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: acesso por "domínio principal [...] barra cPanel"; phpMyAdmin e "banco de dados MySQL"; gerenciador de arquivos e `public_html`; conta FTP; controle de Git; domínios adicionados; contas de e-mail no próprio domínio; métricas e largura de banda; SSH; bloqueador de IP; SSL grátis (AutoSSL) nos três domínios; versão do PHP e instalador de WordPress. Os principais, para o autor: arquivos, banco, domínios e SSL.

## FrontPUSH, hospedagem aula 06: upload, domínios adicionais e AutoSSL

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: "carregar" no gerenciador de arquivos para `public_html`; "domínios adicionais" com raiz em `public_html/frontpush` e `public_html/creatorpush` ([[wiki/concepts/virtual-host]]); "status do certificado SSL barra TLS" verde/vermelho e "executar AutoSSL".

## Key sources

- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: painel geral; credenciais no e-mail técnico
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: tour pelos recursos
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: upload, addon domains, AutoSSL
