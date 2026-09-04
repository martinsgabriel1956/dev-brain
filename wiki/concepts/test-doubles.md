---
type: concept
title: "Test Doubles"
aliases: ["dublê de teste", "mock stub fake spy", "xunit test patterns"]
date_created: 2026-04-22
date_updated: 2026-09-04
source_count: 24
tags: [testes, test-doubles, mock, stub, fake, spy, dummy]
skill: tech-mentor-testing
status: stable
---

# Test Doubles

Termo genérico para qualquer objeto que **substitui uma dependência real nos testes**. Taxonomia de Gerard Meszaros (*xUnit Test Patterns*, 2007). Fonte primária: [[wiki/sources/test-double-xunitpatterns-meszaros]] (a própria página canônica de Meszaros no xUnitPatterns.com).

## Vocabulário formal (SUT / DOC / entrada-saída indireta)

A fonte primária ([[wiki/sources/test-double-xunitpatterns-meszaros]]) sustenta a taxonomia num vocabulário preciso que vale internalizar — é o que falta na descrição informal "mock é fake com asserção":

- **SUT** (*System Under Test*) — o código sendo testado. **Nunca** é o que se substitui. Fonte primária isolada do próprio termo: [[wiki/sources/sut-xunitpatterns]] — SUT é sempre definido **a partir da perspectiva do teste** (papel relativo, não propriedade fixa do código) e seu escopo escala com a granularidade: classe/objeto/método (**CUT**/**OUT**/**MUT**) em unit tests, aplicação inteira ou subsistema (**AUT**) em customer tests.
- **DOC** (*Depended-On Component*) — a dependência real. **É o que o double substitui.** Fonte primária isolada do termo: [[wiki/sources/depended-on-component-doc-xunitpatterns]] — "examinar e controlar" as interações do DOC com o SUT é a motivação formal para existir um Test Double.
- **Entrada indireta** (*indirect input*) — valor que o SUT **recebe** de um DOC → precisa de **ponto de controle** → Stub/Mock. Fonte primária isolada de "control point": [[wiki/sources/control-point-xunitpatterns]] — o termo é mais amplo que só essa injeção (cobre também o próprio ato de exercitar o SUT), e cobra que control points exclusivos de teste nunca sejam usados pelo production code. É durante a fase de **fixture setup** — fonte primária isolada em [[wiki/sources/fixture-setup-xunitpatterns]] — que esses control points normalmente entram em cena, colocando o DOC no estado ("the 'before' picture") necessário para o teste.
- **Saída indireta** (*indirect output*) — chamada/efeito que o SUT **dispara** sobre um DOC → precisa de **ponto de observação** → Spy/Mock. Fonte primária isolada de "observation point": [[wiki/sources/observation-point-xunitpatterns]] — contraparte simétrica de control point ("como o teste inspeciona o estado pós-exercício do SUT"), com escopo mais amplo que só a saída indireta (cobre também a verificação de estado direto do próprio SUT); mesma regra de não usar em production code, aqui pelo risco de expor detalhes de implementação privados.

Esse eixo **controle × observação** é o que organiza os cinco tipos — formalizado com sua própria fonte primária em [[wiki/concepts/indirect-input-output]] (verbete "indirect input" isolado, ver [[wiki/sources/indirect-input-xunitpatterns]]). Meszaros ainda separa duas perguntas ortogonais: **por que** usar o double (define Dummy/Stub/Spy/Mock/Fake) vs. **como** construí-lo (Hard-Coded vs. Configurable Test Double — a técnica de construção não muda o papel). Detalhe importante: o **double só precisa expor a mesma API** que aquele teste exercita — não a interface inteira do DOC ("fiel o suficiente para a cena", na analogia do dublê de cinema).

**Exemplo concreto de Configurable Test Double**: [[wiki/entities/jmock|JMock]], catalogado por Meszaros na categoria "Tools" do mesmo site ([[wiki/sources/jmock]]) como framework dinâmico de Mock Object para Java. O que o verbete elogia especificamente é a **Configuration Interface** fluente usada para especificar expectativas — a API de method chaining que gera o double em runtime via reflexão/proxy dinâmico.

