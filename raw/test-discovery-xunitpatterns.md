# Test Discovery

> Tradução para português do artigo/padrão **"Test Discovery"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Test%20Discovery.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Padrão do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "XUnit Basics".
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 393 de xUnit Test Patterns para a informação mais atual.*

**Problema:** Como o **Test Runner** sabe quais testes executar?

**Resumo:** O **Test Automation Framework** descobre automaticamente todos os testes que pertencem à **test suite**.

Dado que escrevemos vários **Test Methods** (página X) em uma ou mais **Testcase Classes** (página X), precisamos dar ao **Test Runner** (página X) alguma forma de encontrar os testes. *Test Discovery* elimina a maior parte do trabalho manual associado à **Test Enumeration** (página X).

## Como Funciona

O **Test Automation Framework** (página X) usa **reflection** em tempo de execução (ou conhecimento em tempo de compilação) para descobrir todos os **Test Methods** que pertencem à **test suite** e/ou todos os **Test Suite Objects** (página X) que pertencem a uma **Suite of Suites** (ver Test Suite Object). Em seguida, ele constrói os **Test Suite Objects** contendo os **Testcase Objects** (página X) correspondentes e outros **Test Suite Objects**, em preparação para executar todos os testes.

## Quando Usar

Devemos usar *Test Discovery* sempre que nosso **Test Automation Framework** oferecer suporte a isso. Isso reduz o esforço de automatizar testes e diminui bastante a possibilidade de *Lost Tests* (ver Production Bugs, página X). O único momento em que vale considerar a **Test Enumeration** é quando nosso framework não suporta *Test Discovery* ou quando queremos definir uma **Named Test Suite** (página X) composta por um subconjunto de testes escolhidos de outras test suites — um bom exemplo disso é uma suíte de *Smoke Test* [SCM] — e o **Test Automation Framework** não suporta **Test Selection** (página X). Não é incomum combinar **Test Suite Enumeration** (ver Test Enumeration) com **Test Method Discovery**; o oposto é menos comum.

## Notas de Implementação

Construir a **Suite of Suites** a ser executada pelo **Test Runner** envolve duas coisas. Primeiro, precisamos encontrar todos os **Test Methods** a serem incluídos em cada **Test Suite Object** e, segundo, precisamos encontrar todos os **Test Suite Objects** a serem incluídos no **test run** (não necessariamente nessa ordem). Cada uma dessas etapas pode ser feita manualmente, via **Test Method Enumeration** e **Test Suite Enumeration** (ver Test Enumeration), ou automaticamente, via **Test Method Discovery** e **Testcase Class Discovery**.

### Variação: Testcase Class Discovery

*Testcase Class Discovery* é o processo pelo qual o **Test Automation Framework** descobre as **Testcase Classes** sobre as quais deve fazer **Test Method Discovery**. Uma solução envolve marcar cada **Testcase Class** por meio de subclassificação de uma **Testcase Superclass** (página X) ou implementando uma **Marker Interface** [PJV1]. Outra alternativa, usada nas linguagens .Net e em versões mais recentes do **JUnit**, é usar um **class attribute** (ex.: `"[Test Fixture]"`) ou **annotation** (ex.: `"@Testcase"`) para identificar cada **Testcase Class**. Outra solução é colocar todas as classes de teste em um diretório comum e apontar o **Test Runner** (ou algum outro programa) para esse diretório. Uma quarta solução é usar uma convenção de nomenclatura para a **Testcase Class** e usar um programa externo para encontrar todos os arquivos que correspondem ao padrão de nomenclatura. Independentemente de como escolhermos fazer isso, uma vez que uma **Testcase Class** tenha sido descoberta, podemos prosseguir para **Test Method Discovery**.

### Variação: Test Method Discovery

*Test Method Discovery* consiste em fornecer uma forma de o **Test Automation Framework** descobrir os **Test Methods** em nossas **Testcase Classes**. Existem duas formas básicas de indicar que um método de uma **Testcase Class** é um **Test Method**. A forma mais tradicional é o uso de uma convenção de nomenclatura para **Test Method**, como "começa com 'test'". O **Test Automation Framework** itera sobre todos os métodos da **Testcase Class**, seleciona aqueles que começam com a string 'test' (ex.: `testCounters`) e chama o construtor de um argumento para criar o **Testcase Object** referente a esse **Test Method**. A outra alternativa, usada nas linguagens .Net e em versões mais recentes do **JUnit**, é usar um **method attribute** (ex.: `"[Test]"`) ou **annotation** (ex.: `"@Test"`) para identificar cada **Test Method**.

## Exemplo Motivador

O exemplo de código a seguir ilustra o tipo de código que seria necessário para cada **Test Method** fazer **Test Method Enumeration** (ver Test Enumeration) caso não tivéssemos *Test Discovery*:

```cpp
public:
   static CppUnit::Test *suite()
   {
      CppUnit::TestSuite *suite = new CppUnit::TestSuite( "ComplexNumberTest" );
      suite->addTest( new CppUnit::TestCaller<ComplexNumberTest>( "testEquality",
                        &ComplexNumberTest::testEquality ) );
      suite->addTest( new CppUnit::TestCaller<ComplexNumberTest>( "testAddition",
                        &ComplexNumberTest::testAddition ) );
      return suite;
   }
```

