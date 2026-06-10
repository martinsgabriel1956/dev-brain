---
type: concept
title: "Imutabilidade"
aliases: ["immutability", "dados imutáveis", "readonly"]
date_created: 2026-04-25
date_updated: 2026-06-10
source_count: 3
tags: [imutabilidade, software-design, estado, clean-code, programacao-funcional, datomic, event-sourcing, strings, encoding]
skill: tech-mentor-backend
status: stable
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

## Em Sistemas Financeiros

[[ledger-imutavel]]: em bancos, saldo nunca é um campo que se atualiza — é a soma de todas as transações. Entradas no ledger são imutáveis; erros se corrigem com estornos.

[[datomic]] implementa imutabilidade no nível do banco de dados: acumula fatos (datoms) em um log append-only. Histórico completo sempre preservado com time-travel nativo.

[[event-sourcing]] aplica o mesmo princípio ao nível do domínio: eventos são fatos imutáveis, estado é derivado por replay.

## Por que Resolve Complexidade

Bugs de mutabilidade são difíceis de reproduzir, explodem em runtime, e surgem de código distante que modificou estado que você esperava inalterado. Eliminar mutabilidade elimina toda essa classe de bugs — esse é o argumento central do paper *"Out of the Tar Pit"* que influenciou as decisões técnicas do [[nubank]].

## Conexão com Programação Funcional

[[programacao-funcional]] torna imutabilidade o padrão estrutural do paradigma. Em [[clojure]], todas as estruturas de dados são imutáveis por default.

## Imutabilidade de Strings

Em quase todas as linguagens (Go, Java, Python, JavaScript, C#, Rust), [[string|strings]] são imutáveis. O motivo não é apenas evitar aliasing — é proteger o **encoding**. Uma string [[utf-8]] é um slice de bytes onde caracteres podem ocupar 1–4 bytes. Alterar 1 byte arbitrário pode fragmentar um caractere multi-byte, corrompendo silenciosamente o encoding.

Exemplo: o caractere chinês `世` ocupa 3 bytes em UTF-8. Sobrescrever apenas o primeiro byte resultaria em uma sequência inválida — o computador não saberia interpretar os bytes restantes. Por isso, ao invés de mutar, linguagens como Go forçam criar uma nova string.

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[sources/como-strings-realmente-funcionam]] — motivação técnica para imutabilidade de strings: proteger encoding UTF-8 de corrupção por indexação de bytes
