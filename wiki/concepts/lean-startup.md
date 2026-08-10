---
type: concept
title: "Lean Startup"
aliases: ["startup enxuta", "the lean startup", "metodologia lean startup"]
date_created: 2026-07-07
date_updated: 2026-08-06
source_count: 2
tags: [carreira, produto, mvp, startup, validacao, empreendedorismo]
skill: tech-mentor-leadership
status: stable
---

# Lean Startup

Metodologia criada por [[entities/eric-ries]] no livro *A Startup Enxuta* para validar produtos antes de investir tempo pesado em construção. Nasce da observação de que devs (e founders em geral) tendem a construir a partir de uma ideia não validada, gastando meses ou anos num produto que ninguém quer.

## Ideia Central

Não valide a solução que você imaginou — valide se **a dor é real** antes de escrever qualquer linha de código. A metodologia estrutura isso em fases sequenciais:

1. **Visão** — confirmar que existe uma dor real e compartilhada, não apenas a sua dor pessoal → [[concepts/validacao-de-problema]]
2. **Construir-Medir-Aprender** — ciclo iterativo com MVP de funcionalidade única → [[concepts/build-measure-learn]]
3. **Aprendizagem validada** — consolidar decisões de produto com teste A/B, não achismo → [[concepts/aprendizagem-validada]]
4. **Contabilização de inovação** — métricas de negócio consolidadas (faturamento, retenção) → [[concepts/contabilizacao-de-inovacao]]
5. **Crescimento sustentável** — testar modelos de monetização
6. **Pivô ou persevere** — decidir se muda de direção ou dobra a aposta → [[concepts/pivotar-ou-perseverar]]

Depois dessas fases, produtos maduros entram em **inovação contínua**: mantêm a essência validada e adicionam frentes novas sem perder o núcleo → [[concepts/inovacao-continua]]

## Por Que Importa para Devs

O erro clássico do "dev emocionado" é pular direto para a fase de construção — abrir o editor e codar a partir de uma ideia não testada. Isso alimenta dois ciclos de falha:

- Nunca lançar (perfeccionismo técnico, sempre trocando stack/interface)
- Lançar e descobrir que ninguém usa, tentando compensar com mais features

Lean Startup resolve isso invertendo a ordem: validar barato antes de construir caro.

## Relação com MVP

O MVP é a ferramenta tática da fase "Construir" — o menor artefato capaz de gerar aprendizado real sobre o mercado. → [[concepts/mvp]]

## Caso real: Find My SaaS

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], o autor cita explicitamente o ciclo construir-medir-aprender ao justificar por que lançou o Find My SaaS numa VPS mínima, sem arquitetura elaborada: "sem esperar nada perfeito e sem querer prever todas as cascas possíveis" — mas ressalva que isso exige conhecimento suficiente para entregar algo "minimamente seguro", não ausência de cuidado. Ver [[wiki/concepts/mvp]] para a implementação técnica dessa entrega mínima e [[wiki/concepts/over-engineering]] para a recusa explícita de complexidade de infraestrutura antecipada.

## Ver Também

- [[concepts/build-measure-learn]] — o ciclo operacional da metodologia
- [[concepts/mvp]] — a unidade de entrega mínima
- [[concepts/scope-creep]] — o que a metodologia previne ao forçar escopo mínimo

## Key Sources

- [[sources/lean-startup-para-devs-mano-deivin]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — build-measure-learn aplicado ao lançamento real do Find My SaaS
