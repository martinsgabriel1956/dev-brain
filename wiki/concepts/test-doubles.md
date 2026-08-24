---
type: concept
title: "Test Doubles"
aliases: ["dublê de teste", "mock stub fake spy", "xunit test patterns"]
date_created: 2026-04-22
date_updated: 2026-08-23
source_count: 12
tags: [testes, test-doubles, mock, stub, fake, spy, dummy]
skill: tech-mentor-testing
status: stable
---

# Test Doubles

Termo genérico para qualquer objeto que **substitui uma dependência real nos testes**. Taxonomia de Gerard Meszaros (*xUnit Test Patterns*, 2007). Fonte primária: [[wiki/sources/test-double-xunitpatterns-meszaros]] (a própria página canônica de Meszaros no xUnitPatterns.com).

## Vocabulário formal (SUT / DOC / entrada-saída indireta)

A fonte primária ([[wiki/sources/test-double-xunitpatterns-meszaros]]) sustenta a taxonomia num vocabulário preciso que vale internalizar — é o que falta na descrição informal "mock é fake com asserção":

- **SUT** (*System Under Test*) — o código sendo testado. **Nunca** é o que se substitui.
- **DOC** (*Depended-On Component*) — a dependência real. **É o que o double substitui.** Fonte primária isolada do termo: [[wiki/sources/depended-on-component-doc-xunitpatterns]] — "examinar e controlar" as interações do DOC com o SUT é a motivação formal para existir um Test Double.
- **Entrada indireta** (*indirect input*) — valor que o SUT **recebe** de um DOC → precisa de **ponto de controle** → Stub/Mock. Fonte primária isolada de "control point": [[wiki/sources/control-point-xunitpatterns]] — o termo é mais amplo que só essa injeção (cobre também o próprio ato de exercitar o SUT), e cobra que control points exclusivos de teste nunca sejam usados pelo production code. É durante a fase de **fixture setup** — fonte primária isolada em [[wiki/sources/fixture-setup-xunitpatterns]] — que esses control points normalmente entram em cena, colocando o DOC no estado ("the 'before' picture") necessário para o teste.
- **Saída indireta** (*indirect output*) — chamada/efeito que o SUT **dispara** sobre um DOC → precisa de **ponto de observação** → Spy/Mock.

Esse eixo **controle × observação** é o que organiza os cinco tipos — formalizado com sua própria fonte primária em [[wiki/concepts/indirect-input-output]] (verbete "indirect input" isolado, ver [[wiki/sources/indirect-input-xunitpatterns]]). Meszaros ainda separa duas perguntas ortogonais: **por que** usar o double (define Dummy/Stub/Spy/Mock/Fake) vs. **como** construí-lo (Hard-Coded vs. Configurable Test Double — a técnica de construção não muda o papel). Detalhe importante: o **double só precisa expor a mesma API** que aquele teste exercita — não a interface inteira do DOC ("fiel o suficiente para a cena", na analogia do dublê de cinema).

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

- [[wiki/concepts/indirect-input-output]] — eixo entrada/saída indireta que organiza os cinco tipos
- [[tdd]] — contexto onde test doubles são usados
- [[piramide-de-testes]] — doubles são a ferramenta dos testes unitários
- [[race-condition]] — MSW ajuda a testar race conditions de rede
- [[teste-de-integracao-estreito-vs-amplo]] — uso de doubles fora do unitário, em testes de integração estreitos
- [[unit-test-solitario-vs-sociavel]] — doubles definem se um unit test é solitário ou sociável
- [[wiki/concepts/self-initializing-fake]] — Fake que, na primeira chamada, encaminha ao serviço real e grava a resposta em cache, servindo daí em diante; técnica recomendada por Fowler para doubles usados em [[contract-testing]]

## Limite do mock: verifica a chamada, não o resultado

Mockar um banco de dados permite verificar que `db.save` foi chamado, mas não confirma que o dado foi de fato persistido — para isso o teste precisa parar de mockar e rodar contra um banco real (mesmo que dedicado a testes), o que o desloca de unitário para [[testes-integracao-banco-real|teste de integração]].

## Key Sources

- [[wiki/sources/control-point-xunitpatterns]] — verbete de glossário dedicado ao próprio termo control point: definição formal mais ampla que "back side do SUT", e a regra de que control points exclusivos de teste não devem entrar no production code
- [[wiki/sources/fixture-setup-xunitpatterns]] — verbete de glossário dedicado ao termo fixture setup: a fase em que control points/Test Doubles são usados para preparar o "before" do teste; define test fixture/test context como o produto dessa fase
- [[wiki/sources/depended-on-component-doc-xunitpatterns]] — verbete de glossário dedicado ao próprio termo DOC: definição formal e a motivação "examinar e controlar" para existir um Test Double
- [[wiki/sources/indirect-input-xunitpatterns]] — verbete de glossário dedicado a "indirect input", a metade do eixo entrada/saída que motiva o uso de Stub
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — **fonte primária** da taxonomia (página canônica de Meszaros no xUnitPatterns.com); vocabulário SUT/DOC, entrada/saída indireta, pontos de controle/observação; Mock ≠ "Stub + asserção"
- [[wiki/sources/test-doubles]]
- [[wiki/sources/test-double-martin-fowler]] — fonte secundária que popularizou o termo, com atribuição correta da taxonomia a Gerard Meszaros
- [[wiki/sources/xunit-martin-fowler]] — origem histórica da família de frameworks Xunit que dá nome ao livro de Meszaros
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/contract-test-martin-fowler]] — SelfInitializingFake como técnica para doubles usados em contract testing
- [[wiki/sources/self-initializing-fake-martin-fowler]] — fonte primária do padrão SelfInitializingFake: Fake vs. Stub, mecanismo de cache
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — limite do mock de banco: assertion de chamada não prova persistência
