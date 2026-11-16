---
type: question
title: "NLW #1: as duas trilhas do Ecoleta (Mayk x Diego), o que muda e o que cada uma deixa de fora"
aliases: ["Ecoleta Mayk x Diego", "NLW 1 trilhas comparadas", "NLW 1 starter x Node React React Native"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 10
tags: [nlw, ecoleta, comparacao, ssr, csr, api-rest, nunjucks, react, react-native, sqlite, knex, typescript, seguranca, validacao, rocketseat]
skill: lang-dynamic
status: draft
---

# NLW #1: as duas trilhas do Ecoleta (Mayk x Diego)

**A pergunta:** a [[wiki/entities/next-level-week|NLW #1]] da [[wiki/entities/rocketseat]] construiu o mesmo produto, o Ecoleta (o marketplace de pontos de coleta desenhado pelo Thiago), em duas trilhas de cinco dias. O que muda entre elas, o que cada uma ensina, e que falhas aparecem em uma, na outra ou nas duas?

Esta página é uma síntese das dez fontes da wiki. Nada aqui vem de fora, salvo o que está marcado.

## As duas trilhas em uma tabela

| | Trilha de [[wiki/entities/mayk-brito]] | Trilha de [[wiki/entities/diego-fernandes]] |
|---|---|---|
| Público | "Quem nunca programou" ([[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta\|dia 1]]) | Quem já programa; TypeScript desde o [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native\|dia 1]] |
| Linguagem | JavaScript | TypeScript |
| Arquitetura | Monólito com HTML montado no servidor (SSR), chamado de "full MVC" ([[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta\|dia 4]]) | [[wiki/concepts/api-rest\|API REST]] JSON e dois clientes, SPA web e app nativo ([[wiki/concepts/renderizacao-ssr-vs-csr]]) |
| Front-end | HTML, CSS e JS puro, `fetch` no IBGE, modal caseiro (dias 1–3) | [[wiki/entities/react]] com [[wiki/entities/react-router]] e [[wiki/entities/leaflet]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta\|dia 3]]) |
| Mobile | Só responsividade (media queries) | [[wiki/entities/react-native]] + [[wiki/entities/expo]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta\|dia 4]]) |
| Servidor | [[wiki/entities/express]] + [[wiki/entities/nunjucks]] (layout, partials, `{% for %}`) | Express + controllers (`index/show/create`), [[wiki/concepts/cors]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta\|dia 2]]) |
| Banco | [[wiki/concepts/sqlite]] pelo `sqlite3` cru, SQL escrito à mão ([[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta\|dia 5]]) | SQLite via [[wiki/entities/knex]]: migrations, seeds, transação |
| Modelagem | Uma tabela `places`, com os itens num campo de texto | `points`, `items` e a pivô `point_items` ([[wiki/concepts/relacionamento-muitos-para-muitos\|N:N]]) |
| Busca | `LIKE '%${search}%'` por cidade | `whereIn` por itens + igualdade de cidade e UF |
| Imagem do ponto | Campo `type="url"` (link colado) | Upload com [[wiki/entities/multer]] e Dropzone ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta\|dia 5]]) |
| Validação | `required` no HTML | celebrate + [[wiki/entities/joi]] no dia 5 |
| Fechamento | Venda do Launchbase (oito semanas, R$ 960) | GitHub, `.gitignore` e mapa de deploy |

## O que cada trilha ensina melhor

