---
type: entity
title: "Bubblewrap (bwrap)"
aliases: ["bubblewrap", "bwrap", "brwap"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 1
tags: [ferramenta, sandboxing, linux, gnome, flatpak, security]
skill: tech-mentor-security
status: stub
---

# Bubblewrap (bwrap)

Binário de sandboxing para Linux, mantido pelo time do GNOME, com menos de 1 MB e capaz de rodar sem privilégio de root. É o componente usado pelo **Flatpak** para isolar aplicativos de desktop no Linux.

## Uso em Contenção de Agentes de IA

[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] descreve o **AI Jail**, ferramenta de [[wiki/entities/fabio-akita]] construída sobre o Bubblewrap para isolar agentes de codificação (Claude Code, Codex, OpenCode, Crush) — ver [[wiki/concepts/agent-containment]]. O mesmo binário é usado internamente pelo sandbox nativo do [[wiki/entities/claude-code]] no Linux (desde outubro de 2025), com Sandbox-exec como equivalente no Mac.

## Key Sources

- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]]
