---
date: 2026-04-23
tags: [tech-mentor, mobile, android, baseline-profiles, cold-start, performance, aot]
skill: tech-mentor-mobile/references/performance
level: intermediário
---

# Baseline Profiles — Android (Redução de Cold Start)

## Contexto
Baseline Profiles são um mecanismo do Android Runtime (ART) para compilar antecipadamente (AOT) os métodos mais críticos do app — aqueles usados nos primeiros segundos de execução. Sem Baseline Profiles, o app começa interpretado (JIT) e compila métodos conforme são executados, resultando em cold start mais lento e jank nas primeiras interações. Com o perfil, esses métodos já estão compilados nativamente na instalação.

## Como Funciona

### O problema sem Baseline Profiles

```
Sem perfil (JIT):
Instalação → app começa interpretado → JIT compila métodos durante execução
Resultado: cold start ~40% mais lento, jank nas primeiras interações

Com Baseline Profile (AOT):
Instalação → Play Store aplica perfil → métodos críticos compilados
Resultado: cold start mais rápido, primeiras interações sem jank
```

### Setup — Macrobenchmark + ProfileInstaller

```kotlin
// build.gradle.kts (app)
plugins {
  id("com.android.application")
}

dependencies {
  implementation("androidx.profileinstaller:profileinstaller:1.3.1")
}

// build.gradle.kts (módulo :benchmark)
plugins {
  id("com.android.test")
  id("androidx.baselineprofile")
}

android {
  targetProjectPath = ":app"
  experimentalProperties["android.experimental.self-instrumenting"] = true
}

dependencies {
  implementation("androidx.benchmark:benchmark-macro-junit4:1.2.4")
  implementation("androidx.test.ext:junit:1.1.5")
  implementation("androidx.test:runner:1.5.2")
}
```

### Gerar o perfil

```kotlin
// benchmark/src/main/java/com/yourapp/BaselineProfileGenerator.kt
@ExperimentalBaselineProfilesApi
class BaselineProfileGenerator {

  @get:Rule
  val rule = BaselineProfileRule()

  @Test
  fun generate() {
    rule.collect(
      packageName = "com.yourcompany.app"
    ) {
      // Definir o fluxo crítico do app — o que o usuário faz nos primeiros 30s
      pressHome()
      startActivityAndWait()

      // Navegar pelas telas mais usadas
      device.findObject(By.res("product_list")).click()
      device.waitForIdle()
      device.findObject(By.res("product_card")).click()
      device.waitForIdle()
      device.findObject(By.res("add_to_cart")).click()
      device.waitForIdle()
    }
  }
}
```

```bash
# Gerar o perfil (necessita device físico com Android 9+)
./gradlew :benchmark:generateBaselineProfile

# O arquivo é gerado em:
# app/src/main/baseline-prof.txt
```

### O arquivo gerado

```
# app/src/main/baseline-prof.txt
# Métodos identificados como críticos — compilar em AOT
HSPLcom/yourapp/MainActivity;->onCreate(Landroid/os/Bundle;)V
HSPLcom/yourapp/ui/product/ProductListViewModel;->loadProducts()V
HSPLcom/yourapp/data/repository/ProductRepository;->getProducts()Lkotlinx/coroutines/flow/Flow;
HSPLcom/yourapp/domain/usecase/GetProductsUseCase;->invoke()Lkotlinx/coroutines/flow/Flow;
# H = Hot (executado muitas vezes)
# S = Startup (executado durante cold start)
# P = Post-startup (executado pouco depois)
# L = Library method
```

### Compose — Baseline Profiles específicos

```kotlin
// Para apps Compose, o Compose Compiler gera perfil automaticamente
// Adicionar ao build.gradle.kts
composeOptions {
  kotlinCompilerExtensionVersion = "1.5.x"
}

// O compilador gera compose-stability-config.conf e contribui ao baseline-prof.txt
// Verificar com:
// ./gradlew assembleRelease --info | grep "baseline"
```

### Medir o impacto

```kotlin
// Macrobenchmark para medir cold start antes e depois
@LargeTest
class StartupBenchmark {

  @get:Rule
  val benchmarkRule = MacrobenchmarkRule()

  @Test
  fun startup_cold() = benchmarkRule.measureRepeated(
    packageName = "com.yourcompany.app",
    metrics = listOf(StartupTimingMetric()),
    iterations = 5,
    startupMode = StartupMode.COLD,
    setupBlock = { pressHome() }
  ) {
    startActivityAndWait()
  }

  @Test
  fun startup_warm() = benchmarkRule.measureRepeated(
    packageName = "com.yourcompany.app",
    metrics = listOf(StartupTimingMetric(), FrameTimingMetric()),
    iterations = 5,
    startupMode = StartupMode.WARM
  ) {
    startActivityAndWait()
  }
}
```

```bash
# Rodar benchmark
./gradlew :benchmark:connectedBenchmarkAndroidTest

# Output sample:
# startup_cold: min=1243ms, median=1287ms, max=1350ms
# startup_warm: min=312ms, median=334ms, max=389ms
```

### CI — automatizar geração do perfil

```yaml
# .github/workflows/baseline-profile.yml
name: Generate Baseline Profile

on:
  push:
    branches: [main]
  schedule:
    - cron: "0 2 * * 1" # toda segunda às 2h

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Android Emulator
        uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 34
          target: google_apis
          arch: x86_64
          script: |
            ./gradlew :benchmark:generateBaselineProfile -Pandroid.testoptions.manageddevices.emulator.gpu=swiftshader_indirect

      - name: Commit updated profile
        run: |
          git config --local user.email "ci@company.com"
          git config --local user.name "CI Bot"
          git add app/src/main/baseline-prof.txt
          git diff --staged --quiet || git commit -m "chore: update baseline profile"
```

## Trade-offs

| Aspecto | Sem perfil | Com Baseline Profile |
|---|---|---|
| Cold start | ~2–4s | ~1.2–2.5s (↓ 30–40%) |
| Tamanho APK | Normal | +~100KB (perfil compilado) |
| Setup | Nenhum | ~2h inicial |
| Manutenção | Nenhuma | Regenerar ao mudar flows críticos |
| Android mínimo | N/A | Android 7 (interpretado como fallback em versões anteriores) |

## Quando Usar / Quando Evitar

**Use sempre** em apps de produção com Android como plataforma — o ganho de 30–40% no cold start é expressivo com setup de ~2h.

**Regenere o perfil** quando mudar os flows de startup (nova tela de onboarding, mudança de autenticação, refactor de navegação).

**Não é substituição de otimização de código** — se o cold start está em 5s por trabalho pesado no Application.onCreate(), o perfil vai ajudar menos do que remover esse trabalho.

**iOS não tem equivalente direto** — o App Store compila o binário com Bitcode/ARM64 AOT por padrão.

## Conceitos Relacionados
[[mobile-metricas-criticas]] · [[mobile-profiling]] · [[mobile-cicd]] · [[mobile-monitoramento]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
