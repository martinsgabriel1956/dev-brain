---
type: source
title: "NLW #2 com Diego Fernandes, dia 3: formulário de aulas, estado e conexão do front-end do Proffy com a API"
aliases: ["NLW 2 Diego dia 3", "Proffy dar aulas", "Proffy front-end conectado", "NLW 2 trilha React dia 3"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react, typescript, useState, useEffect, imutabilidade, componente-controlado, renderizacao-condicional, props, rest-spread, input-html-attributes, fieldset, legend, select, textarea, key, axios, react-router, useHistory, whatsapp, css-grid, frontend, lang-dynamic, rocketseat, proffy, iniciante]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2 com Diego Fernandes, dia 3: formulário de aulas, estado e conexão do front-end do Proffy com a API

## TL;DR

Terceira aula (cerca de 1h58) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #2]]. Ela fecha o front-end do Proffy, iniciado no [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy|dia 1]], e o liga à API do [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy|dia 2]]. São três blocos:

1. **O formulário "dar aulas".**
   - `description` opcional no `PageHeader`, com [[wiki/concepts/renderizacao-condicional|`&&`]].
   - `main` com três [[wiki/concepts/formulario-html|`fieldset`/`legend`]] e rodapé com aviso e botão.
   - Componentes `Input`, `Textarea` e `Select` que estendem `InputHTMLAttributes<HTMLInputElement>` (e equivalentes) e repassam o resto com rest/spread ([[wiki/concepts/props-react]]).
   - O `Select` recebe `options` e as renderiza com `map` e [[wiki/concepts/virtual-dom|`key`]].
   - CSS mobile-first, com grid no desktop.
2. **Estado.**
   - O React é declarativo: não se faz `append` na DOM, muda-se o array e o React redesenha.
   - [[wiki/concepts/useState|`useState`]] e [[wiki/concepts/imutabilidade]] (`[...scheduleItems, novo]`) para os horários "infinitos".
   - [[wiki/concepts/componente-controlado|Inputs controlados]] (`value` + `onChange`) e o `setScheduleItemValue(index, field, value)` com `map` e chave computada.
3. **Conexão com a API.**
   - [[wiki/entities/axios]] com `baseURL`.
   - [[wiki/concepts/useEffect|`useEffect(..., [])`]] para o total de conexões.
   - `api.post('classes')` + `useHistory().push('/')` ([[wiki/entities/react-router]]).
   - `api.get('classes', { params })` com async/await nos filtros.
   - `TeacherItem` tipado com `interface Teacher` exportada.
   - O link `wa.me` do WhatsApp e um `api.post('connections')` a cada clique.

## Key Claims

### Descrição opcional e renderização condicional

- **`description?: string`:** o `?` torna a prop opcional; o `TeacherList` não a envia e o `TeacherForm` envia "O primeiro passo é preencher esse formulário de inscrição".
- **Duas formas de `if` no JSX:**
  - o ternário `{props.description ? <p>...</p> : null}`;
  - e, sem `else`, `{props.description && <p>...</p>}`, porque com `&&` "a segunda parte da operação [...] só vai ser executada se a primeira parte for [...] truthy", isto é, "não é zero, não é nulo, não é undefined, não é vazio".
  - Ver [[wiki/concepts/renderizacao-condicional]] e as tensões.

### O formulário: main, fieldsets e legend

- **Semântica:** a caixa branca é o `main`, e cada bloco é um `fieldset` ("Seus dados", "Sobre a aula", "Horários disponíveis"): "é legal a gente utilizar as tags do HTML a nosso favor", em vez de `div`. Ver [[wiki/concepts/html-semantico]] e [[wiki/concepts/formulario-html]].
- **CSS:**
  - `.page-teacher-form main` com `max-width: 74rem` ("os nossos 740 pixels"), `margin: -3.2rem auto 3.2rem` para subir sobre o header, `padding-top` e `overflow: hidden`.
  - `fieldset + fieldset { margin-top: 6.4rem }`.
  - O `legend` tem flex com `space-between` "para já prever" o botão "+ Novo horário" à direita, e `border-bottom`.
