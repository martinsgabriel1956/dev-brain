---
type: entity
title: "Axios"
aliases: ["axios"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
tags: [http, javascript, cliente-http, biblioteca]
skill: tech-mentor-frontend
status: stub
---

# Axios

Cliente HTTP baseado em promises para navegador e Node. Faz serialização JSON automática, tem `baseURL` e interceptors, e rejeita a promise em status 4xx/5xx (o [[wiki/concepts/fetch-api|fetch]] não rejeita).

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]): `axios.create({ baseURL: 'http://localhost:3333' })` em `services/api.ts` concentra o endereço da API ("basta eu trocar aqui dentro"), e `api.get('items')` e `api.post('points', data)` completam o caminho. Para a API do IBGE, usa-se o `axios` direto, sem a `baseURL`. O tipo da resposta vai no genérico: `axios.get<IBGEUFResponse[]>(...)` ([[wiki/concepts/generics-typescript]]).

**Ressalvas:**

- **Não valida nada:** o genérico só *afirma* o formato; quem garante é um schema (Zod) na resposta.
- **A `baseURL` deve vir de [[wiki/concepts/variaveis-de-ambiente]].**
- **`fetch` como alternativa:** hoje um wrapper fino sobre o `fetch`, ou o TanStack Query para estado de servidor ([[wiki/concepts/server-state]]), cobre o mesmo uso sem dependência. `[skill: tech-mentor-frontend]`

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o app mobile repete o `services/api.ts`, agora com o IP da máquina (`192.168.1.13`) na `baseURL`, e envia `params: { items: [1, 2] }`, que o Axios serializa como `items[]=1&items[]=2`.

## Na NLW #2, dia 3 (Diego Fernandes)

Proffy: `axios.create({ baseURL: 'http://localhost:3333' })` em `services/api.ts`; `get('connections')`, `post('classes', data)`, `get('classes', { params })` e `post('connections', { user_id })`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

No app: mesmo `services/api.ts` da web, com o IP da máquina; `get('connections')`, `get('classes', { params })` e `post('connections')`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], o Axios aparece entre os exemplos de JavaScript assíncrono do FrontPUSH, ao lado de AJAX, Promises, Fetch e async/await ([[wiki/concepts/javascript-assincrono]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], o Axios é anunciado como a forma "um pouquinho mais fácil" de tratar requisições com Promise, depois de embrulhar o XHR à mão.

## No FrontPUSH, JavaScript aula 16

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], [[wiki/entities/nasser|Násser]] apresenta o Axios como "um encapsulamento do XML HTTP request" que "já suporta uma API de promise": a Promise com XHR da aula 15 ("o tamanho da parafernália") vira `axios.get(url).then(...)`. Carrega por CDN porque o ambiente com npm/yarn fica para quando houver framework. O objeto "mais completo" é o envelope `{ data, status, headers, config, request }`: os dados estão em `response.data`, e o cache-control fica em `headers`, não em `config`. Falta o `.catch` (o Axios rejeita em 4xx/5xx).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: services/api.ts, baseURL, get/post tipados
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: baseURL com IP; serialização de arrays em params
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: Proffy: baseURL e params
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: Proffy mobile com IP local
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: Axios na lista do assíncrono
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: Axios anunciado como atalho
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: axios.get via CDN; envelope da resposta
