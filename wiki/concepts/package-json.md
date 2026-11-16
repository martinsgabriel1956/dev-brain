---
type: concept
title: "package.json"
aliases: ["package.json", "package-lock.json", "npm init", "manifesto do projeto Node"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [nodejs, npm, dependencias, json, tooling]
skill: lang-dynamic
status: stub
---

# package.json

O manifesto de um projeto Node, em [[wiki/concepts/json|JSON]]. Os campos principais:
- `name`, `version` e `main`.
- `scripts`, como `npm start` e `npm run dev`.
- `dependencies` para produção e `devDependencies` para desenvolvimento, com faixas semver (`^4.17.1`).

O `package-lock.json` grava as versões exatas resolvidas e deve ir para o repositório. É ele que o `npm ci` usa para reproduzir a instalação. O `node_modules` fica fora do Git (`.gitignore`). `[external]` (https://docs.npmjs.com/cli/v10/configuring-npm/package-json)

Ver [[wiki/concepts/gerenciador-de-pacotes]].

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] cria o arquivo com `npm init -y`. Por enquanto, dele importam "só o nome do projeto e o scripts":
- **`main`:** aponta para `src/server.js`.
- **`start`:** `node src/server.js`, depois `nodemon src/server.js`, com o nodemon em `devDependencies` (`npm install nodemon -D`).
- **Dependências:** o `npm install express` aparece em `dependencies`. Quem clona o projeto roda `npm install`, e "sozinho o npm já baixa de novo todas as dependências".
- **Aviso:** com o `package.json` aberto e não salvo durante a instalação, a dependência pode não ser gravada.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: `npm init -y`, `dependencies` x `devDependencies` (`-D` para `@types/express`, `ts-node`, `typescript`) e o script `dev`. Diego chama o `package-lock.json` de "arquivo de cache"; não é, é o lockfile, e vai para o repositório.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], `npm init -y` cria o `package.json`; as dependências aparecem nele, o `package-lock.json` "mapeia" a árvore e um script `dev` com nodemon roda por `npm run dev`.

## Key sources

- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: npm init -y, scripts start, dependencies e devDependencies; node_modules fora do Git
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: npm init -y, -D, script dev; package-lock como "cache" (incorreto)
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: script dev
