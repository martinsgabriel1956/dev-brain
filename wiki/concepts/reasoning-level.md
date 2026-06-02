---
type: concept
title: "Reasoning Level (Nível de Raciocínio)"
aliases: ["reasoning level", "nivel de reasoning", "extended thinking", "thinking budget"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [reasoning, llm, custo, qualidade, tokens]
skill: tech-mentor-ai
status: stable
---

# Reasoning Level (Nível de Raciocínio)

Configuração que controla quantos **tokens internos** o modelo gera antes de produzir a resposta visível ao usuário. Tokens de reasoning são parcialmente ocultos (o usuário vê um preview ou nada); eles representam os "passos intermediários" de raciocínio do modelo — análogo ao chain-of-thought mas implementado no treinamento, não no prompt.

## Analogia

Ao resolver "uma camisa de $40 com 25% de desconto e depois 10% de cupom", você não chuta — você calcula passo a passo: 25% de 40 = 10; 40-10 = 30; 10% de 30 = 3; 30-3 = 27. Reasoning é o modelo fazendo esses passos internamente antes de responder.

## Níveis

| Nível | Quando usar | Custo relativo | Velocidade |
|---|---|---|---|
| None / Off | Tarefas triviais; prompt totalmente definido | Mínimo | Máximo |
| Low | Tarefas simples mas não triviais | Baixo | Alto |
| Medium | Maioria das tarefas (default recomendado quando em dúvida) | Médio | Médio |
| High | Planejamento, design, inovação, tarefas complexas | Alto | Baixo |
| Extra High | Máxima liberdade criativa; tarefas de alta incerteza | Muito alto | Muito baixo |

## Regras Práticas

- **Tarefa bem definida (spec pronta)**: mesmo com extra-high, o modelo vai "ver que está tudo definido" e não vai expandir muito o raciocínio. Não desperdiça tanto quanto parece.
- **Prompt ruim + reasoning alto**: o modelo vai gastar muito reasoning tentando deduzir o que você quis dizer — e ainda assim pode errar. Técnica > nivel de reasoning.
- **Default**: se está na dúvida, use medium.
- **Review de código**: medium basta.
- **Planejamento / spec-driven**: high ou extra-high.
- **Trocar label no UI**: none ou low.

## Claude Code default

Claude Code abre no Extra High com Opus 4.7 por padrão. Para tarefas corriqueiras, ajustar manualmente economiza tokens e tempo.

## Relação com Custo

O nível de reasoning não muda o preço do modelo (input/output price per token é o mesmo), mas gera mais tokens de raciocínio que são cobrados como output. Extra High pode multiplicar o custo de output de uma tarefa em 3–5x.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
