---
type: entity
title: "TypeScript"
aliases: ["TS", "tsc"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 8
tags: [linguagem, typescript, javascript, tipagem, microsoft]
skill: lang-dynamic
status: stub
---

# TypeScript

Superset do JavaScript, mantido pela Microsoft, que acrescenta tipos estáticos checados antes da execução. Para [[wiki/entities/diego-fernandes]], é "o JavaScript com superpoderes" ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]). Ver [[wiki/concepts/sistema-de-tipos]].

- **Para que serve:** documentar o formato dos dados no próprio código. Com isso, o editor (IntelliSense do [[wiki/entities/vs-code]]) sabe se o campo é `user.city` ou `user.address.city` sem um `console.log`.
- **Inferência de tipos:** na maior parte do código, o compilador deduz o tipo sozinho; Diego estima que "10%, 15% dos casos" pedem anotação, sem fonte.
- **Bibliotecas JS:** precisam de um [[wiki/concepts/arquivo-de-declaracao-de-tipos|arquivo de declaração]] (`.d.ts`), embutido no pacote ou publicado em `@types/*`.
- **Execução:** o `tsc` gera JavaScript, configurado pelo `tsconfig.json` (`npx tsc --init`). Em 2020 a aula usava `ts-node`. `[skill: lang-dynamic]` Hoje o Node 24+ roda `.ts` direto por *type stripping* (sem `enum`, decorators e outras sintaxes que geram código, `erasableSyntaxOnly`), e `tsx` substitui o `ts-node` em desenvolvimento. Ver [[wiki/concepts/transpilador]].
- **Não substitui o JavaScript:** o código final continua sendo JS. As novidades do JavaScript entram no TypeScript quando as propostas do TC39 chegam ao estágio 3, não "de forma automática". `[skill: lang-dynamic]`

Relacionado: [[wiki/concepts/tipagem-com-jsdoc]], a alternativa que mantém `.js` e escreve os tipos em comentários.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: `Number(request.params.id)` e `String(request.query.search)` só para calar o compilador (não validam), `import Knex from 'knex'` como tipo para destravar o autocomplete, e `Request`/`Response` do Express nos controllers.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: `interface` para props e respostas de API, generics em `React.FC<P>`, `useState<Item[]>`, `axios.get<T>` e `ChangeEvent<HTMLSelectElement>`, e a regra "sempre que a gente cria um estado para um array ou objeto, a gente precisa manualmente informar o tipo" (senão vira `never[]`).

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: `require` em vez de `import` para PNG (TS sem declaração de módulo), `useState<[number, number]>`, e asserções `route.params as Params` e `{} as Data` para "burlar o sistema do TypeScript", sem checagem em runtime.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: `useState<File>()`, `interface Props { onFileUploaded: (file: File) => void }` e o TS reclamando de `selectedFile` possivelmente indefinido no `FormData` ("o TypeScript já ajuda a gente a evitar esses errinhos").

## Na NLW #2, dia 1 (Diego Fernandes)

Template `--template typescript` no CRA ("a tipagem auxilia na sua produtividade"), `interface PageHeaderProps`, `React.FC<>` e `@types/react-router-dom`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 2 (Diego Fernandes)

`tsc --init`, `target: ES2017`, `interface ScheduleItem` em vez de `any` ("qualquer coisa é muito aberto"), `Request`/`Response` do Express e `as string` nos filtros. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`InputHTMLAttributes<HTMLInputElement>` (chamado de "global do Visual Studio Code", mas vem do `lib.dom.d.ts`), `FormEvent`, `Array<{ value: string; label: string }>` e `export interface Teacher` reaproveitada. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: definição, função esquecida e IntelliSense, cinco mitos, `@types/express`, `ts-node`, `tsc --init`
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: tipos Knex, Request e Response; Number/String como coerção
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: props, generics, estado e eventos tipados no React
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: asserções de tipo em parâmetros de rota
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: File, callback tipado e undefined
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: template, interface de props e @types
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: interface, any e as string na API
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: HTMLAttributes, FormEvent e interfaces exportadas
