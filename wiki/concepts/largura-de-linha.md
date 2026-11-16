---
type: concept
title: "Largura de linha"
aliases: ["largura de texto", "medida de linha", "line length", "measure", "comprimento de linha"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, largura-de-linha, legibilidade, acessibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Largura de linha

Variável tipográfica: quanto texto cabe numa linha. Na aula de abertura de [[wiki/concepts/tipografia]], "largura de texto se deve literalmente a quantidade de palavras que tem uma linha", contando só palavras de duas letras ou mais; no exemplo da Globo, 9 ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## Linha longa cansa

A Wikipedia é o contraexemplo da aula: "deixa muito extenso", com "muitas palavras em uma linha", e "torna-se mais cansativo para ler". A Globo poderia esticar o texto, mas "com estudos, percebe-se que deixar assim mais curtinho [...] fica mais confortável de se ler".

`[external]` A Wikipedia mudou depois: a skin Vector 2022, padrão na versão em inglês desde janeiro de 2023, limita a largura do conteúdo (https://www.mediawiki.org/wiki/Reading/Web/Desktop_Improvements). A aula é de 2020.

## Caracteres, não palavras

`[skill: ux-ui-mentor]` A medida usual é 45–75 caracteres por linha no corpo. No CSS, `max-width: 65ch` (`ch` é a largura do "0"). Linha longa demais faz o olho se perder na volta; curta demais quebra o ritmo.

`[external]` A WCAG 1.4.8 (AAA) pede no máximo 80 caracteres por linha (40 em CJK) (https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html).

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: contar palavras por linha; Wikipedia x Globo
