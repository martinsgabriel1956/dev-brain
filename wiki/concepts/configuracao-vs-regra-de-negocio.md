---
type: concept
title: "Configuração vs Regra de Negócio"
aliases: ["o que vai no .env"]
date_created: 2026-10-09
date_updated: 2026-11-27
source_count: 3
tags: [configuracao, arquitetura, dotenv]
skill: tech-mentor-security
status: draft
---

# Configuração vs Regra de Negócio

Critério para decidir onde um valor mora. **Configuração de servidor** (faz a app funcionar; muda por ambiente; raro em runtime; usuário não acessa) → [[wiki/concepts/dotenv]]/cofre. **Regra de negócio, preferência de usuário, config de cliente** (desconto premium, resolução máxima, logo) → banco de dados + painel administrativo, com cache (Redis etc.). Teste prático: muda 10 vezes por ano, por quem não é dev? Não é `.env`.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], "regra de negócio" é a preparação dos pedidos no back-end (desconto no Natal, presente a 10 km). Ver [[wiki/concepts/regra-de-negocio]].

## O que Ousterhout chama de parâmetro de configuração

[[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] (8.2) critica parâmetros de configuração, mas fala de botões de ajuste de comportamento (cache, retentativas, intervalos) que o módulo poderia decidir sozinho. A configuração de servidor desta página (endereço, credencial) passa no teste do capítulo: o módulo não tem como descobrir esses valores. Distinção da wiki; ver [[wiki/concepts/parametro-de-configuracao]].

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: regra de negócio no back-end
- [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] — 8.2: parâmetros de ajuste de comportamento, diferentes da configuração de ambiente
