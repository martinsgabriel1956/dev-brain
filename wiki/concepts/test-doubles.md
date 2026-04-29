---
type: concept
title: "Test Doubles"
aliases: ["dublê de teste", "mock stub fake spy", "xunit test patterns"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Ver também

- [[tdd]] — contexto onde test doubles são usados
- [[piramide-de-testes]] — doubles são a ferramenta dos testes unitários
- [[race-condition]] — MSW ajuda a testar race conditions de rede

## Key Sources

- [[wiki/sources/test-doubles]]
