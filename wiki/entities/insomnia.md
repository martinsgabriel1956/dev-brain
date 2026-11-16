---
type: entity
title: "Insomnia"
aliases: ["insomnia.rest", "Insomnia REST client"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [ferramenta, http, api, testes, cliente-http]
skill: lang-dynamic
status: stub
---

# Insomnia

Cliente HTTP de desktop para montar e repetir requisições (qualquer método, query, headers, body JSON) e ler as respostas. É a alternativa ao Postman que a Rocketseat usava em 2020.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), resolve o problema de que a barra de endereço do navegador só faz GET. Cada rota do Ecoleta vira uma requisição salva num workspace "nlw": "listar itens", "criar ponto de coleta", "listar ponto específico", "listar pontos filtrados". Diego o descreve como "gratuito [...] open source", feito em JavaScript, sem versão de 32 bits (para isso, o Postman).

Desde 2023 (versão 8), o Insomnia, mantido pela Kong, passou a pedir conta e sincronização na nuvem; o protesto levou ao "scratch pad" local e a forks como o Insomnium `[external, não verificado]`. Alternativas locais: Bruno, Hoppscotch, a extensão REST Client do VS Code e o próprio `curl`.

Relacionado: [[wiki/concepts/metodos-http]], [[wiki/concepts/api-rest]], [[wiki/concepts/cors]] (que o Insomnia, por não ser navegador, ignora).

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], o body muda de JSON para *Multipart* com um campo do tipo *File* para testar o upload.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: testar GET/POST, query e body JSON
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: teste de upload multipart
