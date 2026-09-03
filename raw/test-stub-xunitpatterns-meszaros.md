# Test Stub

> Tradução/adaptação para português do padrão **"Test Stub"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Test%20Stub.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Capítulo de referência do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Também conhecido como: **Stub** (uma variação de Test Double).
> Nota: o site oficial estava fora do ar no momento da ingestão; este documento foi reconstruído a partir de uma extração de conteúdo do próprio xunitpatterns.com (via proxy de leitura) combinada com resultados de busca que citam o texto original. Pode não ser 100% literal frase a frase, mas preserva fielmente a estrutura e o conteúdo técnico do padrão.
> Tradução feita para fins de estudo.

**Pergunta que o padrão resolve:** Como podemos verificar uma lógica de forma independente quando ela depende de **entradas indiretas** (*indirect inputs*) vindas de outros componentes de software?

**Solução em uma frase:** Substituímos um objeto real por um objeto **específico para o teste** que alimenta o sistema sob teste (SUT) com as entradas indiretas desejadas.

---

## Como Funciona

O mecanismo do Test Stub segue estes passos:

1. Definimos uma implementação específica para teste de uma interface da qual o SUT depende.
2. Configuramos essa implementação para responder às chamadas do SUT com valores (ou exceções) que exercitam caminhos de código ainda não testados.
3. Instalamos o Test Stub no lugar da implementação real, de modo que o SUT passe a usá-lo.
4. Durante a execução do teste, o stub retorna os valores pré-definidos sempre que é chamado.
5. Verificamos o resultado usando as asserções normais do teste (sobre a **saída direta** do SUT, não sobre interações com o stub).

Em outras palavras: o Test Stub serve como **ponto de controle** (*control point*) para as entradas indiretas do SUT — ele não é usado para verificar o comportamento do SUT (isso é papel do Mock Object ou do Test Spy).

---

## Quando Usar

Indicadores-chave para aplicar este padrão:

- Existe **código não testado** (*Untested Code*) causado pela incapacidade de controlar as entradas indiretas do SUT.
- Precisamos de um **ponto de controle** para exercitar o SUT com diferentes entradas indiretas — inclusive valores/condições difíceis de reproduzir com o componente real (erros, timeouts, respostas raras).
- **Não** precisamos verificar as **saídas indiretas** do SUT (se precisássemos, o padrão certo seria Mock Object ou Test Spy).
- O componente real de que o SUT depende não está disponível, é lento, ou tem efeitos colaterais indesejados no ambiente de teste.

Se a verificação de saídas indiretas for necessária, considere usar **Mock Object** ou **Test Spy** em vez de (ou além de) um Test Stub. Além disso, é preciso ter algum mecanismo de **dependência substituível** (*substitutable dependency*) para instalar o Test Double no SUT.

---

## Variações

### Responder

Injeta **entradas indiretas válidas** no SUT. É a variação mais comum, usada tipicamente em testes de "caminho feliz" (*happy path*) — geralmente seguindo o padrão **Simple Success Test** — quando o componente real não está disponível ou não é utilizável no ambiente de teste.

### Saboteur (Sabotador)

Injeta **entradas indiretas inválidas** para forçar caminhos de tratamento de erro. Segundo a fonte: *"seu propósito é descarrilar o que quer que o SUT esteja tentando fazer, para que possamos ver como ele lida com essas circunstâncias."* Pode retornar valores inesperados, lançar exceções ou provocar erros em tempo de execução.

### Temporary Test Stub (Stub Temporário)

Substitui temporariamente um componente ainda não implementado, com retornos *hard-coded*. É comum em desenvolvimento orientado a testes (TDD), evoluindo depois para uma classe real conforme o desenvolvimento avança.

### Procedural Test Stub

Implementado em linguagens procedurais — especialmente desafiador em linguagens sem ponteiros de função. Pode exigir "ganchos" de lógica de teste dentro do próprio código de produção (uma forma de *Test Logic in Production*).

### Entity Chain Snipping ("cortando a cadeia de entidades")

Substitui uma rede complexa de objetos relacionados por um único stub, simplificando drasticamente o *fixture setup* e melhorando a legibilidade do teste. Em vez de montar uma cadeia `Customer → Address → City → State` inteira, um único stub de `Customer` já fornece o comportamento necessário via métodos stubados.

### Hard-Coded Test Stub

As respostas ficam embutidas diretamente no código do stub, construído sob medida para um teste específico (ou um pequeno grupo de testes).

### Configurable Test Stub

Permite configurar o comportamento do stub durante a fase de *fixture setup* do teste, evitando ter que criar uma classe de stub nova para cada caso. Muitos frameworks da família xUnit oferecem ferramentas para gerar esse tipo de stub automaticamente (por reflexão/proxy dinâmico).

---

## Notas de Implementação

