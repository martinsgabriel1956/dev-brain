---
type: concept
title: "Navigation Paradox"
aliases: ["navigation paradox", "paradoxo de navegação", "dependência escondida agente"]
date_created: 2026-04-23
date_updated: 2026-08-04
source_count: 2
tags: [ia, agentes, arquitetura, dependencias, tokens, benchmark, pesquisa]
skill: tech-mentor-ai
status: stable
---

# Navigation Paradox

Conceito do paper de Tarakanath Paipuru (fev 2026): janelas de contexto maiores não eliminam a necessidade de navegação estrutural em codebases com arquitetura complexa — elas apenas deslocam o modo de falha.

## O Paradoxo

**Antes:** falha por "não cabe no contexto".
**Com contexto ilimitado:** falha por "não estava saliente o suficiente para o modelo notar".

O agente lê o codebase e simplesmente não descobre que um arquivo é relevante — especialmente quando a ligação entre arquivos existe apenas em runtime (DI containers, registros de IoC), não no código-fonte.

## Os Números (paper, 258 trials, Claude Code)

| Condição | Deps Semânticas (G1) | Deps Estruturais (G2) | Deps Escondidas (G3) |
|---|---|---|---|
| Vanilla | 90.0% | 79.7% | **76.2%** |
| BM25 retrieval | 100.0% | 85.1% | 78.2% |
| Graph navigation | 88.9% | 76.4% | **99.4%** |

**Em G3 (dependências escondidas via DI/inversão), o agente perde 1 em cada 4 arquivos críticos.**

## Por Que Dependency Injection é o Caso Mais Crítico

```python
# O agente lê UserService e não encontra referência a PostgresUserRepo
# A ligação só existe no container de DI em outro arquivo
container.register(UserRepository, PostgresUserRepository)
```

Static AST analysis não consegue rastrear vínculos criados por DI containers. Keyword search (BM25) também não — porque não há keyword ligando os dois arquivos.

## O Problema da Ferramenta Ignorada

Mesmo com uma ferramenta de navegação de grafos disponível e prompt explícito:
- **58% dos trials:** agente ignorou a ferramenta ("glob + read já me dão 80%")
- **Trials com ferramenta usada:** ACS = 99.5%
- **Trials sem ferramenta (mesmo disponível):** ACS = 80.2% — idêntico ao Vanilla

## Implicações para Design

- Cada arquivo a mais é token a mais + chance de dependência escondida
- Arquitetura horizontal (domain/application/infrastructure) obriga 7–13 arquivos para features que em Vertical Slice seriam 1–3
- Bounded Context bem definido limita o escopo → menos tokens, menos erros

## Relacionado

- [[concepts/abstraction-bloat]] — mais abstrações = mais dependências potencialmente escondidas
- [[concepts/yagni]] — previne a criação de dependências desnecessárias
- [[concepts/dependency-injection]] — o mecanismo que cria G3 dependencies
- [[sources/navigation-paradox-2026]] — o paper completo

## Confirmação Independente: Estrutura em Camadas vs. Vertical Slice

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] chega à mesma conclusão central por um ângulo diferente, citando o Navigation Paradox como "segundo paper" que mediu o custo de estrutura em camadas do jeito mais direto possível: uma estrutura horizontal em camadas (domain/application/infrastructure) obriga o agente a atravessar várias camadas e vários arquivos (mappers, DTOs) para implementar uma única funcionalidade, e o agente provavelmente deixa arquivos para trás nesse processo. A fonte reforça [[wiki/concepts/vertical-slice-architecture]] como a estrutura mais óbvia — tanto para agente quanto para humano — citando o padrão *package by feature* do Go como exemplo concreto de adoção crescente.

## Key Sources

- [[sources/navigation-paradox-2026]]
- [[sources/clean-architecture-ia-custo-real]]
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — confirmação independente do custo de estrutura em camadas, com vertical slice/package-by-feature como alternativa recomendada
