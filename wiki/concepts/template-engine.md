---
type: concept
title: "Template engine"
aliases: ["template engine", "motor de templates", "templating", "view engine"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [backend, html, ssr, template-engine, frontend]
skill: lang-dynamic
status: stub
---

# Template engine

Um motor que junta um template (HTML com marcações) e dados para gerar o HTML final, em geral no servidor. Os recursos típicos:
- variáveis interpoladas;
- condicionais e laços;
- partials (`include`);
- herança de layout (`extends` e `block`);
- escape automático contra XSS.

Exemplos: [[wiki/entities/nunjucks]], EJS, Handlebars, Pug, Jinja2 (Python), ERB (Ruby) e Blade (PHP). É a base da renderização no servidor clássica, em que o servidor devolve a página pronta. Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica que a template engine "vai transformar o meu HTML que simplesmente servia para marcação de texto, no arquivo agora que eu posso ter funções [...] if e else [...] variáveis [...] estrutura de repetição". A motivação são os cards de resultados vindos do servidor: "eu não posso ficar colocando na mão". O HTML estático "não tinha vida"; com dados do servidor, fica dinâmico.

A herança de layout evita repetir `head` e `body` em cada página, como pede o [[wiki/concepts/dry]].

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], o template de resultados passa a ser alimentado pelo banco: `{% for place in places %}`, `{{ total }}` e `{% if total > 0 %} ... {% else %}`. No cadastro, `{% if saved %}{% include ... %}{% endif %}` mostra o modal de sucesso. Ver [[wiki/entities/nunjucks]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], [[wiki/entities/diego-fernandes|Diego Fernandes]] usa o template engine (Blade, Handlebars, EJS, Nunjucks) como marca do "MVC" que a trilha dele *não* segue: no lugar de HTML, a rota devolve JSON ([[wiki/concepts/api-rest]]).

## Key sources

- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: motivação, variáveis, include e extends/block com Nunjucks
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: for/if com dados do banco
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: template engine como contraste da API REST
