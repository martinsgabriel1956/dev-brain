---
type: source
title: "NLW #2 com Diego Fernandes, dia 1: interface web do Proffy com React, TypeScript e Mobile First"
aliases: ["NLW 2 Diego dia 1", "Proffy React", "Proffy front-end web", "NLW 2 trilha React dia 1"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react, typescript, jsx, componentes, props, children, react-router, spa, create-react-app, react-scripts, webpack, babel, mobile-first, rem, css-grid, focus-within, pseudo-elemento, google-fonts, frontend, lang-dynamic, rocketseat, proffy, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2 com Diego Fernandes, dia 1: interface web do Proffy com React, TypeScript e Mobile First

## TL;DR

Primeira aula (cerca de 2h20) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #2]]. O projeto é o Proffy, que conecta alunos a professores, escolhido pelo Dia Nacional do Profissional da Educação (6 de agosto). Diferente da [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta|NLW #1]], em que o CSS veio pronto, aqui o HTML e o CSS são escritos do zero, em [[wiki/concepts/mobile-first]]. A aula tem três partes:

1. **Conceitos.**
   - [[wiki/entities/react]] é "uma biblioteca de construção de interfaces que visa a construção de [[wiki/concepts/single-page-application|single page applications]]". O pacote `react` é o núcleo, e cada ambiente tem o seu renderizador (`react-dom`, React Native).
   - O projeto sai do [[wiki/entities/create-react-app]] com `--template typescript` ([[wiki/entities/typescript]]). O `react-scripts` esconde [[wiki/concepts/pipeline-de-assets|Webpack e Babel]].
   - A `div#root` vazia do `index.html` é preenchida pelo `ReactDOM.render` em tempo de execução ([[wiki/concepts/renderizacao-ssr-vs-csr|CSR]]).
   - [[wiki/concepts/componentizacao|Componentes]] são "funções que retornam HTML", com nome em maiúscula, escritos em [[wiki/concepts/jsx]].
   - O estado fica para a próxima aula.
2. **Landing page.**
   - `global.css` com `:root { font-size: 60% }`, cores em [[wiki/concepts/variaveis-css|variáveis]], reset e `100vh`. Fontes Archivo e Poppins do [[wiki/entities/google-fonts]].
   - Tudo em [[wiki/concepts/unidades-de-medida-css|rem]]; a raiz sobe para 62,5% acima de 700 px.
   - Imagens por `import`, `className`, CSS por página (`styles.css`).
   - No desktop (≥ 1100 px), [[wiki/concepts/css-grid]] com `grid-template-areas`.
3. **Navegação e listagem.**
   - [[wiki/entities/react-router]] v5 (`BrowserRouter`, `Route exact`, `Link`), mostrando na aba Network que o `Link` não recarrega a página ([[wiki/concepts/client-side-routing]]).
   - O componente `PageHeader` é reaproveitado entre as telas, com a prop `title` tipada por `React.FC<PageHeaderProps>` ([[wiki/concepts/props-react]], [[wiki/concepts/generics-typescript]]) e o formulário de busca entrando por `props.children`.
   - O formulário tem o `htmlFor` e a linha de foco por `:focus-within::after` ([[wiki/concepts/pseudo-classe-css]], [[wiki/concepts/pseudo-elemento-css]]).
   - Os cards de professor viram o componente `TeacherItem`.
   - A página de cadastro ficou para o dia em que a API for conectada.

## Key Claims

### O projeto e o ambiente

- **Proffy:** landing com "dar aulas" ou "estudar"; formulário do professor (nome, foto, WhatsApp, biografia, matéria, custo da hora) com horários "infinitos" por dia da semana; listagem filtrada por matéria, dia e horário, com contato pelo WhatsApp. No mobile, favoritos guardados "no próprio dispositivo do usuário" (storage local). Layout de Thiago Luchtenberg, com versão web e mobile.
- **Mobile First** como novidade da edição: "a grande maioria das pessoas hoje em dia tá acessando os websites utilizando o próprio celular". Ver [[wiki/concepts/mobile-first]].
- **Ambiente num Notion à parte:** Node, npm e, "opcional, porém recomendável", Yarn ([[wiki/concepts/gerenciador-de-pacotes]]). Haverá uma "versão 2.0" de desafios no fim da semana.

### O que é React

- **Biblioteca de interfaces:** "tudo que a gente consegue enxergar pode ser construído com ReactJS". O exemplo é o Notion, detectado pelo React DevTools ("Production Build"), além de Twitter e Netflix.
- **SPA:** "uma aplicação que não precisa ser recarregada do zero toda vez que o usuário navega". Só muda o que difere entre telas; sidebar e header do Notion ficam. Diego atribui a origem a "uma metodologia implementada pelo Angular, lá em 2011". Ver as tensões e [[wiki/concepts/single-page-application]].
- **Antes:** no modelo MVC, "a parte visual da aplicação [...] sempre foi muito atrelada com o back-end" (PHP, Ruby, Python, Node), com o HTML "pronto lá do servidor". Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **Núcleo e renderizadores:** `react` é "a parte que tem a lógica do React por trás dos panos" em todos os ambientes; o `react-dom` diz que a interface é "com a DOM", e o React Native, "com a interface nativa do iOS, do Android". Diego cita React TV, React VR e React Native Windows/macOS (Microsoft). Ver [[wiki/entities/react-native]] e [[wiki/concepts/dom]].

### Criação e estrutura do projeto

- **Comandos:** `yarn create react-app web --template typescript` ou `npx create-react-app web --template typescript`. O nome é "web", porque "o Front End é tudo que é visual", e o mobile também seria front-end. Sobre o TypeScript: tipagem "não está aqui para diminuir a sua produtividade [...] isso é um grande mito". Ver [[wiki/entities/typescript]].
- **VS Code:** comando `code .`, ou `Install 'code' command in PATH` pela paleta. Ver [[wiki/entities/vs-code]].
- **Limpeza:** saem o README, o `App.css`/`index.css`, o teste, o logo SVG, o `serviceWorker` ("quando você vai criar um PWA") e o `setupTests`. O `public/` fica só com o `index.html`, e o `<title>` vira Proffy.
- **Arquivos da raiz:** `.gitignore` (tira o `node_modules`); `package.json` com `react`, `react-dom` e `react-scripts`; `tsconfig.json` ("vem pronto"); `yarn.lock` com as versões instaladas. O `node_modules` é grande porque "cada dependência tem suas próprias dependências". Ver [[wiki/concepts/gerenciador-de-pacotes]].
- **`react-scripts`:** "um conjunto de configurações" que converte o código porque JSX "não é entendida por nenhum browser". O Babel converte "o JavaScript mais moderno para um JavaScript um pouquinho mais antigo", e o Webpack "faz a automatização desse processo" e permite importar imagem e CSS pelo JavaScript. Ver [[wiki/concepts/transpilador]] e [[wiki/concepts/pipeline-de-assets]].
- **`div#root`:** o React "vai rodar sempre a partir do lado do cliente". Com JavaScript desabilitado, "não vai ter nada". O `ReactDOM.render` é usado "apenas uma única vez" para injetar o `<App />` no `#root`. Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].

