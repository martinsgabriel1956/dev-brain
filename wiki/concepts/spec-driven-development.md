---
type: concept
title: "Spec-Driven Development"
aliases: ["SDD", "spec driven", "desenvolvimento orientado a especificação", "planning-first"]
date_created: 2026-06-02
date_updated: 2026-06-09
source_count: 7
tags: [spec-driven, planejamento, ia-para-devs, harness, agente, qualidade]
skill: tech-mentor-ai
status: stable
---

# Spec-Driven Development

Abordagem de desenvolvimento com IA em que **o planejamento e a especificação da tarefa ocorrem antes da execução**. O dev atua como "gerente" — define o quê e o porquê; a IA executa o como. É o que diferencia o nível L3 (gerente) do L2 (babysitting) na [[wiki/concepts/niveis-adocao-ia-l0-l4|escala de adoção]].

## Por Que é Necessário

No modelo tradicional (L2), o dev instrui a IA em micro-steps sucessivos: "cria o endpoint", "agora adiciona a validação", "agora persiste no banco". Isso:
- Maximiza o idle (esperando cada resposta)
- Impede paralelismo
- Gera contexto poluído de vai-e-vem
- Produz resultado inconsistente (sem visão do todo)

Com spec-driven, uma spec bem escrita é enviada de uma vez para execução autônoma. O dev pode paralelizar outras tarefas enquanto a execução corre.

## O Processo

### 1. Planejamento (Plan Mode)
Criar uma especificação estruturada da tarefa usando [[wiki/concepts/xml-markdown-prompts|XML+Markdown template]]. Iterar com o LLM para refinar:
- Requisitos funcionais
- Contratos de API
- Critérios de aceite
- Restrições (faça/nunca faça)
- Considerações de UI/UX
- Questões técnicas abertas

### 2. Limpeza de Contexto
Após o planejamento, fazer `/clear` para começar a execução com contexto limpo. O planejamento (240–400k tokens) fica registrado no arquivo de spec, não no contexto.

### 3. Execução
Enviar a spec ao agente em modo não assistido (YOLO). O agente usa as [[wiki/concepts/tool-call|tool calls]] do [[wiki/concepts/harness]] para ler o projeto, implementar e executar testes, sem intervenção do dev.

### 4. Revisão
Revisar o resultado final (PR level) + resultado prático (testes passando, comportamento correto), não linha a linha do código.

## Fluxo com Agentes Especializados

Para problemas complexos (múltiplos domínios, semanas de trabalho), o SDD usa agentes especializados com [[wiki/concepts/human-in-the-loop|human-in-the-loop]] em cada etapa:

```
Ideia → [Agente PRD] → PRD aprovado
     → [Agente Tech Spec] → Tech Spec aprovada
     → [Decomposição] → Lista de tarefas aprovada
     → [Execução isolada por tarefa] → [QA] → Done
```

- O [[wiki/concepts/agente-prd|Agente de PRD]] faz perguntas iterativas para refinar requisitos
- O agente de [[wiki/concepts/tech-spec|Tech Spec]] consome PRD + rules + análise do código
- Cada tarefa recebe PRD + Tech Spec + descrição isoladamente (não o projeto inteiro)
- Para projetos grandes: [[wiki/concepts/task-looper|task looper]] automatiza a execução das tarefas

> "PRD não é um documento feito para a empresa, é um documento feito para a IA." — [[wiki/entities/pedro-nauke]]

## Onde Ficam os Padrões de Arquitetura

Padrões globais (framework, linguagem, infraestrutura) ficam nas [[wiki/concepts/rules-agente|rules]], não no PRD ou Tech Spec. O PRD e a Tech Spec **referenciam** as rules, não as repetem.

## Quando Usar SDD

- Features novas complexas (múltiplos arquivos, múltiplos domínios)
- Refactoring de larga escala
- Migrações entre tecnologias ou versões
- Tarefas que normalmente levariam semanas de trabalho humano

Para tarefas menores, use [[wiki/concepts/plan-mode|Plan Mode]].

## Relação com Documentação

A spec não é uma "living documentation" permanente. É produzida para guiar uma execução e pode ser arquivada ou descartada após o merge. O código + testes + PR description documentam a decisão de forma mais duradoura.

## Ferramentas de Suporte

- **Compose** (Pedro Nauke): orquestrador spec-driven open source
- **Cairo**: harness com spec-driven nativo
- **Claude Code Plan Mode**: `/plan` ou Shift+Tab para entrar no modo de planejamento sem executar

## Diferença de Prompt Engineering

| Prompt Engineering | Spec-Driven Development |
|---|---|
| Foco: como estruturar um prompt | Foco: como estruturar o processo completo |
| Escala: tarefa individual | Escala: feature/sprint |
| Artefato: um prompt | Artefato: spec + tasks + contexto do projeto |
| Autonomia: baixa (L2) | Autonomia: alta (L3) |

## Critério de Granularidade Confirmado em Campo

A engenheira do Cursor (2026) articula o critério para tamanho de task para agente:

> "A menor quantidade de trabalho mais a maior quantidade que um agente consegue fazer sem esbarrar em outro agente."

Na prática: uma feature completa com migration, schema e API repository é feita junta — para que o agente entregue de ponta a ponta sem dependência bloqueante de outro agente. Cada feature dispara ~5 agents simultâneos. A coordenação antes era entre devs paralelos; agora é entre agentes paralelos — o trabalho de coordenação não acabou, mudou de objeto.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-abertura]]
- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
