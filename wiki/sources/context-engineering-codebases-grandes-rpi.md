---
type: source
title: "Context Engineering para Codebases Grandes — Progressive Disclosure, On-Demand Loading e o Workflow RPI"
aliases: []
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 0
tags: [context-engineering, rpi-workflow, coding-agents, progressive-disclosure, on-demand-loading, memoria-longo-prazo, subplano, codebase, llmops]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/context-engineering-codebases-grandes-rpi.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-06-01
---

# Context Engineering para Codebases Grandes — Progressive Disclosure, On-Demand Loading e o Workflow RPI

## TL;DR

A diferença entre ganhar ou perder 10 horas com IA está na gestão do contexto. Este vídeo apresenta três técnicas complementares ao [[rpi-workflow]]: **progressive disclosure** (arquivos de contexto por diretório/responsabilidade), **on-demand loading** (Cursor Rules / Claude Skills com gatilhos), e **memória de longo prazo** (planos salvos como markdown para refatorações grandes). O princípio central: manter a [[dumb-zone|smart zone]] em cada fase e nunca misturar research com implement na mesma sessão.

---

## Argumento Central

LLMs são stateless — toda sessão começa do zero. Para codebases grandes, passar o contexto inteiro é contraproducente: acima de ~60% da context window entra na **dumb zone** onde alucinação aumenta. A solução não é um prompt melhor — é entregar tokens melhores em cada fase.

---

## Claims Principais

### Claim 1 — Código modular reduz contexto necessário

**Evidência:** Um MVC com god class força o agente a carregar dezenas de serviços sem relação para entender qualquer mudança. Um codebase modular por domínio (billing, identity, content) permite que o agente carregue só o módulo relevante.

**Implicação prática:** antes de usar IA em escala, avaliar a estrutura do código. Código não modular não é bloqueio, mas exige guidelines mais fortes para compensar.

**Confiança:** Alta — princípio de [[codebase-legibilidade-ia]].

### Claim 2 — Progressive Disclosure: arquivos de contexto por diretório

**Evidência:** Em vez de um `CLAUDE.md` monolítico na raiz, distribuir guidelines por diretório e responsabilidade. O agente carrega o arquivo do módulo que está sendo alterado — não os de todos os módulos.

```
/billing/GUIDELINES.md      ← carregado quando o agente modifica billing
/identity/GUIDELINES.md     ← carregado quando o agente modifica identity
/CLAUDE.md                  ← base mínima sempre presente
```

**Confiança:** Alta — demonstrado com codebase de exemplo no vídeo.

### Claim 3 — On-Demand Loading: Cursor Rules e Claude Skills

**Evidência:** Cursor Rules permitem configurar quando cada arquivo de contexto é carregado:

```yaml
# architecture.mdc — sempre ativo
alwaysApply: true

# ddd-strategic.mdc — carregado quando o agente identifica necessidade
alwaysApply: false
trigger: "criando módulos / dúvidas sobre design patterns"

# domain-identification.mdc — só quando explicitamente pedido
alwaysApply: false
trigger: "quando alguém pedir 'identify domains' no chat"
```

Claude Skills funcionam da mesma forma. agents.md padrão é menos flexível — sem gatilhos configuráveis.

**Confiança:** Alta — demonstrado com configuração real no vídeo.

### Claim 4 — Memória de Longo Prazo para Refatorações Grandes

**Evidência:** Quando uma refatoração é grande demais para um único plano, salvar o output do research em um arquivo `.md` permite:
1. Revisão humana e validação pelo time antes de executar
2. Quebrar em subplanos por fase de implementação
3. Cada fase executada em sessão separada com contexto baixo

Exemplo: refatoração de `SubscriptionService` (13+ serviços) para DDD tático — sem memória de longo prazo, o plano seria enorme demais. Com ela, dividida em 6 PRs revisáveis.

**Confiança:** Alta — demonstrado com plano real (`refactoring-change-plan-use-case-to-tactical-ddd.md`).

### Claim 5 — Sub-agentes: tarefas específicas, não camadas

**Evidência:** O anti-padrão é criar sub-agente de front-end, sub-agente de back-end. O padrão correto é sub-agentes para tarefas específicas e bem definidas:

```
✅ Sub-agente: análise de complexidade
✅ Sub-agente: "quais arquivos não seguem as guidelines?"
✅ Sub-agente: validador de arquitetura
❌ Sub-agente de front-end (gasto de tokens sem necessidade)
```

O agente pai recebe só o output (alguns tokens) em vez de acumular toda a exploração.

**Confiança:** Alta — alinhado com [[separacao-de-contextos]].

---

## Entidades

- [[wiki/entities/valdemar-neto]] — autor; segunda fonte deste canal no wiki

---

## Conceitos Tocados

- [[wiki/concepts/rpi-workflow]] — prática expandida com sub-planos e memória de longo prazo
- [[wiki/concepts/progressive-disclosure-ia]] — novo conceito; central nesta fonte
- [[wiki/concepts/memoria-de-longo-prazo-ia]] — novo conceito; central nesta fonte
- [[wiki/concepts/separacao-de-contextos]] — sub-agentes confirmados como implementação técnica; enriched
- [[wiki/concepts/codebase-legibilidade-ia]] — MVC god class como anti-padrão para IA; enriched
- [[wiki/concepts/claude-md]] — on-demand loading com Cursor Rules / Claude Skills; enriched
- [[wiki/concepts/instruction-budget]] — smart zone 40% / dumb zone 60% confirmados empiricamente

---

## Questões em Aberto

1. Qual o limite de profundidade de links nos arquivos de contexto antes de on-demand loading perder efetividade?
2. Como coordenar sub-planos executados por múltiplos devs em paralelo — risco de conflito de estado entre fases?
3. Claude Skills estão recém lançadas — são tão flexíveis quanto Cursor Rules em termos de gatilhos configuráveis?
