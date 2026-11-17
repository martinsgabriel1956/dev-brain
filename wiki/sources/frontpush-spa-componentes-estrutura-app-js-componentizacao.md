---
type: source
title: "SPA: a estrutura SPA e a componentização (FrontPUSH)"
aliases: ["FrontPUSH SPA Componentes", "módulo de ReactJS, aula 05", "estrutura SPA e componentes"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 0
tags: [spa, componentizacao, componentes, app-js, props, estado, encapsulamento, reuso, client-side-routing, react, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-spa-componentes-estrutura-app-js-componentizacao.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-17
---

# SPA: a estrutura SPA e a componentização (FrontPUSH)

## TL;DR

Aula 05 do módulo de ReactJS do [[wiki/entities/frontpush|FrontPUSH]], cerca de 6,5 min. Segunda de duas aulas sobre [[wiki/concepts/single-page-application|SPA]], continua a [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes|aula 04]]. [[wiki/entities/nasser|Násser]] (autoria pela sequência; não diz o nome) apresenta o slide "Estrutura SPA" e "Componentes".

- **Estrutura SPA** (slide): "Aplicação que carrega uma única página HTML e quaisquer interações com páginas subsequentes não necessitam outras requisições de páginas completas. Ou seja, a página não é recarregada." As rotas trocam no cliente ([[wiki/concepts/client-side-routing]]); o servidor manda "só o que de fato muda", "computacionalmente [...] bem mais barato".
- **Esquema:** `App.js` como "componente maior" ("se ligam nesse nome") com `header.js`, `sidebar.js`, `content.js` e `footer.js`, cada um com `.css`, `<html>` e `index.js` ([[wiki/concepts/componentizacao]]).
- **KaBuM de novo:** trocar de produto muda só sidebar e content; header e footer ficam.
- **Componentes** (slide): organização do código; melhor performance; "um componente não interfere na lógica do outro componente"; "criamos componentes encapsulados que gerenciam seu próprio estado" ([[wiki/concepts/encapsulamento]], [[wiki/concepts/estado]]); aninhamento; compartilhamento.
- **Botão com parâmetros:** passar destino ou cor "como se ele fosse uma função" e reaproveitar em vários lugares ([[wiki/concepts/props-react]]).
- **Tudo junto:** componentes "já torna[m] possível o conceito de uma SPA", e isso "só é possível porque" a comunicação é "um JSON com API fornecendo múltiplos clientes".

## Key Claims

### Estrutura SPA

- "Uma aplicação que carrega uma única página HTML, por isso que é single, de único, de sozinho." As "páginas subsequentes, as rotas que a gente cria [...] não necessita[m] outra requisição de outra página completa."
- No método tradicional, o produto 10 e depois o produto 12 refazem todo o processo, "consumir tudo de novo, sendo que o que muda de uma página para outra é somente a informação". Na SPA, "ele me manda só a informação, então computacionalmente falando é bem mais barato".

### Componentização

- "Todos os meus componentes da página não precisam ser recarregados, só aquele componente, aquele miolo que de fato vai mostrar o meu produto."
- "Um componente maior chamado App.js e se ligam nesse nome, porque é com esse nome que a gente vai construir as próximas páginas do React." Dentro dele, "um componente específico por header [...] por sidebar [...] por content e outro por footer".
- KaBuM: "só iria mudar dois componentes, que é a sidebar carregando elementos e filtros específicos daquele produto e o próprio content [...] o header e o footer eu não preciso mexer, então a página não é completamente recarregada".
- "Cada bloquinho desse vai ter o seu respectivo JavaScript, o seu respectivo HTML e o seu respectivo CSS, ou seja, cada componente não interfere na lógica um do outro, então eu posso muito bem tirar um, atualizar e plotar novamente."
- "Isso faz com que eu tenha melhor performance, porque eu estou carregando somente o que é realmente necessário."
- "A gente consegue criar componentes que são encapsulados e que gerenciam o seu próprio estado."
- Aninhamento e reuso: "colocar um componente dentro do outro"; um botão recebe "um parâmetro [...] como se ele fosse uma função, para onde é que você vai redirecionar quando clicar, ou então qual é a cor desse botão" e é renderizado "em várias partes".

### Os conceitos conversam

- "A ideia de ser componentizado e as características dos componentes já torna possível o conceito de uma SPA e isso tudo só é possível porque o método de comunicação do back-end e do front-end é feito por meio de um JSON com API fornecendo múltiplos clientes [...] eu não consigo desvencilhar um conceito do outro."
- Os conceitos serão aplicados "nas próximas aulas".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; módulo de ReactJS.
- [[wiki/entities/react]]: onde o `App.js` vai aparecer.
- [[wiki/entities/create-react-app]]: origem da convenção `App.js` (inferência; a aula não cita).

## Concepts

- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/client-side-routing]]
- [[wiki/concepts/componentizacao]]
- [[wiki/concepts/props-react]]
- [[wiki/concepts/estado]]
- [[wiki/concepts/levantamento-de-estado]]
- [[wiki/concepts/encapsulamento]]
- [[wiki/concepts/separation-of-concerns]]
- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/code-splitting]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/json]]

