# Strategy — Padrão de Projeto Comportamental

**Fonte:** https://refactoring.guru/pt-br/design-patterns/strategy
**Também conhecido como:** Estratégia
**Categoria:** Padrão Comportamental
**Data de adição:** 2026-05-05

---

## Propósito

O **Strategy** é um padrão de projeto comportamental que permite que você defina uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis.

---

## Problema

Um aplicativo de navegação para viajantes começa simples — apenas rotas de carro. Com o tempo, adiciona caminhada, transporte público, ciclismo, rotas turísticas...

Cada nova opção dobrava o tamanho da classe principal do navegador. O resultado:

- Qualquer mudança em um algoritmo afetava toda a classe
- Alta chance de introduzir bugs em código não relacionado
- Conflitos de merge constantes em equipe — todos mexendo na mesma classe gigante
- Impossível testar cada algoritmo isoladamente

**A raiz do problema:** uma única classe tentando fazer tudo, com condicionais enormes decidindo qual algoritmo executar.

---

## Solução

O padrão Strategy sugere extrair todos os algoritmos para **classes separadas chamadas estratégias**.

A classe original, chamada **contexto**, mantém uma referência para uma dessas estratégias e delega o trabalho para ela — ao invés de executar por conta própria.

O contexto **não é responsável por selecionar** o algoritmo. É o cliente quem passa a estratégia desejada. O contexto não sabe qual estratégia está usando — trabalha com todas através de uma interface genérica com um único método.

Desta forma, você pode adicionar novos algoritmos ou modificar os existentes **sem tocar no contexto ou nas outras estratégias**.

### Exemplo — Aplicativo de Navegação

Cada algoritmo de roteamento é extraído para sua própria classe com um único método `construirRota(origem, destino)`. Mesmo com os mesmos argumentos, cada classe pode construir uma rota diferente. O navegador não se importa com qual estratégia está usando — apenas chama `construirRota` e exibe o resultado.

---

## Analogia com o Mundo Real

Imagine que você tem que chegar ao aeroporto. Você pode:
- Pegar um ônibus
- Chamar um táxi
- Pedalar de bicicleta

Essas são suas **estratégias de transporte**. Você escolhe uma dependendo de fatores como orçamento ou tempo disponível. O objetivo (chegar ao aeroporto) é o mesmo — apenas a estratégia muda.

---

## Estrutura

```
Cliente
   │
   ▼
┌─────────────────────────┐
│         Contexto        │
│  - strategy: Strategy   │
│  + setStrategy(s)       │
│  + doSomething()        │
└─────────────────────────┘
           │ usa
           ▼
    <<interface>>
      Strategy
    + execute(data)
         ▲
    ┌────┴────┐
ConcreteA  ConcreteB  (...)
```

**Participantes:**

1. **Contexto** — mantém referência para uma estratégia concreta, se comunica com ela apenas pela interface. Expõe um setter para trocar a estratégia em tempo de execução.

2. **Interface Estratégia** — comum a todas as estratégias concretas. Declara o método que o contexto usa para executar o algoritmo.

3. **Estratégias Concretas** — implementam diferentes variações do algoritmo.

4. **Cliente** — cria o objeto estratégia específico e passa para o contexto. Pode trocar a estratégia durante a execução.

> O contexto chama o método de execução na estratégia ligada cada vez que precisa rodar o algoritmo. **Não sabe qual tipo de estratégia está usando nem como o algoritmo é executado.**

---

## Pseudocódigo

