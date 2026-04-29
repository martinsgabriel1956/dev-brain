---
type: concept
title: "Abstraction Bloat"
aliases: ["abstraction bloat", "over-engineering ia", "complexidade gerada por agente"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 3
tags: [ia, agentes, arquitetura, over-engineering, qualidade, tokens]
skill: tech-mentor-ai
status: stable
---

# Abstraction Bloat

Fenômeno documentado por Addy Osmani: agentes de IA sem supervisão geram 1000 linhas onde 100 bastariam, criando hierarquias de classes onde uma função resolveria.

## Por Que Acontece

O motivo não é bug — é viés de treinamento. LLMs são treinados com dados superrepresentados por blog posts sobre padrões complexos. Ninguém escreve "fiz um CRUD com 3 arquivos que funciona há 5 anos". Todos escrevem sobre Event Sourcing hexagonal com Saga pattern.

Quando você pergunta "como estruturar esse serviço?", a IA responde com a **média ponderada da internet de tech** — e essa média é enviesada para o complexo.

## O Sinal Diagnóstico

> "Couldn't you just...?" The response is always "Of course!" followed by immediate simplification.

Se o agente simplifica imediatamente ao ser questionado, a complexidade nunca foi necessária. Ele estava otimizando para parecer abrangente, não para manutenibilidade.

## Efeito no Custo com IA

Abstraction bloat cria um loop de custo:
1. Agente gera arquitetura complexa desnecessária
2. Codebase cresce em número de arquivos e indireções
3. Próximas features consumem mais tokens de contexto
4. Agente tem maior chance de perder dependências (ver [[concepts/navigation-paradox]])
5. Custo por feature sobe em tokens, revisão e bugs

## Como Mitigar

- **Supervisão ativa:** questione toda abstração que você não teria criado sem a IA
- **Prompts explícitos:** "implemente de forma simples e direta, sem abstrações preventivas"
- **YAGNI como filtro:** ver [[concepts/yagni]]
- **Leia o código gerado:** não confie só nos testes passando

## Key Sources

- [[sources/addy-osmani-80-problem-agentic-coding]]
- [[sources/clean-architecture-ia-custo-real]]
- [[sources/super-productivity-ai-architecture-guide]]
