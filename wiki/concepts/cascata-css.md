---
type: concept
title: "Cascata do CSS (prioridade entre estilos)"
aliases: ["cascade", "cascata CSS", "prioridade do CSS", "estilo inline", "estilo incorporado", "CSS externo", "formas de aplicar CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [css, cascata, especificidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Cascata do CSS (prioridade entre estilos)

O "C" de [[wiki/concepts/css]]: quando várias declarações miram a mesma propriedade do mesmo elemento, a cascata decide qual vale.

## As três formas de aplicar

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], três formas, em prioridade crescente segundo o slide:

| Forma | Onde | Alcance | Uso |
|---|---|---|---|
| Externo | arquivo `.css` ligado por `<link>` | todas as páginas que o ligam | "a forma mais utilizada" |
| Incorporado | `<style>` no `<head>` | só a página | exceção por página |
| Inline | atributo `style` na tag | só a tag | exceção por tag |

O argumento é de manutenção: com um arquivo externo, trocar uma cor é editar um lugar, não 40 páginas.

## O que de fato decide

`[external]` A ordem é: origem e importância (`!important` vence o normal), depois especificidade do seletor (inline > id > classe > tag), depois ordem no código (o último vence). Externo e incorporado empatam em origem e especificidade, então vence o que aparece depois no documento; a própria aula mostra o `style.css` sobrescrevendo o `<style>`. Fontes: https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade e https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.

`[skill: tech-mentor-frontend]` Em escala, a ordem é controlada por arquitetura: ITCSS (camadas por especificidade crescente) ou `@layer`, em que a ordem das camadas vence a especificidade e o código fora de camada vence tudo em camada.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] diz que o seletor encadeado `#page-home .content` "é uma forma de cascata. É por isso que chama-se Cascading Style Sheet". `[external]` Não é: a cascata é o algoritmo que decide entre declarações conflitantes (https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade). O exemplo certo está na mesma aula: a cor do grupo `h1...h6` riscada no DevTools porque uma regra posterior a sobrescreve.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] ordena os `<link>`: `main.css`, depois a página e "o responsivo fica por último". As variáveis do `main.css` valem no `create-point.css` porque "ele está seguindo essa ordem no documento HTML". É a ordem de declaração da cascata, agora entre arquivos.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] responde uma dúvida da turma: o `responsive.css` tem de vir por último, porque se vier antes, as regras seguintes "sobrescrevem" as da media query. É a cascata por ordem de origem, agora explicada direito (o dia 1 chamava seletor descendente de cascata).

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o React Native não tem cascata nem herança `View` → `Text`: cada `Text` recebe o próprio estilo. A exceção é `Text` dentro de `Text`, que herda.

## Key sources

- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — externo, incorporado e inline; "quanto mais para baixo, maior a prioridade"; demo em que o externo vence o incorporado
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: seletor descendente chamado de cascata (impreciso); cor sobrescrita no DevTools
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: ordem dos arquivos CSS
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: estilos padrão do navegador sobrescritos pelo autor; ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: ordem dos links e sobrescrita
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: sem cascata no React Native
