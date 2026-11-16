---
type: concept
title: "Armazenamento Local — Mobile"
aliases: ["mmkv mobile", "sqlite mobile", "asyncstorage", "room android", "keychain mobile"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 3
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

- [[wiki/concepts/mobile-seguranca]] — o que nunca guardar em texto plano
- [[wiki/concepts/mobile-offline-first-basico]] — como o storage suporta offline
- [[wiki/concepts/mobile-biometria]] — integração Keychain + biometria

## Na NLW #2, dia 4 (Diego Fernandes)

Favoritos no AsyncStorage "como se fosse o local storage lá da web", porque não há login; a API é assíncrona e sem criptografia. A implementação fica para o dia 5. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

Favoritos do Proffy em AsyncStorage: só texto, então JSON sob a chave `favorites`; ids para marcar a lista e objetos inteiros na aba Favoritos (que congelam preço e bio). Sem `try/catch` no `JSON.parse` e com `splice(-1, 1)` possível quando o id não é achado. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key Sources

- [[wiki/sources/mobile-armazenamento-local]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: favoritos do Proffy no AsyncStorage
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: favoritos em JSON no AsyncStorage
