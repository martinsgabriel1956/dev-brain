---
type: concept
title: "Amazon DynamoDB"
aliases: ["DynamoDB", "Dynamo"]
date_created: 2026-08-04
date_updated: 2026-09-14
source_count: 5
tags: ["aws", "dynamodb", "nosql", "banco-de-dados", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon DynamoDB

Banco de dados NoSQL gerenciado da AWS, modelo mental de key-value store (como um hash map). Cada item é acessado por duas chaves — **hash key** (partition key) e **sort key** — usadas para ganho de performance na distribuição/indexação dos dados; estruturalmente, apenas a hash key seria necessária. Esquema flexível, com as vantagens e desvantagens usuais de NoSQL.

## Pontos fortes

- **Escala do zero à escala global.** Global Tables permitem replicação e escalabilidade distribuída entre regiões.
- **Latência muito baixa**, especialmente com grandes volumes de dados, em comparação a outros bancos.
- **Bom suporte a eventos**: reage a mudanças de dados (streams) e também pode emitir eventos para outros serviços.

## Contras

- **Custo por request** pode ficar alto em workloads com volume alto de leitura/escrita — o modelo de cobrança é tipicamente pay-per-use por request/capacidade.
- Curva de aprendizado real para modelar dados com eficiência (design de partition/sort key, acesso por padrão de query em vez de normalização relacional).

## Relação com outros conceitos

- [[wiki/concepts/hashmap]] — modelo mental de acesso por chave
- [[wiki/concepts/rds]] — contraparte relacional da AWS
- [[wiki/concepts/consistent-hashing]] — mecanismo relacionado à distribuição de partições em bancos NoSQL de larga escala
- [[wiki/concepts/db-sharding]]

## Modos de Capacidade e Casos Ideais

Exemplo canônico de partition key + sort key: partition key = customer ID, sort key = order date → busca todos os pedidos de um cliente ordenados por data. Dois modos de capacidade: **Provisioned** (quando o padrão de tráfego é conhecido, mais barato) e **On-Demand** (quando não é, mais caro por request mas sem necessidade de planejamento). Casos ideais: sessões, leaderboards, IoT, carrinhos de compra, metadata — **não** ideal para analytics complexos ou dados fortemente relacionais, reforçando o contraste já registrado com [[wiki/concepts/rds]]. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Desenvolvimento Local com LocalStack

Antes de ir para produção, é possível desenvolver contra uma emulação local do DynamoDB via [[wiki/concepts/localstack]] — evita custo de nuvem e dependência de rede durante o desenvolvimento. [[wiki/entities/lucas-badico]] usa esse caminho no core do seu sistema de mentoria em Go, reservando DynamoDB para casos de uso já pensados nativamente para AWS (ex.: agendar notificação uma hora antes de uma mentoria), enquanto o banco relacional principal é PostgreSQL/PostGIS. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Custo por Payload: WCU e RCU

O modelo de cobrança torna o **tamanho do payload** um fator direto de custo, diferente do [[wiki/concepts/postgresql|Postgres]] (onde o tamanho importa mais para performance/armazenamento que para custo da operação): escrita é cobrada em **WCU** (Write Cost Unit, documento dividido por 1 KB — um documento de 24 KB = 24 WCU), cobrando ainda mais se exigir consistência forte ou escrever em mais de uma tabela ao mesmo tempo; leitura é cobrada em **RCU** (Read Cost Unit, dividido por 4 KB). Ver [[wiki/concepts/criterios-de-escolha-de-banco-de-dados]] e [[wiki/concepts/toast-postgresql]] para o contraste direto com o Postgres.

## Compensa Quando Storage é Alto e Transação é Baixa

Cenário concreto onde DynamoDB supera Postgres: base de dados grande (muito storage) mas com baixa frequência de leitura/escrita. No Postgres, manter o índice de uma tabela grande em memória (shared buffer) para boa performance exigiria uma máquina com muita RAM subutilizada — no Dynamo, o custo de storage é baixo, e como o volume de transações é baixo, o custo de transação (onde o Dynamo realmente cobra) também fica baixo. Ver [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — exemplo de partition/sort key, modos Provisioned vs. On-Demand, e casos ideais vs. não ideais
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — uso via LocalStack para desenvolvimento local, em conjunto com PostgreSQL como banco principal
- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — escolha de NoSQL sobre SQL justificada por dois fatores concretos aplicados a um encurtador de URL: dados naturalmente chave-valor (short-code → URL longa) e requisito não-funcional de baixa latência
- [[wiki/sources/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado]] — modelo de cobrança WCU/RCU por KB de payload, e cenário de storage alto + transação baixa onde DynamoDB compensa mais que Postgres
