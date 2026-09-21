# Production Bugs

> Tradução para português do artigo/test smell **"Production Bugs"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Production%20Bugs.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Test smell do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "Project Smells".
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 268 de xUnit Test Patterns para a informação mais atual.*

**Encontramos bugs demais em teste formal ou em produção.**

## Sintomas

Colocamos todo esse esforço em escrever testes automatizados e, mesmo assim, o número de bugs que aparecem no teste formal (também chamado de teste de sistema) ou em **produção** (*production*) é alto demais.

## Impacto

Leva mais tempo para investigar e corrigir bugs encontrados em teste formal do que aqueles encontrados em desenvolvimento, e ainda mais tempo para os encontrados em **produção**. Isso pode nos forçar a atrasar o lançamento do produto ou a colocada em produção da aplicação, para dar tempo às correções de bugs e a um novo ciclo de testes. Esse tempo e esforço se traduzem diretamente em custo monetário e consomem recursos que poderiam, de outra forma, ser gastos adicionando mais funcionalidades ao produto ou construindo outros produtos. O atraso pode afetar a credibilidade da organização perante seus clientes. A baixa qualidade também tem um custo indireto, pois reduz o valor do produto ou serviço que estamos fornecendo.

## Causas

Bugs chegam à produção por um de vários motivos. Podem ser causados por **Infrequently Run Tests** (testes executados com pouca frequência) ou por **Untested Code** (código não testado). Este último pode ser causado por **Missing Unit Tests** (testes de unidade ausentes) ou por **Lost Tests** (testes perdidos).

Por "testes suficientes", não me refiro à quantidade, mas sim à cobertura de teste. Mudanças em **Untested Code** têm mais chance de resultar em *Production Bugs*, porque não há testes automatizados para avisar o desenvolvedor quando ele introduz um problema. **Untested Requirements** (requisitos não testados) não são verificados toda vez que os testes são executados. Então não sabemos ao certo se estão funcionando. Ambos os casos estão relacionados a *Developers Not Writing Tests* (página X).

### Causa: Infrequently Run Tests

#### Sintomas

Ouvimos dizer que nossos desenvolvedores não estão rodando os testes com frequência. Fazemos algumas perguntas e descobrimos que rodar os testes demora demais (*Slow Tests*, página X) ou produz falhas extraneous demais (*Buggy Tests*, página X).

Estamos vendo falhas de teste no **Integration Build** [SCM] diário. Ao investigarmos mais a fundo, descobrimos que os desenvolvedores frequentemente fazem commit do código sem rodar os testes em suas próprias máquinas.

#### Causa Raiz

Uma vez que tenham visto os benefícios de trabalhar com a rede de segurança dos testes automatizados, a maioria dos desenvolvedores continuará fazendo isso a menos que algo atrapalhe. Os impedimentos mais comuns são *Slow Tests*, que atrasam a integração, ou *Unrepeatable Tests* (ver Erratic Test), que forçam os desenvolvedores a reiniciar o ambiente de teste ou fazer **Manual Intervention** (intervenção manual, página X) antes de rodar os testes.

#### Possível Solução

Se a causa raiz forem *Unrepeatable Tests*, podemos tentar mudar para uma estratégia de **Fresh Fixture** (página X) para tornar os testes mais determinísticos. Mas se a causa forem *Slow Tests*, teremos que investir mais esforço em acelerar a execução dos testes.

### Causa: Lost Test

#### Sintomas

O número de testes sendo executados em uma **test suite** caiu (ou não aumentou tanto quanto o esperado). Podemos notar isso diretamente se estivermos atentos à contagem de testes, ou podemos encontrar um bug que deveria ter sido capturado por um teste que sabemos que existe, mas, ao investigar, descobrimos que o teste foi desabilitado.

#### Causa Raiz

*Lost Tests* podem ser causados tanto por um **Test Method** (página X) quanto por uma **Testcase Class** (página X) que foi desabilitada ou nunca foi adicionada à **AllTests Suite** (ver Named Test Suite, página X).

Testes podem ser deixados de fora (isto é, nunca executados) de uma test suite acidentalmente por:

- esquecer de adicionar o atributo `[test]` ao **Test Method**, ou usar um nome de método que não corresponde à convenção de nomenclatura usada pela **Test Discovery** (página X),
- esquecer de adicionar uma chamada a `suite.addTest` para incluir o **Test Method** no **Test Suite Object** (página X), ao automatizar testes em um **Test Automation Framework** (página X) que só suporta **Test Enumeration** (página X),
- esquecer de adicionar uma chamada explícita ao **Test Method** no **Test Suite Procedure** (ver Test Suite Object) em variações procedurais de **xUnit**,
- esquecer de adicionar a test suite à **Suite of Suites** (ver Test Suite Object), ou esquecer de adicionar o atributo `[Test Fixture]` à **Testcase Class**.

Testes que costumavam rodar podem ter sido desabilitados por:

