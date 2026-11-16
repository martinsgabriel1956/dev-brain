---
type: concept
title: "Arquivo de declaração de tipos (.d.ts e @types)"
aliases: [".d.ts", "@types", "DefinitelyTyped", "declaration file", "definição de tipos"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [typescript, tipagem, npm, dependencias]
skill: lang-dynamic
status: stub
---

# Arquivo de declaração de tipos (.d.ts e @types)

Um `.d.ts` descreve a forma de uma biblioteca JavaScript (funções, parâmetros, retornos, objetos) sem nenhum código executável. É por ele que o [[wiki/entities/typescript]] e o editor sabem o que um pacote escrito em JS oferece.

Há dois caminhos. A biblioteca pode trazer os tipos no próprio pacote (campo `types` no `package.json`), ou alguém os publica à parte no repositório DefinitelyTyped, que vira os pacotes `@types/<nome>` no npm.

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]):

- `import express from "express"` gera o aviso "could not find a declaration file for module express".
- A solução é `npm install @types/express -D`. Diego chama o `@types` de "o repositório que mantém a grande maioria das definições de tipos".
- Ctrl+clique em `express` abre o pacote de tipos: "Não existe código funcional aqui dentro".
- O `-D` (devDependency) faz sentido porque o build final é JavaScript e não precisa dos tipos. Ver [[wiki/concepts/package-json]].

`[skill: lang-dynamic]` Também dá para declarar tipos à mão: arquivos `.d.ts` com *ambient declarations* para módulos sem tipos, e *module augmentation* para estender um tipo existente, como acrescentar `user` no `Request` do Express.

Relacionado: [[wiki/concepts/sistema-de-tipos]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: `@types/react-router-dom` e `@types/react-leaflet` instalados à parte, enquanto o Axios já traz os tipos ("já vem, daí não preciso instalar").

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `import logo from './logo.png'` falha no TypeScript por falta de declaração de módulo para `*.png`, e Diego contorna com `require`. Hoje os templates do Expo trazem essas declarações.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], `@types/multer` e `@types/hapi__joi`: pacotes com escopo (`@hapi/joi`) viram `escopo__nome` no DefinitelyTyped. Hoje o `joi` traz os próprios tipos.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: aviso do import, `@types/express -D`, navegação até os tipos
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: @types de react-router-dom e react-leaflet; axios com tipos
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: declaração de módulo para imagens
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: convenção hapi__joi
