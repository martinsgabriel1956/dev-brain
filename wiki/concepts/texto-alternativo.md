---
type: concept
title: "Texto alternativo (alt text)"
aliases: ["alt text", "atributo alt", "alt", "texto alternativo de imagem", "descrição de imagem"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 2
tags: [acessibilidade, a11y, alt-text, imagens, ilustracoes, html, leitor-de-tela, wcag]
skill: ux-ui-mentor
status: stub
---

# Texto alternativo

Descrição textual de uma imagem, lida por leitores de tela e exibida quando a imagem não carrega. "Seja acessível, ou seja, sempre coloque um texto alternativo para poder descrever a sua imagem", diz [[wiki/entities/nasser|Násser]], citando as diretrizes do [[wiki/entities/material-design]] ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]).

## Informativa x decorativa

O "sempre" precisa de uma ressalva:

- **Imagem informativa** (gráfico, foto de produto, ilustração que explica um passo): `alt` descreve o que ela comunica, não o que ela é.
- **Imagem decorativa** (só ambienta): `alt=""`, vazio mas presente. `[external]` Omitir o atributo não é opção: alguns leitores de tela leem o nome do arquivo. Se possível, use background de CSS (W3C WAI, https://www.w3.org/WAI/tutorials/images/decorative/).

`[skill: ux-ui-mentor]` Quem decide o que é decorativo é o designer, no handoff: "Imagem informativa: alt="Gráfico mostrando crescimento de 40% em março"; Imagem decorativa: alt="" (vazio, não omitido)". Checklist: "Imagens informativas têm descrição documentada para alt text".

## Ligações

- [[wiki/concepts/imagens-em-interfaces]]: "peso é acessibilidade" é a outra face da acessibilidade de imagens na série.
- [[wiki/concepts/ilustracoes-em-interfaces]]: ilustração de onboarding que só preenche a tela tende a ser decorativa.
- [[wiki/concepts/contraste]]: o outro critério de acessibilidade visto nas aulas.

## Textos invisíveis e text-to-speech

Em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]], o slide diz: "Coloque textos e descrições em imagens: 'textos invisíveis'". Isso "ajuda quem tem deficiência visual a utilizar os recursos text-to-speech" dos celulares. É uma das quatro recomendações de [[wiki/concepts/acessibilidade]]; o critério correspondente é o 1.1.1 do [[wiki/concepts/wcag]] (nível A). A aula não faz a ressalva da imagem decorativa (`alt=""`) vista acima.

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — "sempre coloque um texto alternativo"
- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — "textos invisíveis" para o text-to-speech
