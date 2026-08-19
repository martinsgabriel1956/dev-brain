---
type: concept
title: "Níveis de Adoção de IA — L0 a L4"
aliases: ["L0 L1 L2 L3 L4", "escada de maturidade IA dev", "niveis ia branas nauke"]
date_created: 2026-06-02
date_updated: 2026-08-19
source_count: 4
tags: [ia-para-devs, adocao, maturidade, produtividade, spec-driven]
skill: tech-mentor-ai
status: stable
---

# Níveis de Adoção de IA — L0 a L4

Framework criado por Rodrigo Branas e Pedro Nauke para descrever a progressão de maturidade no uso de IA por desenvolvedores. Complementa (e é distinto de) a [[wiki/concepts/escala-maturidade-ia-dev|escala de 7 níveis]] de Steve (ex-Google/Amazon) — esta aqui é mais focada no processo de codificação e no nível de autonomia delegada.

## Os Níveis

### L0 — Hater
Recusa usar IA. Geralmente formado por experiências ruins com modelos antigos (Copilot de 2 anos atrás) ou por medo de perda de controle. *Importante*: todo hater no fundo é um copy-paste em potencial.

### L1 — Copy-paste
Copia respostas do ChatGPT/Claude e cola no editor. Usa IA como buscador avançado. Não dá autonomia ao modelo.

### L2 — Babysitting
Usa Agent Mode mas aprova cada etapa, cada linha de código. Gera 100% do código via IA mas ainda prende o modelo no vai-e-vem contínuo de prompts curtos. **Onde a maioria dos devs está (2026).**

Problema: tempo de idle enorme. O dev fica de braço cruzado esperando cada resposta antes de dar o próximo passo. Não consegue paralelizar.

### L3 — Gerente (objetivo do curso)
Foca no planejamento e definição de objetivos (spec-driven), delega a execução para a IA, e acompanha o resultado. Paraleliza múltiplas tarefas via [[wiki/concepts/worktree-paralelismo|worktrees]].

Características:
- Faz spec antes de executar
- Roda tasks em paralelo (múltiplas worktrees simultâneas)
- Revisa o resultado final, não cada linha
- Usa pipelines de QA, testes, E2E para validar

### L4 — Fábrica
Desenvolvimento totalmente autônomo — IA detecta issues, cria ambiente, corrige bug, abre PR. Exemplo: pipeline no Slack onde um bug aberto dispara automaticamente uma VM no Devin que resolve e abre PR.

Requer:
- Ferramentas caras (Devin, Open Hands, sandboxes isoladas)
- Infraestrutura de CI/CD madura
- Playbooks detalhados

## Armadilha do L2 com 100% de Código Gerado

Ter 100% do código gerado por IA não significa estar no L3. No L2, a autonomia delegada pode ser só 30% mesmo com 100% de geração. A diferença está em **se você paraleliza tarefas e usa planejamento estruturado**.

## Relação com Custo

| Nível | Autonomia | Paralelismo | Custo de ferramenta |
|---|---|---|---|
| L0–L1 | <10% | Nenhum | $0 |
| L2 | 30–50% | Nenhum | $20–100/mês |
| L3 | 70–90% | Alto | $100–200/mês |
| L4 | ~100% | Total | $15k+/mês (Devin) |

## L3 na Prática: o Product Engineer

Dados de campo do Vale do Silício (2026) descrevem o L3 em operação como o [[product-engineer]]. O tech lead do Databricks usa os intervalos entre reuniões para disparar 2–3 agents e revisa os PRs resultantes em blocos concentrados — não linha a linha. A engenheira do Cursor dispara ~5 agents simultâneos por feature com critério claro de granularidade: "a menor quantidade de trabalho mais a maior quantidade que um agente consegue fazer sem esbarrar em outro agente." O paralelismo real no trabalho diário é o marcador que separa L2 de L3.

## Adesão Não é o Mesmo que Nível: 98,5% Usam IA, Maioria Ainda em L2

Dado de mercado de [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] (pesquisa salarial do [[wiki/entities/codigo-fonte-tv]]): 83% dos devs já usavam IA para programar em 2024, saltando para 98,5% em 2026. Esse número mede **adesão** (usa ou não usa IA), não nível de maturidade — é consistente com, e não contradiz, a leitura desta página de que a maioria dos devs está em L2 mesmo gerando 100% do código via IA (ver "Armadilha do L2" acima). Quase todo mundo já usa IA; a diferença de nível está em *como*.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/escala-niveis-uso-ia-engenheiros]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
- [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] — adesão de devs a IA para programar: 83% (2024) → 98,5% (2026), pesquisa salarial do Código Fonte TV
