---
type: concept
title: "Database Branching"
aliases: ["database branching", "banco de dados por branch", "copy-on-write database", "branch de banco de dados"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_count: 1
tags: [banco-de-dados, testes, migrations, postgresql, neon, ci-cd, copy-on-write]
skill: tech-mentor-backend
status: draft
---

# Database Branching

Dar a cada branch de código o seu próprio banco de dados isolado — em vez de todas as branches de teste compartilharem um único banco físico — usando **copy-on-write** para que criar uma branch nova não exija copiar todos os dados do zero.

## O Problema Que Resolve

Quando uma aplicação controla o próprio schema (roda suas próprias migrations), branches de código concorrentes podem aplicar mudanças de schema diferentes no mesmo banco de teste compartilhado — colisão de esquema, migrations se atropelando. Isso degrada três coisas ao mesmo tempo: confiança nos testes (o ambiente deixou de ser "produção + só as minhas mudanças" e virou "produção + mudanças de todo mundo"), integridade dos dados de teste (contaminados por resquícios de outras branches), e velocidade de entrega (times na fila esperando a vez de usar o banco). Ver [[wiki/concepts/database-migration]] para o problema geral de tratar migrations com a mesma seriedade que código de aplicação.

## Mecanismo: Copy-on-Write

Uma branch nova de banco não duplica os dados do banco-mãe — ela compartilha os mesmos blocos físicos e só materializa uma cópia física de um bloco específico no momento em que esse bloco é alterado (escrita de dado ou mudança de schema). Enquanto a branch só lê, ela está lendo diretamente os blocos originais via ponteiro/metadado. Consequência prática: criar uma branch de um banco de 10 GB não custa 10 GB nem o tempo de copiar 10 GB — custa só a cópia dos metadados, e o storage adicional cresce proporcionalmente ao volume de mudanças feitas naquela branch, não ao tamanho do banco inteiro.

## Fluxo Típico

```
production DB  (nunca ramificado diretamente — dados reais de cliente)
      │
      ▼
staging DB     (branch-mãe estável: schema espelhado de produção, dados de seed/mock)
      │
      ├── branch efêmera (feature/login)     ← deploy de preview da branch de código
      ├── branch efêmera (feature/billing)   ← deploy de preview da branch de código
      └── branch efêmera (pr-123)            ← criada e destruída pelo CI
```

Regra chave: nunca ramificar direto de produção. A branch-mãe das branches de teste é um staging com schema idêntico a produção mas dados de seed/mock — evita expor dado real de cliente em ambiente de teste. Cada branch efêmera de teste roda quantas migrations precisar, sem risco para as demais branches nem para produção; ao final, só a branch validada é mergeada e o deploy segue para produção normalmente.

## Implementações Conhecidas

- **Neon** ([[wiki/entities/neon-database]]) — Postgres serverless com branching nativo via CLI/API; integração automática com Vercel atualiza `DATABASE_URL` e roda migrations pendentes a cada deploy de preview.
- **PlanetScale** — MySQL serverless; branching nativo + *deploy requests* (fluxo tipo PR para mudanças de schema) e *online DDL* não-bloqueante.

## Quando Vale o Custo

Times com migrations frequentes e concorrentes entre branches, e/ou dados sensíveis que não podem ser copiados livremente para staging. Projetos pequenos com poucos devs e poucas mudanças de schema simultâneas sentem menos a dor do banco compartilhado — mas o caso relatado em [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] mostra que mesmo uma equipe de dois devs já sente colisão de schema quando ambos mexem na mesma área do domínio ao mesmo tempo.

## Relacionado

- [[wiki/concepts/database-migration]] — o problema de fundo (migrations como código versionado); database branching resolve o *onde testar* essas migrations com segurança
- [[wiki/concepts/expand-contract]] — resolve o mesmo tipo de risco (não corromper produção durante mudança de schema) por um eixo diferente: isolamento no tempo (fases sequenciais) em vez de isolamento no espaço (banco físico separado por branch) — técnicas complementares, não concorrentes
- [[wiki/concepts/testes-integracao-banco-real]] — database branching é a forma de ter banco real por branch sem pagar o custo de um banco compartilhado
- [[wiki/concepts/variaveis-de-ambiente]] — cada branch de banco precisa de sua própria `DATABASE_URL`, tipicamente atualizada automaticamente pela plataforma de deploy

## Key Sources

- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] — caso real (`fernandakipper.com`) com Neon + Vercel, incluindo o mecanismo de copy-on-write e o setup de dois projetos (`certificates app` produção / `certificates dev` staging + branches efêmeras)
