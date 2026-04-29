---
type: concept
title: "JSX"
aliases: ["JavaScript XML", "React markup"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, jsx, sintaxe, compilador]
skill: tech-mentor-frontend
status: stable
---

# JSX

Extensão de sintaxe do JavaScript que se parece com HTML. Compilado por Babel/TypeScript para chamadas `React.createElement(...)`.

## Como funciona

```typescript
// JSX escrito pelo dev
const el = <h1 className="title">Olá</h1>;

// O que o compilador gera
const el = React.createElement("h1", { className: "title" }, "Olá");
```

## Diferenças do HTML

| HTML | JSX |
|---|---|
| `class` | `className` |
| `for` | `htmlFor` |
| Atributos em kebab-case | Atributos em camelCase |
| Sem raiz obrigatória | Precisa de uma raiz única |

Use `<>...</>` (Fragment) quando não quiser adicionar nó extra ao DOM.

## Expressões JS

Qualquer expressão JS válida pode ser usada dentro de `{}`:

```typescript
<p>{isLoggedIn ? "Bem-vindo" : "Faça login"}</p>
<ul>{items.map(i => <li key={i.id}>{i.name}</li>)}</ul>
```

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
