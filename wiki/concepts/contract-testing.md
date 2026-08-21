---
type: concept
title: "Contract Testing"
aliases: ["teste de contrato", "pact", "consumer-driven contracts", "can-i-deploy"]
date_created: 2026-04-22
date_updated: 2026-08-21
source_count: 8
tags: [testes, contract-testing, pact, microservices, ci, distribuídos]
skill: tech-mentor-testing
status: stable
---

# Contract Testing

Valida que dois serviços que se comunicam **concordam com o formato da comunicação** — sem precisar rodá-los juntos ao mesmo tempo. Solução para o problema de integração em sistemas distribuídos.

## Origem do termo: Ian Robinson (2006)

O nome "Consumer-Driven Contracts" e o modelo de inversão descrito abaixo vêm de [[wiki/sources/consumer-driven-contracts-martin-fowler|um artigo de 2006 de Ian Robinson]] (Thoughtworks), publicado no site de [[wiki/entities/martin-fowler]] mas não escrito por ele. Robinson propõe um modelo de três camadas: **Provider Contract** (tudo que o serviço expõe), **Consumer Contract** (o subconjunto que um consumidor específico usa) e **Consumer-Driven Contract** (o contrato do provedor derivado da união de todos os consumer contracts conhecidos). Na formulação original o padrão é agnóstico de implementação — planilha, teste automatizado ou asserção em runtime — e a comunicação entre provedor e consumidores acontece fora de banda. A ferramentagem moderna (Pact, `can-i-deploy`) descrita abaixo é uma implementação concreta dessa ideia, não a origem dela.

Robinson também descreve o [[wiki/concepts/must-ignore-pattern|Must Ignore pattern]] — pontos de extensão de schema que um consumidor pode ignorar com segurança — e aplica o Robustness Principle (validar só o que se usa, não o payload inteiro) como forma de reduzir a superfície do que conta como *breaking change*.

**Limitação apontada pelo próprio Robinson**: o padrão funciona melhor dentro de uma empresa ou comunidade fechada de serviços, onde o provedor consegue negociar com os consumidores. Não elimina o acoplamento — só torna um acoplamento antes escondido em visível e negociável.

## Consumer-Driven Contracts na prática — A inversão

Abordagem tradicional: provider define a API, consumer se adapta.
Consumer-Driven: **consumer define o que precisa**, provider verifica que ainda satisfaz.

```
Consumer escreve teste → Pact gera arquivo de contrato
                                  ↓
                       Publica no Pact Broker
                                  ↓
          Provider baixa contratos → Verifica → Publica resultado
                                  ↓
          can-i-deploy consulta o Broker antes do release
```

`can-i-deploy` é o gate: se o provider quebrou algum consumer, o deploy é bloqueado.

## Matchers — não hardcode valores

O consumer define o **mínimo que precisa**, com matchers flexíveis:

```typescript
body: {
  id: string("123"),          // string() = qualquer string
  amount: integer(150),       // integer() = qualquer inteiro
  createdAt: iso8601DateTime(),
  items: eachLike({           // eachLike() = array com ao menos 1 item
    productId: string("prod-1"),
    quantity: integer(2),
  }),
}
```

## Comparativo

| | Contract Testing | Integration E2E | Schema (OpenAPI) |
|---|---|---|---|
| Velocidade | Rápido (unitário) | Lento | Rápido |
| Detecta | Quebra de contrato | Bugs de integração real | Desvio do schema |
| Não detecta | Bugs de lógica | — | Comportamento |
| Escala com | Muitos microservices | Mal | APIs públicas |

## Quando usar / evitar

**Use:** múltiplos microsserviços com dependências, times diferentes owning consumer e provider.
**Evite:** API pública com consumers desconhecidos → OpenAPI + Schemathesis; monólito — não faz sentido.

Contract testing não substitui E2E — são camadas diferentes da [[piramide-de-testes]].

## Papel no teste de integração estreito (Fowler)

[[teste-de-integracao-estreito-vs-amplo|Martin Fowler]] descreve o combo narrow integration test + contract test como substituto do teste de integração amplo: o narrow test roda contra um double do serviço externo, e o contract test garante que esse double é fiel ao provider real. Sem o contract test, o ponto fraco do teste estreito é justamente não saber se o double mentiu — o risco central que Meszaros já sinalizava ao dizer que o double só precisa expor a "mesma API, fiel o suficiente" (ver [[wiki/sources/test-double-xunitpatterns-meszaros|fonte primária dos Test Doubles]]). O contract test é o que fecha esse "fiel o suficiente".

## Cadência, falha e o que de fato é validado (Fowler)

Em [[wiki/sources/contract-test-martin-fowler]], Fowler detalha a operação prática do contract test:

- **Não precisa rodar em todo pipeline** — o serviço externo muda no próprio ritmo, geralmente mais devagar que o time consumidor; execução diária costuma bastar.
- **Falha não deve quebrar o build automaticamente** — deve virar uma tarefa de reconciliação: atualizar o double/código do lado consumidor, ou abrir conversa com o time do serviço sobre a mudança de contrato. Para serviços críticos em produção, uma mudança não detectada pode forçar correção de emergência.
- **Roda contra ambiente de teste, não produção** — testar direto contra produção do fornecedor exige coordenação explícita.
- **Valida formato, não dado** — o contract test garante que o *formato* da chamada/resposta continua válido; é aceitável que os stubs sejam snapshots de uma resposta real capturada numa data específica, desde que o formato não tenha mudado.
- **Técnica recomendada para construir o double**: [[wiki/concepts/self-initializing-fake|SelfInitializingFake]] — um Fake que, na primeira chamada, encaminha ao serviço real e grava a resposta em cache, servindo esse cache nas chamadas seguintes; mecanismo detalhado na fonte primária do padrão, [[wiki/sources/self-initializing-fake-martin-fowler]].

## Ver também

- [[piramide-de-testes]] — onde contract testing se encaixa
- [[bdd]] — complementar para specs de comportamento
- [[race-condition]] — problema que contract testing não resolve (lógica de negócio)
- [[teste-de-integracao-estreito-vs-amplo]] — onde contract testing entra na estratégia de Fowler

## Alternativa mais barata: mockar as pontas do sistema

Quando ativar o serviço externo real (ex.: staging de um provedor de pagamentos) é caro ou lento, uma alternativa observada na prática é mockar as pontas do fluxo e testar só o sistema próprio no meio — aceitando o risco de não saber se a dependência externa de fato se comporta como o mock assume. Contract testing é o que fecha esse risco sem precisar do serviço real rodando junto.

## Key Sources

- [[wiki/sources/contract-testing]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/contract-test-martin-fowler]] — cadência de execução, tratamento de falha e SelfInitializingFake
- [[wiki/sources/self-initializing-fake-martin-fowler]] — mecanismo detalhado do double recomendado: cache na primeira chamada, caso de dados remotos que mudam, pipeline em dois estágios
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — exemplo de PSP/fornecedor mockados nas pontas de um fluxo de pagamento
- [[wiki/sources/consumer-driven-contracts-martin-fowler]] — origem do termo (Ian Robinson, 2006), modelo de três camadas, Must Ignore pattern
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — o "fiel o suficiente" do double que o contract test existe para garantir
- [[wiki/sources/microsservicos-martin-fowler-james-lewis]] — Tolerant Reader e Consumer-Driven Contracts citados como técnicas que permitem contratos de serviço evoluírem de forma independente sem gerenciamento central; menciona um time na Austrália que orienta a construção de novos serviços pelo contrato (definido antes do código), evitando over-building via YAGNI
