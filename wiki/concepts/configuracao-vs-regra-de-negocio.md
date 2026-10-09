---
type: concept
title: "Configuração vs Regra de Negócio"
aliases: ["o que vai no .env"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [configuracao, arquitetura, dotenv]
skill: tech-mentor-security
status: draft
---

# Configuração vs Regra de Negócio

Critério para decidir onde um valor mora. **Configuração de servidor** (faz a app funcionar; muda por ambiente; raro em runtime; usuário não acessa) → [[wiki/concepts/dotenv]]/cofre. **Regra de negócio, preferência de usuário, config de cliente** (desconto premium, resolução máxima, logo) → banco de dados + painel administrativo, com cache (Redis etc.). Teste prático: muda 10 vezes por ano, por quem não é dev? Não é `.env`.

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
