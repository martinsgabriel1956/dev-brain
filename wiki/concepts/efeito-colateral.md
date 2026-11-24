---
type: concept
title: "Efeito Colateral"
aliases: ["side effect", "efeitos colaterais", "funções puras"]
date_created: 2026-04-25
date_updated: 2026-11-24
source_count: 6
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
- [[wiki/concepts/idempotencia]] — funções idempotentes têm efeitos colaterais controlados e repetíveis

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]

## Key sources (adição 2026-10-06)

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — `enableBlackFriday` só muta um `discount` global e não retorna nada: a ordem das chamadas altera o resultado. Ver [[wiki/concepts/dependencia-externa-oculta]].

## Key sources (adição 2026-10-09)

- [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] — [[wiki/concepts/cqs]]: query não pode ter efeito colateral observável; exemplo `visualizarNotificacoes` que também marca como lida, separado em `obterNaoLidas` + `marcarComoLidas`

## No JavaScript Ninja, semana 2, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-unarios]], o critério na escala de um operador: `-x` "não causa efeito colateral. Se eu chamar o valor de x aqui, vai continuar sendo 3"; `++` e `--` "causam o efeito colateral" porque gravam o novo valor na variável ([[wiki/concepts/operadores-unarios-javascript]]).

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], `pessoa.aniversario()` não devolve nada e muda `pessoa.idade`; `pessoa.nomeCompleto()` só devolve. O método com efeito altera o objeto compartilhado, visível por qualquer referência a ele.

## Key sources (adição 2026-11-03)

- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] — testar notificações exige não enviar e-mail de verdade ao cliente; Strategy com dependência injetada como solução
- [[wiki/sources/javascript-ninja-operadores-unarios]]: JavaScript Ninja, semana 2, vídeo 02: -x puro × ++/-- com efeito
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: aniversario com efeito × nomeCompleto puro
