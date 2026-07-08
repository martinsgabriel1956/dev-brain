---
title: "5 (ou 6) Dicas Para Projetos Novos"
source_url: ""
author: "desconhecido (canal YouTube, patrocínio HostGator)"
date_published: "desconhecido"
date_ingested: 2026-07-07
type: transcript
language: pt-BR
tags: [projetos, stack, deploy, orm, migrations, testes, documentacao, ci-cd, mvp]
---

# 5 (ou 6) Dicas Para Projetos Novos

> Nota: vídeo patrocinado pela HostGator (VPS, domínios, hospedagem para N8N/OpenClaw). Menções ao patrocinador foram mantidas onde fazem parte do conteúdo técnico (ex.: fluxo de deploy contínuo numa VPS), mas o CTA comercial em si não é o foco da ingestão.

Se você tá começando um projeto novo agora, iniciando sua codebase do zero, seguem algumas coisas que costumo fazer que ajudam a progredir de um jeito um pouco menos difícil.

## 1. Escolha da Stack

A escolha de stack está sempre muito atrelada àquilo que o profissional já conhece. Geralmente, ao iniciar um projeto novo, é uma de duas coisas:

- **Você está iniciando para aprender algo novo.** Nesse caso, as pessoas costumam escolher uma stack em que têm interesse mas ainda não dominam — Elixir, Golang, Rust, etc.
- **Você está iniciando para ganhar dinheiro.** Nesse caso, a maioria tende a escolher o que já domina, já que o foco não é aprender tecnologia nova, e sim fazer um projeto que renda uma quantidade de dinheiro interessante. Na prática, isso costuma ser JavaScript (a linguagem mais popular), mas quem trabalha com Golang, PHP, Ruby ou Python vai iniciar o projeto na stack que já conhece.

Dentro da escolha da stack, normalmente também se escolhe um framework. Hoje em dia vale a pena conversar com uma IA para levantar possibilidades e discutir o que faz mais ou menos sentido para o seu caso.

Quando você é um desenvolvedor solo fazendo um SaaS que precisa sair do zero para encontrar os primeiros usuários, um framework **mais "batteries included"** costuma ser mais fácil:

- Python → Django (painel de admin, modelos e convenções prontas)
- Ruby → Rails
- PHP → Laravel

Esses frameworks já têm muita coisa pronta e saem do zero mais rápido do que algo mais "bare bones", como Node + Express, que dá menos coisas out of the box — você vai precisar agregar plugins e montar mais peças manualmente para sair do zero de fato.

Também vale escolher a stack baseado no que o projeto vai fazer: uma single-page application pode fazer sentido em Next.js; um backend muito pesado computacionalmente talvez não faça tanto sentido em Python ou JavaScript.

## 2. Pensar na Estrutura Inicial (Rumo ao MVP)

Depois de escolher a stack, pense no seu MVP e na estrutura inicial do projeto. É importante colocar esse pensamento no papel — ou melhor, num documento `.md` — e não simplesmente sair codando, senão você acaba fazendo uma gambiarra macarrônica difícil de evoluir.

Hoje em dia você provavelmente vai codar com IA, e ter essa estrutura pensada e documentada de antemão é muito vantajoso para não seguir por um caminho que não faz sentido.

## 3. Deploy Imediato

O framework escolhido geralmente já vem com algum boilerplate/"Hello World". A primeira coisa que eu quero que você faça é **fazer deploy desse boilerplate imediatamente** — só o Hello World.

Por quê? É muito comum construir algo que roda localmente, sem estar dockerizado, com banco de dados e infraestrutura toda rodando só na sua máquina. Na hora de levar isso para alguma cloud/provedor, o deploy simplesmente não funciona, e você passa horas debugando. Se o primeiro passo já é fazer o deploy, os problemas vão sendo endereçados conforme a codebase evolui, em vez de se acumularem para o final.

Fluxo recomendado: dentro do projeto, configurar cedo (ex.: GitHub Actions) um **CD automático a cada merge para `main`**, apontando para um servidor. Ferramenta usada aqui: **HostGator**, com planos de VPS a partir de ~R$21/mês, servidores em São Paulo (boa latência para usuários no Brasil), suficiente para hospedar todo o backend, com capacidade escalável conforme a base de usuários cresce.

## 4. ORM, Migrations e Banco de Dados

Sempre vale usar uma **ORM** — evitar usar SQL cru direto deixa os projetos mais robustos, principalmente por causa de migrações de banco de dados.

Preferência por ORMs **menores/mínimas**, que garantam:

- Geração automática de arquivos de **migration**
- **Schema** explícito
- **Type safety** na codebase

Sem inflar demais a API — o ideal é ficar o mais próximo possível de SQL puro, mas com a geração automática de migrations, schema e type safety como o grande diferencial. No mundo JavaScript, a recomendação é **Drizzle**, mas existem outras boas opções.

Isso volta a conectar com o deploy: mesmo que o projeto ainda seja só um Hello World, se ele vai ter banco de dados, é bom já iniciar o banco de dev e fazer o deploy **triggar automaticamente as migrations**. Se isso não for feito cedo, vira problema mais pra frente. No fim do primeiro dia de um projeto novo: um Hello World que não faz nada, e uma primeira migração no banco (por exemplo, para armazenar usuários) — o projeto ainda não faz nada, mas já está em produção, permitindo ver os problemas que podem surgir depois.

## 5. Testes na Pipeline

Mesmo antes de qualquer funcionalidade, vale configurar testes na pipeline — libs de teste e algum esquema de CI que rode os testes antes de mergear para `main`.

- Unitário (JS): **Vitest** (a preferência entre libs de unit test não importa tanto, são bem parecidas)
- End-to-end: **Cypress** é o mais comum

Ter isso rodando desde cedo na pipeline garante mais robustez.

## 6. Documentar o Setup

Depois de todo esse setup, a última etapa é **documentar**:

- **README**: como instalar, como rodar localmente, comandos de teste, decisões de stack/arquitetura (atualizado conforme a codebase evolui), padrões e convenções da codebase, o que o projeto faz.
- **AGENTS.md**: instruções para a IA trabalhar no projeto — como rodar os testes, se é para seguir TDD, quais são os padrões de tipagem, qual a arquitetura e estrutura dos repositórios/serviços, e qual é o objetivo explícito do projeto.

Essa documentação é o que torna produtivo trabalhar com IA na codebase depois.

## Resumo das 5-6 primeiras coisas ao iniciar uma codebase nova

1. Escolher a stack (e framework)
2. Pensar/documentar a estrutura inicial rumo ao MVP
3. Deploy imediato do Hello World, com CD automático a cada merge
4. ORM mínima + migrations automáticas + banco desde o primeiro deploy
5. Testes (unitário + e2e) rodando na pipeline antes de mergear
6. Documentar tudo em README + AGENTS.md
