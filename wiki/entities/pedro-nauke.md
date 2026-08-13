---
type: entity
title: "Pedro Nauke"
aliases: ["Nauke", "Nauck", "Pedro Nauke", "Pedro Nauck", "pernop"]
date_created: 2026-06-02
date_updated: 2026-08-12
source_count: 9
tags: [instrutor, ia-para-devs, compose, tooling, brasil, open-source, carreira]
skill: tech-mentor-ai
status: stable
---

# Pedro Nauke

Desenvolvedor brasileiro com 20+ anos de experiência (a fonte de carreira usa "22 anos"; outra fonte usa "mais de 20 anos" — mesma pessoa, pequena variação de arredondamento entre vídeos), iniciou aos 12 anos. Especialista em tooling (Rust, Go), com background extenso em frontend, e nos últimos 3+ anos focado profundamente em IA aplicada ao desenvolvimento. Co-criador da Formação IA para Devs. Criador do Compose, ferramenta open source de orquestração spec-driven. Também criador do **Docz**, gerador de documentação open source (~20 mil estrelas no GitHub), citado como exemplo pessoal do peso de manter um projeto open source popular. No vídeo de carreira, se apresenta como dev na **Fuel Network**. Grafia do sobrenome varia entre fontes: "Nauke" (Formação IA para Devs) e "Nauck" (vídeo de carreira) — mesma pessoa.

## Perfil

- **Background**: web dev completo (UI/UX, frontend, backend), viragem para low-level/tooling nos últimos 10 anos
- **Linguagens**: Rust, Go, JavaScript/TypeScript
- **Criações open source**: Compose (orquestrador spec-driven, ~600 stars GitHub)
- **Instagram**: @pernop — conteúdo sobre IA e dev
- **Processo de trabalho**: spec-driven extensivo; já rodou 6 contas simultâneas (3 Codex + 3 Claude Code); trabalha principalmente à noite com tasks rodando em paralelo

## Posições e Opiniões Conhecidas

- "Team OpenAI" — prefere GPT-5.x para backend complexo; Opus para frontend/review
- Defende que Go é a linguagem mais AI-friendly (escopo fechado, erros explícitos, baixa ambiguidade)
- Acredita que problemas com IA são quase sempre de contexto/técnica, não do modelo
- Não recomenda Sonnet 4.6 ("de tanto que eu não gosto dele")
- Neurodivergente — acredita ter vantagem natural em paralelismo de tarefas

## Compose Tool

Ferramenta de orquestração spec-driven que:
- Gerencia worktrees e execução paralela de tarefas
- Integra com Code Rabbit para fazer fetch de issues e resolver em loop
- Filosofia: spec-driven sem ficar preso no babysitting

## Posições e Opiniões Conhecidas (Carreira)

- Ego não discrimina entre júnior e sênior — o sintoma mais nocivo no sênior é travar discussões técnicas por teimosia em vez de aceitar o consenso do time
- Side projects populares podem virar "mais maldição que bênção" pela pressão de manutenção que criam
- Reinventar a roda raramente é inovação genuína — geralmente é remix, e o custo real está na manutenção extra desnecessária
- Overthinking/over-engineering (ex.: resolver escalabilidade antes de ter um usuário) é um erro que ele mesmo cometeu; código é ferramenta a serviço de pessoas, não o objetivo final
- Entregar algo funcional e imperfeito vale mais que algo inacabado e "perfeito"

## Posições e Opiniões Conhecidas (Loop Engineering)

- Constrói o Compose sobre o conceito de loop engineering desde julho de 2025 — antes do termo virar hype em 2026
- Argumenta que "loop engineering matou harness engineering" é uma leitura invertida: o loop contém o harness, não o substitui
- Gerencia no máximo 4-5 loops/worktrees paralelos antes de perder controle
- Divide loop em **determinístico** (script que reinicia sessão a cada round, exemplo o próprio Compose) vs. **agêntico** (via `/go`, nunca reinicia run, compacta em vez de reiniciar) — a divisão que, na visão dele, mais decide qual modelo usar e quanto se gasta ([[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]])
- Considera o Codex, hoje, o harness que melhor entrega loop agêntico via `/go`, por causa da qualidade de compactação de contexto
- Testou spec driven com e sem breakdown prévio de tasks em loop determinístico e agêntico: sem breakdown, resultado pior mesmo em loop agêntico — contraria a leitura popular de que "spec driven morre" em loops agênticos
- Usa "padrão judge" (agente separado, via stop hook, julga se a run terminou) principalmente com modelos menos densos em long tasks (Opus, Grok, Sonnet); considera desnecessário com Fable/GPT 5.6
- Usa "padrão orquestrador": modelo caro/denso orquestra modelos mais baratos por tipo de tarefa (ex.: GPT 5.6 para back-end, Opus 4.8/Grok 4.5 para front-end) em vez de implementar ele mesmo
- Relata estar substituindo cada vez mais o próprio Compose (determinístico) por loop agêntico com modelos de reasoning alto, por evitar o autoconsumo de contexto do reinício de sessão a cada round

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-abertura]]
- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
- [[wiki/sources/verdades-duras-programador-20-anos-pedro-nauck]]
- [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — vídeo 2 da série (autoria inferida): loop determinístico vs. agêntico, padrão judge, padrão orquestrador, gerenciamento de estado, skills
