# Testcase Object

> Tradução para português do artigo/padrão **"Testcase Object"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Testcase%20Object.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Padrão do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "XUnit Basics".
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 382 de xUnit Test Patterns para a informação mais atual.*

**Problema:** Como executamos os testes?

**Resumo:** Criamos um objeto **Command** para cada teste e chamamos o método `run` quando queremos executá-lo.

O **Test Runner** (página X) precisa de uma forma de encontrar e invocar os **Test Methods** (página X) apropriados e de apresentar os resultados ao usuário. Muitos **Graphical Test Runners** (ver Test Runner) permitem que o usuário navegue pela árvore de testes e escolha testes individuais para executar. Isso exige que o Test Runner seja capaz de inspecionar e manipular os testes em tempo de execução.

## Como Funciona

Instanciamos um objeto **Command** [GOF] para representar cada **Test Method** a ser executado. Usamos a **Testcase Class** (página X) como uma **Test Suite Factory** (ver Test Enumeration, página X) para criar um **Test Suite Object** (página X) que armazena todos os *Testcase Objects* de uma determinada **Testcase Class**. Podemos usar **Test Discovery** (página X) ou **Test Enumeration** (página X) para criar os *Testcase Objects*.

## Por Que Fazemos Isso

Tratar os testes como objetos de primeira classe abre uma série de possibilidades que não estariam disponíveis se os tratássemos como simples procedimentos. É muito mais fácil para o **Test Runner** do **Test Automation Framework** (página X) manipular os testes quando eles são objetos. Podemos mantê-los em coleções (**Test Suite Objects**), iterar sobre eles, invocá-los, etc.

A maioria dos membros da família **xUnit** cria um *Testcase Object* separado para cada teste, para isolar os testes uns dos outros, conforme prescrito por **Independent Test** (ver Principles of Test Automation, página X). Infelizmente, sempre existe uma exceção (ver **There's Always an Exception**, página X) e os usuários dos **Test Automation Frameworks** afetados precisam ser um pouco mais cautelosos.

## Notas de Implementação

Cada *Testcase Object* implementa uma interface de teste padrão, de modo que o **Test Runner** não precisa conhecer a interface específica de cada teste. Isso permite que cada *Testcase Object* atue como um objeto **Command** [GOF]. Isso nos permite construir coleções desses *Testcase Objects*, sobre as quais podemos iterar para contar, executar, exibir, etc.

Na maioria das linguagens de programação, precisamos criar uma classe para definir o comportamento dos *Testcase Objects*. Poderíamos criar uma **Testcase Class** separada para cada *Testcase Object*, mas é mais conveniente hospedar vários **Test Methods** em uma única **Testcase Class**, já que isso resulta em menos classes para gerenciar e facilita a reutilização de **Test Utility Methods** (página X). Isso exige uma forma de cada *Testcase Object* da **Testcase Class** saber qual **Test Method** deve invocar. **Pluggable Behavior** [SBPP] é a forma mais comum de fazer isso. O construtor da **Testcase Class** recebe o nome do método a ser invocado como parâmetro e armazena esse nome em uma variável de instância. Quando o método `run` é invocado pelo **Test Runner** no *Testcase Object*, ele usa **reflection** para encontrar e invocar o método cujo nome está na variável.

## Exemplo: Testcase Object

A principal evidência da existência dos *Testcase Objects* aparece no **Test Tree Explorer** (ver Test Runner) quando "descemos" (drill down) no **Test Suite Object** para expor os *Testcase Objects* que ele contém. Aqui está um exemplo do **Graphical Test Runner** do **JUnit** embutido no Eclipse. Segue a lista de objetos criados a partir do código de exemplo do texto sobre **Testcase Class**:

```
TestSuite("...flightstate.featuretests.AllTests")
   TestSuite("...flightstate.featuretests.TestApproveFlight")   
      TestApproveFlight("testScheduledState_shouldThrowIn..ReEx")
      TestApproveFlight("testUnsheduled_shouldEndUpInAwai..oval")
      TestApproveFlight("testAwaitingApproval_shouldThrow..stEx")
      TestApproveFlight("testWithNullArgument_shouldThrow..ntEx")
      TestApproveFlight("testWithInvalidApprover_shouldTh..ntEx")
   TestSuite("...flightstate.featuretests.TestDescheduleFlight")
      TestDescheduleFlight("testScheduled_shouldEndUpInSc..tate")
      TestDescheduleFlight("testUnscheduled_shouldThrowIn..stEx")
      TestDescheduleFlight("testAwaitingApproval_shouldTh..stEx")
   TestSuite("...flightstate.featuretests.TestRequestApproval")
      TestRequestApproval("testScheduledState_shouldThrow..stEx")
      TestRequestApproval("testUnsheduledState_shouldEndU..oval")
      TestRequestApproval("testAwaitingApprovalState_shou..stEx")
   TestSuite("...flightstate.featuretests.TestScheduleFlight")
      TestScheduleFlight("testUnscheduled_shouldEndUpInSc..uled")
      TestScheduleFlight("testScheduledState_shouldThrowI..stEx")
      TestScheduleFlight("testAwaitingApproval_shouldThro..stEx")
```

O nome fora dos parênteses é o nome da classe, enquanto a string dentro dos parênteses é o nome do objeto criado a partir dessa classe. Por convenção, o nome do **Test Method** a ser executado é usado como o nome do *Testcase Object*, e o nome de um **Test Suite Object** é a string que foi passada ao construtor.

*(Nota do autor original: partes de alguns nomes foram substituídas por ".." para manter cada linha dentro do limite de largura da página.)*

---

*Página gerada originalmente em: Wed Feb 09 16:39:47 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
