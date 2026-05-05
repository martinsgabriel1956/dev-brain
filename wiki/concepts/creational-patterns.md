---
type: concept
title: "Creational Patterns"
aliases: ["padrões criacionais", "criacionais"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, gof, creational]
skill: tech-mentor-backend
status: stable
---

# Creational Patterns (Padrões Criacionais)

Uma das três categorias dos 23 padrões [[gang-of-four]]. Tratam de **como objetos são criados**, dando flexibilidade sobre quando, como e qual objeto é instanciado — em vez de criar diretamente com `new`.

## Os 5 Padrões Criacionais GoF

| Padrão | Problema que resolve |
|---|---|
| [[singleton-pattern]] | Garante uma única instância global |
| [[builder-pattern]] | Constrói objetos complexos passo a passo |
| [[factory-pattern]] | Centraliza lógica de criação, desacopla cliente do tipo concreto |
| Abstract Factory | Cria famílias de objetos relacionados sem especificar classes concretas |
| Prototype | Cria novos objetos clonando um existente |

## Padrão de uso

Todos os padrões criacionais resolvem o mesmo problema central: **o código cliente não deve saber como o objeto é criado**, apenas o que ele faz. Isso permite trocar implementações sem alterar quem usa.

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
