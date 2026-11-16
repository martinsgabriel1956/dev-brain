---
type: entity
title: "IBGE (API de localidades)"
aliases: ["IBGE", "Instituto Brasileiro de Geografia e Estatística", "servicodados.ibge.gov.br"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [orgao-publico, api, dados-abertos, brasil]
skill: tech-mentor-frontend
status: stub
---

# IBGE (API de localidades)

Instituto Brasileiro de Geografia e Estatística. Publica APIs abertas em servicodados.ibge.gov.br; a de localidades lista regiões, estados e municípios.

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `/api/v1/localidades/estados` (27 objetos com id, sigla, nome e região) para preencher o select de UF do Ecoleta e `/api/v1/localidades/estados/{UF}/municipios` para as cidades, com o id do estado (33 é o Rio de Janeiro, 11 Rondônia). Escolheu usar "um serviço que já existe na internet" para não preencher à mão. Ver [[wiki/concepts/fetch-api]] e [[wiki/concepts/json]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], a API de localidades alimenta os selects do formulário React: `/estados` para as siglas e `/estados/{UF}/municipios` num `useEffect` dependente da UF. A troca rápida de UF sem cleanup abre uma race condition.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o app mobile usa `TextInput` para UF e cidade e deixa o select com a API do IBGE (via `react-native-picker-select`) como desafio. A busca exige o nome exato da cidade.

## Key sources

- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: estados e municípios para o formulário do Ecoleta
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: selects de UF e cidade no React; race na troca de UF
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: desafio do select no mobile
