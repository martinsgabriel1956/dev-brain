---
type: concept
title: "Fake Delay"
aliases: ["minimum delay", "delay mínimo UX", "perceived performance"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [ux, performance-percebida, animações, feedback-visual, design]
skill: tech-mentor-frontend
status: stable
---

# Fake Delay

Técnica de UX que **aplica um delay mínimo intencional** em interações muito rápidas para que o feedback visual (spinner, loading state) seja perceptível ao usuário.

## O problema

Quando uma operação completa em < 100ms, o spinner aparece e desaparece tão rápido que parece um bug ou glitch — pior do que não ter spinner. O usuário não tem certeza se a ação foi registrada.

## A solução

```typescript
const MIN_DELAY_MS = 300;

async function submitForm(data: FormData) {
  const [result] = await Promise.all([
    api.submit(data),
    new Promise(resolve => setTimeout(resolve, MIN_DELAY_MS)) // fake delay
  ]);
  return result;
}
```

O `Promise.all` garante que a operação real e o delay rodam em paralelo — se a API demorar 500ms, o delay não adiciona tempo. Só adiciona se a API responder em < 300ms.

## Threshold recomendado

- **300ms** — threshold perceptual humano para feedback de ação
- Abaixo de 100ms: resposta parece instantânea (ok para hover, highlights)
- 100–300ms: zona cinza — spinner pode piscar estranhamente
- Acima de 300ms: usuário espera feedback explícito

## Quando aplicar

✅ Submissão de formulários
✅ Ações destrutivas (deletar, arquivar)
✅ Navegação entre páginas pesadas

❌ Hover states
❌ Inputs de texto (feedback deve ser imediato)
❌ Operações que o usuário sabe que são lentas (upload de arquivo)

## Relação com performance percebida

Fake delay é o oposto de [[optimistic-updates]] — em vez de esconder a espera, **valida a espera** mostrando que algo aconteceu. As duas técnicas coexistem dependendo do contexto.

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
