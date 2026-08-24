---
type: source
title: "Deployment Pipeline (Martin Fowler)"
aliases: ["deployment pipeline bliki", "pipeline de deploy fowler"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/deployment-pipeline-martin-fowler.md
source_url: "https://martinfowler.com/bliki/DeploymentPipeline.html"
author: "Martin Fowler"
date_published: 2013-05-30
date_ingested: 2026-08-23
source_count: 0
tags: [cicd, continuous-delivery, pipeline, martin-fowler, build-scripting]
skill: tech-mentor-infra
status: stable
---

# Deployment Pipeline (Martin Fowler)

## TL;DR

Bliki curto (2013) em que Fowler define e nomeia o "deployment pipeline": a resposta à tensão entre feedback rápido e testes abrangentes é quebrar o build em **estágios progressivos**, cada um oferecendo mais confiança ao custo de mais tempo. Estágios iniciais (compilação, testes rápidos) pegam a maioria dos problemas rápido; estágios finais (verificações manuais, deploy em produção) fazem uma checagem mais lenta e minuciosa. Fowler amplia o escopo do pipeline além de velocidade: seu trabalho é detectar qualquer mudança que cause problemas em produção (performance, segurança, usabilidade), e ele deve dar **visibilidade e trilha de auditoria** a todos os grupos envolvidos na entrega — não só rodar testes. Termina com uma recomendação prática: para introduzir continuous delivery, modele o processo de entrega atual como um deployment pipeline e procure gargalos, oportunidades de automação e pontos de colaboração.

## Key Claims

- **Definição central**: um deployment pipeline quebra o build em estágios, cada um trocando tempo extra por confiança crescente — a resposta à tensão entre build rápido (feedback) e testes abrangentes (lentos).
- **Estágios iniciais vs. finais**: estágios iniciais pegam a maioria dos problemas com feedback rápido; estágios finais fazem probing mais lento e minucioso. O primeiro estágio normalmente compila e gera binários para os estágios seguintes; estágios finais podem incluir verificações manuais (testes que não dá para automatizar).
- **Estágios podem ser automáticos ou manuais**, e podem ser paralelizados em várias máquinas para acelerar o build. O deploy em produção costuma ser o estágio final.
- **Escopo maior que "só rodar testes"**: o trabalho do pipeline é detectar qualquer mudança que leve a problemas em produção — inclui performance, segurança e usabilidade, não só corretude funcional.
- **Função de colaboração e visibilidade**: um deployment pipeline deve viabilizar colaboração entre os grupos envolvidos na entrega e dar a todos visibilidade sobre o fluxo de mudanças, junto com uma trilha de auditoria completa.
- **Deployment pipelines são parte central de Continuous Delivery** — não um conceito à parte.
- **Recomendação prática de adoção**: modelar o processo de entrega atual como um deployment pipeline e examiná-lo em busca de gargalos, oportunidades de automação e pontos de colaboração é uma boa forma de introduzir continuous delivery.

## Entities

[[wiki/entities/martin-fowler]]

## Concepts

[[wiki/concepts/ci-cd]] · [[wiki/concepts/pipeline-de-ci]] · [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]

## Conexão com o que a wiki já sabia

[[wiki/concepts/ci-cd]] já citava, numa única linha, que "o termo 'Deployment Pipeline' é de Martin Fowler" e já usava a ideia de fail-fast (testes rápidos primeiro) sem uma fonte primária dedicada — esta ingestão fecha essa lacuna. [[wiki/concepts/pipeline-de-ci]] já detalhava uma estrutura de 7 estágios (lint → build → integration → security gates) sem citar de onde vem o princípio de estágios progressivos por confiança — agora rastreável a esta fonte. [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] já tinha uma linha de tabela ("estágio inicial do CI/CD" vs. "staging, geralmente como gate de deploy") que é exatamente o raciocínio de estágios por confiança/velocidade descrito aqui.

## Open Questions

- Fowler não detalha, nesta fonte curta, exemplos concretos de ferramentas ou de uma implementação real de deployment pipeline — o artigo fica no nível de definição e princípio, remetendo ao capítulo 5 do livro *Continuous Delivery* (Humble & Farley) para profundidade.
- Não fica claro se "trilha de auditoria completa" é uma característica que Fowler considera obrigatória ou apenas desejável — o texto não distingue os dois.

## Raw Quotes

*(Tradução completa em `raw/deployment-pipeline-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
