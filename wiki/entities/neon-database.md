---
type: entity
title: "Neon (Database)"
aliases: ["Neon", "Neon Database", "Neon Postgres"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_count: 1
tags: [banco-de-dados, postgresql, serverless, cloud, database-branching]
skill: tech-mentor-backend
status: stub
---

# Neon (Database)

Plataforma de Postgres serverless em nuvem, escalável conforme o uso (aumenta/diminui recursos com o volume de requisições), com **[[wiki/concepts/database-branching|database branching]]** nativo via copy-on-write como diferencial central. Além do banco em si, oferece funcionalidades adjacentes de plataforma backend — gerenciamento de autenticação, AI gateway, storage de objetos.

## Database Branching

Branches de banco funcionam como branches de git: criar uma branch nova não copia os dados originais, só materializa cópias físicas dos blocos alterados sob demanda (copy-on-write). Isso permite dar a cada branch de código/PR um banco de teste isolado sem o custo de duplicar o banco inteiro. Ver [[wiki/concepts/database-branching]] para o mecanismo completo.

## Integração com Vercel

Integração nativa: a cada deploy de preview de uma branch no GitHub, a Vercel aciona automaticamente a criação da branch de banco correspondente no Neon (a partir de uma branch-mãe de staging), atualiza a variável de ambiente `DATABASE_URL` do ambiente de preview, e roda as migrations pendentes no momento do deploy — sem necessidade de escrever esse mecanismo manualmente. Ver [[wiki/entities/vercel]].

## Caso: `fernandakipper.com`

[[wiki/entities/fernanda-kipper]] usa dois projetos Neon para o portal de cursos: `certificates app` (produção, nunca ramificado) e `certificates dev` (branch `main` funcionando como staging com schema espelhado de produção e dados de seed/mock; cada branch de PR deriva dessa `main`). Adotado após conflitos reais de migrations concorrentes entre dois devs no banco de teste compartilhado que usavam antes.

## Key Sources

- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]]
