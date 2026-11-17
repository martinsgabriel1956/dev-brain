---
type: concept
title: "Bundler (Webpack, Vite, esbuild, Rollup)"
aliases: ["module bundler", "empacotador", "Webpack", "Vite", "empacotamento de módulos"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 1
tags: [frontend, build, webpack, vite, esbuild, rollup, modulos, tooling]
skill: tech-mentor-frontend
status: stub
---

# Bundler

Ferramenta de build que parte de um arquivo de entrada, segue os `import` e junta os módulos num ou em poucos arquivos que o navegador carrega. Também transforma o que não é JavaScript em algo que o JS consegue importar (CSS, imagens, fontes, JSON) e serve a aplicação em desenvolvimento com recarregamento automático. `[skill: tech-mentor-frontend]`

- **Bundler × transpilador:** o bundler empacota e resolve módulos; o [[wiki/concepts/transpilador]] (Babel, SWC, esbuild) reescreve sintaxe. O Webpack chama o Babel por um *loader* (`babel-loader`); no Vite, o esbuild e o Rollup/Rolldown fazem os dois papéis.
- **Webpack** (2012): configuração por loaders e plugins; padrão do create-react-app ([[wiki/entities/create-react-app]]). Ainda é base de muito código; o Rspack o reimplementa em Rust.
- **Vite:** usa ES Modules nativos no dev server (sem empacotar em desenvolvimento) e empacota só no build. Padrão para projetos React novos sem framework.
- **Dev server:** live reload (recarrega a página) ou HMR/Fast Refresh (troca o módulo sem perder o estado) ([[wiki/concepts/setup-live-reload-debug-testes]]).
- Otimizações do build: [[wiki/concepts/tree-shaking]], [[wiki/concepts/code-splitting]], minificação ([[wiki/concepts/pipeline-de-assets]]).

## No FrontPUSH

Em [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]], [[wiki/entities/nasser]] resume o Webpack como o que "ensina ao JavaScript como importar arquivos, CSS, imagens e etc." e faz o Live Reload, ao lado do Babel, que transpila. O curso não configura nenhum dos dois: usa o create-react-app.

## Related

- [[wiki/concepts/transpilador]]
- [[wiki/concepts/pipeline-de-assets]]
- [[wiki/concepts/modulos-nodejs]]
- [[wiki/concepts/tree-shaking]]
- [[wiki/concepts/code-splitting]]

## Key Sources

- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: o Webpack ao lado do Babel