- **Rodapé:** `footer` com ícone de aviso, "Importante! Preencha todos os dados" (`<br />` precisa fechar no React) e o botão "Salvar cadastro", com hover em `transition: background-color 0.2s`. O `--color-secundary` estava escrito errado no projeto, e Diego deixa assim "para não mexer com a sua cabeça".
- **Desktop (≥ 700 px):**
  - `fieldset` com `padding: 0 6.4rem` e rodapé em flex com `space-between`.
  - `.schedule-item { display: grid; grid-template-columns: 2fr 1fr 1fr; column-gap: 1.6rem }`: o dia ocupa metade, e "das" e "até", um quarto cada.
  - `margin-top: 0 !important` dentro do item.
  - Ver [[wiki/concepts/css-grid]] e [[wiki/concepts/especificidade-css]].

### Os componentes Input, Textarea e Select

- **Por que extrair:** o input do cadastro "é exatamente igual" ao da busca, então vira `components/Input`, com o CSS movido de `TeacherList` para lá. A cor da label fica de fora, porque "só é diferente dentro da página Teacher List". Ver [[wiki/concepts/componentizacao]].
- **Tipagem que aceita tudo:**

```tsx
interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  name: string;
  label: string;
}

const Input: React.FC<InputProps> = ({ label, name, ...rest }) => (
  <div className="input-block">
    <label htmlFor={name}>{label}</label>
    <input type="text" id={name} {...rest} />
  </div>
);
```

  - Com isso, o componente pode receber "todos os atributos que um input tradicional do HTML já receberia" (`required`, `maxLength`, `autoFocus`, `onBlur`): "a gente não pode limitar o usuário".
  - O `...rest` dos parâmetros é o rest operator; o `{...rest}` no JSX é o spread.
  - O teste é `type="time"`, que no Chrome traz seletor de horário ("no Firefox, eu acho que a gente não tem").
  - Ver [[wiki/concepts/props-react]], [[wiki/concepts/generics-typescript]] e [[wiki/concepts/desestruturacao-javascript]].
- **Textarea:** cópia do Input com `TextareaHTMLAttributes`, altura de 16 rem, `min-height: 8rem` e `resize: vertical`. A linha de foco do `::after` precisou de `bottom: 7px` "pelo que eu entendi [...] por causa dessa opção do resize".
- **Select:** recebe uma prop nova, `options: Array<{ value: string; label: string }>`, em vez de `<option>` como filhos ("de uma forma mais legal").
  - As opções são renderizadas com `options.map(option => <option key={option.value} value={option.value}>{option.label}</option>)`.
  - Sem `key`, o console acusa "each child in a list should have a unique key prop". A key vai "somente no primeiro elemento dentro do map" e "ajuda o React a conseguir identificar os elementos em tela". Ver [[wiki/concepts/virtual-dom]] e [[wiki/concepts/listas-html]].
  - O placeholder é `<option value="" disabled hidden>Selecione uma opção</option>`, e o `selected` sai a pedido do React, que quer o valor no `value`/`defaultValue` do `select`.
  - As matérias ditas na gravação são Artes, Biologia, Ciências, Educação Física, Português e Química, e outras entram fora da fala (Geografia aparece no teste). Os dias vão de 0 (domingo) a 6. O `React Select` fica citado como alternativa completa.

### Estado e interface declarativa

- **Conceito:** "sempre que a gente precisar manipular [...] algum valor através de uma ação do usuário [...] a gente vai criar um estado".
- **Declarativo:** no React "a gente não vai no HTML e diretamente vai lá e adiciona uma nova div", como no jQuery. "A nossa interface é montada a partir do nosso JavaScript", e basta pôr um item novo no array.
- **A demonstração em três passos:**
  1. `scheduleItems.push(...)` não muda nada na tela, porque "o React não fica observando variáveis comuns".
  2. Com `useState`, ainda não muda, porque "a gente não pode manipular diretamente": as variáveis do estado "não são modificáveis" ([[wiki/concepts/imutabilidade]]).
  3. Com `setScheduleItems([...scheduleItems, { week_day: 0, from: '', to: '' }])`, copiando o array com spread, o novo horário aparece.
  - Ver [[wiki/concepts/useState]] e as tensões.
