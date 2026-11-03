---
type: concept
title: "Árvore de Decisão de Computação em Nuvem"
aliases: ["compute decision tree", "fluxo de decisão de compute", "choose an azure compute service"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cloud, azure, decisao-arquitetural, infra]
skill: tech-mentor-infra
status: stub
---

# Árvore de Decisão de Computação em Nuvem

Fluxograma que reduz as dezenas de serviços de um provedor a um candidato inicial, a partir de perguntas sobre a aplicação. A fonte usa o da documentação do Azure como exemplo e diz que ele vale para quem usa outros provedores, combinado a um de-para. [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]

## Lógica geral

1. **Migrar ou criar?** Migrar legado costuma ser mais difícil. Ver [[wiki/concepts/lift-and-shift]].
2. **Está conteinerizada?** Se não, as opções diminuem bastante.
3. **Quanto controle você quer?** Controle total leva a VM ([[wiki/concepts/ec2]] na AWS) e a mais trabalho de operação.
4. **Qual é a natureza da carga?** Batch, eventos curtos, web gerenciada ou contêineres.
5. **Quer as APIs do Kubernetes?** Se sim, [[wiki/concepts/kubernetes]] gerenciado; se não, [[wiki/concepts/conteineres-gerenciados-sem-kubernetes]].

Os passos estão detalhados em [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]. O resultado é só o começo: `[external]` a [Microsoft](https://learn.microsoft.com/azure/architecture/guide/technology-choices/compute-decision-tree) manda avaliar o candidato nas tabelas de comparação, e cada componente separadamente se a carga tiver partes distintas. A decisão final passa por [[wiki/concepts/criterios-de-adocao-de-servico-cloud]].

## Cuidado: envelhece

`[external]` O Azure Spring Apps, citado no vídeo, não aparece mais nessa página e será aposentado em março de 2028.

## Key Sources

- [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]
