---
type: concept
title: "TDD — Test-Driven Development"
aliases: ["test driven development", "red green refactor", "desenvolvimento guiado por testes"]
date_created: 2026-04-22
date_updated: 2026-07-10
source_count: 6
tags: [testes, tdd, design, red-green-refactor, qualidade, dora]
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

Essas duas escolas mapeiam quase diretamente para a distinção de Fowler entre [[unit-test-solitario-vs-sociavel|unit test solitário (London) e sociável (Detroit)]].

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

### Não deixe a IA deletar testes que falham

Padrão de falha comum: a IA implementa uma feature, o teste continua falhando, e em vez de corrigir o código ela deleta ou enfraquece o teste para "fazer passar". Isso precisa ser proibido explicitamente na instrução — ver [[gaming-de-testes-por-ia]].

### "Outrunning your headlights" — por que a IA precisa de TDD mais que o humano

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] aplica um termo do Pragmatic Programmer ("outrunning your headlights" — dirigir mais rápido do que o alcance dos faróis permite enxergar) ao comportamento padrão de LLMs: mesmo com type-checking, acesso ao browser e testes automatizados disponíveis, a IA tende a gerar uma quantidade grande de código de uma vez, e só depois checa tipos ou roda testes — o oposto do ciclo RED-GREEN-REFACTOR. A taxa de feedback é o "limite de velocidade"; TDD força a IA a andar nesse limite, em passos pequenos e deliberados, em vez de acumular risco antes de qualquer verificação.

### TDD depende de módulos testáveis

A mesma fonte argumenta que testar é intrinsecamente difícil (decidir tamanho da unidade, o que mockar, quais comportamentos testar) e que **[[wiki/concepts/modulo-profundo|módulos profundos]]** — poucos módulos grandes com interface simples — são o que torna uma base de código genuinamente testável: a fronteira de teste é a própria interface do módulo, sem precisar mockar uma teia de dependências internas. Uma base de código cheia de módulos rasos gera testes flaky ou excessivamente mockados, prejudicando o próprio loop de feedback que o TDD depende.

## TDD não é o que atrasa a entrega

Contraintuitivamente, aplicar TDD não torna a entrega mais lenta — a pesquisa [[dora-metrics|DORA]] (*Accelerate*) mostra que equipes com melhores práticas de engenharia (incluindo testes automatizados como pré-condição para deploy contínuo) entregam com mais frequência e menor lead time, não menos. TDD é parte do que torna um sistema seguro de mudar rapidamente — sem ele, cada mudança exige validação manual, que é o gargalo real. Ver [[over-engineering]] para a discussão mais ampla dessa correlação.

## 100% de cobertura não é o objetivo

Cobertura alta prova que uma linha foi executada, não que ela foi exercitada com os valores certos — não existe forma de testar (via TDD ou não) um bug que ninguém pensou em cobrir. Ver [[criterios-de-bom-teste]] para os cinco critérios (determinístico, conciso, relevante, compreensível, durável) usados para julgar se um teste feito sob TDD realmente vale o ciclo red-green-refactor.

## Key Sources

- [[wiki/sources/tdd]]
- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/tdd-sdd-bdd-era-ia]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — cobertura alta ≠ ausência de bugs
