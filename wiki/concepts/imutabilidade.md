---
type: concept
title: "Imutabilidade"
aliases: ["immutability", "dados imutáveis", "readonly"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [imutabilidade, software-design, estado, clean-code]
skill: tech-mentor-backend
status: stub
---

# Imutabilidade

Imutabilidade significa que um valor **não pode ser alterado após ser criado**. Em vez de mutar, você cria um novo valor com a mudança aplicada.

## Por que importa

Dados mutáveis compartilhados são a principal fonte de bugs difíceis de rastrear (ver [[estado-compartilhado]]). Se os dados não podem ser mutados, múltiplas partes do sistema podem acessá-los com segurança.

## No TypeScript

```typescript
// readonly — sinaliza intenção no tipo
type Config = {
  readonly baseUrl: string;
  readonly timeout: number;
};

// Object.freeze — impede mutação em runtime
const CONFIG = Object.freeze({ baseUrl: "https://api.exemplo.com", timeout: 5000 });

// spread para criar novo objeto com mudança
const updatedConfig = { ...CONFIG, timeout: 10000 };
```

## Padrão funcional

Em vez de mutar, retornar novo estado:

```typescript
// mutável (problemático)
function addItem(cart: Cart, item: Item) {
  cart.items.push(item); // muta o original
}

// imutável (correto)
function addItem(cart: Cart, item: Item): Cart {
  return { ...cart, items: [...cart.items, item] };
}
```

## Relações

- [[estado-compartilhado]] — imutabilidade é a solução para os problemas de estado compartilhado
- [[efeito-colateral]] — funções imutáveis não têm efeitos colaterais
- [[acoplamento]] — dados imutáveis reduzem acoplamento implícito

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
