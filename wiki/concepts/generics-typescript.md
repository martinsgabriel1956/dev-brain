---
type: concept
title: "Generics (TypeScript)"
aliases: ["generic", "genéricos", "tipo genérico", "type parameter"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [typescript, tipagem, sistema-de-tipos]
skill: tech-mentor-frontend
status: stub
---

# Generics (TypeScript)

Parâmetros de tipo: um tipo ou função que recebe outro tipo entre `< >`, como `Array<T>`, `useState<T>` e `axios.get<T>`. Escreve-se o código uma vez e cada uso dá o tipo concreto, sem perder a checagem. Ver [[wiki/concepts/sistema-de-tipos]].

Para [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), um generic é "um tipo do TypeScript que pode receber um parâmetro". "O nome é generic, mas eu estou falando parâmetro porque eu acho mais fácil de fazer uma relação." Os usos na aula:

- `React.FC<HeaderProps>` diz quais props o componente aceita ([[wiki/concepts/props-react]]).
- `useState<Item[]>([])`, porque um array vazio seria inferido como `never[]` ("property title does not exist on type never").
- `useState<[number, number]>([0, 0])`, uma tupla para latitude e longitude.
- `axios.get<IBGEUFResponse[]>(url)` tipa o `response.data`.
- `ChangeEvent<HTMLSelectElement>` diz de que elemento o evento vem.

**Limite:** em `axios.get<T>`, o T é uma promessa do programador, não uma verificação. Dados externos precisam de validação em runtime. Ver [[wiki/entities/typescript]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `useState<[number, number]>` como tupla e `{} as Data` como asserção. Um generic tipa; um `as` só afirma.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: React.FC, useState, axios e ChangeEvent com generics
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: tupla e asserção no app
