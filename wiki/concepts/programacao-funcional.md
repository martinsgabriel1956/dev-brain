---
type: concept
title: "Programação Funcional"
aliases: ["functional programming", "FP", "paradigma funcional"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [programacao-funcional, imutabilidade, efeitos-colaterais, clojure, scala, paradigma]
skill: tech-mentor-backend
status: stable
---

# Programação Funcional

## TL;DR

Paradigma que trata computação como avaliação de funções matemáticas puras. Proíbe (ou torna explícito) estado mutável e efeitos colaterais. Resolve estruturalmente as principais fontes de [[complexidade-acidental]] em sistemas grandes.

## Princípios Centrais

### Funções Puras
Dado o mesmo input, sempre retorna o mesmo output. Sem efeitos colaterais.

```clojure
; Função pura — determinística
(defn calcular-preco [item desconto]
  (* (:preco item) (- 1 desconto)))

; Impura — efeito colateral escondido (envia email, salva no banco)
(defn calcular-preco! [item desconto]
  (let [preco (* (:preco item) (- 1 desconto))]
    (send-email! ...)     ; efeito colateral inesperado
    (save-db! ...)        ; efeito colateral inesperado
    preco))
```

### [[Imutabilidade]]
Variáveis não mudam após criadas. Elimina toda uma classe de bugs de estado compartilhado.

### [[Efeitos-colaterais]] Explícitos
Efeitos colaterais existem (I/O é inevitável), mas são declarados explicitamente e empurrados para as periferias do sistema.

## Por que Resolve Complexidade

A programação funcional força:
1. **Funções pequenas** com responsabilidade única
2. **Composição** em vez de herança e estado compartilhado
3. **Testabilidade** — funções puras são testadas com input/output, sem mocks
4. **Raciocínio local** — você entende uma função sem ler o sistema todo

## Linguagens

| Linguagem | Nível Funcional | JVM |
|-----------|----------------|-----|
| [[clojure]] | 100% funcional | ✅ |
| Haskell | 100% puro | ❌ |
| Scala | Multi-paradigma | ✅ |
| Kotlin | Multi-paradigma | ✅ |
| Elixir | Funcional | ❌ |

## Conexão com DDD e Event Sourcing

[[ddd]] + programação funcional são complementares:
- Domínio puro no centro = funções puras sem efeitos colaterais
- Adapters na borda = onde os efeitos colaterais são explicitamente isolados

[[event-sourcing]] é naturalmente funcional: `estado_atual = reduce(eventos, estado_inicial)`.

## Código Envelhece como Vinho

Sistemas funcionais com [[ddd]] e [[event-sourcing]] têm menor taxa de degradação. Contraste com sistemas Java/Ruby OO tradicionais onde mutabilidade acumulada vira legado intocável — "código que envelhece como leite".

## Uso no Nubank

O [[nubank]] escolheu [[clojure]] (Lisp funcional sobre JVM) como linguagem principal baseado explicitamente nos benefícios de [[imutabilidade]] e controle de [[efeitos-colaterais]] para sistemas financeiros de alta escala.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
