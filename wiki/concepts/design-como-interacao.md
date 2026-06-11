---
type: concept
title: "Design como Interação"
aliases: ["design is interaction", "design além do visual", "design funcional"]
date_created: 2026-06-11
date_updated: 2026-06-11
source_count: 1
tags: [design, ux, interação, micro-interações, performance-percebida]
skill: tech-mentor-frontend
status: stable
---

# Design como Interação

Design não é o que o usuário vê quando abre a aplicação — é o que ele **sente enquanto usa**. A qualidade de um design se revela na interação, não na primeira impressão visual.

> "Por que é mais prazeroso clicar num botão do Linear do que num botão qualquer?" — essa diferença é design.

---

## O que Constitui Design Além do Visual

| Dimensão | Exemplo |
|---|---|
| **Micro-interações** | Animações de botão, transições de página |
| **Feedback visual** | Spinner, loading state, confirmação de ação |
| **Performance percebida** | [[concepts/fake-delay]] para tornar ações rápidas perceptíveis |
| **Onboarding** | Primeira experiência do usuário com o produto |
| **Acessibilidade** | Produto funciona para o público-alvo em qualquer contexto |
| **Linguagem** | Tom dos erros, labels, mensagens vazias |

---

## A Ilusão do "Bonito"

Estudar design só pela parte visual (combinar cores, espaçamentos) pode produzir layouts bonitos sem utilidade. O diferencial é **conhecer o público** e construir algo direcionado.

- Botões são visualmente quase idênticos entre aplicações
- O que diferencia é a resposta ao clique: timing, animação, estado intermediário
- [[entities/linear]] é a referência mais citada por devs frontend justamente por esse nível de cuidado

---

## Para o Dev

O papel do [[concepts/design-engineer]] é implementar essas camadas de detalhe. Não é apenas "fazer bonito" — é garantir que cada interação seja intencional e coerente.

Técnicas concretas:
- `Promise.all([fetch, sleep(MIN_DELAY)])` para garantir feedback mínimo visível
- Transições CSS com duração e easing cuidadosos
- Estados de loading, erro e vazio tratados como partes do design

---

## Relação com Outros Conceitos

- [[concepts/fake-delay]] — exemplo prático de design de interação
- [[concepts/design-engineer]] — o papel que implementa design como interação
- [[entities/linear]] — referência máxima de aplicação com design de interação de alta qualidade

## Key Sources

- [[sources/design-first-vs-code-first-referencias]]
