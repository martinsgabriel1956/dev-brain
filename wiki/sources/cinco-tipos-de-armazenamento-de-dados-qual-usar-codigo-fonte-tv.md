---
type: source
title: "Cinco Tipos de Armazenamento de Dados: Qual Usar em Cada Problema (Código Fonte TV)"
aliases: ["cinco tipos de armazenamento", "como escolher armazenamento de dados código fonte tv", "mapa de armazenamento da loja virtual"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 0
tags: [banco-de-dados, persistencia-poliglota, relational, nosql, key-value, cache, full-text-search, mensageria, yagni, dicionario-do-programador]
skill: tech-mentor-data
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv.md"
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: "2026-10-05"
---

## TL;DR

Vídeo da série "Dicionário do Programador" de [[wiki/entities/codigo-fonte-tv]]. Tese: o maior erro de escolha de armazenamento é achar que todos os dados vão para o mesmo lugar ([[wiki/concepts/persistencia-poliglota]]). Usando uma loja virtual, mapeia cinco necessidades a cinco tipos: **relacional** (clientes, pedidos, pagamento, estoque; transação "tudo ou nada", SQL — [[wiki/concepts/acid]]), **documento/NoSQL** (catálogo de estrutura variável — [[wiki/concepts/dado-semiestruturado]]), **chave-valor** (sessão, cache, rate limit — [[wiki/concepts/chave-valor]]), **mecanismo full-text** (busca com relevância, Elasticsearch/OpenSearch) e **fila/mensageria** (RabbitMQ, SQS, Kafka; assíncrono, desacoplamento, idempotência). Avisos: "sem esquema" não é "sem modelagem"; cache e índice de busca são cópias, nunca fonte de verdade ([[wiki/concepts/fonte-de-verdade-vs-copia-derivada]]); e o mapa é **de possibilidades, não lista obrigatória** — comece no relacional e adicione peças quando o problema aparecer ([[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]]). Contém trecho patrocinado da [[wiki/entities/hostinger]] (VPS + Dokploy).

---

## Reivindicações Principais

**Claim:** O erro mais grave é tratar todos os dados como iguais e mandá-los ao mesmo lugar; a escolha deve partir de perguntas sobre o dado (durar para sempre? sempre atualizado? relações? muda de formato? expira? precisa de busca por texto? precisa ser entregue a outro processo?), não de popularidade, curso ou "o que a gigante usa".
**Evidência:** Cinco cenários de uma loja virtual; efeitos colaterais citados: lentidão, inconsistência, redundância, despadronização.
**Confiança:** Alta como enquadramento; converge com [[wiki/concepts/criterios-de-escolha-de-banco-de-dados]] e [[wiki/concepts/cargo-cult-tecnologico]]. Sem dados medidos.

**Claim:** Relacional serve a dados de estrutura conhecida, com relações e que precisam ficar corretos; a **transação** (criar pedido + registrar pagamento + baixar estoque) garante "ou tudo ou nada"; SQL é declarativo e estável por décadas.
**Evidência:** Exemplo do servidor cair entre pagamento e baixa de estoque; analogia gaveta × cartório; modelo relacional dos anos 70.
**Confiança:** Alta — [[wiki/concepts/acid]], [[wiki/concepts/postgresql]], [[wiki/concepts/mysql]], [[wiki/concepts/sqlite]]. A data "anos 70" confere com o artigo de Codd (1970) [external, não verificado aqui].

**Claim:** Relacional é boa decisão inicial para a maioria dos projetos, mas vira o martelo para tudo (sessão, cache, log, fila improvisada) por inércia.
**Evidência:** Posição dos apresentadores.
**Confiança:** Média-alta — opinião experiente, coerente com [skill: tech-mentor-data, `references/databases/nosql.md`] ("comece com PostgreSQL… adicione NoSQL com necessidade comprovada").

**Claim:** Documentos (JSON) acomodam produtos com atributos distintos sem migração por tipo; o relacional também consegue, mas pode virar "lutar contra a estrutura". "Sem esquema rígido" não elimina a modelagem — a estrutura passa a viver no código ([[wiki/concepts/dado-semiestruturado]]).
**Evidência:** Notebook × camiseta × livro; exemplo `preço` vs `valor` quebrando o código; "NoSQL" como guarda-chuva (documentos, colunas largas: Cassandra/Bigtable).
**Confiança:** Alta. Ressalva do vídeo: fugir de migration não justifica sozinho o NoSQL.

**Claim:** Chave-valor serve a dados consultados em altíssima frequência, sem relações e que podem expirar (sessão, código de verificação de 10 min, contador de rate limit, carrinho temporário "com cuidados", cache); rápido por viver em memória (Redis, Memcached).
**Evidência:** Demonstração no Redis instalado via Dokploy, com chaves de sessão e TTL.
**Confiança:** Alta — [[wiki/concepts/redis]], [[wiki/concepts/session-management]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/cache]].

**Claim:** Cache é cópia temporária que evita repetir operação cara; erro perigoso é torná-lo a **única** fonte de algo importante, pois expira ou é despejado — "pedido pago só no cache é roleta-russa".
**Evidência:** Exemplo da home com os mais acessados; recomendação de saber reconstruir da fonte original.
**Confiança:** Alta — [[wiki/concepts/fonte-de-verdade-vs-copia-derivada]].

