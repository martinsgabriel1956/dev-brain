---
type: concept
title: "Classe Como Conceito de Domínio"
aliases: ["classe não é estrutura de dados", "objeto inválido nunca deve existir", "Produto com preço negativo"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [oop, modelagem-de-dominio, invariante, encapsulamento, java]
skill: tech-mentor-leadership
status: draft
---

# Classe Como Conceito de Domínio

Classes representam **conceitos do negócio**, não meros agregados de campos. Uma `Produto(String nome, double preco, int estoque)` com getters/setters compila, mas permite `setPreco(-30)` e `setEstoque(-30)` — estados que o negócio não aceita; logo o objeto deveria ser impossível de construir. Remédio: proteger invariantes por construtor/métodos que validam ([[wiki/concepts/encapsulamento]], [[wiki/concepts/precondicao-poscondicao-invariante]], [[wiki/concepts/fail-fast]]), tipos de domínio em vez de primitivos ([[wiki/concepts/primitive-obsession]]) e comportamento junto do dado, evitando o [[wiki/concepts/anemic-domain-model]]. Ver [[wiki/concepts/validacao-de-entrada]] para a borda do sistema.

## Key Sources

- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — `Produto` com setters; 'esse objeto nunca deveria existir'
