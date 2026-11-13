---
type: concept
title: "Ícones em interfaces"
aliases: ["ícone", "ícones", "iconografia", "icon", "icons", "ícones de sistema", "system icons"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 7
tags: [ui, ui-design, elementos-da-interface, icones, iconografia, carga-cognitiva, padroes-de-interface, acessibilidade]
skill: ux-ui-mentor
status: stub
---

# Ícones em interfaces

"Um ícone é um símbolo, uma representação visual de um objeto, ação ou ideia usados em algum contexto para comunicar algo" (slide de [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]).

## Três coisas que um ícone representa

| Representa | Exemplo | Observação |
|---|---|---|
| Ideia | nuvem = internet; arroba = e-mail/usuário | metáfora; o ícone "fiel" (computadores ligados) seria complexo demais |
| Ação | engrenagem = configurar; "+" = adicionar; sininho = notificações | "convidando para uma ação" |
| Objeto | chip = processador da Apple; câmera = câmera | literal |

O significado das ideias e ações vem do uso repetido: é um [[wiki/concepts/padroes-de-interface|pattern]] aprendido ("o ser humano é movido por padrões"), não do desenho em si. Ver [[wiki/concepts/reconhecimento-de-padroes]].

## Por que usar

- **Reduz a [[wiki/concepts/carga-cognitiva]]**, se for [[wiki/concepts/simplicidade-visual|simples]].
- **Comunica mais rápido que texto**: "o ser humano [...] é extremamente visual".
- **Deixa a interface mais leve**: itens em tópicos, cada um com ícone ao lado (site da Apple).
- **Atravessa idiomas, até certo ponto**: Násser trocou o idioma de um retroprojetor em japonês guiado pelos ícones.

## Regras

- Simples, geométrico, sem detalhe desnecessário ([[wiki/entities/material-design]]: "simple, modern, friendly").
- Shapes e tamanhos consistentes; uma [[wiki/concepts/familia-de-icones]] por projeto ([[wiki/concepts/consistencia-visual]]).
- O estilo (reto x arredondado, linha x preenchido) segue a identidade visual ([[wiki/concepts/formas-geometricas-e-organicas]]).
- Formato: SVG ([[wiki/concepts/formato-svg]]).

## Limites

`[external]` Para a Nielsen Norman Group, ícones "universais" são raros (casa, impressora, lupa); a maioria é ambígua, então ícones precisam de rótulo de texto e de teste de reconhecimento (https://www.nngroup.com/articles/icon-usability/). A própria aula dá o exemplo: a avó de Násser não reconhecia o "compartilhar" de três bolinhas.

## Olhar de dev

`[skill: ux-ui-mentor]` Ícone funcional sem texto visível leva `aria-label` (ou `title` no SVG); ícone decorativo ao lado de texto, `aria-hidden="true"`. Contraste mínimo de 3:1 para ícones informativos. Alvo de toque de pelo menos 44×44 px. Em RTL, ícones direcionais espelham; engrenagem e coração, não. Estado nunca só por cor: cor + ícone + texto. Ver [[wiki/concepts/texto-alternativo]].

## Como construir (parte 2)

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: tamanho é secundário porque o ícone é SVG e escala (Material: 24×24; Násser: 56 para ênfase, 32 para os menores); margem para ter ponto focal; tamanhos pares e [[wiki/concepts/simetria-visual|simetria]], porque o olho vê um pixel torto; [[wiki/concepts/centralizacao-optica|centralização óptica]] no play; [[wiki/concepts/grid-de-icones|grid de construção]] (área útil 20×20); componente com constraints em scale no [[wiki/entities/figma]]. Preenchido ou linha é decisão de [[wiki/concepts/hierarquia-visual]].

## Estudo de caso (parte 3)

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]]: ícones resumem uma grade densa em cards; o processo vai do módulo a uma palavra-chave e dela a uma busca no Google e em bibliotecas de linha ([[wiki/entities/feather-icons]], [[wiki/entities/eva-icons]], Flaticon, Noun Project). Regra final: o objeto basta ("só o chapéuzinho", "só o livrinho"). Associações arbitrárias, como heptágono = sete dias, não são pattern e dependem do texto ao lado (inferência).

## Facebook em japonês

Ícones ficam numa classe à parte das ilustrações porque dizem o que fazer. Com o Facebook em japonês, ainda dá para navegar: caixa de entrada, sininho, engrenagem, lápis, escudo ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). A aula diz que isso dá "melhor acessibilidade"; vale para quem enxerga e conhece o pattern. `[skill: ux-ui-mentor]` Para leitor de tela, ícone sem texto precisa de `aria-label`.

## Ícone ilustrado vetorizado à mão

O "app telefone" de [[wiki/entities/nasser|Násser]] é um ícone de app ilustrado: fundo com gradiente linear verde e sombras, telefone com sombra interna e externa, desenhado com a [[wiki/concepts/vetorizacao-com-pen-tool|Pen Tool]] sobre uma imagem da internet ([[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]). É mais ilustração que ícone de sistema; a aula não usa [[wiki/concepts/grid-de-icones|grid]] nem [[wiki/concepts/familia-de-icones|família]].

## Dicas da edição "W7"

Na aula teórica da edição "W7" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]), o slide organiza o tema em comunicação, dicas e consistência. Quatro dicas: **clareza** (comunicar rápido; label "pode ser necessário ou não"; ícone ao lado do texto do botão enfatiza a ação), **legibilidade** (simples e em [[wiki/concepts/formato-svg|SVG]], reconhecível "em diferentes tamanhos e ambientes"), **alinhamento** (cards para homogeneizar ícones de proporções diferentes, sem desculpar um play fora do centro; ver [[wiki/concepts/centralizacao-optica]]) e **personalidade** (preenchido mais realista, linha mais simplificada). O senso comum manda: engrenagem é mais forte que chave de boca para configuração; carta, balão, escudo e carrinho/sacola são os exemplos do [[wiki/entities/feather-icons]]. O exemplo de idioma desta edição é uma viagem a Viena.

## Prática da edição "W7"

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: plugins da comunidade do [[wiki/entities/figma]] (Feather, Bootstrap Icons, Material Design Icons, Iconify); ícones próprios para os módulos do site, cada um dizendo o que o módulo trata (computador + smartphone = interface web responsiva; átomo = React; colunas mescladas = grid x Flexbox; presente = bônus); e o ícone dentro de círculo, card ou quadrado para equilibrar proporções diferentes, com [[wiki/concepts/constraints-no-figma|constraints]] para não deformar.

## Key Sources

- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — aula teórica de ícones: definição, patterns, objeto x ação, Material Design, identidade visual, famílias
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — como construir: tamanho, SVG, margem, simetria, grid, componente
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — estudo de caso do FrontPUSH: grade em cards, palavra-chave, bibliotecas, "só o chapéuzinho"
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — ícones que se entendem sem o idioma; ressalva de acessibilidade
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — ícone de app (telefone) vetorizado à mão com Pen Tool e Bend Tool
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — aula teórica "W7": pistas visuais, senso comum, clareza, legibilidade, alinhamento em cards, personalidade, no máximo duas famílias
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — aula prática "W7": plugins, ícones próprios dos módulos, ícone dentro de círculo, constraints
