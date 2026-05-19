---
type: entity
title: "Claude Code"
aliases: ["claude code cli"]
date_created: 2026-05-18
date_updated: 2026-05-18
source_count: 1
tags: [ferramenta, agentes-ia, anthropic, llmops, cli]
skill: tech-mentor-ai
status: stub
---

## O Que É

CLI da Anthropic que permite usar Claude como [[agente-ia]] diretamente no terminal, com acesso a ferramentas (leitura/escrita de arquivos, execução de código, busca na web). Opera com uma [[janela-de-contexto]] que acumula ao longo da sessão e faz reset em intervalos (tipicamente 3–5 horas, dependendo do plano).

---

## Relevância para Token Anxiety

O mecanismo de reset da janela de contexto do Claude Code é um dos principais catalisadores do fenômeno [[token-anxiety]]: desenvolvedores sentem urgência de maximizar o uso dos tokens disponíveis antes do próximo reset, o que distorce rotinas e prioridades.

---

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
