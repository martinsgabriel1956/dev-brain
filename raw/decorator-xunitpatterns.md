---
title: "Decorator"
author: "Gerard Meszaros"
source_url: "http://xunitpatterns.com/Decorator.html"
date_published: 2011-02-09
date_ingested: 2026-09-04
note: "Tradução para PT-BR do verbete original (entrada curta de padrão externo no catálogo xUnit Patterns, categoria 'External Patterns'). Para o texto exato em inglês, consultar a source_url."
---

# Decorator

> Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente.

**Um objeto que é posicionado entre um cliente e outro objeto com o propósito de adicionar comportamento.**

> Anexe responsabilidades adicionais a um objeto dinamicamente. Decorators oferecem uma alternativa flexível à subclasse para estender funcionalidade.

Um *Decorator* implementa a mesma interface do objeto decorado e adiciona comportamento antes ou depois de chamar, no objeto decorado, o mesmo método que foi chamado nele mesmo.

De [GOF] (Gang of Four, *Design Patterns: Elements of Reusable Object-Oriented Software*).

## Metadados do artigo

- Entrada curta do catálogo de "External Patterns" (padrões externos, originados de outras fontes como o GOF) do site xUnitPatterns.com, de Gerard Meszaros (autor do livro *xUnit Test Patterns: Refactoring Test Code*).
- Página gerada originalmente em 09/02/2011.
- Tema central: o Decorator é catalogado como um padrão de design clássico (GOF) referenciado no contexto de xUnit Patterns, tipicamente relevante para a construção de **Test Doubles** que envolvem (wrap) um objeto real adicionando comportamento de verificação/registro antes ou depois de delegar a chamada.
- Contexto: parte da taxonomia de padrões de teste (xUnit Patterns) de Meszaros, que referencia padrões de design gerais (não exclusivos de teste) quando eles são usados como técnica de implementação de padrões de teste — por exemplo, um **Test Spy** ou **Mock Object** frequentemente é implementado como um Decorator em torno de um **Depended-On Component** real.