### Componentes e JSX

- **Componente** é "uma função que retorna um HTML", usado para "reaproveitar código entre várias telas". O exemplo previsto é o card de professor, repetido na listagem e nos favoritos. Ver [[wiki/concepts/componentizacao]].
- **Maiúscula obrigatória,** "porque letra minúscula são as tags do HTML": `<app>` vira tag desconhecida.
- **`import React` obrigatório** em todo arquivo com JSX, "mesmo que o React não esteja sendo utilizado".
- **JSX** é "JavaScript mais XML", e TSX é "TypeScript com XML". Ver [[wiki/concepts/jsx]].
- **Propriedades e estado** são adiados para quando forem usados.

### Estilos globais e rem

- **Assets:** imagens SVG prontas para download ("um formato mais leve"), em `src/assets/images` e `images/icons`.
- **`global.css`:**
  - `:root { font-size: 60% }` e as cores em variáveis, "caso você queira customizar o tema da aplicação [...] para algum tema dark". Ver [[wiki/concepts/variaveis-css]].
  - `* { margin: 0; padding: 0; box-sizing: border-box }`.
  - `html, body, #root { height: 100vh }` ([[wiki/concepts/unidades-de-viewport]]).
  - `#root` com flex para centralizar.
  - `body, input, button, textarea` com Poppins 500 e `1.6rem`, porque os campos "utilizam uma fonte própria" ([[wiki/concepts/heranca-css]]).
  - O global entra com `import './assets/styles/global.css'` no `App.tsx`.
