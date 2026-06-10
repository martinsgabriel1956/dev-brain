# Aprenda antes de aplicar — Fundamentos e Otimização Prematura

**Fonte:** transcrição de vídeo (canal não identificado — dev brasileiro)
**Idioma original:** Português (Brasil)
**Data estimada:** ~2019–2022

---

## O problema: afoiteza no aprendizado

Uma tendência comum tanto em quem está entrando na área quanto em quem já tem experiência: querer aprender muitas coisas ao mesmo tempo e aplicá-las antes de entendê-las bem.

Conceitos como design patterns, arquitetura, TDD e refatoração têm sua própria complexidade. Estudá-los bem antes de aplicar não é perda de tempo — é o que garante uma aplicação correta.

**O sintoma mais comum:** aplicar design patterns sem entender orientação a objetos. O resultado é código que força padrões onde não cabem — o chamado "verde neném" (engenharia excessiva e mal direcionada). Isso acontece tanto com iniciantes quanto com devs experientes.

---

## A progressão correta de aprendizado

O aprendizado deve ser **incremental e respeitar pré-requisitos**. Pular etapas não acelera — atrapalha.

### Estágio 1 — Programação e lógica
- Dominar uma linguagem de programação
- Aprender algoritmos
- Dado um problema, saber desenvolver um algoritmo para resolvê-lo
- **Base de tudo. Sem isso, nada funciona.**

### Estágio 2 — Modelagem orientada a objetos
- Saber o que vai ser classe no domínio
- Saber o que vai ser atributo de cada classe
- Entender como os objetos se associam
- Entender os tipos de relacionamento entre classes
- Vale um curso específico de modelagem — é o fundamento para design patterns e arquitetura

### Estágio 3 — Design patterns, testes e arquitetura
- Design patterns (GoF etc.)
- TDD (Test-Driven Development)
- Princípios de arquitetura (Clean Architecture, SOLID etc.)
- **Só faz sentido depois de dominar os dois estágios anteriores**

> "Antes de saber modelar não dá pra usar design patterns nem arquitetura."

---

## Otimização prematura

Tema relacionado: a tentação de otimizar código para performance antes da hora.

> **"Premature optimization is the root of all evil."** — Donald Knuth

Otimizar prematuramente significa gastar energia em performance antes de ter um projeto bem estruturado. O resultado quase sempre é código difícil de manter — e que frequentemente nem performa melhor.

### A ordem correta

1. **Primeiro: refatorar e projetar bem o código**
2. **Depois: otimizar para performance**

Um código bem projetado é muito mais fácil de otimizar do que um código mal estruturado. O contrário — refatorar código já otimizado para performance — é um pesadelo.

---

## Resumo das dicas

- Aprenda bem antes de querer aplicar tudo
- Respeite a progressão: programação → modelagem → design patterns / arquitetura
- Não pule fases
- Cuide primeiro do projeto, depois da performance
- Otimização prematura é a raiz de todo mal
