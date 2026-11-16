---
type: entity
title: "React Router"
aliases: ["react-router-dom", "React Router DOM", "BrowserRouter"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [react, roteamento, spa, biblioteca]
skill: tech-mentor-frontend
status: stub
---

# React Router

Biblioteca de roteamento do [[wiki/entities/react]]: liga URLs a componentes e troca de tela sem recarregar a página ([[wiki/concepts/client-side-routing]], [[wiki/concepts/single-page-application]]).

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), na versão 5:

- `<BrowserRouter>` usa caminhos "normais" (`/create-point`), via History API. Há também `HashRouter`, `MemoryRouter` e `StaticRouter`.
- `<Route component={Home} path="/" exact />`: sem `exact`, a regra é "começa com", e `/create-point` cairia na Home.
- `<Link to="/create-point">` no lugar de `<a href>`, e a aba Network prova que nada recarrega.
- `useHistory().push('/')` navega depois do submit.

**Depois de 2020** `[external]` (https://reactrouter.com/6.30.0/upgrading/v5):

- O **v6** trouxe `<Routes>`, `element={<Home />}` e correspondência exata por padrão (o `exact` sumiu), e trocou o `useHistory` pelo `useNavigate`.
- `[skill: tech-mentor-frontend]` No **v7**, o React Router absorveu o Remix v2: modos library, data e framework, com loaders e actions.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], Diego compara o `NavigationContainer` do React Navigation ao `BrowserRouter`. No mobile as telas têm nome, não URL.

## Na NLW #2, dia 1 (Diego Fernandes)

v5 no Proffy: `BrowserRouter`, `Route path exact component`, `Link to`, e a aba Network mostrando que o `Link` não recarrega a página. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`useHistory().push('/')` depois do cadastro, para redirecionar "depois que alguma ação acontece", e não por clique (que é o `Link`). No v6 virou `useNavigate`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: BrowserRouter, Route exact, Link, useHistory
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: comparação com o React Navigation
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: rotas /, /study e /give-classes
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: useHistory no cadastro de aula
