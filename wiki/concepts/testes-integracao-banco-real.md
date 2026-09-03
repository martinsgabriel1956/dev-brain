---
type: concept
title: "Testes de Integração com Banco Real"
aliases: ["testes integração banco", "não mockar banco", "banco de teste dedicado"]
date_created: 2026-04-25
date_updated: 2026-09-02
source_count: 5
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

## Um mock de banco mal pensado "não integra"

Se o double do banco não reproduz os mesmos problemas do banco real (constraints, tipos, comportamento de driver), o teste de integração que o usa não está de fato validando integração nenhuma — é só um teste mais fraco escrito pelo próprio autor do código, testando as próprias suposições em vez da realidade. Isso é a face oposta da recomendação de Meszaros ([[wiki/sources/test-double-xunitpatterns-meszaros]]): um [[test-doubles|Fake]] de banco em memória é legítimo *quando a fidelidade não importa para aquele teste* (ele cita um caso de ~50× de ganho de velocidade), mas a própria fonte alerta para **sempre ter ao menos um teste sem double** — que aqui é justamente o teste contra o banco real.

## Um Banco Real Compartilhado Entre Branches Recria o Mesmo Problema Que Mockar

Testar contra um banco real (não mockado) só entrega o valor prometido nesta página se esse banco for isolado por branch. Um único banco de teste compartilhado por todas as branches concorrentes sofre colisão de esquema quando migrations se atropelam — o teste passa a validar um estado de banco que é "produção + minhas mudanças + mudanças de todo mundo", não mais fiel a produção do que um mock mal calibrado seria. [[wiki/concepts/database-branching]] resolve isso dando a cada branch seu próprio banco isolado via copy-on-write, preservando o benefício de testar contra um banco real sem o custo do compartilhamento.

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — Fake em memória (ganho de velocidade) vs. a regra "ao menos um teste sem double"
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — "se você não criar o banco de dados de teste real, você está testando um mock que você mesmo escreveu"
- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] — banco real só é confiável entre branches concorrentes se for isolado por branch