- **A key dos horários** é o `week_day`, porque Diego vai "instruir o usuário para que ele selecione apenas um dia da semana por item". Ver as tensões.

### Axios e o total de conexões

- **`services/api.ts`:** `axios.create({ baseURL: 'http://localhost:3333' })`, com `baseURL` "todo URL em maiúsculo". O back-end tem de estar rodando (`yarn start` na pasta `server`, conferido no [[wiki/entities/insomnia]]). Ver [[wiki/entities/axios]].
- **Estado inicial 0,** porque "esse processo de ir até a API [...] demora um pouquinho". Daria para mostrar um loading.
- **`useEffect`:** o primeiro argumento é a função, e o segundo é o "array de dependências": as informações "que quando forem alteradas vão disparar essa função novamente" (o exemplo é o total de likes). Com o array vazio, roda "apenas uma única vez, assim que o componente é exibido em tela". O corpo é `api.get('connections').then(response => { const { total } = response.data; setTotalConnections(total) })`. Ver [[wiki/concepts/useEffect]] e [[wiki/concepts/promise-javascript]].

### O formulário controlado e o envio

- **"A forma mais raiz possível":** "existem várias bibliotecas" para formulários, mas cada campo vira um estado (`name`, `avatar`, `whatsapp`, `bio`, `subject`, `cost`) com `value` e `onChange={e => setName(e.target.value)}`. "Não estranhe se vai ficar um pouco verboso demais." Ver [[wiki/concepts/componente-controlado]] e [[wiki/concepts/event-handler]].
- **Atalhos do VS Code:** multicursor e `Ctrl+Shift+L` ("select all occurrences of find match"), "essas mandingas do VS Code". Ver [[wiki/entities/vs-code]].
- **`<form onSubmit={handleCreateClass}>`** com o botão `type="submit"`. Sem `e.preventDefault()`, a página recarrega, porque esse é "o comportamento padrão de um formulário no HTML". Como a função é declarada fora do JSX, o evento precisa de tipo explícito, `FormEvent` do React.
- **Os horários:**
  - `map((scheduleItem, index) => ...)` passa o índice, e cada campo chama `setScheduleItemValue(index, 'week_day', e.target.value)`.
  - A função faz `scheduleItems.map((item, position) => index === position ? { ...item, [field]: value } : item)`. O `map` "sempre vai retornar o array com a mesma quantidade", o spread copia o item, e `[field]` é "uma forma de eu conseguir usar uma variável para definir o nome da propriedade".
  - O `input type="time"` exibe AM/PM, mas o valor sai em 24 horas ("o 6 aqui já virou 18").
- **Envio:** `api.post('classes', { name, avatar, whatsapp, bio, subject, cost: Number(cost), schedule: scheduleItems })`, com `.then(() => { alert('Cadastro realizado com sucesso!'); history.push('/') })` e `.catch(() => alert('Erro no cadastro!'))`.
  - O `week_day` vai como string, porque "o banco de dados vai conseguir converter".
  - Async/await aqui não teria "necessidade" por ser uma chamada só.
  - O `useHistory` é para redirecionar "depois que alguma ação acontece", e não por clique, que é o caso do `Link`.
  - O teste cadastra Vini Fraga (Geografia, R$ 120) e Thiago Marinho (Biologia), e confere no Insomnia.

### Filtros da listagem e TeacherItem

