# Local Variable

> Tradução para português do verbete de glossário **"local variable"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/local%20variable.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Uma variável associada a um **bloco de código**, e não a um objeto ou classe. Uma *local variable* (variável local) só é acessível de dentro do bloco de código e sai de escopo quando esse bloco retorna para quem o chamou.

## Termos relacionados

- **instance variable** — variável associada a um objeto; pode ser sobreposta (shadowed) por uma local variable dentro de um método.
- **class variable** — variável associada à classe como um todo, e não a uma instância ou a um bloco de código.
- **block** / **block closure** — bloco de código dentro do qual uma local variable existe e é acessível.
- **global variable** — variável acessível de qualquer ponto do programa, em contraste com o escopo restrito de uma local variable.
