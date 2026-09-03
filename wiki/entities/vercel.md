---
type: entity
title: "Vercel"
aliases: ["Vercel"]
date_created: 2026-07-28
date_updated: 2026-09-02
source_count: 3
tags: [tech-mentor-ai, harness, tool-call, deploy, serverless]
skill: tech-mentor-ai
status: stub
---

# Vercel

Plataforma de deploy amplamente usada por devs, especialmente com IA. Já entidade indireta na wiki via [[wiki/entities/vercel-ai-sdk]] (o SDK) e via [[wiki/concepts/connection-pooling]] ("attach database pool" da Vercel Functions em ambiente serverless) — esta página cobre a empresa/plataforma em si, não o SDK.

## Caso: Remover 80% das Ferramentas de um Agente Melhorou a Performance

[[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] relata um experimento interno da Vercel com agentes de IA: um agente com muitas ferramentas disponíveis tinha performance ruim. Em vez de adicionar mais ferramentas (decisão intuitiva), a Vercel removeu 80% das ferramentas disponíveis — a performance melhorou, porque cada etapa passou a exigir escolher entre menos opções. Ver [[wiki/concepts/tool-call]] e [[wiki/concepts/harness]] para o enquadramento completo do caso.

## Caso: hospedagem de site pessoal (name servers apontados pela GoDaddy)

[[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] usa a Vercel como exemplo concreto de "onde um site está hospedado": o site de [[wiki/entities/fernanda-kipper]] (`fernandakipper.com`) roda na Vercel, e ao descobrir o [[wiki/concepts/endereco-ip|IP]] do domínio chega-se a um servidor da Vercel. O domínio foi comprado na [[wiki/entities/godaddy]], onde os **name servers** foram configurados para encaminhar à Vercel — que faz o mapeamento domínio → projeto/site correto.

## Caso: Integração Nativa com Neon Para Database Branching

[[wiki/sources/database-branching-testes-neon-fernanda-kipper]]: a cada deploy de preview de uma branch de código, a Vercel aciona automaticamente a criação de uma branch de banco correspondente no [[wiki/entities/neon-database|Neon]] (copy-on-write a partir de uma branch-mãe de staging), atualiza a [[wiki/concepts/variaveis-de-ambiente|variável de ambiente]] `DATABASE_URL` do ambiente de preview, e roda as migrations pendentes no momento do deploy — sem exigir mecanismo manual. Ver [[wiki/concepts/database-branching]].

## Key Sources

- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — Vercel como host do site pessoal da autora; name servers do domínio (na GoDaddy) apontando para a Vercel
- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] — integração automática Vercel↔Neon para banco de teste isolado por branch
