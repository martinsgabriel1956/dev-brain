---
type: concept
title: "Caminho relativo de arquivos (HTML x CSS)"
aliases: ["caminho relativo", "relative path", "../", "voltar um diretório", "src relativo", "url() relativo"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [frontend, html, css, caminho-relativo, arquivos]
skill: tech-mentor-frontend
status: stub
---

# Caminho relativo de arquivos

Um caminho relativo parte da pasta do arquivo que o escreve. `imagens/bird1.jpg` entra numa pasta vizinha; `../imagens/bird1.jpg` sobe um nível antes.

## HTML e CSS partem de lugares diferentes

Em [[wiki/sources/principais-propriedades-css-color-background-font]], [[wiki/entities/nasser|Násser]] mostra a mesma imagem chamada de dois lugares:

- **No `<img src>`** o caminho parte do `index.html`. Como ele está na raiz, ao lado da pasta de imagens, "eu posso ir direto".
- **No `background-image: url()`** o caminho parte do `style.css`, que está numa subpasta. Então "eu tenho que voltar para essa página principal para depois entrar a imagem", com "ponto, ponto", isto é, `../`.

`[external]` A regra: `url()` dentro de uma folha de estilo é resolvida a partir da URL da folha, não da página que a carrega (https://developer.mozilla.org/en-US/docs/Web/CSS/url_value). Um caminho que começa com `/` parte da raiz do site e não depende de onde o arquivo está.

## css/style.css, ./ e ../ no <link>

Em [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]], [[wiki/entities/nasser|Násser]] liga `CSS/style.css` pelo `<link>`: entrar numa pasta é `pasta/arquivo`, `./` é "esse diretório de agora" e `../` volta uma pasta (no exemplo, chega à área de trabalho). Digitar `./` faz o [[wiki/entities/vs-code]] listar o que há na pasta.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], `href="style.css"` funciona no `index.html` da raiz, mas copiado para `page/page.html` o navegador procura `page/style.css`. Com uma barra na frente, `/style.css` parte da raiz do servidor (`127.0.0.1:5500/`). "Por causa de uma barra eu poderia estar dias descobrindo o porquê". Inferência do agente: aberto por dois cliques (`file://`), o mesmo `/` apontaria para a raiz do disco.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], mover `style.css` para `styles/` quebra o estilo: "ele não vai achar porque agora não está nesse local". Os links passam a `/styles/main.css` e `/styles/partials/page-landing.css`, e Mayk avisa que "muitos erros que eu vejo os alunos cometendo" são arquivos fora da pasta `partials`.

## require × fs (JStack, aula 06)

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], `require('../mocks/users')` resolve a partir do arquivo que importa. Já caminhos de `fs` (`readFile('./x')`) resolvem a partir do diretório onde o processo foi iniciado; por isso se usa `__dirname` para eles.

Em [[wiki/sources/frontpush-modules-js-import-export-default]], o `import` usa `from "./retângulo.js"`: "como está no mesmo diretório, eu faço ponto barra". No navegador, `./` e a extensão são obrigatórios; acento no nome do arquivo funciona, mas complica URL e terminal.

## Key Sources

- [[wiki/sources/principais-propriedades-css-color-background-font]]: `src` a partir do index, `url()` a partir do style.css com `../`
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: `CSS/style.css`, `./` e `../` no `<link>`
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: style.css sem barra x com barra
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: styles/partials e o erro comum dos alunos
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: require relativo ao arquivo, fs relativo ao cwd
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: ./ no import do navegador
