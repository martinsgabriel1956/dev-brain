---
type: concept
title: "Linux"
aliases: ["distro Linux", "GNU/Linux", "Linux kernel"]
date_created: 2026-07-20
date_updated: 2026-08-11
source_count: 2
tags: [sistema-operacional, linux, servidor, open-source, cs-fundamentals]
skill: cs-fundamentals
status: stub
---

# Linux

Não é um único sistema operacional, mas uma família de sistemas — as distribuições, ou "distros" — construídas em torno do kernel Linux, criado em 1991 por Linus Torvalds como alternativa gratuita e de código aberto ao [[wiki/concepts/unix]] e a sistemas comerciais.

## Vantagens

- Leve e seguro; não exige hardware potente — roda de máquinas antigas a servidores de alto desempenho.
- Amplamente usado em programação, segurança cibernética e administração de servidores (Google, Facebook e NASA citados como usuários de servidores Linux).
- Gratuito e open source.

## Desvantagens

- Barreira de entrada alta para iniciantes — interface distinta de [[wiki/concepts/windows]]/[[wiki/concepts/macos]], forte uso de linha de comando em vez de menus gráficos.
- Baixa compatibilidade nativa com softwares e jogos comerciais, feitos majoritariamente para Windows/Mac.

## Kernel

O Linux é um exemplo canônico de kernel monolítico que suporta módulos carregados dinamicamente (drivers) — ver [[wiki/concepts/kernel]].

## Relação com BSD e Unix

Linux é um clone de [[wiki/concepts/unix]] construído do zero (não deriva de código Unix original), diferente do [[wiki/concepts/bsd]], que é um descendente direto do código-fonte Unix de Berkeley.

## Comandos como Interface de Trabalho (e de Agentes)

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]], conhecer os comandos básicos de Linux importa por dois motivos práticos: ~90% dos servidores rodam Linux/Unix (operados por [[wiki/concepts/ssh|SSH]] e pipelines de [[wiki/concepts/ci-cd|CI/CD]]), e as [[wiki/concepts/harness|harnesses]] de IA manipulam a máquina rodando esses mesmos comandos nativos. Ver [[wiki/concepts/comandos-basicos-linux]] e [[wiki/concepts/shell-terminal]].

## Key Sources

- [[wiki/sources/8-sistemas-operacionais-explicados]] — panorama comparativo de propósito e mercado
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — comandos básicos de shell e por que devs precisam reconhecê-los na era dos agentes
