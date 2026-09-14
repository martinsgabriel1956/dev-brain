---
type: source
title: "Como Escolher o Banco de Dados Certo (Além do Tipo de Dado)"
aliases: ["critérios de escolha de banco de dados", "banco de dados em entrevista de system design"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-escolher-banco-de-dados-criterios-alem-do-tipo-de-dado.md
source_url: ""
author: "não identificado"
date_published: ""
date_ingested: 2026-09-14
source_count: 1
tags: [banco-de-dados, system-design, postgresql, mongodb, dynamodb, mvcc, cap-theorem, entrevista-tecnica, backend]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Vídeo (autor/canal não identificado, colado diretamente no prompt pelo usuário) argumentando que a pergunta "qual banco de dados você usaria?" é a mais importante de uma entrevista de system design, e que a resposta baseada só no **tipo do dado** (documento → Mongo, relacional → SQL) é correta mas rasa. Propõe um framework de 8 critérios — [[wiki/concepts/criterios-de-escolha-de-banco-de-dados|data schema, forma de acesso, leitura vs. escrita, transacional vs. storage, consistência, latência, escalabilidade e custo]] — para decidir entre bases relacionais (Postgres), documentais (MongoDB) e key-value (DynamoDB), com exemplos concretos de arquitetura interna (MVCC, TOAST, fillfactor, WCU/RCU) que conectam a escolha a custo real.

## Key Claims

**Claim:** Resposta baseada só no tipo do dado (documento → NoSQL, relacional → SQL) é considerada correta, mas superficial — falta considerar forma de acesso, frequência de atualização e custo.
**Confidence:** alta — tese central do vídeo, consistente com [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] ("escolha de banco é decisão de arquitetura/negócio, não hype técnico").

**Claim:** Postgres tradicional é otimizado para leitura por padrão — índice B+ tree fica no shared buffer para consultas em milissegundos de um dígito; escrita exige recalcular/rebalancear o índice. `CREATE TABLE ... UNLOGGED` pula o WAL e desativar `synchronous_commit` (ganho de ~3-5%) são alavancas para aumentar throughput de escrita.
**Evidence:** Consistente com [[wiki/concepts/postgresql]] (processo por conexão, PgBouncer) e [[wiki/concepts/mvcc]] (custo de versionamento). `UNLOGGED` e `synchronous_commit` são features reais do Postgres.
**Confidence:** média-alta — mecanismo geral correto; o número "~3-5%" é estimativa do autor sem benchmark linkado.

**Claim:** MongoDB e DynamoDB já vêm com sharding/separação em múltiplas instâncias por padrão — arquitetura otimizada para volume maior de escrita, mesmo suportando leitura alta.
**Evidence:** Consistente com [[wiki/concepts/nosql]] (escalabilidade horizontal nativa) e [[wiki/concepts/sharding]].
**Confidence:** média — direção geral correta; MongoDB não faz sharding "por padrão" em toda instalação (requer configuração explícita de cluster), então a formulação do autor simplifica.

**Claim:** Estrutura de dados pode ser mais "transacional" (muda com frequência, base menor) ou mais "storage" (volume grande, poucas mutações) — ex.: carrinho de e-commerce (transacional) vs. catálogo de produtos (storage).
**Confidence:** alta — analogia didática consistente com padrões de modelagem já registrados em [[wiki/concepts/mongodb]] (catálogo heterogêneo) e [[wiki/concepts/ecommerce-marketplace]] (se existente).

**Claim:** Tabela grande sem particionamento no Postgres precisa manter o índice inteiro em memória (shared buffer) para boa performance — se o volume de transações é baixo, isso significa pagar uma máquina grande com muita RAM subutilizada; nesse cenário, DynamoDB (custo de storage baixo, custo de transação alto) pode compensar mais.
**Evidence:** Consistente com [[wiki/concepts/buffer-pool]] e com o modelo de cobrança do DynamoDB (WCU/RCU) descrito no vídeo.
**Confidence:** média — direção arquitetural correta; não há benchmark citado comparando custo real Postgres-com-RAM-grande vs. DynamoDB para esse cenário específico.

**Claim:** Escrita muito alta numa base MVCC (Postgres) gera tuplas versionadas acumuladas (dead tuples), exigindo `VACUUM` frequente — sem isso, degrada performance (table bloat).
**Evidence:** Idêntico ao mecanismo já registrado em [[wiki/concepts/mvcc]] via [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]].
**Confidence:** alta — consistente com documentação pública do Postgres e com claim já validada na wiki.

