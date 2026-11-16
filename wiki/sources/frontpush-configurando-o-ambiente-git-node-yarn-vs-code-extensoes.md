---
type: source
title: "Configurando o ambiente: Git, Node.js, Yarn, VS Code e extensões (FrontPUSH)"
aliases: ["FrontPUSH configurando o ambiente", "aula introdutória do módulo de front-end FrontPUSH", "instalar Git Node Yarn VS Code"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, ambiente-de-desenvolvimento, git, nodejs, yarn, npm, vs-code, extensoes, live-server, sass, compatibilidade-entre-navegadores, git-bash, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Configurando o ambiente: Git, Node.js, Yarn, VS Code e extensões (FrontPUSH)

## TL;DR

Aula 01, introdutória, do módulo de front-end "de código em si" do [[wiki/entities/frontpush|FrontPUSH]], dada por [[wiki/entities/nasser|Násser]] (ele diz o próprio nome: "Ah, Násser, o meu sistema operacional não é o Windows"). Tese de abertura: para HTML, CSS e JavaScript puros não é preciso instalar nada além de um editor, porque todo navegador entende essas três linguagens. O resto é para quando o curso chegar a React. Ordem recomendada: **[[wiki/concepts/git|Git]] → [[wiki/entities/nodejs|Node.js]] (LTS) → Yarn → [[wiki/entities/vs-code|VS Code]]**. O Git vem primeiro para o VS Code detectá-lo sozinho. No meio, ele explica [[wiki/concepts/git|versionamento]] (voltar a uma versão estável, organizar trabalho em time), [[wiki/entities/github]] x GitLab, o Node como JavaScript fora do navegador e o Can I use para ver o que cada navegador suporta ([[wiki/concepts/compatibilidade-entre-navegadores]]; exemplo: `backdrop-filter`, o vidro desfocado do site do FrontPUSH, que não funcionava no Firefox). Fecha com um tour pelas extensões: vscode-icons, Thunder Client, Prettier, **Live Server** ("por favor, instale"), Live Sass Compiler (com uma explicação de [[wiki/concepts/pre-processador-css|pré-processador]]), HTML Snippets, Color Highlight, temas, e o Git Bash como terminal padrão.

## Key Claims

### Só HTML, CSS e JavaScript: basta um editor

- **Sem biblioteca, não precisa instalar nada**: "somente um editor de código, que é o VSCode". O motivo: "todo o browser, todo o navegador, ele entende três coisas, HTML, CSS e JavaScript" ([[wiki/concepts/html-hipertexto]], [[wiki/concepts/css]]).
- **Os navegadores interpretam de jeitos um pouco diferentes**, "principalmente no CSS", e há técnicas para deixar a interpretação "mais uniforme possível". Ver [[wiki/concepts/compatibilidade-entre-navegadores]].

### Git: instalação

- **Windows**: Git for Windows, que traz o Git Bash. No Linux e no Mac, "você instala o Git pelo próprio terminal": `sudo apt install git` (ou `apt-get`) no Ubuntu, `su` no Debian. Ver [[wiki/concepts/shell-terminal]].
- **sudo** = "me torne super usuário por um tempo específico"; **su** = "super user". `[external]` sudo roda um comando como outro usuário, por padrão o root (https://www.sudo.ws/docs/man/sudo.man/); `su` vem de *substitute user* e troca de usuário, root se nenhum for informado (https://man7.org/linux/man-pages/man1/su.1.html).
- **Git for Windows "vai instalar como se fosse um kernel [...] Um núcleo do Linux"**. `[external]` Incorreto: o Git for Windows traz um Bash e utilitários Unix portados (MSYS2/MinGW), sem kernel Linux nenhum. Linux de verdade no Windows é o WSL, que a própria aula mostra no fim (Ubuntu 20.04): https://gitforwindows.org/ e https://learn.microsoft.com/windows/wsl/about.
- **Instalação "next, next, next"**, aceitando os padrões recomendados. No Mac, `[external]` o caminho comum é `xcode-select --install` ou Homebrew, não apt: https://git-scm.com/download/mac.

### O que é o Git e para que serve o versionamento

- **Git é controle de versão.** Dois motivos: (1) uma atualização sobe com bug e é preciso "retornar a versão antiga para ela se tornar estável de novo"; (2) trabalho em time, cada um subindo um pedaço do código, "precisa de algo para poder organizar isso". Vale até para HTML e CSS. "Trabalhar em times nem se fala, é obrigatório você saber o Git." Ver [[wiki/concepts/git]].
- **Próximas aulas** prometem "o basicão": o que é uma branch, como sobe e desce uma atualização, como reseta.
- **GitHub e GitLab** são "repositórios online que a gente utiliza o Git para poder fazer o versionamento"; Bitbucket é citado como alternativa. Para ele o GitHub "está na frente", e todo dev que conhece usa GitHub. Ver [[wiki/entities/github]].

### Node.js e a versão LTS

- **Node é para rodar JavaScript fora do navegador** e para instalar pacotes, como o React. Ver [[wiki/entities/nodejs]].
- **Os navegadores demoram a adotar recursos novos** de CSS e JavaScript; daí o Can I use, que lista em que versão de cada navegador o recurso chegou. Exemplo: `transform` (CSS3 2D transforms), suportado em toda parte, e `backdrop-filter` ("aquele efeito de vidro desfocado"), que no Firefox 98/99 aparece em vermelho, desligado por padrão mas ativável por flag. Alguns efeitos do site do FrontPUSH não funcionam no Firefox por isso. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].
- **LTS é a versão estável**, a outra é "a versão mais atual, mas pode conter bugs". Recomenda sempre a LTS, 64 bits. `[external]` LTS é *Long Term Support*: no Node, as versões pares viram LTS e recebem correções por cerca de 30 meses; a "Current" é a mais nova sem esse compromisso (https://nodejs.org/en/about/previous-releases).
- **Uma ambiguidade**: ele diz que precisa do Node para rodar JavaScript fora do navegador "e, além disso, que ele seja um pouco mais recente", juntando o argumento de suporte dos navegadores com o Node. `[external]` Os dois são independentes: o Node não deixa o JavaScript que roda no navegador mais novo. Isso é trabalho de transpiladores e bundlers, que rodam *sobre* o Node.

### Yarn

- **Outro gerenciador de pacotes**: no React vai aparecer `npm install alguma coisa` ou `yarn add alguma coisa`. "Yarn for Windows" é um instalador à parte. Com Git, Node e Yarn, "você já está preparado para utilizar tudo que tem disponível no curso". Ver [[wiki/concepts/gerenciador-de-pacotes]].
- `[external]` O npm já vem com o Node; o Yarn moderno (2+) se ativa pelo Corepack (`corepack enable`), e o instalador de Windows é do Yarn 1 (Classic): https://yarnpkg.com/getting-started/install. `[skill: tech-mentor-frontend]` Em monorepos de hoje o pnpm (workspaces, catalog) é a escolha mais citada.

### VS Code e extensões

- **VS Code** é "muitíssimo utilizado"; recomendado também pela compatibilidade com o curso, porque alguns recursos vêm de plugins que outro editor pode não ter. Ordem final: "instala o Git, instala o Node, instala o yarn, depois o VS Code". Ver [[wiki/entities/vs-code]].
- **vscode-icons**: "literalmente estética", ícones por tipo de arquivo.
- **Thunder Client**: testar uma API (requisições) antes de ir para o código; mais fácil que o Postman, que exige instalação. Ensinado na seção de React.
- **Prettier - Code formatter**: organiza a indentação ao salvar.
- **Live Server**, "muitíssimo importante": sobe um "servidorzinho", porque "tem alguns recursos que só funcionam quando são rodados em servidor", diferente de abrir o HTML com dois cliques; e faz *auto reloading* a cada Ctrl+S, sem F5. "As aulas serão meio que nessa pegada." Ver [[wiki/concepts/setup-live-reload-debug-testes]]. `[external]` Exemplos do que falha em `file://`: módulos ES (`<script type="module">`) e `fetch` de arquivos locais, barrados pela política de mesma origem (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/importmap e https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#file_origins).
- **Live Sass Compiler**: detalhado na aula de Sass. O Sass é "um pré-processador do CSS" que "adiciona propriedades de programação" (exemplo: `if/else`, impossível no "CSS nativo") sem mudar o CSS. Ver [[wiki/concepts/pre-processador-css]].
- **HTML Snippets, Material Theme, Color Highlight** (pinta `#FFF` de branco no editor; ver [[wiki/concepts/sistema-hexadecimal]]), **One Dark Theme**. Tema dele: Community Material Theme, Ocean High Contrast.
- **Git Bash como terminal padrão**: Terminal → New Terminal. Como instalou o Git depois do VS Code, teve de escolher o Git Bash no "+" e marcá-lo como default. A lista mostra PowerShell, JavaScript Debug Terminal e Ubuntu 20.04 no WSL. O terminal só entra "nas partes de programação mesmo, como React". Ver [[wiki/concepts/shell-terminal]].

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome na aula.
- [[wiki/entities/frontpush]]: curso; esta é a aula 01 do módulo de front-end e a que configura o editor (as aulas de CSS já ingeridas pressupõem esta).
- [[wiki/entities/vs-code]]: editor recomendado, com a lista de extensões.
- [[wiki/entities/nodejs]]: runtime, versão LTS.
- [[wiki/entities/github]]: repositório online, comparado com GitLab e Bitbucket.
- [[wiki/entities/react]]: a biblioteca que justifica instalar Node e Yarn.
- [[wiki/entities/google]]: "só dá um Google" para resolver problemas de instalação.
- Sem página própria: Chrome, Firefox, Safari, Opera, GitLab, Bitbucket, Can I use, Yarn, Postman, Thunder Client, Prettier, WSL.

## Concepts

- [[wiki/concepts/compatibilidade-entre-navegadores]] (novo)
- [[wiki/concepts/pre-processador-css]] (novo)
- [[wiki/concepts/git]]
- [[wiki/concepts/gerenciador-de-pacotes]]
- [[wiki/concepts/shell-terminal]]
- [[wiki/concepts/setup-live-reload-debug-testes]]
- [[wiki/concepts/html-hipertexto]]
- [[wiki/concepts/css]]
- [[wiki/concepts/sistema-hexadecimal]]

## Tensões com a wiki

- **"HTML, que é uma linguagem de marcação"** bate com [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]]; lá, o mesmo autor chama o CSS de "mais voltada para marcação", aqui de "linguagem de estilo [...] de layout". Esta aula está mais correta.
- **"No CSS nativo" não há condicional.** `[skill: tech-mentor-frontend]` Verdade na época; hoje o CSS tem `if()` (Chromium primeiro, ainda em adoção), além de nesting nativo e [[wiki/concepts/variaveis-css|variáveis]], que tiram boa parte do motivo para o Sass. Ver [[wiki/concepts/pre-processador-css]].
- **`backdrop-filter` no Firefox.** `[external]` Habilitado por padrão desde o Firefox 103 (julho de 2022): https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter#browser_compatibility. A tela da aula (98/99 em vermelho) data a gravação de cerca de março a junho de 2022 (inferência).
- **"O GitHub já foi muito utilizado porque ele tinha melhores planos gratuitos"**: provavelmente lapso por GitLab, que oferecia repositórios privados de graça antes do GitHub. `[external]` O GitHub liberou repositórios privados ilimitados no plano gratuito em janeiro de 2019: https://github.blog/news-insights/product-news/new-year-new-github/.
- **Thunder Client como alternativa "mais fácil" ao Postman.** `[external, não verificado]` Desde 2024 parte dos recursos e o uso comercial do Thunder Client exigem licença paga; conferir antes de adotar no trabalho.

## Open Questions

- "Tem um outro também que eu esqueci o nome agora" (repositório online além de Bitbucket): não identificado.
- As aulas de Git, Sass e Thunder Client (na seção de React) ainda não estão na wiki.
- `date_published` vazio; estimativa de 2022 pela versão do Firefox na tela.

## Raw quotes

- "todo o navegador, ele entende três coisas, HTML, CSS e JavaScript"
- "Trabalhar em times nem se fala, é obrigatório você saber o Git."
- "instala o Git, instala o Node, instala o yarn, depois o VS Code"
