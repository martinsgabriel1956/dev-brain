---
type: entity
title: "Abacus.AI"
aliases: ["Abacus", "Abacus AI"]
date_created: 2026-07-31
date_updated: 2026-08-11
source_count: 4
tags: [abacus, model-routing, ai-gateway, ferramenta, cli, agent-farm]
skill: tech-mentor-ai
status: stub
---

# Abacus.AI

Plataforma de IA por assinatura mensal que, entre outras features, oferece um recurso de "Custom Router": permite criar um roteador de modelos próprio, escolhendo um template inicial (ex.: "Frontier") e configurando categorias de tarefa (ex.: Frontier/problem solving, Complexo, Velocidade, Balanceado, Fallback) mapeadas para modelos específicos de diferentes provedores.

## Duas Formas de Roteamento

Segundo [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]]:

- **RouteLL** — roteamento próprio da Abacus, em que a plataforma decide automaticamente qual modelo é mais adequado para cada prompt (mecanismo de decisão não detalhado na fonte).
- **Custom Router** — o usuário define manualmente as categorias e o modelo associado a cada uma; roteamento por categoria estática configurada pelo humano, não por classificador aprendido. Ver [[wiki/concepts/roteamento-automatico-de-modelo]].

O router gerado expõe uma chave de API que pode ser conectada a outros harnesses de codificação (ex.: [[wiki/entities/opencode]]) como se fosse qualquer outro provider.

**Confiança:** a fonte é um vídeo com bloco de patrocínio explícito da Abacus — a demonstração é tratada como exemplo de um padrão genérico (roteamento configurável por categoria), não como avaliação independente da qualidade ou dos preços da ferramenta.

## Multi-Engine Agent Farm e CLI Própria

Segundo [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] (também bloco patrocinado), a Abacus.AI lançou uma feature chamada **Multi-Engine Agent Farm**: ao pedir a criação de uma feature dentro do produto — principalmente via "ZP Agent" — a plataforma dispara um workflow com vários agentes trabalhando em conjunto para subir um projeto complexo do zero (exemplo demonstrado: um SaaS de RH). A mesma fonte descreve uma **CLI própria** da Abacus, comparável em uso ao [[wiki/entities/codex-openai|Codex]] ou ao [[wiki/entities/claude-code|Claude Code]] — utilizável normalmente dentro de uma [[wiki/concepts/worktree-paralelismo|worktree]], como qualquer outro harness. O chat da Abacus dá acesso, num único lugar, a múltiplos modelos de diferentes provedores (citados na demo: Nano Banana 2, "ChatGPT 5.4" `[transcrição incerta sobre a versão exata]`, Claude Opus 4.7).

**Confiança:** ambas as claims vêm de bloco de patrocínio explícito, sem avaliação técnica independente — tratar como demonstração comercial do produto, não como benchmark.

## Key Sources

- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]]
- [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] — Multi-Engine Agent Farm (ZP Agent), CLI própria, chat multi-modelo
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — patrocínio: Custom Router roteando entre Fable/GPT 5.6 Sol/Gemini 3.5/Química por dificuldade/velocidade, plugável no Claude Code/OpenCode
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — patrocínio: agregador de múltiplas IAs (GPT 5.5, Claude Opus 4.8, Fable 5) em subscription única "ZI" por $10/mês, com IDE, Agent Sessions e hospedagem
