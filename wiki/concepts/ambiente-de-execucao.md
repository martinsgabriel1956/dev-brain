---
type: concept
title: "Ambiente de Execução (dev, staging, QA, produção)"
aliases: ["ambientes", "dev staging prod"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [ambiente, devops, configuracao]
skill: tech-mentor-security
status: draft
---

# Ambiente de Execução (dev, staging, QA, produção)

Cada lugar onde a aplicação roda é um ambiente: desenvolvimento (máquina local), QA (caça a bugs), homologação/staging (mais parecido com produção) e produção (dados reais). Até 10 clientes = 10 ambientes. Mudam: banco, URLs, tokens, [[wiki/concepts/logs-em-producao|nível de log]]. Misturar variáveis de dev e produção é erro comum — risco de enviar dado de teste a produção. Ver [[wiki/concepts/paridade-local-producao]], [[wiki/concepts/variavel-de-ambiente]].

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
