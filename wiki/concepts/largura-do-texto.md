---
type: concept
title: "Largura do texto (medida de linha)"
aliases: ["largura de linha", "largura de texto", "line length", "medida de linha", "comprimento de linha", "caracteres por linha", "measure"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 3
tags: [ui, ui-design, tipografia, largura-do-texto, largura-de-linha, medida-de-linha, legibilidade, leiturabilidade, acessibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Largura do texto (medida de linha)

Variável tipográfica: quantos caracteres ou palavras cabem numa linha. Junto com a [[wiki/concepts/altura-de-linha]], é o que deixa a [[wiki/concepts/tipografia]] "mais confortável ao ler" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]).

## Contar palavras ou caracteres

Na aula de abertura, "largura de texto se deve literalmente a quantidade de palavras que tem uma linha", contando só palavras de duas letras ou mais; no exemplo da Globo, 9 ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). A aula de largura conta das duas formas, caracteres e palavras ([[wiki/sources/altura-de-linha-e-largura-do-texto]]).

`[skill: ux-ui-mentor]` A medida usual é por caracteres. No CSS, `max-width: 65ch` (`ch` é a largura do "0").

## Faixas

As referências não coincidem:

| Referência | Faixa |
|---|---|
| Aula ([[wiki/entities/nasser\|Násser]]) | 60 a 90 caracteres; 9 a 15 palavras por linha |
| `[skill: ux-ui-mentor]` | 45 a 75 caracteres no corpo; `max-width: 65ch` |
| `[external]` WCAG 1.4.8 (AAA) | no máximo 80 caracteres (40 em CJK) (https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html; https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html) |

Fonte da linha da aula: [[wiki/sources/altura-de-linha-e-largura-do-texto]]. A aula chama a faixa de "coringa": há sites menores e maiores. O teto da aula (90 caracteres) passa do teto da WCAG (80) e do da skill (75).

## Longo, curto e de propósito

- **Muito longo cansa:** a [[wiki/entities/wikipedia]] é o contraexemplo das duas aulas. Na de abertura, "deixa muito extenso", com "muitas palavras em uma linha", e "torna-se mais cansativo para ler" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]); na de largura, "te cansa um pouco rápido" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). `[skill: ux-ui-mentor]` O olho se perde ao voltar para a linha seguinte.
- **Curto é mais confortável:** a Globo poderia esticar o texto, mas "com estudos, percebe-se que deixar assim mais curtinho [...] fica mais confortável de se ler" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).
- **Curto acelera:** a coluna da Globo ao lado de uma publicidade tem 4 a 6 palavras por linha, "meio que é de propósito", para um "resumão" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). `[skill: ux-ui-mentor]` Curto demais quebra o ritmo em textos longos.
- **Container:** o [[wiki/entities/new-york-times]] não deixa o texto ir "de ponta a ponta" e o divide em parágrafos ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). Ver [[wiki/concepts/espaco-em-branco]].

Em tela larga, a largura vem do container, não da tela: ver [[wiki/concepts/design-responsivo]].

`[external]` A Wikipedia mudou depois: a skin Vector 2022, padrão na versão em inglês desde janeiro de 2023, limita a largura do conteúdo (https://www.mediawiki.org/wiki/Reading/Web/Desktop_Improvements). A aula de abertura é de 2020.

## max-width do container (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]], o container de largura máxima existe por causa dos monitores 21:9. O mesmo teto evita linhas de texto longas demais.

## Key Sources

- [[wiki/sources/altura-de-linha-e-largura-do-texto]]: 60–90 caracteres, 9–15 palavras; Globo, Wikipedia e NYT
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: contar palavras por linha; Wikipedia x Globo
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: container com `max-width` também limita a linha
