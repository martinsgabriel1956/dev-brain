---
type: entity
title: "PHP"
aliases: ["php", "PHP: Hypertext Preprocessor"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [linguagem, backend, server-side, hospedagem-compartilhada]
skill: tech-mentor-networking
status: stub
---

# PHP

Linguagem executada no servidor que gera o HTML a cada requisição; o navegador só recebe o resultado, nunca o código PHP. Roda ligada a um servidor web: `mod_php` no [[wiki/entities/apache-http-server|Apache]], PHP-FPM com Apache ou Nginx, ou o servidor embutido `php -S` para desenvolvimento `[external]` (https://www.php.net/manual/en/features.commandline.webserver.php). Vem pronta na hospedagem compartilhada (cPanel, [[wiki/entities/hostgator]], [[wiki/entities/hostinger]]), o que explica parte da sua presença na web.

## No FrontPUSH

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], o site do [[wiki/entities/frontpush|FrontPUSH]] "é uma aplicação que está desenvolvida em PHP"; "o browser não entende PHP, ele precisa de um servidor Apache", ligado no [[wiki/entities/xampp]]. O PHP é "um pouco mais simples" que React + MySQL: "só precisa do servidor Apache". Rigorosamente, precisa do interpretador PHP, que o XAMPP já traz. Ver [[wiki/concepts/site-estatico-vs-dinamico]] (PHP é dinâmico no sentido do servidor) e [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]].

## FrontPUSH, hospedagem aula 05

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: "muitas coisas do PHP já vêm pré-instaladas" e dá para escolher a versão do PHP no cPanel; "a tecnologia que eu estou mexendo é o PHP, eu indico" a hospedagem compartilhada.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]], por que o FrontPUSH é PHP: "outras páginas" (cadastro, lista de espera) e "para fazer uma rota em React, eu tenho que configurar todo um ecossistema, com PHP é bem mais fácil"; subir é igual a um estático (`index.php`). Navegação entre páginas não exige PHP; o formulário e os `include` exigiriam (inferência).

## Key sources

- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH feito em PHP; "precisa do Apache"
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: PHP pronto no compartilhado
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: por que o FrontPUSH é PHP
