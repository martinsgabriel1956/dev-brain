---
type: source
title: "Seletores e pseudo-elements em CSS: menos classes, combinadores, atributos e estados (W3Schools Try CSS Selector)"
aliases: ["aula de seletores CSS", "seletores e pseudo-elements", "FrontPUSH aula 05 seletores", "pseudo-elements CSS aula"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, frontend, seletores-css, pseudo-classe, pseudo-elemento, combinadores, seletor-de-atributo, formularios, hover, nth-child, root, w3schools]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/seletores-e-pseudo-elements-css.md"
source_url: "https://www.w3schools.com/cssref/trysel.php"
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Seletores e pseudo-elements em CSS: menos classes, combinadores, atributos e estados

## TL;DR

Aula 05 da pasta "FrontPush" (slides "Básico CSS" com o logo "FE"; autoria de [[wiki/entities/nasser|Násser]] inferida: ele se chama pelo nome nas perguntas imaginadas do aluno). Tese: no [[wiki/concepts/css]] a meta é criar **o mínimo de classes**, e [[wiki/concepts/seletores-css|seletores]] bem aplicados evitam a classe criada "só por causa de um elemento". A aula percorre o **Try CSS Selector** do [[wiki/entities/w3schools]] (que o autor chama de "artigo no W3C"), clicando em cada seletor para ver o que ele pega: classe, ID, agrupamento com vírgula, descendente (espaço), filho direto, adjacente (`+`), universal (`*`), elemento com classe e atributo (`[id=my-Address]`, base para estilizar formulários). Depois, sob o nome "pseudo-elements", vêm estados e posições: `:checked` (hack do menu hambúrguer animado), `:disabled`, `:enabled`, `:empty`, `:focus`, `:first-child`, `::first-letter`, `::first-line`, `:hover` ("o efeito que eu mais utilizo"), `:in-range`, `:invalid`, `:nth-child(even/odd)`, `:only-child` e `:root` para variáveis. Quase tudo isso é [[wiki/concepts/pseudo-classe-css|pseudo-classe]], não [[wiki/concepts/pseudo-elemento-css|pseudo-elemento]] `[external]`.

## Key Claims

### Por que seletores

- **Menos classes = código consistente e organizado.** "A gente tem que tentar ser o mais otimizado possível, ou seja, criar a menor quantidade de classes possíveis." Em layouts complexos a tentação é criar uma classe por exceção ("um estilinho diferente") e logo "você nem entende aquele tanto de classes".
- **Seletores "facilitam a nossa vida"** e os pseudo-elements servem "para podermos definir o estado dos elementos".

### Seletores (slide "Outros Seletores" + W3Schools)

- **Classe:** "ponto intro" seleciona onde a classe `intro` está aplicada.
- **ID:** "hashtag lastname" pega só a tag com aquele ID (no exemplo do W3Schools, `<span id="Lastname">`).
- **Agrupamento com vírgula:** `.intro, #Lastname` aplica o mesmo estilo aos dois; `h1, p` pega todos os `h1` e todos os `p` da página. O slide: "selecionar vários para o mesmo estilo".
- **Descendente (espaço):** `div p` = "apenas os elementos parágrafos que estão dentro de uma tag div", em qualquer nível. Slide: `p a`, "todo `<a>` que está dentro de uma tag `<p>`".
- **Filho direto:** `div > p` (o autor diz "div traço p") "força que seja filho direto"; o neto não recebe o estilo. Slide: `ul > li`.
- **Adjacente:** `ul + p` é o parágrafo que vem logo depois de um `ul`; "é simplesmente a tag que antecede ele na ordem". Slide: `h1 + p`.
- **Universal:** `*` aplica a todos os elementos da página.
- **Elemento com classe:** `p.intro` aplica "somente àquela que está ligada ao parágrafo".
- **Atributo:** "formatar formulários, eles são baseados nisso". Pelo ID dá para usar `#`, mas em um input de texto (background, título, placeholder) "você não consegue fazer como ID" e precisa do seletor de atributo. Slide: `div[attribute="value"]`, "seletor de atribuição".
- O próprio autor manda ler a descrição em inglês do W3Schools: "está bem mais completo do que a minha apresentação".

### Pseudo-elements (como a aula os chama)

- **"Pseudo" vem de falso:** "é meio que um elemento ou um estado dentro de um outro".
- **`:checked`:** estado de radio e checkbox marcados; dispara estilos quando algo está marcado. O autor tem um vídeo no YouTube com um hack de **menu hambúrguer animado** feito com ele.
- **Formulários:** campos desabilitados (`:disabled`), habilitados (`:enabled`), vazios (`:empty`) e em foco (`:focus`, "pronto para poder receber um texto"); "muito importante para [...] aprender a fazer o estilo de formulários".
- **Estrutura:** `:first-child` (no exemplo, a `div.intro` tem três filhos e só o primeiro é estilizado), `:last-child`, `:first-of-type`, `:last-of-type`, `:only-child`.
- **Partes do texto:** `::first-letter` e `::first-line`.
- **`:hover`:** "de disparado é o efeito que a gente mais utiliza, que eu mais utilizo".
- **Validação:** `:in-range`, `:out-of-range`, `:invalid`, `:valid`.
- **`:nth-child`:** seleciona um elemento específico; `even` e `odd` para as linhas de uma tabela; `nth-child(1)` conta do começo e `nth-last-child(1)` do fim.
- **`:root`:** "é quando a gente está definindo variáveis".
- Slide extra (não falado): `a:active`, `a:visited`, `:not(p)`.

