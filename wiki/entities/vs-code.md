---
type: entity
title: "Visual Studio Code"
aliases: ["VS Code", "VSCode"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [ferramenta, editor, frontend]
skill: tech-mentor-frontend
status: stub
---

# Visual Studio Code

Editor de código da Microsoft.

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], é o editor da demonstração do [[wiki/entities/frontpush|FrontPUSH]] (a aula que configura o editor e os plugins é [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]). Dois recursos aparecem: o Emmet, "plugin nativo" que gera a estrutura do HTML5 e a tag `<link>` por abreviação (`[external]` https://code.visualstudio.com/docs/editor/emmet), e a extensão Live Server, que sobe um servidor local e atualiza o navegador a cada Ctrl+S. Ver [[wiki/concepts/setup-live-reload-debug-testes]].

## Extensões da aula de ambiente do FrontPUSH

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], a aula que configura o editor do curso, [[wiki/entities/nasser|Násser]] recomenda instalar o VS Code por último (depois de Git, Node e Yarn) e lista as extensões: vscode-icons (estética), Thunder Client (testar API, no lugar do Postman), Prettier - Code formatter (formata ao salvar), Live Server ("muitíssimo importante"), Live Sass Compiler ([[wiki/concepts/pre-processador-css]]), HTML Snippets, Color Highlight, Material Theme e One Dark Theme. O tema dele é Community Material Theme, Ocean High Contrast. O Git Bash entra como terminal padrão ([[wiki/concepts/shell-terminal]]).

## Key sources

- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — Emmet e Live Server na aula de básico de CSS
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Git → Node → Yarn → VS Code; lista de extensões; Git Bash como terminal
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: pasta "HTML básico", New File `index.html`, Emmet `html` + opção 5 (`html:5`)
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: Emmet `link:css`; autocompletar de caminho com `./`
