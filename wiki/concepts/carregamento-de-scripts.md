---
type: concept
title: "Carregamento de scripts: posição, defer e async"
aliases: ["defer", "async", "script defer", "script no fim do body", "<script> no head", "carregamento de JavaScript"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
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

## Key sources

- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: script no fim do body, no começo (erro) e no head com `defer` (só externo)
