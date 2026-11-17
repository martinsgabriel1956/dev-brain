---
type: concept
title: "JSX"
aliases: ["JavaScript XML", "React markup"]
date_created: 2026-04-22
date_updated: 2026-11-17
source_count: 8
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

## Na NLW #2, dia 1 (Diego Fernandes)

JSX é "JavaScript mais XML" e TSX, "TypeScript com XML". Chaves inserem variáveis (`src={logoImg}`); `className` e `htmlFor` porque `class` e `for` são reservadas. O `import React` era obrigatório em 2020 e deixou de ser com o JSX transform do React 17. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 4 (Diego Fernandes)

No RN, `{'\n'}` no lugar de `<br>`, `{' '}` para espaço, fragment `<>...</>` para não criar view a mais e "text strings must be rendered within a text component" para texto solto. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: "função que retorna HTML"; JSX e bundler
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: JSX x createElement; className e htmlFor
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: JSX sem HTML no React Native
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: JSX/TSX, chaves, className e htmlFor
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: quebra de linha, espaço e fragment no RN
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: "não é HTML, é um negócio que parece com HTML"; compilado no build
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: JSX → React.createElement no REPL; maiúscula muda o tipo, `class` é `className`, nova transformação do React 17
