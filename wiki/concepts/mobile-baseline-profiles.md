---
type: concept
title: "Baseline Profiles — Android"
aliases: ["android baseline profiles", "ART compilation", "cold start android"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, android, baseline-profiles, cold-start, ART, startup]
skill: tech-mentor-mobile
status: stable
---

# Baseline Profiles — Android

Instrui o ART a pré-compilar caminhos críticos antes da primeira execução — reduz cold start 30-40%.

## Como Funciona

Sem Baseline Profile: ART usa JIT na primeira execução — interpretação mais lenta, frames perdidos no startup.

Com Baseline Profile: código marcado como crítico é compilado AOT (Ahead-of-Time) pela Play Store antes do app ser aberto pela primeira vez.

## Geração

```kotlin
// build.gradle
dependencies {
    androidTestImplementation("androidx.benchmark:benchmark-macro-junit4:1.3.0")
}

@RunWith(AndroidJUnit4::class)
class BaselineProfileGenerator {
    @get:Rule val rule = BaselineProfileRule()

    @Test
    fun generate() = rule.collect(packageName = "com.example.app") {
        startActivityAndWait()
        // navegar pelos fluxos críticos
    }
}
```

```bash
./gradlew :app:generateBaselineProfile
```

## Integração em CI

```yaml
- name: Generate Baseline Profile
  run: ./gradlew :app:generateReleaseBaselineProfile
- name: Commit profile
  run: git add app/src/main/baseline-prof.txt
```

Detecta regressões de startup antes de chegar à produção.

## Ver também

- [[mobile-metricas-criticas]] — cold start como KPI
- [[mobile-profiling]] — medir ganho com Macrobenchmark
- [[mobile-cicd]] — geração automática de perfil

## Key Sources

- [[wiki/sources/mobile-baseline-profiles]]
