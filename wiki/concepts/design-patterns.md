---
type: concept
title: "Design Patterns"
aliases: ["padrões de projeto", "GoF", "Gang of Four patterns"]
date_created: 2026-05-16
date_updated: 2026-08-04
source_count: 5
tags: [design, arquitetura, padroes, programacao]
skill: tech-mentor-leadership
status: stable
---

# Design Patterns

Catálogo de soluções reutilizáveis para problemas recorrentes em design de software, popularizado pelo livro *Design Patterns: Elements of Reusable Object-Oriented Software* (1994) — os autores são conhecidos como Gang of Four (GoF): Gamma, Helm, Johnson, Vlissides.

## Origem

Inspirados no livro *A Linguagem de Padrões* de [[wiki/entities/christopher-alexander]] — arquiteto de construções físicas que compilou mais de 250 padrões de organização urbana. A ideia: padrões emergem da observação de centenas de construções e criam uma linguagem comum para descrever seus elementos.

**Antes de 1994**, bons softwares já eram produzidos sem formalização de patterns. O livro do GoF ganhou tração porque coincidiu com o crescimento do mercado Java — pattern-matching com orientação a objetos parecia uma novidade.

## Quando estudar

**Não no início.** [[wiki/entities/fabio-akita]] é direto: para iniciantes, Design Patterns ajuda muito pouco para quase nada. Os patterns são melhor compreendidos quando você já os viu emergir na prática — quando você reconhece o que está fazendo e só precisa de um nome.

A sequência correta:
1. Escrever muito código ([[wiki/concepts/aprendizado-por-exposicao]])
2. Ler muito código de outros
3. Observar repetições surgindo espontaneamente ([[wiki/concepts/pattern-recognition]])
4. *Então* estudar patterns formalmente — para nomear o que você já conhecia

Estudar patterns primeiro e tentar aplicar resulta em uso incorreto de todas as ferramentas.

## Exemplos de patterns clássicos

- **Visitor** — percorrer estruturas de objetos sem modificá-las
- **Observer** — notificação de mudança de estado
- **Builder** — construção incremental de objetos complexos
- **Chain of Responsibility** — passar request por uma cadeia de handlers
- **Repository** — abstrair o acesso a dados (popularizado no Rails via [[wiki/entities/martin-fowler]])
- **Active Record** — registro que conhece sua própria persistência ([[wiki/entities/martin-fowler]], PoEAA, 2003)

## Frameworks como implementações de patterns

Frameworks *são* manifestações de patterns em forma de código reutilizável:
- Frameworks de UI (UIKit, WPF) → Observer, MVC, Command
- Frameworks web (Rails, Laravel) → Active Record, Repository, Front Controller
- Frameworks de sistemas distribuídos (Elixir/OTP) → Supervisor, GenServer

Estudar a [[wiki/concepts/fundacao-tecnica|fundação]] antes de estudar frameworks torna o aprendizado de qualquer framework muito mais rápido.

## Pré-requisito: Modelagem OO

Antes de estudar design patterns é obrigatório dominar [[modelagem-orientada-a-objetos]] — saber o que vira classe, o que vira atributo e como os objetos se relacionam. Sem esse fundamento, o dev não tem critério para avaliar quando um pattern é adequado. O resultado é [[over-engineering]]: patterns aplicados em todo lugar sem problema correspondente ("verde neném").

## Key Sources

- [[wiki/sources/akita-como-aprender-programacao]] — quando *não* estudar patterns; origem em Christopher Alexander; relação com GoF e Java; patterns como nomes para o que você já fazia
- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]] — modelagem OO como pré-requisito; verde neném como sintoma de pular estágios
- [[wiki/sources/arquitetura-limpa-na-pratica]] — [[wiki/concepts/template-method-pattern|Template Method]] implementado via composição (não herança) num controlador web, citando a recomendação do próprio livro GoF de favorecer composição sobre herança
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — [[wiki/concepts/observer-pattern|Observer]] e [[wiki/concepts/singleton-pattern|Singleton]] combinados para recriar o mecanismo central do [[wiki/concepts/zustand|Zustand]] com JavaScript puro
- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — [[wiki/concepts/factory-pattern|Factory]] e [[wiki/concepts/observer-pattern|Observer]] usados lado a lado como dois estágios progressivos de desacoplamento (não como escolhas concorrentes), numa refatoração incremental de um jogo em JavaScript
