---
type: concept
title: "DOM — Document Object Model"
aliases: ["Document Object Model"]
date_created: 2026-07-28
date_updated: 2026-08-03
source_count: 2
tags: [browser, dom, html-parsing, rendering-pipeline, frontend-frameworks]
skill: tech-mentor-frontend
status: draft
---
# DOM — Document Object Model

Árvore de nós que representa a estrutura do HTML: cada tag vira um nó, cada texto vira um nó, cada atributo fica acessível. É construída pelo parser de HTML em etapas: bytes → caracteres (decodificados via a codificação declarada, geralmente UTF-8) → tokens (tags de abertura/fechamento, atributos, texto) → nós → árvore, organizada pela hierarquia de abertura/fechamento das tags.

**Parsing incremental**: o parser não espera o documento inteiro chegar — constrói o DOM conforme os bytes chegam pela rede. É por isso que páginas grandes renderizam de cima para baixo.

**Tolerância a erros**: o parser de HTML nunca falha. Tags não fechadas são fechadas automaticamente; elementos mal aninhados (ex. `<div>` dentro de `<p>`) são reorganizados segundo o algoritmo de parsing do HTML5.

**Limitação**: o DOM sozinho não sabe aparência — cor, tamanho, posição. Isso vem do [[wiki/concepts/cssom]], que é combinado com o DOM para formar a [[wiki/concepts/render-tree]]. Ver o pipeline completo em [[wiki/concepts/critical-rendering-path]].

## Por que os frameworks de UI existem: o custo de tocar o DOM

Cada mutação de DOM tem custo real — o navegador pode precisar recalcular estilos, recalcular layout ([[wiki/concepts/reflow-layout]]) e repintar pixels. Uma mudança isolada é barata; várias em sequência descontrolada deixam o navegador lento. Essa é a motivação declarada por trás de praticamente todo mecanismo interno de React/Vue/Angular: [[wiki/concepts/virtual-dom]] e [[wiki/concepts/signals]] existem para decidir *o que* mudou sem recalcular tudo, [[wiki/concepts/reconciliacao]] decide *como* aplicar a mudança mínima necessária, e [[wiki/concepts/batching]] agrupa várias mudanças de estado numa única passada de DOM em vez de uma por mudança.

## Ver também

- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/hydration]] — como o DOM gerado no servidor é conectado a comportamento no cliente

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
