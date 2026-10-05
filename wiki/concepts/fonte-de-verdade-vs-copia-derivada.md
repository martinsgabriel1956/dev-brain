---
type: concept
title: "Fonte de Verdade vs. Cópia Derivada"
aliases: ["source of truth","cache não é fonte de verdade","índice de busca é cópia"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [arquitetura, cache, busca, consistencia, banco-de-dados]
skill: tech-mentor-data
status: draft
---

# Fonte de Verdade vs. Cópia Derivada

Regra repetida duas vezes em [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]: cache e índice de busca são **cópias derivadas**; a fonte oficial é outra, e as cópias devem poder ser **reconstruídas do zero**.

- **Cache** ([[wiki/concepts/cache]], [[wiki/concepts/chave-valor]]): valor pode expirar ou ser despejado por falta de memória. "Um pedido pago que existe só no cache não é arquitetura, é roleta-russa."
- **Índice de busca** ([[wiki/concepts/full-text-search]], Elasticsearch/OpenSearch — ver [[wiki/sources/elasticsearch-opensearch]]): recebe cópia do necessário para buscar; pode haver atraso de segundos entre alterar o produto e a busca refletir (ex.: anúncios em OLX/Mercado Livre) — o sistema deve conviver com isso ([[wiki/concepts/eventual-consistency]]).
- **Fonte**: tipicamente o relacional ou o de documentos.

Teste prático: "se eu apagar este armazenamento agora, consigo reconstruí-lo a partir da fonte?" Se não, ele deixou de ser cópia. Mecanismos de manter a cópia em dia (eventos/CDC): [[wiki/concepts/outbox-pattern]], [[wiki/concepts/mensageria]]. Relacionado: [[wiki/concepts/persistencia-poliglota]].

## Key Sources

- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]
