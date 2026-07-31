---
type: concept
title: "Coolify"
aliases: ["coolify", "coolify deploy", "paas self-hosted"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [coolify, traefik, deploy, docker, self-hosted, vps, reverse-proxy, paas]
skill: tech-mentor-security
status: stub
---

# Coolify

PaaS self-hosted open source para gerenciar deploy de aplicações em uma VPS própria — alternativa a plataformas gerenciadas (Vercel, Heroku, Railway) sem abrir mão de rodar em infraestrutura própria. Usa Docker por baixo e um [[wiki/concepts/reverse-proxy|proxy reverso]] (Traefik) para rotear o tráfego das aplicações gerenciadas.

## Auto-update do proxy — risco observado

Por padrão, o Coolify atualiza o Traefik automaticamente (semanalmente, segundo relato em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]). Isso é conveniente até uma versão nova introduzir uma regressão severa: no caso relatado, o Traefik 3.6.16 passou a consumir 35% de CPU constante mesmo sem tráfego e apresentou memory leak (4,7 GB em 40 minutos) — consumindo capacidade que deveria estar disponível para a aplicação, e piorando um [[wiki/concepts/ddos-syn-flood|SYN flood]] simultâneo. O aprendizado registrado na fonte foi travar a versão do proxy em produção, em vez de depender do auto-update.

## Instalação via VPS gerenciada

A forma mais simples de subir o Coolify é via um instalador de VPS que já traz um gerenciador Docker com opção de instalação em um clique (ex.: [[wiki/entities/hostinger]]), evitando configurar Docker e comandos de instalação manualmente.

## Key sources

- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
