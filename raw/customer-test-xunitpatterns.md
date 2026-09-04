# customer test

> Tradução para português do verbete de glossário **"customer test"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/customer%20test.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

Um **teste** que verifica o comportamento de uma fatia da funcionalidade visível do sistema geral. O **sistema sob teste (SUT)** pode ser o sistema inteiro ou uma fatia (ou "módulo") totalmente funcional, de ponta a ponta, do sistema.

Um *customer test* deve ser independente das decisões de design tomadas ao construir o SUT. Ou seja, deveríamos exigir o mesmo conjunto de *customer tests* independentemente de como escolhemos construir o SUT. (Mas *como* os *customer tests* interagem com o SUT pode ser afetado por decisões de arquitetura de software de alto nível.)

---

*Página gerada originalmente em: Wed Feb 09 16:39:10 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