Este exemplo é de uma versão mais antiga do tutorial do **CppUnit**. Versões mais recentes não exigem mais isso.

## Notas de Refatoração

Por sorte para nós, usuários dos membros existentes da família **xUnit**, os criadores do **xUnit** perceberam a importância de *Test Discovery*, e tudo o que precisamos fazer é seguir as recomendações deles sobre como identificar nossos métodos de teste. Se eles implementaram usando uma convenção de nomenclatura, talvez precisemos fazer uma refatoração **Rename Method** [Fowler] para que o **xUnit** descubra nosso **Test Method**. Se implementaram via **method attribute**, basta adicionarmos o atributo apropriado aos nossos **Test Methods**.

## Exemplo: Test Method Discovery (usando nomenclatura de método e macro do compilador)

Quando a linguagem de programação é capaz de gerenciar os testes como objetos e invocar os métodos, mas não consegue facilmente encontrar todos os métodos a usar como testes, talvez precisemos dar um pequeno empurrão. Versões mais recentes do **CppUnit** fornecem uma macro que encontra todos os **Test Methods** em tempo de compilação e gera o código para construir a test suite, como ilustrado no exemplo anterior. O trecho de código a seguir dispara a **Test Method Discovery**:

```cpp
CPPUNIT_TEST_SUITE_REGISTRATION( FlightManagementFacadeTest );
```

Essa macro usa uma convenção de nomenclatura de método para determinar quais métodos ("member functions") transformar em **Testcase Objects**, encapsulando cada um deles com um `TestCaller`, de forma parecida com o exemplo manual que vimos anteriormente.

## Exemplo: Test Method Discovery (usando nomenclatura de método)

Os exemplos a seguir chamam atenção mais pelo código que está faltando do que pelo que está presente. Note que **não há** código para adicionar os **Test Methods** ao **Test Suite Object**.

Neste exemplo em Java, todos os métodos de teste que começam com "test" e não têm argumentos (um total de dois) são executados automaticamente pelo framework.

```java
public class TimeDisplayTest extends TestCase {
   public void testDisplayCurrentTime_AtMidnight() throws Exception {
      // Setup SUT:
      TimeDisplay theTimeDisplay = new TimeDisplay();
      // Exercise SUT:
      String actualTimeString = theTimeDisplay.getCurrentTimeAsHtmlFragment();
      // Verify outcome:
      String expectedTimeString = "<span class=\"tinyBoldText\">Midnight</span>";
      assertEquals( "Midnight", expectedTimeString,
                    actualTimeString);
   }

   public void testDisplayCurrentTime_AtOneMinuteAfterMidnight() throws Exception {
      // Setup SUT:
      TimeDisplay actualTimeDisplay = new TimeDisplay();
      // Exercise SUT:
      String actualTimeString = actualTimeDisplay.getCurrentTimeAsHtmlFragment();
      // Verify outcome:
      String expectedTimeString = "<span class=\"tinyBoldText\">12:01 AM</span>";
      assertEquals( "12:01 AM", expectedTimeString,
                    actualTimeString);
   }
}
```

## Exemplo: Test Method Discovery (usando method attributes)

Neste exemplo em C#, os testes são rotulados com o **method attribute** `[Test]`. Tanto o **CsUnit** quanto o **NUnit** usam essa forma de identificar **Test Methods**.

```csharp
   [Test]
   public void testFlightMileage_asKm()
   {
      // setup fixture
      Flight newFlight = new Flight(validFlightNumber);
      newFlight.setMileage(1122);
      // exercise mileage translater
      int actualKilometres = newFlight.getMileageAsKm();
      int expectedKilometres = 1810;
      // verify results
      Assert.AreEqual( expectedKilometres, actualKilometres);
   }

   [Test]
   [ExpectedException(typeof(InvalidArgumentException))]
   public void testSetMileage_invalidInput_attribute()
   {
      // setup fixture
      Flight newFlight = new Flight(validFlightNumber);
      // exercise SUT
      newFlight.setMileage(-1122);
   }
```

## Exemplo: Testcase Class Discovery (usando class attributes)

Aqui está um exemplo de uso de um **class attribute** para identificar uma **Testcase Class** (chamada de "Fixture" no **NUnit**) para o **Test Runner**:

```csharp
[TestFixture]
public class GoodExamples
{

}
```

## Exemplo: Testcase Class Discovery (usando localização comum e Testcase Superclass)

O exemplo em Ruby a seguir encontra todos os arquivos com a extensão `.rb` no diretório "tests" e faz `require` deles a partir deste arquivo. Isso faz com que o **Test::Unit** procure por todos os testes em cada arquivo, porque a **Testcase Class** em cada arquivo estende `Test::Unit::TestCase`.

```ruby
Dir['tests/*.rb'].each do |each|
   require each
end
```

O `Dir['tests/*.rb']` retorna uma coleção de arquivos sobre a qual o `each do` itera para implementar **Testcase Class Discovery**. O interpretador Ruby e o **Test::Unit** terminam o trabalho fazendo **Test Method Discovery** em cada classe que sofreu `require`.

---

*Página gerada originalmente em: Wed Feb 09 16:39:46 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
