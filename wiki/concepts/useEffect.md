---
type: concept
title: "useEffect"
aliases: ["use effect", "efeitos React", "side effects React"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 2
tags: [react, hooks, efeitos, side-effects, useEffect]
skill: tech-mentor-frontend
status: stable
---

# useEffect

Hook para **sincronizar o componente com sistemas externos** — APIs, DOM, timers, WebSockets, subscriptions. Não é para lógica de negócio.

## Assinatura

```typescript
useEffect(() => {
  // efeito
  return () => { /* cleanup */ };
}, [dependências]);
```

## Array de dependências

| Configuração | Quando executa |
|---|---|
| `[]` | Só no mount |
| `[dep1, dep2]` | No mount e quando dep1 ou dep2 mudar |
| Sem array | Em todo render |

**⚠️ Nunca ignore os warnings de dependências** — o ESLint/linter está certo.

## Cleanup obrigatório

Todo efeito que abre uma conexão, registra um listener ou inicia um timer precisa de cleanup para evitar memory leak e bugs no Strict Mode (double invocation).

```typescript
// ✅ Fetch com AbortController
useEffect(() => {
  const controller = new AbortController();
  fetchUser(userId, { signal: controller.signal }).then(setUser);
  return () => controller.abort();
}, [userId]);

// ✅ Event listener
useEffect(() => {
  window.addEventListener("resize", handleResize);
  return () => window.removeEventListener("resize", handleResize);
}, []);
```

## Strict Mode e double invocation

Em desenvolvimento, React monta → desmonta → monta novamente para detectar side effects sem cleanup. Se seu efeito quebrar, falta cleanup.

## Quando NÃO usar useEffect

- Transformar dados para render → calcule direto no body do componente
- Reagir a evento do usuário → use o handler do evento
- Buscar dados em Next.js → use Server Components ou TanStack Query

## Anti-padrões comuns

### 1. Sincronizar estado derivado (mais comum)
Usar `useEffect` para setar `filteredItems` quando `items` muda gera **3+ renderizações em cadeia** e deixa o componente em estado inconsistente entre elas. Solução: calcular na renderização — ver [[derived-state]].

### 2. Stale closure em timers/counters
`useEffect` com `[]` congela variáveis da primeira renderização. Solução: updater function `setCount(prev => prev + 1)` — ver [[stale-closure]].

### 3. Fetch sem AbortController
Race condition + memory leak. Solução: `AbortController` no cleanup, ou melhor ainda: [[tanstack-query]] — ver [[race-condition]].

## Regra de ouro

> "O melhor effect é o que você deleta."

```
Se dá para calcular → calcule na renderização
Se é fetch         → use TanStack Query / SWR
Se é efeito externo ao React → aí sim use useEffect
```

## `useEffect` como implementação React do ciclo de vida

`useEffect` é a forma específica do React de expor as três fases universais de [[wiki/concepts/component-lifecycle]] (montar/atualizar/desmontar) — outros frameworks usam sintaxe própria para o mesmo conceito (`onMounted`/`onUnmounted` no Vue, `ngOnInit`/`ngOnDestroy` no Angular). O exemplo canônico de por que o cleanup (função de retorno do effect) importa: um componente que abre uma conexão WebSocket ao montar precisa fechá-la ao desmontar, ou conexões vão se acumulando a cada nova montagem.

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/useeffect-problemas-e-solucoes]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