## Entities

- [[wiki/entities/nasser]]: autor inferido. "Násser, mas espera aí..." e "Násser, o que significa..." nas falas do aluno imaginado; "um vídeo do meu YouTube"; pasta "FrontPush".
- [[wiki/entities/frontpush]]: curso da pasta da transcrição; slides "Básico CSS".
- [[wiki/entities/w3schools]] (novo): o Try CSS Selector usado na aula (https://www.w3schools.com/cssref/trysel.php).
- [[wiki/entities/w3c]]: citado por engano ("um artigo no W3C"); a página é do W3Schools, que não tem ligação com o W3C.

## Concepts

- [[wiki/concepts/seletores-css]] (novo)
- [[wiki/concepts/pseudo-classe-css]] (novo)
- [[wiki/concepts/pseudo-elemento-css]] (novo)
- [[wiki/concepts/css]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/cssom]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/maquina-de-estados-ui]]
- [[wiki/concepts/design-tokens]]
- [[wiki/concepts/botoes-em-interfaces]]

## Tensões com a wiki

- **Pseudo-classe ≠ pseudo-elemento.** `[external]` Pseudo-classe (`:`) seleciona elementos por estado ou posição (`:hover`, `:checked`, `:nth-child`); pseudo-elemento (`::`) estiliza uma parte do elemento ou cria uma caixa que não está no HTML (`::first-letter`, `::first-line`, `::before`, `::placeholder`): https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes e https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements. Da lista da aula, só `first-letter` e `first-line` são pseudo-elementos. A mesma troca já aparecia na aula de style guide ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]); ver [[wiki/concepts/css]].
- **"Sufixo pseudo":** é prefixo.
- **"Artigo no W3C":** a página é do W3Schools, empresa privada sem relação com o W3C, que publica as especificações.
- **Slide com erros de grafia CSS:** `:p::first-line` e `:p::first-letter` têm dois-pontos sobrando (o certo é `p::first-line`); "seletor de atribuição" é seletor de **atributo**; `h1 + p` não é "o `<p>` que tem ao lado um `<h1>`", é o `<p>` que vem **imediatamente depois** de um `<h1>` no mesmo pai `[external]`.
- **`even` e `odd` trocados na fala.** O autor hesita ("even é o quê? Ímpar, odd ou é par"). `[external]` `even` = pares (2, 4, 6), `odd` = ímpares (1, 3, 5): https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child.
- **`p` dentro de `p` não existe.** O exemplo do neto ("se eu colocar um p dentro do p") não funciona no HTML: o parser fecha o primeiro `<p>` ao abrir o segundo, e os dois viram irmãos `[external]` (https://html.spec.whatwg.org/multipage/grouping-content.html#the-p-element). O exemplo correto do filho direto é um `<p>` dentro de uma `<section>` dentro da `div`. Ver [[wiki/concepts/dom]].
- **`:first-child` é posição relativa ao pai.** `p:first-child` pega o `<p>` que é o primeiro filho do seu pai, não "o primeiro filho do `p`". No exemplo do W3Schools o resultado coincide com a fala (o primeiro `<p>` da `div.intro`), mas `.intro:first-child` e `.intro :first-child` são seletores diferentes `[external]`.
- **Placeholder não é atributo selecionável para estilo.** O seletor de atributo pega o input (`input[type="text"]`); o texto do placeholder se estiliza com o pseudo-elemento `::placeholder` `[external]`.
- **`:root` não define variáveis, só é o lugar costumeiro.** `:root` casa com `<html>`; as custom properties declaradas ali herdam para a página toda `[external]`. A skill gera tokens em `:root { --color-brand-50: ... }` `[skill: tech-mentor-frontend]`. Ver [[wiki/concepts/design-tokens]].
- **Menos classes x convenções de classe.** A aula prega seletores para criar menos classes. `[skill: tech-mentor-frontend]` BEM vai pelo caminho contrário: uma classe explícita por bloco, elemento e modificador (`.card__title--truncated`), para manter a especificidade plana e evitar conflitos em CSS global; seletores longos por estrutura do DOM quebram quando o HTML muda. As duas posições cabem: combinadores e pseudo-classes para estados e padrões estruturais (zebra de tabela, `:focus`), classes para componentes. Inferência do agente.

## Open Questions

- "Vai flodando": provável "floodando" (inundando de classes); mantido literal no raw.
- "A tag b está dentro da tag p": a demonstração atual do W3Schools usa `<span>`; a versão da época da gravação pode ter sido outra.
- O vídeo do menu hambúrguer com `:checked` não está na wiki.
- Slides com logo "FE"; a relação com a edição "W7" das aulas de UI não está clara.
- `date_published` vazio.

## Raw Quotes

> "A gente tem que tentar ser o mais otimizado possível, ou seja, criar a menor quantidade de classes possíveis."

> "Esse sufixo pseudo vem de falso, então é um falso elemento, é meio que um elemento ou um estado dentro de um outro."

> "De disparado é o efeito que a gente mais utiliza, que eu mais utilizo."
## Ver também

- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: aula irmã do módulo de front-end: os mesmos combinadores na prática, `nth-child` e `::before`/`::after` (setinha do botão do FrontPUSH); separa melhor pseudo-element de pseudo-classe