- **Google Fonts:** Archivo 400 e 700 (botões e títulos) e Poppins 400, via `<link>` no `index.html`. Ver [[wiki/entities/google-fonts]].
- **A conta do rem:** com o padrão de 16 px, 60% dá 9,6 px, então "toda vez que eu escrever 1 rem [...] representa 9,6 pixels". A partir de 700 px, a raiz vai para 62,5% ("16 vezes 0.625 [...] retorna 10"). Para mudar "todo o tamanho" basta mexer na raiz, o que ajuda "principalmente também para acessibilidade". Ver [[wiki/concepts/unidades-de-medida-css]].
- **`.container`:** `width: 90vw; max-width: 700px`.

### Landing page

- **Componente de página:** `pages/Landing/index.tsx`. O import da pasta acha o `index`.
- **HTML via Emmet:** `div#page-landing > div#page-landing-content.container > div.logo-container` (logo + `h2`), `img.hero-image`, `div.buttons-container` com dois links e `span.total-connections` ("Total de 200 conexões já realizadas" + coração).
- **Imagens por import:** `import logoImg from '../../assets/images/logo.svg'` e `src={logoImg}`, porque o React "não vai entender que essa imagem existe" por caminho. Chaves para "utilizar uma variável javascript" no JSX.
- **`className`,** porque "class é uma palavra reservada do JavaScript". O `alt` serve "para a gente descrever exatamente o que aquela imagem está querendo dizer".
- **CSS por página:** `styles.css` na pasta da landing, importado com `./`. Sem `./`, o import "vai achar que isso aqui é um pacote".
- **Mobile:** `#page-landing` com `100vw`/`100vh` e flex; `h2` com `font-weight: 500` "porque por padrão os headings [...] setam uma fonte negrito"; links de 30 × 10,4 rem com `border-radius`, flex e `text-decoration: none`; `:first-child` para a margem só no primeiro; `:hover` com `transition: background-color 0.2s`. Os valores saem do layout pronto: "Eu já construí o layout antes".

### Landing page no desktop

- **Breakpoint de 1100 px:** "cada layout é um layout diferente", e não há regra fixa. A tela de desktop "mais pequena" seria 1366. Ver [[wiki/concepts/breakpoint]].
- **`#page-landing-content { max-width: 1100px }`** sobrescreve o `.container` porque "o id ele é sempre mais poderoso que a classe". Ver [[wiki/concepts/especificidade-css]].
- **Grid** ("display grid unido ao display flexbox é uma delicinha"; antes "criava tudo com float left, float right"):

```css
#page-landing-content {
  display: grid;
  grid-template-rows: 350px 1fr;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-areas:
    "logo hero hero"
    "buttons buttons total";
}
```

  - `1fr` é "ocupe o espaço que sobrar".
  - `2fr 1fr 1fr` em vez de `2fr 2fr`, porque os botões "passa[m] do tamanho da imagem" e precisam de três das quatro frações.
  - Ajustes: `align-self: center`, `justify-self: end`, `text-align: left`, fonte maior. Ver [[wiki/concepts/css-grid]].

### Navegação

- **`react-router-dom`** é "o módulo mais utilizado hoje na web para fazer navegação". O erro de tipos se resolve com `yarn add @types/react-router-dom -D`, porque alguns módulos "não incluem a tipagem do TypeScript". Ver [[wiki/concepts/arquivo-de-declaracao-de-tipos]].
- **`routes.tsx`:** `<BrowserRouter>` com `<Route path="/" exact component={Landing} />`, `/study` (`TeacherList`) e `/give-classes` (`TeacherForm`). Props são "exatamente atributos que a gente passa pra uma tag", só que para um componente.
- **`exact`:** sem ele, a landing aparece junto com Teachers, porque o roteador "não faz uma verificação de igualdade [...] Ele faz a verificação de conteúdo", e "a barra [...] sempre vai estar em todos os outros caminhos".
- **`<a href>` × `<Link to>`:** com `<a>`, o favicon pisca e a aba Network mostra "tudo de novo, CSS todo, JavaScript". Com `Link`, "não tem nenhum carregamento adicional". Ver [[wiki/concepts/client-side-routing]] e [[wiki/concepts/single-page-application]].