- **Estados `subject`, `week_day` e `time`** com `onSubmit={searchTeachers}`. Diego cogita buscar ao mudar o horário, mas desiste: "eu não quero fazer da maneira errada". Ele acrescenta um botão "Buscar" (`type="submit"`), porque o botão "seria muito melhor" para a acessibilidade. O grid do filtro passa a ter quatro colunas.
- **`api.get('classes', { params: { subject, week_day, time } })`:** no GET, os query params vão em `params`, e não como segundo argumento direto, que é como se faz "se for requisição do tipo post ou put". A função usa `async/await` e `setTeachers(response.data)`, com `useState([])` inicial. Ver [[wiki/concepts/query-string]] e [[wiki/concepts/async-await]].
- **`TeacherItem` com prop:** `{teachers.map((teacher: Teacher) => <TeacherItem key={teacher.id} teacher={teacher} />)}`. A `export interface Teacher { id; avatar; bio; cost; name; subject; whatsapp }` é importada pelo `TeacherList` "porque eu tô utilizando a mesma tipagem". Segundo Diego, a gente "só declara na interface o que eu for utilizar". O componente era "hard-coded" e passa a usar `teacher.name`, `teacher.avatar` e os demais. O preço fica sem formatação "por enquanto".

### Entrar em contato

- **Link do WhatsApp:** o botão vira `<a href={`https://wa.me/${teacher.whatsapp}`} target="_blank">`. Texto com variável exige template literal, porque com aspas "eu não posso usar uma variável dessa forma aqui, com chaves". O parâmetro `text` permitiria uma mensagem pronta.
- **Registrar a conexão:** `onClick={createNewConnection}` faz `api.post('connections', { user_id: teacher.id })` sem esperar a resposta. O contador da landing vai de 7 para 8. "Você achou que eu ia esquecer, né?"
- **Encerramento:** amanhã e sexta vem o mobile.

## Tensões e precisões

