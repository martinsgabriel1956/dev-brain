# Instance Variable

> Tradução para português do verbete de glossário **"instance variable"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/instance%20variable.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Também conhecida como: **member variable** (variável de membro).

Uma variável associada a um **objeto**, e não à classe do objeto. Uma *instance variable* (variável de instância) só é acessível de dentro da instância ou através dela, e normalmente é usada para armazenar informação que se espera ser diferente de uma instância para outra.

```java
private int uniqueFlightNumber = 2000;

// Exemplo de InstanceVariable extraído de java/com/clrstream/ex6/services/test/SetupStyles.java
```

A sintaxe exata usada para acessar uma *instance variable* varia de linguagem para linguagem. A sintaxe mais comum é `objectReference.variableName` (quando a *instance variable* não é considerada **private**). Quando referenciada de dentro de métodos do próprio objeto, algumas linguagens exigem uma referência explícita ao objeto (por exemplo, `self.myVariableName` ou `this.myVariableName`), enquanto outras simplesmente assumem que qualquer variável é uma *instance variable*, a menos que seja sobreposta por **local variables** (variáveis locais).

## Termos relacionados

- **member variable** — sinônimo de instance variable.
- **local variable** — variável local; pode sobrepor (fazer shadow de) uma instance variable dentro de um método.
- **class variable** — variável associada à classe como um todo, e não a uma instância específica (contraste com instance variable).
- **attribute** — no xUnit, um dos dois sentidos do termo é sinônimo de instance variable.