### PageHeader, props e children

- **Cabeçalho da listagem:** `header.page-header` com `top-bar-container` (Link de voltar + logo) e `header-content` com `strong` ("Estes são os proffys disponíveis"). O seletor `.top-bar-container > img` pega só a logo e deixa de fora o ícone dentro do link. O `opacity` cai no hover, "até porque no mobile não existe hover".
- **Erro de digitação:** a largura não aplicava por um erro de escrita no CSS. "Revisa cada letrinha que você escreve."
- **Extração:** `src/components/PageHeader`, para "os componentes que a gente vai conseguir compartilhar entre várias páginas". O mesmo header entra em `TeacherForm` ("Que incrível que você quer dar aulas"). Ver [[wiki/concepts/componentizacao]].
- **Prop `title` tipada:**
  - `interface PageHeaderProps { title: string }`, com `title?` para opcional, caso em que seria preciso "deixar um valor default".
  - `const PageHeader: React.FC<PageHeaderProps> = (props) => ...`, com `FC` "uma abreviação de function component". Componentes de classe aparecem em código antigo "porque o React teve várias versões".
  - O "parâmetro" entre `< >` é um Generic. O autocomplete de `props.` mostra `title`, e o TypeScript "ajuda a gente com essa inteligência do nosso editor".
  - Ver [[wiki/concepts/props-react]] e [[wiki/concepts/generics-typescript]].
- **`props.children`** é "uma propriedade automática do React [...] qual o conteúdo que eu passei para dentro desse componente". O `<form id="search-teachers">` entra entre `<PageHeader>` e `</PageHeader>` e só existe na página de estudar.
- **Detalhe:** a seta é ligadura da fonte Fira Code.

### Formulário de busca

- **Campos:** `div.input-block` com `label` e `input` (subject, week_day, time), por enquanto todos de texto ("o certo seria select"). O `htmlFor` substitui o `for`, que no JavaScript "é uma palavra reservada para a gente fazer estruturas de repetição". Ele "precisa ser o mesmo" que o `id`.
- **Estilo:** inputs de 5,6 rem, `border-radius`, `outline: 0`, padding de 1,6 rem e Archivo.
- **Linha de foco:**

```css
.input-block:focus-within::after {
  content: '';
  width: calc(100% - 3.2rem);
  height: 2px;
  background: var(--color-primary-light);
  position: absolute;
  left: 1.6rem; right: 1.6rem; bottom: 0;
}
```

  - `:focus-within` "vai verificar se dentro desse input block existe um input que tenha focus". Diego chamou de pseudo-elemento, conferiu e corrigiu para "pseudoclasse".
  - O `content` é "obrigatório sempre que a gente coloca o after e o before".
  - Ver [[wiki/concepts/pseudo-classe-css]], [[wiki/concepts/pseudo-elemento-css]] e [[wiki/concepts/indicador-de-foco]].
- **Espaço entre campos:** `.input-block + .input-block { margin-top: 1.4rem }`, "todo input block que antes dele tem outro", sem `first-child`/`last-child`.
- **Desktop (≥ 700 px):** `grid-template-columns: repeat(3, 1fr)`, `column-gap: 16px` e `position: absolute; bottom: -28px` para o form ficar "exatamente aqui no meio" do header e do conteúdo (testou −44, −34, −30 e −28). O CSS do header muda para o `styles.css` do `PageHeader`: header de 340 px, `max-width` 1100/740 e `strong` com `max-width: 350px`.

### Listagem e TeacherItem

