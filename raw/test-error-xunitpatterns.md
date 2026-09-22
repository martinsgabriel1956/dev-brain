# test error

> Tradução para português do verbete de glossário **"test error"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/test%20error.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

Um *test error* (erro de teste) ocorre quando um *[[test]]* é executado e um erro acontece que o impede de rodar até a conclusão. O erro pode ser explicitamente levantado ou lançado pelo *[[SUT]]* (system under test) ou pelo próprio teste, ou pode ser lançado pelo sistema em tempo de execução (sistema operacional, máquina virtual, etc.).

Em geral, é muito mais fácil depurar um *test error* do que uma *[[test failure]]*, porque a causa do problema tende a ser muito mais local ao ponto onde o *test error* ocorre.

Contraste com *[[test failure]]* e *[[test success]]*.

---

*Página gerada originalmente em: Wed Feb 09 16:39:20 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
