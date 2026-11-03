---
type: concept
title: "Abordagem Evolutiva"
aliases: ["evoluir conforme a necessidade", "pense grande comece pequeno", "abordagens evolutivas"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [over-engineering, mvp, refatoracao, produto, decisao-arquitetural]
skill: tech-mentor-backend
status: stub
---

# Abordagem Evolutiva

Começar pequeno e aumentar o sistema conforme a necessidade comprovada, em vez de antecipar problemas que talvez nunca aconteçam.

## O ciclo

Segundo [[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]]:

1. Manter simples no início ([[wiki/concepts/kiss]], [[wiki/concepts/yagni]]).
2. Entregar um [[wiki/concepts/mvp]] e testar com o público-alvo.
3. Receber feedback e métricas de uso.
4. Escolher o próximo passo com esses dados, não com suposições.

É a mesma estrutura de [[wiki/concepts/build-measure-learn]], aplicada aqui como defesa contra [[wiki/concepts/over-engineering]].

## Contexto muda a fonte da informação

- **Empresa consolidada:** o levantamento de requisitos já indica boa parte do que é necessário.
- **Negócio novo ou inovador:** a necessidade ainda é hipótese, então a validação do produto pesa mais.

## Começar simples não basta

A fonte responde à objeção de que produto simples vira bagunça: o erro está em como o software foi mantido, não em ter começado simples. Por isso a abordagem depende de [[wiki/concepts/refatoracao]] e de princípios de código, sem os quais vira [[wiki/concepts/under-engineering]] (inferência minha sobre a ligação entre os termos).

A fonte também afirma que evoluir algo simples é muito mais fácil do que cortar partes de algo inflado. Não apresenta dados, e [[wiki/sources/monolith-first-martin-fowler]] registra um contra-argumento em substituições de sistema.

## Distinção de Evolutionary Architecture

`[skill: tech-mentor-backend]` *Evolutionary Architecture* é um termo mais específico: arquitetura projetada para mudança guiada e incremental, com *fitness functions* verificando características automaticamente. A fonte não fala disso. Sua abordagem é um princípio de produto e escopo, sem mecanismo de verificação.

## Ver também

- [[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]] — mesma lógica aplicada a armazenamento de dados
- [[wiki/concepts/walking-skeleton]] — fatia mínima fim a fim em produção
- [[wiki/concepts/decisao-tecnica-embasada-em-metricas]] — os dados que orientam cada passo

## Key Sources

- [[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]]
