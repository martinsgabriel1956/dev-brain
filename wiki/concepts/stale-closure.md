---
type: concept
title: "Stale Closure"
aliases: ["closure congelada", "closure stale React", "variável desatualizada closure"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, javascript, closure, useEffect, bugs, hooks]
skill: tech-mentor-frontend
status: stable
---

# Stale Closure

Bug onde uma função **captura uma variável de uma renderização antiga** e continua usando aquele valor mesmo depois que o estado mudou.

## Como acontece

Cada renderização do React cria **novas variáveis**. Uma closure captura as variáveis da renderização em que foi criada — não os valores mais recentes.

```typescript
// ❌ Counter nunca passa de 1
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // count está congelado em 0 — sempre seta 0+1=1
    }, 1000);
    return () => clearInterval(id);
  }, []); // [] → closure criada na primeira renderização, nunca recriada

  return <p>{count}</p>;
}
```

O `useEffect` com `[]` é criado uma vez. A closure captura `count = 0` da primeira renderização. Todas as chamadas do `setInterval` leem esse mesmo `0`.

## A solução — updater function

```typescript
// ✅ Updater function — React fornece o valor mais recente
useEffect(() => {
  const id = setInterval(() => {
    setCount(prev => prev + 1); // prev = valor atual no momento da execução
  }, 1000);
  return () => clearInterval(id);
}, []);
```

Com a updater function `prev => prev + 1`, você não lê `count` da closure — pede ao React o valor mais recente no momento da execução.

## Onde stale closure aparece

- `useEffect` com `[]` que acessa estado
- `useCallback` sem a dependência correta
- `setTimeout`/`setInterval` sem cleanup ou updater function
- Event handlers que capturam estado no mount

## Relação com useEffect

O bug de stale closure **só existe porque há um effect**. Se o código não dependesse de `useEffect` para lógica de estado, o problema não existiria — ver [[derived-state]].

## Ver também

- [[useEffect]] — onde stale closure aparece com frequência
- [[useState]] — updater function como solução
- [[useCallback]] — outro local comum de stale closure

## Key Sources

- [[wiki/sources/useeffect-problemas-e-solucoes]]
