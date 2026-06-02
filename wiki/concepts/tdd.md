---
type: concept
title: "TDD — Test-Driven Development"
aliases: ["test driven development", "red green refactor", "desenvolvimento guiado por testes"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [testes, tdd, design, red-green-refactor, qualidade]
skill: tech-mentor-testing
status: stable
---

# TDD — Test-Driven Development

Prática onde o **teste é escrito antes do código de produção**. O benefício central não é cobertura — é **sentir o acoplamento antes de criá-lo**. Código difícil de testar é código com problemas de design.

## Ciclo obrigatório

```
RED → GREEN → REFACTOR → RED → GREEN → REFACTOR → ...
```

- **RED**: escreva um teste que falha — o comportamento ainda não existe
- **GREEN**: escreva o *mínimo* de código para o teste passar — sem over-engineering
- **REFACTOR**: melhore sem quebrar os testes

Sem o Refactor, TDD é apenas "testes primeiro" — acumula débito técnico com os testes.

## Armadilha: testar implementação, não comportamento

```typescript
// ❌ Frágil — quebra se renomear método interno
it("should call calculateSubtotal", () => {
  const spy = jest.spyOn(order, "calculateSubtotal");
  order.totalWithDiscount(0.1);
  expect(spy).toHaveBeenCalled();
});

// ✅ Robusto — testa o resultado observável
it("should return correct total with 10% discount", () => {
  expect(order.totalWithDiscount(0.1)).toBe(225);
});
```

## As duas escolas

### Detroit (Inside-Out / Classicist)
Começa pelas unidades internas do domínio. Usa objetos reais, mocka apenas I/O externo real (DB, HTTP). Integração validada mais cedo nas unidades.

### London (Outside-In / Mockist)
Começa pelo comportamento externo. Mocka todos os colaboradores ainda não existentes — o design emerge das interfaces que o teste exige. Risco: mocks podem mascarar integração quebrada.

## Quando usar / evitar

**Use:** lógica de negócio com múltiplos caminhos, refatorando legado (testes antes de mudar qualquer linha), algoritmos com comportamento claro antes da implementação.

**Evite:** exploração de APIs desconhecidas (spike primeiro), protótipos descartáveis, UI visual, IaC.

## Ver também

- [[bdd]] — extensão do TDD para linguagem de negócio
- [[test-doubles]] — como isolar dependências no ciclo TDD
- [[piramide-de-testes]] — onde TDD vive na estratégia de testes
- [[testar-proprio-codigo]] — hábito relacionado

## TDD com IA

Na [[era-agentica]], TDD via IA é mais poderoso do que nunca — e mais necessário. A IA gera testes em volume rapidamente, mas tende a criar testes que apenas executam o código sem validar o comportamento real. TDD inverte esse problema: o teste é escrito primeiro (por você ou pela IA), e o código só existe para passar no teste.

Forçar TDD via [[harness-de-qualidade]]:
- Pipeline rejeita código sem cobertura de teste adequada
- [[teste-de-mutacao]] valida que os testes gerados pela IA realmente testam comportamento
- O ciclo red-green-refactor garante que o código é testável por design

> *"Manda a IA fazer TDD. Ela consegue fazer isso. Configura os linters com boas regras. Ela vai seguir."*

## Key Sources

- [[wiki/sources/tdd]]
- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