- renomear o **Test Method** de forma que ele deixe de corresponder ao padrão que faz a **Test Discovery** incluí-lo na test suite (ex.: nome de método que deveria começar com "test..."),
- adição de um atributo `[Ignore]` em variantes de xUnit que usam atributos de método para indicar **Test Methods**,
- comentar (ou apagar) o código que adiciona o teste (ou a suite) explicitamente à suite.

Tipicamente, isso ocorre quando um teste está falhando e alguém o desabilita para evitar ter que lidar com falhas ao rodar outros testes, embora também possa ocorrer acidentalmente.

#### Possível Solução

Há várias formas de evitar introduzir *Lost Tests*.

Podemos usar uma **Single Test Suite** (ver Named Test Suite) para rodar um único **Test Method**, em vez de desabilitar o teste que está falhando ou lento. Podemos usar o **Test Tree Explorer** (ver Test Runner, página X) para navegar até um teste específico e rodá-lo isoladamente dentro de uma test suite. Ambas as técnicas são dificultadas por **Chained Tests** (página X) — uma forma deliberada de *Interacting Tests* (ver Erratic Test) — o que é mais um motivo para evitá-los.

Se a nossa variante de **xUnit** suportar, podemos usar o mecanismo fornecido para ignorar um teste (por exemplo, o **NUnit** permite colocar o atributo `[Ignore]` em um **Test Method** para impedir que ele seja executado). Isso tipicamente nos lembra da quantidade de testes que não estão sendo executados, para que não esqueçamos de reabilitá-los. Também podemos configurar nossa ferramenta de **continuous integration** para falhar o build caso o número de testes "ignorados" ultrapasse um determinado limite.

Podemos comparar o número de testes que temos depois do check-in com o número que existia na branch de código imediatamente antes de começarmos a integração. Simplesmente verificamos se ele aumentou pela quantidade de testes que adicionamos.

Podemos implementar, ou aproveitar, a **Test Discovery** se a nossa linguagem de programação suportar reflection.

Podemos usar uma estratégia diferente para encontrar os testes a serem executados no **Integration Build**. Algumas ferramentas de build (como o Ant) permitem encontrar todos os arquivos que correspondem a um padrão de nome (como terminar em "Test"). Não perderemos suites de teste inteiras se usarmos essa capacidade para pegar todos os testes.

### Causa: Missing Unit Test

#### Sintomas

Todos os **unit tests** passam, mas um **customer test** ainda está falhando. Em algum momento, o **customer test** foi feito para passar, mas nenhum teste de unidade foi escrito para verificar o comportamento das classes individuais. Então, uma mudança de código subsequente alterou o comportamento de uma das classes e isso quebrou a funcionalidade.

#### Causa Raiz

*Missing Unit Tests* costumam acontecer quando um time foca em escrever os **customer tests**, mas não pratica **test-driven development** usando testes de unidade. Eles construíram funcionalidade suficiente para passar nos **customer tests**, mas um refactoring subsequente quebrou isso. Testes de unidade provavelmente teriam impedido que a mudança de código chegasse ao **Integration Build**.

*Missing Unit Tests* também podem acontecer durante o **test-driven development** quando alguém se adianta e escreve código sem ter um teste falhando para guiá-lo.

#### Possível Solução

A resposta óbvia é escrever mais testes de unidade, mas isso é mais fácil de falar do que fazer, e nem sempre é eficaz. Praticar de verdade o **test-driven development** é a melhor forma de evitar *Missing Unit Tests* sem escrever testes desnecessários só para aumentar a contagem de testes.

### Causa: Untested Code

#### Sintomas

Podemos simplesmente "saber" que algum trecho de código no **system under test (SUT)** não está sendo exercitado por nenhum teste. Isso pode ser porque nunca o vimos executar, ou porque usamos ferramentas de cobertura de código para provar isso sem sombra de dúvida. No exemplo a seguir, como podemos testar que, quando o timeProvider lança uma exceção, ela é tratada corretamente?

```java
   public String getCurrentTimeAsHtmlFragment() throws TimeProviderEx {
      Calendar currentTime;
      try {
         currentTime = getTimeProvider().getTime();
      } catch (Exception e) {
         return e.getMessage();
      }
      // etc.
```
*Exemplo UntestedCode extraído de java/com/clrstream/ex7/TimeDisplay.java*

#### Causa Raiz

A causa mais comum de *Untested Code* é que o SUT tem caminhos de código que reagem a formas específicas de comportamento de um **depended-on component**, e não encontramos uma forma de exercitar esses caminhos. Tipicamente, o depended-on component é chamado de forma síncrona e ou retorna determinados valores ou lança exceções. Durante o teste normal, apenas um subconjunto das possíveis **equivalence classes** de **indirect inputs** é de fato encontrado.

Outra causa comum é a incompletude da test suite, causada por uma caracterização incompleta da funcionalidade exposta pela interface do SUT.

#### Possível Solução

