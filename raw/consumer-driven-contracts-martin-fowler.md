---
title: "Consumer-Driven Contracts: A Service Evolution Pattern"
author: "Ian Robinson"
source_url: "https://martinfowler.com/articles/consumerDrivenContracts.html"
date_published: 2006-06-12
date_ingested: 2026-07-27
note: "Resumo/paráfrase em PT-BR preparado para a wiki, não é tradução literal do artigo original. Para o texto exato, consultar a source_url."
---

# Consumer-Driven Contracts: A Service Evolution Pattern — resumo comentado

Artigo de Ian Robinson (Principal Consultant na Thoughtworks), publicado no site de Martin Fowler em 12 de junho de 2006. O tema é como arquiteturas orientadas a serviço (SOA) podem evoluir seus contratos sem quebrar consumidores, e sem que provedor e consumidores fiquem presos a um acoplamento rígido demais.

## O problema que motiva o artigo

O artigo usa como exemplo recorrente um serviço fictício `ProductSearch`, consumido tanto por uma aplicação interna de marketing quanto por aplicações externas de revendedores (resellers). Cada consumidor usa apenas uma parte do contrato exposto pelo serviço.

O problema aparece quando o provedor precisa evoluir o schema: por exemplo, adicionar um campo novo, ou remover um campo (`InStock`) que ninguém mais usa. Se a validação for rígida (XSD tradicional, exigindo conformidade total com o schema), qualquer mudança — mesmo em uma parte do contrato que um consumidor específico nunca usou — pode quebrar esse consumidor. O provedor fica refém do medo de quebrar alguém, e a evolução do serviço trava.

## Versionamento de schema e "Must Ignore"

Robinson revisita as estratégias de versionamento de schema do W3C, que vão de permissivas (aceitam qualquer mudança) a rígidas (rejeitam qualquer coisa fora do esperado). Ele defende um meio-termo: schemas com pontos de extensão explícitos, seguindo o padrão **Must Ignore** — o schema permite elementos adicionais que um consumidor pode simplesmente ignorar se não os reconhecer, preservando compatibilidade retroativa e "para frente" (forward compatibility).

## Validação "na medida certa" e o Robustness Principle

Para o caso de remover um campo não utilizado, Robinson recorre ao **Robustness Principle** do Internet Protocol ("seja conservador no que envia, liberal no que recebe"). A recomendação prática: consumidores devem validar apenas os dados que efetivamente usam, não o payload inteiro.

Para viabilizar isso ele cita o **Schematron** como alternativa ao XSD: em vez de validação tudo-ou-nada contra um schema completo, o Schematron permite escrever asserções pontuais sobre os elementos específicos que aquele consumidor realmente precisa. Isso reduz o acoplamento do consumidor a partes do contrato que não lhe interessam.

## O padrão Consumer-Driven Contracts

O núcleo do artigo é um modelo de contrato em três camadas:

- **Provider Contract**: tudo que o serviço expõe — schemas, interfaces, conversas/protocolos, políticas, garantias de qualidade de serviço.
- **Consumer Contract**: o subconjunto do provider contract que um consumidor específico efetivamente usa e espera.
- **Consumer-Driven Contract**: o contrato do provedor *derivado* da união de todos os consumer contracts conhecidos — ou seja, construído de baixo para cima a partir das necessidades reais dos consumidores, em vez de definido unilateralmente pelo provedor.

A inversão proposta é essa: ao invés do provedor desenhar um contrato "completo" e esperar que os consumidores se adaptem a ele, o provedor enxerga explicitamente quais partes do contrato realmente sustentam valor de negócio (porque algum consumidor as usa) e quais partes são seguras para remover ou alterar sem coordenação.

### Como implementar na prática

O padrão é agnóstico de implementação. Os contratos de consumidor podem existir como planilhas, testes automatizados, ou asserções em tempo de execução (via Schematron, WS-Policy, etc). A comunicação entre provedor e consumidores acontece fora de banda — conversa direta entre times, ou apoiada por alguma infraestrutura de coordenação — não é um mecanismo automático embutido no protocolo.

## Benefícios

- Alinha a evolução do serviço ao que de fato gera valor de negócio para os consumidores existentes.
- Dá ao provedor feedback granular: antes de fazer uma mudança, dá para avaliar exatamente qual consumidor será afetado e decidir deliberadamente sobre compatibilidade retroativa.

## Limitações e escopo

- O padrão funciona melhor dentro de uma única empresa ou em uma comunidade fechada de serviços, onde o provedor tem influência real sobre os consumidores (consegue negociar e fazer com que eles adotem os consumer contracts).
- Não elimina o acoplamento entre provedor e consumidor — apenas torna esse acoplamento "escondido" visível e negociável explicitamente.
- Há um risco: se consumidores fizerem exigências que fogem do escopo de negócio do serviço, atender a esses consumer contracts pode comprometer a integridade e coerência do próprio serviço.

## Conceitos e trabalhos relacionados citados no artigo

- Trabalho de David Orchard sobre extensibilidade em XML.
- "Data on the Outside vs. Data on the Inside", de Pat Helland.
- Frameworks WS-Policy e WS-SecurityPolicy.
- WS-Agreement e WSLA — citados explicitamente como algo *diferente* de consumer contracts (são acordos de nível de serviço/SLA, não expressões de expectativas funcionais de um consumidor específico).
