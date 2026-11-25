---
type: concept
title: "Programação Funcional"
aliases: ["functional programming", "FP", "paradigma funcional"]
date_created: 2026-05-31
date_updated: 2026-11-25
source_count: 7
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

### [[wiki/concepts/imutabilidade]]
Variáveis não mudam após criadas. Elimina toda uma classe de bugs de estado compartilhado.

### [[wiki/concepts/efeitos-colaterais]] Explícitos
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

[[wiki/concepts/event-sourcing]] é naturalmente funcional: `estado_atual = reduce(eventos, estado_inicial)`.

## Código Envelhece como Vinho

Sistemas funcionais com [[ddd]] e [[wiki/concepts/event-sourcing]] têm menor taxa de degradação. Contraste com sistemas Java/Ruby OO tradicionais onde mutabilidade acumulada vira legado intocável — "código que envelhece como leite".

## Uso no Nubank

O [[nubank]] escolheu [[clojure]] (Lisp funcional sobre JVM) como linguagem principal baseado explicitamente nos benefícios de [[imutabilidade]] e controle de [[efeitos-colaterais]] para sistemas financeiros de alta escala.

## Influência sobre linguagens orientadas a objetos

[[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]] lembra as raízes no cálculo lambda e em Lisp, e cita lambdas e streams em Java como influência funcional sobre linguagens tradicionalmente associadas à [[wiki/concepts/programacao-orientada-a-objetos|POO]]. Segundo o autor, conhecer FP valia pouco profissionalmente nas décadas de 1990 e 2000, comparado a dominar POO.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]

## No JavaScript Ninja, semana 7, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]], a primeira menção no curso: guardar uma função num array e chamá-la depois é "algumas coisas de programação funcional no JavaScript"; passar função por parâmetro fica "mais para frente" ([[wiki/concepts/funcoes-de-primeira-classe]]).

## No JavaScript Ninja, semana 8, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], o fecho anuncia o próximo vídeo: "a gente fala um pouquinho sobre a programação funcional em JavaScript". A aula prepara o terreno lembrando que função é objeto e mantendo as anônimas para "alguns casos específicos".

## No JavaScript Ninja, semana 8, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]], [[wiki/entities/fernando-daciuk|Fernando Daciuk]] define o paradigma como "uma forma de você programar" em que os programas "são baseados em funções, ou nas características que as funções têm", e o liga às funções de primeira classe do JavaScript. É uma definição mais larga que a desta página: funções de primeira classe são o pré-requisito da linguagem; pureza, imutabilidade e efeitos explícitos são a disciplina do estilo, que JavaScript permite mas não impõe (leitura da wiki). A aula contrasta com Java, "executando linha a linha"; `[external]` Java tem lambdas e streams desde a versão 8 (2014).

## Key sources (adição 2026-10-06)

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — o vídeo cita a tração de FP (funções autocontidas, sem side effects) e traços de FP em Python/TypeScript; ver [[wiki/concepts/dependencia-externa-oculta]].
- [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]] — FP como paradigma paralelo à POO e influência posterior sobre Java e TypeScript
- [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos]]: JavaScript Ninja, semana 3, vídeo 01: funções de primeira classe, só a atribuição (ver [[wiki/concepts/funcoes-de-primeira-classe]])
- [[wiki/sources/javascript-ninja-arrays-metodo-push-e-loop-for]]: JavaScript Ninja, semana 7, vídeo 03: prévia de programação funcional com função no array
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: anuncia programação funcional para o vídeo seguinte
- [[wiki/sources/javascript-ninja-introducao-a-programacao-funcional]]: JavaScript Ninja, semana 8, vídeo 02: FP como "baseada em funções"; primeira classe como pré-requisito
