---
type: source
title: "A história do front end (Akita — episódio 4 do Developer World Map)"
aliases: ["história do front end", "akita front end", "akita ep 4"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/historia-do-front-end-akita-ep4.md
source_url: ""
author: "Fábio Akita"
date_published: ""
date_ingested: 2026-10-14
source_count: 1
tags: [frontend, historia, web, css, javascript, spa, build, fabio-akita, fundamentos]
skill: tech-mentor-frontend
status: stable
---

## TL;DR

[[wiki/entities/fabio-akita]] explica a "sopa de letrinhas" do front end contando a história da web em vez de listar o que estudar: [[wiki/concepts/historia-do-front-end]]. Cadeia: servidor de arquivos → [[wiki/concepts/cgi-common-gateway-interface|CGI]] → templates/[[wiki/concepts/css|CSS]] → [[wiki/concepts/guerra-dos-navegadores]] → [[wiki/concepts/framework-web|frameworks]] (Rails) → [[wiki/concepts/ajax]]/[[wiki/entities/gmail|Gmail]] → iPhone mata [[wiki/concepts/plugin-de-navegador|plugins]] → HTML5/CSS3 → [[wiki/concepts/transpilador|transpiladores]], [[wiki/concepts/gerenciador-de-pacotes]], [[wiki/concepts/pipeline-de-assets]] → [[wiki/concepts/single-page-application|SPAs]] e [[wiki/concepts/aplicativo-hibrido|híbridos]]. Método de estudo: perguntar a história e o problema que a tecnologia resolve.

## Key Claims

**Claim:** Servidor web mais simples = URL mapeada a arquivo; sem checagem é inseguro. **Evidence:** exemplo `~usuario`. **Confidence:** alta. Ver [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]], [[wiki/concepts/porta-de-rede]], [[wiki/concepts/dns]].

**Claim:** CGI (executar programa e devolver HTML) criou a web dinâmica; Perl dominou; Apache (open source, "patchy") venceu; PHP e ASP embutiram lógica no servidor. **Confidence:** alta. [external] RFC 3875 (https://www.rfc-editor.org/rfc/rfc3875). Ver [[wiki/entities/apache-http-server]], [[wiki/concepts/regex-expressao-regular]].

**Claim:** HTML marcava estrutura (herança SGML); o visual vinha do navegador. CSS separou estilo de conteúdo (~1995–96). **Confidence:** alta. Ver [[wiki/concepts/html-hipertexto]].

**Claim:** A guerra IE × Netscape fragmentou padrões, gerou acusações antitruste (IE no Win98) e levou à abertura do Mozilla. **Confidence:** alta no geral; detalhes de datas são do autor. Ver [[wiki/entities/netscape]], [[wiki/entities/microsoft]].

**Claim:** O Gmail realizou o medo de Bill Gates: navegador substituindo o SO. **Evidence:** substituiu o Outlook; ameaçava o monopólio do Office. **Confidence:** média (interpretação do autor). 

**Claim:** iPhone (2007, 320×480) + recusa ao Flash matou plugins (Flash, ActiveX, applets, Silverlight) e acelerou HTML5/CSS3 (oficiais em 2014). **Confidence:** alta; [external] *Thoughts on Flash* (Jobs, 2010). Ver [[wiki/entities/adobe-flash]].

**Claim:** 2008–2015 foi transição caótica; surgiram meta-linguagens (Sass, Less, CoffeeScript), frameworks de CSS ([[wiki/entities/twitter-bootstrap]]), gerenciadores de pacote, minificação e pipelines (Rails → Grunt/Gulp → Webpack); HTTP/2 reduziu a necessidade de concatenar ([[wiki/concepts/http2]]). **Confidence:** alta.

**Claim:** SPAs e frameworks de componentes (Backbone, Ember, Angular, React + [[wiki/concepts/virtual-dom]], Vue) deslocam o estado para o cliente; híbridos (Electron, React Native) reusam a stack web. **Confidence:** alta. Ver [[wiki/entities/react]], [[wiki/concepts/design-responsivo]], [[wiki/concepts/sandbox]], [[wiki/concepts/biblioteca-javascript-de-compatibilidade]], [[wiki/entities/ruby-on-rails]].

## Entidades e conceitos

Entidades: [[wiki/entities/fabio-akita]], [[wiki/entities/microsoft]], [[wiki/entities/netscape]], [[wiki/entities/apache-http-server]], [[wiki/entities/ruby-on-rails]], [[wiki/entities/adobe-flash]], [[wiki/entities/gmail]], [[wiki/entities/twitter-bootstrap]], [[wiki/entities/w3c]]. Conceitos: ver links acima, além de [[wiki/concepts/jquery]], [[wiki/concepts/xml-extensible-markup-language]], [[wiki/concepts/renderizacao-ssr-vs-csr]], [[wiki/concepts/linux]].

## Open Questions

- Fonte é legenda automática; vários nomes foram inferidos (Dojo, Grunt/Gulp, lista inicial de siglas) — marcados no raw.
- O autor atribui o AJAX à Mozilla; [external] o `XMLHttpRequest` nasceu na Microsoft (IE5).
- Episódios seguintes (back end, DevOps) não ingeridos; Linux/Arch do ep. anterior só citado.
- Datas citadas de memória pelo autor (ex.: CSS3 em 2012, HTML5 em 2014) não foram checadas contra o W3C.

## Raw quotes

> "Se você tem poucas perguntas, não está se esforçando o suficiente. Faça a pergunta errada e vai receber a resposta errada."

> "Sempre que tiver dúvida sobre uma tecnologia, comece do começo: pesquise sua história."
