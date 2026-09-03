# Test Fixture (in xUnit)

> Tradução para português do verbete de glossário **"test fixture (in xUnit)"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/test%20fixture%20-%20xUnit.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

Em [xUnit](xunit-xunitpatterns.md), uma **test fixture** ("fixture de teste") é tudo aquilo que precisamos ter em vigor para poder rodar um teste e esperar um resultado específico. Algumas pessoas chamam isso de **test context** ("contexto de teste").

Algumas variantes de xUnit mantêm o conceito de **test context** separado da **Testcase Class** (classe de caso de teste) que o cria; [JUnit](junit-xunitpatterns.md) e seus portes diretos se enquadram nesse grupo.

Configurar a *test fixture* é a primeira fase do **Four-Phase Test** (Teste de Quatro Fases).

Para outros significados do termo *test fixture* em contextos diferentes, veja *test fixture (disambiguation)*.

---

*Página gerada originalmente em: Wed Feb 09 16:39:21 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
