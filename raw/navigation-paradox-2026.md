---
date: 2026-04-23
tags: [ia, agentes, arquitetura, clean-architecture, dependencias, contexto, tokens, pesquisa, mcp]
skill: tech-mentor-ai
level: avançado
source_url: https://arxiv.org/html/2602.20048v1
author: Tarakanath Paipuru
date_published: 2026-02
---

# The Navigation Paradox in Large-Context Agentic Coding (2026)

## TL;DR

Janelas de contexto maiores não eliminam o problema de navegação estrutural em codebases com arquitetura complexa — elas apenas deslocam o modo de falha. O Navigation Paradox: quando arquivos críticos estão semanticamente distantes, o modelo simplesmente não os encontra, mesmo com contexto ilimitado.

## Hipótese Central

A suposição tácita da indústria é que janelas de contexto de milhões de tokens dissolvem os gargalos de retrieval. Os autores contestam: **contexto maior não resolve dependências escondidas — muda o tipo de falha de "não cabe no contexto" para "não estava saliente o suficiente para o modelo notar".**

## Setup Experimental

- **Benchmark:** 30 tarefas no FastAPI RealWorld example app
- **Agente testado:** Claude Code
- **258 trials** completados (de 270 planejados; 12 falharam por esgotamento de crédito)
- **Ferramenta:** CodeCompass — MCP server que expõe grafos estáticos de dependência (edges: IMPORTS, INHERITS, INSTANTIATES via AST)

### Taxonomia de Tarefas

| Grupo | Tipo | Descrição |
|---|---|---|
| G1 | Semântico | Dependências encontráveis por busca de keywords |
| G2 | Estrutural | Alcançáveis via import chains |
| G3 | Escondido | Dependências arquiteturais não-semânticas, invisíveis para keyword search e vector retrieval |

G3 é o grupo relevante para Clean Architecture: DI containers, inversão de dependência, registros em runtime.

## Resultados

### ACS (Architectural Coverage Score) por Condição e Grupo

| Condição | G1 ACS | G2 ACS | G3 ACS |
|---|---|---|---|
| A — Vanilla Claude Code | 90.0% | 79.7% | 76.2% |
| B — BM25 (keyword retrieval) | 100.0% | 85.1% | 78.2% |
| C — CodeCompass (graph nav) | 88.9% | 76.4% | **99.4%** |

**Interpretação:**
- BM25 domina em G1 (semântico) — 100% com variância zero
- BM25 não ajuda em G3 — 78.2% vs 76.2% Vanilla, praticamente idêntico
- Graph navigation (CodeCompass) resolve G3: **+23.2 pontos percentuais** sobre ambas as baselines
- Em G2 (estrutural), CodeCompass *regride* — pior do que Vanilla (76.4% vs 79.7%)

### O Dado Mais Importante: O Agente Ignora a Ferramenta

Mesmo quando o CodeCompass estava disponível e o prompt instruía explicitamente a usá-lo:

- **58% dos trials: agente ignorou a ferramenta** e aplicou heurística própria ("glob + read já me dão 80%, não vale usar o MCP")
- **42% dos trials com tool invocada:** ACS médio = **99.5%**
- **58% dos trials sem tool (mesmo disponível):** ACS = **80.2%** — indistinguível da baseline Vanilla

**Conclusão:** a ferramenta funciona quando usada. O problema é que o agente decide racionalmente não usá-la na maioria das vezes.

### Adoção por Grupo de Tarefa

| Grupo | Adoção da Graph Tool |
|---|---|
| G1 (semântico) | 22.2% — corretamente ignorado |
| G2 (estrutural) | **0%** — nunca usado, mesmo sendo o caso de uso principal |
| G3 (escondido) | 100% — usado após melhoria no prompt |

G2 = zero adoção é o achado mais surpreendente: as tarefas que a ferramenta foi projetada para resolver (dependências via import chains) foram exatamente onde o agente nunca a invocou.

## Por Que Dependency Injection é o Caso Mais Crítico

DI containers criam conexões entre arquivos que **não existem no código-fonte** — existem no runtime. Exemplo:

```python
# O agente lê UserRepository e não encontra referência a PostgresUserRepository
# A ligação só existe no container de DI configurado em outro arquivo
container.register(UserRepository, PostgresUserRepository)
```

Static AST analysis (o que o CodeCompass faz) resolve isso porque rastreia INSTANTIATES edges. Mas sem essa ferramenta, ou sem o agente usar a ferramenta, o arquivo é invisível.

**Resultado prático:** em projetos com Clean Architecture ritualística, o Claude Code perde um arquivo em cada quatro arquivos críticos — silenciosamente.

## Implicações para Arquitetura

1. **Mais arquivos = mais tokens + mais chance de dependência escondida** — você paga duplamente
2. **Arquitetura horizontal (domain/application/infrastructure)** força abertura de 7–13 arquivos para uma feature que em Vertical Slice seria 1–3
3. **Cada indireção sem propósito semântico** é ruído competindo com a lógica que importa
4. **Contexto delimitado por domínio** (pastas por bounded context) reduz o espaço de busca do agente — otimização de token, não só clareza de modelo

## Limitações do Paper

- Benchmark em um único projeto (FastAPI RealWorld) — generalização limitada
- Apenas Claude Code testado — comportamento pode diferir em outros agentes
- G2 regredindo com CodeCompass é não-explicado e precisa de investigação

## Conceitos Relacionados

- [[concepts/shared-sdk]] — SDK bem separado reduz dependências escondidas
- [[sources/clean-architecture]] — o target da crítica
- [[sources/addy-osmani-80-problem-agentic-coding]] — abstraction bloat complementar
- [[sources/mcp]] — Model Context Protocol, o protocolo do CodeCompass

---

*Fonte: arxiv.org/html/2602.20048v1 · Tarakanath Paipuru · Fevereiro 2026*
