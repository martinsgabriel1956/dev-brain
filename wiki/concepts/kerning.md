---
type: concept
title: "Kerning"
aliases: ["kerning e tracking", "espaçamento entre pares", "kern", "font-kerning"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, tipografia, kerning, tracking, branding, logotipo, css]
skill: ux-ui-mentor
status: stub
---

# Kerning

Ajuste da distância entre dois caracteres específicos (AV, To, Wa). O [[wiki/concepts/tracking]] aplica a mesma distância a todas as letras; o kerning mexe num par. Parte de [[wiki/concepts/tipografia]].

## Coisa de marca

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], [[wiki/entities/nasser|Násser]]: kerning é "muito utilizado em criação de marcas", sempre "em um pequeno trecho", nunca no corpo do texto. Aproximar letras de propósito para que "se liguem e crie uma outra forma", ou afastá-las "para poder criar personalidade e identidade". Para treinar, indica o jogo KernType (type.method.ac).

`[external]` A aula chama a fusão de letras de "ligatura". Ligatura tipográfica é um glifo próprio que substitui dois caracteres (fi, fl); encostar letras num logotipo é desenho de marca. As fontes já trazem tabelas de kerning, que o CSS aplica por padrão e liga ou desliga com `font-kerning` (`font-kerning: auto`, https://developer.mozilla.org/en-US/docs/Web/CSS/font-kerning); ajuste manual par a par fica para logos e títulos grandes.

## Kerning x tracking na aula de abertura

O roteiro do módulo lista as duas variáveis juntas: "Alinhamento, tracking e kerning". Na aula de abertura, a definição dada mistura as duas: "Kerning é literalmente o espaçamento entre as letras." [[wiki/entities/nasser|Násser]] digita "teste" na ferramenta de texto, abre e fecha o espaçamento e cita o logo da Tesla, "bem espaçada". É um recurso "para criar branding, para criar coisa de logo", que "traz uma ideia também por trás" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

`[external]` Pela distinção padrão, o que essa aula descreve, e o logo da Tesla, é [[wiki/concepts/tracking]] (`letter-spacing`, espaço uniforme de um trecho inteiro, https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing), não kerning (ajuste entre pares). Confiança alta. A aula posterior, [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], já separa os dois termos do jeito padrão; as duas aulas concordam que o recurso serve à marca.

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]]: definição; criação de marcas; KernType
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: "kerning é o espaçamento entre as letras" (na verdade tracking); logo da Tesla