## Precisões e tensões com a wiki

- **A definição de SPA está certa, e é a primeira vez que o curso menciona as rotas.** Uma página HTML; as rotas trocam no cliente (History API), sem pedir outra página. Faltou dizer quem faz isso: no React, uma biblioteca como o [[wiki/entities/react-router]] ([[wiki/concepts/client-side-routing]]). "Mais barato" vale para as navegações seguintes; a primeira visita baixa o bundle inteiro (ver a [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes|aula 04]]).
- **"Encapsulados que gerenciam seu próprio estado" é a frase da antiga home do React.** "Build encapsulated components that manage their own state, then compose them to make complex UIs" (https://legacy.reactjs.org/) `[external]`. O slide a traduz quase literalmente. Confiança alta.
- **Mas o estado nem sempre fica no próprio componente.** Quando dois componentes precisam do mesmo dado (o filtro da sidebar e a lista do content, no exemplo da KaBuM), o estado sobe para o pai comum e desce por props ([[wiki/concepts/levantamento-de-estado]]) ou vai para Context ou um store. No exemplo dele, quem sabe "qual produto" é o `App` ou a rota, não o `content`. "Não interfere na lógica do outro" vale para o estado local, não para o compartilhado. `[skill: tech-mentor-frontend]`
- **Componentizar organiza; não é o que dá performance.** Todo o código dos componentes vai no bundle (salvo [[wiki/concepts/code-splitting]] com `lazy`). O que evita mexer no header é a [[wiki/concepts/reconciliacao]]: quando o estado muda, o React re-renderiza o componente dono do estado e os filhos, compara e só toca o DOM que mudou. Se o estado do produto ficar no `App`, header e footer também re-renderizam (sem mudar o DOM), a menos que se use `memo` ou o React Compiler. `[skill: tech-mentor-frontend]` Confiança alta.
- **No React, um componente não tem "seu HTML, seu CSS e seu JS" separados.** É uma função JavaScript que devolve [[wiki/concepts/jsx|JSX]]; o "HTML" mora dentro do JS. O CSS importado num componente é **global** por padrão e vaza para os outros; isolar exige CSS Modules, styled-components ou similar. O slide (`.css`, `<html>`, `index.js` por bloco) se parece mais com Web Components ou com o single-file component do [[wiki/entities/vue]].
- **Separar por componente, não por tecnologia.** O ponto de fundo da aula é a virada que o React provocou: em vez de um arquivo de HTML, um de CSS e um de JS para a página toda, um pacote por pedaço da tela. Pete Hunt defendeu isso em 2013 ("Rethinking Best Practices") como separação de responsabilidades por componente, não por linguagem ([[wiki/concepts/separation-of-concerns]]). `[external]` Confiança média-alta.
- **"Como se ele fosse uma função": no React é literal.** Componentes de função recebem as props como argumento ([[wiki/concepts/props-react]]). Um botão que recebe "para onde redirecionar" costuma ser um link (`<a>`/`<Link>`), não um `<button>`, por acessibilidade.
- **A ligação "componentes → SPA → JSON" é forte demais.** São ideias independentes que combinam bem. SPAs existiram antes dos componentes (Backbone com templates); componentes existem fora de SPA (React no servidor, Blade, ViewComponent, Web Components); e uma SPA pode falar XML, GraphQL ou RPC. Ele mesmo admite que pegou "meio que" um esquemático.
- **`App.js` é convenção, não regra.** Veio do create-react-app; com Vite o arquivo nasce como `App.jsx`/`App.tsx`, e em Next.js o "componente maior" é o layout da rota. O nome não tem significado para o React.

## Open Questions

- Que estrutura de pastas o curso vai usar? O slide sugere `header.js` + `.css` + `index.js` por bloco.
- Qual biblioteca de rotas entra (React Router, citado na aula 03)?
- Onde ficará o estado do produto no projeto: no `App`, num Context, na URL?

## Raw quotes

- "por isso que é single, de único, de sozinho"
- "se ligam nesse nome, porque é com esse nome que a gente vai construir as próximas páginas do React"
- "como se ele fosse uma função"
