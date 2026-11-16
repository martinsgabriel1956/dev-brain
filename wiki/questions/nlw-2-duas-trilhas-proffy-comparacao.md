---
type: question
title: "NLW #2: as duas trilhas do Proffy (Mayk x Diego), o que muda e o que cada uma deixa de fora"
aliases: ["Proffy Mayk x Diego", "NLW 2 trilhas comparadas", "NLW 2 starter x Node React React Native"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 10
tags: [nlw, proffy, comparacao, ssr, csr, api-rest, nunjucks, react, react-native, sqlite, knex, typescript, seguranca, validacao, rocketseat]
skill: tech-mentor-frontend
status: draft
---

# NLW #2: as duas trilhas do Proffy (Mayk x Diego)

**A pergunta:** a [[wiki/entities/next-level-week|NLW #2]] da [[wiki/entities/rocketseat]] construiu o mesmo produto em duas trilhas de cinco dias. O produto é o Proffy, a plataforma para quem quer estudar ou dar aulas, com layout do Thiago. O que muda entre as duas, o que cada uma ensina e que falhas aparecem em uma, na outra ou nas duas? E o que mudou desde a [[wiki/questions/nlw-1-duas-trilhas-ecoleta-comparacao|comparação da NLW #1]]?

Esta página é uma síntese das dez fontes da wiki. Nada aqui vem de fora, salvo o que está marcado.

## As duas trilhas em uma tabela

| | Trilha de [[wiki/entities/mayk-brito]] | Trilha de [[wiki/entities/diego-fernandes]] |
|---|---|---|
| Linguagem | JavaScript | TypeScript, desde o [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy\|dia 1]] |
| Arquitetura | Monólito com HTML montado no servidor pelo [[wiki/entities/nunjucks]] ([[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy\|dia 4]]) | [[wiki/concepts/api-rest\|API REST]] JSON e dois clientes, uma SPA web e um app nativo ([[wiki/concepts/renderizacao-ssr-vs-csr]]) |
| Dias 1–3 | HTML e CSS puros, depois JS puro no [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy\|dia 3]] | [[wiki/entities/react]] com CRA e [[wiki/entities/react-router]]; a API fica no dia 2, e o formulário com Axios, no [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy\|dia 3]] |
| "Novo horário" | `cloneNode(true)` + limpar inputs + `appendChild` | Estado com `[...scheduleItems, novo]` ([[wiki/concepts/useState]], [[wiki/concepts/imutabilidade]]) |
| Landing no desktop | [[wiki/concepts/css-grid\|Grid]] `2fr 1fr 2fr` ([[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy\|dia 2]]) | Grid `2fr 1fr 1fr`, com outra divisão de áreas |
| Mobile | Só responsividade (mobile first com media queries) | [[wiki/entities/react-native]] + [[wiki/entities/expo]], pilha e abas com [[wiki/entities/react-navigation]] ([[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy\|dia 4]]) |
| Banco | [[wiki/concepts/sqlite]] pelo `sqlite-async`, SQL escrito à mão ([[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy\|dia 5]]) | SQLite via [[wiki/entities/knex]], com migrations e transação ([[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy\|dia 2]]) |
| Tabelas | `proffys`, `classes`, `class_schedule` | `users`, `classes`, `class_schedule` e `connections` |
| Contador de conexões | Texto fixo ("200 conexões") | Tabela `connections` e `GET /connections`, contando cliques no WhatsApp |
| Horário | Em minutos, por `convertHoursToMinutes` | Em minutos, por `split(':').map(Number)` |
| Pós-cadastro | `POST` → redirect para `/study` já filtrado | `alert` + `history.push('/')` |
| Favoritos | — | `AsyncStorage` no app ([[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy\|dia 5]]) |
| Fechamento | Três desafios (um deles, a versão 2.0 do layout) e o aviso de que não haverá turma do Launchbase | A "versão 2.0" como desafio: login, perfil, upload, paginação infinita, cadastro de aulas no app |

## O que cada trilha ensina melhor

- **Mayk ensina a plataforma.** Na NLW #2, ele vai mais fundo no CSS que na NLW #1: [[wiki/concepts/especificidade-css]], [[wiki/concepts/heranca-css]], [[wiki/concepts/unidades-de-medida-css|px x % x rem x em]], [[wiki/concepts/mobile-first]], `:focus-within::after` e `position`. No back-end, mostra um formulário HTML de verdade, com `method="post"`, `req.body` e redirect depois do POST.
- **Diego ensina a arquitetura.** Contrato JSON, [[wiki/concepts/database-migration|migrations]], [[wiki/concepts/database-transactions|transação]], [[wiki/concepts/componente-controlado|componentes controlados]], estado imutável, navegação em pilha e em abas, e armazenamento local no celular.
- **A comparação direta mais útil continua sendo o modelo de renderização.** O mesmo cadastro aparece de duas formas. Num, `<form method="post">` vai para o Express, que grava e redireciona. No outro, o estado do React vai por `api.post` para uma API que devolve 201. Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **O mesmo "botão de adicionar horário"** é a melhor aula sobre o que o React esconde. Mayk copia nós do DOM e precisa limpar os valores copiados à mão. Diego acrescenta um objeto ao array e deixa o React redesenhar a lista.

