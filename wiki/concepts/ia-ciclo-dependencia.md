---
type: concept
title: "IA — Ciclo de Dependência"
aliases: ["ia dependencia", "degradacao por ia", "vibe coding dependencia", "ciclo de degradacao"]
date_created: 2026-04-29
date_updated: 2026-07-09
source_count: 2
tags: [ia, carreira, vibe-coding, competencia, fundamentos]
skill: tech-mentor-leadership
status: stable
---

# IA — Ciclo de Dependência

Armadilha sutil do uso de IA para geração de código: quanto menos você entende o que foi gerado, menos consegue avaliar se é bom — o que leva a usar mais IA para compensar, degradando progressivamente a competência técnica.

## O Ciclo

```
usa IA sem entender
     ↓
não avalia qualidade do output
     ↓
aceita código ruim
     ↓
sistema fica frágil
     ↓
usa mais IA pra consertar
     ↓
entende ainda menos
```

## Por Que é Sutil

- Acontece devagar. Não tem um momento de ruptura claro.
- O código *funciona* — a degradação é na capacidade de avaliação, não no output imediato.
- Só se percebe quando não consegue mais resolver nada sem IA.

## Contraponto: Uso Saudável de IA

IA amplifica o que você já sabe. Dev que entende sistemas usa IA para acelerar execução. Dev que não entende usa IA para substituir entendimento — efeitos opostos.

**Checklist de validação antes de aceitar código de IA:**
- [ ] Esse código vai escalar com o crescimento esperado do sistema?
- [ ] Em que condições esse código vai quebrar?
- [ ] Está coerente com a arquitetura e convenções do projeto?
- [ ] Entendo o que ele faz linha a linha?

## Relações

- [[concepts/vibe-coding]] — padrão de uso irrefletido de IA que acelera o ciclo
- [[concepts/piramide-de-testes]] — testes como seguro contra decisões ruins da IA
- [[concepts/pensamento-sistemico]] — o que se perde quando a dependência cresce

## Key Sources

- [[sources/roadmap-dev-senior-2026]]
- [[sources/apagao-de-seniors-vibe-coding]]
- [[sources/pensamento-estruturado-resolucao-de-problemas]] — sem pensamento estruturado, a IA devolve "um milhão de possibilidades" em vez de uma solução específica; pensar bem é o que torna o uso de IA produtivo em vez de mais um ciclo de dependência
