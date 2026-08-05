---
type: concept
title: "Vertical Slice Architecture"
aliases: ["vertical slice", "feature-first architecture", "slice por feature"]
date_created: 2026-04-23
date_updated: 2026-08-04
source_count: 5
tags: [arquitetura, modularidade, feature-first, agentes, tokens, frontend]
skill: tech-mentor-backend
status: stub
---

# Vertical Slice Architecture

Organização de código por *feature* (corte vertical), não por *camada* (corte horizontal). Cada feature contém tudo que precisa: handler, lógica de negócio, acesso a dados.

## Contraste com Clean Architecture Horizontal

**Horizontal (Clean Architecture):**
```
domain/
  user.entity.ts
application/
  create-user.usecase.ts
infrastructure/
  user.repository.ts
presentation/
  user.controller.ts
```
Uma feature toca 4+ arquivos em 4 pastas diferentes.

**Vertical Slice:**
```
features/
  create-user/
    handler.ts        # HTTP + validação
    logic.ts          # regra de negócio
    repository.ts     # acesso a dados
```
Uma feature = uma pasta, 2–3 arquivos.

## Por Que Importa com IA

O Navigation Paradox (ver [[concepts/navigation-paradox]]) mostra que arquitetura horizontal obriga o agente a abrir 7–13 arquivos para uma feature que em Vertical Slice seria 1–3. Cada arquivo a mais é token a mais e chance de perder uma dependência.

Vertical Slice não resolve tudo — shared code (auth, logging, DB client) ainda precisa de uma camada compartilhada. Mas o core de cada feature fica contido.

## Quando Usar

- Times que querem feature independence: um dev trabalha em `create-user/` sem tocar em `list-users/`
- Codebases onde o agente de IA é parte ativa do fluxo de desenvolvimento
- Projetos que precisam de clareza rápida do que pertence a cada feature

## Limitação

Sem discipline, Vertical Slice pode levar a duplicação de lógica entre features. A solução é extrair para `shared/` *depois* do segundo caso — ver [[concepts/yagni]].

## Vertical Slice Dentro de um Módulo (Frontend)

[[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] aplica o mesmo princípio um nível abaixo do módulo, dentro de uma arquitetura [[wiki/concepts/monolito-modular-frontend|modular]]: quando uma funcionalidade dentro de um módulo já nasce mais complexa, o instinto de "por que não desacopla, cria um projeto/microfrontend separado?" deve ser resistido — primeiro isola-se a funcionalidade via vertical slice dentro do próprio módulo, e só se extrai de fato quando a necessidade real de desacoplamento aparecer. É a mesma lógica de extração tardia documentada em [[wiki/concepts/microsservicos]] (monolito modular como ponto de partida, extração só com necessidade real), aplicada à fronteira entre "módulo" e "feature complexa dentro do módulo" em vez de entre "monólito" e "serviço".

**Risco registrado pelo autor:** tratar vertical slice como regra filosófica rígida ("isso deveria ficar dentro do módulo/feature") em vez de ferramenta prática já gerou conflito de time — o critério deve ser "isso facilita", não "isso está no lugar certo segundo a teoria".

## "Package by Feature" do Go Como Exemplo de Adoção Crescente

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] cita o padrão *package by feature* do Go como exemplo concreto de vertical slice ganhando tração fora do contexto original de VSA em .NET, e liga isso diretamente ao [[wiki/concepts/navigation-paradox]]: estrutura horizontal em camadas obriga o agente a atravessar múltiplos arquivos (mappers, DTOs) para uma única funcionalidade, com risco real de deixar arquivos para trás; vertical slice reduz esse custo por ser mais óbvia tanto para agente quanto para humano — mesma conclusão já registrada acima via [[wiki/concepts/monolito-modular-frontend]] e a comparação horizontal-vs-vertical no topo desta página.

## Key Sources

- [[sources/clean-architecture-ia-custo-real]]
- [[sources/erros-workflow-research-plan-implement]] — plano vertical como aplicação do VSA a workflow de agente
- [[sources/context-engineering-avancado-para-coding-agents]] — implementação incremental para manter context window baixa
- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — vertical slice dentro de um módulo frontend como isolamento pré-extração, e o risco de virar regra filosófica rígida em vez de ferramenta prática
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — package by feature do Go como exemplo de adoção crescente, ligado ao custo medido pelo Navigation Paradox
