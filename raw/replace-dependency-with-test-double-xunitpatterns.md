# Replace Dependency with Test Double

> Tradução para português da refatoração de teste **"Replace Dependency with Test Double"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Replace%20Dependency%20with%20Test%20Double.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Capítulo de referência do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Categoria: Test Refactorings.
> Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente em relação a esta versão web.
> Tradução feita para fins de estudo.

**Problema que a refatoração resolve:** As dependências do objeto sendo testado atrapalham a execução dos testes.

**Solução em uma frase:** Quebramos a dependência substituindo um **componente do qual se depende** (*depended-on component*) por um **Test Double**.

---

## Notas de Implementação

O primeiro passo é decidir qual forma de substituição de dependência será usada. **Dependency Injection** (injeção de dependência) é a melhor opção para **unit tests** (testes de unidade), enquanto **Dependency Lookup** (busca de dependência) costuma funcionar melhor para **customer tests** (testes de aceitação/cliente). Em seguida, refatoramos o **SUT** (*system under test*) para suportar essa substituição — ou já projetamos essa capacidade no SUT desde o início, como parte do **test-driven development** (desenvolvimento orientado a testes).

A próxima decisão é entre usar um **Fake Object**, um **Test Stub** ou um **Mock Object**, com base em como o Test Double será utilizado pelo teste. Essa decisão é discutida em mais detalhes no capítulo/narrativa "Using Test Doubles".

Se estivermos usando um **Test Stub** ou **Mock Object**, também é preciso decidir entre um **Hard-Coded Test Double** (com respostas embutidas no código) ou um **Configurable Test Double** (configurável durante o fixture setup). Os trade-offs entre essas duas abordagens são discutidos no capítulo mencionado e nas descrições detalhadas de cada padrão. Essa escolha determina o formato do teste — testes com **Mock Object**, por exemplo, tendem a ser mais "carregados no início" (*front loaded*), já que boa parte do trabalho acontece na construção do próprio Mock Object.

Por fim, modificamos o teste para:

1. Construir o Test Double.
2. Opcionalmente configurá-lo.
3. Instalá-lo no lugar da dependência real.

Para alguns tipos de **Mock Object**, também pode ser necessário adicionar uma chamada ao método de **verification** (verificação) ao final do teste.

Em linguagens estaticamente tipadas, pode ser necessário aplicar antes a refatoração **Extract Interface** [Fowler] para então introduzir a implementação falsa. Depois disso, usamos essa interface como o tipo da variável que guarda a referência à **substitutable dependency** (dependência substituível).

---

## Vocabulário-chave

- **SUT** (*System Under Test*) — o sistema/código sendo testado.
- **Depended-On Component (DOC)** — componente do qual o SUT depende, alvo da substituição.
- **Test Double** — termo guarda-chuva para qualquer objeto que substitui uma dependência real em um teste (Fake Object, Test Stub, Mock Object, etc.).
- **Dependency Injection** — mecanismo de substituição de dependência via injeção (construtor, setter, etc.), preferido para unit tests.
- **Dependency Lookup** — mecanismo de substituição de dependência via busca/registro (ex.: service locator), mais comum em customer tests.
- **Substitutable dependency** (dependência substituível) — ponto do SUT projetado para permitir a troca da dependência real por um Test Double.
- **Verification method** — método chamado ao final do teste para confirmar que as interações esperadas com um Mock Object ocorreram.

---

## Padrões e Refatorações Relacionados

- Test Double (padrão guarda-chuva)
- Fake Object, Test Stub, Mock Object (variações de Test Double)
- Hard-Coded Test Double, Configurable Test Double (técnicas de construção)
- Dependency Injection, Dependency Lookup (mecanismos de substituição)
- Extract Interface [Fowler] (refatoração de código, pré-requisito em linguagens estaticamente tipadas)
- SUT, unit test, customer test, test-driven development (conceitos relacionados)
- "Using Test Doubles" (narrativa introdutória que detalha a escolha entre Fake Object, Test Stub e Mock Object)
