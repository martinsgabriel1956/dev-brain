---
type: concept
title: "JavaDoc / API Reference"
aliases: ["javadoc", "api reference de linguagem", "documentação de classes e métodos"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [java, documentacao, aprendizado, ide]
skill: tech-mentor-leadership
status: stub
---

# JavaDoc / API Reference

Camada de documentação mais próxima do código, uma etapa além do [[wiki/concepts/padrao-de-secoes-de-documentacao-tecnica|getting started/tutorial]]: documenta cada classe e método com precisão. No caso do Java, é o **JavaDoc** (ex.: `docs.oracle.com` para a versão 25); em outras linguagens o formato muda de nome, mas o papel é o mesmo.

## O que uma entrada de API reference expõe

- **Hierarquia** — de quem a classe herda e quais interfaces implementa (ex.: `String` herda de `Object`, implementa `Comparable` e `Serializable` — o que já diz, sem ler tutorial nenhum, que uma `String` pode ser serializada e comparada)
- **Construtores**, incluindo marcação de **deprecated** quando existe alternativa melhor em versão mais nova
- **Assinatura e tipo de retorno de cada método** (ex.: `contains` retorna `boolean`; `charAt` retorna `char` e documenta o comportamento exato — "o valor do caractere no índice especificado")

## Navegação via IDE

A mesma documentação aparece embutida na IDE ao passar o mouse sobre um método. Ctrl+clique (JetBrains) vai além: abre a implementação real do método, permitindo auditar como ele funciona por dentro — por exemplo, descobrir que `String.contains` usa `indexOf` internamente. A IDE pode inclusive sugerir a alternativa "mais direta" (`indexOf(...) >= 0`), evidenciando que múltiplos métodos públicos podem expor o mesmo mecanismo interno.

Navegar da API reference até a implementação real é uma forma de [[wiki/concepts/ler-codigo-de-terceiros]] aplicada à própria standard library da linguagem.

## Ver Também

- [[wiki/concepts/padrao-de-secoes-de-documentacao-tecnica]] — onde a API reference se encaixa no padrão geral de documentação
- [[wiki/concepts/associacao-lexical-documentacao]] — técnica para encontrar o método certo dentro da API reference
- [[wiki/concepts/documentacao-api-swagger]] — API reference aplicada a APIs HTTP (Swagger/OpenAPI) em vez de bibliotecas/linguagens

## Key Sources

- [[wiki/sources/como-ler-documentacao-de-uma-linguagem-de-programacao]]
