---
type: concept
title: "Efeitos Colaterais"
aliases: ["side effects", "side-effects"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [efeitos-colaterais, programacao-funcional, complexidade-acidental, ddd]
skill: tech-mentor-backend
status: stable
---

# Efeitos Colaterais

## TL;DR

Um efeito colateral é qualquer coisa que uma função faz além de calcular e retornar um valor: salvar no banco, enviar email, modificar estado externo, fazer I/O. Em [[programacao-funcional]], efeitos colaterais existem mas são **explícitos** e **isolados nas periferias** do sistema.

## O Problema

Funções que escondem efeitos colaterais violam o princípio de menor surpresa:

```typescript
// Nome promete: calcular preço
// Realidade: calcula + envia email + salva no banco
function calcularPreco(item: Item): number {
  const preco = item.preco * 0.9;
  sendEmail(item.clienteId, preco);     // efeito colateral escondido
  db.save({ itemId: item.id, preco });  // efeito colateral escondido
  return preco;
}
```

Isso viola o contrato implícito da função, torna testes difíceis e bugs imprevisíveis.

## Efeitos Colaterais Explícitos

[[programacao-funcional]] obriga declarar efeitos:

```clojure
; Clojure — io! por convenção sinaliza efeito colateral
(defn calcular-preco [item desconto]
  (* (:preco item) (- 1 desconto)))   ; pura — sem efeitos

(defn processar-pedido! [item desconto]   ; ! sinaliza efeito colateral
  (let [preco (calcular-preco item desconto)]
    (send-email! ...)
    (db/save! ...)
    preco))
```

## Efeitos nas Periferias (Arquitetura Hexagonal)

Em [[ddd]] com arquitetura hexagonal:
- **Centro (domínio)**: lógica pura, sem efeitos colaterais
- **Periferias (adapters)**: onde I/O, banco, email, APIs externas vivem

```
[HTTP Adapter] → [Domain (puro)] → [DB Adapter]
                      ↑
              sem efeitos colaterais
```

O domínio não sabe que existe banco de dados. Isso o torna testável com funções puras.

## Conexão com Event Sourcing

[[event-sourcing]] aplica esse princípio ao nível de persistência: o aggregate (domínio) apenas emite eventos (puro), e o framework/adapter persiste esses eventos (efeito colateral explícito nas bordas).

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
