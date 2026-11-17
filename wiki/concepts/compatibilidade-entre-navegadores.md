---
type: concept
title: "Compatibilidade entre navegadores (Can I use, Baseline)"
aliases: ["suporte de navegadores", "cross-browser", "Can I use", "caniuse", "browser support"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 5
tags: [frontend, navegador, css, javascript, compatibilidade, baseline]
skill: tech-mentor-frontend
status: stub
---

# Compatibilidade entre navegadores (Can I use, Baseline)

Todo navegador entende HTML, CSS e JavaScript, mas cada um interpreta "com uma diferençazinha", principalmente no CSS, e recursos novos chegam em tempos diferentes. Para saber o que já dá para usar, consulta-se o **Can I use**, que mostra em que versão de cada navegador um recurso chegou, se está desligado por padrão e como ativá-lo ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]).

## Exemplo da aula: backdrop-filter

[[wiki/entities/nasser|Násser]] mostra `transform` (CSS3 2D transforms), suportado em toda parte, e `backdrop-filter` ("aquele efeito de vidro desfocado"), que no Firefox 98/99 vinha desligado por padrão. Efeitos do site do [[wiki/entities/frontpush]] não apareciam no Firefox por isso. `[external]` O Firefox passou a suportar por padrão na versão 103, em julho de 2022: https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter#browser_compatibility.

## Como se decide hoje

`[skill: tech-mentor-frontend]` O **Baseline** (web.dev, badge no MDN) resume o suporte: *newly available* quando o recurso está na versão atual de Chrome, Edge, Firefox e Safari; *widely available* depois de cerca de 30 meses, seguro para uso geral (https://web.dev/baseline). O alvo do projeto fica num `.browserslistrc`, lido por PostCSS, Lightning CSS e bundlers. Para recursos ainda incompletos, `@supports` e progressive enhancement: a página funciona sem o efeito.

O [[wiki/entities/mdn-web-docs|MDN]] traz a tabela de compatibilidade e o selo Baseline em cada página. Ver também [[wiki/concepts/guerra-dos-navegadores]], [[wiki/concepts/biblioteca-javascript-de-compatibilidade]] e [[wiki/concepts/css]].

## Can I use na introdução ao Sass

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], Násser volta ao Can I use com `transform`: legenda (verde suportado, vermelho não, verde escuro parcial, cinza desconhecido), versões de IE e Edge, e os prefixos `-moz-`, `-ms-`, `-webkit-` em versões antigas; 98% com prefixo, 96% sem. Diz que o Sass põe os prefixos sozinho; quem faz isso é o Autoprefixer ([[wiki/concepts/prefixo-de-fornecedor]]).

## Prefixos no CSS compilado

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o CSS que sai do Live Sass Compiler já traz `-webkit-` e `-ms-` "para poder melhorar a compatibilidade com browsers antigos" ([[wiki/concepts/prefixo-de-fornecedor]]).

## Key sources

- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Can I use, `transform` x `backdrop-filter` no Firefox
- [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]]: slide: usar `flex` em vez das propriedades separadas "para melhor consistência entre os browsers" (`0` sem unidade era problema do IE10/11)
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: Can I use, legenda e prefixos de `transform`
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: prefixos automáticos no CSS compilado
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: "o browser não entende JS atualizado", com arrow function e CSS Grid como exemplos
