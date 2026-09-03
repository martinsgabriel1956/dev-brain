# unit test

> Tradução para português do verbete de glossário **"unit test"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/unit%20test.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

Um **teste** que verifica o comportamento de uma pequena parte do sistema como um todo. O que torna um teste um *teste de unidade* é que o **sistema sob teste (SUT)** é um subconjunto muito pequeno do sistema geral, e pode ser irreconhecível para alguém que não esteja envolvido na construção do software.

O **SUT** real pode ser tão pequeno quanto um único objeto ou método, que é consequência de uma ou mais decisões de design — embora seu comportamento também possa ser rastreado até algum aspecto dos requisitos funcionais.

Não há necessidade de os *testes de unidade* serem legíveis, reconhecíveis ou verificáveis pelo cliente ou pelo especialista de domínio de negócio. Contraste isso com um **teste de cliente** (*customer test*), que é derivado quase inteiramente dos requisitos e que deve ser verificável pelo cliente.

Em **eXtreme Programming**, os *testes de unidade* também são chamados de **testes de desenvolvedor** (*developer tests*) ou **testes de programador** (*programmer tests*).

---

*Página gerada originalmente em: Wed Feb 09 16:39:22 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
