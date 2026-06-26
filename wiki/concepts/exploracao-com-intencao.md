---
type: concept
title: "Exploração com Intenção"
aliases: ["intentional exploration", "explorar código com objetivo", "seguir o fio", "navegação intencional"]
date_created: 2026-04-29
date_updated: 2026-06-20
source_count: 2
tags: [codebase, aprendizado, debugging, fluxo-de-dados, onboarding]
skill: tech-mentor-leadership
status: stable
---

# Exploração com Intenção

Técnica de leitura de codebase que consiste em usar o software como usuário final e depois seguir o rastro exato daquela ação no código — em vez de navegar aleatoriamente pela estrutura de arquivos.

## Como fazer

1. Execute uma ação específica na aplicação (ex: usar o apagador no Excalidraw)
2. Formule perguntas concretas sobre aquela ação:
   - Qual código é acionado no `mouseDown`?
   - Onde o elemento é adicionado ao estado?
   - Quais componentes re-renderizam?
   - Onde o undo é disparado?
3. Vá aos arquivos reais e responda cada pergunta lendo o código

## Por que funciona

Cria um [[wiki/concepts/modelo-mental-de-fluxo-de-dados]] claro porque você tem contexto antes de ler — você sabe o que o código *deveria* fazer porque acabou de fazer aquilo como usuário. A busca tem um alvo, não é exploração cega.

## Exemplo concreto

> "Quando desenho um retângulo, qual código roda no mouse down? Onde o shape vai para o estado? Quais componentes re-renderizam? Onde o undo é acionado?"

Rastrear essa pergunta no Excalidraw revela `onPointerDown` → `createGenericElement` → atualização de estado → re-render — um [[wiki/concepts/modelo-mental-de-fluxo-de-dados]] completo para aquela ação.

## Contraste

| Exploração com intenção | Browse aleatório |
|---|---|
| Começa pelo comportamento | Começa pela estrutura |
| Pergunta antes de ler | Lê esperando entender |
| Constrói modelo mental | Acumula código solto |
| Progresso mensurável | Sensação vaga de familiaridade |

## Key Sources

- [[wiki/sources/como-aprender-novas-codebases]]
