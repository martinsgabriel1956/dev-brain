---
type: entity
title: "Create React App"
aliases: ["CRA", "create-react-app", "react-scripts"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [react, build, scaffolding, ferramenta, descontinuado]
skill: tech-mentor-frontend
status: stub
---

# Create React App

Gerador oficial de projetos React (2016–2025), `npx create-react-app web --template typescript`. Escondia webpack, Babel, ESLint e Jest atrás do `react-scripts`.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native|dia 1]] e [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]): gera o projeto web; no dia 3, a limpeza tira favicon, manifest, `serviceWorker`, `setupTests` e logos. A estrutura tem `public/index.html` só com a `div#root` e `src/index.tsx` com o `ReactDOM.render` ([[wiki/concepts/renderizacao-ssr-vs-csr|CSR]]).

**Descontinuado** em fevereiro de 2025. O time do React recomenda um framework (Next.js, React Router) ou um build tool (Vite, Parcel, Rsbuild) `[external]` (https://react.dev/blog/2025/02/14/sunsetting-create-react-app).

Relacionado: [[wiki/entities/react]], [[wiki/entities/typescript]].

## Na NLW #2, dia 1 (Diego Fernandes)

`yarn create react-app web --template typescript`; limpeza de README, CSS, teste, logo, `serviceWorker` (PWA) e `setupTests`; o `react-scripts` com Webpack e Babel. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: criação do projeto com template TypeScript
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: limpeza e estrutura
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: template TypeScript e react-scripts
