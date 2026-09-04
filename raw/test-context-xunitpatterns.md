# test context

Fonte original: xUnitPatterns.com — Glossário

Um *test context* (contexto de teste) é tudo o que um sistema sob teste (system under test, SUT) precisa ter em vigor para poder ser exercitado com o propósito de verificar seu comportamento. Por essa razão, o RSpec chama o test fixture (em xUnit) de "context" (contexto).

```
Fixture: um conjunto fruits com
   conteúdo = {apple, orange, pear}
Exercise: remover orange do conjunto fruits
Verify: conteúdo do conjunto fruits = {apple, pear}
```
*Exemplo de código inline*

Neste exemplo, o fixture é composto por um único conjunto e é criado diretamente no teste. Mas a forma como escolhemos construir o fixture tem ramificações de grande alcance em todos os aspectos da escrita e manutenção de testes.

---

Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.
Fonte: http://xunitpatterns.com/test%20context.html