**Claim:** O banco relacional faz busca textual (inclusive full-text próprio) e basta para catálogos pequenos; mecanismos dedicados (Elasticsearch/OpenSearch) valem quando crescem volume, campos, tolerância a variação de escrita e **relevância**, usando índice (tipo índice remissivo). O índice é cópia reconstruível, com delay de segundos.
**Evidência:** Exemplo "notebook leve para programação" × "ideal para desenvolvedores"; OLX/Mercado Livre como exemplo de delay.
**Confiança:** Alta — [[wiki/concepts/full-text-search]], [[wiki/sources/elasticsearch-opensearch]]. "Índice de busca" descrito sem citar o termo técnico *índice invertido* (inferência [skill]).

**Claim:** Hoje a IA pode substituir a abordagem de busca ao receber dados brutos e decidir relevância, inclusive acrescentando conhecimento que não está na descrição.
**Evidência:** Anedota pessoal sobre uma cadeira de escritório para podcast.
**Confiança:** Baixa-média — anedota única; ignora custo, latência e alucinação ([[wiki/concepts/alucinacao-llm]]); relacionado a [[wiki/concepts/busca-semantica]] e [[wiki/concepts/hybrid-search]].

**Claim:** Mensageria permite responder ao usuário na hora e executar o resto (estoque, e-mail, nota, logística, relatório) depois ou em outro processo; produtor → fila/log → consumidores no seu ritmo; ganho de desacoplamento (novo consumidor sem mexer no fluxo da compra).
**Evidência:** E-mail lento não deve derrubar a compra; analogia do SMS de recuperação de senha atrasado.
**Confiança:** Alta — [[wiki/concepts/mensageria]], [[wiki/concepts/processamento-assincrono]], [[wiki/concepts/comunicacao-assincrona]].

**Claim:** Kafka tecnicamente não é fila tradicional, é um log distribuído de eventos; no mapa cumpre o mesmo papel de transporte (com RabbitMQ e Amazon SQS).
**Evidência:** Afirmação do apresentador.
**Confiança:** Alta — [[wiki/concepts/kafka]], [[wiki/entities/rabbitmq]].

**Claim:** Fila não resolve sozinha a integração, só muda os problemas de lugar: exige idempotência (cobrança duplicada em reprocessamento), retries, ordem e destino para mensagem que nunca é processada (fila travada).
**Evidência:** Exemplo de cobrança dupla e da fila de impressão travada.
**Confiança:** Alta — [[wiki/concepts/idempotencia]], [[wiki/concepts/dlq]]. Não cita [[wiki/concepts/outbox-pattern]] (consistência entre gravar no banco e publicar o evento) — lacuna.

**Claim:** O mapa é de possibilidades, não obrigação: loja pequena pode ficar só no relacional; cada tecnologia nova traz instalação, monitoramento, backup, segurança e novos modos de falha; maturidade é adicionar peças quando o problema chega "com nome e sobrenome".
**Evidência:** Fecho do vídeo.
**Confiança:** Alta — [[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]], [[wiki/concepts/yagni]], [[wiki/concepts/over-engineering]].

---

## Entidades e Conceitos Tocados

- [[wiki/entities/codigo-fonte-tv]] — canal/autoria; [[wiki/entities/hostinger]] — patrocínio (VPS, Dokploy); [[wiki/entities/rabbitmq]]
- Novos: [[wiki/concepts/persistencia-poliglota]] (draft), [[wiki/concepts/dado-semiestruturado]] (draft), [[wiki/concepts/chave-valor]] (draft), [[wiki/concepts/fonte-de-verdade-vs-copia-derivada]] (draft), [[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]] (stub)
- Existentes atualizados: [[wiki/concepts/criterios-de-escolha-de-banco-de-dados]], [[wiki/concepts/nosql]], [[wiki/concepts/relational-vs-nosql]], [[wiki/concepts/acid]], [[wiki/concepts/postgresql]], [[wiki/concepts/mysql]], [[wiki/concepts/mongodb]], [[wiki/concepts/redis]], [[wiki/concepts/cache]], [[wiki/concepts/session-management]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/full-text-search]], [[wiki/concepts/mensageria]], [[wiki/concepts/fila]], [[wiki/concepts/kafka]], [[wiki/concepts/idempotencia]], [[wiki/concepts/processamento-assincrono]], [[wiki/concepts/yagni]], [[wiki/concepts/over-engineering]]

---

## Perguntas em Aberto

- Como manter o índice de busca/cache sincronizado com a fonte (CDC, outbox, eventos)? Não abordado — ver [[wiki/concepts/outbox-pattern]].
- Critério de quando a busca do próprio banco deixa de bastar (volume/latência)? Só qualitativo; [[wiki/sources/elasticsearch-opensearch]] cita >10M docs.
- Vídeos do Dicionário do Programador sobre NoSQL, SQL, Elasticsearch e Kafka são citados mas ainda não estão na wiki.
- Sem tratamento de armazenamento de arquivos/objetos, séries temporais, grafos ou vetores (cobertos em [skill: tech-mentor-data]).

---

## Citações Preservadas

> "O maior erro ao escolher um banco de dados não é escolher a tecnologia errada… é achar que todos os dados deveriam ir sempre pro mesmo lugar."

> "Um pedido pago que existe só no cache não é uma arquitetura, é uma verdadeira roleta-russa."

> "Maturidade muitas vezes é começar com o bom e velho banco de dados relacional e adicionar as outras peças quando o problema aparecer de verdade."
