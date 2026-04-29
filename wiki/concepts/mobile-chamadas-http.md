---
type: concept
title: "Chamadas HTTP — Mobile"
aliases: ["mobile networking", "mobile http client", "tanstack query mobile", "okhttp interceptor"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, networking, http, tanstack-query, retrofit, okhttp, interceptor, loading-states]
skill: tech-mentor-mobile
status: stable
---

# Chamadas HTTP — Mobile

## React Native — TanStack Query

```ts
function useUser(id: string) {
    return useQuery({
        queryKey: ['user', id],
        queryFn: () => api.getUser(id),
        staleTime: 5 * 60 * 1000,
    });
}

function UserScreen({ id }) {
    const { data, isLoading, error } = useUser(id);
    if (isLoading) return <Skeleton />;
    if (error) return <ErrorState onRetry={() => refetch()} />;
    return <UserCard user={data} />;
}
```

## Android — Retrofit + OkHttp

```kotlin
val okHttpClient = OkHttpClient.Builder()
    .addInterceptor(AuthInterceptor(tokenProvider))
    .addInterceptor(HttpLoggingInterceptor())
    .connectTimeout(10, TimeUnit.SECONDS)
    .readTimeout(30, TimeUnit.SECONDS)
    .build()
```

Interceptors para auth, logging e retry — sem repetir por endpoint.

## Flutter — Riverpod FutureProvider

```dart
final userProvider = FutureProvider.family<User, String>((ref, id) async {
    return ref.watch(apiServiceProvider).getUser(id);
});
```

## UX de Loading

- Skeleton/shimmer > spinner — posiciona conteúdo antes de carregar
- Badge "Offline" + dados em cache > tela de erro
- Retry explícito com botão — não tentar automaticamente infinitamente

## Ver também

- [[mobile-offline-first-basico]] — servir cache quando sem rede
- [[mobile-state-management-global]] — onde server state NÃO vai

## Key Sources

- [[wiki/sources/mobile-chamadas-http]]
