---
type: source
title: "Microservices (artigo original de 2014)"
aliases: ["microsservicos martin fowler", "the term microservice", "smart endpoints and dumb pipes", "componentization via services"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/microsservicos-martin-fowler-james-lewis.md
source_url: "https://martinfowler.com/articles/microservices.html"
author: "James Lewis, Martin Fowler"
date_published: 2014-03-25
date_ingested: 2026-07-27
source_count: 0
tags: [microsservicos, arquitetura, martin-fowler, james-lewis, thoughtworks, conways-law, bounded-context, distributed-monolith, circuit-breaker, polyglot-persistence, tolerant-reader, consumer-driven-contracts, soa]
skill: tech-mentor-backend
status: stable
---

## TL;DR

O artigo canônico que cunhou a definição amplamente citada de "microsserviços" (25 mar 2014): um estilo de construir uma única aplicação como um conjunto de pequenos serviços, cada um rodando no próprio processo, comunicando-se via mecanismos leves (tipicamente HTTP/API de recursos), construídos em torno de capacidades de negócio, implantáveis de forma totalmente automatizada e independente, com o mínimo de gerenciamento centralizado — podendo usar linguagens e tecnologias de dados diferentes entre si. Descreve nove características comuns (não uma definição formal e obrigatória) e termina com uma postura de "otimismo cauteloso" — os autores explicitamente recusam declarar que microsserviços são "o futuro" definitivo da arquitetura de software.

## Key Claims

**Claim:** Microsserviços componentizam via serviços (fora de processo, chamada remota), não via bibliotecas (em processo) — e essa escolha é o que torna cada serviço implantável de forma independente.
**Evidence:** Uma aplicação com múltiplas bibliotecas em um processo único exige reimplantar tudo a cada mudança. Decomposta em serviços, a maioria das mudanças exige reimplantar só o serviço alterado — não absoluto (mudanças de interface exigem coordenação), mas o objetivo de uma boa arquitetura de microsserviços é minimizar isso via fronteiras coesas e evolução de contrato. Trade-off explícito: chamadas remotas são mais caras que chamadas em processo, forçando APIs de granularidade mais grossa.
**Confidence:** alta — claim central do artigo, citado universalmente na indústria desde 2014.

**Claim:** A decomposição correta é por capacidade de negócio (bounded context), não por camada técnica — decompor por camada técnica (times de UI, de lógica, de banco) é um sintoma da Lei de Conway operando contra a modularidade.
**Evidence:** Citação direta de Melvin Conway (1968): "qualquer organização que projeta um sistema produzirá um design cuja estrutura é uma cópia da estrutura de comunicação da organização". Exemplo real: www.comparethemarket.com organiza times multifuncionais por produto, cada produto dividido em serviços que se comunicam via barramento de mensagens.
**Confidence:** alta.

**Claim:** "Smart endpoints and dumb pipes" — a inteligência (lógica de domínio) deve viver nos serviços, não no mecanismo de comunicação; ESBs que embutem roteamento sofisticado, coreografia e regras de negócio na infraestrutura de mensagens são um anti-padrão que o artigo relaciona à má reputação histórica de SOA.
**Evidence:** Citação de Jim Webber: ESB = "Erroneous Spaghetti Box". O artigo lista os dois protocolos favoritos da comunidade: requisição-resposta HTTP com APIs de recursos, e mensageria leve sobre brokers "burros" (RabbitMQ, ZeroMQ) que só roteiam — a inteligência fica nos produtores/consumidores.
**Confidence:** alta.

**Claim:** Governança e dados são descentralizados por design — cada serviço pode escolher sua própria stack (linguagem, banco) e gerencia seu próprio armazenamento (Polyglot Persistence), trocando transações distribuídas por consistência eventual e operações compensatórias.
**Evidence:** Transações distribuídas são "notoriamente difíceis de implementar"; microsserviços preferem "coordenação sem transações", aceitando que a consistência pode ser só eventual — o artigo argumenta que isso frequentemente reflete a própria prática de negócio (tolerar inconsistência temporária em troca de resposta rápida, com processo de reversão para corrigir erros).
**Confidence:** alta.

**Claim:** Design for Failure é obrigatório — falha parcial é o estado normal em um sistema de serviços remotos, e o artigo cita o Simian Army da Netflix (indução deliberada de falhas em produção) e o Circuit Breaker (de *Release It!*) como respostas típicas.
**Evidence:** Qualquer chamada de serviço pode falhar por indisponibilidade do fornecedor. Sidebar do artigo: "chamadas síncronas em cadeia" multiplicam downtime (downtime do sistema = produto dos downtimes dos componentes); Guardian.co.uk limita a uma chamada síncrona por requisição de usuário; Netflix redesenhou a API para assincronicidade nativa.
**Confidence:** alta.

**Claim:** Os próprios autores não afirmam que microsserviços sejam definitivamente superiores nem "o futuro" — reconhecem riscos reais de imaturidade (fronteiras de componente difíceis de acertar e caras de refatorar entre processos, deslocamento de complexidade das conexões internas para as externas, dependência de habilidade do time).
**Evidence:** "Não estamos argumentando que temos certeza de que microsserviços são a direção futura"; citam a possibilidade de que a "verdadeira consequência" de uma decisão arquitetural só apareça anos depois, e que um time ruim vai construir um sistema ruim independentemente do estilo escolhido.
**Confidence:** alta — postura textual explícita, frequentemente perdida em resumos populares que tratam o artigo como um manifesto pró-microsserviços sem ressalvas.

## Entities & Concepts Touched

- [[wiki/entities/martin-fowler]]
- [[wiki/entities/ian-robinson]] (citado: "Be of the web, not behind the web")
- [[wiki/entities/thoughtworks]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/application-boundary]]
- [[wiki/concepts/contexto-organizacional-para-arquitetura]] (Lei de Conway)
- [[wiki/concepts/circuit-breaker]]
- [[wiki/concepts/contract-testing]] (Tolerant Reader, Consumer-Driven Contracts citados como padrões de evolução de contrato em microsserviços)
- [[wiki/concepts/yagni]]

## Open Questions

- O artigo cita "distributed monolith" apenas implicitamente (via os riscos de acoplamento por transações e por refatoração cara entre processos) — o termo explícito "Distributed Monolith" como anti-padrão nomeado já aparece em várias páginas desta wiki ([[wiki/concepts/microsservicos]], [[wiki/sources/anti-patterns]]) mas a página de conceito `wiki/concepts/distributed-monolith` ainda não existe — link quebrado preexistente, fora do escopo desta ingestão, registrado aqui para o próximo sweep de lint.
- O artigo menciona "Bounded Context" (DDD) e "Conway's Law" com links para os bliki entries originais de Fowler — esta wiki já tem `wiki/sources/ddd-strategic` e `wiki/sources/conways-law` como fontes ingeridas, mas as páginas de conceito correspondentes (`wiki/concepts/ddd-strategic`, `wiki/concepts/conways-law`) também estão ausentes — mesmo padrão de link quebrado, mesma recomendação de lint.
- O artigo (2014) é anterior ao livro de Sam Newman (mencionado no próprio texto como "ainda sendo escrito" em 2014) e ao artigo posterior "Microservice Trade-Offs" (jul 2015, referenciado inline) — nenhum dos dois foi ingerido nesta wiki ainda; ambos aprofundam trade-offs que este artigo apenas introduz.
