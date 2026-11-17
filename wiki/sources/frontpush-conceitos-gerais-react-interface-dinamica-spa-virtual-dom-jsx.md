---
type: source
title: "Conceitos gerais do React: interface dinâmica, SPA, Virtual DOM e JSX (FrontPUSH)"
aliases: ["FrontPUSH Conceitos Gerais React", "módulo de ReactJS, aula 03", "React: biblioteca ou framework?"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 0
tags: [react, react-native, spa, virtual-dom, jsx, babel, webpack, declarativo, componentes, biblioteca, framework, ecossistema, site-estatico, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-17
---

# Conceitos gerais do React (FrontPUSH)

## TL;DR

Aula 03 do módulo de ReactJS do [[wiki/entities/frontpush|FrontPUSH]], cerca de 14 min, teórica, com o slide "Conceitos gerais / React.js" e demonstração no site da KaBuM. [[wiki/entities/nasser|Násser]] (diz o nome: "o que é, Násser?") apresenta o [[wiki/entities/react|React]] por oito tópicos do slide.

- **Origem:** biblioteca JS do Facebook ([[wiki/entities/meta]]), "por volta de 2013, 2014". A interface do Facebook motiva: chat e curtidas atualizam "sem precisar carregar a tela inteira".
- **Interface dinâmica × estática:** dinâmica não é ter motion (GSAP); é a página "reconstruída de maneira diferente dependendo da rota", com JavaScript ou outra linguagem por trás. Estática é "um site com HTML e CSS só" ([[wiki/concepts/site-estatico-vs-dinamico]]).
- **Exemplo KaBuM:** a página da TV e a do cooler têm a mesma estrutura com dados diferentes. Com HTML e CSS puro seriam "quantas milhões de páginas".
- **React.js e React Native:** web e mobile, "mesmos fundamentos" ([[wiki/entities/react-native]]).
- **Biblioteca ou framework?** "React.js" é a biblioteca; "React", com o ecossistema de pacotes npm ([[wiki/entities/react-router|react-router]], styled-components, [[wiki/entities/axios]], Formik), "pode ser sim chamado de framework" ([[wiki/concepts/framework-web]]).
- **SPA:** [[wiki/concepts/single-page-application|single-page application]] com "abordagem declarativa: atualiza apenas os componentes necessários" ([[wiki/concepts/ui-declarativa]], [[wiki/concepts/componentizacao]]), "maior performance" e [[wiki/concepts/virtual-dom|Virtual DOM]], uma "cópia virtual" para comparar "as reais modificações antes de [...] a renderização" ([[wiki/concepts/reconciliacao]]).
- **Tudo é o JS que faz:** HTML e CSS viram "uma sintaxe que parece muito com os dois", passada ao JavaScript; a estrutura fica "toda em páginas .js" ([[wiki/concepts/criacao-de-elementos-dom]]).
- **Babel e Webpack:** recarregar a página ao detectar mudança e transpilar código novo para antigo, por compatibilidade entre browsers ([[wiki/concepts/transpilador]]).
- **JSX:** "colocando HTML dentro do JavaScript, mas que na real não é HTML" ([[wiki/concepts/jsx]]).

## Key Claims

### Por que o React existe

- "O primeiro ponto é uma biblioteca JavaScript criada pelo Facebook. Se não me engano, por volta de 2013, 2014."
- O Facebook "tem muito recurso": o chat "precisa estar atualizando de maneira independente [...] sem precisar carregar a tela inteira"; no feed, "quando eu curto um post, automaticamente para o dono daquele post vai mostrar quem curtiu em tempo real".

### Interface dinâmica e estática

- "Ao contrário do que eu já vi algumas pessoas falarem [...] que uma interface dinâmica é aquela que detém algum tipo de motion, a página sendo carregada com a biblioteca GSAP ou elementos de carregamento, e não é isso." Motion é assunto de outra seção do curso.
- "Uma interface dinâmica é aquela que [...] eu tenho várias rotas e tem como eu [...] ter uma página e ela ser reconstruída de maneira diferente dependendo da rota que eu clico [...] necessariamente são aquelas páginas que detêm de JavaScript ou uma linguagem de programação por trás."
- "O que seria uma interface estática é aquela que eu não consigo agregar a funcionalidade, ou seja, um site com HTML e CSS só."
- Demonstração na KaBuM: TV 4K (43 e 48 polegadas, preços, especificações) e depois um cooler. "Dependendo da rota que eu criei, ele recriou meio que a página [...] Eu tenho a mesma estrutura de página." Ao clicar na TV, "ele vai recarregar".
- "Será que ele fez isso com HTML e CSS puro, daria quantas milhões de páginas [...] quantos mil produtos tem na KaBuM?"

### React.js, React Native e o ecossistema

- React.js é "voltada para desenvolvimento web" e React Native "para desenvolvimento mobile"; "os fundamentos são extremamente parecidos e eles derivam de um ecossistema que é o React".
- "Se eu falar de React.js, eu estou especificando que eu estou falando da biblioteca [...] mas se eu for falar do React, propriamente dito [...] o React detém de um ecossistema [...] eu estou falando de framework." Pacotes npm de terceiros: "o react-router, o styled-components, o axios ou então o Formik para poder a gente construir formulários".
- Slide: "Se considerar o ecossistema do React, todas as ferramentas, pode ser sim chamado de framework."

### SPA, abordagem declarativa e Virtual DOM

- "O React vai utilizar uma abordagem declarativa, o que significa isso? Basicamente, ele atualiza apenas os componentes necessários." No chat do Facebook, "atualiza [...] somente o chat, o resto da sua página ele não recarrega". "Eu meio que consigo seccionar a minha página e fazer da minha página, ela baseada em componentes."
- "O React utiliza [...] o virtual DOM, que ele primeiro faz uma cópia virtual, se é que eu posso dizer assim, para poder comparar quais são as reais modificações antes de fazer propriamente dita a renderização, isso a gente ganha performance, porque ele está carregando não a página inteira, mas pequenas seções que são os componentes."

### Tudo é o JavaScript que faz

- Antes: HTML para estrutura, CSS para estilo, JavaScript para funcionalidade. "No caso aqui vocês vão perceber que o JavaScript faz tudo." Remete ao `createElement` e ao `.style` do módulo de JS ([[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]).
- "Na real não é HTML nem CSS, é uma sintaxe que parece muito com os dois, que a gente passa para o JavaScript [...] a nossa estrutura vai ser toda em páginas .js." O que foi estudado "não vai ser perdido".
- Há 10 s sem legenda (00:10:59–00:11:09) antes de "O JavaScript que faz"; o slide traz "Tudo é o JS que faz / Baseado em componentes".

### Babel, Webpack e JSX

- Babel e Webpack fazem "com que a nossa página carregue automaticamente quando percebe algum tipo de mudança" e fazem "a transpilação [...] para um código um pouquinho mais antigo para poder ter compatibilidade entre todos os browsers".
- JSX "é meio que colocando HTML dentro do JavaScript, mas que na real não é HTML, é um negócio que parece com HTML [...] na real é o JavaScript que está compilando aquilo ali tudo".

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de ReactJS.
- [[wiki/entities/react]]: assunto.
- [[wiki/entities/react-native]]: mesmo ecossistema, mobile.
- [[wiki/entities/meta]]: o Facebook como criador e caso de uso.
- [[wiki/entities/react-router]], [[wiki/entities/axios]]: pacotes do ecossistema citados.
- KaBuM, GSAP, styled-components, Formik: citados de passagem, sem página.

## Concepts

- [[wiki/concepts/site-estatico-vs-dinamico]] (criado neste ingest)
- [[wiki/concepts/ui-declarativa]] (criado neste ingest)
- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/componentizacao]]
- [[wiki/concepts/jsx]]
- [[wiki/concepts/transpilador]]
- [[wiki/concepts/framework-web]]
- [[wiki/concepts/client-side-routing]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/criacao-de-elementos-dom]]
- [[wiki/concepts/gerenciador-de-pacotes]]
- [[wiki/concepts/setup-live-reload-debug-testes]]

