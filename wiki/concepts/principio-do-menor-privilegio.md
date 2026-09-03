---
type: concept
title: "Princípio do Menor Privilégio"
aliases: ["least privilege", "principle of least privilege", "PoLP", "menor privilégio", "permissão mínima"]
date_created: 2026-06-10
date_updated: 2026-08-28
source_count: 5
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

O menor privilégio também se aplica ao próprio acesso SSH: [[wiki/concepts/ssh]] configurado com `PubkeyAuthentication` e sem fallback de senha já restringe quem consegue autenticar; combinar isso com um bastion host acessível só por chave é o menor privilégio aplicado em duas camadas (rede + credencial).

**Funcionários e admins**
- Admin completo não deve ser o default para todos
- Mapear o que cada papel precisa e conceder exatamente isso
- Acesso just-in-time para ambientes de produção — sem standing privilege

**Agentes de IA (não só serviços/humanos)**
[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] aplica o mesmo princípio a um agente de codificação de IA: em vez de dar acesso total ao filesystem do usuário, o [[wiki/concepts/agent-containment|AI Jail]] expõe apenas o diretório do projeto atual, com granularidade por subpasta (ex.: `.claude/` como somente leitura, o restante do projeto como leitura+escrita) — o agente recebe exatamente o que precisa para operar, nada além disso.

**Whitelist de tool calling em agentes autônomos**: [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] descreve o mesmo princípio como um dos 4 componentes essenciais de um agente de produção — uma lista explícita das ferramentas que o agente pode chamar (ex.: rodar query, checar stats de tabela, rotacionar connection pool para um agente de DBA), com operações destrutivas (`DROP TABLE`) permanentemente fora da whitelist, independente do que o modelo decida.

## Usuário de Banco Dedicado por Serviço, Como Camada Contra SQL Injection

[[wiki/sources/sql-injection-guia-completo-solucoes-galego]] aplica PoLP à conexão servidor↔banco: em vez de uma credencial única com acesso total, cada serviço (ex.: "aplicação de e-mails") tem seu próprio usuário de banco, restrito a `SELECT`/`INSERT`/`DELETE` em tabelas específicas. Isso não previne [[wiki/concepts/sql-injection]] em si — não impede a injeção de acontecer — mas minimiza o dano: mesmo uma injeção bem-sucedida não consegue `DROP TABLE` se o usuário não tiver esse privilégio. O mesmo raciocínio é generalizado para além de SQLi: se um atacante comprometer o servidor inteiro (SSH, RCE), privilégios mínimos no banco limitam o raio de explosão daí em diante.

## Relação com Outros Conceitos

- [[defense-in-depth]] — o menor privilégio é uma das camadas; contém o dano quando outras camadas falham
- [[wiki/concepts/agent-containment]] — PoLP aplicado especificamente ao processo de um agente de IA, não só a serviços humanos
- [[attack-surface]] — reduzir privilégios reduz o impacto de cada ponto de entrada
- [[secure-by-default]] — o menor privilégio é o default seguro para permissões
- [[secrets-management]] — secrets acessíveis apenas pelos serviços que precisam deles

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — exemplos: backend read-only, banco dentro de VPC, bastion host para acesso externo
- [[wiki/sources/ssh-chaves-como-funcionam]] — chave SSH como credencial mínima para acesso a bastion hosts
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — permissões granulares de leitura/escrita por pasta para um agente de IA
- [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] — whitelist de tool calling como um dos 4 componentes de um agente autônomo de produção
- [[wiki/sources/sql-injection-guia-completo-solucoes-galego]] — usuário de banco dedicado por serviço, restrito a `SELECT`/`INSERT`/`DELETE`, como camada de contenção contra SQL Injection e contra comprometimento total do servidor
