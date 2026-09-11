# Substitutable Dependency

> Tradução para português do verbete de glossário **"substitutable dependency"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/substitutable%20dependency.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Um componente de software pode depender de qualquer número de outros componentes. Se quisermos testar esse componente isoladamente, precisamos ser capazes de substituir os outros componentes por um **Test Double**. Existem várias maneiras de tornar algo em uma *substitutable dependency* (dependência substituível), incluindo **Dependency Injection**, **Dependency Lookup** e **Test-Specific Subclass**.

## Termos relacionados

- **Test Double** — padrão usado para substituir a dependência real por um equivalente específico para teste.
- **Dependency Injection** — técnica para tornar uma dependência substituível ao injetá-la de fora do componente (via construtor, setter ou parâmetro).
- **Dependency Lookup** — técnica para tornar uma dependência substituível ao buscá-la através de um mecanismo de lookup configurável (ex.: service locator).
- **Test-Specific Subclass** — técnica para tornar uma dependência substituível ao sobrescrever o método de criação/acesso em uma subclasse usada apenas nos testes.

---

*Página gerada originalmente em: Wed Feb 09 16:39:19 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
