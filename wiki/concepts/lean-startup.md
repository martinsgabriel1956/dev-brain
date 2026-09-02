---
type: concept
title: "Lean Startup"
aliases: ["startup enxuta", "the lean startup", "metodologia lean startup"]
date_created: 2026-07-07
date_updated: 2026-09-02
source_count: 3
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

## Lean Canvas Como Ferramenta de Diagnóstico, Não Ritual Obrigatório

[[wiki/sources/pare-de-ter-ideias-icp-lean-canvas-obsoleto-ia]] questiona a prática, comum a partir de ~2012, de preencher o [[wiki/concepts/lean-canvas]] de Ash Maurya inteiro como passo 1 antes de captar investimento ou construir. O argumento não é abandonar o Lean Startup, mas reconhecer que o gargalo mudou: com IA, o MVP leva dias em vez de meses (ver [[wiki/concepts/mvp#MVP e a Compressão do Tempo de Construção com IA]]), então vale gastar menos tempo documentando hipóteses num canvas e mais tempo executando o ciclo [[concepts/build-measure-learn]] de verdade. Os dois quadrantes do canvas que o autor mantém como essenciais — problema e [[wiki/concepts/icp-ideal-customer-profile|ICP]] — mapeiam diretamente para a fase "Visão" do Lean Startup, reforçando de fonte independente que [[wiki/concepts/validacao-de-problema]] continua sendo o ponto de partida correto.

## Ver Também

- [[concepts/build-measure-learn]] — o ciclo operacional da metodologia
- [[concepts/mvp]] — a unidade de entrega mínima
- [[concepts/scope-creep]] — o que a metodologia previne ao forçar escopo mínimo
- [[wiki/concepts/lean-canvas]] — ferramenta de diagnóstico da fase "Visão", com crítica ao uso como passo 1 obrigatório
- [[wiki/concepts/icp-ideal-customer-profile]] — especificação do "cliente" na fase de validação de problema

## Key Sources

- [[sources/lean-startup-para-devs-mano-deivin]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — build-measure-learn aplicado ao lançamento real do Find My SaaS
- [[wiki/sources/pare-de-ter-ideias-icp-lean-canvas-obsoleto-ia]] — crítica ao Lean Canvas como passo 1 obrigatório; gargalo real deslocado de "programar" para "validar" na era da IA
