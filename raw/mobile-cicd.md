---
date: 2026-04-23
tags: [tech-mentor, mobile, cicd, fastlane, github-actions, eas-build, code-signing, rollout]
skill: tech-mentor-mobile/references/cicd
level: avançado
---

# CI/CD Mobile — Fastlane, GitHub Actions, EAS Build, Code Signing, Rollout Gradual

## Contexto
CI/CD mobile é mais complexo do que web: envolve certificados criptográficos (provisioning profiles, keystores), builds demorados (10–30min), e distribuição por duas stores com processos diferentes. Um pipeline bem construído automatiza signing, testes, build, upload e rollout — sem intervenção manual.

## Como Funciona

### Arquitetura geral do pipeline

```
PR → CI (lint + unit tests) → merge em main → CD:
  → build iOS (Fastlane + Xcode Cloud / GitHub Actions macOS)
  → build Android (Fastlane + GitHub Actions)
  → upload TestFlight / Firebase App Distribution (beta)
  → após aprovação → rollout gradual na store (5% → 20% → 100%)
```

### Code Signing — iOS

Code signing iOS é o maior pain point. O modelo Fastlane Match centraliza certificados e profiles em um repositório privado.

```ruby
# Matchfile
git_url("https://github.com/yourorg/certs-private")
storage_mode("git")
type("appstore")
app_identifier(["com.yourapp", "com.yourapp.extension"])
username("apple@yourcompany.com")
```

```ruby
# Fastfile
lane :setup_certificates do
  match(
    type: "appstore",
    readonly: is_ci,               # CI sempre readonly — não gera certificados novos
    git_basic_authorization: Base64.strict_encode64("#{ENV["GITHUB_USERNAME"]}:#{ENV["MATCH_PAT"]}")
  )
end

lane :beta do
  setup_certificates
  increment_build_number(
    build_number: ENV["BUILD_NUMBER"] || number_of_commits
  )
  build_app(
    workspace: "ios/MyApp.xcworkspace",
    scheme: "MyApp",
    configuration: "Release",
    export_method: "app-store"
  )
  upload_to_testflight(
    api_key_path: "fastlane/app-store-connect-key.json",
    skip_waiting_for_build_processing: true
  )
  slack(message: "🚀 Beta iOS enviado para TestFlight", slack_url: ENV["SLACK_WEBHOOK"])
end
```

```yaml
# .github/workflows/ios-deploy.yml
name: iOS Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: "3.2"
          bundler-cache: true

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Install pods
        run: cd ios && pod install

      - name: Deploy to TestFlight
        env:
          MATCH_PAT: ${{ secrets.MATCH_PAT }}
          GITHUB_USERNAME: ${{ secrets.MATCH_GITHUB_USERNAME }}
          APP_STORE_CONNECT_API_KEY_ID: ${{ secrets.ASC_KEY_ID }}
          APP_STORE_CONNECT_API_ISSUER_ID: ${{ secrets.ASC_ISSUER_ID }}
          APP_STORE_CONNECT_API_KEY_CONTENT: ${{ secrets.ASC_KEY_CONTENT }}
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
          BUILD_NUMBER: ${{ github.run_number }}
        run: bundle exec fastlane beta
```

### Code Signing — Android

Android usa keystore. Nunca commitar o keystore no repositório.

```ruby
# Fastfile — Android
lane :deploy_android do
  gradle(
    task: "bundle",
    build_type: "Release",
    project_dir: "android/",
    properties: {
      "android.injected.signing.store.file" => ENV["KEYSTORE_PATH"],
      "android.injected.signing.store.password" => ENV["KEYSTORE_PASSWORD"],
      "android.injected.signing.key.alias" => ENV["KEY_ALIAS"],
      "android.injected.signing.key.password" => ENV["KEY_PASSWORD"]
    }
  )

  upload_to_play_store(
    track: "internal",           # internal → alpha → beta → production
    aab: "android/app/build/outputs/bundle/release/app-release.aab",
    json_key_data: ENV["GOOGLE_PLAY_JSON_KEY"]
  )
end
```

```yaml
# .github/workflows/android-deploy.yml
- name: Decode keystore
  run: |
    echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > android/app/release.keystore

- name: Deploy to Play Store
  env:
    KEYSTORE_PATH: "app/release.keystore"
    KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
    KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
    KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
    GOOGLE_PLAY_JSON_KEY: ${{ secrets.GOOGLE_PLAY_JSON_KEY }}
  run: bundle exec fastlane deploy_android
```

