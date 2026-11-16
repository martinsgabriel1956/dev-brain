---
type: entity
title: "Visual Studio Code"
aliases: ["VS Code", "VSCode"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 19
tags: [ferramenta, editor, frontend]
skill: tech-mentor-frontend
status: stub
---

# Visual Studio Code

Editor de código da Microsoft.

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], é o editor da demonstração do [[wiki/entities/frontpush|FrontPUSH]] (a aula que configura o editor e os plugins é [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]). Dois recursos aparecem: o Emmet, "plugin nativo" que gera a estrutura do HTML5 e a tag `<link>` por abreviação (`[external]` https://code.visualstudio.com/docs/editor/emmet), e a extensão Live Server, que sobe um servidor local e atualiza o navegador a cada Ctrl+S. Ver [[wiki/concepts/setup-live-reload-debug-testes]].

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] instala o VS Code, um tema ("Launch Base Theme", nome dito assim) e o Live Server, que abre a página em 127.0.0.1:5500 e recarrega a cada Ctrl+S. O Emmet completa tags, gera a estrutura com `!` e expande `#page-home` em `<div id="page-home">`; o hover sobre um seletor mostra o HTML que ele atinge.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa mais abreviações do Emmet: `.field` cria uma `div` com a classe, `*2` multiplica, `label+input` cria irmãos e `mr` vira `margin-right`. A linha guia de indentação mostra onde uma tag fecha, para não apagar só a abertura. Ctrl+/ comenta a linha.

## Extensões da aula de ambiente do FrontPUSH

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], a aula que configura o editor do curso, [[wiki/entities/nasser|Násser]] recomenda instalar o VS Code por último (depois de Git, Node e Yarn) e lista as extensões: vscode-icons (estética), Thunder Client (testar API, no lugar do Postman), Prettier - Code formatter (formata ao salvar), Live Server ("muitíssimo importante"), Live Sass Compiler ([[wiki/concepts/pre-processador-css]]), HTML Snippets, Color Highlight, Material Theme e One Dark Theme. O tema dele é Community Material Theme, Ocean High Contrast. O Git Bash entra como terminal padrão ([[wiki/concepts/shell-terminal]]).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa Ctrl+D para editar a próxima ocorrência ao mesmo tempo, o localizar e substituir (Ctrl+F) para renomear `page-create-point` → `page-search-results` e desliga o minimapa na revisão final.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] configura o Git Bash como "Select Default Shell" do terminal integrado (Ctrl+crase abre e fecha). Para o [[wiki/entities/nunjucks]], instala a extensão Nunjucks Template e mexe no `settings.json`:
- `files.associations` com `*.html` lido como `njk`;
- `emmet.includeLanguages` com `njk` lido como `html`, para devolver o Emmet;
- a extensão vscode-icons, para os ícones.

Usa ainda Format Document para indentar e Reveal in File Explorer.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]): tema Omni (derivado do Dracula), Material Icon Theme, `code .` via "Install Code Command in Path" e o IntelliSense como argumento a favor do [[wiki/entities/typescript]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: a extensão SQLite (Open Database, SQLite Explorer, Show Table, Run Query), o terminal dividido, `material-icon-theme.folders.associations` e o atalho Copy Line Down.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Emmet habilitado em JSX (`emmet.includeLanguages`, `javascript: javascriptreact`) e a fonte FiraCode com ligaduras.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: Ctrl+D, *Add Cursors to Line Ends* (Shift+Alt+I) e Shift+Ctrl+→ para gerar os `data.append(...)` em lote ("umas 46 hotkeys").

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] esconde status bar e minimap, instala o tema dito "launch base" e o Live Server, e mostra o Emmet (`!` + Enter, `img` + Enter com `src` e `alt`), o word wrap com Alt+Z, Ctrl+/ para comentar, a documentação ao passar o mouse e o seletor de cor que troca hexadecimal, RGB e HSL. Para os atalhos de cada sistema: Ctrl+Shift+P → Keyboard Shortcuts. A pasta tem de ser aberta por Open Folder, senão "Open with Live Server" não aparece.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: Emmet com classe (`.logo-container` + Tab, `p.total-connections`), Ctrl+D para selecionar a próxima ocorrência, Alt + clique para vários cursores, Ctrl+F e Alt+Z. O editor acusa o ponto e vírgula esquecido, mas na linha seguinte: "ele não soube interpretar que o erro, na verdade, estava aqui".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: Ctrl+P abre qualquer arquivo pelo nome, clique + Shift + clique seleciona um bloco inteiro e Ctrl+D troca `study` por `give-classes` de uma vez. O Emmet completa `small` + Enter.

## Sass no FrontPUSH

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o VS Code é a forma principal de compilar Sass no curso: extensão [[wiki/entities/live-sass-compiler]] ("tudo no próprio Visual Studio [...] sem utilizar aplicativos externos"), com o Live Server para recarregar.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o terminal integrado passa a usar o Git Bash (Select Default Shell), com split para dois terminais; fechar o painel deixa o processo rodando, a lixeira mata. Shift + End seleciona até o fim da linha, Alt + clique cria vários cursores.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], a extensão SQLite abre o `database.sqlite` (Open Database) no SQLite Explorer, com Show Table. O editor deixa cinza uma variável não usada, e foi assim que Mayk achou `insertedClass` trocado; Alt+clique põe aspas em vários `${}` de uma vez.

## Key sources

- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — Emmet e Live Server na aula de básico de CSS
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: tema, Live Server, Emmet e hover de seletor
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: Emmet `.classe`, `*2`, `+`, `mr`; linha guia de tag
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Git → Node → Yarn → VS Code; lista de extensões; Git Bash como terminal
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: pasta "HTML básico", New File `index.html`, Emmet `html` + opção 5 (`html:5`)
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: Emmet `link:css`; autocompletar de caminho com `./`
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: Ctrl+D, localizar e substituir, minimapa
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: Git Bash no terminal; extensão Nunjucks, Emmet e settings.json
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: tema Omni, Material Icon Theme, IntelliSense
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: extensão SQLite, terminal split, ícones por pasta
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Emmet em JSX, FiraCode
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: pasta "Flexbox aula", index.html + css/style.css e Live Server na prática 1 de flexbox
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: multicursor para gerar código repetitivo
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: Emmet, Live Server, Alt+Z, Ctrl+/, color picker
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: Ctrl+D, Alt + clique, aviso de sintaxe
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: Ctrl+P, Shift + clique, Ctrl+D
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Live Sass Compiler e Live Server
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: Git Bash no terminal integrado
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: extensão SQLite e variável não usada
