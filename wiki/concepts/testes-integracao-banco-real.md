---
type: concept
title: "Testes de Integração com Banco Real"
aliases: ["testes integração banco", "não mockar banco", "banco de teste dedicado"]
date_created: 2026-04-25
date_updated: 2026-07-07
source_count: 2
tags: [testes, integracao, banco-de-dados, portfolio, backend]
skill: tech-mentor-leadership
status: stable
---

# Testes de Integração com Banco Real

Testes end-to-end / de integração devem bater nas rotas **e** no banco de dados real — nunca mockar o banco.

## Por que não mockar o banco

Mock de banco mascara bugs reais: a query pode funcionar no mock e falhar em produção por diferenças de tipo, constraint, índice ou comportamento do driver. O valor do teste está exatamente em validar que a query funciona no banco real.

## O padrão

```yaml
# docker-compose.yml — banco dedicado para testes
services:
  db_test:
    image: postgres:16
    environment:
      POSTGRES_DB: app_test
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
    ports:
      - "5433:5432"
```

```typescript
// variável de ambiente aponta para banco de teste
process.env.DATABASE_URL = "postgresql://test:test@localhost:5433/app_test";
```

- Banco de teste separado do banco de desenvolvimento
- Limpar entre testes com `TRUNCATE` ou transaction rollback
- Mockar apenas integrações externas reais (envio de e-mail, APIs de terceiros)

## O que testar

- Todas as rotas da aplicação (happy path + edge cases)
- Regras de negócio que dependem do banco (unicidade, constraints, transações)
- Coverage report para demonstrar cobertura concreta

## Por que isso diferencia

Ausência de testes é fator eliminatório em processos seletivos. Testes de integração com banco real são mais valiosos que unitários isolados para demonstrar que a aplicação funciona de ponta a ponta.

## Onde isso se encaixa na distinção estreito/amplo de Fowler

Bater no banco real não é a mesma coisa que um [[teste-de-integracao-estreito-vs-amplo|teste de integração amplo]] no sentido de Fowler: banco de dados é infraestrutura *própria* da aplicação, não um serviço externo mantido por outro time — por isso mockar o banco não vira um "narrow integration test" válido, é só um teste mais fraco. A recomendação desta página (nunca mockar o banco) e a de Fowler (usar double para *serviços externos*) não competem: ambas apontam para o mesmo princípio — dublê só onde a dependência é de fato externa e cara de ativar, banco próprio não se qualifica.

## Relações

- [[portfolio-backend-junior]]
- [[efeito-colateral]] — mockar banco esconde efeitos colaterais reais
- [[idempotencia]] — testes de integração validam idempotência de operações
- [[teste-de-integracao-estreito-vs-amplo]] — por que banco real não é "teste amplo" no sentido de Fowler

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[wiki/sources/integration-test-martin-fowler]]
