---
type: concept
title: "Planning Fallacy"
aliases: ["viés de planejamento", "planning fallacy", "subestimação de esforço"]
date_created: 2026-04-29
date_updated: 2026-08-18
source_count: 3
tags: [psicologia, estimativa, projetos, produtividade, carreira]
skill: tech-mentor-leadership
status: stable
---

# Planning Fallacy

Tendência cognitiva de subestimar o tempo, custo e riscos de tarefas futuras enquanto superestima os benefícios — especialmente em tarefas desconhecidas. Cunhado por Kahneman e Tversky (1979).

## Por Que Devs São Especialmente Vulneráveis

- Muitas tarefas envolvem domínios novos (frameworks, APIs, infra)
- O Efeito Dunning-Kruger amplifica: quanto menos sabe, mais confiante na estimativa
- Complexidade oculta só emerge durante a construção, não durante o planejamento

## Manifestação em Projetos Paralelos

```
Estimativa mental: "2 fins de semana"
Realidade: auth sozinho leva 1 semana
→ escopo creep para compensar → projeto abandona
```

## Exemplo Numérico: Custo Oculto Multiplicando por 3x

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] ilustra o viés com uma conta concreta: uma feature trivial (formulário → endpoint) estimada ingenuamente em 2h chega a 6h somando revisão de PR, troca de contexto do revisor, correção pós-review, testes, margem para imprevisto aleatório e pausas humanas — sem nenhum evento excepcionalmente ruim no meio do caminho. A fonte também argumenta que, como esse viés tende a ser **consistente** (a mesma pessoa/time subestima repetidamente na mesma direção), medir o erro passado é a única forma de corrigi-lo de forma confiável — ver [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]] e a seção "Calibrando a Direção do Erro" em [[wiki/concepts/estimativas-de-software]].

## Contramedidas

- **Reference class forecasting**: quanto tempo projetos *similares* levaram, não o atual
- **[[concepts/mvp]]**: escopo mínimo reduz exposição à planning fallacy
- **Pre-mortem**: imaginar que o projeto falhou e identificar por quê antes de começar

## Ver Também

- [[concepts/scope-creep]] — consequência direta da planning fallacy
- [[concepts/dopamina-e-projetos]] — otimismo na ideação amplifica o viés

## Key Sources

- [[sources/por-que-devs-nao-terminam-projetos]]
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — o problema grave não é errar a estimativa, é não *mensurar* o erro dela (planejar 40 pontos e entregar 30 repetidamente sem medir o gap); liga a subestimação sistemática à necessidade de [[wiki/concepts/folga-de-capacidade-slack|folga de capacidade]]
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — exemplo numérico de custo oculto (2h→6h) e argumento de que a redução de incerteza antes de estimar é uma contramedida estrutural ao viés, não só um ajuste de fator
