---
type: concept
title: "Elementos de composição"
aliases: ["elemento de composição", "ambiência", "elementos de ambiência", "elementos decorativos de fundo", "background decorativo"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, elementos-da-interface, elementos-de-composicao, ambiencia, background, branding, identidade-visual]
skill: ux-ui-mentor
status: stub
---

# Elementos de composição

Elementos de fundo que "servem para dar ambiência": deixam o usuário mais imerso no tema da interface, em vez de um fundo "chapado". Estrelas, poeira cósmica, ondas, órbitas, linhas, círculos tracejados, bubbles, texturas, gradientes ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]). Item do roteiro de [[wiki/concepts/elementos-da-interface]].

## Quatro regras da aula

1. **Observar os elementos da natureza** (céu, ondas, espaço).
2. **Compõem o background, sem muito [[wiki/concepts/contraste]]**: o contraste fica com o ponto focal (logo, título, CTA). Ver [[wiki/concepts/hierarquia-visual]].
3. **Acompanham a branding, a ideia, o tema**: foguete e espaço na [[wiki/entities/rocketseat]], quadrado/X/triângulo/círculo na [[wiki/entities/playstation|PSN]], eclipse no [[wiki/entities/frontpush]], Matrix no [[wiki/entities/codesec]]. Ver [[wiki/concepts/harmonia-visual]].
4. **Ajudam a compor [[wiki/concepts/empty-state|empty screens]].**

## Como se fazem (no Figma)

- Luz difusa: uma elipse na cor da marca com layer blur alto (400 no FrontPUSH).
- Iluminação: camada extra de preenchimento radial.
- Pontinhos = estrelas; riscos = estrelas cadentes; círculos = órbitas.
- Integração de fotos: [[wiki/concepts/blend-modes]].

## Não é regra

"Depende do projeto": o [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] usa textura e foto, quase sem elemento de composição.

## Olhar de dev

`[skill: ux-ui-mentor]` Decorativo não é conteúdo: vai em `background-image` no CSS ou em SVG/imagem com `aria-hidden="true"` / `alt=""` (ver [[wiki/concepts/texto-alternativo]]). Se animado, respeitar `prefers-reduced-motion`. WCAG não exige contraste de elemento decorativo, mas o texto por cima precisa passar no pior ponto do fundo `[external]` (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Na visão geral

Descritos em uma frase: trazem "pontos de atenção" e deixam a interface "um pouco mais elegante" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Key Sources

- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — definição em uma frase na visão geral
