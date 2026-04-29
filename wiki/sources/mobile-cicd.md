---
type: source
title: "CI/CD Mobile — Fastlane, GitHub Actions, EAS Build, Code Signing, Rollout Gradual"
aliases: ["mobile cicd", "fastlane match", "eas build", "mobile code signing", "mobile deploy"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-cicd.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, cicd, fastlane, github-actions, eas-build, code-signing, rollout]
skill: tech-mentor-mobile
status: stable
---

# CI/CD Mobile

## TL;DR

Fastlane `match` gerencia certificados/provisioning em repositório git criptografado — elimina "works on my machine" em signing. EAS Build para Expo/RN Managed sem servidor macOS próprio. Rollout gradual na Play Console (10% → 50% → 100%) e TestFlight para iOS. Pipeline mínimo: lint → testes → build → distribute → notify.

## Claims Principais

| Claim | Confiança |
|---|---|
| Fastlane `match` — certificados em git criptografado, renovação automática, sem dependência de conta pessoal | Alta |
| EAS Build elimina necessidade de macOS runner para builds Expo/RN — custo menor | Alta |
| Rollout gradual Play Console detecta crashes antes de atingir 100% da base | Alta |
| Xcode Cloud gratuito até 25h/mês — suficiente para times iOS pequenos | Alta |

## Conceitos Abordados

- [[mobile-cicd]] · [[mobile-testes]] · [[mobile-monitoramento]] · [[mobile-baseline-profiles]] · [[cicd-pipeline]]