**Correção/refinamento (2026-09-04):** o lado Configurable não é uniforme — [[wiki/sources/utwhcm-xunitpatterns]] revela, pela estrutura de link do próprio site (`Configurable Test Double.html#Hand-Built Test Double`), que existe uma subseção **Hand-Built Test Double** dentro da página Configurable Test Double. Isso significa que "escrito à mão" **não** é sinônimo de Hard-Coded: um Hand-Built Test Double é uma classe escrita manualmente pelo desenvolvedor, mas ainda **configurável** em runtime (ex.: via setters), diferente de um Hard-Coded Test Double (comportamento fixo no código do double) e diferente também de um Configurable Test Double **gerado dinamicamente** por um framework (o caso do JMock, via reflexão/proxy). A definição completa de Hand-Built ainda depende da página primária "Configurable Test Double", não ingerida até o momento — ver questão aberta em [[wiki/sources/utwhcm-xunitpatterns]].

## Os cinco tipos

```
Dummy  → passa na assinatura, nunca é usado
Stub   → retorna valor fixo, não verifica chamada
Fake   → implementação funcional simplificada
Spy    → observa sem alterar comportamento real
Mock   → controla retorno E verifica como foi chamado
```

## Test Stub em detalhe: Responder, Saboteur e Entity Chain Snipping

Fonte primária dedicada: [[wiki/sources/test-stub-xunitpatterns-meszaros]]. A página guarda-chuva de Test Double já define Stub como o ponto de controle das entradas indiretas, mas a fonte específica de Test Stub detalha duas variações operacionais:

- **Responder** — entrega entradas **válidas** para exercitar o caminho normal (tipicamente um Simple Success Test).
- **Saboteur** — entrega entradas **inválidas** ou lança exceções, para verificar como o SUT trata falhas do seu DOC. O teste correspondente ainda segue Simple Success Test (espera-se que o SUT capture e trate a exceção internamente), não Expected Exception Test (que esperaria a exceção se propagar para fora do SUT).

Também descreve o **Entity Chain Snipping**: em vez de montar uma cadeia inteira de objetos relacionados (`Customer → Address → City → State`) só para o SUT chegar a um valor, um único stub de `Customer` já responde com o valor final necessário — reduz o *fixture setup*, ao custo de acoplar o teste ao caminho de navegação que o SUT usa.

## Da taxonomia à prática: a refatoração "Replace Dependency with Test Double"

Fonte primária dedicada: [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]]. Enquanto as fontes acima definem **o que** cada tipo de double é, esta fonte define **como** introduzi-lo num teste existente, como uma sequência de três decisões ortogonais:

1. **Mecanismo de substituição** — [[wiki/concepts/dependency-injection|Dependency Injection]] (melhor para unit tests) vs. **Dependency Lookup** (melhor para customer tests).
2. **Papel do double** — Fake Object, Test Stub ou Mock Object, decidido por como o teste vai usá-lo (não pela técnica de construção).
3. **Técnica de construção** — Hard-Coded vs. Configurable Test Double (já registrado acima). Fonte primária isolada do mecanismo por trás do lado "Configurable": [[wiki/sources/procedure-variable-xunitpatterns]] — uma **procedure variable** (function pointer, ou delegate em .Net) é uma variável que referencia um procedimento em vez de um dado, permitindo atribuir o comportamento do double em runtime (dynamic binding) em vez de fixá-lo no código do double (o caminho Hard-Coded). A mesma fonte situa isso como precursor histórico do despacho polimórfico: C++ inicial montava suas dispatch tables de objetos/classes manualmente com tabelas de procedure variables, antes de existir sintaxe de método virtual — ver [[wiki/concepts/polimorfismo]].

Em linguagens estaticamente tipadas, normalmente é preciso aplicar antes a refatoração **Extract Interface** [Fowler], para que a variável que guarda a dependência seja tipada pela interface — não pela classe concreta —, permitindo trocar a implementação real pelo double sem alterar o SUT. Testes com Mock Object tendem a ser mais "front-loaded" (trabalho concentrado na construção do double) e costumam fechar com uma chamada a um método de `verification`.

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

