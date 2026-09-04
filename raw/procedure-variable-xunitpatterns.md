# procedure variable

> Tradução para português do verbete de glossário **"procedure variable"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/procedure%20variable.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

**Também conhecido como:** function pointer (ponteiro de função), delegate nas linguagens .Net

Uma variável que referencia um procedimento ou função, em vez de um dado. Isso permite que o código a ser chamado seja determinado em tempo de execução (*dynamic binding* — vinculação dinâmica), em vez de em tempo de compilação. O procedimento efetivo a ser invocado é atribuído à variável durante a inicialização do programa ou durante a execução.

*Procedure variables* foram um precursor das linguagens de programação verdadeiramente orientadas a objetos (OOPLs). As primeiras OOPLs, como C++, foram construídas usando tabelas (arrays) de estruturas de dados contendo *procedure variables* para implementar as tabelas de despacho (*dispatch tables*) de objetos/classes.

---

*Página gerada originalmente em: Wed Feb 09 16:39:17 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
