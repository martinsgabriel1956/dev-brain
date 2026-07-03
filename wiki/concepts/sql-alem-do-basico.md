---
type: concept
title: "SQL Além do Básico"
aliases: ["sql avançado portfolio", "joins agregações subqueries", "domínio SQL"]
date_created: 2026-04-25
date_updated: 2026-07-03
source_count: 2
tags: [sql, postgresql, mysql, portfolio, backend, banco-de-dados]
skill: tech-mentor-leadership
status: stub
---

# SQL Além do Básico

Demonstrar domínio de SQL vai além do CRUD. Queries com JOINs, agregações e subqueries mostram que o dev entende como o banco de dados funciona de verdade.

## O que demonstrar

```sql
-- JOIN: buscar pedidos com dados do usuário e produto
SELECT
  u.name AS usuario,
  p.created_at,
  SUM(pi.quantidade * pi.preco_unitario) AS total
FROM pedidos p
INNER JOIN usuarios u ON u.id = p.usuario_id
INNER JOIN pedido_itens pi ON pi.pedido_id = p.id
WHERE p.status = 'concluido'
GROUP BY u.name, p.id, p.created_at
ORDER BY p.created_at DESC;

-- Subquery: usuários que fizeram mais de 5 pedidos
SELECT u.name, u.email
FROM usuarios u
WHERE (
  SELECT COUNT(*) FROM pedidos p WHERE p.usuario_id = u.id
) > 5;

-- Window function: ranking de usuários por total gasto
SELECT
  u.name,
  SUM(p.total) AS total_gasto,
  RANK() OVER (ORDER BY SUM(p.total) DESC) AS ranking
FROM usuarios u
INNER JOIN pedidos p ON p.usuario_id = u.id
GROUP BY u.id, u.name;
```

## Por que PostgreSQL

PostgreSQL é o banco relacional mais comum em vagas backend modernas. Demonstrar domínio nele (não apenas ORM) mostra que o candidato entende o que o ORM está gerando por baixo.

## Relações

- [[portfolio-backend-junior]]
- [[testes-integracao-banco-real]] — SQL complexo precisa de testes reais, não mocks
- [[wiki/concepts/orm]] — ORM esconde SQL até você bater num caso de borda; dominar SQL é o que resolve esse caso

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