- **Estrutura:** `main` ("o conteúdo principal da página") com um `article.teacher-item` por professor: `header` (avatar do GitHub, `strong` com o nome, `span` com a matéria), `p` com a bio (dois parágrafos por `<br />`) e `footer` com "Preço/hora" em `strong` e um `<button type="button">` com o ícone do WhatsApp. "Todo botão ele precisa ter um tipo."
- **CSS:** card com `overflow: hidden`, avatar de 8 rem com `border-radius: 50%` ("sempre deixa totalmente arredondado"), `.teacher-item > p` para pegar só o parágrafo direto ("por isso que eu boto sinal de maior"), footer com flex e `space-between`, botão verde com `justify-content: space-evenly`. No desktop, paddings em rem "para respeitar as nossas condições" e botão de 24,5 rem, "exatamente [...] 245" px.
- **`TeacherItem`** vai para `components/`, porque "se a nossa aplicação crescer, bem provavelmente vai ser utilizado em mais lugares". Um esquecimento: o CSS do componente não tinha sido importado.
- **Encerramento:** ficam para o dia em que a API em Node.js for conectada a página de cadastro, o CSS dela e o conceito de estado.

## Tensões e precisões

- **APIs de 2020 que mudaram** (as mesmas da [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta|NLW #1]]). `[skill: tech-mentor-frontend]`
  - **`React.FC` e `children`:** a aula depende do `children` implícito do `React.FC`. Nos tipos do React 18, o `FC` deixou de incluir `children` `[external]` (https://github.com/DefinitelyTyped/DefinitelyTyped/pull/56210). Hoje o `{props.children}` do `PageHeader` dá erro de tipo sem `children?: React.ReactNode` na interface. Ver [[wiki/concepts/props-react]].
  - **`import React`:** o novo JSX transform (React 17, outubro de 2020, dois meses depois da aula) tornou o import desnecessário `[external]` (https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html). Na época, a afirmação estava certa.
  - **`ReactDOM.render`:** substituído por `createRoot` no React 18 e removido no 19 `[external]` (https://react.dev/blog/2024/04/25/react-19-upgrade-guide#removed-reactdom-render).
  - **React Router v5 → v6/v7:** `exact` e `component=` deram lugar a `<Routes>`, `element={<Landing />}` e correspondência exata por padrão `[external]` (https://reactrouter.com/6.30.0/upgrading/v5). O v6 traz tipos próprios, sem `@types/react-router-dom`. Ver [[wiki/entities/react-router]].
  - **CRA:** descontinuado em 2025, com Vite no lugar ([[wiki/entities/create-react-app]]).
- **"Verificação de conteúdo" é prefixo.** O v5 não testa se o endereço "contém" o path; testa se começa por ele, por segmento (`/study` casa com `/study/1`, não com `/studying`). O resultado da aula é o mesmo, mas `/` casar com tudo é porque toda URL começa com `/`.
- **SPA não nasceu no Angular.** O AngularJS saiu em 2010 `[external]`, e aplicações de página única com XHR (Gmail, 2004) e o termo são anteriores. O React (2013) não implementou "a metodologia do Angular"; o diferencial dele foi o modelo de componentes com re-renderização declarativa. Ver [[wiki/concepts/single-page-application]] e [[wiki/concepts/virtual-dom]].
- **`1.6rem` não é "60% a mais do font size do elemento".** Ele é 1,6 × o font-size da raiz (aqui, 1,6 × 9,6 = 15,36 px), qualquer que seja o elemento. A regra relativa ao próprio elemento é o `em`. Ver [[wiki/concepts/unidades-de-medida-css]].
- **A raiz de 60% encolhe tudo para quem aumentou a fonte?** Não: porcentagem na raiz respeita a preferência do usuário (quem configurou 20 px ganha 12 px por rem). O que se perde é a correspondência 1 rem = 10 px, e o texto base em 1,6 rem fica abaixo de 16 px no celular (15,36 px), o que o Safari do iOS trata como motivo para dar zoom ao focar inputs com fonte menor que 16 px `[external, não verificado nesta sessão]`. O Mayk usa 60% e 62,5% em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]] e [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]].
- **`font-weight: 500` sem o peso 500 carregado.** Só Poppins 400 foi incluída, então o navegador usa a face mais próxima (400), e o "500 padrão" não aparece na tela. Ver [[wiki/entities/google-fonts]].
- **`100vw`/`100vh`.** `100vw` inclui a barra de rolagem vertical e gera rolagem horizontal no desktop quando a página rola. `100vh` no celular ignora a barra do navegador, e `100dvh`/`svh` resolvem `[skill: tech-mentor-frontend]`. Ver [[wiki/concepts/unidades-de-viewport]].
- **`id` "sempre mais poderoso" vale para especificidade** (1-0-0 contra 0-1-0), não para "poder". O mesmo efeito, sem depender de id, viria de ordem na cascata ou de um modificador. Ver [[wiki/concepts/especificidade-css]].
- **Mesma tela, dois grids.** Para o mesmo layout, Mayk usa `2fr 1fr 2fr` em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], e Diego usa `2fr 1fr 1fr` com outra divisão de áreas. Os dois chegam à imagem do Figma.
- **Linha de foco: o indicador existe, mas só para o bloco.** `outline: 0` some com o foco nativo; a linha do `::after` o substitui, o que atende a [[wiki/concepts/indicador-de-foco]] se o contraste for suficiente (WCAG 2.4.7 e 1.4.11). Os inputs de texto para dia e hora ainda viram `select` e `time` depois.
- **Avatar e bio fixos com `alt` de nome** são aceitáveis. O botão de WhatsApp tem texto visível, e o `alt="WhatsApp"` do ícone repete a informação para o leitor de tela ("WhatsApp Entrar em contato"); um ícone decorativo leva `alt=""`. Ver [[wiki/concepts/acessibilidade]].
- **Bundler:** a explicação do `react-scripts` está certa no essencial. O Babel também retira os tipos do TypeScript (a checagem de tipos roda à parte) e transforma o JSX, não só o "JavaScript moderno". Ver [[wiki/concepts/transpilador]].
- **React TV e React VR:** o React VR virou React 360 e foi descontinuado, e o React TV era um projeto da comunidade, abandonado `[external, não verificado nesta sessão]`. React Native Windows e macOS continuam mantidos pela Microsoft.
- **Data comemorativa:** o Dia Nacional dos Profissionais da Educação, em 6 de agosto, foi instituído pela Lei 13.054/2014 `[external, não verificado nesta sessão]`.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react]]: biblioteca de UI
- [[wiki/entities/typescript]]: template, props tipadas, `@types`
- [[wiki/entities/create-react-app]]: estrutura inicial e `react-scripts`
- [[wiki/entities/react-router]]: rotas da SPA
- [[wiki/entities/react-native]]: citado como renderizador irmão
- [[wiki/entities/google-fonts]]: Archivo e Poppins
- [[wiki/entities/vs-code]]: `code .`, auto import, Emmet, Fira Code
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: Notion, React DevTools, Twitter, Netflix, Angular, Vue, Webpack, Babel, Yarn, npx, Git/GitHub, Microsoft (React Native Windows/macOS), React TV, React VR, Thiago Luchtenberg (designer), Mayk Brito (o texto do card dele).

