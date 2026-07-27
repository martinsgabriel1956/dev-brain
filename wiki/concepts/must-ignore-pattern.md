---
type: concept
title: "Must Ignore Pattern"
aliases: ["must-ignore", "schema extension point", "ponto de extensão de schema"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [api, schema-evolution, contrato-de-api, backward-compatibility, xml, xsd]
skill: tech-mentor-testing
status: stub
---

# Must Ignore Pattern

Padrão de extensibilidade de schema: o schema declara pontos de extensão explícitos, e um consumidor que não reconhece um elemento nesse ponto de extensão **deve simplesmente ignorá-lo**, em vez de rejeitar a mensagem inteira. Descrito por [[wiki/entities/ian-robinson]] em [[wiki/sources/consumer-driven-contracts-martin-fowler]] como resposta ao meio-termo entre versionamento de schema permissivo (aceita qualquer coisa) e rígido (rejeita qualquer coisa fora do esperado).

## Por que importa

Sem pontos de extensão explícitos, evoluir um schema força uma escolha ruim: ou a validação é permissiva demais (perde a capacidade de pegar erros reais) ou é rígida demais (qualquer adição de campo quebra consumidores existentes, mesmo os que nunca usariam esse campo). Must Ignore resolve isso preservando compatibilidade retroativa (consumidores antigos continuam funcionando com mensagens novas) e "para frente" (consumidores novos toleram mensagens antigas que ainda não têm o campo).

## Relação com outros conceitos

- [[wiki/concepts/contrato-de-api]] — Must Ignore é uma técnica concreta para versionar contratos sem quebrar consumidores
- [[wiki/concepts/contract-testing]] — reduz a superfície de mudanças que contam como "breaking" e precisam de coordenação via contract test
- Analogia em outros formatos: Protobuf ignora automaticamente campos com field numbers desconhecidos; Avro com Schema Registry projeta o schema do writer para o do reader e ignora o que sobra — o mesmo princípio, garantido pelo protocolo em vez de por convenção manual (ver `wiki/sources/tolerant-reader.md`)

## Open Questions

- Só documentado nesta wiki via um artigo (Robinson, 2006) focado em XML/XSD. Vale checar se alguma fonte futura sobre OpenAPI/JSON Schema usa esse nome especificamente, ou se o equivalente moderno é tratado só sob o guarda-chuva de "campo opcional" sem nome próprio.

## Key Sources

- [[wiki/sources/consumer-driven-contracts-martin-fowler]]
