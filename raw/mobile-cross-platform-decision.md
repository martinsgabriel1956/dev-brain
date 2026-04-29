---
date: 2026-04-23
tags: [tech-mentor, mobile, cross-platform, flutter, react-native, kmp, nativo, decisão]
skill: tech-mentor-mobile/references/arquitetura
level: avançado
---

# Decisão Cross-Platform — Flutter vs React Native vs KMP vs Nativo

## Contexto
Esta é a decisão de arquitetura mais estratégica de um projeto mobile. Errar aqui custa 6–18 meses de retrabalho. Não existe resposta universal — existe a resposta correta dado o contexto de negócio, equipe e escala. A pergunta não é "qual é a melhor tecnologia?" mas "qual otimiza o maior número de restrições do meu contexto?".

## Como Funciona

### Mapa de decisão

```
Equipe tem expertise em TypeScript/React?
  → Sim: React Native + Expo (time-to-market mais rápido)
  → Não: avançar

App precisa de UI altamente customizada e consistência pixel-perfect entre plataformas?
  → Sim: Flutter
  → Não: avançar

Produto é iOS-only ou iOS-first com equipe Swift?
  → Sim: Swift + SwiftUI nativo
  → Não: avançar

Produto é Android-only ou precisa de integração profunda com ecossistema Google?
  → Sim: Kotlin + Compose nativo
  → Não: avançar

Precisa compartilhar lógica de negócio entre iOS e Android mas manter UI nativa?
  → Sim: Kotlin Multiplatform (KMP)
  → Não: React Native ou Flutter
```

### Tabela de trade-offs

| Critério | React Native | Flutter | Swift/SwiftUI | Kotlin/Compose | KMP |
|---|---|---|---|---|---|
| **Performance** | Boa (nova arquitetura) | Excelente | Excelente | Excelente | Excelente (nativo) |
| **Consistência de UI** | Usa componentes nativos | UI própria (pixel-perfect) | 100% nativa | 100% nativa | UI nativa por plataforma |
| **Acesso a APIs nativas** | Via bridge/turbomodules | Via platform channels | Direto | Direto | Direto |
| **Custo de equipe** | 1 equipe JS | 1 equipe Dart | Equipe iOS | Equipe Android | 1 equipe Kotlin + devs UI |
| **Ecossistema de libs** | Grande (npm) | Crescendo | Maduro | Maduro | Emergindo |
| **Hot reload/DX** | Bom | Excelente | Médio (previews) | Bom (compose preview) | Médio |
| **Startup time** | Médio (JS load) | Excelente | Excelente | Excelente | Excelente |
| **Tamanho do app** | Médio (+5–10MB) | Médio (+10–20MB) | Mínimo | Mínimo | Mínimo |
| **Empresa por trás** | Meta | Google | Apple | JetBrains/Google | JetBrains |
| **Adoção enterprise** | Alta | Alta e crescendo | Alta | Alta | Crescendo (Philips, Netflix, VMware) |

### React Native — Quando escolher

```
✓ Equipe com expertise TypeScript/React
✓ Precisa compartilhar lógica com frontend web (hooks, services)
✓ App com UI seguindo guidelines de cada plataforma (iOS look no iOS, Material no Android)
✓ Integrar com ecossistema npm (SDKs de terceiros com suporte RN)
✓ Time-to-market é prioridade máxima
✓ App de conteúdo (feeds, listagens, forms)

✗ App de câmera/vídeo com processamento em tempo real
✗ App com animações complexas de 120fps (ProMotion)
✗ Jogo ou app com rendering custom por frame
✗ Equipe sem experiência em JavaScript
```

### Flutter — Quando escolher

```
✓ UI altamente customizada (app de design, fintech com UI própria)
✓ Consistência visual perfeita entre iOS e Android é requisito de negócio
✓ App com animações complexas e telas com muitos elementos visuais
✓ Equipe nova pode aprender Dart sem bagagem de JS/TS
✓ Performance como requisito não negociável
✓ Aplicações de kiosk/embedded onde o look nativo não importa

✗ Integração profunda com APIs nativas específicas de plataforma
✗ App que precisa "parecer nativo" para usuários iOS (eles percebem a diferença)
✗ SDK de terceiro só disponível como plugin iOS/Android sem suporte Flutter
```

### Nativo (Swift/Kotlin) — Quando escolher

```
✓ App de sistema ou com integração profunda com hardware (ARKit, CoreML, Camera2)
✓ iOS-only ou Android-only sem planos de expansão
✓ Widgets, Extensions, Complications, Live Activities (não suportados por cross-platform)
✓ Jogo ou app de câmera com processamento por frame
✓ Equipe especializada na plataforma com expertise existente
✓ App onde UX nativa é diferencial competitivo (ex: app de produtividade iOS)

✗ Equipe única precisando manter 2 codebases
✗ Prazo apertado sem equipes dedicadas por plataforma
```

### KMP — Quando escolher

```
✓ Lógica de negócio complexa que precisa ser idêntica em iOS e Android
✓ Empresa já usa Kotlin no backend (reutiliza expertise)
✓ Quer UI nativa em cada plataforma mas com regras de negócio compartilhadas
✓ Casos: apps de banco, saúde, logística (regras complexas, UI nativa crítica)

✗ Time pequeno sem experiência em Kotlin
✗ MVP ou prova de conceito
✗ App simples onde compartilhar lógica não traz benefício real
```

### O que cross-platform não resolve

```
Problemas que cross-platform não elimina:
1. Você ainda precisa entender iOS e Android nativamente para debugar, fazer submit e otimizar
2. APIs nativas novas (Live Activities, Dynamic Island, Predictive Back) chegam no cross-platform meses depois
3. Bugs de integração com plataforma requerem conhecimento nativo para resolver
4. Code signing, provisioning, distribuição são nativos — o framework não abstrai isso
```

### Decisão por contexto de negócio

| Contexto | Recomendação | Justificativa |
|---|---|---|
| Startup, MVP, B2C | React Native (Expo) ou Flutter | Speed over perfection |
| Fintech (UI própria) | Flutter | Consistência + animações |
| Fintech (UI nativa) | KMP + Swift/Kotlin | Regras de negócio compartilhadas, UI que inspira confiança |
| Empresa com equipe web | React Native | Reutiliza expertise JS/TS |
| Enterprise com time Android | KMP ou Kotlin nativo | Reutiliza expertise Kotlin |
| App de sistema (iOS) | SwiftUI nativo | Integração com WidgetKit, App Intents, Live Activities |
| B2B, app interno | Flutter ou RN | Qualquer um funciona, priorizar a expertise da equipe |

## Quando Usar / Quando Evitar

**A maior armadilha:** escolher cross-platform pensando em economizar uma equipe inteira. Na prática, você ainda precisa de alguém com expertise iOS e Android para code signing, store submission, debugging de performance e integração com APIs nativas. Cross-platform reduz o tamanho da equipe, não elimina a necessidade de expertise nativa.

**A segunda armadilha:** migrar de plataforma no meio do projeto. Defina com dados antes de começar — performance bench, expertise da equipe, requisitos de UI — e comprometa-se.

## Conceitos Relacionados
[[mobile-kmp]] · [[mobile-cicd]] · [[mobile-metricas-criticas]] · [[mobile-design-system]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
