---
date: 2026-04-23
tags: [tech-mentor, mobile, kmp, kotlin-multiplatform, ios, android, shared-logic]
skill: tech-mentor-mobile/references/arquitetura
level: avançado
---

# Kotlin Multiplatform (KMP) — Compartilhar Lógica de Negócio entre iOS e Android

## Contexto
KMP permite escrever a camada de negócio (domain, data, networking, storage) em Kotlin e compilar para iOS (via Kotlin/Native) e Android nativamente — mantendo UI nativa em cada plataforma. Não é um framework de UI como Flutter: o "compartilhar" é exclusivamente de lógica. O resultado: sem bridge, sem runtime intermediário, performance nativa em ambas as plataformas.

## Como Funciona

### Arquitetura KMP

```
shared/
├── commonMain/         → código compartilhado (domain, data, networking)
│   ├── domain/
│   │   ├── model/      → data classes, enums
│   │   └── usecase/    → regras de negócio
│   ├── data/
│   │   ├── repository/
│   │   ├── api/        → Ktor client
│   │   └── db/         → SQLDelight
│   └── di/             → Koin/Kodein para DI
├── androidMain/        → implementações específicas Android
│   └── Platform.android.kt
├── iosMain/            → implementações específicas iOS
│   └── Platform.ios.kt
androidApp/             → UI Android (Kotlin + Compose)
iosApp/                 → UI iOS (Swift + SwiftUI)
```

### Setup — build.gradle.kts

```kotlin
// shared/build.gradle.kts
plugins {
  kotlin("multiplatform")
  kotlin("native.cocoapods")
  id("com.android.library")
  id("app.cash.sqldelight")
}

kotlin {
  androidTarget { compilations.all { kotlinOptions.jvmTarget = "1.8" } }

  iosX64()
  iosArm64()
  iosSimulatorArm64()

  cocoapods {
    summary = "Shared KMP logic"
    homepage = "https://github.com/yourorg/yourapp"
    version = "1.0"
    ios.deploymentTarget = "16.0"
    framework { baseName = "shared" }
  }

  sourceSets {
    commonMain.dependencies {
      implementation("io.ktor:ktor-client-core:2.3.x")
      implementation("io.ktor:ktor-client-content-negotiation:2.3.x")
      implementation("io.ktor:ktor-serialization-kotlinx-json:2.3.x")
      implementation("app.cash.sqldelight:runtime:2.0.x")
      implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.x")
      implementation("io.insert-koin:koin-core:3.5.x")
    }

    androidMain.dependencies {
      implementation("io.ktor:ktor-client-android:2.3.x")
      implementation("app.cash.sqldelight:android-driver:2.0.x")
    }

    iosMain.dependencies {
      implementation("io.ktor:ktor-client-darwin:2.3.x")
      implementation("app.cash.sqldelight:native-driver:2.0.x")
    }
  }
}
```

### Networking — Ktor (shared)

```kotlin
// commonMain/data/api/ProductApi.kt
class ProductApi(private val client: HttpClient) {

  suspend fun getProducts(page: Int, limit: Int): List<ProductDto> {
    return client.get("/products") {
      parameter("page", page)
      parameter("limit", limit)
    }.body()
  }

  suspend fun getProduct(id: String): ProductDto {
    return client.get("/products/$id").body()
  }
}

// commonMain/data/api/ApiClient.kt
fun createHttpClient(): HttpClient {
  return HttpClient {
    install(ContentNegotiation) {
      json(Json { ignoreUnknownKeys = true; isLenient = true })
    }
    install(HttpTimeout) {
      requestTimeoutMillis = 10_000
      connectTimeoutMillis = 10_000
    }
    defaultRequest {
      url(Env.API_BASE_URL)
      header("Content-Type", "application/json")
    }
  }
}

// androidMain
actual fun createPlatformHttpClient() = createHttpClient().config {
  engine { /* Android engine config */ }
}

// iosMain
actual fun createPlatformHttpClient() = createHttpClient().config {
  engine { /* Darwin engine config */ }
}
```

### Database — SQLDelight (shared)

```sql
-- commonMain/sqldelight/com/yourapp/db/Product.sq
CREATE TABLE Product (
  id TEXT NOT NULL PRIMARY KEY,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  imageUrl TEXT NOT NULL,
  synced INTEGER NOT NULL DEFAULT 0
);

getAll:
SELECT * FROM Product ORDER BY name;

getById:
SELECT * FROM Product WHERE id = :id;

upsert:
INSERT OR REPLACE INTO Product(id, name, price, imageUrl, synced)
VALUES(?, ?, ?, ?, ?);

getUnsynced:
SELECT * FROM Product WHERE synced = 0;

markSynced:
UPDATE Product SET synced = 1 WHERE id IN :ids;
```