### EAS Build — Expo (React Native)

EAS Build gerencia signing na nuvem — zero configuração local de certificados.

```json
// eas.json
{
  "cli": { "version": ">= 7.0.0" },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "ios": { "simulator": false },
      "android": { "buildType": "apk" }
    },
    "production": {
      "autoIncrement": true,
      "ios": {
        "resourceClass": "m-medium"
      },
      "android": {
        "buildType": "app-bundle"
      }
    }
  },
  "submit": {
    "production": {
      "ios": {
        "appleId": "apple@company.com",
        "ascAppId": "1234567890"
      },
      "android": {
        "serviceAccountKeyPath": "./google-play-key.json",
        "track": "internal"
      }
    }
  }
}
```

```yaml
# .github/workflows/eas-build.yml
- name: Build and Submit
  env:
    EXPO_TOKEN: ${{ secrets.EXPO_TOKEN }}
  run: |
    npx eas-cli build --platform all --profile production --non-interactive
    npx eas-cli submit --platform all --profile production --non-interactive
```

### OTA Updates — Expo Updates (sem passar pela store)

```typescript
// app.json — configurar EAS Update
{
  "expo": {
    "updates": {
      "url": "https://u.expo.dev/PROJECT_ID",
      "checkAutomatically": "ON_LOAD",
      "fallbackToCacheTimeout": 0
    },
    "runtimeVersion": { "policy": "appVersion" }
  }
}
```

```typescript
// Verificar update em background
import * as Updates from "expo-updates";

export async function checkForUpdate(): Promise<void> {
  if (__DEV__) return;

  try {
    const update = await Updates.checkForUpdateAsync();
    if (update.isAvailable) {
      await Updates.fetchUpdateAsync();
      // Notificar usuário antes de recarregar
      Alert.alert(
        "Atualização disponível",
        "Uma nova versão foi instalada. Reinicie o app.",
        [{ text: "Reiniciar", onPress: () => Updates.reloadAsync() }]
      );
    }
  } catch (err) {
    console.log({ message: "OTA check failed", error: err });
  }
}
```

### Rollout Gradual

Play Store suporta rollout percentual nativo. App Store Review limita a 100% após aprovação, mas TestFlight serve para staged rollout interno.

```ruby
# Fastlane — rollout gradual na Play Store
lane :production_rollout do |options|
  percentage = options[:percentage] || 5

  upload_to_play_store(
    track: "production",
    rollout: (percentage / 100.0).to_s, # "0.05" = 5%
    aab: lane_context[SharedValues::GRADLE_AAB_OUTPUT_PATH]
  )

  slack(
    message: "🎯 Android em rollout #{percentage}% na produção",
    slack_url: ENV["SLACK_WEBHOOK"]
  )
end

# Chamar com porcentagem
# fastlane production_rollout percentage:5
# fastlane production_rollout percentage:20
# fastlane production_rollout percentage:100
```

## Trade-offs

| Solução | Setup | Custo | Signing management | Ideal para |
|---|---|---|---|---|
| Fastlane + GitHub Actions (macOS) | Alto | Alto (macOS runner) | Match (git) | Apps nativos complexos |
| EAS Build | Baixo | Pago por build | Automático na nuvem | Expo/RN Managed |
| Xcode Cloud | Médio | Grátis (25h/mês) | Nativo Xcode | iOS-first teams |
| Bitrise / AppCircle | Médio | Pago | Integrado | Enterprise |

## Quando Usar / Quando Evitar

**EAS Build** para novos projetos React Native — zero configuração de signing, build na nuvem.

**Fastlane + Match** quando precisar de controle total e já tiver infraestrutura GitHub.

**OTA Updates** para hotfixes e ajustes de UI — não passam pela review da store, mas têm restrições (não pode alterar código nativo).

**Nunca:** commitar keystore ou certificados no repositório, usar signing manual em CI, ignorar versionamento de build number (causa rejeição na store).

## Conceitos Relacionados
[[mobile-testes]] · [[mobile-monitoramento]] · [[mobile-baseline-profiles]] · [[cicd-pipeline]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
