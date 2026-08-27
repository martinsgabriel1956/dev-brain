---
type: source
title: "Prompt Engineering, Context Engineering e Harness Engineering — Os Três Pilares"
aliases: ["três pilares da ia", "prompt context harness engineering"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 0
tags: [prompt-engineering, context-engineering, harness, clean-architecture, evolucao-conceitual]
skill: tech-mentor-ai
status: stable
source_file: raw/prompt-context-harness-engineering-tres-pilares.md
source_url: ""
author: "não identificado"
date_published: 2026
date_ingested: 2026-08-27
---

# Prompt Engineering, Context Engineering e Harness Engineering — Os Três Pilares

## TL;DR

Transcrição didática (autor não identificado) que narra a evolução histórica prompt engineering → context engineering → harness engineering como resposta ao crescimento da janela de contexto (4.000 tokens em 2022 → 1 milhão hoje). Reafirma, em português, a versão traduzida do mantra viral de [[wiki/entities/peter-steinberger]] ("se você não é o modelo, você é o harness") e usa o gráfico de complexidade-versus-tempo de [[wiki/entities/uncle-bob]] (Clean Architecture) como justificativa para investir em harness/arquitetura à medida que um projeto cresce. Fonte majoritariamente corroborativa — não traz claims novos de peso frente ao que já está documentado em [[wiki/concepts/harness]] e [[wiki/concepts/context-engineering-harness]], mas fecha a ponte narrativa entre os três conceitos numa única fala contínua e amarra explicitamente o argumento de Clean Architecture ao motivo de investir em harness.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Em 2022 (era ChatGPT inicial), a janela de contexto era de ~4.000 tokens; hoje chega a 1 milhão | Falado diretamente, sem fonte citada, mas consistente com a tabela já registrada em [[wiki/concepts/context-window]] (GPT-3, 2020: 4.096 tokens) | Média — número redondo, sem modelo específico nomeado |
| Evolução prompt engineering → context engineering → harness engineering acompanha o crescimento da janela de contexto disponível | Narrativa central da fonte | Média — plausível e consistente com o resto da wiki, mas apresentada como intuição do autor, não como fato historicamente documentado |
| "Se você não é o modelo, você é o harness" | Mantra citado sem atribuição de autoria | Alta como corroboração (o mantra em si já está atribuído a [[wiki/entities/peter-steinberger]] noutra fonte) — esta fonte não credita ninguém |
| Complexidade de software cresce com o tempo independente de IA (gráfico de Robert Martin/Clean Architecture); harness é o mecanismo para manter essa complexidade sob controle | Citação direta a Robert Martin, sem gráfico específico apontado | Média — referência de memória, sem página/capítulo do livro citado |
| Harness tem duas camadas: a embutida na ferramenta (Claude Code, Cursor, AntiGravity, e dois nomes não identificados por ruído de transcrição) e a que o usuário constrói (CLAUDE.md, regras, skills, MCP, workflow de planejamento e testes) | Descrição ao vivo com diagrama | Alta — consistente com a dicotomia provider harness/user harness já registrada em [[wiki/concepts/harness]] |
| Contexto insuficiente ou contexto excessivo levam a "besteira"; o ponto ótimo é contexto certo no momento certo, alcançável só com bom harness | Conclusão da fonte | Alta — reafirma a tese central já registrada em [[wiki/concepts/context-engineering-harness]] |

## Entidades Mencionadas

- [[wiki/entities/claude-code]] — citado como exemplo de harness
- [[wiki/entities/cursor]] — citado como exemplo de harness
- Dois nomes de harness não identificados por ruído de ASR na transcrição original ("Itubilot CLI", "diminers") — possivelmente GitHub Copilot CLI e Gemini CLI, não confirmado
- AntiGravity (Google) — citado como exemplo de harness, ver [[wiki/entities/google]]
- [[wiki/entities/uncle-bob]] — citado pelo gráfico de complexidade versus tempo do livro Clean Architecture

## Conceitos Tocados

- [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/context-window]]
- [[wiki/concepts/clean-architecture]]

## Open Questions

1. **Autoria não identificada.** A transcrição não contém nome do canal/autor nem se autorreferencia. Tratado como fonte anônima até identificação futura.
2. **Dois harnesses citados de ouvido, não identificados com confiança** ("Itubilot CLI", "diminers") — mantidos como transcritos, sem forçar correspondência a ferramentas reais.
3. **Número "4.000 tokens em 2022" não amarrado a um modelo específico** — a wiki já registra GPT-3 (2020) com 4.096 tokens em [[wiki/concepts/context-window]]; a fonte fala genericamente de "quando começou a ter ChatGPT", o que teria sido GPT-3.5 (nov/2022), sem confirmar se o número citado é preciso para esse modelo especificamente.

## Raw Quotes

> "Se você não é o modelo, você é o harness."

> "Se eu passo pouco contexto para a IA, ela faz besteira. Se eu passo contexto demais para a IA, ela também faz besteira. Então o ponto ótimo é o meio-termo."

> "A LLM por si só é como se fosse um cérebro que não faz nada. Tem muita inteligência, eu consigo pensar um monte de coisas, mas eu não entrego nenhum valor."

## Key Sources (fontes citadas nesta ingestão)

Nenhuma — fonte primária desta ingestão.