## Conceitos

[[wiki/concepts/single-page-application]] · [[wiki/concepts/client-side-routing]] · [[wiki/concepts/renderizacao-ssr-vs-csr]] · [[wiki/concepts/dom]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/jsx]] · [[wiki/concepts/props-react]] · [[wiki/concepts/generics-typescript]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/transpilador]] · [[wiki/concepts/pipeline-de-assets]] · [[wiki/concepts/gerenciador-de-pacotes]] · [[wiki/concepts/mobile-first]] · [[wiki/concepts/breakpoint]] · [[wiki/concepts/unidades-de-medida-css]] · [[wiki/concepts/unidades-de-viewport]] · [[wiki/concepts/variaveis-css]] · [[wiki/concepts/heranca-css]] · [[wiki/concepts/especificidade-css]] · [[wiki/concepts/css-grid]] · [[wiki/concepts/pseudo-classe-css]] · [[wiki/concepts/pseudo-elemento-css]] · [[wiki/concepts/indicador-de-foco]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/virtual-dom]]

## Open Questions

- O estado (`useState`) e a imutabilidade, adiados nesta aula, devem chegar com o formulário de cadastro e os horários dinâmicos, num dia futuro da trilha.
- A API em Node está em [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]. A conexão com o front-end, o mobile com React Native e os favoritos em storage local ainda não foram ingeridos.
- A legenda trocou o nome da classe digitada errado por "t-shirt" ("Eu escrevi t-shirt"). O erro real não é recuperável pelo áudio transcrito.
- Data provável: 3 de agosto de 2020 `[external, não verificado]`.
