---
type: entity
title: "FileZilla"
aliases: ["filezilla", "FileZilla Client", "FileZilla Server"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 2
tags: [ftp, sftp, ftps, cliente, ferramenta, hospedagem]
skill: tech-mentor-networking
status: stub
---

# FileZilla

Cliente de transferência de arquivos open source com suporte a FTP, FTPS e SFTP; existe também o FileZilla Server, que vem no [[wiki/entities/xampp]] `[external]` (https://filezilla-project.org; alta). Na conexão rápida pede host, usuário, senha e porta.

No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]): "indicado pelo próprio pessoal do HostGator"; com IP do servidor, usuário e senha, aparece `public_html`, "exatamente a mesma pasta" do gerenciador de arquivos do [[wiki/entities/cpanel]]. O aviso de conexão sem criptografia aparece "porque o FTP [...] não é criptografado", e a aula manda clicar em sim. Melhor: "FTP explícito sobre TLS" (FTPS) ou SFTP ([[wiki/concepts/ftp]]).

## Key sources

- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: serviço FileZilla no painel do XAMPP
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: upload do portfólio para public_html via FTP
