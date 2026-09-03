---
type: concept
title: "Tail Call Optimization (TCO)"
aliases: ["TCO", "tail call optimization", "tail recursion", "recursão de cauda"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 1
tags: [cs-fundamentals, recursao, compiladores, otimizacao, call-stack]
skill: cs-fundamentals
status: stub
---

# Tail Call Optimization (TCO)

Otimização de compilador/runtime que elimina o crescimento da [[wiki/concepts/pilha|call stack]] em chamadas recursivas, quando a chamada recursiva é a **última operação** executada pela função (uma *tail call*).

## Quando é possível

Só quando não sobra **nenhum trabalho pendente** depois da chamada recursiva — nada precisa ser feito com o valor de retorno além de simplesmente devolvê-lo.

```c
// NÃO é tail call — ainda falta multiplicar por n depois do retorno
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// É tail call — a chamada recursiva é literalmente a última coisa feita
int factorial_helper(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_helper(n - 1, n * acc);
}
```

No segundo caso, toda a informação necessária para a próxima chamada já foi passada como parâmetro (o acumulador `acc`) — o compilador pode reescrever a chamada como um `jump` de volta ao início da função, em vez de um `call` que empilha um novo frame. Efetivamente vira um loop, sem crescer a call stack.

## Suporte por linguagem (irregular)

| Linguagem | Suporte a TCO |
|---|---|
| Python | Não implementa (decisão de design da CPython) |
| Go | Não otimiza |
| Kotlin, Scala | `tailrec` explícito — precisa marcar a função |
| JavaScript | TCO está na spec ES6, mas não é garantida na prática pelos engines mainstream |
| C (com otimização de compilador) | Possível — depende da flag de otimização (`-O2`/`-O3`) |

TCO não é uma propriedade universal de "toda linguagem Turing-completa" — é uma escolha de implementação de cada compilador/runtime, independente do poder computacional da linguagem.

## Por que importa

Sem TCO, uma função recursiva profunda estoura a call stack (**stack overflow**) mesmo quando o algoritmo em si é correto e o volume de dados é razoável. Com TCO, a mesma função recursiva roda com uso de memória constante — equivalente, na prática, a uma versão iterativa escrita à mão.

## Relação com outros conceitos

- [[wiki/concepts/recursao]] — TCO é o que torna certos algoritmos recursivos tão eficientes quanto sua contraparte iterativa
- [[wiki/concepts/pilha]] — TCO existe especificamente para evitar o crescimento da call stack
- [[wiki/concepts/church-turing-thesis]] — toda recursão é conversível em iteração (equivalência computacional); TCO é o compilador fazendo essa conversão automaticamente, quando a forma da função permite

## Key sources

- [[wiki/sources/recursao-vs-iteracao-call-stack-tail-call-optimization]] — demonstração em C (compiler explorer) do assembly gerado com e sem forma de tail call; caso do fatorial reescrito com helper+acumulador para viabilizar TCO
