---
type: concept
title: "Princípio do Menor Privilégio"
aliases: ["least privilege", "principle of least privilege", "PoLP", "menor privilégio", "permissão mínima"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
tags: [security, least-privilege, iam, vpc, appsec, arquitetura-seguranca, defense-in-depth]
skill: tech-mentor-security
status: stable
---

# Princípio do Menor Privilégio

Cada componente — serviço, usuário, processo — deve ter **exatamente** as permissões necessárias para sua função, e nada além. É um dos pilares do [[defense-in-depth]]: limitar o raio de explosão quando uma parte do sistema é comprometida.

## Por Que Funciona

Se um serviço comprometido só tem permissão de leitura no banco, o atacante apenas lê — não modifica, não deleta. O dano é contido mesmo que a invasão seja real.

## Na Prática

**IAM / Roles de serviço**
```json
// ❌ Acesso irrestrito
{ "Action": "s3:*", "Resource": "*" }

// ✅ Acesso mínimo necessário
{ "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::bucket/uploads/*" }
```

**Usuários de banco de dados por operação**
- `app_reader` — apenas SELECT
- `app_writer` — INSERT, UPDATE
- `app_migrator` — DDL (usado apenas durante migrations, nunca pela aplicação)

**Banco de dados dentro de VPC**
Na maioria dos sistemas não existe motivo para o banco ser acessível fora da VPC. O frontend jamais deve ter acesso direto ao banco. Para acesso externo necessário (migrations, debugging), use um **bastion host**: uma EC2 dentro da VPC, acessada via SSH, que então se comunica com o banco. O endpoint do banco nunca fica exposto.

**Funcionários e admins**
- Admin completo não deve ser o default para todos
- Mapear o que cada papel precisa e conceder exatamente isso
- Acesso just-in-time para ambientes de produção — sem standing privilege

## Relação com Outros Conceitos

- [[defense-in-depth]] — o menor privilégio é uma das camadas; contém o dano quando outras camadas falham
- [[attack-surface]] — reduzir privilégios reduz o impacto de cada ponto de entrada
- [[secure-by-default]] — o menor privilégio é o default seguro para permissões
- [[secrets-management]] — secrets acessíveis apenas pelos serviços que precisam deles

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — exemplos: backend read-only, banco dentro de VPC, bastion host para acesso externo
