---
type: concept
title: "Servidor Web vs. Servidor de Aplicação"
aliases: ['web server vs application server']
date_created: 2026-10-14
date_updated: 2026-11-21
source_count: 8
tags: [web, backend, servidor, infra]
skill: tech-mentor-frontend
status: draft
---

# Servidor Web vs. Servidor de Aplicação

- **Servidor web** (Apache, Nginx): função principal é servir arquivos/páginas HTML.
- **Servidor de aplicação** (ex.: servidores Java/J2EE): função principal é **executar programas que cospem HTML**.
- Todo servidor de aplicação é também um servidor web, mas nem todo servidor web é de aplicação.

O servidor mais simples mapeia URL → caminho de arquivo sem checagem, o que é problema de segurança (acesso a arquivos não públicos). Origem: [[wiki/concepts/cgi-common-gateway-interface]]; ver [[wiki/entities/apache-http-server]], [[wiki/concepts/porta-de-rede]], [[wiki/concepts/historia-do-front-end]].

## index.html como página inicial

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], `index.html` é "um padrão da internet": o browser identifica o arquivo como a primeira página do site. `[external]` Quem resolve isso é o servidor web, que serve o documento padrão do diretório quando a URL não nomeia arquivo (no Apache, `DirectoryIndex`): https://httpd.apache.org/docs/2.4/mod/mod_dir.html.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] mostra que o Live Server "criou para você um servidor" na porta 5500, mas ele só serve arquivos. O Express com rotas e templates é o primeiro servidor de aplicação do Ecoleta; o `express.static("public")` cuida da parte de arquivos estáticos.

## Live Server no FrontPUSH

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o Live Server é o "servidorzinho em localhost" que serve o HTML e recarrega ao salvar: servidor estático, como na NLW.

## No JStack, aula 04

Em [[wiki/sources/jstack-criando-o-servidor-http]], o próprio processo Node é o servidor HTTP: `http.createServer` + `listen(3000)`, sem Nginx ou Apache na frente. Em produção é comum pôr um proxy reverso antes dele (TLS, arquivos estáticos, compressão).

## FrontPUSH, hospedagem aula 01

Em [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]], de novo "o próprio browser faz isso" sobre o `index.html`; é o servidor que serve o documento padrão. A aula também separa website ("você upa ele") de aplicação web ("necessita de mais configurações"), a mesma linha entre servir arquivos e executar código ([[wiki/concepts/hospedagem-de-sites]]).

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], "o PHP precisa do Apache para rodar": o FrontPUSH em PHP só abre em `http://localhost/frontpush` depois de ligar o Apache no [[wiki/entities/xampp]]. Precisões: quem executa é o interpretador PHP (`mod_php`/PHP-FPM), e com o Apache desligado nem um HTML puro abriria; a demo mostra falta de servidor, não de PHP.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]], desta vez certo: "quando ele ver index.html, por padrão, ele já vai executar" (é o servidor que serve o documento padrão). O FrontPUSH em PHP sobe igual a um estático porque a HostGator já tem Apache com PHP; "não se engane".

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — `index.html` como documento padrão (escolha do servidor, não do browser)
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: Live Server (estático) x Express (aplicação)
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Live Server como servidor estático (FrontPUSH, Sass)
- [[wiki/sources/jstack-criando-o-servidor-http]]: Node como servidor HTTP direto
- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: FrontPUSH, hospedagem aula 01: index.html atribuído ao browser outra vez; site × aplicação
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: PHP + Apache no XAMPP
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: index.html padrão; PHP sobe igual a estático
