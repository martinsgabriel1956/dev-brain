---
type: concept
title: "Estado Compartilhado"
aliases: ["shared state", "estado global", "estado mutável", "estado"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [estado, estado-compartilhado, software-design, imutabilidade, debugging]
skill: tech-mentor-backend
status: stable
---

# Estado Compartilhado

**Estado** é o valor armazenado por uma variável num dado momento. **Estado compartilhado** é quando múltiplas funções leem e mutam o mesmo estado.

## O problema

```typescript
const estadoGlobal = { saldo: 1000 };

function fazerCompra(valor: number) {
  estadoGlobal.saldo -= valor;
}

function aplicarDesconto(percentual: number) {
  estadoGlobal.saldo *= 1 - percentual / 100;
}

fazerCompra(500);    // saldo: 500
aplicarDesconto(10); // saldo: 450
// qual foi a causa? em que ordem? quem mutou o quê?
```

Quando algo quebra, você não sabe qual função mutou o estado, em que ordem, e qual sequência causou o problema. Em sistemas grandes, com múltiplas funções assíncronas mutando o mesmo objeto, isso se torna impossível de debugar.

## A solução: estado isolado

Funções que **recebem** estado e **retornam** novo estado, sem mutar o original:

```typescript
function fazerCompra(saldoAtual: number, valor: number): number {
  return saldoAtual - valor;
}

function aplicarDesconto(saldoAtual: number, percentual: number): number {
  return saldoAtual * (1 - percentual / 100);
}

const saldo = 1000;
const saldoAposCompra = fazerCompra(saldo, 500);        // 500
const saldoFinal = aplicarDesconto(saldoAposCompra, 10); // 450
```

Rastreabilidade total: cada transformação é explícita, com input e output claros.

## Conexão com imutabilidade

[[imutabilidade]] é a forma de tornar estado compartilhado seguro: se os dados não podem ser mutados, múltiplas funções podem acessá-los sem risco.

## No frontend (React)

Estado compartilhado via `useState` que passa por props cria prop drilling e acoplamento. Zustand e Context são formas de compartilhar estado de forma controlada. Mesmo assim, preferir estado local (`useState`) sempre que possível.

## Relações

- [[imutabilidade]] — solução estrutural para o problema de estado compartilhado
- [[efeito-colateral]] — mutar estado global é um efeito colateral; isolá-lo elimina o efeito
- [[acoplamento]] — estado compartilhado cria acoplamento implícito entre funções
- [[idempotencia]] — funções idempotentes não dependem de estado externo mutável

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
