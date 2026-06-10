---
type: source
title: "Formação IA para Devs — Aula 05: Hands-on — Harness e Prompt Engineering"
aliases: ["IA para Devs Aula 5", "Hands-on Harness Prompt Engineering"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [ia-para-devs, prompt-engineering, xml-markdown, meta-prompting, plan-mode, hands-on, harness]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 05 - Hands-on - Harness e Prompt Engineering.md"
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: "2026"
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 05: Hands-on — Harness e Prompt Engineering

## TL;DR

Demo prática comparando três harnesses (Codex/GPT-5.5, Claude Code/Opus 4.7, Cursor/Kimi K2.5) rodando o mesmo prompt em dois cenários: prompt vago e prompt estruturado com XML+Markdown template. O resultado mostra que um prompt estruturado melhora drasticamente o alinhamento com expectativas — mesmo sem rules/skills — e que um modelo open source 10x mais barato entrega resultado comparável em tarefas bem especificadas.

## Key Claims

- **Prompt vago = resultado imprevisível**: prompt "implemente um painel de clima" sem especificar campos resultou em time zone e percentual de nuvem não solicitados, componente único com 320 linhas. Evidência: demo ao vivo com Codex/GPT-5.5.
- **XML+Markdown template melhora alinhamento** sem mudar o modelo: mesma tarefa com prompt estruturado por seções (task, requirements, ui-ux, constraints, acceptance-criteria) produziu painel com 7 dias de previsão, ícones corretos, UV index, layout responsivo — tudo conforme especificado. Evidência: comparação direta ao vivo.
- **Custo do planejamento**: 260k tokens = ~$1 para a fase de spec. Isso é substancialmente mais barato do que vai-e-vem iterativo de L2. Evidência: Branas mostra o contador de tokens no terminal.
- **Meta-prompting**: usar `[placeholder: instrução]` dentro do template para guiar o LLM a substituir com conteúdo específico — funciona como variável. Misturar XML com Markdown é recomendado por pesquisas da Anthropic e OpenAI. Evidência: Nauke cita papers de prompting.
- **Tags XML não precisam ser fechadas nem ter nome padronizado**: não é compilado, é probabilístico. Funciona igual em português, inglês ou japonês. Evidência: Nauke explica a diferença de parsing sintático vs semântico.
- **Plan Mode na mão**: pedir "você sugere algo a mais?" ativa uma "chave diferente" no LLM — ele para de gerar tokens de código e passa a sugerir melhorias. Iterativo + orientado a template = plan mode manual. Evidência: demo de Branas.
- **Contexto limpo antes de executar**: após planejamento (260k tokens), fazer `/clear` e iniciar nova sessão de execução com o prompt refinado. Evidência: Branas demonstra o workflow completo.
- **Evolução**: prompt engineering → context engineering → harness engineering. O próximo passo citado: "ADI engineering"? Evidência: Nauke coloca a linha evolutiva.
- **Inglês vs Português**: diferença de resultado "quase zero" nos modelos atuais — embeddings de "blue" e "azul" estão próximos no espaço vetorial. Evidência: Branas explica via embedding space.
- **Adobe liberou 50+ tools via MCP** durante a aula (marco histórico citado ao vivo) — acesso ao Photoshop, Illustrator etc. via Claude Code. Evidência: Nauke anuncia ao vivo como "grandíssimo marco".
- **Comparativo de harnesses**: Codex/GPT-5.5 e Claude Code/Opus 4.7 tiveram resultados similares (Opus melhor no design arquitetural do backend); Cursor/Kimi K2.5 foi mais rápido e entregou resultado comparável custando ~10x menos. Evidência: três runs lado a lado com mesma spec.

## Template de Prompt Estruturado (padrão XML+Markdown)

```xml
<task>
  Nome da tarefa — referenciável nas outras seções sem repetir
</task>

## Requirements
[placeholder: liste os requisitos funcionais da <task>]

## API Contract
[placeholder: descreva os endpoints necessários]

## UI/UX
[placeholder: descreva o layout esperado com base nos requisitos]

## Constraints
- Faça: ...
- Nunca faça: ...

## Acceptance Criteria
[placeholder: critérios Given/When/Then]
```

## Workflow Demonstrado

1. Escrever prompt inicial simples (vago)
2. Criar template com seções XML+Markdown
3. Pedir ao LLM: "converta o prompt na estrutura do template e salve em prompt2.md"
4. Iterar: "adicione previsão de 7 dias", "traga velocidade do vento e UV index", "você sugere algo?"
5. Abrir contexto limpo (`/clear`)
6. Executar com o prompt refinado

## Entities

- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/claude-code]]
- [[wiki/entities/codex-openai]]
- [[wiki/entities/cursor]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/adobe]] — liberou 50+ tools via MCP durante a aula

## Concepts

- [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/xml-markdown-prompts]]
- [[wiki/concepts/meta-prompting]]
- [[wiki/concepts/plan-mode]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/mcp-server]]

## Open Questions

- Existe um formato padronizado de template para spec-driven (além do XML+Markdown)?
- Como o "plan mode manual" via prompts se compara ao plan mode nativo dos harnesses em eficiência de tokens?

## Raw Quotes

> "Requisitos vagos — sabor spec driven, né? A gente não tem os requisitos claros. O modelo foi lá e gerou o que ele quis." — Pedro Nauke

> "Você concorda que quando eu falar em painel de tempo pode vir qualquer coisa? Não tem bola de cristal." — Rodrigo Branas

> "A evolução: prompt engineering → context engineering → harness engineering. Qual é o próximo?" — Pedro Nauke

> "A Adobe dobrou os joelhos para a IA. Agora é possível acessar Photoshop, Illustrator e tudo mais via Claude Code." — Pedro Nauke
