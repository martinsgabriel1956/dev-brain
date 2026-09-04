---
type: concept
title: "RPI Workflow"
aliases: ["research plan implement", "RPI", "research-plan-implement"]
date_created: 2026-05-04
date_updated: 2026-09-03
source_count: 5
tags: [coding-agents, context-engineering, workflow, ai-engineering]
skill: tech-mentor-ai
status: stable
---

# RPI Workflow

Framework de três fases para trabalhar com coding agents em codebases reais. Objetivo central: manter o agente na [[concepts/dumb-zone|smart zone]] da context window durante todo o trabalho e preservar o [[concepts/mental-alignment]] do dev sobre o que está sendo construído.

## As Três Fases

### Research
- O agente **apenas observa** — sem modificar nada
- Coleta quais arquivos existem, como o código está organizado, dependências
- Output: documento com arquivos exatos e números de linha relevantes ao problema
- Regra crítica: o dev precisa ler o suficiente para ter um modelo mental do que o agente encontrou — não linha por linha, mas o suficiente para detectar se a direção está errada

### Plan
- Recebe o output do research como input
- Produz os passos exatos de implementação, com snippets de código reais
- Inclui como testar após cada mudança
- Tamanho ideal: revisável em ~10 minutos — o suficiente para confiança, não tanto que dobre o trabalho

### Implement
- Executa o plano mantendo a context window baixa
- Segue o [[concepts/plano-vertical]]: cada entrega é testável antes de continuar
- Dev acompanha o que está sendo gerado — sem deixar o agente ir longe demais sem revisão

## Por Que Funciona

LLMs são stateless. A única forma de obter melhor performance é colocar tokens melhores. O RPI estrutura o trabalho para que cada fase receba apenas os tokens que ela precisa, sem ruído de fases anteriores.

A separação research/plan evita [[concepts/separacao-de-contextos|contaminação de contexto]] — o modelo não toma decisões de arquitetura escondidas numa suposta fase de observação.

## Anti-patterns

- **Plano de 1.000 linhas** — dobra o trabalho sem garantia de que o código vai bater
- **Não ler o código** durante o research — você perde a capacidade de detectar problemas cedo
- **Mesma sessão para research e plan** — o modelo mistura o que observou com o que acha que deveria construir
- **Plano horizontal** (banco todo → serviços todos → API toda) — nada é testável no meio

## Relação com Spec-Driven Development

O RPI pertence à mesma família do Spec-Driven Development, mas com foco explícito em **context engineering** em vez de especificação formal. A distinção importa porque "spec-driven dev" sofreu semantic diffusion — o termo virou vago. O que importa não é o nome, mas os princípios: compaction, smart zone, human-in-the-loop nos pontos de maior alavancagem.

## Memória de Longo Prazo para Refatorações Grandes

Quando a mudança é grande demais para um único plano (ex.: refatoração de 13+ serviços para DDD tático), o plano se tornaria enorme e geraria um PR irrevisuável. A solução:

1. Salvar o output do research em um arquivo `.md` (memória de longo prazo)
2. Revisar e validar manualmente — compartilhar com o time
3. Quebrar em subplanos por fase de implementação
4. Executar cada fase em uma sessão separada com contexto baixo
5. Um PR por fase → revisão humana → merge

Ver [[memoria-de-longo-prazo-ia]] para o padrão detalhado.

## Enriquecimento com Progressive Disclosure

O RPI funciona melhor quando o codebase usa [[progressive-disclosure-ia]]: arquivos de contexto organizados por diretório/responsabilidade. Na fase de implement, o agente carrega apenas as guidelines do módulo que está sendo alterado — não de todo o projeto.

## Confirmação de Campo: Heurística de ~200k Tokens

Independentemente da fonte original, [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] confirma a mesma heurística prática — manter o uso da janela em torno de ~200k tokens mesmo quando o modelo suporta até 1M — e amarra explicitamente RPI ao Spec-Driven Development como resposta ao mesmo problema (quanto mais janela ocupada, maior a chance de alucinação), com um exemplo concreto de mudança em ~90 arquivos conduzida sem estourar essa faixa.

## Subagentes na Fase de Research Sempre Compensam

[[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] reforça, dentro de um modelo mental de 4 critérios para quando usar subagentes, que a fase de **Research** é o caso mais claro: o agente principal passa um prompt dizendo o que quer de volta, o subagente varre o codebase e retorna só o necessário — preserva a janela do principal e não a polui. Diferente da fase de Implement (onde a granularidade de subagentes importa muito e pode piorar o resultado se for excessiva — ver [[wiki/concepts/subagentes]]), a fase de Research não teve nenhum cenário testado onde usar subagente saiu pior que não usar.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
- [[wiki/sources/context-engineering-codebases-grandes-rpi]] — sub-planos para refatorações grandes; memória de longo prazo; progressive disclosure na prática
- [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — heurística de ~200k tokens; RPI e SDD como resposta ao mesmo problema; exemplo de campo com ~90 arquivos
- [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] — fase de Research como caso claro onde subagente sempre compensa (sem cenário testado em que piorou o resultado)
