---
type: concept
title: "Servidor Web vs. Servidor de Aplicação"
aliases: ['web server vs application server']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 5
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

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — `index.html` como documento padrão (escolha do servidor, não do browser)
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: Live Server (estático) x Express (aplicação)
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Live Server como servidor estático (FrontPUSH, Sass)
- [[wiki/sources/jstack-criando-o-servidor-http]]: Node como servidor HTTP direto