- **A key `week_day` duplica no primeiro clique.** O item inicial começa com `week_day: 0` e o novo também, então duas linhas com `key={0}` disparam o aviso de chave duplicada, e o React pode reaproveitar o elemento errado. Trocar o dia muda a key, o que desmonta a linha e faz o campo perder o foco. "Instruir o usuário" não garante a unicidade. O certo é um id próprio do item, gerado na criação (`crypto.randomUUID()`), ou o índice se a lista só cresce no fim. Ver [[wiki/concepts/virtual-dom]] e [[wiki/concepts/listas-html]].
- **`id` duplicado nos horários.** O `Input` usa `id={name}` e `htmlFor={name}`, então cada linha nova repete `id="from"` e `id="to"`. HTML com ids repetidos é inválido, e o clique na segunda label "Das" foca o input da primeira; o leitor de tela também se perde. Uma saída é `useId()` (React 18) ou um id derivado do índice. Ver [[wiki/concepts/acessibilidade]] e [[wiki/concepts/formulario-html]].
- **"Não são modificáveis" e "observar".** O JavaScript deixa o `push` acontecer. O React não observa variável nenhuma: ele re-renderiza quando o `set` é chamado e compara referências (`Object.is`). Mutar e passar o mesmo array ao `set` não muda nada, daí a cópia. Também se diz "conceito agora de mutabilidade" onde seria imutabilidade. A forma funcional, `setScheduleItems(items => [...items, novo])`, protege contra closures antigas. Ver [[wiki/concepts/imutabilidade]] e [[wiki/concepts/useState]].
- **`&&` com número renderiza o zero.** `{count && <p/>}` mostra "0" quando `count` é 0, porque o React renderiza números; strings vazias, `null`, `undefined` e `false` não aparecem. Para `description` (string) funciona; para contadores, o padrão seguro é `count > 0 &&` ou o ternário. Ver [[wiki/concepts/renderizacao-condicional]].
- **`target="_blank"` sem `rel`.** O aviso do ESLint (`react/jsx-no-target-blank`) foi dispensado ("Ah, tudo bem"). Desde 2021 os navegadores tratam `_blank` como `noopener` por padrão, então o risco de *tabnabbing* caiu, mas `rel="noopener noreferrer"` segue como boa prática `[external]` (https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/noopener).
- **O link do WhatsApp sem normalização.** O `wa.me` espera só dígitos com DDI ("55..."). O campo aceita qualquer texto, e o `text` exigiria `encodeURIComponent`. É a mesma lacuna registrada no [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|dia 4 do Mayk]]. Ver [[wiki/concepts/validacao-de-entrada]].
- **Busca sem erro, loading nem estado vazio.** O `await api.get` não tem `try/catch`: com um filtro faltando, a API devolve 400, a promise rejeita sem tratamento e a lista fica como estava. Não há "nenhum professor encontrado" nem indicador de carregamento. `[skill: tech-mentor-frontend]` Para estado de servidor, a skill recomenda TanStack Query (cache, loading, erro, refetch). Ver [[wiki/concepts/server-state]].
- **A conexão conta cliques, não contatos.** O `post` sem `await` dispara a cada clique, sem deduplicação, e o back-end aceita qualquer `user_id`. Diego já tinha admitido isso no [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy|dia 2]] ("não vai saber realmente se houve a conexão").
- **Strings no lugar de números.** `cost` vai convertido, mas o `week_day` dos horários segue como string. Funciona porque o SQLite aplica afinidade de tipo, mas é uma inconsistência que um Postgres estrito ou uma validação no back-end recusariam.
- **`HTMLInputElement` "global do Visual Studio Code"** não procede: é um tipo da DOM nas definições `lib.dom.d.ts` do TypeScript. O editor só mostra. A mesma frase apareceu no [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta|dia 3 da NLW #1]].
- **`React.FC` de novo,** com as mesmas ressalvas do dia 1 (o `children` implícito sumiu no React 18). `useHistory` virou `useNavigate` no React Router v6 `[external]` (https://reactrouter.com/6.30.0/upgrading/v5#use-usenavigate-instead-of-usehistory). Ver [[wiki/concepts/props-react]] e [[wiki/entities/react-router]].
- **`useEffect` sem cleanup** é aceitável aqui (uma leitura do total), mas no React 18 o `StrictMode` chama o efeito duas vezes em desenvolvimento. Ver [[wiki/concepts/useEffect]].
- **`!important` para zerar margem** resolve um conflito de especificidade criado pelos seletores `.input-block + .input-block`. Um seletor mais específico (`.schedule-item .input-block`) bastaria. Ver [[wiki/concepts/especificidade-css]].
- **Positivos:** `fieldset`/`legend`, botão "Buscar" no lugar do submit automático (por acessibilidade), `type="submit"`/`type="button"` explícitos, `InputHTMLAttributes` com rest/spread, `interface Teacher` compartilhada, `preventDefault` explicado e `alert` no erro do cadastro.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react]]: estado, efeitos, componentes
- [[wiki/entities/typescript]]: `InputHTMLAttributes`, `FormEvent`, interfaces exportadas
- [[wiki/entities/axios]]: cliente HTTP com `baseURL` e `params`
- [[wiki/entities/react-router]]: `useHistory`
- [[wiki/entities/insomnia]]: conferência dos cadastros
- [[wiki/entities/vs-code]]: multicursor, `Ctrl+Shift+L`, auto import
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: WhatsApp (`wa.me`, click to chat), jQuery, React Select, Discord, Chrome, Firefox, Vini Fraga e Thiago Marinho (professores de teste, da Rocketseat).

## Conceitos

[[wiki/concepts/useState]] · [[wiki/concepts/useEffect]] · [[wiki/concepts/imutabilidade]] · [[wiki/concepts/componente-controlado]] · [[wiki/concepts/renderizacao-condicional]] · [[wiki/concepts/props-react]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/generics-typescript]] · [[wiki/concepts/desestruturacao-javascript]] · [[wiki/concepts/virtual-dom]] · [[wiki/concepts/listas-html]] · [[wiki/concepts/event-handler]] · [[wiki/concepts/formulario-html]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/css-grid]] · [[wiki/concepts/especificidade-css]] · [[wiki/concepts/promise-javascript]] · [[wiki/concepts/async-await]] · [[wiki/concepts/query-string]] · [[wiki/concepts/server-state]] · [[wiki/concepts/validacao-de-entrada]]

## Open Questions

- O mobile começa em [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]. Os favoritos em storage local estão em [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].
- A formatação do preço (`Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' })`) ficou "para logo".
- A legenda manteve "Preula" no texto do botão "+ Novo horário" e "insgano" numa sobreposição de "se não me engano". Os dois ficaram literais no raw.
- Data provável: 5 de agosto de 2020 `[external, não verificado]`.
