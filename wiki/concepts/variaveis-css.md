---
type: concept
title: "Variáveis CSS (custom properties)"
aliases: ["custom properties", "variáveis no CSS", "var()", ":root", "CSS variables"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 10
tags: [frontend, css, variaveis-css, design-tokens, cores]
skill: tech-mentor-frontend
status: stub
---

# Variáveis CSS (custom properties)

Propriedades com nome começando por `--`, declaradas num seletor (em geral `:root`, a raiz do documento) e lidas com `var(--nome)`. Herdam como qualquer propriedade e podem ser trocadas em tempo de execução, o que as torna o veículo usual de design tokens no CSS. Ver [[wiki/concepts/css]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] declara `--title-color: #322153` e `--primary-color: #34CB79` em `:root` para não repetir cores: "se algum dia eu quiser mudar essa cor aqui, eu não preciso ir em todos os lugares que apareça essa cor e vir mudando". Chama de "um atalho" e "em formato de variáveis".

## Precisões

- `var()` aceita um valor reserva: `var(--primary-color, green)` `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/var).
- Diferente das variáveis de Sass, existem no navegador: mudar `--primary-color` num `.dark` troca o tema sem recompilar `[skill: tech-mentor-frontend]`.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], as variáveis do Proffy ficam em `:root` com "dois tracinhos" e são lidas com `var(--color-background)`. Trocar o valor de `--color-primary-darker` por "um super vermelho" muda o documento inteiro: "fica fácil de eu alterar as cores".

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], a variável `--color-secundary` (com U) foi corrigida para `--color-secondary`; quem digitou com U fica sem a cor, porque `var()` com nome inexistente não acha valor. Os botões e cards usam `--color-primary-lighter`, `--color-secondary-dark`, `--color-box-base` e `--color-line-in-white`.

## "Só cores" no CSS puro? (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], [[wiki/entities/nasser|Násser]] diz que "no CSS puro você só tem como criar variáveis com cores, com hexadecimais", e que o Sass permite variáveis com "propriedades inteiras", como um `box-shadow` de várias camadas. `[external]` Custom properties aceitam qualquer valor: `--sombra: 0 1px 2px #0003, 0 4px 8px #0002;` e `box-shadow: var(--sombra)` funcionam (https://developer.mozilla.org/en-US/docs/Web/CSS/--*). A vantagem do Sass está noutro lugar: `$variáveis` em contas e laços na compilação.

## Arquivo de cores no Sass (FrontPUSH, aula 03)

Em [[wiki/sources/frontpush-import-e-partials-sass]], as variáveis de cor ficam num `_colors.scss` importado no topo do `style.scss`: "quando eu quiser modificar alguma cor, basta eu modificar nessas variáveis". Ele troca `gray` por `cinza` para não misturar inglês e português. `[external]` No Sass são `$branco: #fff;`, resolvidas na compilação; o CSS final só tem os valores.

## Sass × custom properties (FrontPUSH, aula 04)

Em [[wiki/sources/frontpush-variaveis-sass]], as variáveis são as do Sass (`$branco`), que desaparecem na compilação. A comparação com custom properties (tempo de execução, cascata, temas) está em [[wiki/concepts/variaveis-sass]].

## Tema por @if × tema por custom property (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-if-else-sass]], o tema light/dark é escolhido por `$layout` na compilação: sai um CSS com um tema só. Para o usuário trocar, ou para seguir `prefers-color-scheme`, as cores têm de ser custom properties redefinidas por `[data-theme]` ou media query.

## Na NLW #2, dia 1 (Diego Fernandes)

As cores do layout vêm prontas como custom properties no `global.css`, "caso você queira customizar o tema [...] para algum tema dark", e o CSS nunca usa cor fixa. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 4 (Diego Fernandes)

No RN não há custom properties; constantes de JS funcionariam, mas Diego prefere Styled Components com tema em projetos maiores. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: `--title-color` e `--primary-color` em `:root`
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Sass como pré-processador; ver [[wiki/concepts/pre-processador-css]]
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: cores do Proffy em :root
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: o erro secundary/secondary
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: Sass: "só cores" no CSS puro (impreciso)
- [[wiki/sources/frontpush-import-e-partials-sass]]: Sass: arquivo de cores importado
- [[wiki/sources/frontpush-variaveis-sass]]: aula de variáveis do Sass; comparação em variaveis-sass
- [[wiki/sources/frontpush-if-else-sass]]: tema de compilação (Sass) × tema em tempo de execução
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: cores em variáveis para trocar o tema
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: sem variáveis de CSS no RN
