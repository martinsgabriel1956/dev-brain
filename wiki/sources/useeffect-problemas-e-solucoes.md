---
type: source
title: "useEffect — Problemas, Armadilhas e Soluções"
aliases: ["useeffect anti-patterns", "derived state react", "race condition fetch"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/useeffect-problemas-e-solucoes.md
source_url: ""
author: "Transcrição de vídeo (speaker não identificado)"
date_published: 2026-04-22
date_ingested: 2026-04-22
source_count: 0
tags: [react, useEffect, hooks, derived-state, race-condition, stale-closure, performance]
skill: tech-mentor-frontend
status: stable
---

# useEffect — Problemas, Armadilhas e Soluções

## TL;DR

Transcrição de vídeo sobre os três principais anti-padrões do `useEffect`: (1) usar effect para sincronizar estado derivado em vez de calcular na renderização, (2) stale closure em contadores/timers, (3) fetch de dados com race condition e memory leak. Para cada problema, apresenta a solução correta.

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Usar `useEffect` para sincronizar estado derivado causa 3+ renderizações em cadeia | Cada effect que faz `setState` dispara nova renderização | Alta |
| Entre renderizações encadeadas por effects, o componente fica em estado inconsistente | `items` já mudou mas `total` ainda é o valor antigo | Alta |
| Filtrar 1000 itens na renderização leva < 1ms — o overhead de effects encadeados é maior | Dado empírico de performance | Alta |
| `useEffect` com `[]` congela variáveis da primeira renderização (stale closure) | Closure captura variáveis, não valores — cada render cria novas variáveis | Alta |
| Fetch em `useEffect` sem `AbortController` tem race condition + memory leak | Resposta de request anterior pode sobrescrever a mais recente | Alta |
| TanStack Query / SWR existem especificamente porque fetch correto em effect tem ~30 linhas | Race condition, cache, retry, loading, erro — tudo manual em effect | Alta |

---

## Conceitos Abordados

- [[derived-state]]
- [[stale-closure]]
- [[race-condition]]

## Conceitos Relacionados (wiki existente)

- [[useEffect]] — página central, atualizada com backlink e anti-padrões desta source
- [[useState]] — relação com estado derivado
- [[useMemo]] — solução para cálculos pesados na renderização
- [[tanstack-query]] — solução para fetch sem useEffect

---

## Os Três Anti-padrões

### 1. Estado derivado em useEffect (mais comum)

```typescript
// ❌ 3 renderizações, estado inconsistente entre elas
const [items, setItems] = useState([]);
const [filtered, setFiltered] = useState([]);
const [total, setTotal] = useState(0);

useEffect(() => { setFiltered(items.filter(...)); }, [items]);
useEffect(() => { setTotal(filtered.length); }, [filtered]);

// ✅ 1 renderização, impossível ficar inconsistente
const [items, setItems] = useState([]);
const filtered = items.filter(...);   // valor derivado
const total = filtered.length;        // valor derivado
```

### 2. Stale closure em counter

```typescript
// ❌ Nunca passa de 1 — count congelado em 0 na closure
useEffect(() => {
  const id = setInterval(() => setCount(count + 1), 1000);
  return () => clearInterval(id);
}, []);

// ✅ Updater function — React fornece o valor mais recente
useEffect(() => {
  const id = setInterval(() => setCount(prev => prev + 1), 1000);
  return () => clearInterval(id);
}, []);
```

### 3. Fetch sem AbortController

```typescript
// ❌ Race condition + memory leak
useEffect(() => {
  fetchUser(userId).then(setUser);
}, [userId]);

// ✅ AbortController no cleanup
useEffect(() => {
  const controller = new AbortController();
  fetchUser(userId, { signal: controller.signal }).then(setUser);
  return () => controller.abort();
}, [userId]);

// ✅✅ Melhor ainda — sem useEffect para fetch
const { data: user } = useQuery({ queryKey: ['user', userId], queryFn: () => fetchUser(userId) });
```

---

## Usos Legítimos do useEffect

- Event listeners no `window`/`document`
- Subscriptions a WebSockets
- Integração com libs que manipulam o DOM diretamente
- Timers e intervalos com cleanup
- Analytics / logging

---

## Regra de ouro da source

> "O melhor effect é o que você deleta."

```
Se dá para calcular → calcula na renderização (não use useEffect)
Se é fetch de dados → use TanStack Query / SWR
Se é efeito colateral externo ao React → aí sim use useEffect
```

---

## Questões Abertas

- Existe caso legítimo de effect encadeado (effect A dispara effect B) que não pode ser colapsado em cálculo direto?
- Qual o limite de complexidade de cálculo na renderização antes de ser obrigatório usar `useMemo`?
