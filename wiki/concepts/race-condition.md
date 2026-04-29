---
type: concept
title: "Race Condition"
aliases: ["condição de corrida", "race condition fetch React", "request fora de ordem"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, bug, fetch, async, useEffect, race-condition]
skill: tech-mentor-frontend
status: stable
---

# Race Condition

Bug onde **múltiplos requests assíncronos completam fora de ordem**, fazendo o componente exibir dados incorretos — resposta de um request antigo sobrescreve a de um request mais recente.

## O cenário clássico em React

```typescript
// ❌ Race condition — sem AbortController
useEffect(() => {
  fetchUser(userId).then(data => setUser(data));
}, [userId]);
```

Fluxo do bug:
1. `userId = 1` → request A dispara
2. `userId = 2` → request B dispara
3. Request B responde primeiro → `setUser(userB)` ✅
4. Request A responde depois → `setUser(userA)` ❌ — dados errados na tela

## Os três bugs do fetch em useEffect

```typescript
// ❌ Três bugs: race condition, memory leak, estado inconsistente
useEffect(() => {
  fetchUser(userId).then(setUser); // bug 1: race condition
                                   // bug 2: memory leak se componente desmonta
                                   // bug 3: sem loading, exibe dados do userId anterior
}, [userId]);
```

## Solução com AbortController

```typescript
// ✅ Race condition e memory leak resolvidos
useEffect(() => {
  const controller = new AbortController();

  fetchUser(userId, { signal: controller.signal })
    .then(setUser)
    .catch(err => {
      if (err.name !== "AbortError") setError(err);
    });

  return () => controller.abort(); // cancela request ao trocar userId ou desmontar
}, [userId]);
```

O cleanup do effect cancela o request anterior antes de disparar o novo.

## Solução real — não fazer fetch em useEffect

```typescript
// ✅✅ TanStack Query — race condition, cache, retry, loading, erro: tudo resolvido
const { data: user, isLoading, error } = useQuery({
  queryKey: ["user", userId],
  queryFn: () => fetchUser(userId)
});
```

TanStack Query e SWR existem porque **fetch correto em `useEffect` exige ~30 linhas** e ainda assim é fácil esquecer um caso. Essas bibliotecas resolvem race condition, cache, retry, loading e erro por padrão.

## Quando AbortController ainda é necessário

Em fetch fora de TanStack Query — como em Server Actions ou `fetch` manual em event handlers:

```typescript
function handleSearch(query: string) {
  const controller = new AbortController();
  fetch(`/api/search?q=${query}`, { signal: controller.signal })
    .then(r => r.json())
    .then(setResults);
  return () => controller.abort();
}
```

## Ver também

- [[useEffect]] — onde race condition aparece
- [[tanstack-query]] — solução recomendada para fetch
- [[stale-closure]] — outro bug comum em useEffect

## Key Sources

- [[wiki/sources/useeffect-problemas-e-solucoes]]