- **Mayk ensina a web por baixo.** Cliente-servidor, HTTP e portas, HTML semântico, [[wiki/concepts/box-model]], [[wiki/concepts/flexbox]] e [[wiki/concepts/css-grid]], DOM e eventos sem framework, SQL cru e [[wiki/concepts/template-engine]]. Quem faz essa trilha vê o que o React e o Knex escondem.
- **Diego ensina a arquitetura moderna.** O contrato JSON entre API e clientes, [[wiki/concepts/parametros-de-requisicao]], [[wiki/concepts/database-migration|migrations]] e [[wiki/concepts/seed-de-banco-de-dados|seeds]], [[wiki/concepts/database-transactions|transações]], componentes e estado ([[wiki/concepts/useState]], [[wiki/concepts/useEffect]]), [[wiki/concepts/navegacao-em-pilha]] e tipagem com [[wiki/entities/typescript]].
- **A comparação direta mais útil** é o modelo de renderização: o mesmo cadastro feito com `<form method="post">` e Nunjucks (SSR) e com `FormData` + Axios contra uma API (CSR). Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **O termo "full MVC"** aparece nos dois sentidos. Mayk chama assim o que constrói; Diego, o que evita ([[wiki/entities/mayk-brito]]). Nenhum dos dois é um termo usual: um é SSR monolítico, o outro é API + clientes.

## Falhas: de quem são

| Falha | Mayk | Diego |
|---|---|---|
| [[wiki/concepts/sql-injection]] | Sim: busca com interpolação no `LIKE` (dia 5) | Não: o Knex parametriza |
| [[wiki/concepts/xss]] | Risco no `innerHTML` com dados de API (dia 2). O Nunjucks escapa por padrão | XSS armazenado via upload sem filtro servido por `express.static` (dia 5) |
| [[wiki/concepts/validacao-de-entrada]] no servidor | Nenhuma | Só no dia 5, e incompleta (arquivo gravado antes, `uf` frouxa, imagem não obrigatória → 500) |
| Modelagem | Itens em texto, contra a 1FN | Pivô sem chave composta, aceita duplicatas |
| Falso positivo | — | O "rollback" do dia 2 só "funcionou" porque faltava o `trx.commit()`, e o SQLite vem com FKs desligadas |
| Concorrência no cliente | — | [[wiki/concepts/race-condition]] na troca de UF (web) e nas buscas de pontos (mobile) |
| Acessibilidade | Modal sem foco nem Esc (dia 3) | Itens como `li` clicável (web) e `TouchableOpacity` sem `accessibilityRole` (mobile) |
| URL e endereço fixos | — | `localhost`, depois o IP `192.168.1.13` e `.12`, editados à mão nos dias 2, 4 e 5 ([[wiki/concepts/variaveis-de-ambiente]]) |
| Persistência no deploy | Não discute deploy | Recomenda o Heroku, onde uploads em disco e o `database.sqlite` somem ([[wiki/concepts/sistema-de-arquivos-efemero]]) |
| Pós-POST | Render direto, sem PRG ([[wiki/concepts/post-redirect-get]]) | `alert` + `history.push` |
| Datado em 2026 | Express 4, Node 12 | Também CRA, React Router v5, react-leaflet v2, expo-cli global, React Navigation v5, `ReactDOM.render`, `React.FC` |

**Leitura:** a trilha mais simples comete o erro de segurança mais grave (SQL injection), e a mais sofisticada leva a complexidade a quebras mais sutis (transação sem commit, race, disco efêmero). Nenhuma das duas valida no servidor antes do último dia, e as duas confiam no que o cliente envia.

## O que as duas compartilham

- **O mesmo design e os mesmos dados:** o layout do Thiago, os seis itens de coleta, a API de localidades do [[wiki/entities/ibge]] e o SQLite como banco "que não precisa instalar nada".
- **A mesma lição de fundo:** separar front e back e dar ao servidor a responsabilidade pelas regras de negócio ([[wiki/concepts/arquitetura-cliente-servidor]]).
- **O mesmo padrão pedagógico:** CSS entregue pronto, desafios no fim (tela de sucesso, select com o IBGE no mobile, regex dos itens) e a promessa de que a prática vence a teoria ([[wiki/concepts/pratica-deliberada]]).

## Em aberto

- Qual trilha um iniciante deveria fazer primeiro? As fontes não dizem. *Inferência:* Mayk → Diego segue a ordem natural, a plataforma antes das abstrações. A trilha de Diego assume JavaScript e noções de HTTP que a de Mayk constrói.
- As datas de cada dia (1 a 5 de junho de 2020) seguem `[external, não verificado]` nas dez fontes.
- O nome oficial de cada trilha não aparece nas transcrições.

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]
