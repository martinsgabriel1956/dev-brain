---
type: concept
title: "Feedback do Sistema"
aliases: ["feedback em UI", "visibilidade do status do sistema", "system feedback", "feedback de interface"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 5
tags: [ui, ux, ui-design, feedback, estados, heuristicas-nielsen, acessibilidade]
skill: ux-ui-mentor
status: stub
---

# Feedback do Sistema

A interface sempre responde ao usuário sobre o que aconteceu e onde ele está: "isso aqui deu certo", "o e-mail foi enviado", "isso aqui deu erro", "você está em tal passo", "só falta isso para concluir". Inclui caixas de diálogo que mostram a situação dele no sistema, se falta algo ou se há pendência ([[wiki/sources/elementos-da-interface-introducao-ui-design]]).

Não confundir com feedback entre pessoas ([[wiki/concepts/feedback-continuo-diario]]) nem com [[wiki/concepts/loop-de-feedback-rapido]] de desenvolvimento.

## Onde aparece

- Uma das seis melhores práticas de [[wiki/concepts/ui-design]] em [[wiki/sources/elementos-da-interface-introducao-ui-design]], ao lado de simplicidade, consistência, hierarquia, cor e contraste e patterns.
- Nos slides de [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], sob acessibilidade, junto com "uso de patterns".

## Tipos citados na aula

| Tipo | Exemplo da aula |
|---|---|
| Sucesso / confirmação | "Deu certo", "o e-mail foi enviado" |
| Erro | "Deu erro, cuidado com isso" |
| Progresso | "Você está em tal passo", "quase concluindo" |
| Pendência | "Só falta isso para concluir" |

`[skill: ux-ui-mentor]` É a heurística 1 de Nielsen, visibilidade do status do sistema: o usuário sempre sabe o que está acontecendo. Violação clássica: botão "Confirmar pedido" que não reage enquanto processa e parece travado. A skill lista oito estados que toda feature precisa projetar (empty, loading, partial, populated, error, validation error, success, offline), e feedback de estado nunca deve usar só cor: cor + ícone + texto.

## Por que importa

Sem resposta, o usuário repete a ação, desiste ou não sabe se concluiu. Para quem tem ansiedade ou é idoso, a confirmação clara pesa mais `[skill: ux-ui-mentor]`. Ver [[wiki/concepts/contexto-do-usuario]] e [[wiki/concepts/usuarios-como-agentes-do-caos]].

## Hover em botões e links

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]], o hover é feedback de interação: o botão cresce um pouco, ganha sombra da cor dele (no slide, `rgba(252,189,56,0.8)`) ou muda a opacidade; no [[wiki/entities/sketch]], o link clareia. "O objetivo do movimento é melhorar a interatividade." `[skill: ux-ui-mentor]` Micro-hover dura 100–150 ms e precisa de par: focus visível e estado active para toque. Ver [[wiki/concepts/botoes-em-interfaces]].

## Sombra como hover

A aula prática constrói o hover como uma [[wiki/concepts/sombra-em-interfaces|sombra]] suave na cor da marca e manda "deixar isso muito bem claro no meu style guide" ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]). "A grande questão do momento é saber aplicar o efeito hover e como a gente exporta depois isso para o CSS."

## Estados de input no style guide

Os inputs têm estados próprios: hover (o placeholder "acende"), focus (borda cinza), sucesso (verde), erro (borda vermelha, ícone e mensagem no lugar certo) e warning. São "respostas ao usuário", e o style guide padroniza "o que vai acontecer, aonde e por quê" ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Key Sources

- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — definição e exemplos
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — feedback listado sob acessibilidade (slide)
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — hover: crescer, sombra da cor do botão, opacidade
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — hover como sombra suave na cor da marca, documentado no style guide
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — estados de input: hover, focus, sucesso, erro, warning
