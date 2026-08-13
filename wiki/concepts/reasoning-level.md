---
type: concept
title: "Reasoning Level (Nível de Raciocínio)"
aliases: ["reasoning level", "nivel de reasoning", "extended thinking", "thinking budget"]
date_created: 2026-06-02
date_updated: 2026-08-12
source_count: 4
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

## Custo do Contexto Inicial em Loops que Reiniciam Sessão

Em loops determinísticos que abrem uma sessão nova a cada round (contexto anterior descartado — ver [[wiki/concepts/loop-engineering#Loop Determinístico vs. Loop Agêntico]]), o trecho mais custoso do reasoning é a formulação inicial de contexto, paga run atrás de run e descartada a cada round. [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] recomenda reasoning mais baixo nesse cenário quando já existe bom aparato de artefatos de estado salvos — situação distinta de "prompt ruim + reasoning alto" acima porque aqui o desperdício vem da repetição estrutural do loop, não da qualidade do prompt.

**Tensão a resolver:** essa mesma fonte também afirma que, em tasks de spec driven já bem definidas (critérios de sucesso, testes, descrição mínima por task), reasoning muito alto (GPT 5.6, Fable) faz cada task demorar mais do que precisaria. Isso está em tensão direta com a regra já registrada acima ("tarefa bem definida: mesmo com extra-high, o modelo não desperdiça tanto quanto parece" — de [[wiki/sources/formacao-ia-devs-aula-03-llm]]/[[wiki/sources/formacao-ia-devs-aula-04-harness]]). Uma leitura possível: a regra antiga fala de desperdício de *tokens/qualidade*, e a nova fala de desperdício de *tempo/latência* — reasoning alto pode não piorar o resultado, mas ainda assim ser lento demais para tasks já bem especificadas. Tratar como não resolvido até mais fontes confirmarem.

## Reasoning Baixo Pode Esconder Oportunidades de Paralelismo

Com effort/reasoning baixo, o Claude Code pode deixar de reconhecer que uma tarefa é paralelizável em [[wiki/concepts/subagentes]] — um mesmo prompt de pesquisa (comparar 3 provedores) só disparou 3 subagentes em paralelo depois de subir o effort de low para high. Reasoning insuficiente não só piora a resposta, como pode reduzir a própria capacidade de orquestração do agente.

## Relação com Custo

O nível de reasoning não muda o preço do modelo (input/output price per token é o mesmo), mas gera mais tokens de raciocínio que são cobrados como output. Extra High pode multiplicar o custo de output de uma tarefa em 3–5x.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — custo de reformulação de contexto em loops que reiniciam sessão; tensão não resolvida com a regra de "tarefa bem definida não desperdiça reasoning alto"
