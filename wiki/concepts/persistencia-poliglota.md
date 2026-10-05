---
type: concept
title: "Persistência Poliglota (um armazenamento por necessidade)"
aliases: ["polyglot persistence","mapa de armazenamento","cinco tipos de armazenamento"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [banco-de-dados, arquitetura, nosql, cache, busca, mensageria, tomada-de-decisao]
skill: tech-mentor-data
status: draft
---

# Persistência Poliglota

Ideia central de [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]: o maior erro na escolha de armazenamento **não é a tecnologia errada, é achar que todos os dados devem ir sempre para o mesmo lugar**. Um pedido, uma sessão, uma busca por descrição e uma mensagem entre serviços têm necessidades diferentes.

## O mapa (loja virtual)

| Necessidade do dado | Armazenamento | Ver |
|---|---|---|
| Estrutura conhecida, relações, corretude, transação (clientes, pedidos, pagamento, estoque) | Relacional | [[wiki/concepts/postgresql]], [[wiki/concepts/acid]] |
| Estrutura que varia por registro (catálogo de produtos) | Documento (NoSQL) | [[wiki/concepts/dado-semiestruturado]], [[wiki/concepts/mongodb]] |
| Lookup por chave, rápido, temporário (sessão, cache, rate limit) | Chave-valor | [[wiki/concepts/chave-valor]], [[wiki/concepts/redis]] |
| Achar palavras/trechos com relevância | Mecanismo full-text | [[wiki/concepts/full-text-search]] |
| Entregar o evento a outro processo, sem bloquear | Fila / log | [[wiki/concepts/mensageria]], [[wiki/concepts/kafka]] |

As perguntas certas são sobre o **dado**: precisa durar para sempre? estar sempre atualizado? tem relações? muda de formato? expira em minutos? precisa ser achado por texto? precisa ser entregue a outro processo? Critérios de ranking popular ("o que a gigante usa", "o que eu sei usar") são o erro comum.

## Ressalva (a frase mais importante do vídeo)

É um **mapa de possibilidades, não uma lista obrigatória**: loja pequena pode ficar só no relacional. Ver [[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]]. Cada peça nova traz instalação, monitoramento, backup, segurança e um novo jeito de falhar.

Duas das cinco peças são **cópias derivadas** (cache, índice de busca) e nunca a fonte oficial: [[wiki/concepts/fonte-de-verdade-vs-copia-derivada]].

## Relação com a wiki

Complementa [[wiki/concepts/criterios-de-escolha-de-banco-de-dados]] (8 critérios para escolher *entre bancos*) e [[wiki/concepts/relational-vs-nosql]]; aqui o eixo é *quais tipos de armazenamento coexistem*. [skill: tech-mentor-data, `references/databases/nosql.md`] — regra prática análoga: "comece com PostgreSQL; adicione NoSQL especializado com necessidade comprovada". Em microsserviços, o corolário é [[wiki/concepts/database-per-service]].

## Key Sources

- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]
