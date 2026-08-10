---
type: concept
title: "Multitenancy"
aliases: ["multi-tenant", "multi-tenancy", "isolamento de tenant"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 1
tags: [multitenancy, banco-de-dados, isolamento, idor, rls]
skill: tech-mentor-data
status: stub
---

# Multitenancy

Arquitetura em que múltiplos clientes (tenants) compartilham a mesma instância de aplicação e, frequentemente, as mesmas tabelas/documentos no banco de dados — em vez de cada cliente ter sua própria base isolada.

## Risco de segurança associado

Compartilhar tabelas entre tenants aumenta a superfície de [[wiki/concepts/idor|IDOR]]: se a aplicação não valida corretamente a qual tenant um registro pertence antes de retorná-lo, um usuário autenticado de um tenant pode acessar dados de outro tenant apenas variando um identificador na requisição. [[wiki/sources/uuid-quando-usar-pergunta-diogo]] cita esse cenário como motivação para usar identificadores difíceis de adivinhar (UUID) como camada extra de proteção — sem que isso substitua a checagem de autorização por tenant em cada query.

## Ver também

- [[wiki/concepts/idor]] — a vulnerabilidade que a falta de isolamento entre tenants amplifica
- [[wiki/concepts/uuid]] — identificador não sequencial como mitigação parcial de enumeração entre tenants

## Key Sources

- [[wiki/sources/uuid-quando-usar-pergunta-diogo]]
