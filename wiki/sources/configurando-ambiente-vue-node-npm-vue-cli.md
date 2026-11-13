---
type: source
title: "Configurando o ambiente de desenvolvimento para Vue: Node, npm e o CLI do Vue"
aliases: ["ambiente vue node npm", "instalar vue cli", "npm install -g @vue/cli"]
date_created: 2026-11-12
date_updated: 2026-11-12
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/configurando-ambiente-vue-node-npm-vue-cli.md"
source_url: ""
author: "Não identificado"
date_published:
date_ingested: 2026-11-12
tags: [vue, vue-cli, nodejs, npm, yarn, pnpm, homebrew, gerenciador-de-pacotes, dependencias, ambiente-de-desenvolvimento, curso]
skill: tech-mentor-frontend
status: draft
---

# Configurando o ambiente de desenvolvimento para Vue: Node, npm e o CLI do Vue

**Formato:** transcrição de aula em vídeo (legenda automática, PT-BR), limpa sem alteração de conteúdo. É uma aula de curso: a anterior explicou o que é o Vue, e as próximas vão tratar de dependências e criação do projeto. O autor não se identifica.

## TL;DR

Aula introdutória que lista três pré-requisitos para trabalhar com [[wiki/entities/vue]]: [[wiki/entities/nodejs]], um [[wiki/concepts/gerenciador-de-pacotes]] (o npm, que já vem com o Node; Yarn e pnpm são citados como alternativas) e o Vue CLI. O autor mostra três formas de instalar o Node (apt-get no Linux, instalador do site no Windows e no Mac, Homebrew no Mac), confere as versões (Node 24.10.0, npm 11.6.0), instala o CLI com `npm install -g` e explica o `-g` como [[wiki/concepts/instalacao-global-vs-local|instalação global]]. Fecha com uma definição curta de dependência. O passo central está desatualizado: a documentação oficial diz que o Vue CLI está em modo de manutenção e recomenda o `create-vue` (`npm create vue@latest`), que não precisa de instalação global. Ver [[wiki/concepts/scaffolding-de-projeto]].

## Key Claims

1. **Para trabalhar com Vue são precisos três itens: Node, um gerenciador de pacotes e o CLI do Vue.** Confiança: alta para os dois primeiros, baixa para o terceiro. Hoje o guia oficial pede só Node.js e um gerenciador de pacotes; o projeto é criado com `npm create vue@latest` (também `pnpm create`, `yarn create`, `bun create`), que gera um projeto com Vite ([external](https://vuejs.org/guide/quick-start.html)). A página do Vue CLI avisa que ele está em modo de manutenção e que, para projetos novos, a recomendação é o `create-vue` ([external](https://cli.vuejs.org/guide/)). Ver [[wiki/concepts/scaffolding-de-projeto]].
2. **O Node já vem com o npm; Yarn e pnpm são alternativas.** Confiança: alta. O guia oficial mostra o comando de criação para npm, pnpm, Yarn e Bun ([external](https://vuejs.org/guide/quick-start.html)). Ver [[wiki/concepts/gerenciador-de-pacotes]].
3. **No Linux, instala-se o Node com `apt-get install`.** Confiança: média. Funciona, mas a fonte omite três detalhes: o pacote no Debian/Ubuntu se chama `nodejs`, o comando pede `sudo`, e o repositório padrão costuma trazer versão antiga. No Ubuntu 24.04 é a 18.19.1 ([external](https://packages.ubuntu.com/noble/nodejs)), abaixo do que o `create-vue` exige (`^22.18.0 || >=24.12.0`, campo `engines` no npm e no guia oficial). Um gerenciador de versões (nvm, fnm) ou o repositório do NodeSource evita esse problema `[skill: tech-mentor-frontend]`.
4. **No Windows e no Mac, baixa-se o instalador no site do Node; no Mac, também dá para usar o Homebrew (`brew install node`).** Confiança: alta. Na fala, o autor diz "o comando para instalar o Vue e o npm", mas o comando mostrado instala o Node; parece lapso de fala.
5. **Depois de instalar, o comando de versão mostra Node 24.10.0 e npm 11.6.0.** Confiança: média. O Node 24.10.0 saiu em 08/10/2025 com o npm 11.6.1 embutido ([external](https://nodejs.org/dist/index.json)). A fórmula do Homebrew compila o Node `--without-npm` e instala o npm à parte ([external](https://github.com/Homebrew/homebrew-core/blob/master/Formula/n/node.rb)), então uma versão de npm diferente da embutida é plausível. A 24.10.0 ainda não era LTS: a linha 24 virou LTS na 24.11.0, em 28/10/2025.
6. **`npm install -g` instala no computador, não dentro de um projeto ou pasta.** Confiança: alta. Ver [[wiki/concepts/instalacao-global-vs-local]].
7. **Dependências são pacotes de que o projeto precisa para rodar; bibliotecas prontas (calendário, agenda) poupam escrever componentes, CSS e JavaScript.** Confiança: alta, com a ressalva de que é uma definição simplificada. Não cita dependências transitivas, `package.json` nem lockfile; dependência de desenvolvimento fica para as próximas aulas.
8. **`vue --version` mostrou "Vue, versão 5.0.9".** Confiança: alta para o número, mas o rótulo está errado. Esse comando mostra a versão do `@vue/cli` (a 5.0.9 foi publicada em 21/08/2025 e é a `latest` no npm), não a do framework. O Vue em si está na linha 3.x (3.5.45 no npm em 12/11/2026) ([external](https://registry.npmjs.org/@vue/cli)).

> "Esse G significa que eu estou instalando no meu computador, eu não estou instalando dentro de um projeto." (autor não identificado)

## Entidades

- [[wiki/entities/vue]]: página criada neste ingest.
- [[wiki/entities/nodejs]]: página criada neste ingest.
- Sem página própria: npm, Yarn, pnpm, Homebrew, apt-get, Vue CLI (coberto em [[wiki/concepts/scaffolding-de-projeto]]).

## Conceitos

- [[wiki/concepts/gerenciador-de-pacotes]]
- [[wiki/concepts/instalacao-global-vs-local]]: página criada neste ingest.
- [[wiki/concepts/scaffolding-de-projeto]]: página criada neste ingest.
- [[wiki/concepts/ambiente-de-execucao]]: a máquina local como ambiente de desenvolvimento.
- [[wiki/concepts/historia-do-front-end]]: o npm como passo da cadeia causal do front end.

## Relação com fontes anteriores

- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] já assume um projeto Vue montado; esta aula é o passo anterior.
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]] explica o que o framework resolve por baixo; esta aula só prepara a máquina.
- [[wiki/sources/historia-do-front-end-akita-ep4]] explica por que o npm existe; esta aula o usa sem contexto histórico.

## Open Questions

- Qual curso é este e quem é o autor? A transcrição não diz.
- ~~As próximas aulas vão criar o projeto com `vue create` (Vue CLI, webpack) ou com `create-vue` (Vite)?~~ **Respondido pelo usuário em 2026-11-12:** o curso segue com o Vue CLI. Quem acompanhar vai aprender um caminho que a documentação oficial já não recomenda para projetos novos: build com webpack em vez de Vite e CLI instalado globalmente. Os conceitos de Vue continuam valendo, mas a parte de configuração e build vai diferir de um projeto criado com `create-vue`. Ver [[wiki/concepts/scaffolding-de-projeto]].
- O Node 24.10.0 do vídeo está abaixo do mínimo atual do `create-vue` (24.12.0 na linha 24). Quem seguir a aula com essa versão pode receber aviso de `engines`.
