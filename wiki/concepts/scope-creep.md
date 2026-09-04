---
type: concept
title: "Scope Creep"
aliases: ["escopo crescente", "feature creep", "scope inflation"]
date_created: 2026-04-29
date_updated: 2026-09-04
source_count: 2
tags: [projetos, produtividade, mvp, planejamento, carreira]
skill: tech-mentor-leadership
status: stable
---

# Scope Creep

Expansão gradual e não planejada do escopo de um projeto além dos objetivos originais. Em side projects, ocorre antes de ter um único usuário — funcionalidades são adicionadas por entusiasmo, não por demanda.

## Padrão Clássico em Side Projects

```
Blog simples
  → auth para comentários
  → dark mode + light mode
  → CMS
  → notificações por email
  → assistente de escrita com IA
  → app all-in-one de produtividade
  → abandono
```

## Raiz do Problema

- **[[concepts/planning-fallacy]]**: subestimar complexidade de cada adição
- **[[concepts/dopamina-e-projetos]]**: cada nova feature traz dopamina de ideação
- Ausência de definição clara de "pronto" permite expansão ilimitada

## Consequência

Nunca há entrega porque o projeto nunca está "completo". O MVP que deveria existir fica enterrado sob camadas de funcionalidades não essenciais.

## Scope Creep em Serviços Para Cliente Externo

Em [[wiki/sources/3-fatores-nao-tecnicos-para-entregar-projetos-de-ia-em-empresas]], o mesmo fenômeno aparece fora do contexto de side project solo: em projetos de IA vendidos a um cliente, o escopo cresce porque o próprio cliente (ou um stakeholder que entra depois da proposta original) descobre o que realmente quer só ao ver o produto funcionando — não por entusiasmo do desenvolvedor. A mitigação também muda: em vez de disciplina pessoal, a ferramenta é negociação explícita de trade-off (estender prazo vs. manter prazo e tratar o pedido como escopo futuro com custo adicional). Ver [[wiki/concepts/gerenciamento-de-expectativa-em-servicos-de-ia]].

## Mitigação

- **[[concepts/mvp]]**: definir o menor conjunto de funcionalidades que valida a ideia
- **"Will it wait?"**: para cada feature nova, perguntar "isso pode esperar o MVP?"
- Lista separada de "future scope" — documenta sem bloquear o presente

## Key Sources

- [[sources/por-que-devs-nao-terminam-projetos]]
- [[wiki/sources/3-fatores-nao-tecnicos-para-entregar-projetos-de-ia-em-empresas]] — mesma dinâmica em contexto de cliente externo pagante, não side project
