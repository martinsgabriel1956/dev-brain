---
type: source
title: "Como Escolher o Banco de Dados Certo: História, ACID, CAP e Números Reais"
aliases: ["escolha de banco de dados", "historia dos bancos de dados", "numeros reais de bancos de dados"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-escolher-banco-de-dados-historia-acid-cap.md
source_url: ""
author: "TI das Antigas"
date_published: ""
date_ingested: 2026-07-27
source_count: 1
tags: [banco-de-dados, acid, cap-theorem, mysql, postgresql, oracle, sql-server, sqlite, redis, mongodb, system-design, backend]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Vídeo em três partes: (1) história do modelo relacional — de arquivos ISAM acoplados dos anos 70/80 ao paper de Edgar F. Codd (IBM, 1970) que introduziu independência de dados; (2) ACID e CAP como os dois conceitos fundamentais que a maioria dos devs pula; (3) números reais de instância única (conexões, volume, latência) para MySQL, PostgreSQL, Oracle, SQL Server, SQLite, Redis e MongoDB, com casos de uso e empresas que usam cada um. Tese central: escolha de banco é decisão de arquitetura/negócio, não hype técnico — e todos os números citados são o piso de uma instância única, sem escala horizontal.

## Key Claims

**Claim:** Antes do modelo relacional (Codd, 1970), programas eram acoplados à estrutura física do arquivo (ISAM/CSV) — mudar um campo quebrava todos os módulos que liam aquele arquivo.
**Evidence:** Sem SGBD, o programa precisava saber o byte exato de início de cada campo; buscas sem índice liam o arquivo inteiro sequencialmente. Codd propôs que o programa declare o que quer e o sistema decida como buscar — "independência de dados". Oracle V2 (1979) e IBM DB2 (1983) nasceram dessa ideia.
**Confidence:** alta — consistente com a história documentada do modelo relacional.

**Claim:** ACID (Atomicidade, Consistência, Isolamento, Durabilidade) é o motivo pelo qual sistemas financeiros e de saúde usam bancos relacionais.
**Evidence:** Alinhado com [[wiki/concepts/acid]] já existente na wiki.
**Confidence:** alta.

**Claim:** Teorema CAP (Eric Brewer, 2000) — em partição de rede, escolha real é entre Consistência (CP) e Disponibilidade (AP), já que Partition Tolerance é praticamente obrigatória em sistemas distribuídos reais.
**Evidence:** Consistente com [[wiki/concepts/cap-theorem]] e com a referência `distributed-systems.md` da skill `tech-mentor-backend` (PostgreSQL/MySQL = CP; Cassandra/DynamoDB = AP).
**Confidence:** alta.

**Claim:** Conexão simultânea ≠ usuário online — 600 usuários navegando geram tipicamente 20–50 conexões reais simultâneas no banco; o que ocupa conexão de fato é query longa, transação aberta não comitada, ou conexão vazada por bug.
**Confidence:** média-alta — é um comportamento observável, mas o número exato (20–50) depende do padrão de acesso da aplicação.

**Claim:** MySQL — padrão de fábrica 151 conexões (`my.cnf`); viável 5.000–10.000 em servidores com 128–256 GB RAM; até ~100.000 documentado em 512 GB. Cada conexão consome ~1 MB de RAM (thread). Acima de 5.000 conexões em instância única, degradação por context switching. Erro ao estourar: `1040 Too many connections` (reserva 1 conexão extra para `root`).
**Confidence:** média — números específicos de configuração variam por versão/hardware; a ordem de grandeza é consistente com documentação pública do MySQL.

**Claim:** PostgreSQL usa processo por conexão (não thread) — isolamento melhor, mas custo maior por conexão IDLE; por isso PgBouncer é padrão de indústria, elevando o limite prático de conexões diretas para 500–2.000.
**Evidence:** Consistente com padrão documentado em `database-connection-patterns.md` da skill `tech-mentor-backend` e com [[wiki/concepts/postgresql]] (regra de ouro já cita PgBouncer).
**Confidence:** alta.

**Claim:** Oracle com RAC (Real Application Cluster) multiplica sessões horizontalmente; instância única dedicada suporta 10.000–65.000 sessões ativas. Recursos exclusivos: Flashback Query, Advanced Compression, particionamento nativo avançado. Custo: licenciamento por núcleo de CPU e DBA sênior dedicado.
**Confidence:** média — números de sessão dependem fortemente de hardware/licença; direção geral (Oracle = robustez cara) é consistente com o mercado.

**Claim:** SQL Server Express (gratuito) — limite de 10 GB por banco, 1 socket/4 cores, 1 GB de buffer pool; degrada acima de 50 usuários simultâneos escrevendo. Edição Standard eleva para 128 GB de memória e 200–1.000 conexões.
**Confidence:** média-alta — limites de edição são documentados publicamente pela Microsoft; o "número de usuários" que degrada é estimativa do autor.

**Claim:** SQLite não é servidor — é biblioteca embarcada, arquivo único, lock global de escrita (escritas concorrentes serializadas mesmo em modo WAL). Certificado pela norma DO-178C em aviônica (Airbus); usado em todo app Android/iOS, Chrome, Firefox, npm.
**Confidence:** alta — comportamento de lock de escrita do SQLite é bem documentado; certificação DO-178C é claim específica não verificada nesta ingestão.

**Claim:** Redis atinge >100 mil OPS/s em hardware comum e até 1 milhão de OPS/s com pipeline/batching; em quase 100% dos casos reais não é o banco principal, vive como camada de cache/velocidade em cima de um banco relacional que é a fonte de verdade.
**Evidence:** Consistente com [[wiki/concepts/redis]] já existente.
**Confidence:** alta.

**Claim:** MongoDB resolve bem catálogos com schema variável (ex.: notebook vs. camiseta vs. livro no mesmo e-commerce) sem exigir tabela com 200 colunas nulas ou arquitetura EAV; mas não tem JOIN nativo (`$lookup` tem custo) e sofre com relacionamento complexo — não substitui o banco relacional, complementa. Limite: até 65.536 conexões simultâneas em instância única.
**Evidence:** Consistente com [[wiki/concepts/nosql]] e [[wiki/concepts/relational-vs-nosql]] já existentes na wiki.
**Confidence:** alta na tese (complementar, não substituto); média no número exato de conexões.

## Entities & Concepts Touched

- [[wiki/concepts/acid]]
- [[wiki/concepts/cap-theorem]]
- [[wiki/concepts/mysql]]
- [[wiki/concepts/postgresql]]
- [[wiki/concepts/redis]]
- [[wiki/concepts/nosql]]
- [[wiki/concepts/relational-vs-nosql]]
- [[wiki/concepts/oracle-database]]
- [[wiki/concepts/sql-server]]
- [[wiki/concepts/sqlite]]
- [[wiki/concepts/mongodb]]
- [[wiki/concepts/connection-pooling]]
- [[wiki/concepts/database-index]]
- [[wiki/entities/edgar-codd]]

## Open Questions

- Os números de conexões/sessões por hardware (MySQL, Oracle, SQL Server) são estimativas do autor do vídeo, sem benchmark linkado — vale validar contra documentação oficial de cada fornecedor antes de usar como referência de capacity planning.
- A certificação DO-178C do SQLite em aviônica Airbus é citada sem fonte primária — não verificada nesta ingestão.
- Vídeo promete um próximo episódio sobre escala horizontal/vertical (réplicas, shards, clusters, proxies) — ainda não ingerido.

## Raw Quotes

> "Escolher banco de dados errado não é um problema que aparece no dia 1, ele aparece no dia que você tem mil usuários conectados."

> "Quando alguém te disser: usa o MongoDB que é mais rápido, o que essa pessoa está realmente dizendo é: esse banco abre mão de algumas garantias de consistência em troca de velocidade e escala."

> "Todos os números aqui citados — conexões, volume, latência — são em instâncias únicas, sem escala horizontal. É basicamente o piso, o ponto de partida."

## Ver também

- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]
- [[wiki/sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
