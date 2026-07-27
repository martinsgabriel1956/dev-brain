---
type: concept
title: "MongoDB"
aliases: ["mongo", "bson"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [mongodb, nosql, banco-de-dados, document-database, backend]
skill: tech-mentor-backend
status: stub
---

# MongoDB

Banco de documentos (BSON — JSON binário, sem esquema fixo). Cada documento na mesma coleção pode ter campos completamente diferentes. Resolve um problema específico muito bem — o problema é tentar usá-lo para tudo. Ver [[wiki/concepts/nosql]] e [[wiki/concepts/relational-vs-nosql]].

## Onde Realmente Resolve

Catálogo de e-commerce com produtos heterogêneos (notebook, camiseta, livro — cada um com campos próprios), sistemas de log/eventos com esquema evoluindo com o tempo, dados de IoT (sensores com estruturas ligeiramente diferentes), CMS com tipo de conteúdo variável. Em todos, inserir um documento novo não exige migration nem `ALTER TABLE`.

## Trade-off Central: Sem JOIN Nativo

`$lookup` existe mas tem custo de performance. Se o sistema tem relacionamento complexo entre entidades (clientes, pedidos, itens, fornecedores todos se referenciando), MongoDB vai custar caro em performance — o banco relacional foi criado exatamente para isso.

## Complementa, Não Substitui o Relacional

Arquitetura real combina os dois: catálogo de produtos em MongoDB para flexibilidade, mas pedido, pagamento, cliente e estoque ficam em PostgreSQL/Oracle, porque exigem transações, integridade referencial e consistência ACID absoluta. Ver [[wiki/concepts/acid]].

## Limites Técnicos

Até 65.536 conexões simultâneas em instância única. Excelente para escrita volumosa e inserção de alta frequência.

## Quem Usa

Mercado Livre e Amazon (catálogo de produtos), plataformas de analytics de comportamento, sistemas de log (Graylog).

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
