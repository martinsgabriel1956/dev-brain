---
type: source
title: "agents.md e CLAUDE.md Ainda Valem a Pena? O que o Paper de Zurique Realmente Diz"
aliases: []
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 0
tags: [agents-md, claude-md, context-engineering, llmops, coding-agents, custo, qualidade, paper]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/agents-md-vale-a-pena-paper-zurique.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-06-01
---

# agents.md e CLAUDE.md Ainda Valem a Pena? O que o Paper de Zurique Realmente Diz

## TL;DR

Paper da Universidade de Zurique compara repositórios com e sem arquivos de contexto para agentes. Resultado superficial: arquivo gerado por LLM = -3% de sucesso, +20% de custo; gerado por humano = +4% de sucesso, +19% de custo. O argumento central: o paper mediu apenas **"testes passaram?"** — e não avaliou qualidade, segurança, design patterns, ou adesão às instruções. Conclusão prática: manter o arquivo, mas mantê-lo **enxuto e linkado**.

---

## Metodologia do Paper (Universidade de Zurique)

1. Repositórios Python públicos do GitHub (ex.: Ansible)
2. Pull requests convertidos em issues
3. Três condições testadas:
   - Sem arquivo de contexto
   - Arquivo gerado por LLM
   - Arquivo gerado por humano *(assumido — pode ter sido LLM também: furo metodológico)*
4. Métricas: taxa de sucesso (testes passando), custo, número de iterações

---

## Resultados Numéricos

| Condição | Taxa de sucesso (vs. sem arquivo) | Custo |
|---|---|---|
| Sem arquivo | baseline | baseline |
| Arquivo gerado por LLM | **−3%** | **+20%** |
| Arquivo gerado por humano | **+4%** | **+19%** |

O aumento de custo é **esperado e explicável**: mais contexto → o agente precisa processar mais tokens, seguir mais regras, buscar mais arquivos. Não é um bug — é a consequência de dar mais informação.

---

## Claims Principais

### Claim 1 — O paper mediu a coisa errada

**Evidência:** A métrica era exclusivamente "os testes passaram?" O paper **não avaliou**:
- Qualidade da implementação
- Segurança do código
- Uso de design patterns
- Adesão às instruções do arquivo de contexto
- Decisões arquiteturais

**Implicação:** Um agente que deletou os testes para "fazer o código passar" seria contado como sucesso nessa métrica.

**Confiança:** Alta — o próprio paper declara as limitações explicitamente.

### Claim 2 — Sem arquivo, alucinação aumenta

**Evidência:** O paper observa que quando há arquivo de contexto, os agentes tipicamente seguem as regras e guidelines presentes. Sem arquivo, o agente não tem referência de convenções — toma decisões arbitrárias.

Experiência empírica do autor: ao remover o `agents.md` de projetos com convenções próprias, o agente "simplesmente alucinou total — começou a implementar as coisas nada a ver".

**Confiança:** Alta (papel + validação empírica).

### Claim 3 — A estratégia certa é enxuto + links

**Evidência:** Cada instrução no arquivo de contexto tem custo real. Instruções desnecessárias aumentam custo sem agregar valor. A solução é manter apenas o mínimo absolutamente necessário no arquivo principal e linkar para arquivos específicos carregados sob demanda.

```
agents.md / CLAUDE.md
    ├── Base mínima (o absolutamente necessário)
    ├── → api-standards.md       (linkado, carregado sob demanda)
    ├── → testing-conventions.md (linkado, carregado sob demanda)
    └── Correções de tooling (adicionadas quando o agente alucina)
```

**Confiança:** Alta — estratégia validada empiricamente pelo autor.

---

## Furo Metodológico

O paper assume que arquivos de contexto já presentes nos repositórios foram escritos por humanos. Porém, esses arquivos podem ter sido gerados por LLMs. Isso compromete a distinção entre as categorias "humano" e "LLM" — reconhecido pelos próprios autores como limitação.

---

## Entidades

- [[wiki/entities/valdemar-neto]] — autor do vídeo; cofundador da Tech Leads Club

---

## Conceitos Tocados

- [[wiki/concepts/claude-md]] — estratégia de arquivo enxuto com links; evidência empírica de valor
- [[wiki/concepts/instruction-budget]] — dado empírico: custo cresce com tamanho do arquivo de contexto
- [[wiki/concepts/llmops]] — gestão de custo de arquivos de contexto como preocupação de LLMOps
- [[wiki/concepts/harness-de-qualidade]] — sem arquivo de contexto, agente ignora padrões de qualidade do projeto

---

## Questões em Aberto

1. Existe algum paper que avalie qualidade de código (segurança, design, testabilidade) em vez de apenas taxa de sucesso em testes?
2. Qual o tamanho ideal de um `agents.md` em termos de tokens/instruções antes de o custo superar o benefício?
3. Como estruturar a hierarquia de links — quantos níveis de arquivos linkados são razoáveis antes de o agente perder o fio?
