---
type: concept
title: "Secret Scanning"
aliases: ["secret scanning", "gitleaks", "trufflehog", "credential leak scanning", "ghas"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 2
tags: [secret-scanning, gitleaks, trufflehog, devsecops, security]
skill: tech-mentor-security
status: draft
---

# Secret Scanning

Detecção automatizada de credenciais (API keys, tokens, senhas) acidentalmente commitadas em um repositório de código. Trabalha em camadas: **pre-commit** (bloqueia localmente antes de o secret entrar no histórico git), **CI/CD** (escaneia cada PR, incluindo histórico completo), e **nível de plataforma** (GitHub Advanced Security, com push protection nativo bloqueando o push em si).

## Por Que Olhar Só o Estado Atual Não Basta

Apagar um arquivo com uma credencial num commit novo não remove o conteúdo do **histórico** do git — o valor continua acessível em algum commit anterior para quem tiver acesso ao repositório. Por isso ferramentas sérias (Gitleaks, TruffleHog) varrem todo o histórico de commits desde o início do projeto, não só o `HEAD`. Ver detalhe em [[wiki/concepts/secrets-management]] (seção "Scanner de Histórico de Git como Teste de Autopentest").

## Ferramentas Citadas na Wiki

- **Gitleaks** — hook de pre-commit e scan de CI/CD baseado em regex/regras.
- **TruffleHog** — varre repositório inteiro + histórico; com `--only-verified`, testa a credencial encontrada contra o provedor real antes de alertar, reduzindo falsos positivos.
- **GitHub Advanced Security (GHAS)** — nível de plataforma, inclui push protection nativo (bloqueia o push antes mesmo de o secret chegar ao repositório).

## Resposta a Vazamento

Sequência correta se um secret vazar: **revogar/rotacionar imediatamente** → investigar uso indevido via audit logs → só então reescrever o histórico do git (BFG/`git filter-repo`) se necessário. Revogar antes de investigar: o custo de revogar algo que não foi comprometido é baixo; o custo de não revogar algo que foi é alto.

## Relação com Outros Conceitos

- [[wiki/concepts/secrets-management]] — secret scanning é a camada de **detecção**; secrets management é a camada de **gestão/prevenção** (onde a credencial deveria estar desde o início).
- [[wiki/concepts/github-search-api-limites]] — do lado ofensivo, a busca pública de código do GitHub tem limites de indexação que a tornam diferente (e menos confiável) do secret scanning feito sobre o próprio repositório no momento do push.
- [[wiki/concepts/attack-surface]] — cada credencial vazada expande a superfície de ataque.

## Key Sources

- [[wiki/sources/secret-scanning]] — três camadas (pre-commit, CI/CD, GHAS); sequência de resposta a vazamento; TruffleHog `--only-verified`
- [[wiki/sources/secrets-vazadas-no-github-conceitos-e-riscos]] — ângulo da descoberta em escala (por que histórico de commits precisa ser varrido, não só o estado atual)
