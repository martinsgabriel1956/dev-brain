---
type: concept
title: "Feature Envy"
aliases: ["inveja de funcionalidade", "feature envy smell"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [feature-envy, code-smells, acoplamento, coesao, clean-code]
skill: tech-mentor-backend
status: stub
---

# Feature Envy

Ocorre quando uma parte do código faz o trabalho que deveria pertencer a outra parte — tipicamente uma classe acessando atributos internos de outra classe (ou de uma classe encadeada, a duas ou mais camadas de distância) para realizar um cálculo que é responsabilidade de quem possui aqueles dados.

## Exemplo canônico

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] ilustra com um domínio de e-commerce: uma classe `OrderPrinter` com um método `print_total()` itera sobre `order.items`, acessando diretamente `product.price` e `product.discount` para calcular o total do pedido e imprimi-lo. O problema: a classe `Order` nunca expôs uma API para esse cálculo — quem deveria saber o total de um pedido é a própria `Order`, não uma classe externa que "espia" seus atributos internos e os de `Product` por baixo dela.

```
# feature envy — OrderPrinter acessa dados internos de Order e Product
def print_total(order):
    total = 0
    for item in order.items:
        total += item.product.price * item.quantity * (1 - item.product.discount)
    print(total)

# correção — a responsabilidade volta para quem possui o dado
class Order:
    def get_total(self):
        return sum(i.product.price * i.quantity * (1 - i.product.discount) for i in self.items)
```

## Por que é grave

Descrito na fonte como o smell de acoplamento mais severo do catálogo — "mais acoplado que espaguete", "um nó". Consequências concretas:

- **Manutenção:** renomear um campo interno de `Product` (ex.: `price`) quebra uma classe a duas camadas de distância (`OrderPrinter` → `Order` → `Product`), sem que exista uma dependência declarada e visível entre elas.
- **Testabilidade:** testar `print_total()` exige montar um `Order` inteiro com `Product`s populados — o teste acaba exercitando várias camadas empilhadas em vez de isolar o comportamento sob teste.

## Correção

Mover a responsabilidade do cálculo para dentro da classe que possui os dados (ex.: um método `get_total()` em `Order`). A classe consumidora (`OrderPrinter`, se ainda existir) passa a apenas exibir um valor já calculado, sem acessar variáveis internas de outra classe para fazer um cálculo que não é da sua alçada.

## Relacionado

[[wiki/concepts/code-smells]] · [[wiki/concepts/acoplamento]] · [[wiki/concepts/coesao]] · [[wiki/concepts/red-flags-de-design]] (Information Leakage é o red flag equivalente na linguagem de Ousterhout)

## Key Sources

- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]]
