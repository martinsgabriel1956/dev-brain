---
type: source
title: "Offline-First Básico — Mobile"
aliases: ["mobile offline", "offline first mobile", "mobile cache strategy"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-offline-first-basico.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, offline-first, cache, sync, connectivity, stale-while-revalidate]
skill: tech-mentor-mobile
status: stable
---

# Offline-First Básico

## TL;DR

Offline-first: mostrar dados em cache imediatamente, buscar atualização em background, sinalizar estado de rede. Detectar conectividade com `NetInfo` (RN) ou `ConnectivityManager` (Android). Stale-while-revalidate: servir cache enquanto atualiza em background. Fila de operações pendentes para sincronizar quando online. Não bloquear UI aguardando rede — nunca.

## Claims Principais

| Claim | Confiança |
|---|---|
| App deve funcionar em modo leitura sem rede — dados em cache, não tela de erro | Alta |
| Detectar `isConnected` antes de tentar operações de escrita — enfileirar se offline | Alta |
| Stale-while-revalidate é o padrão de UX — conteúdo imediato + refresh silencioso | Alta |
| Badge "Offline" + dados em cache > tela de erro vazia em modo desconectado | Alta |

## Conceitos Abordados

- [[mobile-offline-first-basico]] · [[mobile-offline-first-avancado]] · [[mobile-armazenamento-local]] · [[mobile-chamadas-http]]