- [[wiki/sources/doc-xunitpatterns]] — verbete de glossário dedicado à definição formal de DOC, o que um Test Double substitui
- [[wiki/sources/control-point-xunitpatterns]] — verbete de glossário dedicado ao próprio termo control point: definição formal mais ampla que "back side do SUT", e a regra de que control points exclusivos de teste não devem entrar no production code
- [[wiki/sources/fixture-setup-xunitpatterns]] — verbete de glossário dedicado ao termo fixture setup: a fase em que control points/Test Doubles são usados para preparar o "before" do teste; define test fixture/test context como o produto dessa fase
- [[wiki/sources/depended-on-component-doc-xunitpatterns]] — verbete de glossário dedicado ao próprio termo DOC: definição formal e a motivação "examinar e controlar" para existir um Test Double
- [[wiki/sources/sut-xunitpatterns]] — verbete de glossário dedicado ao próprio termo SUT: papel relativo ao teste (não propriedade fixa do código) e as siglas irmãs CUT/OUT/MUT/AUT conforme a granularidade
- [[wiki/sources/indirect-input-xunitpatterns]] — verbete de glossário dedicado a "indirect input", a metade do eixo entrada/saída que motiva o uso de Stub
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — **fonte primária** da taxonomia (página canônica de Meszaros no xUnitPatterns.com); vocabulário SUT/DOC, entrada/saída indireta, pontos de controle/observação; Mock ≠ "Stub + asserção"
- [[wiki/sources/test-stub-xunitpatterns-meszaros]] — fonte primária dedicada à variação Test Stub; detalha Responder vs. Saboteur e o padrão Entity Chain Snipping
- [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — fonte primária da refatoração mecânica: Dependency Injection vs. Dependency Lookup, escolha do papel do double, Hard-Coded vs. Configurable, e Extract Interface como pré-requisito em linguagens estaticamente tipadas
- [[wiki/sources/test-doubles]]
- [[wiki/sources/test-double-martin-fowler]] — fonte secundária que popularizou o termo, com atribuição correta da taxonomia a Gerard Meszaros
- [[wiki/sources/xunit-martin-fowler]] — origem histórica da família de frameworks Xunit que dá nome ao livro de Meszaros
- [[wiki/sources/xunit-xunitpatterns]] — verbete de glossário formal do próprio Meszaros para o termo "xUnit": qualquer framework baseado no padrão do JUnit ou SUnit
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/contract-test-martin-fowler]] — SelfInitializingFake como técnica para doubles usados em contract testing
- [[wiki/sources/self-initializing-fake-martin-fowler]] — fonte primária do padrão SelfInitializingFake: Fake vs. Stub, mecanismo de cache
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — limite do mock de banco: assertion de chamada não prova persistência
- [[wiki/sources/test-fixture-xunitpatterns]] — verbete de glossário dedicado ao termo test fixture/test context, o "palco" onde Test Doubles entram durante a fixture setup; nuance: em JUnit esse fixture é produto da Testcase Class, não estado embutido nela
- [[wiki/sources/test-context-xunitpatterns]] — verbete de glossário dedicado ao próprio termo test context: mesma equivalência de test fixture, agora com fonte primária isolada e o dado de que o RSpec usa literalmente o nome "context" para o mesmo conceito
- [[wiki/sources/procedure-variable-xunitpatterns]] — verbete de glossário dedicado ao termo "procedure variable" (function pointer/delegate): mecanismo de dynamic binding por trás do Configurable Test Double, e precursor histórico do despacho polimórfico em C++ pré-OOP
- [[wiki/sources/observation-point-xunitpatterns]] — verbete de glossário dedicado ao próprio termo observation point: contraparte simétrica de control point, fecha a hierarquia interaction point → control point | observation point
- [[wiki/sources/interaction-point-xunitpatterns]] — verbete de glossário dedicado ao próprio termo interaction point: a categoria mãe de control point e observation point, partição binária e exaustiva de como um teste interage com o SUT
- [[wiki/sources/jmock]] — verbete de "Tools" (não Glossary) do mesmo site: descreve o JMock como exemplo concreto de framework de Mock Object com Configurable Test Double via Configuration Interface fluente
- [[wiki/sources/utwhcm-xunitpatterns]] — verbete de "References" (não Glossary/Tools) do mesmo site: revela a subdivisão Hand-Built vs. Dinamicamente Gerado dentro de Configurable Test Double, corrigindo a imprecisão anterior desta página
- [[wiki/sources/decorator-xunitpatterns]] — verbete de "External Patterns" (não Glossary/Tools/References) do mesmo site: cita a definição original do GOF para o [[wiki/concepts/decorator-pattern|Decorator]]; conexão com a construção de Test Doubles por wrapping (ex.: Test Spy em torno de um DOC real) **não confirmada** por esta fonte isolada — ver questão aberta na source page
