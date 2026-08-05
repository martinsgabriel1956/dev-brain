---
type: concept
title: "Factory Pattern"
aliases: ["factory", "factory method", "simple factory"]
date_created: 2026-05-05
date_updated: 2026-08-04
source_count: 2
tags: [design-patterns, creational, factory, gof]
skill: tech-mentor-backend
status: stable
---

# Factory Pattern

Padrão [[creational-patterns|criacional]] que centraliza a lógica de criação de objetos em um único lugar, escondendo qual classe concreta é instanciada do código cliente.

## Como funciona

```typescript
class UserFactory {
  static create(type: string, id: string, name: string) {
    switch (type) {
      case "admin": return new AdminUser(id, name);
      case "moderator": return new ModeratorUser(id, name);
      default: return new RegularUser(id, name);
    }
  }
}

// Uso — sem saber qual classe concreta é criada
const user = UserFactory.create("admin", "1", "John");
```

## Quando usar

- O operador `new` aparece espalhado pelo código com condicionais repetidas
- O tipo do objeto a criar depende de contexto (configuração, parâmetro, estado)
- Quer centralizar logging, validação ou pooling de objetos

## Trade-offs

| ✅ | ❌ |
|---|---|
| Lógica de criação centralizada | Adiciona camada de abstração |
| Trocar implementação = mudar só a factory | Código cliente fica acoplado à factory |
| Logging/validação/pooling em um lugar | |

## Variações GoF

- **Factory Method**: subclasses decidem qual objeto criar (polimorfismo via herança)
- **Abstract Factory**: cria famílias de objetos relacionados
- **Simple Factory**: switch/if centralizado (não é GoF oficial, mas muito comum)

## Factory como segundo estágio de desacoplamento

[[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] usa Factory para isolar uma camada de jogo (`createGame()`) misturada com a camada de input. A função factory retorna um objeto com estado privado (`players`, `frutas`) e um método público (`multiplayer(command)`) — o código cliente (camada de input) passa a chamar só esse método, sem conhecer a implementação interna. Isso resolve o **estágio 1** de acoplamento (tudo misturado), mas não elimina o acoplamento por completo: a camada de input ainda conhece explicitamente o método `game.multiplayer` — é uma chamada estática (**estágio 2**). O próprio autor nota que [[wiki/concepts/dependency-injection]] tornaria essa dependência mais flexível (fácil de trocar/mockar), mas não a removeria — só o [[wiki/concepts/observer-pattern|Observer]] chega ao terceiro estágio, onde nenhum componente conhece o outro nem estaticamente.

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — Factory como segundo estágio de desacoplamento (isolamento com chamada estática explícita), intermediário entre código "ameba" e Observer
