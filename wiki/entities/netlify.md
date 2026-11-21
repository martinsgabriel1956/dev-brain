---
type: entity
title: "Netlify"
aliases: ["netlify", "Netlify Deploy"]
date_created: 2026-11-16
date_updated: 2026-11-21
source_count: 2
tags: [deploy, frontend, hospedagem, jamstack, ferramenta]
skill: lang-dynamic
status: stub
---

# Netlify

Plataforma de hospedagem para front-ends e sites estáticos: liga a um repositório Git, roda o build a cada push, publica numa CDN e cria *deploy previews* por pull request. Tem também funções serverless e formulários.

Na NLW #1 ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]), é a recomendação de [[wiki/entities/diego-fernandes]] para o front-end React: "como se fosse um Heroku, porém para front-end", em que basta apontar a URL do repositório. Ele o acha "um pouquinho mais fácil" que a [[wiki/entities/vercel]].

**Nota:** os "100 GB" citados na aula eram de banda mensal no plano gratuito, e o modelo de preço mudou depois `[external, não verificado]`. Para SPAs com React Router, o deploy precisa de um *redirect* de `/*` para `/index.html`, senão recarregar `/create-point` dá 404. Ver [[wiki/concepts/client-side-routing]].

Relacionado: [[wiki/concepts/deploy-strategies]], [[wiki/concepts/object-storage]].

## FrontPUSH, hospedagem aula 01

Em [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]], "plano starter [...] para projetos pessoais"; "você pode buildar a sua aplicação sem precisar [...] entrar no servidor [...] por meio de um FTP", "direto pelo Git". O módulo fará o deploy nele e no GitHub Pages. Os nomes dos planos mudaram desde então `[external]` (https://www.netlify.com/pricing/).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: opção de deploy do front-end
- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: FrontPUSH, hospedagem aula 01: plano starter, deploy pelo Git em vez de FTP
