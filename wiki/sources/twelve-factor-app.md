---
type: source
title: "Twelve-Factor App"
aliases: ["twelve factor app", "12 factor", "12 factor app", "cloud native methodology", "heroku twelve factor"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/twelve-factor-app.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [twelve-factor, cloud-native, configuration, stateless, disposability, dev-prod-parity, backing-services, logs-as-streams]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Twelve-Factor App (Heroku, 2011): 12 práticas para aplicações SaaS portáveis e escaláveis. Mais críticos: III. Config em env vars (nunca hardcode), VI. Processos stateless, IX. Graceful shutdown + startup rápido, X. Dev/Prod parity. Pré-requisito para Kubernetes, serverless e PaaS. Não é framework — é contrato de boas práticas pressupostas por cloud-native infra.

## Key Claims

**Claim:** Fator III (Config) é o mais violado — config em código força redeploy para mudança de ambiente.
**Evidence:** `const db = new Pool({ host: "prod-db.internal" })` hardcoded: não funciona em staging sem alterar código. Twelve-Factor: `process.env.DATABASE_URL`. Benefício: mesmo artefato Docker em dev/staging/prod com configs diferentes via env vars. Kubernetes: ConfigMaps e Secrets. Validação obrigatória na inicialização com Zod.
**Confidence:** alta

**Claim:** Fator VI (Processos stateless) é pré-requisito para escala horizontal — sessão em memória quebra com múltiplas instâncias.
**Evidence:** Sessão em memória local: request 1 para instância A cria sessão, request 2 vai para instância B → sessão não encontrada. Stateless: sessão em Redis, state em banco. Qualquer instância processa qualquer request. Escala horizontal automática funciona sem sticky sessions no load balancer.
**Confidence:** alta

**Claim:** Fator IX (Disposability) é obrigatório para K8s — pods são efêmeros, shutdown gracioso previne requests perdidos.
**Evidence:** K8s: pod é terminado com SIGTERM a qualquer momento. Sem graceful shutdown: requests em andamento são cortadas. Com `process.on("SIGTERM", () => server.close(gracefulShutdownCallback))`: finaliza requests pendentes, fecha conexões de banco, para de aceitar novas. `preStop sleep 5` absorve lag de remoção do endpoint no load balancer.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/twelve-factor]]
- [[concepts/config-as-env-vars]]
- [[concepts/stateless-processes]]
- [[concepts/disposability]]
- [[concepts/dev-prod-parity]]
- [[concepts/backing-services]]

## Open Questions

- Beyond Twelve-Factor (Kevin Hoffman, 2016) — quais fatores adicionais são relevantes para microserviços modernos?
- Twelve-Factor com secrets (não podem ser env vars plaintext) — como conciliar o Fator III com secrets managers?
