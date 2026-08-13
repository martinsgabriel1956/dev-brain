---
type: concept
title: "Encapsulamento"
aliases: ["encapsulamento", "encapsulation", "information hiding"]
date_created: 2026-08-10
date_updated: 2026-08-13
source_count: 2
tags: [encapsulamento, separation-of-concerns, arquitetura, modularidade, backend, oop, invariante]
skill: tech-mentor-backend
status: draft
---

# Encapsulamento

Esconder os detalhes internos de uma unidade e expor apenas uma interface controlada de interação. A analogia usada em [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]: uma classe expõe **getters e setters** definindo como o mundo externo interage com ela; um módulo de [[wiki/concepts/monolito-modular]] faz o mesmo via **contratos** — os outros módulos não chamam seus internals, só o que ele expõe. Anda junto com [[wiki/concepts/separation-of-concerns]] e materializa-se em [[wiki/concepts/hexagonal-architecture]].

## O objetivo real: proteger o estado, não esconder atributos

[[wiki/sources/encapsulamento-proteger-estado-invalido]] corrige um mal-entendido comum: encapsular **não é "esconder atributos"** — esconder é o *meio*, não o *fim*. O verdadeiro objetivo é **impedir que qualquer parte do sistema coloque o objeto num estado inválido**.

O exemplo em Java: uma classe `Product` com atributos `public` aceita silenciosamente `name = ""`, `price = -500` e `stock = -20` — o objeto entra em estado inválido e ninguém impede. Ao tornar os atributos `private` e forçar toda mutação a passar por métodos que validam as regras de negócio, o objeto **nunca** chega a um estado inconsistente:

```java
public void changePrice(double price) {
    if (price <= 0) throw new IllegalArgumentException("price must be greater than zero");
    this.price = price;
}
public void decreaseStock(int quantity) {
    if (quantity <= 0)      throw new IllegalArgumentException("quantity must be greater than zero");
    if (quantity > stock)   throw new IllegalArgumentException("insufficient stock");
    this.stock -= quantity;
}
```

Duas distinções que a fonte deixa explícitas:

- **`private` é a ferramenta; a regra de negócio dentro do objeto é o fim.** O ponto não é ocultar dados, é garantir que *toda* alteração passe pelas invariantes da própria classe.
- **Encapsulamento ≠ acesso.** Tornar os atributos `private` é o encapsulamento; getters/setters e a forma de programar depois são sobre *acesso* a esses atributos. Um `setPrice` que só atribui não protege nada — o que protege é o método de comando que valida (`changePrice`).

Uma classe que expõe só setters de atribuição, sem comportamento, é um [[wiki/concepts/modelo-de-dominio-anemico]] — o anti-padrão que o encapsulamento de verdade evita. Em sistemas com muitos desenvolvedores, essa proteção é **estrutural** (não dá para esquecer de validar), e por isso previne bugs difíceis de rastrear. Conecta diretamente com [[wiki/concepts/objeto-vs-estrutura-de-dados]]: a versão `public` era uma estrutura de dados disfarçada de objeto; a versão encapsulada é um objeto de verdade (comportamento + dados privados).

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] — encapsulamento como isolamento de módulos via contratos
- [[wiki/sources/encapsulamento-proteger-estado-invalido]] — o objetivo real é proteger o estado contra estados inválidos; `private` é meio, invariante é fim; encapsulamento ≠ acesso