**Claim:** Bases relacionais em geral seguem ACID; bases NoSQL documentais/key-value tendem a consistência eventual, principalmente quando há sharding (necessário para replicar entre nós).
**Confidence:** alta — consistente com [[wiki/concepts/acid]] e [[wiki/concepts/cap-theorem]].

**Claim:** Bases relacionais tradicionais escalam principalmente **verticalmente** — mesmo com réplicas de leitura, o nó primário (escrita) está limitado ao hardware; sharding existe mas não é processo natural/automático do banco. DynamoDB escala automaticamente e horizontalmente conforme o workload.
**Evidence:** Consistente com [[wiki/concepts/read-replicas]] e [[wiki/concepts/sharding]] ("sharding pressupõe decomposição por DDD/microsserviços" — não é automático).
**Confidence:** alta.

**Claim:** Réplicas de leitura têm consistência eventual — request pode não chegar na réplica já atualizada, gerando pequena latência de replicação, geralmente aceitável em sistemas de alta performance.
**Evidence:** Consistente com [[wiki/concepts/read-replicas]] (replication lag estimado em 1-3s por [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]]).
**Confidence:** alta.

**Claim:** No Postgres, documento/registro grande (ex.: 24 KB) estoura o tamanho da página — o dado vai para TOAST (armazenamento binário fora da página principal, referenciado), o que impacta performance mas não custo direto de operação (só custo de disco/transferência).
**Confidence:** alta na mecânica (TOAST é feature documentada do Postgres); não verificado nesta ingestão contra a documentação oficial do limite exato de página (8 KB por padrão, o que motiva o TOAST acima de ~2 KB de valor de coluna, não exatamente "24 KB" como limiar).

**Claim:** DynamoDB cobra por WCU (Write Cost Unit, documento dividido por 1 KB) e RCU (Read Cost Unit, dividido por 4 KB) — tamanho do payload importa diretamente para custo, diferente do Postgres onde o tamanho importa mais para performance/armazenamento do que para custo direto da operação.
**Evidence:** Consistente com [[wiki/concepts/dynamodb]] (modelo de cobrança pay-per-request/capacidade).
**Confidence:** alta — mecanismo de WCU/RCU por KB é documentado publicamente pela AWS.

**Claim:** Custo total só pode ser calculado depois de analisar toda a estrutura (schema, acesso, leitura/escrita, transação/storage, consistência, latência, escalabilidade) — é um resumo de todos os critérios anteriores, não um critério isolado.
**Confidence:** alta — conclusão lógica do próprio framework apresentado.

## Entities & Concepts Touched

- [[wiki/concepts/criterios-de-escolha-de-banco-de-dados]]
- [[wiki/concepts/postgresql]]
- [[wiki/concepts/mongodb]]
- [[wiki/concepts/dynamodb]]
- [[wiki/concepts/mvcc]]
- [[wiki/concepts/toast-postgresql]]
- [[wiki/concepts/read-replicas]]
- [[wiki/concepts/sharding]]
- [[wiki/concepts/nosql]]
- [[wiki/concepts/cap-theorem]]
- [[wiki/concepts/acid]]
- [[wiki/concepts/database-index]]

## Open Questions

- O ganho de "~3-5%" ao desativar `synchronous_commit` é citado sem benchmark linkado — vale validar contra medições próprias antes de usar como referência de capacity planning.
- O limiar de "24 KB" para acionar TOAST no Postgres não bate exatamente com a documentação oficial (TOAST ativa por coluna quando o valor ultrapassa ~2 KB, com o objetivo de manter a linha dentro de uma página de 8 KB) — tratado como simplificação didática do autor, não verificado como número técnico exato.
- A afirmação de que MongoDB "já vem" com sharding por padrão simplifica: sharding no MongoDB é uma configuração explícita de cluster, não o comportamento de uma instância standalone — vale reconciliar com [[wiki/concepts/mongodb]] numa futura revisão.
- Vídeo não cita fontes primárias (documentação AWS/Postgres) para nenhum dos números — todas as claims técnicas são apresentadas com autoridade mas sem link, e foram cruzadas aqui apenas contra o conhecimento já presente na wiki e na skill `tech-mentor-backend`.

## Raw Quotes

> "Escolher banco de dados errado não é um problema que aparece no dia 1" — [tese equivalente já registrada via outra fonte; não há citação literal marcante nesta transcrição além do argumento central sobre profundidade da resposta em entrevista.]

> "Percebam que eu escolhi aqui entre Dynamo, Mongo e Postgres sem me preocupar com o formato da informação, mas sim com a frequência que eu atualizo e o tipo de consulta que eu faço."

> "O custo... é exatamente um resumo entre tudo que tá aqui."

## Ver também

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]]
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]]
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]]
