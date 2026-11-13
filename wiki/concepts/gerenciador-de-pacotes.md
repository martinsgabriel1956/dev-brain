---
type: concept
title: "Gerenciador de Pacotes (CPAN, Bundler, npm, Bower)"
aliases: ['package manager', 'npm']
date_created: 2026-10-14
date_updated: 2026-11-12
source_count: 2
tags: [dependencias, npm, build, historia]
skill: tech-mentor-frontend
status: draft
---

# Gerenciador de Pacotes (CPAN, Bundler, npm, Bower)

Substitui baixar bibliotecas manualmente (zip por site). Perl: CPAN; Ruby: Bundler (também **versões corretas**); JavaScript: npm (padrão de fato, só ficou usável após concorrentes como Yarn), Bower. Alimenta o [[wiki/concepts/pipeline-de-assets]].

Hoje o npm vem junto com o [[wiki/entities/nodejs]]; Yarn e pnpm são as alternativas mais citadas, e o guia do [[wiki/entities/vue]] mostra o comando de criação de projeto para npm, pnpm, Yarn e Bun ([[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]). A fonte define dependência como pacote de que o projeto precisa para rodar, como uma biblioteca de calendário pronta. O `-g` muda onde o pacote fica: ver [[wiki/concepts/instalacao-global-vs-local]]. Ver [[wiki/concepts/historia-do-front-end]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
