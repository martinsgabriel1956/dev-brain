---
type: concept
title: "Modal (janela modal)"
aliases: ["janela modal", "modal dialog", "dialog", "<dialog>"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [ui, html, css, javascript, acessibilidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Modal (janela modal)

Uma janela que abre sobre a página sem sair dela e bloqueia a interação com o resto até ser fechada. Para ser acessível, o modal precisa de cinco coisas:
- `role="dialog"` com `aria-modal` e um rótulo;
- mover o foco para dentro ao abrir e prendê-lo ali;
- fechar com Esc;
- devolver o foco ao botão que o abriu;
- deixar o resto da página `inert`.

`[skill: tech-mentor-frontend]` O elemento `<dialog>` com `showModal()` já entrega tudo isso: a camada superior (sem disputa de `z-index`), o `::backdrop` estilizável, o foco e o Esc. É preferível a uma `div` montada à mão. A Popover API cobre os casos sem bloqueio. Ver [[wiki/concepts/acessibilidade]].

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] define modal como "uma janela [...] dentro dessa própria página sem sair da página". Ele monta o da busca de pontos de coleta assim:
- **Estrutura:** `div#modal` em `position: fixed`, com 100vw × 100vh e fundo `#0e0a14` mais alfa em hexadecimal.
- **Abrir e fechar:** a classe `hide` (`display: none`), trocada com [[wiki/concepts/classlist-javascript|classList]].
- **Fechar:** o "Fechar" é um `<a href="#">` com ícone de fundo e o texto em `font-size: 0.01px`.

Faltam foco, Esc e semântica, como a fonte detalha nas tensões. Ver [[wiki/concepts/css-position]].

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: modal de busca com div fixa, classe `hide` e JavaScript; sem foco nem Esc