- Devemos ter **pelo menos um teste** que verifique o funcionamento do SUT **sem** o Test Stub — afinal, estamos testando o SUT em uma configuração diferente daquela usada em produção.
- Cuidado para **não substituir partes do próprio SUT** em vez de suas dependências — é preciso manter claro o que é o SUT e o que é *fixture*/dependência.
- Uso excessivo de stubs pode levar a **software superespecificado** (*Overspecified Software*) e a **testes frágeis** (*Fragile Tests*).
- Existem múltiplas formas de implementação (manual vs. gerada dinamicamente), a escolha depende das necessidades do teste e das ferramentas disponíveis.

---

## Exemplo Motivador

Cenário: testar um componente `TimeDisplay` que formata a hora atual como HTML. Usar o relógio real do sistema torna o teste não-determinístico e não-confiável. Tentar calcular o resultado esperado dinamicamente (com base na hora real, no momento do teste) cria dois problemas: caminhos de código não testados e duplicação da lógica do próprio SUT dentro do teste.

## Refatoração

Aplicando a refatoração **"Replace Dependency with Test Double"**, substituímos o relógio real do sistema (`TimeProvider`) por um "relógio virtual" implementado como Test Stub, configurado com o valor de hora desejado como entrada indireta.

## Exemplo — Stub construído à mão (hand-coded)

```java
TimeProviderTestStub tpStub = new TimeProviderTestStub();
tpStub.setHours(0);
tpStub.setMinutes(0);
TimeDisplay sut = new TimeDisplay();
sut.setTimeProvider(tpStub);
```

A implementação do stub mantém internamente um objeto `Calendar`, com métodos de configuração (`setHours`, `setMinutes`) e um método `getTime` que retorna a hora configurada.

## Exemplo — Stub gerado dinamicamente (JMock)

Usando um framework como o JMock, evitamos escrever a classe de stub à mão:

```java
Mock tpStub = mock(TimeProvider.class);
tpStub.stubs().method("getTime").withNoArguments()
   .will(returnValue(midnight));
sut.setTimeProvider((TimeProvider) tpStub);
```

O framework usa reflexão para gerar a implementação do stub em tempo de execução.

## Exemplo — Saboteur lançando exceção

Um stub do tipo Saboteur pode ser implementado como uma classe interna anônima que lança uma exceção:

```java
TimeProvider testStub = new TimeProvider() {
   public Calendar getTime() throws TimeProviderEx {
      throw new TimeProviderEx("Sample");
   }
};
```

Nesse tipo de teste, espera-se que o **SUT capture e trate a exceção adequadamente** — por isso o teste normalmente segue o padrão **Simple Success Test** (o SUT deve continuar funcionando/tratando o erro), e não o padrão **Expected Exception Test** (que espera que a exceção se propague para fora do SUT).

## Exemplo — Entity Chain Snipping

Uma configuração de *fixture* complexa pode ser drasticamente simplificada. Em vez de montar uma hierarquia completa `Customer → Address → City → State`, um único stub de `Customer` fornece, via métodos stubados, apenas o comportamento necessário para o teste.

---

## Distinções Importantes

- **Test Stub vs. Mock Object:** o Test Stub fornece entradas indiretas e serve como ponto de controle, mas **não verifica** saídas indiretas do SUT. O Mock Object faz as duas coisas — fornece respostas *e* verifica as interações.
- **Test Stub vs. Test Spy:** o Test Spy também verifica saídas (assim como o Mock Object), o que o torna apropriado quando é necessário um **ponto de observação**, além do ponto de controle que o Stub já oferece.

---

## Cuidados

*"Estamos testando o SUT em uma configuração diferente daquela que será usada em produção."* Por isso:

- Deve existir **ao menos um teste** que valide o comportamento real, sem stub algum.
- Um erro comum de iniciantes é **substituir partes do próprio SUT** em vez de apenas suas dependências externas — isso invalida o propósito do teste.

---

## Vocabulário-chave

- **SUT** (*System Under Test*) — o sistema/código sendo testado.
- **Indirect input** (entrada indireta) — valor que o SUT recebe de um DOC, controlado pelo Test Stub.
- **Control point** (ponto de controle) — mecanismo usado pelo teste para fornecer entradas indiretas ao SUT.
- **Observation point** (ponto de observação) — mecanismo para observar saídas indiretas do SUT (não é o foco do Test Stub puro).
- **DOC** (*Depended-On Component*) — componente do qual o SUT depende, substituído pelo stub.

---

## Padrões Relacionados

- Test Double (padrão "guarda-chuva" do qual Test Stub é uma variação)
- Test Spy, Mock Object, Fake Object, Dummy Object (outras variações de Test Double)
- Hard-Coded Test Double, Configurable Test Double (técnicas de construção)
- Four-Phase Test, Substitutable Dependency (dependência substituível)
- Simple Success Test, Expected Exception Test
- Fragile Test, Overspecified Software (armadilhas relacionadas ao uso excessivo de stubs)
