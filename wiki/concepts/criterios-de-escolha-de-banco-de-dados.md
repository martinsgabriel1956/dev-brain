---
type: concept
title: "Critérios de Escolha de Banco de Dados"
aliases: ["como escolher banco de dados", "framework de escolha de banco", "database selection criteria"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [banco-de-dados, system-design, postgresql, mongodb, dynamodb, entrevista-tecnica, backend, arquitetura]
skill: tech-mentor-backend
status: stable
---

# Critérios de Escolha de Banco de Dados

Resposta mais rasa: escolher banco pelo **tipo do dado** — esquema livre → documental ([[wiki/concepts/mongodb]]), dado relacionado/normalizado → relacional ([[wiki/concepts/postgresql]]). Não está errada, mas ignora como o dado é acessado, atualizado e paga por si — o que separa uma resposta júnior de uma sênior numa entrevista de system design. Ver [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]].

## Os 8 Critérios

1. **Data schema** — o formato do dado (estruturado/normalizado vs. livre) e a frequência com que esse esquema muda.
2. **Forma de acesso** — consulta por múltiplos campos variáveis (filtros compostos, formulário de busca) favorece SQL-like; busca estritamente por chave favorece [[wiki/concepts/dynamodb|key-value store]].
3. **Leitura vs. escrita** — [[wiki/concepts/postgresql|Postgres]] tradicional é otimizado para leitura (índice em shared buffer); [[wiki/concepts/mongodb|MongoDB]]/[[wiki/concepts/dynamodb|DynamoDB]] já nascem com sharding/distribuição horizontal, mais otimizados para volume de escrita.
4. **Transacional vs. storage** — base pequena com alta frequência de mutação (ex.: carrinho de compra) vs. base grande com baixa frequência de mutação (ex.: catálogo de produtos). Determina se o custo real está em manter índice em RAM (Postgres) ou em WCU/RCU por operação ([[wiki/concepts/dynamodb|DynamoDB]]).
5. **Consistência** — [[wiki/concepts/acid|ACID]] (relacional) vs. consistência eventual (a maioria dos NoSQL, especialmente com sharding). Ver [[wiki/concepts/cap-theorem]].
6. **Latência** — impacto no *worst case*; depende do uso real dado ao banco (base otimizada para escrita usada com carga de leitura forte, ou vice-versa, sofre).
7. **Escalabilidade** — relacional tradicional escala majoritariamente **vertical** (o nó de escrita tem teto de hardware; sharding manual não é automático); [[wiki/concepts/dynamodb|DynamoDB]] escala automaticamente e **horizontal**.
8. **Custo** — não é um critério isolado, é o resumo de todos os anteriores. Só se calcula depois de resolver os outros sete.

## Exemplo Central: Postgres vs. DynamoDB Não é Sobre o Formato do Dado

O vídeo-fonte escolhe entre DynamoDB, MongoDB e Postgres **sem considerar o formato da informação** — só frequência de atualização e tipo de consulta:

- Transações altas + base pequena + majoritariamente leitura → Postgres.
- Transações baixas + storage muito alto → DynamoDB (custo de storage barato, custo de transação caro).
- Escrita muito alta → MongoDB.

Isso inverte a heurística mais comum ("dado flexível → Mongo, dado relacional → SQL"): aqui a decisão vem inteiramente do padrão de workload, não do shape do dado.

## Onde o Critério Vira Custo Concreto

- **Postgres**: tabela grande sem particionamento precisa manter o índice inteiro no [[wiki/concepts/buffer-pool|buffer pool]] para performance — se o volume de transações é baixo, isso significa pagar uma máquina com muita RAM subutilizada. Documento/linha grande (~24 KB, citado como exemplo) estoura o tamanho de página e vai para [[wiki/concepts/toast-postgresql|TOAST]] — impacta performance, não custo direto da operação.
- **DynamoDB**: cobra por WCU (write, documento dividido por 1 KB) e RCU (read, dividido por 4 KB) — tamanho do payload importa **diretamente** para o custo, ao contrário do Postgres.
- **Escrita intensa em base MVCC** (Postgres): gera tuplas versionadas acumuladas, exigindo `VACUUM` frequente — sem isso, degrada performance por table bloat. Ver [[wiki/concepts/mvcc]].

## Alavancas de Throughput de Escrita no Postgres

`CREATE TABLE ... UNLOGGED` (pula o write-ahead log) e desativar `synchronous_commit` (não espera propagar o WAL pro disco antes de responder, ganho estimado de ~3-5% pela fonte) são configurações que aumentam throughput de escrita à custa de garantias de durabilidade — trade-off explícito contra o padrão de fábrica do Postgres, que prioriza leitura e durabilidade.

## Consistência Eventual em Réplicas de Leitura

Réplicas de leitura ([[wiki/concepts/read-replicas]]) têm consistência eventual: o request pode não chegar exatamente na réplica já atualizada, gerando pequena latência de replicação — geralmente aceitável em sistemas de alta performance, mas inaceitável para saldo financeiro ou inventário crítico.

## Regra Prática

Em alguns cenários não há liberdade de escolha (empresa já padronizada em um banco). Quando há liberdade, a base mais barata/performática/evolutiva exige responder, nesta ordem: como salvo → como acesso → leio ou escrevo mais → transação ou storage → preciso de ACID ou eventual basta → quais restrições de latência → como escalo → só então, qual o custo.

## Relação com outros conceitos

- [[wiki/concepts/postgresql]] — exemplo central de banco otimizado para leitura e consistência forte
- [[wiki/concepts/mongodb]] — exemplo de banco otimizado para escrita e schema flexível
- [[wiki/concepts/dynamodb]] — exemplo de banco key-value com custo diretamente ligado ao payload
- [[wiki/concepts/mvcc]] — mecanismo por trás do trade-off leitura/escrita no Postgres
- [[wiki/concepts/cap-theorem]] — formaliza o trade-off de consistência citado no critério 5
- [[wiki/concepts/sharding]] — mecanismo por trás da escalabilidade horizontal citada no critério 7
- [[wiki/concepts/read-replicas]] — mecanismo concreto de escalabilidade vertical com alívio de leitura

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]] — framework completo dos 8 critérios, com exemplos de Postgres/MongoDB/DynamoDB
