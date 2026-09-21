# continuous integration

> Tradução para português do verbete de glossário **"continuous integration"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/continuous%20integration.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

A prática ágil de desenvolvimento de software de integrar mudanças de código continuamente. Na prática, isso significa que os desenvolvedores integram suas mudanças a cada poucas horas ou dias. A *continuous integration* frequentemente inclui a prática de um build automatizado disparado a cada check-in. O processo de build tipicamente roda todos os testes automatizados, podendo até rodar testes que não são executados antes do check-in por demorarem demais. O build é considerado "falho" se algum teste falhar. Quando o build falha, os times tipicamente tratam consertar o build de novo como prioridade máxima — só mudanças de código voltadas a corrigir o build são permitidas até que um build bem-sucedido ocorra.

---

*Página gerada originalmente em: Wed Feb 09 16:39:10 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
