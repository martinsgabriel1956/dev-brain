---
type: concept
title: "Formulário HTML (form, fieldset, label, input, select)"
aliases: ["form", "formulário", "fieldset", "legend", "label", "input", "select", "option", "input hidden", "button submit"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 5
tags: [html, formulario-html, acessibilidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Formulário HTML (form, fieldset, label, input, select)

O `form` agrupa campos e os envia (`action`, `method`) ao clicar num `button type="submit"`. Cada campo vai no envio pelo seu `name`. `fieldset` + `legend` agrupam campos relacionados com um título; `label` dá nome ao campo; `input` tem tipos (`text`, `number`, `hidden`...); `select` + `option` oferecem uma lista. Ver [[wiki/concepts/html-semantico]] e [[wiki/concepts/acessibilidade]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] monta o cadastro de ponto de coleta do Ecoleta:

- `form` > `h1` + dois `fieldset` com `legend` > `h2` (dados da entidade; itens de coleta) + `button type="submit"`. `fieldset` em vez de `div` "para uma ideia mais semântica".
- `div.field` (label + input) e `div.field-group` (dois campos lado a lado).
- `name` é o que leva o valor: "vai servir pra mim mais tarde, pra eu pegar o valor que tem nesse input". O envio sem `method` mostra os pares na URL.
- `type="number"` só aceita dígitos; descartado em "Número/Complemento" para aceitar "bloco, apartamento".
- `select` de cidade começa `disabled`; o JavaScript o habilita depois de carregar as opções.
- `input type="hidden" name="state"` guarda o nome do estado, porque o select envia o id.

## Precisões

- O `for` do `label` casa com o `id` do campo, não com o `name`. A aula usa `for="name"` com `name="name"` e sem `id`, e o label fica solto `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label). Alternativa: pôr o input dentro do label.
- Sem `method`, o padrão é GET; dados sensíveis vão com POST.
- `hidden` não é segredo: o valor aparece no HTML e no envio.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] completa o formulário do dia 2:
- **`required`** nos inputs e selects: o navegador bloqueia o envio com "por favor, preencha esse campo". "Não é uma tag desculpa é um atributo."
- **Itens de coleta:** um `input type="hidden" name="items"` recebe os itens.
- **Valor da cidade:** o select manda o nome em vez do id.

No modal, o form de busca ganha `action="/search-results"`. O `label for="search"` repete o problema do dia 2: aponta para um input sem `id`.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], o formulário do Ecoleta ganha `method="post"` e `action="/savepoint"`, e cada `name` vira uma chave de `req.body`. Os `data-id` dos itens passam a ser os próprios nomes ("Lâmpadas"...) para gravar texto no banco. [[wiki/entities/mayk-brito|Mayk Brito]] mostra antes a versão GET, com os campos em query string.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: cadastro do Ecoleta, fieldset, name, number, disabled, hidden
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: `form` e `input` de tipo texto ou botão, apresentados no tour de tags
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `input[type="text"]` muda só o input de texto; `input:button`/`input:text` do Emmet
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: required, hidden de itens, action; label for sem id de novo
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: method post, action /savepoint, name → req.body
