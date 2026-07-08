---
type: concept
title: "useState"
aliases: ["use state", "estado local React"]
date_created: 2026-04-22
date_updated: 2026-07-07
source_count: 2
tags: [react, hooks, estado, useState]
skill: tech-mentor-frontend
status: stable
---

# useState

Hook que adiciona **memória local** a um componente funcional. Quando o estado muda, o componente re-renderiza.

## Uso básico

```typescript
const [value, setValue] = useState<string>("");
```

## Regra crítica — callback form

Sempre use callback quando o novo valor depende do anterior. Sem isso, em Concurrent Mode o closure pode capturar um valor stale.

```typescript
// ✅ Correto
setCount(prev => prev + 1);

// ❌ Stale closure
setCount(count + 1);
```

## Estado com objeto

```typescript
const [form, setForm] = useState({ name: "", email: "" });

// Ao atualizar, sempre espalhar o estado anterior
function handleNameChange(name: string) {
  setForm(prev => ({ ...prev, name }));
}
```

## Lazy initialization

Use quando o valor inicial é caro de calcular — a função só roda uma vez:

```typescript
const [data, setData] = useState(() => JSON.parse(localStorage.getItem("data") ?? "[]"));
```

## Quando migrar para `useReducer`

Quando há mais de 2-3 estados relacionados que mudam juntos → ver [[useReducer]].

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/useeffect-problemas-e-solucoes]]
