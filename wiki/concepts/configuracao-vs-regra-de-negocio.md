---
type: concept
title: "Configuração vs Regra de Negócio"
aliases: ["o que vai no .env"]
date_created: 2026-10-09
date_updated: 2026-11-16
source_count: 2
tags: [configuracao, arquitetura, dotenv]
skill: tech-mentor-security
status: draft
---

# Configuração vs Regra de Negócio

Critério para decidir onde um valor mora. **Configuração de servidor** (faz a app funcionar; muda por ambiente; raro em runtime; usuário não acessa) → [[wiki/concepts/dotenv]]/cofre. **Regra de negócio, preferência de usuário, config de cliente** (desconto premium, resolução máxima, logo) → banco de dados + painel administrativo, com cache (Redis etc.). Teste prático: muda 10 vezes por ano, por quem não é dev? Não é `.env`.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], "regra de negócio" é a preparação dos pedidos no back-end (desconto no Natal, presente a 10 km). Ver [[wiki/concepts/regra-de-negocio]].

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: regra de negócio no back-end
