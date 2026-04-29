---
type: source
title: "Secret Scanning"
aliases: ["secret scanning", "gitleaks", "trufflehog", "credential leak", "ghas", "pre-commit secrets"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/secret-scanning.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [secret-scanning, gitleaks, trufflehog, credential-leak, pre-commit, ghas, devsecops]
skill: tech-mentor-security
status: stable
---

## TL;DR

Secret Scanning: 3 camadas. Pre-commit (Gitleaks hook): bloqueia antes de commitar. CI/CD (Gitleaks + TruffleHog): escaneia cada PR com histórico completo. GitHub Advanced Security (GHAS): escaneia repositório inteiro + push protection nativo. Se vazar: revogar imediatamente, rotacionar, assumir comprometido, auditar logs. Nunca: hardcode de API keys, tokens, passwords no código.

## Key Claims

**Claim:** Pre-commit é a defesa mais barata — bloqueia antes de o secret entrar no histórico git.
**Evidence:** Secret no histórico git = existe mesmo após `git rm`. Reescrever histórico (`git filter-branch`, `git-filter-repo`) é destrutivo e nem sempre funciona (forks, pull mirrors). Pre-commit Gitleaks: `git add` com secret → hook detecta → commit bloqueado → secret nunca entra no repositório. Custo: instalação de hook por dev (automatizável via Makefile/devcontainer).
**Confidence:** alta

**Claim:** Se um secret vazar, assuma comprometido e revogue imediatamente — auditoria depois, não antes.
**Evidence:** Sequência correta: (1) revogar/rotacionar o secret imediatamente, (2) auditar logs para verificar uso indevido, (3) investigar como vazou. Ordem errada: "vou verificar se foi usado antes de revogar" — enquanto você audita, o secret pode estar sendo usado. Custo de falsa revogação (rotacionar um secret não comprometido) é baixo. Custo de não revogar comprometido é alto.
**Confidence:** alta

**Claim:** TruffleHog com `--only-verified` reduz falsos positivos — valida secrets contra APIs reais antes de alertar.
**Evidence:** TruffleHog: detecta padrões de secrets com entropy analysis e regex. `--only-verified`: tenta autenticar com o secret encontrado (AWS key, GitHub token, etc.). Se autenticação falha, não alerta. Reduz falsos positivos de ~40% para ~5% em repositórios com código legado cheio de exemplos de configuração.
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/gitleaks]]
- [[entities/trufflehog]]
- [[concepts/secret-scanning]]
- [[concepts/credential-leak]]
- [[concepts/pre-commit]]
- [[entities/github-advanced-security]]

## Open Questions

- Secret scanning em repositórios históricos com 10+ anos — como priorizar findings sem paralisar o time?
- Gitleaks com regras customizadas para secrets internos (chaves de integração proprietárias) — como manter regras atualizadas?