```
// Interface comum a todas as estratégias
interface Strategy is
    method execute(a, b)

// Estratégias concretas — cada uma implementa o algoritmo à sua forma
class ConcreteStrategyAdd implements Strategy is
    method execute(a, b) is
        return a + b

class ConcreteStrategySubtract implements Strategy is
    method execute(a, b) is
        return a - b

class ConcreteStrategyMultiply implements Strategy is
    method execute(a, b) is
        return a * b

// Contexto — não sabe qual estratégia está usando
class Context is
    private strategy: Strategy

    method setStrategy(strategy: Strategy) is
        this.strategy = strategy

    method executeStrategy(a, b) is
        return strategy.execute(a, b)

// Uso
context = new Context()

context.setStrategy(new ConcreteStrategyAdd())
result = context.executeStrategy(3, 4)  // 7

context.setStrategy(new ConcreteStrategyMultiply())
result = context.executeStrategy(3, 4)  // 12
```

---

## Como Implementar

1. **Identifique** na classe contexto o algoritmo sujeito a frequentes mudanças — ou uma condicional enorme que seleciona variantes.

2. **Declare a interface** da estratégia comum a todas as variantes do algoritmo.

3. **Extraia cada algoritmo** para sua própria classe. Todas devem implementar a interface estratégia.

4. **Na classe contexto**, adicione um campo para armazenar referência ao objeto estratégia e um setter para substituí-lo. O contexto deve trabalhar com a estratégia **apenas pela interface**.

5. **Os clientes** devem associar o contexto com a estratégia adequada ao comportamento esperado.

---

## Aplicabilidade

**Use o Strategy quando:**

- Você quer usar diferentes variantes de um algoritmo dentro de um objeto e ser capaz de **trocar durante a execução**.

- Você tem **muitas classes parecidas** que diferem apenas na forma que executam algum comportamento. O Strategy permite extrair o comportamento variante para uma hierarquia separada e combinar as classes originais em uma só.

- Você quer **isolar a lógica de negócio** dos detalhes de implementação de algoritmos que não são essenciais para ela.

- Sua classe tem um **operador condicional muito grande** que troca entre variantes do mesmo algoritmo. O Strategy elimina essa condicional extraindo cada variante para sua própria classe.

---

## Prós e Contras

| ✅ Prós | ❌ Contras |
|---|---|
| Troca de algoritmos durante a execução | Desnecessário se há poucos algoritmos que raramente mudam |
| Isola detalhes de implementação do algoritmo | Clientes precisam conhecer as diferenças entre estratégias para escolher a adequada |
| Substitui herança por composição | Linguagens modernas com funções anônimas/lambdas podem dispensar as classes extras |
| *Princípio aberto/fechado* — novas estratégias sem mudar o contexto | |

---

## Relações com Outros Padrões

- **Strategy vs Command:** ambos parametrizam um objeto com uma ação, mas com propósitos diferentes.
  - **Command** converte qualquer operação em objeto — permite enfileirar, desfazer, enviar remotamente.
  - **Strategy** descreve diferentes formas de fazer a *mesma coisa*, trocando algoritmos dentro de um único contexto.

- **Strategy vs Template Method:** ambos definem algoritmos, mas por mecanismos opostos.
  - **Template Method** usa herança — o esqueleto fica na classe base, etapas nas subclasses. Estático.
  - **Strategy** usa composição — o algoritmo inteiro é trocado em tempo de execução. Dinâmico.

- **Strategy vs State:** ambos trocam o comportamento de um objeto em runtime via composição. A diferença é de intenção:
  - **State** — os estados podem conhecer uns aos outros e iniciar transições entre si.
  - **Strategy** — as estratégias raramente se conhecem. A troca é feita pelo cliente.

- **Strategy vs Decorator:** Decorator muda a *pele* de um objeto (adiciona comportamento em camadas); Strategy muda o *miolo* (substitui o algoritmo inteiro).

- **Bridge, State, Strategy (e Adapter):** têm estruturas muito parecidas — todos baseados em composição, delegando trabalho para outros objetos. A diferença está na *intenção*, não na estrutura.

---

## Referência

- **URL:** https://refactoring.guru/pt-br/design-patterns/strategy
- **Site:** Refactoring Guru
- **Série:** Padrões de Projeto — Padrões Comportamentais
