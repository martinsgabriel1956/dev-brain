---
type: concept
title: "Pseudo-classe CSS"
aliases: ["pseudo-classe", "pseudo-class", "pseudo-classes CSS", ":hover", ":focus", ":checked", ":nth-child", ":root"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, frontend, seletores-css, pseudo-classe, estados, formularios]
skill: tech-mentor-frontend
status: draft
---

# Pseudo-classe CSS

Palavra-chave com **um dois-pontos** que se junta a um [[wiki/concepts/seletores-css|seletor]] para pegar elementos por **estado** (o mouse em cima, marcado, em foco) ou por **posição** na árvore (primeiro filho, linha par), sem classe extra no HTML. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes

A aula [[wiki/sources/seletores-e-pseudo-elements-css]] as apresenta todas como "pseudo-elements"; a wiki separa: ver [[wiki/concepts/pseudo-elemento-css]].

## Grupos da aula

- **Interação:** `:hover` ("o efeito que eu mais utilizo"), `:active`, `:focus`, `:visited`.
- **Formulário:** `:checked` (radio e checkbox), `:disabled`, `:enabled`, `:in-range`, `:out-of-range`, `:valid`, `:invalid`. "Muito importante para [...] aprender a fazer o estilo de formulários."
- **Estrutura:** `:first-child`, `:last-child`, `:only-child`, `:first-of-type`, `:last-of-type`, `:nth-child(even | odd | n)`, `:nth-last-child(n)`, `:empty`.
- **Lógica:** `:not(p)` (só no slide).
- **Documento:** `:root`, onde se declaram as variáveis.

`[external]` `even` = pares, `odd` = ímpares (a aula hesita). `:first-child` é relativo ao pai: `p:first-child` é o `p` que é o primeiro filho, não o primeiro filho de um `p`. `:root` casa com `<html>`; custom properties declaradas ali valem na página toda ([[wiki/concepts/design-tokens]]).

## `:checked` como estado sem JavaScript

Násser usa `:checked` num hack de menu hambúrguer animado: um checkbox escondido guarda o estado aberto/fechado e o CSS reage a ele ([[wiki/sources/seletores-e-pseudo-elements-css]]). `[external]` O padrão funciona, mas o checkbox precisa de label e de teclado acessíveis; hoje `:has()` permite estilizar o pai a partir do estado do filho.

## Estados de design viram pseudo-classes

Os estados do [[wiki/concepts/style-guide]] (normal, hover, focus, disabled) chegam ao código como pseudo-classes; a aula de style guide chamava hover de pseudo-element ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). Ver [[wiki/concepts/maquina-de-estados-ui]], [[wiki/concepts/affordance]] e [[wiki/concepts/botoes-em-interfaces]].

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — lista do W3Schools: checked, disabled, focus, hover, nth-child, root
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — `card-hover` e estados de input no style guide
