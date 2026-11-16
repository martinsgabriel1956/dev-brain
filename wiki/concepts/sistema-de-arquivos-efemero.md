---
type: concept
title: "Sistema de arquivos efêmero"
aliases: ["ephemeral filesystem", "disco efêmero", "filesystem efêmero"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [deploy, paas, containers, infraestrutura, armazenamento]
skill: lang-dynamic
status: stub
---

# Sistema de arquivos efêmero

Em PaaS (Heroku, Render, Railway), containers (Kubernetes, ECS, Cloud Run) e serverless, o disco local da instância é descartável. O que a aplicação escreve ali some a cada deploy, reinício ou troca de instância, e não é compartilhado entre réplicas. No Heroku, os dynos reiniciam pelo menos uma vez por dia `[external]` (https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem).

**O conflito no Ecoleta** ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]): o [[wiki/entities/multer]] grava as imagens em `uploads/`, e o banco é um arquivo `database.sqlite`. Os dois se perdem no [[wiki/entities/heroku]], primeira opção de deploy da mesma aula. Com duas réplicas, cada uma veria um conjunto diferente de imagens.

**Como se resolve:**

- **Arquivos** em [[wiki/concepts/object-storage]] ([[wiki/concepts/amazon-s3]], GCS, R2), com upload direto por URL assinada ([[wiki/concepts/media-upload-pattern]]).
- **Banco** gerenciado (Postgres), ou volume persistente quando a plataforma oferece.
- **A aplicação** fica *stateless* ([[wiki/concepts/stateless]]): qualquer instância atende qualquer requisição.

Relacionado: [[wiki/concepts/design-efemero-zero-persistencia]], [[wiki/concepts/deploy-strategies]].

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o problema aparece um passo antes do disco: o cadastro fica num array em memória e some a cada restart. Ver [[wiki/concepts/dados-em-memoria-vs-persistencia]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: uploads em disco x deploy no Heroku
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: estado em memória some ao reiniciar
