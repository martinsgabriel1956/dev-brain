---
type: concept
title: "Virtual host (vários sites no mesmo servidor)"
aliases: ["virtual host", "vhost", "name-based virtual hosting", "domínio adicional", "addon domain", "vários sites no mesmo servidor"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 2
tags: [virtual-host, apache, nginx, host-header, sni, tls, hospedagem-compartilhada, networking]
skill: tech-mentor-networking
status: stub
---

# Virtual host (vários sites no mesmo servidor)

Um único servidor web, num único IP e porta, serve sites diferentes conforme o **nome** pedido: o navegador manda o domínio no cabeçalho `Host` do HTTP, e o servidor escolhe a pasta (*document root*) correspondente. No HTTPS, o nome também segue no **SNI** do handshake TLS, para o servidor escolher o certificado certo antes de ver o `Host` `[skill: tech-mentor-networking]` (alta). No Apache é `<VirtualHost>` com `ServerName`; no Nginx, `server_name`.

## No cPanel: domínio adicional

O "domínio adicional" (*addon domain*) do [[wiki/entities/cpanel]] é um virtual host de painel: escolhe-se o domínio e a pasta raiz. No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]), o portfólio do autor fica em `public_html`, e `frontpush.com.br` e `creatorpush.com.br` apontam para `public_html/frontpush` e `public_html/creatorpush`: "quando você receber esse domínio como requisição, eu quero que você direcione ele para uma outra pasta". Efeito colateral: com a raiz dentro de `public_html`, o site também abre como subpasta do domínio principal.

Pré-requisito: o domínio já resolver para o servidor ([[wiki/concepts/name-server]], [[wiki/concepts/dns]]).

## Consequências

- **Acessar pelo IP** cai no site padrão do servidor, não no seu, quando o IP é compartilhado ([[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]).
- **Subpasta × domínio:** `/Nubank` e `/Spider-Man` no FrontPUSH são só diretórios do mesmo virtual host; ganhar domínio próprio é criar outro.

Ver também [[wiki/concepts/hospedagem-de-sites]], [[wiki/entities/apache-http-server]], [[wiki/concepts/http-vs-https]].

## Key sources

- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: "como colocar vários sites no mesmo servidor" anunciado
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: domínios adicionais no cPanel com raiz em subpastas de public_html
