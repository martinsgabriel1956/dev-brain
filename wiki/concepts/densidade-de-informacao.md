---
type: concept
title: "Densidade de Informação"
aliases: ["espaço vs. meio", "espaço versus meio", "information density", "densidade", "compacto vs. confortável"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, layout, espacamento, densidade-de-informacao, espaco-em-branco, cards, linhas]
skill: ux-ui-mentor
status: stub
---

# Densidade de Informação

Quanto conteúdo cabe por área de tela, e quanto espaço sobra entre ele. Na aula de espaçamento e linhas, a ideia aparece como **espaço vs. meio**, "meio que uma dualidade": o espaço certo depende do meio ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]).

## Denso pede menos espaço e mais estrutura

- **Conteúdo de consumo frequente é denso.** Portal de notícia (G1) e Facebook se abrem quase todo dia; um site institucional se lê "uma vez só". Com o espaçamento largo de um site simples, o portal "talvez não seria tão confortável" de ler.
- **Em interfaces densas, a organização vem de linhas e cards.** O [[wiki/entities/meta|Facebook]] separa o feed em cards; dentro do card, as informações ficam mais juntas, e uma linha de ponta a ponta separa a seção de conteúdo da seção de interação. O G1 usa linhas e espaçamento do mesmo jeito.
- **Conteúdo simples permite espaçamentos maiores**, como o site do autor.

A regra de base continua a da [[wiki/concepts/lei-da-proximidade-gestalt]]: o que muda com a densidade é a escala dos vãos e quanto a linha precisa ajudar o espaço. Ver também [[wiki/concepts/espaco-em-branco]] ("a linha entra quando o espaço não basta").

## Densidade x sobrecarga

Densidade não é [[wiki/concepts/sobrecarga-de-informacao|sobrecarga]]. Um feed denso bem organizado se lê com conforto; a sobrecarga é informação sem hierarquia nem agrupamento, como a tela de ERP que "não conduz para nada".

## Olhar de dev

`[skill: ux-ui-mentor]` Em design systems, densidade vira **modo do sistema**: 2 ou 3 modos (compacto, padrão, confortável) que mudam altura de controle, padding e espaçamento, mas não a tipografia mínima legível nem a área de toque. Implementação típica: tokens resolvidos por escopo (`[data-density="compact"] { --control-h: 32px; }`) e, em telas touch, voltar a 44 px de altura mínima. Usuários operacionais de B2B (conciliação, cadastros em lote) costumam preferir alta densidade.

`[skill: ux-ui-mentor]` Contraponto: design de iniciante tende a ser denso demais; na dúvida, mais espaço. A aula e a skill não brigam: densidade alta é escolha para conteúdo lido todo dia, não ponto de partida.

## Relação com outros conceitos

- [[wiki/concepts/escala-de-espacamento]] — a mesma escala, aplicada com valores menores ou maiores conforme o modo.
- [[wiki/concepts/hierarquia-visual]] — em telas densas, o espaço sozinho não cria hierarquia; cards e linhas ajudam.

## Key Sources

- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — espaço vs. meio: Facebook e G1 densos com cards e linhas; site simples com espaços grandes
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — prática da aula de espaço vs. meio no Figma (wireframe pouco denso, vãos de até 128)
