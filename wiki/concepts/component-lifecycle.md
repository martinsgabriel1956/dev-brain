---
type: concept
title: "Component Lifecycle (Ciclo de Vida de Componente)"
aliases: ["ciclo de vida do componente", "mount update unmount", "lifecycle hooks"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, lifecycle, react, vue, angular, cleanup, memory-leak]
skill: tech-mentor-frontend
status: stable
---

# Component Lifecycle

Todo componente de UI, independente do framework, passa por três fases universais:

1. **Monta** — aparece na tela pela primeira vez.
2. **Atualiza** — re-renderiza toda vez que estado ou props mudam.
3. **Desmonta** — sai da tela e deixa de existir.

Cada framework expõe uma forma de rodar código em cada fase, com sintaxe própria: hooks de ciclo de vida (`useEffect` no React — ver [[wiki/concepts/useEffect]]), lifecycle hooks (`onMounted`/`onUnmounted` no Vue, `ngOnInit`/`ngOnDestroy` no Angular).

## Por que importa: cleanup na desmontagem

O caso canônico é um componente que abre uma conexão externa ao montar (ex. WebSocket de uma sala de chat) e precisa fechá-la ao desmontar. Sem esse cleanup, cada vez que o componente monta e desmonta sem limpar — por exemplo, o usuário trocando de sala três vezes — deixa conexões, timers ou event listeners acumulando, sem serem liberados. Isso é uma fonte comum de vazamento de memória e de comportamento "fantasma" (código de uma instância antiga ainda reagindo a eventos).

## Ver também

- [[wiki/concepts/useEffect]] — implementação React-específica deste conceito, incluindo array de dependências e função de cleanup

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
