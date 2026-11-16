---
type: concept
title: "Classificação tipográfica"
aliases: ["classificações tipográficas", "tipos de fonte", "serifada", "sem serifa", "sans-serif", "slab serif", "serifada grossa", "egípcia", "script", "cursiva", "blackletter", "monoespaçada", "monospaced", "display", "decorativa"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, fonte, serifa, sem-serifa, script, blackletter, monoespacada, display]
skill: ux-ui-mentor
status: stub
---

# Classificação tipográfica

Agrupar fontes por desenho e sensação para escolher e combinar com um porquê: "entender o porquê que a gente escolheu uma, porquê que a gente escolheu a outra" ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]). Parte de [[wiki/concepts/tipografia]].

## As sete classificações da aula

| Classificação | Desenho | Passa | Uso | Exemplos |
|---|---|---|---|---|
| Serifada | Entalhes e curvas nas pontas | Clássica, elegante; a moderna, luxo | Títulos; corpo é possível, mas incomum na web | Times New Roman (vitrine), Garamond, Baskerville, Bodoni, [[wiki/entities/new-york-times]] |
| Sem serifa | Retas, simples, sóbrias | Neutra, moderna, tecnologia | Tudo, "principalmente para corpo de texto" | Helvetica e Arial (vitrines), Candara, Bauhaus |
| Serifada grossa (slab, egípcia) | Serifada encorpada, peso alto | Impacto | Título, anúncio, botão | Rockwell |
| Cursiva / script | Parece feita à mão | "Mais perto da pessoa" | Título, marca, anúncio; convites | Script |
| Blackletter | Grafia de época (Alemanha, Idade Média) | Muito característica | Título, anúncio, botão | — |
| Monoespaçada | Cada caractere com a mesma largura | — | Código | Roboto Mono |
| Display | "O que sobra" | Diferente das demais | Título, anúncio, botão | — |

As duas primeiras dominam a web; as outras ficam fora do corpo de texto por [[wiki/concepts/legibilidade-tipografica|legibilidade]].

## Subclasses

O slide divide as serifadas em humanistas, "transacional", moderna e egípcia, e as sem serifas em humanistas, "transacional" e geométricas. A geométrica é a ponte com [[wiki/concepts/formas-geometricas-e-organicas]]: a Bauhaus é feita de círculos, semicircunferências e retângulos. A script faz o papel do orgânico, "feita à mão".

`[external]` O termo técnico é "transicional". No Vox-ATypI, a Garamond é garalde, não humanista; o sistema foi aposentado pela ATypI em 2021 (https://en.wikipedia.org/wiki/Vox-ATypI_classification). Os catálogos usam nomes próprios: o [[wiki/entities/google-fonts]] chama script de handwriting; o [[wiki/entities/adobe-fonts]] tem Slab Serif, Script, Blackletter, Mono, Hand e Decorative.

## Classificação vira token

`[skill: ux-ui-mentor]` Num design system, a classificação aparece como papel: tokens `display`, `body`, `serif` e `mono`, no máximo duas famílias com papéis definidos. Números em tabela pedem `font-variant-numeric: tabular-nums`, não uma mono.

## Key Sources

- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]] — as sete classificações, exemplos e a regra título x corpo
