---
type: concept
title: "Native Module (React Native)"
aliases: ["módulo nativo", "NativeModules RN", "TurboModule"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [mobile, react-native, native-module, ios, android, kotlin, swift]
skill: tech-mentor-mobile
status: stable
---

# Native Module (React Native)

Native Module é a ponte entre JavaScript e código nativo (Kotlin/Swift) no React Native. Usado quando não existe lib npm madura para uma funcionalidade específica da plataforma.

## Quando criar

Apenas quando não existe lib madura — o custo de manter código nativo iOS + Android é alto (dois codebases, dois reviewers com conhecimento nativo, dois conjuntos de bugs).

## Estrutura

```
Android (Kotlin)   →   @ReactMethod expose via Promise
iOS (Swift/ObjC)   →   @objc + RCTPromiseResolveBlock
TypeScript         →   typed wrapper sobre NativeModules
```

## Exemplo: SecureStorage

O wrapper TypeScript abstrai `NativeModules.SecureStorage` com tipos explícitos, expondo uma API limpa (`secureStorage.set`, `.get`, `.delete`) sem expor os detalhes de Promise/NativeModules para o código de produto.

## Alternativa moderna

TurboModules (nova arquitetura RN via JSI) eliminam a bridge serializada — acesso direto à memória. Para novos módulos, preferir a API de TurboModules se o projeto já usa nova arquitetura.

## Key sources

- [[sources/mobile-platform-engineering]]
