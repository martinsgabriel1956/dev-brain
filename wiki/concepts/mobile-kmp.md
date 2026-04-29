---
type: concept
title: "Kotlin Multiplatform (KMP)"
aliases: ["kmp", "kotlin multiplatform mobile", "kmm", "shared business logic mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, kmp, kotlin-multiplatform, ios, android, shared-logic, ktor, sqldelight]
skill: tech-mentor-mobile
status: stable
---

# Kotlin Multiplatform (KMP)

Compartilha lógica de negócio (domain + data) entre iOS e Android. UI permanece nativa em cada plataforma.

## Estrutura de Módulos

```
shared/
├── commonMain/       ← domain, use cases, repositories (interfaces)
│   └── domain/
│       └── usecase/GetProductsUseCase.kt
├── androidMain/      ← implementações Android-specific
└── iosMain/          ← implementações iOS-specific (via expect/actual)

androidApp/           ← Compose UI
iosApp/               ← SwiftUI
```

## expect/actual

```kotlin
// commonMain
expect fun currentTimeMillis(): Long

// androidMain
actual fun currentTimeMillis() = System.currentTimeMillis()

// iosMain
actual fun currentTimeMillis() = NSDate().timeIntervalSince1970.toLong() * 1000
```

## Ktor — Networking

```kotlin
// commonMain
val client = HttpClient {
    install(ContentNegotiation) { json() }
    install(HttpTimeout) { requestTimeoutMillis = 10_000 }
}

val user: User = client.get("$baseUrl/users/$id").body()
```

## SQLDelight — Storage

```sql
-- commonMain/sqldelight/app/database/User.sq
CREATE TABLE User (id TEXT PRIMARY KEY, name TEXT NOT NULL);
selectAll:
SELECT * FROM User;
```

Gera código Kotlin type-safe por plataforma — equivalente ao sqlc.

## Ver também

- [[mobile-cross-platform-decision]] — quando KMP vs Flutter vs Nativo
- [[mobile-armazenamento-local]] — SQLDelight como alternativa ao Room

## Key Sources

- [[wiki/sources/mobile-kmp]]
