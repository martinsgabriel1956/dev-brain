---
type: concept
title: "JSX"
aliases: ["JavaScript XML", "React markup"]
date_created: 2026-04-22
date_updated: 2026-11-16
source_count: 4
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], o componente React é "uma função que retorna o HTML". O "HTML" é JSX, e o import de CSS e imagens no mesmo arquivo é obra do bundler.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], JSX é "a possibilidade de nós escrevermos HTML diretamente dentro do JavaScript", comparado ao `React.createElement` aninhado. O arquivo precisa ser `.tsx`, e `className`/`htmlFor` substituem `class`/`for`. Precisão: JSX tem sintaxe parecida com XML, mas não é HTML, e HTML não é XML.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o JSX do React Native usa `View`, `Text` e `Image` no lugar das tags HTML, e todo texto precisa estar em `<Text>` ("Text strings must be rendered within a `<Text>` component").

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: "função que retorna HTML"; JSX e bundler
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: JSX x createElement; className e htmlFor
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: JSX sem HTML no React Native