## Precisões e tensões com a wiki

- **A KaBuM é o contraexemplo do React.** Ele diz que, ao clicar na TV, a página "vai recarregar". Página nova a cada clique, gerada no servidor a partir de um modelo e do banco, é o site dinâmico clássico (PHP, Rails), não uma SPA. O argumento "seriam milhões de páginas em HTML puro" é verdadeiro, mas a resposta histórica a ele é o template no servidor, não o React ([[wiki/concepts/site-estatico-vs-dinamico]], [[wiki/concepts/renderizacao-ssr-vs-csr]]). A mesma confusão apareceu no e-commerce da aula 01 de JS ([[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]). Confiança alta quanto ao conceito; sobre a KaBuM em si, a stack na época da gravação não é verificável aqui. Na aula seguinte ([[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]) o próprio Násser usa a mesma página da KaBuM como exemplo do "método tradicional", com HTML montado no servidor, o que confirma a leitura.
- **"Estático" não é "sem JavaScript".** Site estático é o que serve arquivos prontos, sem gerar HTML por requisição. Um build de React (`npm run build`) é um site estático que é altamente interativo; e um site PHP sem uma linha de JS é dinâmico. A divisão dele (HTML+CSS × JS) mistura interatividade no navegador com geração no servidor. `[skill: tech-mentor-frontend]` Confiança alta.
- **Declarativo não significa "atualiza só o necessário".** Declarativo é descrever *o que* a UI deve ser para um estado (`UI = f(state)`), em vez de *como* mudar o DOM passo a passo. Atualizar só o que mudou é consequência da [[wiki/concepts/reconciliacao]] e do [[wiki/concepts/virtual-dom]], que tornam o declarativo viável. A própria home do React separa os dois ([[wiki/concepts/ui-declarativa]]). Confiança alta.
- **Virtual DOM não é "mais performance" por si.** É uma camada extra: o React compara árvores e só depois toca o DOM real. Ganha de manipulações ingênuas (reescrever `innerHTML` inteiro), mas perde de atualizações manuais bem feitas e de frameworks sem VDOM (Svelte compila para JS imperativo; Solid usa sinais). O motivo do VDOM é tornar o modelo declarativo barato o bastante, não ser o mais rápido. `[skill: tech-mentor-frontend]` ([[wiki/concepts/virtual-dom]]). Confiança alta.
- **SPA e "atualizar só o chat" são coisas diferentes.** Atualizar uma parte da página sem recarregar é [[wiki/concepts/ajax|AJAX]], que existe desde os anos 2000 e funciona em página multi-página. SPA é a aplicação inteira numa página, com rotas trocadas no cliente ([[wiki/concepts/client-side-routing]]). O slide põe declarativo, performance e Virtual DOM como subitens de SPA, mas são características do React, não da SPA.
- **Data de criação.** O React foi usado internamente no Facebook a partir de 2011 (feed) e 2012 (Instagram), e aberto em maio de 2013, na JSConf US (https://legacy.reactjs.org/blog/2013/06/05/why-react.html) `[external]`. "2013, 2014" está certo para o lançamento público. Confiança alta.
- **"Talvez tenha perdido para o Instagram".** Pelo número de usuários ativos, o Facebook continua acima do Instagram, e os dois são da [[wiki/entities/meta]] (inferência a partir de dados públicos; não verificado nesta sessão). Irrelevante para o conteúdo.
- **Biblioteca × framework: a resolução dele é boa.** Distinguir o pacote (`react`, biblioteca) do ecossistema (framework de fato) bate com o que a wiki registra. `[skill: tech-mentor-frontend]` Hoje a documentação oficial recomenda começar por um framework (Next.js, React Router v7 em modo framework, Expo), e "React Router" passou de pacote a framework. "React.js" não é nome oficial: o projeto se chama React, e `react-dom` é o renderizador web ([[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]).
- **Babel e Webpack fazem coisas diferentes, e o recarregamento é do dev server.** O Babel transpila (inclusive o JSX); o Webpack empacota módulos; o recarregamento automático vem do webpack-dev-server (hot reload / Fast Refresh) ([[wiki/concepts/setup-live-reload-debug-testes]]). Em 2020–2021 o create-react-app escondia os três. `[skill: tech-mentor-frontend]` Hoje o padrão é Vite (esbuild/Rolldown e SWC/Oxc em vez de Babel), e o create-react-app foi descontinuado em fevereiro de 2025.
- **"Acessibilidade" é compatibilidade.** "Para poder a gente ter acessibilidade e rodar a aplicação em vários browsers": no sentido de alcance, não de a11y ([[wiki/concepts/acessibilidade]]).
- **JSX não é "o JavaScript compilando".** O JSX é compilado no build (pelo Babel ou equivalente) para chamadas `React.createElement`/`jsx()`; no navegador só roda JavaScript comum ([[wiki/concepts/jsx]]).

## Open Questions

- "Tem a parte do chat mobile": provavelmente "chat online", como ele diz depois; deixado literal.
- "Hardware, civis digitais, periféricos": categorias do menu da KaBuM. "Civis digitais" não é reconhecível (talvez "TVs digitais" ou "câmeras digitais"); deixado literal.
- Os 10 s sem legenda (00:10:59–00:11:09) provavelmente cobriram a passagem para o tópico "Tudo é o JS que faz".
- "Uma seção de motion design aqui no curso": não ingerida.

## Raw quotes

- "uma interface dinâmica é aquela que detém algum tipo de motion [...] e não é isso"
- "se eu falar especificamente da React.js, é uma biblioteca"
- "na real não é HTML nem CSS, é uma sintaxe que parece muito com os dois"

## Continuação

- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: a aula 06 detalha o JSX, o Babel e o Webpack anunciados aqui.
