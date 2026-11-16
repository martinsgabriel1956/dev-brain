---
type: concept
title: "Gerenciador de Pacotes (CPAN, Bundler, npm, Bower)"
aliases: ['package manager', 'npm']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 8
tags: [dependencias, npm, build, historia]
skill: tech-mentor-frontend
status: draft
---

# Gerenciador de Pacotes (CPAN, Bundler, npm, Bower)

Substitui baixar bibliotecas manualmente (zip por site). Perl: CPAN; Ruby: Bundler (também **versões corretas**); JavaScript: npm (padrão de fato, só ficou usável após concorrentes como Yarn), Bower. Alimenta o [[wiki/concepts/pipeline-de-assets]].

Hoje o npm vem junto com o [[wiki/entities/nodejs]]; Yarn e pnpm são as alternativas mais citadas, e o guia do [[wiki/entities/vue]] mostra o comando de criação de projeto para npm, pnpm, Yarn e Bun ([[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]). A fonte define dependência como pacote de que o projeto precisa para rodar, como uma biblioteca de calendário pronta. O `-g` muda onde o pacote fica: ver [[wiki/concepts/instalacao-global-vs-local]]. Ver [[wiki/concepts/historia-do-front-end]].

## Yarn no FrontPUSH

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], [[wiki/entities/nasser|Násser]] pede para instalar o Yarn ("yarn for windows") além do npm que vem com o [[wiki/entities/nodejs]]: no React vai aparecer `npm install alguma coisa` ou `yarn add alguma coisa`. `[external]` O Yarn 2+ se ativa pelo Corepack (`corepack enable`); o instalador de Windows é do Yarn 1 (Classic): https://yarnpkg.com/getting-started/install.

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: npm é o "Node Package Manager", o "gerenciador de dependências do Node". `npm init -y`, `npm install express` e `npm install nodemon -D` criam o `node_modules` e o `package-lock.json`. Ver [[wiki/concepts/package-json]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], dois níveis: npm para bibliotecas (comparado a Composer, pip e RubyGems) e gerenciadores do sistema (Homebrew, Chocolatey, apt) para instalar o próprio Node. `[skill: lang-dynamic]` Para alternar versões, use nvm, fnm, Volta ou mise.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], npm é o "gerenciador de pacotes do Node", de "sub-aplicações": `npm init -y`, `npm install express`, `npm install nunjucks` e `npm install nodemon -D`. Tensão: `-D` grava em devDependencies, na mesma `node_modules`.

## Na NLW #2, dia 1 (Diego Fernandes)

Node, npm e Yarn ("opcional, porém recomendável"); `yarn create react-app` ou `npx create-react-app`; `yarn.lock` com as versões; o `node_modules` cresce porque "cada dependência tem suas próprias dependências". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## No JStack, aula 03

Em [[wiki/sources/jstack-o-que-sao-modulos]], os pacotes do npm são o terceiro tipo de módulo: "um lugar pra gente conseguir publicar esses módulos que a gente cria [...] com a comunidade". O uso fica para o capítulo seguinte. O npm publica pacotes (pasta com `package.json`), não arquivos soltos. Ver [[wiki/concepts/modulos-nodejs]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Yarn ao lado do npm; `npm install` x `yarn add`
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: npm init, install, -D
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: npm x Composer/pip/RubyGems; Homebrew e Chocolatey para o Node
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: init, install, -D
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: yarn create, npx, yarn.lock e dependências transitivas
- [[wiki/sources/jstack-o-que-sao-modulos]]: npm como terceiro tipo de módulo
