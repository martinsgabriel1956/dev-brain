---
type: concept
title: "Test Doubles"
aliases: ["dublê de teste", "mock stub fake spy", "xunit test patterns"]
date_created: 2026-04-22
date_updated: 2026-07-27
source_count: 6
tags: [testes, test-doubles, mock, stub, fake, spy, dummy]
skill: tech-mentor-testing
status: stable
---

# Test Doubles

Termo genérico para qualquer objeto que **substitui uma dependência real nos testes**. Taxonomia de Gerard Meszaros (*xUnit Test Patterns*, 2007).

## Os cinco tipos

```
Dummy  → passa na assinatura, nunca é usado
Stub   → retorna valor fixo, não verifica chamada
Fake   → implementação funcional simplificada
Spy    → observa sem alterar comportamento real
Mock   → controla retorno E verifica como foi chamado
```

## Guia de escolha

| Tipo | Use quando |
|---|---|
| **Dummy** | Dependência exigida pela assinatura mas irrelevante para o teste |
| **Stub** | Teste importa com o resultado, não com quem foi chamado |
| **Fake** | Repositório/serviço com estado entre chamadas — `InMemoryUserRepository` |
| **Spy** | Verificar que efeito colateral aconteceu sem substituir o comportamento |
| **Mock** | Controlar retorno E verificar a interação (quantidade, argumentos) |

## Regra de ouro: Fake > Mock

```typescript
// ❌ Mock frágil — quebra se renomear "charge" para "processPayment"
expect(mockPayment.charge).toHaveBeenCalledWith(250);

// ✅ Fake robusto — testa o contrato, não o nome do método
const fakePayment = new InMemoryPaymentGateway();
await useCase.execute({ amount: 250 });
expect(fakePayment.getLastCharge().amount).toBe(250);
```

## Code smell: mocks excessivos

Se um teste precisa mockar 5+ dependências, o código tem **acoplamento alto demais** — refatore antes de continuar testando.

## MSW — Test Double de rede

Substitui APIs externas no nível da rede com `msw`. O código nem sabe que está sendo interceptado — mais fiel ao comportamento real que mocks de `fetch`.

## O termo "TestDouble" e o teste de integração estreito

O termo guarda-chuva "Test Double" (analogia a dublê de cinema) foi divulgado por [[wiki/entities/martin-fowler]] em seu bliki em 2006 — mas a taxonomia interna dos cinco tipos (Dummy/Fake/Stub/Spy/Mock) é de autoria de [[wiki/entities/gerard-meszaros]], criada para capturar padrões de uso da família de frameworks "[[wiki/entities/junit|Xunit]]" (ver [[wiki/sources/xunit-martin-fowler]] para a origem dessa família, criada por [[wiki/entities/kent-beck]] e Erich Gamma) e publicada no livro *xUnit Test Patterns* (2007). Fowler relata explicitamente essa autoria no próprio artigo; ver [[wiki/sources/test-double-martin-fowler]]. Test Double é a peça que viabiliza o [[teste-de-integracao-estreito-vs-amplo|narrow integration test]]: em vez de ativar um serviço externo real para testar a integração, exercita-se o código que fala com esse serviço contra um double — desde que ele seja fiel o suficiente (checado por [[contract-testing]]).

## Ver também

- [[tdd]] — contexto onde test doubles são usados
- [[piramide-de-testes]] — doubles são a ferramenta dos testes unitários
- [[race-condition]] — MSW ajuda a testar race conditions de rede
- [[teste-de-integracao-estreito-vs-amplo]] — uso de doubles fora do unitário, em testes de integração estreitos
- [[unit-test-solitario-vs-sociavel]] — doubles definem se um unit test é solitário ou sociável
- [[wiki/concepts/self-initializing-fake]] — Fake que se autovalida contra o serviço real, técnica recomendada por Fowler para doubles usados em [[contract-testing]]

## Limite do mock: verifica a chamada, não o resultado

Mockar um banco de dados permite verificar que `db.save` foi chamado, mas não confirma que o dado foi de fato persistido — para isso o teste precisa parar de mockar e rodar contra um banco real (mesmo que dedicado a testes), o que o desloca de unitário para [[testes-integracao-banco-real|teste de integração]].

## Key Sources

- [[wiki/sources/test-doubles]]
- [[wiki/sources/test-double-martin-fowler]] — fonte primária do termo, com atribuição correta da taxonomia a Gerard Meszaros
- [[wiki/sources/xunit-martin-fowler]] — origem histórica da família de frameworks Xunit que dá nome ao livro de Meszaros
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/contract-test-martin-fowler]] — SelfInitializingFake como técnica para doubles usados em contract testing
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — limite do mock de banco: assertion de chamada não prova persistência
