---
type: concept
title: "Elementos da Interface"
aliases: ["elementos de interface", "elementos da UI", "UI elements"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 10
tags: [ui, ui-design, design, elementos-da-interface, tipografia, cor, icones, botoes]
skill: ux-ui-mentor
status: stub
---

# Elementos da Interface

As peças com que se monta uma tela: espaçamentos, linhas, formas, ilustrações, imagens, iconografia, botões e links, elementos de composição, cores e tipografia. São o meio de pôr em prática as melhores práticas de [[wiki/concepts/ui-design]]: tratados de forma "harmônica", convertem em boa interação com o produto ([[wiki/sources/elementos-da-interface-introducao-ui-design]]).

## Roteiro do curso

O módulo de [[wiki/entities/nasser|Násser]] trata os elementos nesta ordem:

1. Espaçamentos, linhas e formas (com parte prática).
2. Ilustrações, imagens, iconografia, botões e links, elementos de composição.
3. Cores e tipografia, em módulos próprios por serem "tão densos".

## Dos princípios aos elementos

A cadeia que a aula monta:

| Camada | O quê | Página |
|---|---|---|
| Contexto | Objetivo, usuário, preferências, comportamento, cultura | [[wiki/concepts/objetivo-da-interface]], [[wiki/concepts/contexto-do-usuario]] |
| Princípios | Eixo, simetria, consistência, contraste, simplicidade | [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] |
| Melhores práticas | Simplicidade, consistência, hierarquia, cor e contraste, feedback, patterns | [[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/padroes-de-interface]] |
| Elementos | Espaço, linha, forma, imagem, ícone, botão, link, cor, tipo | esta página |

## Botão não é link

Um dos poucos detalhes de elemento já adiantados: o botão está ligado à ação que o usuário precisa tomar, e "link é diferente de botão" ([[wiki/sources/elementos-da-interface-introducao-ui-design]]). Ver [[wiki/concepts/affordance]].

`[skill: ux-ui-mentor]` No código, `<button>` para ação e `<a href>` para navegação. Um `<div>` clicável ou um link estilizado de botão que dispara uma ação quebra o teclado e o leitor de tela.

## Saber explicar cada elemento

O objetivo do módulo é olhar uma interface e dizer por que cada elemento está ali: cor do fundo, escala tipográfica, typeface, cinzas versus títulos em alto contraste, ícone preenchido maior para criar hierarquia. Ver [[wiki/concepts/porque-das-decisoes-de-design]].

## Primeiro elemento: espaço em branco

O item "espaçamentos e linhas" do roteiro virou a aula de [[wiki/concepts/espaco-em-branco]] (whitespace), tratada de forma mais abrangente e dividida em duas partes. A parte 1 cobre micro e macro espaço e o [[wiki/concepts/grid-de-8-pontos]] ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]).

## Segundo elemento: formas

A aula de formas trata o "formas" do roteiro: geométricas passam precisão, exatidão e racionalidade; orgânicas passam impressão, emoção e realidade; o segredo está na predominância e na [[wiki/concepts/harmonia-visual|harmonia]] com tipografia, cor e ilustração. Ver [[wiki/concepts/formas-geometricas-e-organicas]] e [[wiki/concepts/tipografia]] ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]).

## Terceiro elemento: imagens

A aula de imagens abre o item "ilustrações, imagens" do roteiro, começando pelas fotos: [[wiki/concepts/banco-de-imagens|bancos de imagens]], formatos para web ([[wiki/concepts/formato-png|PNG]], [[wiki/concepts/formato-jpeg|JPG]], [[wiki/concepts/formato-svg|SVG]], [[wiki/concepts/formato-webp|WebP]]), alta resolução e [[wiki/concepts/otimizacao-de-imagens]]. Ilustrações, contraste sobre imagem, fotos de pessoas e ponto focal ficam para a parte 2. Ver [[wiki/concepts/imagens-em-interfaces]] ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]).

## Elementos de composição

O item "elementos de composição" do roteiro: fundo que dá ambiência, alinhado à branding e em baixo contraste; também compõe [[wiki/concepts/empty-state|empty screens]]. Ver [[wiki/concepts/elementos-de-composicao]] ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]).

## Visão geral: todo elemento comunica ou interage

Uma segunda aula de abertura do módulo passa por cada elemento com sites reais: espaço e linhas no Google, retângulo e círculo como formas dominantes, [[wiki/concepts/cor-semantica|cor que informa]], hierarquia textual no G1, ícones que se entendem com o Facebook em japonês, link que se distingue do texto. O fio da aula: todo elemento existe para **comunicar ou interagir**, e uma boa interface tem propósito, simplicidade e consistência ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Espaçamento e linhas em profundidade

Primeira aula de aprofundamento da edição "W7": organização, ênfase, consistência, visualização, espaço vs. meio ([[wiki/concepts/densidade-de-informacao]]), sistema de espaçamento ([[wiki/concepts/escala-de-espacamento]]) e padding ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]).

## Botões e links em profundidade

A aula teórica de botões e links ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]) cumpre a ordem anunciada: botões guiam a jornada, com consistência, primário e secundário, [[wiki/concepts/area-clicavel|área clicável]], label objetivo, cor de contraste e hover. Ver [[wiki/concepts/botoes-em-interfaces]].

## Key Sources

- [[wiki/sources/elementos-da-interface-introducao-ui-design]]
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — espaço em branco, primeiro elemento do módulo
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — formas geométricas e orgânicas; harmonia entre elementos
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — imagens (parte 1): bancos, formatos, resolução, otimização
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — formas (parte 2): radius e consistência nos projetos do autor
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — elementos de composição, último item da linha 2 do roteiro
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — visão geral elemento a elemento; propósito, simplicidade e consistência
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — aprofundamento de espaçamento e linhas
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — formas, versão "W7": exemplos de sites reais
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — aula de botões e links (edição "W7")
