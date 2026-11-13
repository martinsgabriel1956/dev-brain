---
type: concept
title: "Constraints no Figma"
aliases: ["constraints", "restrições de layout", "constraints do Figma", "top e left", "scale constraint"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [figma, ui-design, layout, responsividade, icones]
skill: ux-ui-mentor
status: stub
---

# Constraints no Figma

Regra que diz como uma camada se comporta quando o frame que a contém muda de tamanho: fica presa a um lado (top, left, bottom, right), aos dois lados (estica junto), ao centro, ou escala (Scale). É o que impede um [[wiki/concepts/icones-em-interfaces|ícone]] de deformar quando o card ou o artboard em volta dele é redimensionado.

## Opções

- **Top / Left** (e Bottom / Right): mantém a distância até aquela borda. `[external]` É o padrão do Figma (https://help.figma.com/hc/en-us/articles/360039957734).
- **Left & Right / Top & Bottom**: mantém as duas distâncias, então o objeto estica junto com o frame.
- **Center**: fica centralizado no eixo escolhido.
- **Scale**: cresce e encolhe na proporção do frame.

## Nas aulas

- Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: constraints definem "como o objeto vai se comportar quando eu modificar as dimensões do frame"; top/left fixa, right-bottom inverte, scale escala; usadas junto com o [[wiki/concepts/grid-de-icones|grid]] e o componente.
- Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: o ícone do [[wiki/entities/feather-icons]] chega como frame; dentro de outro frame, ele esticava junto ("a escala fica presa ao tamanho do frame"). A correção é fixar "acima e na esquerda" (top e left) ou centralizar, e então agrupar (Ctrl G) e posicionar no centro do círculo. "Depende do que você quer fazer."

## Olhar de dev

`[skill: ux-ui-mentor]` Constraints são o equivalente, no protótipo, a posicionamento e dimensionamento no CSS: top/left fixo ≈ `position` com offsets; Left & Right ≈ largura fluida; Center ≈ `margin: auto` ou `place-items: center`; Scale ≈ unidades relativas. Para layouts que mudam de conteúdo, o Auto Layout do Figma (o flexbox do Figma) costuma substituir constraints. Ver [[wiki/concepts/design-responsivo]].

## Key Sources

- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — top/left, right-bottom e scale no ícone com grid e componente
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — ícone do plugin deformando com o frame; top/left e center
