---
type: concept
title: "Armazenamento Local — Mobile"
aliases: ["mmkv mobile", "sqlite mobile", "asyncstorage", "room android", "keychain mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, armazenamento, mmkv, sqlite, keychain, keystore, room]
skill: tech-mentor-mobile
status: stable
---

# Armazenamento Local — Mobile

## Hierarquia de Decisão

| Dado | Solução | Por quê |
|---|---|---|
| Tokens, flags, prefs | MMKV | Síncrono, AES nativo, 10x mais rápido que AsyncStorage |
| Dados relacionais/offline | SQLite (expo-sqlite) / Room | SQL completo, queries complexas |
| Segredos, chaves privadas | Keychain (iOS) / Keystore (Android) | Hardware-backed, nunca sai do dispositivo |
| Prefs Flutter simples | SharedPreferences / Hive | Key-value async |
| Legacy RN | AsyncStorage | Evitar para dados frequentes |

## MMKV

```js
import { MMKV } from 'react-native-mmkv';
const storage = new MMKV({ encryptionKey: 'my-key' });
storage.set('token', 'abc123');
const token = storage.getString('token');
```

Mmap-based, síncrono — leitura sem overhead de I/O assíncrono. AES nativo para dados sensíveis não-críticos.

## SQLite (offline-first)

```js
// expo-sqlite
const db = await SQLite.openDatabaseAsync('app.db');
await db.execAsync('CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT)');
```

SQLCipher para criptografia em repouso — obrigatório para PII offline.

## Keychain / Keystore

**iOS Keychain:** `SecItemAdd` / `SecItemCopyMatching` — protegido por Secure Enclave.
**Android Keystore:** chaves geradas no hardware, nunca exportáveis.

Usar para: tokens de autenticação sensíveis, chaves de criptografia, credenciais biométricas.

## Ver também

- [[mobile-seguranca]] — o que nunca guardar em texto plano
- [[mobile-offline-first-basico]] — como o storage suporta offline
- [[mobile-biometria]] — integração Keychain + biometria

## Key Sources

- [[wiki/sources/mobile-armazenamento-local]]