Se o *Untested Code* é causado pela incapacidade de controlar os **indirect inputs** do **SUT**, a solução mais comum é usar um **Test Stub** (página X) para alimentar os diversos tipos de indirect inputs no SUT, cobrindo todos os caminhos de código. Caso contrário, pode ser suficiente configurar o depended-on component para fazê-lo retornar os diversos indirect inputs necessários para testar completamente o SUT.

### Causa: Untested Requirement

#### Sintomas

Podemos simplesmente "saber" que algum trecho de funcionalidade não está sendo testado. Ou podemos estar tentando testar um software, mas não conseguimos ver nenhuma funcionalidade visível que possa ser testada via interface pública do software. Todos os testes que escrevemos passam.

Ao fazer **test-driven development**, sabemos que precisamos adicionar algum código para atender a um requisito, mas não conseguimos encontrar uma forma de expressar a necessidade de um código que registre a ação em um **Fully Automated Test** (ver Goals of Test Automation, página X), como este:

```java
public void testRemoveFlight() throws Exception {
      // setup
      FlightDto expectedFlightDto = createARegisteredFlight();
      FlightManagementFacade facade = new FlightManagementFacadeImpl();
      // exercise
      facade.removeFlight(expectedFlightDto.getFlightNumber());
      // verify
      assertFalse("flight should not exist after being removed",
                  facade.flightExists( expectedFlightDto.getFlightNumber()));
   }
```
*Exemplo UntestedRequirementTest extraído de java/com/clrstream/ex8/test/FlightManagementFacadeTest.java*

Note que esse teste não verifica se a ação de log correta foi feita. Ele vai passar independentemente de o log ter sido implementado corretamente ou não. Aqui está o código que o teste está verificando, junto com o **indirect output** do SUT que não foi implementado corretamente.

```java
   public void removeFlight(BigDecimal flightNumber) throws FlightBookingException {
      System.out.println("      removeFlight("+flightNumber+")");
      dataAccess.removeFlight(flightNumber);
      logMessage("CreateFlight", flightNumber); // Bug!
   }
```
*Exemplo UntestedRequirement extraído de java/com/clrstream/ex8/FlightManagementFacadeImpl.java*

Se pretendemos depender da informação capturada pelo logMessage ao manter a aplicação em produção, como garantir que ela está correta? Claramente, é desejável ter testes automatizados para essa funcionalidade.

#### Impacto

Parte do comportamento exigido do **SUT** poderia ser acidentalmente desabilitada sem causar falha em nenhum teste. Software com bugs poderia ser entregue ao cliente. O medo de introduzir bugs poderia desencorajar um refactoring implacável ou a remoção de código suspeito de estar morto (não utilizado).

#### Causa Raiz

A causa mais comum de *Untested Requirements* é que o **SUT** tem comportamento que não é visível através de sua interface pública. Ele pode ter "efeitos colaterais" esperados que não podem ser observados diretamente pelo teste (como escrever um arquivo, um registro, ou chamar um método em outro objeto ou componente). Chamamos esses efeitos colaterais de **indirect outputs**.

Quando o **SUT** é uma aplicação inteira, o *Untested Requirement* pode ser resultado de não haver um conjunto completo de **customer tests** que verifiquem todos os aspectos do comportamento visível do SUT.

#### Possível Solução

Se o problema for a ausência de **customer tests**, precisamos escrever pelo menos customer tests suficientes para garantir que todos os componentes estejam integrados corretamente. Isso pode exigir melhorar a design-for-testability da aplicação, separando a camada de apresentação da camada de lógica de negócio.

Quando temos **indirect outputs** que precisamos verificar, podemos fazer **Behavior Verification** (página X) por meio do uso de **Mock Objects** (página X). O teste de indirect outputs é abordado na narrativa *Using Test Doubles*.

### Causa: Neverfail Test

#### Sintomas

Podemos simplesmente "saber" que algum trecho de funcionalidade não está funcionando, mas os testes para essa funcionalidade continuam passando mesmo assim. Ao fazer **test-driven development**, adicionamos um teste para uma funcionalidade que ainda não escrevemos, mas não conseguimos fazê-lo falhar.

#### Impacto

Se um teste não falha mesmo quando o código que implementa a funcionalidade não existe, de que utilidade ele é para **Defect Localization** (ver Goals of Test Automation)? (Não muita!)

#### Causa Raiz

Isso pode ser causado por asserções codificadas incorretamente, como `assertTrue(aVariable, true)` em vez de `assertEquals(aVariable, true)`. Outra causa é mais sinistra:

Quando temos **asynchronous tests**, falhas lançadas em outra thread ou processo podem não ser vistas ou reportadas pelo **Test Runner**.

#### Possível Solução

Podemos implementar mecanismos de detecção de falha cross-thread para garantir que os **asynchronous tests** de fato falhem, mas uma solução melhor é refatorar o código para suportar **Humble Executable** (ver Humble Object, página X).

---

*Página gerada originalmente em: Wed Feb 09 16:39:52 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
