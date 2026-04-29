---
date: 2026-04-13
tags: [tech-mentor, arquitetura, documentacao, adr, decisao-tecnica]
skill: tech-mentor-leadership/references/documentation
level: fundamento
---

# ADR — Architecture Decision Record

## Contexto

ADR é um documento curto que registra **uma decisão arquitetural significativa** junto com o contexto que levou a ela e as consequências esperadas. Criado por Michael Nygard.

O problema que resolve: **"por que fizemos isso?"** — 6 meses depois, ninguém lembra por que escolhemos Kafka em vez de RabbitMQ, ou por que temos dois bancos, ou por que a autenticação funciona daquele jeito específico. ADRs são a memória do sistema.

Características fundamentais:
- **Imutável após aprovação** — decisões antigas não são editadas, são supersedidas
- **Um ADR por decisão** — não documente múltiplas decisões no mesmo arquivo
- **Curto** — 1-2 páginas, não um artigo acadêmico

## Formato

```markdown
# ADR-0001: Uso de Kafka para comunicação entre serviços

**Status:** Accepted  
**Date:** 2026-04-13  
**Deciders:** @alice, @bob, @carol

## Contexto

Nossa plataforma de e-commerce cresce 20% ao mês. A comunicação síncrona entre
Order Service e Payment Service via REST gera acoplamento temporal: se Payment
está down, o checkout falha completamente.

Precisamos de comunicação assíncrona com garantias de entrega (at-least-once),
replay de eventos para novos consumidores, e capacidade de fan-out para múltiplos
serviços (Notification, Analytics, Fraud Detection) consumirem o mesmo evento.

## Decisão

Usar Apache Kafka como broker de eventos para comunicação entre serviços.

## Consequências

### Positivas
- Desacoplamento temporal: Order Service não precisa que Payment esteja up
- Replay: novo serviço pode processar histórico de eventos
- Fan-out: múltiplos consumidores sem alterar o produtor
- Throughput alto (milhões de eventos/segundo se necessário)

### Negativas
- Complexidade operacional: requer ZooKeeper/KRaft, monitoramento de lag, etc.
- Eventual consistency: consumidores ficam para trás em picos
- Debugging mais difícil: rastrear um pedido requer correlação de eventos

### Neutras
- Schema Registry (Confluent) necessário para evolução de schema
- Time precisa aprender garantias de entrega (at-least-once vs exactly-once)

## Alternativas Consideradas

**RabbitMQ:** descartado — sem replay de eventos nativo, menor throughput
**Amazon SQS/SNS:** descartado — vendor lock-in, sem replay nativo
**REST síncrono com retry:** descartado — acoplamento temporal permanece
```

### Status Possíveis

```
Proposed  → em discussão
Accepted  → decisão tomada e em vigor
Deprecated → ainda em vigor mas planejando substituir
Superseded by ADR-0042 → substituído por decisão mais recente
Rejected  → proposta mas não aprovada
```

### Numeração e Organização

```
docs/
└── architecture/
    └── decisions/
        ├── 0001-kafka-para-eventos.md
        ├── 0002-postgresql-como-banco-principal.md
        ├── 0003-nextjs-app-router.md
        └── 0004-redis-para-sessoes.md  (Supersedes: 0002 parcialmente)
```

Ferramentas: `adr-tools` (CLI), `log4brains` (web UI), qualquer editor de texto.

## Processo de ADR

```
1. Dev identifica decisão significativa
   ↓
2. Cria ADR com status "Proposed"
   ↓
3. Pull Request com o ADR no repositório
   ↓
4. Review assíncrono pelos devs relevantes (1-3 dias)
   ↓
5. Discussão no PR: contexto, alternativas, consequências
   ↓
6. Aprovação → merge com status "Accepted"
   ↓
7. Decisão documentada, buscável no git
```

### O que é "Significativo"?

Merece ADR quando a decisão:
- Afeta múltiplos times ou serviços
- Tem consequências difíceis de reverter (escolha de banco, protocolo de comunicação)
- Foi debatida com múltiplas opções legítimas
- Vai confundir futuros devs sem contexto

**Não merece ADR:**
- Preferência de biblioteca trivial (lodash vs ramda)
- Convenções de código (use prettier)
- Decisões reversíveis sem consequências arquiteturais

## Trade-offs do Processo

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Memória organizacional | Preserva o "porquê" das decisões | Overhead inicial de escrever o documento |
| Onboarding | Novo dev entende contexto rapidamente | ADRs desatualizados são piores que nenhum |
| Revisão | Força discussão explícita de trade-offs | Pode atrasar decisão urgente |
| Rastreabilidade | Git history liga código ao ADR | Exige disciplina para manter atualizado |

## Quando Criar / Quando Pular

**Criar ADR:**
- Escolha de banco de dados, broker, protocolo
- Padrão de autenticação (JWT vs session)
- Estratégia de deploy (blue/green, canary)
- Decisão de extrair monolito para serviços
- Trade-off explícito com consequências negativas aceitas

**Pular ADR:**
- Decisões óbvias dado o stack
- Convenções de estilo (use linter)
- Algo que pode ser revertido sem custo

## Conceitos Relacionados

[[c4-model]] · [[rfc]] · [[wardley-maps]] · [[evolutionary-architecture]] · [[tech-debt]]

---
*Fonte: tech-mentor skill · tech-mentor-leadership · 2026-04-13*
