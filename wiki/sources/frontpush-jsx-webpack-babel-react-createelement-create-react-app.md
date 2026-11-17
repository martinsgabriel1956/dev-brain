---
type: source
title: "JSX, Webpack e Babel (FrontPUSH)"
aliases: ["FrontPUSH JSX & Webpack-Babel", "módulo de ReactJS, aula 06", "React.createElement e Babel REPL"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 0
tags: [jsx, react-element, createelement, babel, webpack, bundler, transpilacao, live-reload, create-react-app, compatibilidade, arrow-functions, react, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-jsx-webpack-babel-react-createelement-create-react-app.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-17
---

# JSX, Webpack e Babel (FrontPUSH)

## TL;DR

Aula 06 do módulo de ReactJS do [[wiki/entities/frontpush|FrontPUSH]], cerca de 14 min, "a última aula um pouco mais carregada de teoria". [[wiki/entities/nasser|Násser]] (autoria pela sequência; não diz o nome) explica o JSX com o REPL do Babel e o papel do Babel e do Webpack, com dois slides.

- **Componentes "tripartidos":** estrutura (HTML), estilo (CSS) e lógica (JS), tudo "dentro do JavaScript", que renderiza a SPA ([[wiki/concepts/componentizacao]]).
- **React Element** (slide): "todo elemento, toda TAG é criada com a função createElement". Como isso é verboso, o [[wiki/concepts/jsx|JSX]] deixa escrever algo que "parece com o HTML, mas não é"; o Babel o transforma em `React.createElement("div", {id: "main"}, "Meu App")` ([[wiki/concepts/virtual-node]]).
- **"JSX = Javascript + XML (HTML)"**: "o X vem de XML, que é o HTML".
- **REPL do Babel** (`babeljs.io/repl`): `function Button` devolvendo `<button id="main" class="botão">enviar</button>` vira `React.createElement("button", {id, class}, "enviar")`. Componentes com inicial maiúscula "por convenção"; a mesma coisa com `const` e com [[wiki/concepts/arrow-functions|arrow function]].
- **Babel** (slide): "o browser não entende JS atualizado"; o Babel "converte o código em uma versão mais antiga" ([[wiki/concepts/transpilador]], [[wiki/concepts/compatibilidade-entre-navegadores]]). Exemplos: arrow function e [[wiki/concepts/css-grid|CSS Grid]] quando eram novos.
- **Webpack** (slide): "ensinar ao JS como importar arquivos CSS, imagens e etc." e "Live Reload" ([[wiki/concepts/bundler]], [[wiki/concepts/setup-live-reload-debug-testes]]).
- **No curso:** [[wiki/entities/create-react-app]], "uma função que o próprio Facebook disponibiliza", porque configurar Babel e Webpack à mão arrisca "esquecer uma coisa ou outra ou deixar de otimizar".

## Key Claims

### Componentes e JavaScript

- "A nossa página é inteira feita por componentes, componentes que são tripartidos [...] a parte estrutural, que é o HTML [...] a parte de estilo, que é o CSS e [...] a parte de lógica, que é o próprio JavaScript."
- "Eu insiro o HTML dentro do JavaScript, eu insiro o CSS dentro do JavaScript, ele que vai renderizar [...] porque, afinal de contas, é isso que o browser entende."

### React Element e JSX

- "Todo elemento, toda tag é criada com a função createElement, que é própria do React [...] essa sintaxe aqui é um pouco mais verbosa." A saída foi "continuar trabalhando com o HTML e com o CSS que eu tinha lá anteriormente", "a caráter didática".
- "É mais fácil eu criar [...] uma função que retorna para mim um HTML do que criar uma função estabelecendo o objeto do React e acessando o createReactElement."
- "O JSX é algo que parece muito com o HTML [...] mas não é. Na verdade, isso aqui é o JavaScript." "O X vem de XML, que é o HTML, mais JavaScript."
- "O Babel é o responsável por transformar esse elemento criado com o JSX [...] em funções do React [...] que é o createElement." Slide: "O JSX é um JS que parece HTML, imita as tags HTML, porém, no fundo é JS. E assim o JS cria os componentes, os elementos." Exemplo no slide: `function App(){ return <div id="main"> Meu APP</div> }` → `return React.createElement("div", {id: "main"}, "Meu App");`.
- "Você pode até criar as suas próprias tags."

### No REPL do Babel

- "Todo componente que você for fazer, por convenção, sempre coloque a primeira letra dele maiúscula, vai facilitar você em entender que aquilo ali é um componente."
- "O que identifica uma função como um JSX e um componente de fato é quando eu estou retornando uma HTML nele."
- `<button>` vira `React.createElement` com "button" no 1º argumento; `id="main"` e `class="botão"` vão para "o outro argumento [...] um objeto onde [...] cada propriedade [...] se diz respeito ao atributo"; o texto "enviar" vai no 3º.
- Três sintaxes equivalentes: `function Button`, `const Button = function`, `const Button = () =>`, que "funciona da mesmíssima forma".

### Babel e Webpack

- "O browser não entende o JavaScript atualizado [...] tudo e qualquer recurso novo que é lançado, o browser demora para poder entender." Quando a arrow function saiu, o browser "vai olhar para aquilo ali e fala assim, não estou entendendo essa sintaxe". O mesmo "aconteceu [...] com o CSS Grid", que "os browsers não entendiam" no começo.
- "Não é todo mundo que tem o browser atualizado e [...] por mais que seja atualizado, não é garantido que ele [...] entenda essa sintaxe." O Babel "vai converter o código em uma versão mais antiga".
- O Webpack "ensina ao JavaScript como importar arquivos, CSS, imagens e etc." Logo depois: "Como eu vou colocar o CSS dentro do JavaScript, como eu vou colocar uma imagem [...]? Isso aí quem faz é o Babel" (lapso: o slide atribui ao Webpack).
- Live Reload: "quando a gente salvar [...] ele vai perceber que alguma alteração foi feita e vai recompilar [...] e atualizar a nossa página automaticamente".

### create-react-app

- "É possível você configurar o Babel e configurar o Webpack [...] de maneira manual [...] porém, porém, porém, quase nunca a gente vai executar esses dois configurando nós mesmos."
- create-react-app é "uma função que o próprio Facebook disponibiliza onde a gente digita esse comando e o nome da aplicação e ele já faz todo esse build". Motivo: "a gente configurar na mão [...] pode até esquecer uma coisa ou outra ou deixar de otimizar".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; módulo de ReactJS.
- [[wiki/entities/react]]: `React.createElement`.
- [[wiki/entities/create-react-app]]: ferramenta adotada no curso.
- [[wiki/entities/meta]]: o Facebook como quem "disponibiliza" o create-react-app.
- Babel, Webpack: sem página de entidade; ver [[wiki/concepts/transpilador]] e [[wiki/concepts/bundler]].

## Concepts

- [[wiki/concepts/jsx]]
- [[wiki/concepts/virtual-node]] (o React Element)
- [[wiki/concepts/transpilador]]
- [[wiki/concepts/bundler]] (criado neste ingest)
- [[wiki/concepts/compatibilidade-entre-navegadores]]
- [[wiki/concepts/setup-live-reload-debug-testes]]
- [[wiki/concepts/componentizacao]]
- [[wiki/concepts/criacao-de-elementos-dom]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/ecmascript]]
- [[wiki/concepts/css-grid]]
- [[wiki/concepts/pipeline-de-assets]]

## Precisões e tensões com a wiki

- **A inicial maiúscula não é só convenção: muda o resultado.** No JSX, tag minúscula vira string e é tratada como elemento do DOM (`<button>` → `createElement("button")`); tag maiúscula vira referência à variável (`<Button>` → `createElement(Button)`). Uma função `button` usada como `<button />` renderiza o botão nativo, não o componente (https://react.dev/learn/your-first-component) `[external]`. No exemplo da aula a função se chama `button` e não é usada como tag, então o problema não aparece. Confiança alta.
- **`class` em JSX é `className`.** O Babel não reclama (só copia a prop), mas o React avisa "Invalid DOM property `class`. Did you mean `className`?". O mesmo vale para `for` → `htmlFor`. Atributos em JSX seguem os nomes das propriedades do DOM em camelCase ([[wiki/concepts/jsx]]). Confiança alta.
- **Desde o React 17 o JSX não vira mais `React.createElement`.** A "nova transformação JSX" (outubro de 2020) compila para `_jsx("div", { id: "main", children: "Meu App" })`, importado automaticamente de `react/jsx-runtime`; por isso não é mais preciso `import React` em cada arquivo. O REPL do Babel mostra uma ou outra conforme a opção `runtime` (classic/automatic). `createElement` continua existindo e é o modelo mental certo (https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) `[external]`. Confiança alta.
- **O que o `createElement` cria é um objeto, não uma tag.** `React.createElement` devolve um React Element, um objeto leve `{type, props, ...}` que descreve o que deve existir. A tag de verdade só aparece quando o `react-dom` reconcilia e chama `document.createElement`. É o [[wiki/concepts/virtual-node]] da wiki. A frase "toda TAG é criada com a função createElement" mistura os dois ([[wiki/concepts/criacao-de-elementos-dom]]).
- **"O X vem de XML, que é o HTML".** XML e HTML são linguagens diferentes; o JSX usa uma sintaxe *parecida com XML* (toda tag precisa fechar, `<br />`), mais estrita que o HTML. "No fundo é JS" vale depois de compilado: JSX cru não é JavaScript válido e o navegador não o executa ([[wiki/concepts/jsx]]).
- **"Insiro o CSS dentro do JavaScript" não é o padrão.** O `import './App.css'` do create-react-app é processado pelo Webpack (css-loader + style-loader) e vira uma `<style>` global ou um arquivo `.css` à parte no build. CSS dentro do JS de verdade é CSS-in-JS (styled-components, citado na aula 03) ou `style={{}}` inline ([[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]).
- **Babel cuida de sintaxe; APIs novas pedem polyfill.** Transformar arrow function em `function` é transpilação. Um `Promise` ou `Array.prototype.includes` que o navegador não tem não se resolve reescrevendo sintaxe; exige polyfill (core-js). `[skill: tech-mentor-frontend]` ([[wiki/concepts/transpilador]]).
- **O exemplo do CSS Grid não é com o Babel.** Babel só mexe em JavaScript. Para CSS, o create-react-app usa PostCSS com Autoprefixer, que acrescenta prefixos (`-ms-grid`) mas não faz o Grid funcionar onde ele não existe ([[wiki/concepts/css-grid]], [[wiki/concepts/compatibilidade-entre-navegadores]]). O Grid saiu nos navegadores em 2017 e não é "do CSS3" (é o módulo CSS Grid Layout Level 1).
- **CSS e imagens: Webpack, não Babel.** Na fala ele diz "Isso aí quem faz é o Babel"; o slide, certo, diz Webpack (loaders). E o Live Reload é do webpack-dev-server; o create-react-app 4+ tem Fast Refresh, que recarrega o componente sem perder o estado ([[wiki/concepts/bundler]], [[wiki/concepts/setup-live-reload-debug-testes]]).
- **Hoje o papel do Babel encolheu.** Todos os navegadores atuais entendem ES2015+; transpilar sintaxe só importa para navegador antigo. O que ainda precisa de compilação é JSX e TypeScript, e isso hoje é feito por esbuild, SWC ou Oxc (Vite, Next.js), não pelo Babel. `[skill: tech-mentor-frontend]` O React Compiler é a exceção: roda como plugin do Babel.
- **create-react-app não é uma "função" e foi descontinuado.** É uma ferramenta de linha de comando (`npx create-react-app nome`); por baixo, o pacote `react-scripts` esconde Babel, Webpack, ESLint e Jest, com `eject` para expor a configuração. O React o descontinuou em 14/02/2025 e recomenda um framework (Next.js, React Router) ou Vite (https://react.dev/blog/2025/02/14/sunsetting-create-react-app) `[external]` ([[wiki/entities/create-react-app]]). O argumento "não configure à mão" continua válido; o que mudou foi a ferramenta.
- **"Retornar HTML" identifica um componente?** Um componente é uma função que devolve elementos React (ou `null`, texto, um array); devolver JSX é o caso comum, não a definição.

## Open Questions

- "Acessando o createReactElement": lapso por `React.createElement`; deixado literal.
- "E olhei, funciona da mesmíssima forma": provável "e olha aí"; deixado literal.
- Que versão do create-react-app (e do React) o curso vai instalar? A aula 07 deve mostrar.

## Raw quotes

- "parece com o HTML, mas não é. Na verdade, isso aqui é o JavaScript"
- "o browser não entende o JavaScript atualizado"
- "porém, porém, porém, quase nunca a gente vai executar esses dois configurando nós mesmos"
