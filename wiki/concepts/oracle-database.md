---
type: concept
title: "Oracle Database"
aliases: ["oracle db", "oracle rdbms"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [oracle, banco-de-dados, relacional, rac, licenciamento, backend]
skill: tech-mentor-backend
status: stub
---

# Oracle Database

Banco relacional corporativo — a escolha quando o requisito é garantia, suporte contratual e performance previsível em qualquer cenário, ao custo de um licenciamento por núcleo de CPU que pode chegar a milhões de reais/ano.

## Concorrência e Clustering

Com **RAC** (Real Application Cluster), múltiplos servidores físicos acessam o mesmo banco como se fosse uma instância única, multiplicando horizontalmente a capacidade de sessões. Uma instância única dedicada suporta entre 10.000 e 65.000 sessões ativas, dependendo do hardware.

## Recursos Exclusivos

- **Flashback Query** — consulta o dado como estava em qualquer ponto do passado, sem restaurar backup.
- **Advanced Compression** — reduz custo de storage em produção via compressão inteligente.
- **Particionamento nativo avançado** — divide tabelas enormes em pedaços gerenciáveis, transparente para a aplicação.

Esses recursos existem há décadas no Oracle; outros bancos vêm implementando versões equivalentes aos poucos.

## Custo Real

Além da licença por núcleo de CPU, Oracle exige DBA sênior dedicado para gerenciar parâmetros de memória (SGA, PGA) — mal configurados, degradam o sistema inteiro.

## Quem Usa

Grandes bancos, instituições financeiras e governos — sistemas que não podem errar e têm budget para isso.

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
