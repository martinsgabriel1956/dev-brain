---
type: source
title: "ORM vs. SQL Puro: Organização de Regras de Negócio e Escolha de Banco de Dados"
aliases: ["orm vs sql", "stored procedure regra de negocio", "relacional vs nao relacional q&a"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [orm, sql, stored-procedure, banco-de-dados, relational-vs-nosql, read-replicas, database-index, arquitetura]
skill: tech-mentor-backend
status: stable
source_file: "raw/orm-sql-organizacao-regras-negocio-bancos-dados.md"
source_url: ""
author: "desconhecido (Q&A de live/stream, transcrição automática com ruído — ver nota no arquivo raw)"
date_published: ""
date_ingested: "2026-07-03"
---

## TL;DR

Respostas a perguntas de chat sobre três temas conectados: (1) por que sistemas com relacionamentos profundos e chaves compostas tornam o ORM quase inviável, forçando SQL direto; (2) como organizar regra de negócio quando ela cresce dentro do banco — stored procedures ajudam, mas o autor evita usá-las, functions e triggers em excesso, preferindo mover para o banco só o que realmente precisa de agregação em escala (ex.: apuração de inadimplência sobre 1 milhão de faturas) e manter tudo mais na aplicação, com views/materialized views como meio-termo; (3) como escolher entre banco relacional e não relacional — depende da necessidade de fazer múltiplas junções sobre um schema formalizado (relacional) vs. dado não estruturado/ML/grafo/documento (não relacional), lembrando que bancos relacionais modernos (coluna JSON indexável) já cobrem boa parte do que levaria alguém a um NoSQL.

---

## Reivindicações Principais

**Claim:** Em sistemas com relacionamentos muito profundos e muitas chaves compostas, algumas lógicas ficam quase impossíveis de expressar via ORM, forçando o uso de SQL direto.
**Evidência:** Afirmação direta do autor respondendo a uma observação do chat, sem exemplo de código nomeado.
**Confiança:** Média-alta — consistente com a limitação de "leaky abstraction" já registrada em [[wiki/concepts/orm]], mas sem caso concreto detalhado nesta fonte.

**Claim:** Queries escritas diretamente em SQL tendem a ser mais otimizadas que queries geradas por ORM, porque o desenvolvedor sabe exatamente quais tabelas relaciona, quais colunas retorna, quais cláusulas usa e se está batendo o índice.
**Evidência:** Contraste explícito entre "escrever query mais curta e específica" vs. depender de query gerada pelo ORM.
**Confiança:** Média — é uma posição de preferência pessoal do autor ("eu não gosto tanto de ORM"), não uma medição de benchmark citada na fonte.

**Claim:** Regras de negócio que crescem em volume dentro do SQL tendem a ser organizadas em stored procedures, mas o autor considera saudável usar isso com moderação — tenta se manter fora de stored procedures, functions e triggers na maior parte do tempo, reconhecendo que "existem casos e casos".
**Evidência:** Resposta direta a pergunta do chat sobre organização de regra de negócio em SQL.
**Confiança:** Alta quanto à posição do autor (é uma opinião declarada explicitamente); é uma recomendação de estilo, não uma regra objetiva.

**Claim:** Decisão de responsabilidade aplicação vs. banco: operações de agregação sobre volume muito grande de dados (ex.: 1 milhão de faturas para apurar inadimplência de um mês) devem ser executadas no banco, não trazidas para a memória da aplicação — nenhum servidor de aplicação aguentaria esse volume processado linha a linha.
**Evidência:** Exemplo concreto do domínio do autor (faturas de cartão de crédito, conta de luz, conta de água).
**Confiança:** Alta — é um argumento de escala bem fundamentado (mover agregação para onde o dado já está, evitar I/O de rede e serialização de 1M de linhas).

**Claim:** Views (incluindo materialized views, com um nível de cache embutido) são um meio-termo saudável entre "SQL cru toda vez" e "regra de negócio inteira dentro do banco via stored procedure".
**Evidência:** Afirmação do autor ao equilibrar a resposta anterior contra o uso de stored procedures.
**Confiança:** Média — mencionado de forma breve, sem exemplo de implementação.

**Claim:** Relatórios devem sempre consultar um banco réplica, nunca o banco de produção primário, porque produção está concorrendo com processos mais críticos (ex.: rastreamento de veículos, chamadas telefônicas) — e a maioria dos sistemas lê muito mais do que escreve (~10% do tempo é escrita), o que torna réplicas uma forma eficiente de ganhar escala.
**Evidência:** Regra geral declarada pelo autor com exemplos de domínios concorrentes.
**Confiança:** Alta — consistente com a prática padrão de [[wiki/concepts/read-replicas]] documentada em outras fontes desta wiki.

**Claim:** A escolha entre banco relacional e não relacional depende da necessidade do sistema de alcançar um mesmo dado por vários caminhos via junções (teoria dos conjuntos) — se essa necessidade existe, banco relacional é necessário; se o caso é dado não estruturado, machine learning, ou data lake, um banco não relacional (grafo, documento, etc.) pode ser mais adequado.
**Evidência:** Resposta a duas perguntas do chat (Bruna e Renan Mateus) sobre "qual o melhor tipo de banco".
**Confiança:** Alta quanto à posição do autor; consistente com o quadro de decisão já registrado em [[wiki/concepts/relational-vs-nosql]].

**Claim:** Bancos relacionais modernos já incorporam características de bancos não relacionais (ex.: colunas JSON indexáveis), o que reduz a necessidade de montar uma infraestrutura poliglota complexa.
**Evidência:** Comentário final do autor fechando a resposta sobre escolha de banco.
**Confiança:** Alta — consistente com o suporte a `JSONB` do PostgreSQL já documentado em [[wiki/concepts/postgresql]].

---

## Conceitos

- [[wiki/concepts/orm]] — limitação do ORM em relacionamentos profundos/chaves compostas; reforça a leaky abstraction já registrada
- [[wiki/concepts/sql-alem-do-basico]] — preferência por queries diretas, curtas e específicas em vez de SQL gerado por ORM
- [[wiki/concepts/database-index]] — precisão de saber se a query está batendo o índice como vantagem do SQL direto
- [[wiki/concepts/stored-procedure]] — organização de regra de negócio no banco; posição cautelosa do autor sobre uso excessivo
- [[wiki/concepts/materialized-view]] — meio-termo entre SQL cru e stored procedure, com camada de cache
- [[wiki/concepts/read-replicas]] — relatório sempre bate em réplica, nunca em produção
- [[wiki/concepts/relational-vs-nosql]] — critério de decisão: necessidade de junções múltiplas (relacional) vs. dado não estruturado/ML/grafo (não relacional)
- [[wiki/concepts/postgresql]] — colunas JSON indexáveis como ponte entre relacional e não relacional

## Ver também

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — mesma tensão entre abstrair SQL (ORM/DSL) e escrever SQL direto, sob outro ângulo (SQL embutido no código como "erro grave")
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — quadro de decisão relacional/ACID vs. não relacional/BASE por domínio de negócio
- [[wiki/sources/read-replicas-connection-pooling]] — aprofundamento técnico em réplicas de leitura e pooling

---

## Conexões com Outras Sources

- [[wiki/sources/banco-de-dados]] — fundamentos gerais de banco de dados, incluindo índice, réplica e N+1

---

## Perguntas Abertas

- O autor não detalha um exemplo concreto de query com chave composta que se torna inviável em ORM — vale registrar um caso real na próxima vez que aparecer.
- Falta critério objetivo de "quando uma stored procedure deixa de ser saudável" — o autor reconhece "casos e casos" sem definir um limite prático (nº de linhas? complexidade ciclomática? acoplamento a lógica de domínio?).

---

## Citações

> "Quando você usa muito o ORM, a tendência é que essas queries não sejam otimizadas. Já quando você escreve a query diretamente, você sabe quais tabelas vai relacionar, que colunas vai retornar, que tipo de cláusulas vai usar, se está batendo o índice ou não."

> "Eu tento me manter fora das stored procedures, fora das functions, fora das triggers — é bom até certo ponto, mas eu já acho que você está passando de um ponto que eu considero saudável, apesar de reconhecer que existem casos e casos."

> "Relatório sempre tem que bater num banco réplica. Você não deve colocar relatório pra bater no banco de produção, porque você está concorrendo com uma série de outros processos mais importantes que esse."
