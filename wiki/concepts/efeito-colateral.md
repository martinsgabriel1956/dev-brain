---
type: concept
title: "Efeito Colateral"
aliases: ["side effect", "efeitos colaterais", "funções puras"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [efeito-colateral, software-design, clean-code, funcional]
skill: tech-mentor-backend
status: stub
---

# Efeito Colateral

Um **efeito colateral** é qualquer coisa que uma função faz além de computar e retornar um valor: mutar estado externo, escrever no banco, enviar um e-mail, logar, chamar uma API.

## Funções puras vs. com efeitos

```typescript
// função pura — sem efeitos colaterais
function calcularTotal(itens: Item[]): number {
  return itens.reduce((acc, item) => acc + item.preco, 0);
}

// função com efeito colateral — muta estado externo
function fazerCompra(valor: number) {
  estadoGlobal.saldo -= valor; // efeito colateral: muta estado global
}
```

Funções puras são previsíveis: mesmo input → sempre mesmo output. Funções com efeitos colaterais dependem do estado do mundo.

## Quando efeitos colaterais são necessários

Sistemas úteis precisam de efeitos (persistir dados, enviar notificações, fazer requisições). O objetivo não é eliminar efeitos colaterais, mas **isolá-los e torná-los explícitos**:

- Efeitos no nível mais externo possível (controllers, use cases)
- Lógica de negócio sem efeitos (domain entities, transformações)
- Testes fáceis para código sem efeitos; mocks para código com efeitos

## Relações

- [[estado-compartilhado]] — mutar estado global é o efeito colateral mais problemático
- [[imutabilidade]] — dados imutáveis eliminam a classe de efeitos de mutação
- [[acoplamento]] — efeitos colaterais ocultos criam acoplamento implícito e imprevisível
- [[idempotencia]] — funções idempotentes têm efeitos colaterais controlados e repetíveis

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
