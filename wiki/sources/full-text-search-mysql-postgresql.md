---
type: source
title: "Full-Text Search: Por Que o LIKE Está Errado (e Como Fazer Busca Inteligente em MySQL e PostgreSQL)"
aliases: ["full text search", "match against", "to_tsvector to_tsquery", "índice invertido busca", "like vs full text search"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 0
tags: [banco-de-dados, full-text-search, mysql, postgresql, sql, indice-invertido, performance, gin, relevancia]
skill: tech-mentor-data
status: stable
source_file: "raw/full-text-search-mysql-postgresql.md"
source_url: ""
author: "Renato Augusto (canal do 'Mapa do Arquiteto', mesma entidade já registrada em [[wiki/entities/renato-augusto]])"
date_published: ""
date_ingested: "2026-07-29"
---

## TL;DR

`LIKE '%termo%'` é a abordagem intuitiva para busca no backend, mas está estruturalmente errada em dois eixos: (1) relevância — compara substring de caracteres, não palavras, então "Ana" também casa com "Luciana" e "anel" também casa com "panela"; (2) performance — força um full table scan (`Seq Scan`/table scan) em toda a tabela, e o custo escala como tamanho-da-tabela × usuários-concorrentes. **Full-Text Search** resolve os dois problemas com um índice invertido dedicado: `FULLTEXT INDEX` + `MATCH ... AGAINST` no MySQL, `tsvector`/`tsquery` + índice `GIN` no PostgreSQL — ordens de grandeza mais rápido (0,35 vs. 1028 de custo interno no MySQL; 0,3–0,8ms vs. 139ms no Postgres) e com ranking de relevância nativo. PostgreSQL vai além do MySQL: entende plural/singular e reduz palavras ao mesmo lexema automaticamente (stemming), permitindo tesauros/sinônimos configuráveis — recurso que o MySQL não oferece.

---

## Reivindicações Principais

**Claim:** `LIKE '%termo%'` busca por sequência de caracteres em qualquer posição da string, não por palavras — por isso retorna falsos positivos semânticos (buscar "Ana" retorna "Luciana"; buscar "anel" retorna "panela").
**Evidência:** Demonstração ao vivo em tabela de 10.000 usuários e 10.000 produtos via DBeaver, com queries `LIKE '%Ana%'` e `LIKE '%anel%'` e inspeção manual dos falsos positivos retornados.
**Confiança:** Alta — é o comportamento documentado e esperado de pattern matching por substring em SQL padrão.

**Claim:** Remover o wildcard inicial (`'termo%'`) não resolve o problema de forma estrutural — apenas desloca o ponto de falha (ex.: `'Maria%'` ainda casa com "Mariana"; `'capa%'` ainda casa com "capacete").
**Evidência:** Testes ao vivo mostrando falha em múltiplos termos após a correção aparentemente funcionar para o primeiro caso testado ("Ana").
**Confiança:** Alta — consequência direta e demonstrável de continuar sendo matching por prefixo de string, não por fronteira de palavra.

**Claim:** `LIKE` não suporta busca composta robusta — `'%anel prata%'` não encontra o registro "anel solitário prata" porque a ordem exata das palavras no texto raramente coincide com a ordem digitada pelo usuário.
**Evidência:** Query executada ao vivo retornando zero resultados para o termo composto, contra o Mercado Livre retornando resultados corretos para a mesma busca.
**Confiança:** Alta.

**Claim:** `EXPLAIN ANALYZE` numa query com `LIKE '%termo%'` mostra table scan/Seq Scan sobre a tabela inteira (10.000 linhas, custo interno MySQL = 1028), independentemente da seletividade real do termo buscado.
**Evidência:** Plano de execução inspecionado ao vivo no MySQL e no PostgreSQL (`Seq Scan`), mesmo comportamento nos dois motores.
**Confiança:** Alta — consistente com [[wiki/concepts/database-index]] (seção Diagnóstico: `Seq Scan` = full table scan = falta de índice utilizável).

**Claim:** O custo de um table scan escala multiplicativamente entre tamanho da tabela e número de usuários concorrentes pesquisando ao mesmo tempo (10.000 linhas × N usuários simultâneos).
**Evidência:** Raciocínio aritmético apresentado (1 usuário = 10.000 comparações; 100 usuários = 1.000.000), sem benchmark de carga real medido.
**Confiança:** Média-alta — o mecanismo (cada conexão executa seu próprio scan independente) é correto, mas o número exato depende de concorrência de I/O e cache do banco, não é uma extrapolação linear garantida em todo hardware.

**Claim:** `FULLTEXT INDEX` no MySQL + `MATCH(colunas) AGAINST('termo')` substitui o `LIKE` com relevância ranqueada e custo de execução ordens de grandeza menor (0,35 vs. 1028; 419 linhas examinadas vs. 10.000).
**Evidência:** `CREATE FULLTEXT INDEX search_idx ON products (name, description)` seguido de `EXPLAIN ANALYZE` antes/depois, comparando os dois planos de execução lado a lado.
**Confiança:** Alta — reproduzido ao vivo com números concretos de antes/depois.

**Claim:** O Full-Text Search funciona internamente via tokenização (quebra em palavras, remoção de stop words) seguida da construção de um índice invertido (palavra → lista de IDs de registro onde ela ocorre); buscas compostas retornam a interseção dos IDs de cada termo.
**Evidência:** Explicação conceitual com exemplo simplificado de 10 registros e visualização da estrutura palavra→IDs no Miro.
**Confiança:** Alta — descrição correta do mecanismo padrão de índice invertido usado por motores de busca em geral (não é específico do MySQL). Ver [[wiki/concepts/indice-invertido]].

**Claim:** No PostgreSQL, `to_tsvector(idioma, texto) @@ to_tsquery(idioma, termo)` sem índice roda **mais lento** que o próprio `LIKE` (139ms vs. 4,9ms) porque o `tsvector` é recalculado em tempo de execução a cada linha/chamada.
**Evidência:** `EXPLAIN ANALYZE` comparando os dois tempos na ausência de índice `GIN`.
**Confiança:** Alta — reproduzido ao vivo; é a razão prática pela qual a fonte insiste que o índice `GIN` sobre a expressão `to_tsvector(...)` é obrigatório, não opcional, para produção.

**Claim:** Criar `CREATE INDEX ... USING GIN (to_tsvector(...))` derruba o tempo de 139ms para ~0,3–0,8ms e elimina o `Seq Scan` do plano de execução.
**Evidência:** `EXPLAIN ANALYZE` antes/depois da criação do índice GIN.
**Confiança:** Alta.

**Claim:** PostgreSQL reduz variações morfológicas da mesma palavra a um único **lexema** (stemming) — buscar "prata" ou "prateado" retorna o mesmo resultado, e "cadernos" (plural) encontra "caderno" (singular) sem a forma plural existir literalmente no texto.
**Evidência:** `SELECT to_tsvector('portuguese', 'programador programando programação programadores')` reduzindo as quatro formas a um único token; teste comparativo `anel & prata` vs. `anel & prateado` retornando o mesmo resultado.
**Confiança:** Alta — comportamento documentado do dicionário linguístico (`portuguese` snowball stemmer) do PostgreSQL; a fonte não expõe o nome técnico do algoritmo de stemming, apenas o efeito observável.

**Claim:** MySQL tem suporte a idioma/vocabulário "básico" comparado ao PostgreSQL — sem tesauros configuráveis nem stemming avançado, e sem retornar plural/singular de forma tão flexível.
**Evidência:** Comparação qualitativa em tabela apresentada na fonte, sem demonstração ao vivo equivalente à do Postgres (não há teste mostrando MySQL falhando em plural/singular).
**Confiança:** Média — é uma alegação plausível e consistente com a documentação pública de ambos os motores, mas não foi demonstrada empiricamente na fonte da mesma forma que os outros claims.

---

## Comparativo LIKE vs. Full-Text Search (MySQL e PostgreSQL)

| Recurso | LIKE | MySQL Full-Text | PostgreSQL Full-Text |
|---|---|---|---|
| Evita full table scan | Não | Sim | Sim |
| Busca por palavra, não substring | Não | Sim | Sim |
| Ranking de relevância | Não | Sim | Sim |
| Busca composta (múltiplas palavras) | Frágil | Sim | Sim |
| Stemming (plural/singular, mesma raiz) | Não | Limitado | Avançado |
| Tesauros/sinônimos configuráveis | Não | Não | Sim |
| Peso configurável por campo | Não | Não | Sim |

---

## Entidades e Conceitos

- [[wiki/concepts/full-text-search]] — novo, conceito central desta fonte
- [[wiki/concepts/indice-invertido]] — novo, a estrutura de dados por baixo do Full-Text Search
- [[wiki/concepts/mysql]] — `FULLTEXT INDEX` + `MATCH ... AGAINST`
- [[wiki/concepts/postgresql]] — `tsvector`/`tsquery` + índice `GIN`
- [[wiki/concepts/database-index]] — GIN como tipo de índice distinto do B-tree padrão
- [[wiki/entities/renato-augusto]] — autor
- [[wiki/entities/mercado-livre]] — usado como exemplo de motor de busca relevante em produção

## Ver também

- [[wiki/sources/elasticsearch-opensearch]] — o próximo degrau quando o Full-Text Search nativo do banco relacional não é mais suficiente (facets, >10M documentos, BM25)
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — mesma tese de fundo: entender o que o banco faz por baixo do SQL, em vez de tratá-lo como caixa-preta
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — "o operador usa o índice, o engenheiro sabe por que ele existe"; aqui o índice invertido é o exemplo concreto
- [[wiki/concepts/sql-alem-do-basico]] — Full-Text Search como sinal de domínio de SQL além do CRUD básico

---

## Perguntas Abertas

- A fonte não demonstra `pg_trgm`/similarity (fuzzy search, tolerância a erro de digitação) nem `ts_rank`/`setweight` (peso por campo) ao vivo — apenas cita a existência desses recursos avançados do lado do Postgres. Ver seção "Além da Fonte" em [[wiki/concepts/full-text-search]] para o que a skill `tech-mentor-data` acrescenta sobre isso.
- Não fica claro na fonte a partir de que volume de dados ou complexidade de relevância (facets, busca multi-idioma, autocomplete) o Full-Text Search nativo do PostgreSQL deixa de ser suficiente e migrar para Elasticsearch/OpenSearch passa a valer a pena — [[wiki/sources/elasticsearch-opensearch]] já documenta o critério ">10M documentos, relevância customizada, facets/aggregations complexas" como resposta parcial a essa pergunta.
- A alegação de que o suporte a idioma do MySQL é "básico" não foi demonstrada com um caso de falha ao vivo (só comparação em tabela) — vale verificar contra a documentação oficial do MySQL em algum ingest futuro.

---

## Citações

> "Esse é o problema disso aqui: a falta de relevância. Porque ele não tá pesquisando pelo nome, ele não entende idioma, ele não entende vocabulário."

> "Ao invés de procurar na tabela quando você roda uma query dessa com match against/full text search, ele tá procurando um índice — ele nunca mais tá olhando pra tabela."

> "Pensa assim: pega um livro aí aleatório e encontra a palavra 'cachorro' dentro desse livro... Full-Text Search é como se ele fosse direto na última página do livro, no índice remissivo, e visse: a palavra cachorro existe na página 5, 48, 210."

> "Esse é o super poder do Postgres que muito pouca gente conhece."
