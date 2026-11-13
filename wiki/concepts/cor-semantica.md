---
type: concept
title: "Cor semântica"
aliases: ["cores semânticas", "cor de feedback", "cor de estado", "semantic color", "status colors"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, cor, cor-semantica, feedback, acessibilidade, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Cor semântica

Cor usada para dizer algo, não para enfeitar: o usuário lê o estado ou o tipo da informação pela cor antes de ler o texto. Na aula de Násser, "cores funcionam para poder dar informação" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## As convenções da aula

| Cor | Leitura | Exemplo da aula |
|---|---|---|
| Azul | link, informação | link azul se reconhece "de cara" |
| Vermelho | alerta, erro | "alertas geralmente são colocados na cor vermelha" |
| Amarelo | warning | "para poder sinalizar alguma coisa para o usuário" |
| Cor de destaque / preenchimento | hierarquia maior | botão preenchido acima do não preenchido |

É um [[wiki/concepts/padroes-de-interface|pattern]]: funciona porque o usuário já aprendeu. Ver também [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/feedback-do-sistema]].

`[skill: ux-ui-mentor]` A skill dá o mapa completo de feedback: verde sucesso, vermelho erro, âmbar warning, azul info. No código, isso vira tokens semânticos (`--color-error`, `--color-warning`), não cores cruas. No dark mode, os tokens mudam de valor, não de nome.

## Nunca só a cor

`[skill: ux-ui-mentor]` Regra crítica: estado não se comunica só pela cor. Daltonismo afeta cerca de 8% dos homens; acompanhe com ícone, texto ou padrão.

`[external]` WCAG 2.2, critério 1.4.1 (Use of Color): https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. Link diferenciado só pela cor precisa de contraste de 3:1 com o texto ao redor e de outro sinal no foco ou hover; o sublinhado resolve.

## Cor como código entre cursos

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: nos ícones do site do autor, "tudo que é laranja está remetendo ao curso de UI Design", "uma seleção que o seu cérebro faz até pela cor". É convenção de marca, não de estado; vale a mesma regra de nunca depender só da cor.

## Key Sources

- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — azul link, vermelho alerta, amarelo warning; botão preenchido como hierarquia
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — laranja = curso de UI Design nos ícones do site