## Falhas: de quem são

| Falha | Mayk | Diego |
|---|---|---|
| [[wiki/concepts/sql-injection]] | Sim, em toda a SQL: o `INSERT` e a busca são montados por template string com `req.body` e `req.query`. É pior que na NLW #1, cujo `INSERT` usava `?` | Não para valores, porque o Knex parametriza. Mas o `whereRaw` usa `??` (binding de identificador) onde seria `?` |
| Conversão de horário | Bug: `540 + "00"` concatena, e "09:30" vira 54030. O filtro só funciona porque cadastro e busca usam a mesma função | Correta (`map(Number)`) |
| Transação | Nenhuma: um erro nos horários deixa professor e aula gravados pela metade | Manual, com `commit` e `rollback` corretos (ao contrário da NLW #1, em que faltava o `commit`) |
| Chaves estrangeiras | `REFERENCES` sem `PRAGMA foreign_keys = ON` | `onDelete('CASCADE')` sem o mesmo PRAGMA, então não roda |
| [[wiki/concepts/validacao-de-entrada]] no servidor | Nenhuma: `push(req.query)` no dia 4, `req.body` direto no dia 5 | Nenhuma no `POST /classes`, e `as string` mascara arrays em `request.query` |
| Consulta | — | `select('classes.*', 'users.*')`: o `id` da aula é sobrescrito pelo do usuário |
| Status HTTP | — | 400 para "erro inesperado", que deveria ser 500 |
| Erros assíncronos | — | Handlers `async` sem `try/catch` no Express 4. No front, a busca não tem tratamento de erro, loading nem estado vazio |
| Estado no cliente | — | A key `week_day` se repete no primeiro clique. O `useState(favorited)` não acompanha a prop, que é a causa real do favorito que não some. E `splice(-1, 1)` apaga o favorito errado |
| [[wiki/concepts/acessibilidade]] | `label for` "aponta para o name"; os clones ficam sem `id`; o `select` fica sem indicador de foco | `id` repetido em cada linha de horário; no mobile, `BorderlessButton` sem rótulo |
| Datado em 2026 | Node 12, Express 4 | Também CRA, React Router v5 (`useHistory`), `React.FC` com `children` implícito, `ReactDOM.render`, `expo init`, `AppLoading`, `tabBarOptions` |

**Leitura:** o padrão da [[wiki/questions/nlw-1-duas-trilhas-ecoleta-comparacao|NLW #1]] se repete e fica mais nítido.
- **Mayk:** a trilha mais simples comete as falhas mais graves e mais fáceis de ver, a SQL injectável e o bug de concatenação.
- **Diego:** a trilha mais sofisticada erra no que a abstração esconde: o binding errado do Knex, o `id` sobrescrito no join, o estado inicial que não segue a prop.
- **Progresso desde a NLW #1:** Diego acertou a transação, e Mayk acertou o redirect depois do POST.

## O que as duas compartilham

- **O mesmo design e o mesmo modelo de dados:** o layout do Thiago e a divisão entre professor, aula e horário ([[wiki/concepts/normalizacao-de-dados]]). Nos dois, o horário é guardado em minutos e filtrado por `time_from <= x AND time_to > x`.
- **As mesmas lacunas:**
  - O link do WhatsApp usa o número sem normalizar e o texto sem `encodeURIComponent` (Mayk no dia 4; Diego no dia 3 e no dia 5 do mobile).
  - Nenhuma das duas valida o cadastro no servidor ([[wiki/concepts/confiar-no-frontend]]).
- **As mesmas imprecisões de fala:**
  - "A porta padrão é 80": Mayk no dia 4, Diego no dia 2. Ver [[wiki/concepts/porta-de-rede]].
  - "Força" ou "poder" onde o certo é especificidade: Mayk nos dias 1 a 3, Diego no dia 1.
  - `rem` descrito como relativo à tela ou ao elemento.
- **A mesma raiz em 60%** (`1.6rem` = 15,36 px, e não 16 px), nos dois casos abaixo do limite em que o Safari do iOS dá zoom no input `[external, não verificado]`.

## Em aberto

- Qual trilha um iniciante deveria fazer primeiro? As fontes não dizem. *Inferência:* Mayk → Diego, como na NLW #1, porque a trilha de Diego assume JavaScript, HTTP e CSS que a de Mayk constrói.
- A data de cada dia (agosto de 2020) segue `[external, não verificado]` nas dez fontes.
- As transcrições não dão o nome oficial de nenhuma das trilhas.
- As duas fecham com a "versão 2.0" como desafio. As fontes não dizem se alguma trilha voltou depois para corrigir a SQL injectável (Mayk) ou o bug dos favoritos (Diego).

## Key sources

- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]
