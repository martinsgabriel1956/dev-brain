---
type: source
title: "Armazenamento Local — Mobile"
aliases: ["mobile storage", "mmkv", "sqlite mobile", "asyncstorage", "room android"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-armazenamento-local.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, armazenamento, mmkv, sqlite, asyncstorage, keychain, keystore, room]
skill: tech-mentor-mobile
status: stable
---

# Armazenamento Local — Mobile

## TL;DR

Hierarquia de armazenamento: MMKV para flags/tokens/prefs (síncrono, AES nativo), SQLite/Room para dados relacionais com offline-first, Keychain/Keystore para segredos que nunca devem sair do dispositivo. Evitar AsyncStorage para dados frequentemente lidos — performance perceptível vs MMKV. Dados sensíveis em texto plano no storage são acessíveis via backup do Android.

## Claims Principais

| Claim | Confiança |
|---|---|
| MMKV é 10x mais rápido que AsyncStorage — mmap vs I/O síncrono | Alta |
| AsyncStorage para objetos grandes ou lidos em cada render = anti-pattern | Alta |
| SQLite com SQLCipher para dados PII offline — criptografia em repouso | Alta |
| Keychain (iOS) / Keystore (Android) — únicos storages seguros para segredos/biometria | Alta |
| Room é ORM sobre SQLite para Android com suporte nativo a Flow/coroutines | Alta |

## Conceitos Abordados

- [[mobile-armazenamento-local]] · [[mobile-offline-first-basico]] · [[mobile-seguranca]]