```kotlin
// commonMain/data/db/ProductLocalDataSource.kt
class ProductLocalDataSource(private val db: AppDatabase) {

  fun getAllProducts(): Flow<List<Product>> {
    return db.productQueries.getAll().asFlow().mapToList()
  }

  fun upsert(product: Product) {
    db.productQueries.upsert(
      id = product.id,
      name = product.name,
      price = product.price,
      imageUrl = product.imageUrl,
      synced = if (product.synced) 1L else 0L
    )
  }
}

// Driver por plataforma
// androidMain
actual fun createDatabaseDriver(context: Any?): SqlDriver {
  return AndroidSqliteDriver(AppDatabase.Schema, context as Context, "app.db")
}

// iosMain
actual fun createDatabaseDriver(context: Any?): SqlDriver {
  return NativeSqliteDriver(AppDatabase.Schema, "app.db")
}
```

### Domain — Use Cases (shared)

```kotlin
// commonMain/domain/usecase/GetProductsUseCase.kt
class GetProductsUseCase(
  private val repository: ProductRepository,
  private val connectivity: ConnectivityService
) {
  operator fun invoke(): Flow<Result<List<Product>>> = flow {
    // Emitir cache local imediatamente
    emitAll(repository.getLocalProducts().map { Result.success(it) })

    // Se online, atualizar do servidor
    if (connectivity.isConnected()) {
      try {
        repository.refreshFromServer()
      } catch (e: Exception) {
        emit(Result.failure(e))
      }
    }
  }
}
```

### expect/actual — Código específico de plataforma

```kotlin
// commonMain — declarar expect
expect class Platform {
  val name: String
  val osVersion: String
}

expect fun generateUUID(): String

// androidMain — implementar actual
actual class Platform {
  actual val name = "Android"
  actual val osVersion = Build.VERSION.RELEASE
}

actual fun generateUUID(): String = UUID.randomUUID().toString()

// iosMain — implementar actual
actual class Platform {
  actual val name = "iOS"
  actual val osVersion = UIDevice.currentDevice.systemVersion
}

actual fun generateUUID(): String = NSUUID().UUIDString
```

### Expondo para Swift — KMP → SwiftUI

```kotlin
// shared — expor com suspend functions e Flow
// Para iOS, o Kotlin Coroutines precisam de wrapping

// Opção 1: SKIE (Touchlab) — converte suspend + Flow para async/AsyncStream automaticamente
// build.gradle.kts: id("co.touchlab.skie")

// Opção 2: KMP-NativeCoroutines
// Adicionar annotation:
@NativeCoroutines
suspend fun getProduct(id: String): Product = repository.getProduct(id)

@NativeCoroutinesFlow
fun observeProducts(): Flow<List<Product>> = repository.observeProducts()
```

```swift
// SwiftUI usando o shared module
import shared

struct ProductListView: View {
  @StateObject private var viewModel = ProductListViewModel()

  var body: some View {
    List(viewModel.products, id: \.id) { product in
      ProductRow(product: product)
    }
    .task { await viewModel.load() }
  }
}

@MainActor
class ProductListViewModel: ObservableObject {
  @Published var products: [Product] = []

  private let useCase = GetProductsUseCase(/* dependencies */)

  func load() async {
    for await result in asyncSequence(for: useCase.invoke()) {
      if let products = try? result.getOrThrow() {
        self.products = products
      }
    }
  }
}
```

## Trade-offs

| Aspecto | KMP | React Native | Flutter |
|---|---|---|---|
| UI | 100% nativa (2 codebases) | Componentes nativos (1 codebase) | UI própria (1 codebase) |
| Lógica compartilhada | Máxima (compilação nativa) | Via JS bridge | Via platform channels |
| Curva de aprendizado | Alta (Kotlin + iOS interop) | Média | Média |
| Debugging | Complexo (duas plataformas) | Médio | Bom (DevTools) |
| Ecossistema | Emergindo | Maduro | Crescendo |
| DX | Boa (IntelliJ) | Boa (VS Code) | Ótima (DevTools) |
| Maturidade | Stable desde 2023 | Stable | Stable |

## Quando Usar / Quando Evitar

**KMP é ideal quando:** domínio complexo (financeiro, saúde, logística) onde garantir consistência de regras de negócio entre plataformas é crítico, equipe já tem Kotlin expertise, e UI nativa é requisito.

**Evite KMP quando:** time pequeno sem experiência nativa em iOS e Android (você vai precisar de devs dedicados de cada plataforma para a camada de UI), ou app simples onde o benefício de compartilhamento não compensa o setup.

**Netflix, Philips, VMware usam KMP** — é produção-ready. O risco é de ecossistema (menos libs disponíveis que RN/Flutter), não de maturidade técnica.

## Conceitos Relacionados
[[mobile-cross-platform-decision]] · [[mobile-cicd]] · [[mobile-offline-first-avancado]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
