---
type: entity
title: "Axios"
aliases: ["axios"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
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

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: services/api.ts, baseURL, get/post tipados
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: baseURL com IP; serialização de arrays em params
