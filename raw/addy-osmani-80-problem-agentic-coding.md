---
date: 2026-04-23
tags: [ia, agentes, arquitetura, abstraction-bloat, comprehension-debt, qualidade, ownership]
skill: tech-mentor-ai
level: sênior
source_url: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
author: Addy Osmani (Google)
date_published: 2026-01-28
---

# The 80% Problem in Agentic Coding — Addy Osmani (2026)

## TL;DR

O problema não é mais "a IA chega a 70% e para". O problema mudou: a IA chega mais longe, mas os erros que ela comete são diferentes — e mais insidiosos. A dívida cognitiva (comprehension debt) acumulada durante o desenvolvimento agentic é o novo risco principal.

## O Contexto

Andrej Karpathy (jan 2026): *"I rapidly went from 80% manual coding to 80% agent coding. I really am mostly programming in English now."*

Boris Cherney (criador do Claude Code): *"Praticamente 100% do nosso código é escrito pelo Claude Code + Opus 4.5. Eu pessoalmente shipei 22 PRs ontem e 27 antes de ontem, cada um 100% escrito pelo Claude."*

Pesquisa Sonar: **44% dos devs escrevem menos de 10% do código manualmente.** Outros 26% estão na faixa de 10–50% manual. O threshold foi cruzado.

**Mas:** os problemas não desapareceram — eles se deslocaram. Alguns ficaram piores.

## Os Novos Tipos de Erro

Os erros mudaram de **bugs de sintaxe** para **falhas conceituais** — o tipo que um desenvolvedor júnior descuidado cometeria sob pressão de tempo.

### 1. Abstraction Bloat

> "Dado free rein, agentes complicam sem parar. Eles scaffoldam 1.000 linhas onde 100 bastariam, criando hierarquias de classes onde uma função resolveria."

O agente está otimizando para parecer abrangente, não para manutenibilidade. Quando você diz "Não poderia simplificar isso?", a resposta é sempre "Claro!" seguida de simplificação imediata — o que significa que a complexidade não era necessária desde o início.

**Por quê?** Os LLMs são treinados com dados enviesados para o complexo. Ninguém escreve artigos sobre "fiz um CRUD com 3 arquivos que funciona há 5 anos". As pessoas escrevem sobre Event Sourcing hexagonal.

### 2. Assumption Propagation

O modelo entende algo errado cedo e constrói a feature inteira em cima de premissas erradas. Você não percebe até estar 5 PRs adiante com a arquitetura cimentada.

### 3. Dead Code Accumulation

Agentes deixam código morto: fallbacks que nunca ativam, feature flags que nunca mudam, abstrações que nunca têm segunda implementação.

## Comprehension Debt — A Nova Dívida Técnica

> Termo cunhado por Jeremy Twei. É a dívida que se acumula quando você revisa e aprova código que entende superficialmente.

**O mecanismo:** geração de código (escrever) e discriminação de código (ler criticamente) são capacidades cognitivas diferentes. Você pode revisar código competentemente mesmo depois que sua capacidade de escrevê-lo do zero atrofiou. Mas existe um threshold onde "revisão" vira "rubber stamping".

O agente não se cansa. Ele sprinta através de implementação após implementação com confiança inabalável. O código parece plausível. Os testes passam (ou parecem passar). Você está sob pressão para shipar. Você segue em frente.

**Com o tempo, você entende menos do seu próprio codebase.**

### O Loop de Vício

> "O agente implementou uma feature incrível e errou talvez 10% da coisa, e você pensa 'eu consigo arrumar isso com mais 5 minutos de prompt'. Isso foi 5 horas atrás." — Yoko Li

Você está sempre *quase* lá. O psychological hook é real.

## Verificação: O Gargalo Atual

Pesquisa Sonar (jan 2026): **apenas 48% dos devs checam consistentemente o código gerado por IA antes de commitar.**

O novo gargalo não é geração — é verificação. E verificação requer compreensão. O comprehension debt erode exatamente essa capacidade.

## O Que Ainda Funciona

O artigo não é pessimista — é calibrado. O que continua funcionando com agentes:

- **Greenfield/projetos pessoais:** a IA performa muito bem
- **Tarefas mecânicas bem-especificadas:** excelente
- **Refactoring com escopo claro:** ótimo

O que degrada:
- **Codebases grandes e existentes:** a IA tem que ler mais para entender o contexto, aumenta a chance de assumption propagation
- **Features que tocam muitos domínios:** cada domínio adicional é mais contexto consumido e mais chance de inventar relações

## Implicações Práticas

1. **Supervise ativamente a complexidade gerada** — questione toda abstração que você não teria criado sem a IA
2. **Leia o código, não só aprove** — comprehension debt se acumula silenciosamente
3. **Prompts específicos produzem código mais simples** — "implemente de forma simples e direta" é instrução válida
4. **A IA responde bem ao pushback** — "não poderia resolver com menos código?" funciona, o que prova que a complexidade não era necessária

## Conceitos Relacionados

- [[navigation-paradox-2026]] — custo quantificado das abstrações para agentes
- [[concepts/divida-cognitiva]] — comprehension debt é a versão técnica da dívida cognitiva
- [[sources/clean-architecture-ia-custo-real]] — caso prático com o mesmo diagnóstico
- [[super-productivity-ai-architecture-guide]] — abstraction illusion complementar

---

*Fonte: addyo.substack.com/p/the-80-problem-in-agentic-coding · Addy Osmani · 28 jan 2026*
