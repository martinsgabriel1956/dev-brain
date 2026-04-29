---
type: concept
title: "Offline-First Básico — Mobile"
aliases: ["mobile offline", "stale while revalidate mobile", "mobile cache first"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, offline-first, cache, stale-while-revalidate, connectivity]
skill: tech-mentor-mobile
status: stable
---

# Offline-First Básico — Mobile

Mostrar dados imediatamente do cache — buscar atualização em background.

## Princípio

```
1. Carregar do cache local (imediato)
2. Mostrar dados na UI sem esperar rede
3. Buscar atualização em background
4. Atualizar UI silenciosamente se houve mudança
5. Indicar estado offline com badge, não com tela de erro
```

## Detectar Conectividade

```js
// React Native
import NetInfo from '@react-native-community/netinfo';

const unsubscribe = NetInfo.addEventListener(state => {
    setIsOnline(state.isConnected ?? false);
});
```

```kotlin
// Android
val connectivityManager = getSystemService<ConnectivityManager>()
val network = connectivityManager?.activeNetwork
val isConnected = connectivityManager?.getNetworkCapabilities(network)
    ?.hasCapability(NET_CAPABILITY_INTERNET) == true
```

## Stale-While-Revalidate

TanStack Query faz isso automaticamente com `staleTime`. Para storage manual:

```ts
async function getProducts(): Promise<Product[]> {
    const cached = await storage.getProducts();
    if (cached) {
        fetchInBackground(); // sem await
        return cached;
    }
    return await api.getProducts();
}
```

## UX de Offline

```ts
{!isOnline && (
    <View style={styles.offlineBanner}>
        <Text>Modo offline — dados podem estar desatualizados</Text>
    </View>
)}
```

Badge informativo > tela de erro vazia.

## Ver também

- [[mobile-offline-first-avancado]] — sync, conflitos, CRDT
- [[mobile-armazenamento-local]] — SQLite/MMKV como cache local
- [[mobile-chamadas-http]] — TanStack Query para stale-while-revalidate automático

## Key Sources

- [[wiki/sources/mobile-offline-first-basico]]
