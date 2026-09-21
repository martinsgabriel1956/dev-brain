# Sempre Existe uma Exceção

> Tradução para português do artigo/sidebar **"There's Always an Exception"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/There%20is%20Always%20an%20Exception.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Sidebar do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "Sidebars".
> Tradução feita para fins de estudo.

Seja aprendendo a conjugar verbos numa língua nova, seja procurando padrões em como software é construído, **sempre existe uma exceção**!

Uma das exceções mais notáveis na família [xUnit](xUnit.html) diz respeito ao uso de um **Testcase Object** (página X) para representar cada **Test Method** (página X) em tempo de execução. Esse é um recurso de design chave do xUnit, uma forma de alcançar **Independent Test** (ver Principles of Test Automation, página X). Os únicos membros da família (que o autor conhece) que não fazem isso são o **TestNG** e o **NUnit** (versão 2.x). Pelos motivos descritos abaixo, os criadores do NUnit 2.0 escolheram se afastar do caminho já bem estabelecido de uma **Testcase Object** por **Test Method** e criar apenas uma única instância da **Testcase Class** (página X) (que eles chamam de *test fixture*) e reutilizá-la para cada Test Method. Um dos autores do NUnit 2.0, James Newkirk, escreve:

> "Acho que uma das maiores burradas que cometemos ao escrever o NUnit V2.0 foi não criar uma nova instância da classe de test fixture para cada método de teste contido nela. Digo 'nós', mas acho que essa foi culpa minha. Eu não entendia direito o raciocínio do JUnit para criar uma nova instância do test fixture a cada método de teste. Olhando para trás agora, percebo que reutilizar a instância para cada método de teste permite que alguém armazene uma variável de membro em um teste e a use em outro. Isso pode introduzir dependências de ordem de execução que, para esse tipo de teste, é um anti-padrão. É muito melhor isolar completamente cada método de teste dos demais. Isso exige que um novo objeto seja criado para cada método de teste."

Infelizmente, isso tem consequências bem interessantes para quem está acostumado com o "comportamento de nova instância do JUnit" — um Testcase Object separado por método. Como o objeto é reutilizado, qualquer objeto referenciado por ele via uma variável de instância fica disponível para todos os testes subsequentes. Isso resulta num **Shared Fixture** implícito (página X), junto com todas as várias formas de *Erratic Test* (página X) que o acompanham. James continua:

> "Como seria difícil mudar a forma como o NUnit funciona agora — muita gente reclamaria — hoje eu deixo todas as variáveis de membro nas classes de test fixture como `static`. É quase uma propaganda enganosa verdadeira. O resultado é que só existe uma instância dessa variável, não importa quantos objetos de test fixture sejam criados. Se a variável é static, alguém que talvez não esteja familiarizado com como o NUnit executa não vai assumir que uma nova é criada antes de cada teste ser executado. É o mais próximo que consigo chegar de como o JUnit funciona, sem mudar a forma como o NUnit executa os métodos de teste."

Martin Fowler considerou essa exceção importante o suficiente para escrever um artigo sobre por que a abordagem do JUnit está correta. Ver http://martinfowler.com/bliki/JunitNewInstance.html

---

*Página gerada originalmente em: Wed Feb 09 16:39:03 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
