---
type: concept
title: "Variável de Ambiente"
aliases: ["environment variable", "env var"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [configuracao, twelve-factor, security]
skill: tech-mentor-security
status: draft
---

# Variável de Ambiente

Valor de configuração externo ao código que muda entre [[wiki/concepts/ambiente-de-execucao|ambientes]] (host/porta do banco, URL de API, tokens, nome do ambiente, flags de debug, SMTP, cache). Origem: Fator III do [[wiki/sources/twelve-factor-app]]. Pode vir do SO (inclusive configurada no painel da hospedagem, ex.: [[wiki/entities/hostinger]]), de um [[wiki/concepts/dotenv]] ou injetada por [[wiki/concepts/secret-manager]]; ler da memória do processo é mais barato que reler arquivo. A app consulta primeiro o ambiente e só depois o `.env` (fallback).

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
