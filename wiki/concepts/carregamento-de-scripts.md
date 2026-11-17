---
type: concept
title: "Carregamento de scripts: posição, defer e async"
aliases: ["defer", "async", "script defer", "script no fim do body", "<script> no head", "carregamento de JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [javascript, html, performance, dom, critical-rendering-path, frontend]
skill: tech-mentor-frontend
status: stub
---

# Carregamento de scripts

Quando o navegador lê um `<script>` comum, ele para de montar o HTML, baixa o arquivo (se for externo), executa e só então continua. O script só enxerga os elementos que vieram antes dele. Por isso a regra antiga era pôr os scripts no fim do `body`. Ver [[wiki/concepts/critical-rendering-path]] e [[wiki/concepts/dom]].

- **`defer`** (só em script externo): baixa em paralelo enquanto o HTML é lido e executa quando a análise do documento termina, antes do `DOMContentLoaded`, na ordem em que aparecem. Permite pôr o script no `head` sem travar a página.
- **`async`** (externo): baixa em paralelo e executa assim que chega, sem esperar o HTML nem respeitar a ordem. Serve para scripts independentes, como analytics.
- **`type="module"`** já se comporta como `defer` por padrão.
- Script inline ignora `defer` e `async`.

`[external]` https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script

`[skill: tech-mentor-frontend]` Padrão atual: `<script src="..." defer>` (ou `type="module"`) no `head`. Isso descobre o arquivo cedo, sem bloquear o parser e com a ordem garantida.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], [[wiki/entities/mayk-brito|Mayk]] mostra as três situações. No fim do body o script funciona. No começo do body falha ("o jeito do HTML ler as coisas é linha a linha"; o container "não foi colocado em tela" ainda) e dá o erro de [[wiki/concepts/null-e-undefined|null]]. No `head` com `defer`, funciona, desde que o script seja externo (`scripts/addField.js`): "ele não pega o script inline". A explicação dele, "leia esse script somente depois de um certo tempo" e "depois de passar por toda a renderização da página", simplifica demais: o `defer` espera o fim da leitura do HTML, não um tempo nem a página desenhada.

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], `document.querySelector('#app')` só encontra a div se o script rodar depois dela; com o `<script>` no `head` sem `defer`, devolve `null`.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], o script do Axios "tem que ser declarado primeiro": a tag da CDN vem antes do `app.js`, porque é ela que cria a variável global `axios`.

Em [[wiki/sources/frontpush-modules-js-import-export-default]], `<script type="module">` é o requisito para `import`/`export` no navegador. Um script módulo é adiado como `defer` por padrão, roda em *strict mode* e não cria globais ([[wiki/concepts/modulos-nodejs]]).

## Key sources

- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: script no fim do body, no começo (erro) e no head com `defer` (só externo)
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: querySelector('#app') depende da ordem do script
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: ordem das tags (Axios antes do app)
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: type="module"
