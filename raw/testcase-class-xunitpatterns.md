# Testcase Class

> Tradução para português do artigo **"Testcase Class"**, categoria "XUnit Basics" do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Testcase%20Class.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: XUnit Basics
> Também conhecido como: Test Fixture
> Tradução feita para fins de estudo.

---

*Nota do site original: "O livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Veja a página 373 de xUnit Test Patterns para as informações mais atuais."*

**Também conhecido como:** Test Fixture

_Onde colocamos nosso código de teste?_

**Agrupe um conjunto de Test Methods relacionados em uma única Testcase Class.**

Colocamos nossa lógica de teste em Test Methods, mas os Test Methods precisam estar associados a uma classe. Uma *Testcase Class* nos dá um lugar para hospedar esses métodos, que mais tarde podem ser transformados em Testcase Objects.

## Como Funciona

Reunimos todos os Test Methods que são relacionados de alguma forma em uma classe especial, a *Testcase Class*. Em tempo de execução, a *Testcase Class* atua como uma Test Suite Factory (veja Test Enumeration) que cria um Testcase Object para cada Test Method e os adiciona a um Test Suite Object, que o Test Runner usará para executá-los todos.

## Por Que Fazemos Isso

Em linguagens orientadas a objetos, preferimos colocar nossos Test Methods em uma classe em vez de tê-los como funções ou procedimentos globais (mesmo quando isso é permitido). Ao torná-los métodos de instância de uma *Testcase Class*, podemos criar um Testcase Object para cada teste instanciando a *Testcase Class* uma vez para cada Test Method. Isso nos permite manipular os Test Methods em tempo de execução. Poderíamos, é claro, implementar cada Test Method em uma classe separada, mas isso cria overhead adicional e polui o espaço de nomes de classes. Também torna mais difícil (embora não impossível) reutilizar funcionalidade entre os testes.

## Notas de Implementação

A maior parte da complexidade de escrever testes envolve como escrever os Test Methods: o que incluir inline e o que extrair para Test Utility Methods, como isolar o SUT (veja Principles of Test Automation), e assim por diante. A verdadeira "mágica" associada à *Testcase Class* ocorre em tempo de execução e é descrita em Testcase Object e Test Runner. Do nosso lado, tudo o que precisamos fazer é escrever alguns Test Methods que contenham nossa lógica de teste e deixar o Test Runner fazer sua mágica. Podemos evitar *Test Code Duplication* usando o refactoring Extract Method [Fowler] para extrair código comum em Test Utility Methods. Esses métodos podem permanecer na *Testcase Class* ou podem ser movidos para a Testcase Superclass ou para um Test Helper.

## Exemplo: Testcase Class

Aqui está um exemplo de uma *Testcase Class* simples:

```java
public class TestScheduleFlight extends TestCase {

   public void testUnscheduled_shouldEndUpInScheduled() throws Exception {
      Flight flight = FlightTestHelper.getAnonymousFlightInUnscheduledState();
      flight.schedule();
      assertTrue( "isScheduled()", flight.isScheduled());
   }

   public void testScheduledState_shouldThrowInvalidRequestEx() throws Exception {
      Flight flight = FlightTestHelper.getAnonymousFlightInScheduledState();
      try {
         flight.schedule();
         fail("not allowed in scheduled state");
      } catch (InvalidRequestException e) {
         assertEquals("InvalidRequestException.getRequest()", "schedule",
                      e.getRequest());
         assertTrue(  "isScheduled()", flight.isScheduled());
      }
   }

   public void testAwaitingApproval_shouldThrowInvalidRequestEx() throws Exception {
      Flight flight = FlightTestHelper.getAnonymousFlightInAwaitingApprovalState();
      try {
         flight.schedule();
         fail("not allowed in schedule state");
      } catch (InvalidRequestException e) {
         assertEquals("InvalidRequestException.getRequest()", "schedule",
                      e.getRequest());
         assertTrue(  "isAwaitingApproval()", flight.isAwaitingApproval());
      }
   }
}
```

Exemplo `TestcaseClassPerFeature`, extraído de `java/com/clrstream/ex3/solution/flightbooking/domain/flightstate/featuretests/TestScheduleFlight.java`.

## Leitura Adicional

Em algumas variantes do xUnit, mais notavelmente VbUnit e NUnit, a *Testcase Class* é chamada de *test fixture*. Esse uso do termo não deve ser confundido com o *test fixture* que consiste em tudo o que precisamos ter em vigor antes de podermos começar a exercitar o system under test (SUT) (essas são as precondições do teste). Também não deve ser confundido com o termo *fixture* usado pelo framework Fit, que é o Adapter [GOF] que interage com a tabela do Fit e, assim, implementa um Data-Driven Test Interpreter [GOF].

---

*Página gerada originalmente em: Wed Feb 09 16:39:47 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
