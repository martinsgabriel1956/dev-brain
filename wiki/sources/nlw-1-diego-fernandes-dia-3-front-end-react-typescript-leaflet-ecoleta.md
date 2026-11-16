---
type: source
title: "NLW #1 com Diego Fernandes, dia 3: front-end web do Ecoleta com React, TypeScript e Leaflet"
aliases: ["NLW 1 Diego dia 3", "Ecoleta React", "Ecoleta front-end web", "NLW 1 trilha React dia 3"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react, typescript, jsx, componentes, props, useState, useEffect, imutabilidade, react-router, leaflet, react-leaflet, axios, ibge, geolocation, formulario-controlado, create-react-app, react-icons, feather-icons, spa, frontend, lang-dynamic, rocketseat, ecoleta, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1 com Diego Fernandes, dia 3: front-end web do Ecoleta com React, TypeScript e Leaflet

## TL;DR

Terceira aula (cerca de 2h10) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #1]]. O front-end web do Ecoleta é construído em [[wiki/entities/react]] com [[wiki/entities/typescript]], consumindo a API do [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta|dia 2]]. A aula tem duas metades:

1. **Os conceitos do React.**
   - O projeto do [[wiki/entities/create-react-app]] é limpo e o "mistério" da `div#root` é explicado: a página é montada pelo JavaScript depois do carregamento (`ReactDOM.render(<App />, root)`), então o "View Page Source" vem vazio ([[wiki/concepts/renderizacao-ssr-vs-csr|CSR]]).
   - O [[wiki/concepts/jsx]] é "HTML dentro do JavaScript", contraposto ao `React.createElement`.
   - [[wiki/concepts/componentizacao|Componentes]] com letra maiúscula, um `Header` reutilizável.
   - [[wiki/concepts/props-react|Props]] tipadas com `React.FC<HeaderProps>` e `interface`, o que leva aos [[wiki/concepts/generics-typescript|generics]].
   - [[wiki/concepts/useState|Estado]] com um contador e o conceito de [[wiki/concepts/imutabilidade]]. Para Diego, "com isso aqui, acabou o React".
2. **O app.**
   - A página Home com CSS pronto, Google Fonts (Roboto e Ubuntu), `react-icons` ([[wiki/entities/feather-icons]]) e `import` de imagens.
   - Navegação [[wiki/concepts/single-page-application|SPA]] com o [[wiki/entities/react-router]] (`BrowserRouter`, `Route exact`, `Link`).
   - O formulário de cadastro com `fieldset`/`legend` e um mapa [[wiki/entities/leaflet]] (react-leaflet + OpenStreetMap).
   - Os itens vêm da API com [[wiki/entities/axios]] (`baseURL`) dentro de [[wiki/concepts/useEffect]], com `key` no `map`. As UFs e cidades vêm da API do [[wiki/entities/ibge]], encadeadas por `useEffect([selectedUf])`.
   - O clique no mapa vira estado. A posição inicial vem da [[wiki/concepts/geolocation-api]].
   - Os inputs são [[wiki/concepts/componente-controlado|controlados]] com um `formData` atualizado por spread. Os itens selecionados entram e saem com `findIndex`/`filter`.
   - O submit usa `preventDefault`, `api.post('points', data)`, `alert` e `useHistory().push('/')`.

## Key Claims

### Limpeza do projeto e a `div#root`

- **Limpeza:**
  - Saem favicon, logos, manifest, `index.css`, `serviceWorker`, `setupTests`, o arquivo de teste e o README.
  - O `index.html` fica com `<title>Ecoleta</title>` e `theme-color` verde, "a cor que aparece no browser do Android".
  - A API do dia 2 fica rodando num terminal à parte ("nunca mais mexo ali").
- **Por que o HTML vem vazio:** "a interface [...] é montada a partir do JavaScript [...] a partir do momento que o site já carregou". O "View Page Source" mostra só a `div#root`, e o `h1` aparece apenas no inspetor, que é "uma árvore de elementos em tempo real". Ver [[wiki/concepts/dom]] e [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **`ReactDOM.render(<App />, document.getElementById('root'))`:** o `react-dom` integra o React com a DOM, porque o React serve "para web, quanto para mobile, quanto para VR". Diego cita que a Microsoft o usa "para 46 aplicações", sem fonte.
- **Emmet em arquivos JS/TS:** vem no VS Code, mas é preciso habilitá-lo no `settings.json` com `emmet.syntaxProfiles` e `emmet.includeLanguages: { javascript: 'javascriptreact' }`. Exemplo: `div#app>ul>li*5`. Ver [[wiki/entities/vs-code]].

### JSX, componentes e props

- **[[wiki/concepts/jsx]]:** "a possibilidade de nós escrevermos HTML diretamente dentro do JavaScript". Sem ele, seria `React.createElement('h1', { children: 'Hello World' })`, "trabalhoso", sobretudo com tags aninhadas. "O HTML ele segue a sintaxe do XML", daí o X; o arquivo precisa ser `.tsx`.
- **Componentes:** "o grande motivo dele ser tão famoso". O exemplo é o tweet repetido no Twitter, visto pelo React DevTools. O componente `Header` é uma função que retorna JSX, com nome em maiúscula "para ele não bater com as tags do HTML", e é usado como `<Header />` quantas vezes for preciso. Ver [[wiki/concepts/componentizacao]].
- **Hábitos repetidos durante a aula:** "eu sempre preciso importar o React nos meus componentes, mesmo que eu não vá utilizar essa variável diretamente", e parênteses em volta do `return` de várias linhas. Ver as tensões.
- **[[wiki/concepts/props-react|Propriedades]]:** "atributos que a gente envia pro componente", como o `type` e o `value` de um `input`.
  - `<Header title="Hello World" />` dá erro no TypeScript até o componente declarar a prop: `const Header: React.FC<HeaderProps> = (props) => ...` com `interface HeaderProps { title: string }`. O `title?` a tornaria opcional.
  - Sem o `title`: "Property title is missing in type". "Se a gente não estivesse utilizando o TypeScript [...] uma cagada tremenda."
  - `{props.title}`: chaves para "inserir algo de JavaScript dentro do meu HTML".
- **Generics:** "um tipo do TypeScript que pode receber um parâmetro". Ver [[wiki/concepts/generics-typescript]].
- **Detalhe:** a "flechinha" do editor é ligadura da fonte FiraCode.

### Estado e imutabilidade

- **Por que estado:** com `let counter`, o `counter++` muda a variável (o `console.log` mostra 2, 3, 4), "mas na interface isso não muda".
- **`useState`:** `const [counter, setCounter] = useState(0)` retorna um array: o valor e a função de atualização. "Eu nunca vou poder alterar um valor [...] do estado de uma maneira direta"; o que se faz é `setCounter(counter + 1)`. Diego justifica com "várias melhorias na performance". Ver [[wiki/concepts/useState]] e [[wiki/concepts/imutabilidade]].
- **Reatividade:** qualquer JSX que dependa do estado ou de props se atualiza, inclusive `counter * 2` e `<Header title={\`Contador: ${counter}\`} />` em outro componente.
- **"Acabou o React":** "Se você entendeu componente, propriedade e estado [...] todo o resto [...] [é] formado a partir desses."

### Home, CSS e ícones

- **Material pronto para download:** o layout do Figma, as imagens (logo, `home-background`) e o CSS (`App.css` global, `styles.css` por página), "porque o CSS [...] se a gente fizer ele do zero, acaba tomando muito tempo".
- **Google Fonts:** Roboto 400 e Ubuntu 700, via `<link>` no `index.html` ([[wiki/entities/google-fonts]]). "Eu sonho com display flex" ([[wiki/concepts/flexbox]]).
- **`pages/Home/index.tsx`** em vez de `Home.tsx`, para juntar na pasta o CSS, as imagens e os componentes da página. O import de pasta procura o `index`.
- **`className`,** "porque class é uma palavra reservada do JavaScript".
- **Imagens por import:** `import logo from '../../assets/logo.svg'` e `<img src={logo} alt="Ecoleta" />`; "no React a gente não bota o caminho para a imagem". O CSS sem export entra com `import './styles.css'`.
- **`react-icons`** reúne Font Awesome, Material e Feather. `import { FiLogIn } from 'react-icons/fi'` vira componente: `<FiLogIn />`. Ver [[wiki/entities/feather-icons]].

### Navegação

- **[[wiki/entities/react-router]]:**
  - `npm install react-router-dom` e `@types/react-router-dom -D` ([[wiki/concepts/arquivo-de-declaracao-de-tipos]]).
  - `routes.tsx` com `<BrowserRouter>` e `<Route component={Home} path="/" exact />` / `<Route component={CreatePoint} path="/create-point" />`.
  - Sem `exact`, `/create-point` "começa com" `/` e cai na Home.
  - Existem "browser router, hash router, memory router, static router".
- **SPA na prática:** com `<a href>`, a página recarrega inteira ("ele carregou tudo"). Com `<Link to>`, a aba Network não mostra nenhuma requisição, porque "todo CSS, todo HTML, todo código JavaScript é mantido entre as telas". Ver [[wiki/concepts/single-page-application]] e [[wiki/concepts/client-side-routing]].

### HTML do formulário

- **Semântica:** `form` > `fieldset` + `legend` + `h2` (Dados, Endereço, Ítens de coleta, "com acento no i"). "A div ela não representa nada quando a gente for pensar em semântica [...] é muito ruim [para] a acessibilidade." Ver [[wiki/concepts/html-semantico]], [[wiki/concepts/formulario-html]] e [[wiki/concepts/acessibilidade]].
- **`htmlFor` no `label`,** porque `for` também é reservado. `.field` e `.field-group` põem email e WhatsApp lado a lado; o email usa `type="email"`, e o WhatsApp fica `text`.
- **UF e cidade como `select`,** "para a gente conseguir realmente não deixar o usuário selecionar estado ou cidade que não exista". O número do endereço continua fora.
- **Itens em `ul.items-grid` > `li`** com `img` e `span`; a classe `selected` deixa o item verde. O botão é `type="submit"`. O campo de imagem fica para o upload.

### Mapa com Leaflet

- **Por que Leaflet:** o Google Maps teria "plano gratuito bem extenso", mas exige conta e "cartão de crédito", o que "seria um rolo". O [[wiki/entities/leaflet]] é "de código aberto", "não é tão bonito [...] mas [...] totalmente funcional".
- **Montagem:**
  - `npm install leaflet react-leaflet`, mais o CSS do Leaflet no `index.html` e `@types/react-leaflet -D`.
  - `<Map center={[lat, lng]} zoom={15}>` com `<TileLayer>` do OpenStreetMap ("é só o layout") e `<Marker position={...} />`.
  - A latitude e a longitude iniciais foram copiadas da URL do Google Maps.

### Itens de coleta da API com Axios e useEffect

- **[[wiki/entities/axios]]** em vez de `fetch`, porque permite "criar uma base URL": `axios.create({ baseURL: 'http://localhost:3333' })` em `services/api.ts`. "Se um dia eu trocar [...] basta eu trocar aqui dentro." Ver [[wiki/concepts/fetch-api]].
- **[[wiki/concepts/useEffect]]:** o componente "é uma função", e "toda vez que eu mudo alguma coisa dentro dessa função, ela é executada de novo". Uma chamada à API no corpo se repetiria a cada render, e fora do componente não faria sentido.
  - `useEffect(fn, [])` com array vazio roda "uma única vez".
  - Com dependências, roda quando elas mudam.
  - Não aceita `async` direto ("é um bloqueio que o pessoal do React faz"), então o código usa `.then` ([[wiki/concepts/promise-javascript]]).
- **Estado tipado:**
  - `const [items, setItems] = useState<Item[]>([])` com `interface Item { id: number; title: string; image_url: string }`.
  - Sem o tipo, "property title does not exist on type never". "Sempre que a gente cria um estado para um array ou objeto, a gente precisa manualmente informar o tipo."
- **Listas e `key`:** `items.map(item => <li key={item.id}>...)`. Sem `key`, o aviso é "Each child in a list should have a unique key prop", e a `key` serve "pro React conseguir encontrar esse elemento na hora de atualizar". Ver [[wiki/concepts/virtual-dom]] e [[wiki/concepts/listas-html]].

### Estados e cidades do IBGE

- **API de localidades do [[wiki/entities/ibge]]:** `/estados` e `/estados/{UF}/municipios`. Aceita a sigla ou o id, e tem ordenação.
- **UFs:** num `useEffect` separado ("eu gosto sempre de manter cada chamada em um useEffect separado"), `axios.get<IBGEUFResponse[]>(...)` sem a `baseURL` vira `response.data.map(uf => uf.sigla)` e vai para `useState<string[]>`. Diego primeiro cria uma interface `UF` e desiste ("então não precisava nem ter criado isso aqui"); a interface fica só com o que é usado.
- **Select controlado:** `value={selectedUf}` e `onChange={handleSelectUf}`, com `ChangeEvent<HTMLSelectElement>` para tipar o evento e chegar a `event.target.value`. A dica é o "TypeScript React Cheatsheet". Ver [[wiki/concepts/componente-controlado]].
- **Cidades:** `useEffect(() => { if (selectedUf === '0') return; axios.get(\`.../${selectedUf}/municipios\`)... }, [selectedUf])`. O efeito também roda na montagem, por isso o guarda do `'0'`. A cidade também vira estado controlado (`selectedCity`).

### Posição no mapa e geolocalização

- **`<Map onClick={handleMapClick}>`** com `LeafletMouseEvent` vira `setSelectedPosition([event.latlng.lat, event.latlng.lng])`, tipado como tupla `[number, number]` e iniciado em `[0, 0]`. O `Marker` passa a usar `selectedPosition`.
- **[[wiki/concepts/geolocation-api]]:** `navigator.geolocation.getCurrentPosition(position => setInitialPosition([coords.latitude, coords.longitude]))`, e o `center` do mapa usa `initialPosition`. "As vezes é permissão [...] varia da tua internet"; se não funcionar, a dica é deixar fixo.

### Inputs, itens e envio

- **`formData`:** um estado `{ name, email, whatsapp }` e um handler genérico, `setFormData({ ...formData, [name]: value })`. O `set` "substitui totalmente", então o spread "mantém os dados que já tem". O `[name]` é a chave computada.
- **Itens selecionados:**
  - `onClick={() => handleSelectItem(item.id)}`, porque `onClick={handleSelectItem(item.id)}` "está executando a função, ele não está passando a função como referência". Ver [[wiki/concepts/callback-javascript]] e [[wiki/concepts/funcoes-javascript]].
  - Na lógica, `findIndex` decide se `filter(item => item !== id)` remove ou `[...selectedItems, id]` adiciona, com a ressalva de que "o push altera a informação original".
  - A classe vem de `selectedItems.includes(item.id) ? 'selected' : ''`. "Melzinho na chupeta."
- **Submit:**
  - `onSubmit` no `form`, porque "o form pode ser submitado clicando no botão ou apertando o Enter".
  - `event.preventDefault()` com `FormEvent` evita o recarregamento.
  - O objeto `data` junta `formData`, a UF, a cidade, `[latitude, longitude]` e os itens, e segue em `await api.post('points', data)`.
  - Depois vêm `alert('Ponto de coleta criado!')` e `history.push('/')` (`useHistory`).
  - A tela de sucesso que o Thiago desenhou fica "como desafio".
- **Fechamento:** "a gente nunca tinha passado tanto conteúdo gratuito"; amanhã vem o mobile.

## Tensões e precisões

- **APIs de 2020 que mudaram.** `[skill: tech-mentor-frontend]`
  - **`import React`:** deixou de ser obrigatório para JSX com o novo JSX transform (React 17, fim de 2020) `[external]` (https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html). O "sempre preciso importar" virou hábito, não regra.
  - **`ReactDOM.render`:** deu lugar a `createRoot(...).render()` no React 18 e foi removido no React 19 `[external]` (https://react.dev/blog/2024/04/25/react-19-upgrade-guide#removed-reactdom-render).
  - **`React.FC`:** caiu em desuso. Ele injetava `children` implícito (removido nos tipos do React 18), e o próprio template TypeScript do CRA o tirou `[external]` (https://github.com/facebook/create-react-app/pull/8177). O padrão atual é `function Header({ title }: HeaderProps)`. Ver [[wiki/concepts/props-react]].
  - **React Router:** o v5 da aula (`exact`, `component`, `useHistory`) virou `<Routes>`, `element={<Home />}`, correspondência exata por padrão e `useNavigate` no v6 `[external]` (https://reactrouter.com/6.30.0/upgrading/v5). Hoje o React Router 7 absorveu o Remix. Ver [[wiki/entities/react-router]].
  - **react-leaflet:** `<Map>` virou `<MapContainer>` no v3, e `onClick` como prop saiu. Eventos passam por `useMapEvents`, e o `center` só vale na montagem `[external]` (https://react-leaflet.js.org/docs/api-map/). O `setInitialPosition` da aula, por isso, não recentralizaria o mapa no v3+. Ver [[wiki/entities/leaflet]].
  - **CRA:** descontinuado em 2025 ([[wiki/entities/create-react-app]]).
- **Imutabilidade não é "por performance" em primeiro lugar.** O React decide se re-renderiza comparando referências (`Object.is`). Mutar e chamar `set` com o mesmo objeto não muda nada, e a tela não atualiza. A performance (comparações baratas, `memo`) vem depois disso. Outra precisão: `setCounter(counter + 1)` lê o valor da closure. Vários sets seguidos ou sets assíncronos pedem a forma de função, `setCounter(c => c + 1)`. Ver [[wiki/concepts/imutabilidade]] e [[wiki/concepts/useState]].
- **A cadeia UF → cidades tem race condition.** Trocar de SC para PR rápido dispara duas requisições. Se a de SC responder por último, a lista mostra cidades de SC com PR selecionado.
  - O efeito precisa de cleanup (uma flag `ignore` ou um `AbortController` no retorno do `useEffect`).
  - Sem isso, o `StrictMode` do React 18 também duplica as chamadas em desenvolvimento.
  - `[skill: tech-mentor-frontend]` A skill recomenda TanStack Query para estado de servidor.
  - "Não pode usar async no useEffect" tem motivo: o efeito deve retornar a função de cleanup ou nada, e uma função `async` retorna uma promise.
  - Ver [[wiki/concepts/race-condition]], [[wiki/concepts/useEffect]] e [[wiki/concepts/server-state]].
- **`'0'` como "não selecionado" vai para a API.** Sem escolher cidade, UF ou posição, o submit manda `city: '0'` e `[0, 0]`, um ponto no Golfo da Guiné.
  - Não há validação no cliente nem `required`, e não há `try/catch`: falha na API vira rejeição não tratada, sem feedback.
  - O `Marker` aparece em `[0, 0]`, só fora da tela ("como ele está zero, vai dar certo").
  - O dia 2 já apontava a falta de validação no servidor ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]). Ver [[wiki/concepts/validacao-de-entrada]].
- **Geolocalização sem tratamento de erro.** `getCurrentPosition` só funciona em contexto seguro (HTTPS ou localhost) e com permissão. Sem o segundo callback de erro, a recusa deixa o mapa em `[0, 0]` para sempre. Ver [[wiki/concepts/geolocation-api]].
- **Itens clicáveis em `li` não são acessíveis.** `li` com `onClick` não recebe foco nem responde a Enter ou Espaço, e o leitor de tela não anuncia "selecionado". O certo são `<button aria-pressed>` ou checkboxes estilizados. Fica a ironia: a mesma aula defende `fieldset` pela acessibilidade. Ver [[wiki/concepts/acessibilidade]] e [[wiki/concepts/html-semantico]].
- **"HTMLSelectElement é uma variável global do React"** não procede. É um tipo da DOM, que vem das definições `lib.dom.d.ts` do TypeScript; o React só o usa nos genéricos dos eventos. O "synthetic event" mostrado no console é o wrapper do React sobre o evento nativo.
- **JSX não é HTML, e HTML não é XML.** JSX tem sintaxe parecida com XML e compila para chamadas de função. Por isso usa os nomes das propriedades da DOM (`className`, `htmlFor`), e não só por serem palavras reservadas. HTML aceita tags sem fechar; o XHTML é que segue XML. Ver [[wiki/concepts/jsx]].
- **A `baseURL` fixa** repete o problema do `image_url` do dia 2: o endereço deve vir de variável de ambiente (`REACT_APP_API_URL` no CRA, `VITE_*` no Vite). Ver [[wiki/concepts/variaveis-de-ambiente]].
- **"Ítens" com acento** está errado: paroxítonas terminadas em -ens não levam acento. Mayk tinha acertado no [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta|dia 4 da outra trilha]].
- **WhatsApp sem `type="tel"`.** `tel` abre o teclado numérico no celular e aceita `+` e espaços; `number` (cogitado) seria errado, porque remove zeros e aceita `e`.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react]]: biblioteca de UI
- [[wiki/entities/typescript]]: props, generics, tipos de evento
- [[wiki/entities/create-react-app]]: estrutura inicial
- [[wiki/entities/react-router]]: rotas SPA
- [[wiki/entities/leaflet]]: mapa com react-leaflet e OpenStreetMap
- [[wiki/entities/axios]]: cliente HTTP com `baseURL`
- [[wiki/entities/ibge]]: API de localidades
- [[wiki/entities/feather-icons]]: ícones via react-icons
- [[wiki/entities/google-fonts]]: Roboto e Ubuntu
- [[wiki/entities/vs-code]]: Emmet em JSX, FiraCode
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: React DevTools, Twitter, Figma, Notion, Microsoft Office, Font Awesome, Material Icons, Google Maps, OpenStreetMap, TypeScript React Cheatsheet, Thiago (designer).

## Conceitos

[[wiki/concepts/jsx]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/props-react]] · [[wiki/concepts/generics-typescript]] · [[wiki/concepts/useState]] · [[wiki/concepts/imutabilidade]] · [[wiki/concepts/useEffect]] · [[wiki/concepts/race-condition]] · [[wiki/concepts/server-state]] · [[wiki/concepts/componente-controlado]] · [[wiki/concepts/virtual-dom]] · [[wiki/concepts/dom]] · [[wiki/concepts/renderizacao-ssr-vs-csr]] · [[wiki/concepts/single-page-application]] · [[wiki/concepts/client-side-routing]] · [[wiki/concepts/geolocation-api]] · [[wiki/concepts/fetch-api]] · [[wiki/concepts/promise-javascript]] · [[wiki/concepts/callback-javascript]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/listas-html]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/variaveis-de-ambiente]]

## Open Questions

- O dia 4 está em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]. O dia 4 (React Native + Expo) deve consumir `GET /points` e `GET /points/:id`, com deep link para o WhatsApp e Mail Compose.
- O upload de imagens (campo do formulário e back-end) continua pendente. Provavelmente no dia 5.
- A legenda perdeu um trecho logo depois de `import api from '../../services/api'`: uma sequência de pontos, marcada como `[…]` no raw. Ali estava o começo da explicação de por que não chamar a API no corpo do componente.
- Data provável: 3 de junho de 2020 `[external, não verificado]`.
