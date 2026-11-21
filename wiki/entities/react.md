---
type: entity
title: "React"
aliases: ["ReactJS", "React.js"]
date_created: 2026-04-22
date_updated: 2026-11-21
source_count: 28
tags: [react, frontend, biblioteca, facebook, meta]
skill: tech-mentor-frontend
status: stable
---

# React

Biblioteca JavaScript para construção de interfaces de usuário. Criada pelo Facebook (Meta) em 2013. Não é um framework — não inclui roteamento, estado global ou fetch por padrão.

## Modelo Mental

**UI = f(state)** — dado o mesmo estado, o output é sempre o mesmo JSX. Isso torna a UI previsível e testável.

## Versões Relevantes

- **React 16.8** — introduziu Hooks (`useState`, `useEffect`, etc.)
- **React 18** — Concurrent Mode, `useTransition`, `useDeferredValue`, `useSyncExternalStore`
- **React 19** — `use()` hook, `useActionState`, React Compiler (beta), Server Actions aprimorados

## Ecossistema Principal

| Necessidade | Solução |
|---|---|
| Roteamento web | React Router / Next.js App Router |
| Estado global | [[wiki/concepts/zustand|Zustand]], Jotai, Redux Toolkit |
| Server state | [[tanstack-query]], SWR |
| Formulários | React Hook Form + Zod |
| Metaframeworks | Next.js, Remix, Astro |
| Testes | React Testing Library + Vitest |

## Mecanismos Internos (Genéricos a Frameworks de UI)

React usa [[wiki/concepts/virtual-dom]] + [[wiki/concepts/reconciliacao]] como estratégia de reatividade e [[wiki/concepts/batching]] para agrupar atualizações de estado — em contraste com frameworks baseados em [[wiki/concepts/signals]] (Solid.js, Svelte). Compartilha com Vue e Angular a necessidade de resolver os mesmos dez problemas estruturais: gerenciamento de estado (evitar prop drilling — ver [[wiki/concepts/context-api]]), [[wiki/concepts/component-lifecycle]], compilação (JSX → JS), [[wiki/concepts/client-side-routing]], [[wiki/concepts/hydration]] em SSR, e otimização de bundle via [[wiki/concepts/tree-shaking]] + [[wiki/concepts/code-splitting]].

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o React é "uma biblioteca para construção de interfaces" para [[wiki/concepts/single-page-application|SPAs]], com o pacote `react` compartilhado com o [[wiki/entities/react-native]] e [[wiki/concepts/componentizacao]] como primeira vantagem. O projeto sai do `create-react-app --template typescript`, descontinuado em fevereiro de 2025 `[external]` (https://react.dev/blog/2025/02/14/sunsetting-create-react-app).

No dia 3 da NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), o front-end do Ecoleta mostra os fundamentos de 2020: JSX, componentes, props com `React.FC`, `useState`, `useEffect` e `ReactDOM.render`. Para Diego, "se você entendeu componente, propriedade e estado [...] acabou". Várias dessas APIs mudaram: o `import React` deixou de ser obrigatório (React 17), `createRoot` (18) e `React.FC` em desuso.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o mesmo modelo de componentes, props, estado e efeitos roda no React Native; Diego até copia o `handleSelectItem` da web. O fragment `<>...</>` aparece para retornar dois irmãos sem elemento extra.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: componente `Dropzone` com `react-dropzone`, preview por `URL.createObjectURL`, função como prop para subir o arquivo ao pai e `useCallback`.

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], o React é o "framework" para o qual o módulo de JavaScript do FrontPUSH prepara: "pelo menos um basicinho" de JS antes, "para você não se sentir completamente perdido".

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], o React aparece como o lugar onde "é muito comum a gente sempre estar batendo na tecla em Arrow functions". A razão de fundo, o `this` léxico, não é dita ([[wiki/concepts/arrow-functions]]).

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], a diferença `forEach` × `map` é a que importa para renderizar listas no React: só o `map` devolve o array de elementos para o JSX ([[wiki/concepts/metodos-de-array-javascript]]).

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], o React é a motivação para criar HTML pelo JavaScript: "é o próprio JavaScript que renderiza o HTML, é o próprio JavaScript que renderiza o CSS". O CSS não é renderizado pelo React; vem de arquivos importados ou CSS-in-JS.

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], o [[wiki/entities/frontpush|FrontPUSH]] ensina desestruturação como preparo para o React. Os usos que vêm lá: `function Card({ title })` nas props e `const [count, setCount] = useState(0)`.

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
- [[wiki/sources/underengineering-overengineering-mario-souto]] — React Hook Form citado como exemplo de lib madura a preferir em vez de construir gerenciamento de formulário do zero, evitando [[wiki/concepts/under-engineering]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]] — dez mecanismos internos genéricos a frameworks de UI, com React como exemplo citado
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — recriação didática do mecanismo central do [[wiki/concepts/zustand|Zustand]] (Observer + `useState`/`useEffect`) sem `Provider`
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]] — demonstração prática no React DevTools Profiler de `React.memo`, `useMemo`, `useCallback` e do fluxo de reconciliação

