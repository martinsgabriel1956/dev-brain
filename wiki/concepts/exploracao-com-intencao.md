---
type: concept
title: "Exploração com Intenção"
aliases: ["intentional exploration", "explorar código com objetivo", "seguir o fio", "navegação intencional"]
date_created: 2026-04-29
date_updated: 2026-07-23
source_count: 3
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

## Aplicação em Manutenção (Não Só Onboarding)

[[wiki/sources/como-lidar-com-tarefas-dificeis-sendo-junior]] aplica o mesmo mecanismo a um cenário diferente do onboarding original: **descobrir pontos de alteração** numa codebase já conhecida pelo time, ao receber uma tarefa de correção/ajuste. O erro comum descrito é o oposto da exploração com intenção — o iniciante busca direto o ponto aparentemente óbvio (ex.: um `Ctrl+Shift+F` pelo texto exato de uma mensagem de erro), ignorando que a causa real pode estar numa regra de negócio anterior no fluxo. A técnica recomendada é idêntica: comece pela ação do usuário (onde clica, como chega na tela, o que precisa preencher) e siga o fluxo completo — front-end → controller/API → service → banco — anotando o que cada trecho faz, até identificar o ponto real que precisa mudar. Isso amplia o escopo da técnica de "aprender uma codebase nova" para "diagnosticar corretamente onde alterar", mesmo em código já familiar ao time.

## Key Sources

- [[wiki/sources/como-aprender-novas-codebases]]
- [[wiki/sources/como-lidar-com-tarefas-dificeis-sendo-junior]] — mesma técnica aplicada a descoberta de pontos de alteração em manutenção/correção de bugs
