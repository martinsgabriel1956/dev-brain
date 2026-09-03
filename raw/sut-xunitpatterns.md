# SUT (System Under Test)

> Tradução para português do verbete de glossário **"SUT"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/SUT.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Verbete de glossário do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Também conhecido como: **AUT**, **MUT**, **CUT**.
> Tradução feita para fins de estudo.

**Também conhecido como:** AUT, MUT, CUT

O "sistema sob teste" (*system under test*). É a abreviação de "seja lá o que for que estamos testando" e é sempre definido a partir da perspectiva do teste.

Quando estamos escrevendo **testes de unidade** (*unit tests*), o **sistema sob teste (SUT)** é qualquer classe (também conhecida como **CUT** — *class under test*), objeto (também conhecido como **OUT** — *object under test*) ou método(s) (também conhecido como **MUT** — *method(s) under test*) que estamos testando.

Quando estamos escrevendo **testes de cliente** (*customer tests*), o SUT é provavelmente a aplicação inteira (também conhecida como **AUT** — *application under test*) ou pelo menos um subsistema importante dela.

As partes da aplicação que **não** estamos verificando neste teste em particular ainda podem estar envolvidas como um **componente do qual se depende** (*depended-on component* — **DOC**).

---

*Página gerada originalmente em: Wed Feb 09 16:39:16 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
