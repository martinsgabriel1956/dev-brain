---
type: source
title: "Database Migrations — SQL Cru vs. ORM (Drizzle)"
aliases: ["migrate up migrate down", "drizzle migrations", "migrations reproduzíveis"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/database-migrations-sql-cru-vs-orm-drizzle.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [migrations, database-migration, orm, drizzle, postgresql, versionamento, code-review, docker]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Executar DDL manualmente contra o banco (SSH direto na cloud) não é revisável, auditável, reproduzível nem automatizável — deve ser evitado. Migrations devem estar versionadas em git, sujeitas a PR/code review, e aplicadas via scripts reproduzíveis, com pares migrate up/migrate down e versionamento sequencial. Demonstra o fluxo com SQL cru (Postgres local via docker-compose + script de migrate/rollback) e com uma ORM ([[wiki/concepts/drizzle-orm|Drizzle]]), onde o fluxo se inverte: declara-se o estado final do schema e a migration é derivada automaticamente. Mesmo com ORM, migrations continuam podendo causar lock de produção em tabelas grandes — necessário testar em staging com dados similares aos de produção.

## Key Claims

**Claim:** Rodar comandos de migração manualmente (SSH + SQL direto) é uma prática errada, mesmo para um DBA experiente.
**Evidence:** Comandos que vivem só na máquina de quem executa não são revisáveis, auditáveis, reproduzíveis nem automatizáveis — não atingem o nível de robustez/profissionalismo esperado. A recomendação não é abolir migrations manuais como artefato, e sim submetê-las ao mesmo processo do código: PR, review, controle de versão (git).
**Confidence:** alta (opinião forte e explícita do autor, mas apresentada como tal — "no risco de ser um pouco polêmico")

**Claim:** Toda migração deveria ter um par migrate up / migrate down, com versão sequencial rastreada pelo próprio banco.
**Evidence:** Demonstração prática com 3 migrations SQL numeradas (criar tabela → adicionar coluna → adicionar constraint de unicidade), cada uma com down que reverte exatamente o que o up fez. Um script `migrate` identifica a versão atual do banco e aplica só as migrations pendentes; um script `rollback` reverte uma migração por vez. Testado ao vivo: migrate completo, rollback total, e aplicação parcial (rollback parcial seguido de migrate, que detecta e pula o que já estava aplicado).
**Confidence:** alta (demonstrado ao vivo, comportamento observado corresponde ao esperado)

**Claim:** Com uma ORM, o fluxo de criação de migrations se inverte — de "escrever a migration" para "declarar o estado final e deixar a ferramenta derivar a migration".
**Evidence:** Exemplo com Drizzle: schema declarado em TypeScript (`pgTable` com colunas e constraints); `drizzle-kit generate` compara esse schema com o histórico interno (journal + snapshots) e gera o arquivo de migration correspondente ao diff. Alterar o schema (adicionar/remover um campo) e rodar `generate` de novo gera automaticamente uma nova migration para aquele diff, sem exigir SQL manual na maioria dos casos.
**Confidence:** alta (demonstrado ao vivo)

**Claim:** Uma migration gerada por ORM não é garantidamente segura em produção — o mesmo cuidado de engenharia se aplica independente da ferramenta.
**Evidence:** Relato de incidente pessoal do autor: alterar a tabela `users` (~100.000 linhas) para adicionar um campo derivado de outro travou a tabela por ~5 minutos em produção (lock). Recomendação: testar em staging com dados similares a produção antes de aplicar; "não é porque a ORM gerou a migration que ela está correta ou que não vai quebrar tudo".
**Confidence:** média — relato anedótico de um único incidente, sem detalhamento técnico da causa exata do lock (compatível com o padrão documentado com mais profundidade em [[wiki/sources/migrations-schema-evolution]], mas não com o mesmo nível de evidência).

## Entities & Concepts Touched

- [[wiki/concepts/database-migration]]
- [[wiki/concepts/orm]]
- [[wiki/concepts/drizzle-orm]]
- [[wiki/concepts/postgresql]]
- [[wiki/concepts/expand-contract]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/checklist-primeiro-dia-projeto]]

## Open Questions

- O vídeo não detalha o mecanismo exato do lock relatado (~5 min em tabela de 100k linhas) — [[wiki/sources/migrations-schema-evolution]] cobre isso com mais rigor técnico (ex.: `ADD COLUMN NOT NULL` sem default reescreve a tabela inteira). Vale ligar as duas fontes para quem busca o "porquê" do incidente relatado aqui.
- Não é discutido como Drizzle lida com migrations conflitantes quando duas branches geram diffs diferentes do mesmo schema em paralelo (cenário comum em times, coberto de forma mais geral em [[wiki/sources/migrations-schema-evolution]] via checksum/append-only).
