# Pluggable Behavior

> Tradução para português do verbete **"Pluggable Behavior"**, do site xUnit Patterns (categoria "External Patterns").
> Fonte: http://xunitpatterns.com/Pluggable%20Behavior.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Padrão do livro *xUnit Test Patterns: Refactoring Test Code* (2007).
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente.*

**Resumo:** Adicione uma variável que será usada para disparar um comportamento diferente.

> Usar *Pluggable Behavior* é uma solução muito melhor do que criar uma centena de subclasses diferentes, cada uma diferindo das outras em apenas um ou dois métodos.

*Pluggable Behavior* nos permite especificar o comportamento de um objeto em tempo de execução (runtime). Há duas formas comuns de implementar *Pluggable Behavior*: o **Pluggable (Method) Selector** nos permite escolher qual método existente da classe será executado, enquanto o **Pluggable Block** permite que o criador do objeto especifique um bloco de código arbitrário (`block`) a ser executado.

## Leitura adicional

Parafraseado do livro de Kent Beck, "Smalltalk Best Practice Patterns" [SBPP].

---

*Página gerada originalmente em: Wed Feb 09 16:39:06 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
