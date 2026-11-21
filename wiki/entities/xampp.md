---
type: entity
title: "XAMPP"
aliases: ["xampp", "Apache Friends"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 1
tags: [ambiente-local, apache, php, mysql, mariadb, ferramenta]
skill: tech-mentor-networking
status: stub
---

# XAMPP

Pacote da Apache Friends que instala de uma vez [[wiki/entities/apache-http-server|Apache]], MariaDB (o "MySQL" do painel), [[wiki/entities/php|PHP]] e Perl, mais FileZilla FTP, Mercury (e-mail) e Tomcat, com um painel para ligar e desligar cada serviço `[external]` (https://www.apachefriends.org; alta). Os arquivos servidos ficam em `htdocs`, e `http://localhost/pasta` abre a pasta correspondente.

No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]): `http://localhost/frontpush` não abre até o autor dar "start" no Apache, que sobe "na porta 80 e na porta 443"; aí o site em PHP roda. "Para poder rodar o PHP, eu só preciso do Apache" (o PHP já vem no pacote). Ver [[wiki/concepts/localhost]], [[wiki/concepts/porta-de-rede]].

## Key sources

- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: Apache ligado no painel para rodar o FrontPUSH em PHP
