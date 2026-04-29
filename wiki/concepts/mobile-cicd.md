---
type: concept
title: "CI/CD Mobile"
aliases: ["fastlane mobile", "eas build", "mobile code signing", "mobile deploy pipeline"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, cicd, fastlane, eas-build, code-signing, rollout, github-actions]
skill: tech-mentor-mobile
status: stable
---

# CI/CD Mobile

## Pipeline Mínimo

```
lint → unit tests → build → E2E (opcional) → distribute → notify
```

## Fastlane Match — Code Signing

```ruby
# Matchfile
git_url("https://github.com/org/certs")
type("appstore")
app_identifier(["com.example.app"])
```

Certificados e provisioning profiles em repositório git criptografado. Qualquer CI/CD clona e instala sem depender de conta pessoal.

```bash
fastlane match appstore --readonly  # CI: apenas lê
fastlane match appstore             # setup: gera/renova
```

## EAS Build (Expo / RN Managed)

```bash
eas build --platform all --profile production
eas submit --platform ios --latest
```

Sem servidor macOS próprio — builds na nuvem Expo. Signing automático.

## Rollout Gradual

**Google Play:** 10% → 25% → 50% → 100%. Monitorar crash-free rate entre estágios.
**TestFlight:** distribuição para testers antes do rollout público.

## GitHub Actions

```yaml
jobs:
  build-android:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: bundle exec fastlane android build
  build-ios:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - run: bundle exec fastlane match appstore --readonly
      - run: bundle exec fastlane ios build
```

## Ver também

- [[cicd-pipeline]] — princípios gerais de pipeline
- [[mobile-testes]] — o que testar antes do build
- [[mobile-monitoramento]] — monitorar após rollout

## Key Sources

- [[wiki/sources/mobile-cicd]]
