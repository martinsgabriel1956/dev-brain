---
type: source
title: "UUID: qual o melhor caminho? (pergunta do Diogo)"
aliases: ["uuid custo x beneficio", "quando usar uuid", "uuid vs sequence", "hybrid id strategy"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [uuid, guid, primary-key, sharding, idor, multitenancy, snowflake-id, banco-de-dados, seguranca]
skill: tech-mentor-data
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/uuid-quando-usar-pergunta-diogo.md
source_url:
author: Transcrição de áudio (apresentador não identificado no texto), pergunta de Diogo
date_published:
date_ingested: 2026-08-06
---

# UUID: qual o melhor caminho? (pergunta do Diogo)

## TL;DR

Em resposta à pergunta de um espectador (Diogo) sobre quando vale a pena usar UUID como identificador, o apresentador defende duas vantagens concretas — evitar colisão de chave ao fazer merge de bases shardeadas/multi-origem, e dificultar ataques de enumeração de recursos (IDOR) em APIs REST — contra três desvantagens (espaço, comparação manual difícil, performance). A recomendação prática é uma abordagem híbrida: sequência inteira internamente (joins, queries) + UUID/hash público só nas tabelas expostas por rota, sem que isso substitua um sistema de autorização de verdade.

## Key Claims

| Claim | Evidência |
|---|---|
| UUID evita conflito de chave ao consolidar bases separadas por shard/cliente/região | Caso real do apresentador: precisou reescrever chaves manualmente por "boas semanas" ao integrar bases de clientes diferentes que usavam sequências incrementais |
| UUID (128 bits, randômico) tem risco de colisão desprezível mesmo em bilhões de gerações/dia | Espaço de 2^128 valores possíveis |
| IDs sequenciais expostos em URL de API REST habilitam ataques de enumeração (variar o ID para acessar dados de outro usuário/cliente) | Padrão citado: `/organizacoes/1/usuarios/2`; risco mais alto em sistemas multi-tenant com tabelas compartilhadas |
| UUID como identificador público é "proteção extra", não substituto de autorização | Autorização real exige validar toda referência entre entidades (chaves estrangeiras) contra as permissões do usuário autenticado — não é o ID em si que protege |
| UUID pode ser usado deliberadamente como "senha implícita" de recurso não autenticado | Exemplos: comprovante de compra de passagem aérea, ingresso de show acessível só por link com UUID, sem login |
| Desvantagens de UUID: 16+ bytes vs 4-8 de um inteiro, comparação manual inviável, impacto em índices/performance | Comparação direta com custo de armazenamento e leitura de chave sequencial |
| Estratégia híbrida: sequência interna (int) para joins/queries + UUID/hash só nas tabelas expostas por rota | Abordagem que o apresentador diz já ter usado — ganho de agilidade interna sem abrir mão da proteção onde importa |
| Bancos NoSQL orientados a documentos e bancos de grafos tendem a usar UUID/geração dinâmica de ID com mais frequência que bancos relacionais | Ausência do conceito de "tabela"/sequence nesses bancos — resposta a pergunta de outro espectador (Marco Vinícius) |

## Conceitos

- [[wiki/concepts/uuid]] — a página já cobre versões e o problema de performance em MySQL ([[wiki/sources/uuid-primary-key-mysql]]); esta fonte adiciona os dois argumentos de negócio para usar UUID (merge de bases, anti-enumeração) que a página ainda não tinha
- [[wiki/concepts/idor]] — a fonte descreve o mesmo padrão de ataque (variar ID sequencial para acessar recurso de outro usuário) e trata UUID como mitigação parcial, não substituto de checagem de autorização — consistente com a nota já presente em [[wiki/concepts/idor]]
- [[wiki/concepts/db-sharding]] — o caso de merge de bases shardeadas com colisão de chave sequencial é o motivador central da primeira vantagem citada
- [[wiki/concepts/snowflake-id]] — mencionado implicitamente como alternativa (ID sequencial distribuído) mas não citado pelo nome nesta fonte; a estratégia híbrida descrita aqui é análoga em espírito
- [[wiki/concepts/multitenancy]] — contexto citado para o risco de enumeração: "múltiplos clientes rodando na mesma base de dados, compartilhando as mesmas tabelas"

## Open Questions

- A fonte não cita UUIDv7 nem discute o trade-off de performance de índice que [[wiki/sources/uuid-primary-key-mysql]] detalha (page splitting em B+ Tree) — ela trata UUID de forma genérica, sem diferenciar versões.
- Não há detalhe técnico de como gerar o "hash público" da estratégia híbrida (UUID real vs hash derivado do ID interno) — ponto em aberto para quem for implementar.

## Key Sources

_Este é o documento primário._
