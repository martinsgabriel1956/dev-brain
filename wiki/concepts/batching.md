---
type: concept
title: "Batching (Agrupamento de Atualizações)"
aliases: ["batch updates", "automatic batching", "agrupamento de renders"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, react, batching, performance, renderizacao]
skill: tech-mentor-frontend
status: stable
---

# Batching

Mecanismo pelo qual um framework agrupa múltiplas mudanças de estado disparadas no mesmo evento/handler numa única atualização de [[wiki/concepts/dom]], em vez de re-renderizar uma vez para cada mudança.

## Por que existe

Um handler de clique que muda três estados diferentes (nome, e-mail, endereço) causaria três renders separados sem batching — cada um tocando o DOM. Com batching, o framework coleta as mudanças numa fila e processa tudo junto, aplicando o resultado final ao DOM de uma vez só.

## Consequência que pega desenvolvedores

Se o código muda um estado e tenta ler o DOM (ou o próprio valor do estado, em closures antigas) imediatamente em seguida, o valor lido ainda é o antigo — a atualização só é aplicada depois que o framework processa a fila de batching. Esse é um caso específico da classe mais geral de bugs por [[wiki/concepts/stale-closure|stale closure]].

## Ver também

- [[wiki/concepts/reconciliacao]] — o que acontece depois que o batching decide "agora sim atualiza"
- [[wiki/concepts/stale-closure]] — closures capturando valores desatualizados

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