## Key sources (adição 2026-10-14)
- [[wiki/sources/historia-do-front-end-akita-ep4]] — surge do Facebook como evolução das SPAs; Virtual DOM; React Native ([[wiki/concepts/single-page-application]], [[wiki/concepts/aplicativo-hibrido]])

## Na NLW #2, dia 1 (Diego Fernandes)

"Uma biblioteca de construção de interfaces que visa a construção de single page applications." O pacote `react` é o núcleo, e `react-dom`/React Native são renderizadores; Diego cita React TV, React VR e o React Native Windows/macOS da Microsoft. Conceitos do dia: componentes, JSX e props; estado fica para depois. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

Dia 3 da NLW #2: interface declarativa ("a gente não vai no HTML [...] e adiciona uma nova div", como no jQuery), `useState`, `useEffect`, componentes de formulário com `HTMLAttributes` e o front ligado à API. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], React é exemplo de aplicação web que "necessita de um build" e "de um banco de dados, de um MySQL". Precisões: o build gera arquivos estáticos que qualquer host serve; `localhost:3000` é o servidor de desenvolvimento; banco é assunto do back-end.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: "você vai ter que buildar todo o ecossistema do React no servidor" e "para fazer uma rota em React, eu tenho que configurar todo um ecossistema". O build roda local ou no CI e sobe como estático; rotas pedem React Router e redirect para `index.html`.

## Key sources (adição 2026-11-10)

- [[wiki/sources/lazy-load-eager-load-economia-dados-react-trpc]] — renderização condicional como mecanismo de [[wiki/concepts/lazy-vs-eager-loading]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: o React é o motivo para instalar Node e Yarn no curso; sem biblioteca, só um editor
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: biblioteca x framework, SPA, componentização, create-react-app com TypeScript
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: componentes, props, estado e efeitos no Ecoleta web
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: mesmos conceitos no mobile; fragment
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: Dropzone e comunicação filho → pai
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: núcleo × renderizadores; componentes e props
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: estado, efeitos e o front conectado
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: JS básico antes do React
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: arrow functions comuns no React
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: map × forEach, base das listas no JSX
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: React como "tudo JavaScript"
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: desestruturação como preparo para React
- [[wiki/sources/frontpush-intro-modulo-reactjs]]: FrontPUSH, React aula 01: abertura do módulo, "módulo de biblioteca JavaScript", JS ES6+ como pré-requisito
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: o que saber de JS antes; distinguir o que é JavaScript e o que é React
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: Facebook, interface dinâmica, React.js (biblioteca) × React (ecossistema, framework), SPA, Virtual DOM, JSX
- [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]: FrontPUSH, React aula 04: por que usar React: método tradicional (PHP, HTML no servidor) × método SPA (JSON)
- [[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]: FrontPUSH, React aula 05: App.js com header, sidebar, content e footer; "encapsulados que gerenciam seu próprio estado"
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: React.createElement × JSX no REPL do Babel; inicial maiúscula
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: React como "aplicação web" (ressalvas)
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: "buildar no servidor" (ressalva)
