---
type: concept
title: "useState"
aliases: ["use state", "estado local React"]
date_created: 2026-04-22
date_updated: 2026-11-16
source_count: 6
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

## `useState` como cópia local de um estado externo

O padrão de "callback form" (`setValue(prev => ...)`) não é exclusivo de estado interno do componente — o mesmo `typeof value === "function"` é reaproveitado para implementar setters de stores externas ao React (estilo [[wiki/concepts/zustand]]), permitindo que o setter aceite tanto um valor direto quanto uma função atualizadora, igual à API nativa do `useState`. Ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: o contador que só muda no `console.log` com `let`, `const [counter, setCounter] = useState(0)`, "retorna sempre um array", e `useState<Item[]>([])` tipado. Faltou a forma funcional `setCounter(c => c + 1)` para quando o novo valor depende do anterior.

## Na NLW #2, dia 3 (Diego Fernandes)

Os horários "infinitos" do Proffy: `push` não muda a tela, `useState` sem `set` também não, e `setScheduleItems([...scheduleItems, novo])` sim. Cada campo do cadastro e dos filtros vira um estado. A forma funcional (`items => [...items, novo]`) não aparece. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

"Sempre que alguma coisa pode mudar e ela precisa ser manipulada pelo usuário, isso precisa estar no estado": `useState(favorited)` a partir da prop, que só vale na montagem; `useState<number[]>` para os ids; `isFiltersVisible` com toggle `!valor`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/useeffect-problemas-e-solucoes]]
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — `useState` como cópia local sincronizada com uma store externa
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: contador, array [valor, set], estado tipado
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: scheduleItems e campos controlados
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: estado inicial vindo de prop
